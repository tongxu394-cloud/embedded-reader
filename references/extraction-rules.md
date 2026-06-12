# Extraction Rules

## Hardware Fact Policy

Treat the following as hard facts that require source-backed confirmation:

- MCU package and exact part number
- Supply rails and voltage constraints
- Boot and reset strap pins
- Debug and programming pins
- GPIO numbers, package pin numbers, and net names
- Alternate functions and peripheral muxing
- Oscillator and clock source wiring

## Pin Accuracy Rules

- Record both the package pin number and the logical GPIO name when available.
- Distinguish between chip capability and board usage.
- When a pin has multiple alternate functions, record the currently used function and note important alternatives only when they affect conflicts.
- If a schematic net name disagrees with source code, mark the disagreement in `conflicts.md` instead of choosing one silently.

## Answering Rules

- Answer from `pin-map.md` and `peripheral-map.md` first once they exist.
- If those files are incomplete, return to the original sources before giving a definitive hardware answer.
- Do not infer a pin assignment from a similar board or another package variant.

## Memory Hygiene

- Keep extracted facts concise and structured.
- Preserve open questions instead of deleting them.
- Update the affected memory file whenever a new source invalidates an older conclusion.
