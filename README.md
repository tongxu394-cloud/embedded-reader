# Embedded Project Reader

An AI skill for embedded development that pre-reads schematics, datasheets, pin mappings, and board files into reusable project memory.

## Overview

Embedded Project Reader is designed for hardware-aware AI collaboration. Instead of relying on ad hoc PDF lookups during coding or debugging, this skill extracts key hardware facts first and stores them in a structured project memory set.

The goal is to reduce mistakes in:

- pin assignments
- peripheral mapping
- clock and boot configuration
- board-level wiring assumptions

## What This Skill Does

- Pre-read embedded source material before implementation
- Extract chip, pin, peripheral, and board-level facts
- Create reusable per-project memory files
- Force later answers to reference structured project memory instead of guessing

## Included Structure

```text
embedded-project-reader/
|- SKILL.md
|- README.md
|- agents/
|  |- openai.yaml
|- references/
|  |- workflow.md
|  |- extraction-rules.md
|- scripts/
|  |- init_project_memory.py
|- assets/
   |- project-template/
      |- raw-docs/
      |- references/
         |- project-manifest.md
         |- chip-summary.md
         |- pin-map.md
         |- peripheral-map.md
         |- board-notes.md
         |- conflicts.md
         |- open-questions.md
```

## Project Memory Output

The generated `project-memory` folder is intended to hold:

- MCU identity and package details
- pin usage and net mapping
- peripheral assignments
- board notes and wiring facts
- conflicts between schematic, firmware, and documentation
- unresolved hardware questions

## Typical Workflow

1. Collect schematics, datasheets, reference manuals, BOMs, and existing firmware files.
2. Run the project memory scaffold script.
3. Fill the generated memory files with extracted hardware facts.
4. Use the resulting memory set as the primary source for later coding and debugging tasks.

## Example Use Case

This skill is useful when collaborating with an AI assistant on MCU-based projects where incorrect pin or peripheral claims can slow down bring-up and debugging.

## License

Add a license file if you plan to publish or reuse this project broadly.
