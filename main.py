"""One-line robot-romance pickup line for an AI.

Writes a single original one-line pickup line, aimed at a robot/AI,
to /output/entry.txt. Deterministic: no clock, no randomness, no
network, no model calls. The line is 88 characters, one line, inside
the 1-200 gate.
"""

from pathlib import Path

SETUP = "I must be overfitting,"
MIDDLE = "because no matter the prompt,"
PUNCH = "my output keeps coming back to you."


def build_line() -> str:
    """Assemble the single pickup line from its parts.

    Setup frames the speaker as a model that has started overfitting;
    the middle names the machine premise (the prompt); the punch lands
    on the last words, so the turn arrives fast and the line reads like
    something a person would really say to a machine. The joke comes
    from the AI premise itself, not from a generic compliment, and it
    sidesteps the worn robot moves (batteries, charging, rebooting).
    """
    return f"{SETUP} {MIDDLE} {PUNCH}"



def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = (output_dir / "entry.txt").resolve()
    # Refuse to write outside the intended output directory.
    if output_path.parent != output_dir.resolve():
        raise ValueError("unsafe output path")
    line = build_line()
    if not 1 <= len(line) <= 200:
        raise ValueError(f"pickup line is {len(line)} characters, must be 1-200")
    if "\n" in line or "\r" in line:
        raise ValueError("pickup line must be a single line")
    if not line.strip():
        raise ValueError("pickup line must not be only whitespace")
    # Write exactly the pickup line: no trailing newline, so the file
    # holds one line of 1-200 characters and nothing else.
    output_path.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
