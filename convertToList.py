import sys

def convertToList(filename):
    li = [i.strip().split() for i in open(filename).readlines()]
    l = [item for sublist in li for item in sublist]
    f = open(filename, 'w')
    f.write("\n".join(map(lambda x: str(x), l)))
    f.close()

def main(argv):
    convertToList(argv)

if __name__ == "__main__":
    main(sys.argv[1])