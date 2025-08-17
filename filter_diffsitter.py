import re
import sys


def clean_diffsitter_output():
    lines = sys.stdin.readlines()
    buffer = []
    file_diff_started = False

    for i in range(len(lines)):
        line = lines[i]
        nextline = lines[i + 1] if i + 1 < len(lines) else ""

        if line.strip() == "":
            buffer.append("\n")
            continue

        if re.match(r'^===+$', line):
            continue

        if re.match(r'^===+$', nextline):
            filename = re.sub(r'^.*? -> ', '', line).strip()
            file_diff_started = True
            continue

        if file_diff_started:
            file_diff_started = False
            buffer.append(f"\nFILENAME: {filename}\n\n")
        buffer.append(line)

    sys.stdout.writelines(buffer)

if __name__ == "__main__":
    clean_diffsitter_output()