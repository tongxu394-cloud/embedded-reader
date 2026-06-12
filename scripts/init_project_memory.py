#!/usr/bin/env python3
"""
Scaffold a per-project memory folder from the bundled template.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a project-memory folder from the embedded-project-reader template.",
    )
    parser.add_argument(
        "target_path",
        help="Repository or workspace path where the project-memory folder should be created.",
    )
    parser.add_argument(
        "--name",
        default="project-memory",
        help="Name of the generated folder. Defaults to project-memory.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace an existing generated folder.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    script_dir = Path(__file__).resolve().parent
    template_dir = script_dir.parent / "assets" / "project-template"
    target_root = Path(args.target_path).resolve()
    destination = target_root / args.name

    if not template_dir.is_dir():
        print(f"[ERROR] Template directory not found: {template_dir}")
        return 1

    if not target_root.exists():
        print(f"[ERROR] Target path not found: {target_root}")
        return 1

    if destination.exists():
        if not args.force:
            print(f"[ERROR] Destination already exists: {destination}")
            print("Use --force to replace it.")
            return 1
        shutil.rmtree(destination)

    shutil.copytree(template_dir, destination)
    print(f"[OK] Created project memory at: {destination}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
