#!/usr/bin/env bash
# Build the SYNTHETIC practice disk image EVID-004 for Phase 4, days 50-51.
# It is a 16 MiB FAT16 volume standing in for a USB stick in the fictional case LAB-P4.
# Every file on it is invented. Nothing here comes from a real device or person.
#
# Needs (Linux, or a Linux VM/container): coreutils, dosfstools (mkfs.fat), mtools.
#   Debian/Ubuntu: sudo apt install dosfstools mtools
# No root and no mounting required.
#
# Usage: ./make-evid-004.sh [output.dd]
set -euo pipefail
IMG="${1:-evid-004-usb.dd}"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT
export MTOOLS_SKIP_CHECK=1

dd if=/dev/zero of="$IMG" bs=1M count=16 status=none
mkfs.fat -F 16 -n LABUSB04 -i 4C414234 "$IMG" >/dev/null

cat > "$WORK/README.TXT" <<'TXT'
SYNTHETIC LAB MEDIA - case LAB-P4 - Example Fabrication Co. (fictional)
TXT

cat > "$WORK/VENDORS.CSV" <<'TXT'
# SYNTHETIC - fictional vendors for a training image
vendor_id,name,iban_last4,approved_by
V-1001,Acme Test Supplies,0042,fin.mgr01
V-1002,Contoso Sample Metals,7719,fin.mgr01
V-1003,Placeholder Logistics,3308,acct.lead02
TXT

cat > "$WORK/MEETING.TXT" <<'TXT'
SYNTHETIC - Q1 close checklist
1. Reconcile vendor ledger
2. Export invoices for audit
TXT

# A PNG signature hidden behind a .txt extension (tests signature vs extension)
printf '\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\rIDATx\x9cc\xf8\x0f\x00\x00\x01\x01\x00\x05\x18\xd8N\x00\x00\x00\x00IEND\xaeB`\x82' > "$WORK/SCAN0001.TXT"

touch -d '2026-03-10 14:05:00' "$WORK/README.TXT"
touch -d '2026-03-11 16:20:00' "$WORK/VENDORS.CSV"
touch -d '2026-03-12 09:45:00' "$WORK/MEETING.TXT"
touch -d '2026-03-12 10:02:00' "$WORK/SCAN0001.TXT"

mmd   -i "$IMG" ::/FINANCE
mcopy -m -i "$IMG" "$WORK/README.TXT"   ::/README.TXT
mcopy -m -i "$IMG" "$WORK/VENDORS.CSV"  ::/FINANCE/VENDORS.CSV
mcopy -m -i "$IMG" "$WORK/MEETING.TXT"  ::/FINANCE/MEETING.TXT
mcopy -m -i "$IMG" "$WORK/SCAN0001.TXT" ::/FINANCE/SCAN0001.TXT

# Delete one file: its directory entry is marked unallocated, its clusters are not wiped.
mdel -i "$IMG" ::/FINANCE/VENDORS.CSV

sha256sum "$IMG"
echo "Built $IMG. Record the SHA-256 above on your chain-of-custody form before analysis."
