def space_leaver(space, data):
    length = len(str(data))
    return (space-length)

def styling_list(l):
    print("-"*109)
    for i in l:
        c = 1
        for j in i:
            if c == 1:
                print("| " + str(j), end=" "*space_leaver(5,j))
                print('| ', end="")
            elif c==2:
                print(j, end=" "*space_leaver(32,j))
                print(" | ", end='')
            elif c==3:
                print(j, end=" "*space_leaver(5,j))
                print(" | ", end='')
            elif c==4:
                print(j, end=" "*space_leaver(11,j))
                print(" | ", end='')
            elif c==5:
                print(j, end=" "*space_leaver(5,j))
                print(" | ", end='')
            elif c==6:
                print(j, end=" "*space_leaver(15,j))
                print(" | ", end='')
            else:
                print(j, end=" "*space_leaver(15,j))
                print(" | ", end='')
            c+=1
        if i == ["ID","MODEL","AGE","MAX RANGE","SEATS","PRICE","OPERATING COST"]:
            print()
            print("-"*109)
        else:
            print()
    print("-"*109)
