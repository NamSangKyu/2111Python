nation = ['그리스','아테네','독일','베를린','러시아','모스크바','미국','워싱턴']

file = open('nation.txt','wt')

for i in range(0,len(nation),2):
    file.write(nation[i] + "-" + nation[i+1]+"\n")

file.close()