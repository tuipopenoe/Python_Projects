import difflib
import sys

def compareFiles(file1, file2):
    diff = difflib.ndiff(open(file1).readlines(), open(file2).readlines())

    try:
        while True:
            print diff.next()
    except:
        pass

def main(file1, file2):
    compareFiles(file1, file2)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])