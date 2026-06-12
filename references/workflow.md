# Workflow

## Intake

Start by inventorying the project artifacts.
List which files are available for schematics, datasheets, reference manuals, PCB exports, BOMs, pin tables, and existing firmware.

## Initialization

If the project has no memory folder yet, scaffold one with:

```powershell
python scripts/init_project_memory.py C:\path\to\repo
```

The script creates `project-memory/` under the target path by default.

## Extraction Order

Use this order unless the user gives a stronger source:

1. MCU datasheet and reference manual for official capabilities
2. Schematic and PCB export for board-specific wiring
3. Existing firmware or configuration files for current project assignments
4. BOM and module datasheets for external devices

## Population Order

Fill the project memory files in this sequence:

1. `project-manifest.md`
2. `chip-summary.md`
3. `pin-map.md`
4. `peripheral-map.md`
5. `board-notes.md`
6. `conflicts.md`
7. `open-questions.md`

This order keeps the core chip facts stable before assigning board-level conclusions.

## Ongoing Use

When the user asks a coding or debugging question:

1. Check whether the answer is already present in the project memory files.
2. If not, return to the source artifact and update the memory.
3. Answer with the verified conclusion and note any unresolved gaps.
