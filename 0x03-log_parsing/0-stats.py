#!/usr/bin/python3
"""In this module we parse some logfile
from the input stream to a desired output"""


import fileinput
import re
import sys


if __name__ == "__main__":
    total_size = 0
    resp_dict = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }
    loop_count = 0
    for line in fileinput.input():
        pattern1 = r"^(?:(?:\d){1,3}\.){3}(?:\d{1,3})\s\-\s"
        pattern2 = r"\[\d{4}\-\d{2}\-\d{2}\s(?:\d{2}\:){2}\d\d\.\d{6}\]\s"
        pattern3 = r"\"GET\s\/projects\/260\sHTTP\/1\.1\"\s"
        pattern4 = r"(200|301|400|401|403|404|405|500)\s(1?[0-9]?[0-9]?[0-4]?){1}"
        pattern = pattern1 + pattern2 + pattern3 + pattern4
        match = re.search(pattern, line)
        # if match:
        #    print(line)
        # else:
        #    print("No match", line)
        resp_code, file_size = match.group(1, 2)
        total_size += int(file_size)
        if resp_dict.get(int(resp_code)) is not None:
            resp_dict[int(resp_code)] += 1
        loop_count += 1
        if loop_count % 10 == 0:
            print("File size: {}".format(total_size))
            [
                print("{}: {}".format(k, resp_dict[k]))
                if resp_dict.get(k) > 0 else ""
                for k in sorted(resp_dict.keys(), reverse=True)
            ]

