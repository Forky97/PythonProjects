from collections import deque
d = deque()
dct = {}

for _ in range(int(input())):
    row = input().replace(':', '').split()
    dct[row[0]] = []
    for i in range(1, len(row)):
        dct[row[0]].append(row[i])

for _ in range(int(input())):
    searched = []
    classes = input().split()
    if len(classes) > 1:
        if classes[0] == classes[1] and classes[0] in dct:
            print('Yes')
        elif classes[1] in dct:
            if len(dct[classes[1]]) == 0:
                if classes[0] == classes[1]:
                    print('Yes')
                else:
                    print('No')
            else:
                d += dct[classes[1]]
                while d:
                    left_neigh = d.popleft()
                    if left_neigh == classes[0]:
                        print('Yes')
                        d = deque()
                        break
                    else:
                        if left_neigh not in searched:
                            if left_neigh in dct:
                                d += dct[left_neigh]
                                searched.append(left_neigh)

                else:
                    print('No')
        else:
            if classes[0] == classes[1] and classes[0] in dct:
                print('Yes')
            else:
                print('No')
    else:
        print('Yes' if classes[0] in dct else 'No')