"""Panda has a thing for palindromes. Hence he was a given a problem by his master. The master will give Panda an array of strings S having N strings. Now Panda has to select the Palin Pairs from the given strings .

A Palin Pair is defined as :

) is a Palin Pair if Si = reverse(Sj) and

Panda wants to know how many such Palin Pairs are there in S.
Please help him in calculating this.

Input:

The first line contains N, the number of strings present in S.
Then N strings follow.

Output:

Output the query of Panda in single line.

Constraints:

1 ≤ N ≤
1 ≤ |Si| ≤  (length of string)

The string consists of Upper and Lower case alphabets only.

"""

n = int(input())
lst = []
for _ in range(0,n):
    lst.append(input())


count = 0


# for i in range(0,len(lst)):
#     curr = lst[i]
#     for j in range(i+1,len(lst)):
#         if curr == lst[j][::-1]:
#             count = count + 1

d = {}
for i in range(0,len(lst)):
    if lst[i] not in d.keys():
        d[lst[i]] = [i]
    else:
        d[lst[i]] = d[lst[i]] + [i]

# print (d)
# print (count)

final_lst = set(lst)

d_count = 0
for val in final_lst:
    for i in d[val]:
        if val[::-1] in d.keys():
            for c in d[val[::-1]]:
                if c >i:
                    d_count = d_count + 1

print(d_count)