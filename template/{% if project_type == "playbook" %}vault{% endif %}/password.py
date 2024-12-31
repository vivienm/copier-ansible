#!/usr/bin/env -S uv run python

import argparse
import os
import secrets
import subprocess
import sys
from pathlib import Path
from typing import Iterable

CI = os.environ.get("CI", "0") != "0"

SCRIPT_DIR = Path(__file__).parent.relative_to(Path.cwd())
PASSWORD_PATH = SCRIPT_DIR / "password.asc"


def init_password(recipients: Iterable[str]) -> None:
    """Create a new password file."""
    if PASSWORD_PATH.exists():
        print(f"Password file already exists: {PASSWORD_PATH}", file=sys.stderr)
        sys.exit(1)
    password = secrets.token_hex()
    command = ["gpg", "--encrypt", "--armor", "--output", str(PASSWORD_PATH)]
    for recipient in recipients:
        command.extend(["--recipient", recipient])
    try:
        subprocess.run(command, input=password, text=True, check=True)
    except subprocess.CalledProcessError as e:
        print(e, file=sys.stderr)
        sys.exit(e.returncode)


def get_password(dummy: bool) -> str:
    """Return the password from the password file."""
    if dummy:
        return "dummy"

    if not PASSWORD_PATH.exists():
        print(f"Password file does not exist: {PASSWORD_PATH}", file=sys.stderr)
        print(f"Run `{sys.argv[0]} --init` to create it.", file=sys.stderr)
        sys.exit(1)

    try:
        proc = subprocess.run(
            ["gpg", "--quiet", "--decrypt", str(PASSWORD_PATH)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(e.stderr, end="", file=sys.stderr)
        print(e, file=sys.stderr)
        sys.exit(e.returncode)
    return proc.stdout.rstrip()


def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Vault password script")
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--init",
        nargs="*",
        metavar="RECIPIENT",
        help="initialize the password file for the given recipients",
    )
    group.add_argument(
        "--dummy",
        action="store_true",
        help="return a dummy password",
        default=CI,
    )
    args = parser.parse_args()
    if args.init is not None:
        init_password(args.init)
    else:
        password = get_password(dummy=args.dummy)
        print(password)


if __name__ == "__main__":
    main()
