from __future__ import annotations

import argparse
import re
import os.path
from typing import Sequence



def check_decorator(src: bytes, filename: str = '<unknown>',missing_tag) -> int:
    file = src.readlines()
    missing_tag = missing_tag
    lastline = ""
    for line in file:
        if re.search("^class.*:$", line.decode("utf-8")):
            if (
                lastline == ""
                or ('funid_test' not in lastline )
            ):
                index = file.index(line)
                print(
                    f'{filename}:  missing tag "funid_test"'
                    f'(on line {index}).',
                )
                missing_tag = True
                break
        lastline = line.decode("utf-8")
        # print(lastline)
    return missing_tag


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)
    print(args.filenames)
    missing_tag = False
    for filename in args.filenames:
        base = os.path.basename(filename)
        if (
                re.match("^test.*py$", base) and
                base != '__init__.py' 
        ):
            with open(filename, 'rb') as f:
                 missing_tag = check_decorator(f, filename=filename,missing_tag)
    return missing_tag
