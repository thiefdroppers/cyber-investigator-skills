#!/usr/bin/env python3
"""Generate the mkdocs.yml nav block from the curriculum file tree.
Run after adding/renaming any day file, then paste the output into mkdocs.yml's nav: key
(everything this script prints, unchanged).
"""
import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
ROOT = REPO_ROOT / "docs"
CURRICULUM = ROOT / "curriculum"

PHASE_TITLES = {
    1: "Foundations",
    2: "OSINT & Digital Footprint",
    3: "Cyber Threat Intelligence",
    4: "Digital Forensics & Incident Investigation",
    5: "Fraud, Scam & Social-Engineering Investigation",
    6: "Cloud & AI-System Investigation",
    7: "Capstone & Career",
}


def title_of(md_path: Path) -> str:
    text = md_path.read_text(encoding="utf-8")
    m = re.search(r"^#\s+(.*)$", text, re.MULTILINE)
    return m.group(1).strip() if m else md_path.stem


def title_of_dir(phase_dir: Path) -> str:
    num = int(phase_dir.name.split("-")[1])
    return f"Phase {num}: {PHASE_TITLES[num]}"


def phase_dirs():
    return sorted(
        (p for p in CURRICULUM.iterdir() if p.is_dir() and p.name.startswith("phase-")),
        key=lambda p: int(p.name.split("-")[1]),
    )


def build_nav():
    nav = [
        {"Home": "README.md"},
        {"Contributing": "CONTRIBUTING.md"},
        {"Curriculum overview": "curriculum/README.md"},
    ]
    # Non-day pages at the top of curriculum/ (README.md is the overview above;
    # files starting with "_" such as _template.md are excluded from the site).
    for page in sorted(CURRICULUM.glob("*.md")):
        if page.name == "README.md" or page.name.startswith("_"):
            continue
        nav.append({title_of(page): f"curriculum/{page.name}"})
    for phase_dir in phase_dirs():
        rel = phase_dir.relative_to(ROOT)
        entries = []
        for day in sorted(phase_dir.glob("day-*.md")):
            entries.append({title_of(day): f"{rel}/{day.name}"})
        case_packet_index = phase_dir / "case-packet" / "README.md"
        if case_packet_index.exists():
            entries.append({"Capstone case packet": f"{rel}/case-packet/README.md"})
        nav.append({title_of_dir(phase_dir): entries})
    nav.append({"Worksheets": [
        {"Overview": "worksheets/README.md"},
        {"OSINT recon log": "worksheets/osint-recon-log.md"},
    ]})
    industry_entries = []
    industries_dir = ROOT / "ai-agent-skills" / "industries"
    if industries_dir.exists():
        for industry_dir in sorted(industries_dir.iterdir()):
            skill = industry_dir / "SKILL.md"
            if not skill.exists():
                continue
            entry = [{title_of(skill): f"ai-agent-skills/industries/{industry_dir.name}/SKILL.md"}]
            ref_dir = industry_dir / "reference"
            if ref_dir.exists():
                for ref in sorted(ref_dir.glob("*.md")):
                    entry.append({title_of(ref): f"ai-agent-skills/industries/{industry_dir.name}/reference/{ref.name}"})
            group_title = title_of(skill).split(": ", 1)[-1]
            group_title = group_title[0].upper() + group_title[1:]
            industry_entries.append({group_title: entry})

    nav.append({"AI Agent Skills": [
        {"Overview": "ai-agent-skills/SKILL.md"},
        {"Portable prompt": "ai-agent-skills/PORTABLE_PROMPT.md"},
        {"OSINT checklist": "ai-agent-skills/reference/osint-methodology-checklist.md"},
        {"Fraud pattern taxonomy": "ai-agent-skills/reference/fraud-pattern-taxonomy.md"},
        {"Industry skills": industry_entries},
    ]})
    return {"nav": nav}


def main():
    out = yaml.safe_dump(build_nav(), sort_keys=False, allow_unicode=True, width=1000)
    sys.stdout.write(out)


if __name__ == "__main__":
    main()
