
print ("\n\n\n","My Name is ","\n\n\n")
for ctrrow in range (5):
    for ctrcol in range(5):
        if ctrrow == 0:
            for ctr in range(6):
                if ctrcol == 3:
                    if ctr == 0 or ctr == 5:
                        print("*", end=" ")
                    else:
                        print(" ", end=" ")
                else:
                    print("*", end=" ")
            print("\t", end="  ")
    for ctrcol in range(5):
        if ctrrow == 2:
            for ctr in range(6):
                if ctrcol == 2:
                    if ctr == 3:
                        print("*", end=" ")
                    else:
                        print(" ", end=" ")
                if ctrcol == 3:
                    if ctr == 1 or ctr == 3 or ctr == 4:
                        print(" ", end=" ")
                    else:
                        print("*", end=" ")
                if ctrcol != 2 and ctrcol != 3:
                    print("*", end=" ")
            print("\t", end="  ")
    for ctrcol in range(5):
        if ctrrow != 0 and ctrrow != 2:
            for ctr in range(6):
                if ctrcol == 0 :
                    if ctr == 0:
                        print("*", end=" ")
                    else:
                        print(" ", end=" ")
                elif ctrcol == 2:
                    if ctr == 3:
                        print("*", end=" ")
                    else:
                        print(" ", end=" ")
                else:
                    if ctrrow == 1 and ctrcol == 3:
                        if ctr == 2 or ctr == 3:
                            print(" ", end=" ")
                        else:
                            print("*", end=" ")
                    else:
                        if ctr == 0 or ctr == 5:
                            print("*", end=" ")
                        else:
                            print(" ", end=" ")
            print("\t", end="  ")
    print("\n")




