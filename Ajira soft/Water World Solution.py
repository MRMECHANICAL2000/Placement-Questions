n=int(input())
cluster={}
links=[]
final_links=[]
total_water=0
for _ in range(int(input())):
    x=[]
    a,b,c=[i for i in input().split(" ")]
    #print(a,b,c)
    #x=[a,int(b),int(c),int(int(c)/int(b)),1]
    x=[a,int(b),int(c),int(int(c)/int(b)),1,int(c)]
    cluster[x[0]]=x[1:]

for _ in range(int(input())):
    links.append(list(map(str,input().split("_"))))
links.sort(reverse=True)
#print(cluster,links)
check=0
for i in range(len(links)-1,0,-1):
    check=0
    for j in range(0,i):
        #print(i,j)
        if links[j][-1]==links[i][0]:
            links[j].pop()
            links[j].extend(links[i])
            check=1
            break

    if check==0 and (links[i] not in final_links ):
        final_links.append(links[i])
    #print(check,final_links)
final_links.append(links[0])
#print(final_links)

"""
#This solution solves only 12 test cases
for i in range(len(final_links)):
	x=final_links[i][1:]
	x=x[::-1]
	for k in range(len(x)):
		j=x[k]
		if cluster[j][2]*cluster[j][3]>=n:
			total_water+=cluster[j][1]*cluster[j][3]
		else:
			'''aa=1
			while True:
				if int((cluster[j][1]*(cluster[j][3]+aa))/cluster[j][0])>=n:
					how_much_low=aa
					break
				aa+=1'''
			how_much_low=n-cluster[j][2]*cluster[j][3]
			for _ in range(k,len(x)):
				l=x[_]
				cluster[l][3]+=how_much_low
				#cluster[l][1]*=cluster[l][3]
				#print(cluster[l])
			total_water+=cluster[j][1]*cluster[j][3]
		#print(total_water)
print(total_water)"""

#this solution solves all 14 test cases
for i in range(len(final_links)):
	x=final_links[i][1:]
	x=x[::-1]
	for k in range(len(x)):
		j=x[k]
		total_water+=cluster[j][1]

for _ in range(n):
	#print(_,cluster,total_water)
	for i in range(len(final_links)):
		x=final_links[i][1:]
		x=x[::-1]
		for k in range(len(x)):
			j=x[k]

			if cluster[j][4]-cluster[j][0]>=0:
				cluster[j][4]-=cluster[j][0]
				continue

			else:
				#print(cluster[j][0],cluster[j][1],cluster[j][4],cluster[j][4]-cluster[j][0])
				for xyz in range(k,len(x)):
					jj=x[xyz]
					#print(k,total_water,cluster[jj][1],)
					total_water+=cluster[jj][1]
					cluster[jj][4]=cluster[jj][1]
				#print(cluster)
				cluster[j][4]-=cluster[j][0]
				#print(cluster)
					

				


print(total_water)
