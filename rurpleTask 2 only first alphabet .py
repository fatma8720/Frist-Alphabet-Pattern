print ("\n\n\n")
nv = 18
nh = 3
for ctr0 in range (2):
    if ctr0==1:
       nv=12
    for ctr in range(nh):
        for ctr2 in range(nv):
            print("*", end=" ")
        print("\n")
    if ctr0==1:
       nh=5
    for ctr in range(nh):
        for ctr2 in range(4):
            print("*", end=" ")
        print("\n")
