import re

def extract_email(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return None


def extract_phone(text):
    """
    Extract the first phone number found in the resume.
    """

    pattern = r"(\+?\d[\d\s\-()]{7,}\d)"

    match = re.search(pattern, text)

    if match:
        return match.group().strip()

    return None

def extract_name(text):
    """
    Extract the candidate's name from the beginning of the resume.
    """

    lines = text.split("\n")

    for line in lines:
        line = line.strip()

        if line:
            return line

    return None