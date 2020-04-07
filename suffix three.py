a = int(input())
s = [[] for k in range(a)]
for k in range(a):
    s[k] = str(input())
fil = 'po'
jap = 'desu'
jap2 = 'masu'
kor = 'mnida'
def suffchang(x):
    x = list(x)
    x.reverse()
    return x
fil = suffchang(fil)
jap = suffchang(jap)
jap2 = suffchang(jap2)
kor = suffchang(kor)

for k in range (0,len(s)):
    b = suffchang(s[k])
    if b[0] == fil[0] and b[1] == fil[1]:
            print('FILIPINO')
    elif b[0] == jap[0] and b[1] == jap[1] and b[2] == jap[2] and b[3] == jap[3]:
            print('JAPANESE')
    elif b[0] == jap2[0] and b[1] == jap2[1] and b[2] == jap2[2] and b[3] == jap2[3]:
            print('JAPANESE')
    elif b[0] == kor[0] and b[1] == kor[1] and b[2] == kor[2] and b[3] == kor[3] and b[4] == kor[4]:
            print('KOREAN')


