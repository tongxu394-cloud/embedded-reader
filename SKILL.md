---
name: embedded-project-reader
description: Pre-read embedded project source material and turn it into reusable project memory before coding or hardware debugging. Use when Codex needs to work from MCU datasheets, reference manuals, schematics, PCB exports, pin tables, BOMs, board headers, CubeMX or IOC files, or existing board support code and must avoid incorrect pin, peripheral, clock, or board-level assumptions.
---

# Embedded Project Reader

## Overview

Build a verified project memory set before making implementation or debugging claims.
Treat pin names, alternate functions, power domains, and board wiring as facts that must be extracted from project artifacts, not guessed from memory.

## Workflow

1. Locate or create the project memory folder.
   If the repository does not already contain one, run `python scripts/init_project_memory.py <target-path>` from this skill directory to scaffold a fresh memory set.

2. Collect the authoritative inputs.
   Prioritize schematics, MCU datasheets, reference manuals, PCB exports, BOMs, pin tables, board headers, and existing board code.

3. Read enough of each source to extract hardware facts.
   Do not rely on partial skims when answering questions about pins, clocks, boot straps, reset behavior, or peripheral muxing.

4. Populate the project memory files.
   Follow [workflow.md](references/workflow.md) and [extraction-rules.md](references/extraction-rules.md) when filling the template files in `project-memory/references/`.

5. Answer from project memory first.
   For later implementation or debugging tasks, consult the generated `pin-map.md`, `peripheral-map.md`, `board-notes.md`, and `conflicts.md` before making hardware claims.

6. Escalate uncertainty instead of guessing.
   If the source material conflicts or a fact is missing, record it in `open-questions.md` or `conflicts.md` and state that the answer is unresolved.

## Expected Outputs

Create or maintain these files inside each project memory folder:

- `references/project-manifest.md`
- `references/chip-summary.md`
- `references/pin-map.md`
- `references/peripheral-map.md`
- `references/board-notes.md`
- `references/conflicts.md`
- `references/open-questions.md`

## Resources

- `scripts/init_project_memory.py`: scaffold a new project memory folder from the bundled template
- [workflow.md](references/workflow.md): operational flow for pre-reading and updating memory
- [extraction-rules.md](references/extraction-rules.md): rules for pin accuracy, conflicts, and source handling
- `assets/project-template/`: starter files for a per-project memory set
