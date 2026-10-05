#!/usr/bin/env python3
"""Build or serve the docs site, even where git symlinks were not preserved.

docs/ is made of symlinks to the content at the repo root. On Windows without
Developer Mode, with core.symlinks=false, or from a ZIP download, each symlink
checks out as a small text file holding its target path (e.g. "../README.md"),
and MkDocs fails with missing nav pages or a FileNotFoundError.

If the symlinks are intact, this script just runs MkDocs. If they are stubs, it
copies the real content into .docs-build/ and runs MkDocs against that copy,
leaving the working tree untouched.

Usage:
    python scripts/build_docs.py serve      # local preview at http://127.0.0.1:8000
    python scripts/build_docs.py build      # static site in site/
Extra arguments are passed through to MkDocs (e.g. build --strict).
"""
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS = REPO_ROOT / "docs"
STAGE = REPO_ROOT / ".docs-build"
STUB_MAX_BYTES = 256


def stub_target(entry: Path):
    """Return the target path if entry is a symlink checked out as a text stub."""
    if entry.is_symlink() or not entry.is_file():
        return None
    if entry.stat().st_size > STUB_MAX_BYTES:
        return None
    try:
        text = entry.read_text(encoding="utf-8").strip()
    except UnicodeDecodeError:
        return None
    if not text or "\n" in text:
        return None
    target = (entry.parent / text).resolve()
    return target if target.exists() else None


def stage_docs() -> Path:
    """Copy docs/ into .docs-build/docs/ with stubs replaced by real content."""
    if STAGE.exists():
        shutil.rmtree(STAGE)
    staged_docs = STAGE / "docs"
    staged_docs.mkdir(parents=True)
    for entry in DOCS.iterdir():
        source = stub_target(entry) or entry
        dest = staged_docs / entry.name
        if source.is_dir():
            shutil.copytree(source, dest)
        else:
            shutil.copy2(source, dest)
    config = STAGE / "mkdocs.yml"
    config.write_text(
        "INHERIT: ../mkdocs.yml\ndocs_dir: docs\nsite_dir: ../site\n",
        encoding="utf-8",
    )
    return config


def main() -> int:
    command = sys.argv[1] if len(sys.argv) > 1 else "serve"
    if command not in ("serve", "build"):
        print(__doc__)
        return 2

    if any(stub_target(entry) for entry in DOCS.iterdir()):
        print("docs/ symlinks were checked out as plain files; staging real copies in .docs-build/")
        if command == "serve":
            print("Note: edits to the original files need a restart of this script to show up.")
        config = stage_docs()
    else:
        config = REPO_ROOT / "mkdocs.yml"

    mkdocs = [sys.executable, "-m", "mkdocs", command, "-f", str(config), *sys.argv[2:]]
    return subprocess.call(mkdocs, cwd=REPO_ROOT)


if __name__ == "__main__":
    sys.exit(main())
