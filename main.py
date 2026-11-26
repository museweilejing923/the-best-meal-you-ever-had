#!/usr/bin/env python3
"""The Best Meal You Ever Had: one sentence, one specific memory.

Not a banquet and not a restaurant review.
A bowl of noodles on a platform at 2 a.m., while the train leaves.
The train did not wait, and neither did the noodles.
"""

import sys

# The entry never changes: it is the whole submission, fixed in advance.
# Every check below exists only to prove this one sentence is well
# formed before it is written out. Nothing here reads input, touches
# the network, rolls dice, or looks at the clock.
ENTRY = 'The best meal I ever had was a 2 a.m. bowl of instant noodles on a train platform, eaten with plastic chopsticks while my train pulled away without me.'
LIMIT = 200
TARGET = "/output/entry.txt"
EMDASH = "\u2014"
MIN_LETTERS = 1


def fail(reason):
    """Report a failed rule on stderr and stop with exit code 1."""
    print(f"rejected: {reason}", file=sys.stderr)
    raise SystemExit(1)


def check_about_meal(text):
    """True when the sentence is about a meal."""
    return text.lower().find("meal") != -1


def check_ends_full_stop(text):
    """True when the line ends with a full stop."""
    return text.rstrip()[-1:] == "."


def check_nonempty(text):
    """True when trimming the entry leaves something behind."""
    return len(text.strip()) > 0


def check_plain_sentence(text):
    """True when no exclamation or question mark appears."""
    return text.find("!") == -1 and text.find("?") == -1


def check_length_ok(text):
    """True when the entry fits inside the character limit."""
    return len(text) <= LIMIT


def check_no_filler_very(text):
    """True when the filler word very is nowhere in the sentence."""
    return text.lower().find("very") == -1


def check_letters_present(text):
    """True when the entry holds at least MIN_LETTERS letters."""
    found = sum(1 for ch in text if ch.isalpha())
    return found >= MIN_LETTERS


def check_printable(text):
    """True when every character is printable, none a control code."""
    return all(32 <= ord(ch) <= 126 or ord(ch) > 126 for ch in text)


def check_trimmed(text):
    """True when no leading or trailing space survives."""
    return text.strip() == text


def check_clean_spacing(text):
    """True when no double space or newline hides inside the entry."""
    return text.find("  ") == -1 and text.find("\n") == -1


# Each row is a short name, the check that must hold, and the complaint
# printed when it does not. The order below is the order the checks run.
RULES = [
    ("about_meal", check_about_meal, "entry must be about a meal"),
    ("ends_full_stop", check_ends_full_stop, "entry must end with a full stop"),
    ("nonempty", check_nonempty, "entry is empty"),
    ("plain_sentence", check_plain_sentence, "entry must be one plain sentence"),
    ("length_ok", check_length_ok, "entry is longer than the limit"),
    ("no_filler_very", check_no_filler_very, "entry must not contain the word very"),
    ("letters_present", check_letters_present, "entry has no letters"),
    ("printable", check_printable, "entry has control characters"),
    ("trimmed", check_trimmed, "entry has leading or trailing space"),
    ("clean_spacing", check_clean_spacing, "entry has ragged spacing"),
]


def validate(text):
    """Walk RULES top to bottom; the first failed check stops the run."""
    for index, (slug, check, message) in enumerate(RULES):
        try:
            ok = check(text)
        except Exception:
            ok = False
        if not ok:
            fail(f"rule {index + 1} [{slug}]: {message}")


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
