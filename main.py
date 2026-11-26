#!/usr/bin/env python3
"""The Best Meal You Ever Had: one sentence, one specific memory.
Not a banquet and not a restaurant review.
A bowl of noodles on a platform at 2 a.m., while the train leaves.
"""

import sys

ENTRY = 'The best meal I ever had was a 2 a.m. bowl of instant noodles on a train platform, eaten with plastic chopsticks while my train pulled away without me.'
LIMIT = 200
TARGET = "/output/entry.txt"
EMDASH = "\u2014"


def fail(reason):
    """Report a failed rule on stderr and stop with exit code 1."""
    print(f"rejected: {reason}", file=sys.stderr)
    raise SystemExit(1)


def guard_about_meal(text):
    """Check that the sentence is about a meal."""
    return "meal" in text.lower()


def guard_ends_full_stop(text):
    """Check that the line ends with a full stop."""
    return text.rstrip().endswith(".")


def guard_not_blank(text):
    """Check that the text is not empty after trimming."""
    return bool(text.strip())


def guard_plain_sentence(text):
    """Check that no exclamation or question mark appears."""
    return "!" not in text and "?" not in text


def guard_within_limit(text):
    """Check that the text fits inside the character limit."""
    return len(text) <= LIMIT


def guard_no_filler_very(text):
    """Check that the filler word very is nowhere in the sentence."""
    return "very" not in text.lower()


def guard_has_letters(text):
    """Check that at least one letter is present."""
    return any(ch.isalpha() for ch in text)


def guard_no_control(text):
    """Check that no character is a control character."""
    return all(ord(ch) >= 32 for ch in text)


def guard_no_edge_space(text):
    """Check that no leading or trailing space survives."""
    return text == text.strip()


def guard_no_ragged_spacing(text):
    """Check that no double space or newline hides inside."""
    return "  " not in text and "\n" not in text


RULES = [
    ("about_meal", guard_about_meal, "entry must be about a meal"),
    ("ends_full_stop", guard_ends_full_stop, "entry must end with a full stop"),
    ("not_blank", guard_not_blank, "entry is empty"),
    ("plain_sentence", guard_plain_sentence, "entry must be one plain sentence"),
    ("within_limit", guard_within_limit, "entry is longer than the limit"),
    ("no_filler_very", guard_no_filler_very, "entry must not contain the word very"),
    ("has_letters", guard_has_letters, "entry has no letters"),
    ("no_control", guard_no_control, "entry has control characters"),
    ("no_edge_space", guard_no_edge_space, "entry has leading or trailing space"),
    ("no_ragged_spacing", guard_no_ragged_spacing, "entry has ragged spacing"),
]


def validate(text):
    """Run every rule in RULES order; the first failure stops the run."""
    for slug, guard, message in RULES:
        try:
            passed = guard(text)
        except Exception:
            passed = False
        if not passed:
            fail(f"{slug}: {message}")


def emit(text):
    """Write the validated entry plus a trailing newline to TARGET."""
    with open(TARGET, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")


def main():
    """Validate the fixed entry, then emit it."""
    validate(ENTRY)
    emit(ENTRY)


if __name__ == "__main__":
    main()
