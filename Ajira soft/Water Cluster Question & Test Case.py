Year is 3030, water is a scare resource.
Civilizations live around glaciers in clusters, with a federal body (identified as F) in center melting glaciers and controlling the water distribution.
Each cluster has need for water for a day and a water storage capacity.
Cluster are connected to each other with a pipe identified by _.
Linked clusters are connected with overflow pipes.
Every time water starts flowing through pipe, the clusters drain their tanks in an instant, as they can use the water flowing to fill the tanks, and federal body sends water till the capacity is full.
Federal body releases water at start of day, cluster uses water at end of day.
In a pipe link like F-C1-C2-C3-C4, when federal water body targets C3, only C3 and nodes before it (here C1,C2,C3) can fill the tank, C4 can fill it only when it’s targeted.
Pipes are flow controlled and water flows in forward direction only.
Calculate the minimum water needed to help the civilizations survive for n days.
Input is multiline. First line is the number of days to survive. Second line the number of clusters followed by their definitions. Next is the number of links in the system, followed by the link definition.
Read the test cases to understand the scenarios better.

Test Case:1
	3
	4 
	C1 100 300
	C2 100 300
	C3 100 200
	C4 100 400
	4
	F_C1
	F_C2
	C2_C3
	C3_C4
	
output: 1700

Test Case:2	
	2
	3 
	C1 100 300
	C2 150 300
	C3 100 100
	3
	F_C1
	F_C2
	F_C3
output: 800
	
Test Case:3
	2
	3 
	C1 100 300
	C2 150 300
	C3 100 100
	3
	F_C1
	F_C2
	C2_C3
output: 1100


Test Case:4
	5
	C1 1000 1000
	C2 1000 2000
	C3 1000 1500
	C4 1000 4000
	C5 1000 3000
	5
	F_C1
	C1_C2
	C2_C3
	C3_C4
	C4_C5
output: 16000