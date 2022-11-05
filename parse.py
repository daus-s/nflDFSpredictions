import csv

col = []
qbs = []
rbs = []
wr = []
te = []
flex = []
dst = []

filename = "DKSalaries.csv"

def parse(): 
    reader = csv.reader(open(filename, mode='r'))
    for line in reader:
        if line[0] == "Position":
            for i in line:
                col.append(i)
        if line[0] == "QB":
            qbs.append(line)
        if line[0] == "RB":
            rbs.append(line)
            flex.append(line)
        if line[0] == "WR":
            wr.append(line)
            flex.append(line)
        if line[0] == "TE":
            te.append(line)
            flex.append(line)
        if line[0] == "DST":
            dst.append(line)


    
def print_lists():
    print(qbs)
    print(rbs)
    print(wr)
    print(te)
    print(dst)


def print_len():
    print ("561=" + str(len(qbs)+ len(rbs)+ len(wr) + len(te)+ len(dst)))

def main():
    parse()
    print_lists()
    #print_len()
    print("col:" + str( col))


#for testing
if __name__ == "__main__":
    main()