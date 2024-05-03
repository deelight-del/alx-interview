#!/usr/bin/python3
"""In this module we parse some logfile
from the input stream to a desired output"""


import fileinput
import re
import sys
import signal


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

    def signal_handler(_, __):
        """Define signal handler of CTRL+C"""
        print("File size: {}".format(total_size))
        [
            print("{:d}: {}".format(k, resp_dict[k]))
            if resp_dict.get(k) > 0 else ""
            for k in sorted(list(resp_dict.keys()))
        ]

    # Register the signal
    signal.signal(signal.SIGINT, signal_handler)

    for line in fileinput.input():
        pattern1 = r"^(?:(?:(?:\d){1,3}\.){3}(?:\d{1,3})|\S+)\s?\-\s?"
        pattern2 = r"\[\d{4}\-\d{2}\-\d{2}\s(?:\d{2}\:){2}\d\d\.\d{6}\]\s"
        pattern3 = r"\"GET\s\/projects\/260\sHTTP\/1\.1\"\s"
        pattern4 = r"(200|301|400|401|403|404|405|500|\S*)?\s"
        pattern5 = r"([1-9][0-9]{0,2}[0-4]{0,1})"
        pattern = pattern1 + pattern2 + pattern3 + pattern4 + pattern5
        match = re.search(pattern, line)
        if not match:
            continue
            # loop_count += 1
            # if loop_count % 10 == 0:
            #    signal_handler()
        # if match:
        #    print(line)
        # else:
        #    print("No match", line)
        resp_code, file_size = match.group(1, 2)
        total_size += int(file_size)
        # Check if resp code is an int and if not, simulate an arbitray
        # integer.
        if not resp_code.isdigit():
            resp_code = 50005  # Invalid.
        # Check if resp_code is valid among the available keys
        if resp_dict.get(int(resp_code)) is not None:
            resp_dict[int(resp_code)] += 1
        loop_count += 1
        if loop_count % 10 == 0:
            print("File size: {}".format(total_size))
            [
                print("{:d}: {}".format(k, resp_dict[k]))
                if resp_dict.get(k) > 0 else ""
                for k in sorted(resp_dict.keys())
            ]
    # Printing result at end of line too
    signal_handler("_", "__")
