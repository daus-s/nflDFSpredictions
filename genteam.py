import parse


parse.parse()

col = parse.col

salary = col.index('Salary')
name = col.index('Name')
position = col.index('Position')
points = col.index("AvgPointsPerGame")

roster = ["qb","rb","rb","wr","wr","wr","te","flex","dst"]

max_score = 0.0

def calc_score(lst):
    score = 0.0
    for elem in lst:
        score += float(elem[points])
    return score

def calc_salary(lst):
    score = 0.0
    for elem in lst:
        score += float(elem[salary])
    return score


def gen():
    sal_value = 0
    max_score = 0
    max_roster = ["qb","rb","rb","wr","wr","wr","te","flex","dst"]

    #qb loop
    for qb in parse.qbs:
        roster[0] = qb
        for rb1 in parse.rbs:
            roster[1] = rb1
            for rb2 in parse.rbs:
                roster[2] = rb2
                if rb2 != rb1: #check rb positions
                    for wr1 in parse.wr:
                        roster[3] = wr1
                        for wr2 in parse.wr:
                            roster[4] = wr2
                            for wr3 in parse.wr:
                                roster[5] = wr3
                                if not (wr1 == wr2) and not (wr2 == wr3) and not (wr1 == wr3): #check wr positions 
                                    for te in parse.te:
                                        roster[6] = te
                                        for flex in parse.flex:
                                            if not flex in [rb1, rb2, wr1, wr2, wr3, te]:
                                                roster[7] = flex
                                                for dst in parse.dst:
                                                    roster[8] = dst

                                                    score = calc_score(roster)
                                                    #we have checked all same player constraints
                                                    #we now must check salaryy constraint
                                                    #print (roster)
                                                    if calc_salary(roster) <= 50000:
                                                        #now check if the score is the new high score
                                                        if score > max_score:
                                                            max_score = score
                                                            for i in range (0,9):
                                                                max_roster[i] = roster[i]
                                                            print(max_roster)
        return (max_roster)
                                            



def print_roster(roster):
    for player in roster:
        print(str(player[position]) + ": " + str(player[name]))


def main():
    data = gen()
    print_roster(data)
    print ("salary: " + str(calc_salary(data)))
    print ("points: " + str(calc_score(data)))


if __name__ == '__main__':
    main()