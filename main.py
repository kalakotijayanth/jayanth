rows  = int(input())
colunmns = int(input())
m =[]
for i in range(rows):


    a=[]
    for j in range(colunmns):
     a.append(int(input()))
    m.append(a)
for i in range(rows):
    for j in range(colunmns):
        print(m[i][j],end=" ")
    print("")
rows1  = int(input())
colunmns1 = int(input())
m1 =[]
for i in range(rows1):
    a1=[]
    for j in range(colunmns1):
     a1.append(int(input()))
    m1.append(a1)
for i in range(rows1):
    for j in range(colunmns1):
        print(m1[i][j],end=" ")
    print("")
res = []
print(len(m))
print(len(m[0]))
for i in range(len(m)):
    c=[]
    for j in range(len(m1[0])):
        x=0
        for k in range(len(m1)):

            x=x+(m[i][k] * m1[k][j])
        c.append(x)

    res.append(c)

for r in res:
    print(r)



