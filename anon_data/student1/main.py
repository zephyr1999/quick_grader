# this is a test file that does hello world 3 times,
# essentially echoing back what was given to it 3 times.

import sys

def echoer():
    print("Enter something.")
    s = raw_input()
    print(s)

if __name__ == "__main__":
    echoer()
    echoer()
    echoer()
    sys.exit()
