L = [ ['田中', 35] ,['山下', 69], ['中村', 21], ['村上', 12], ['江口', 46] ]

name_age = sorted(L,key = lambda x : x[1])
for i in name_age: print(i)
