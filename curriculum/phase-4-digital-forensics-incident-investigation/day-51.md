# Day 51: File system forensics with The Sleuth Kit

Phase 4, digital forensics and incident investigation. Track goal: read a disk image below the file level, recover a deleted file with its metadata, and turn file system timestamps into a timeline.

## Concept

A file system has two layers you care about. Content is the clusters or blocks holding file data. Metadata is the record that says which clusters belong to which file, plus names and timestamps: the directory entry and FAT on FAT volumes, the inode on ext4, the MFT record on NTFS (day 52).

Deleting a file usually changes only metadata. On FAT, the first byte of the directory entry becomes `0xE5` and the file's chain in the File Allocation Table is zeroed, but the clusters keep their bytes until something else is written there. That is why deleted files are recoverable, and why recovery gets less likely the longer a device stays in use. On ext4 the inode's extent information is usually wiped on delete, so the same trick often fails there, and you fall back on carving (searching raw bytes for file signatures).

Timestamps come in sets. The shorthand is MACB: Modified (content), Accessed, Changed (metadata record changed; on NTFS and ext4), Born (created). FAT stores created, modified and last-access date (date only, no time, for access), in local time with no time zone. An investigator who reads FAT times as UTC is wrong by the device's offset.

The Sleuth Kit (TSK) is a set of command-line tools named by layer: `mm*` for partitions (media management), `fs*` for the file system, `f*` for file names, `i*` for metadata, `blk*` for data units. Autopsy is its GUI.

## Resources

- [The Sleuth Kit](https://www.sleuthkit.org/sleuthkit/) and its [man pages](https://www.sleuthkit.org/sleuthkit/man/) (`fls`, `istat`, `icat`, `mactime`).
- [Autopsy](https://www.autopsy.com/), free GUI on top of TSK.
- Brian Carrier, *File System Forensic Analysis* (Addison-Wesley, 2005): still the reference for FAT, NTFS and ext structures.
- [Body file format](https://wiki.sleuthkit.org/index.php?title=Body_file) on the TSK wiki.

## Practical: The Sleuth Kit on EVID-004, ending in a mactime timeline

Install on Debian/Ubuntu with `sudo apt install sleuthkit`. Use your verified working image from day 50, `~/lab-p4/work/evid-004.raw`. Everything below only reads the image.

1. Check for a partition table.

   ```bash
   mmls ~/lab-p4/work/evid-004.raw
   ```

   The builder script formatted the whole image as one volume with no partition table, so `mmls` reports that it cannot determine the partition type. Real USB sticks usually have an MBR and `mmls` would print a table like:

   ```text
   (illustrative, not from EVID-004)
         Slot      Start        End          Length       Description
   000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
   001:  -------   0000000000   0000002047   0000002048   Unallocated
   002:  000:000   0000002048   0030310399   0030308352   Win95 FAT32 (0x0c)
   ```

   In that case you pass the start sector to every later tool with `-o 2048`. For EVID-004 the offset is 0 and you can omit `-o`.

2. Describe the file system.

   ```bash
   fsstat ~/lab-p4/work/evid-004.raw | head -30
   ```

   Record the file system type (FAT16), volume label (`LABUSB04`), volume ID (`0x4c414234`, set by the builder), sector size and cluster size. These go in your notes as identifiers for the image.

3. List every name, including deleted ones.

   ```bash
   fls -r -p ~/lab-p4/work/evid-004.raw
   ```

   Each line reads `type/type inode: path`. A `*` before the inode number marks a deleted entry. You should see `FINANCE/VENDORS.CSV` flagged with `*`. Show only deleted entries with `fls -r -d -p`.

4. Read the deleted file's metadata, then its content.

   ```bash
   istat ~/lab-p4/work/evid-004.raw <inode-of-VENDORS.CSV>
   icat -r ~/lab-p4/work/evid-004.raw <inode-of-VENDORS.CSV> > ~/lab-p4/work/recovered_VENDORS.CSV
   sha256sum ~/lab-p4/work/recovered_VENDORS.CSV
   cat ~/lab-p4/work/recovered_VENDORS.CSV
   ```

   `istat` shows "Not Allocated", the written, accessed and created times, the size, and the sector list. `icat -r` asks TSK to attempt recovery of a deleted file. You should get the synthetic vendor table back with its header line intact. Note in your log that FAT recovery of a small, contiguous file is reliable; a fragmented deleted file on FAT is not, because the cluster chain is gone.

5. Check signatures against extensions.

   ```bash
   tsk_recover -e ~/lab-p4/work/evid-004.raw ~/lab-p4/work/export/
   file ~/lab-p4/work/export/FINANCE/*
   ```

   `tsk_recover -e` exports allocated and unallocated files. `file` reads magic bytes, so `SCAN0001.TXT` reports as `PNG image data, 1 x 1` despite its `.TXT` name. A renamed extension is weak evidence of intent on its own; it goes in the timeline as an observation, not a conclusion.

6. Build the timeline. `fls -m` writes a body file (one line per timestamp source); `mactime` sorts it.

   ```bash
   timedatectl | grep "Time zone"      # the zone the builder VM wrote FAT times in
   fls -r -m "EVID-004:" -z UTC ~/lab-p4/work/evid-004.raw > ~/lab-p4/work/evid-004.body
   mactime -b ~/lab-p4/work/evid-004.body -d -y -z UTC > ~/lab-p4/work/evid-004-timeline.csv
   ```

   On `fls`, `-z` tells TSK which zone the original machine used when it wrote FAT times; replace `UTC` with whatever `timedatectl` printed if your VM is not on UTC. On `mactime`, `-z` sets the zone used for display, `-d` gives comma-separated output, and `-y` puts the year first. Get the `fls -z` value wrong and every FAT time in the timeline shifts by the offset, silently. The output columns are Date, Size, Type (the `macb` flags), Mode, UID, GID, Meta, File Name. Rows for deleted files have `(deleted)` after the name.

7. Open the CSV in LibreOffice Calc or Timeline Explorer, keep only 2026 rows, and add two columns of your own: `observation` (what happened, in words) and `evidence_ref` (inode number). Colour the deleted-file rows.

Artifact: `evid-004-timeline.csv` annotated with your two columns, the recovered `VENDORS.CSV` with its SHA-256, and a one-paragraph note on how time zones were handled.

## Checkpoint

- Your timeline contains the creation of `FINANCE`, all four file writes, and at least one `(deleted)` row for `VENDORS.CSV`.
- The recovered file's hash is written in your notes next to its inode number, and it opens as a readable CSV.
- You can state, without looking, the difference between what `fls -d` shows and what `icat -r` does.
- Your note says what time zone the FAT timestamps are in and how you would find the real offset for a physical device (the owner's workstation settings, or a file with a known UTC event time).
