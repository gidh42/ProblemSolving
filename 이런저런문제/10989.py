##런타임에러, 시간초과
N = int(input())

my_dict = {}

for i in range(N):
    num = int(input())
    
    if num not in my_dict.keys():
        my_dict[num] = 1
    else:
        my_dict[num] = my_dict[num] + 1
        
sorted_dict = sorted(my_dict.items())

    
for i in range(len(sorted_dict)):
    for j in range(sorted_dict[i][1]):
        print(sorted_dict[i][0])
    