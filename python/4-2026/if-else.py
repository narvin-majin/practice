n = int(input().strip())
if n%2==0:
    if 2<=n<=5:
        print("Not Weird")
    elif 6<=n<=20:
        print("Weird")
    elif n>20:
        print("Not Weird")
else:
    print("Weird")




# edge case

# 1=odd so even is false condition 2 enters if block and first if 5 same as 2 6and 20 is second if. 21 is else block 
# as for negative scale it was not asked in the problem still it is a edge case. 
# we can use n>=0 for positive if the first if line for even condition is removed even condition will not be checked and
#  hence it is more inportant so we can use n%2==0 and conditon. is there any other way

# solution 
n = int(input().strip())

if n % 2 == 1 or (6 <= n <= 20):
    print("Weird")
else:
    print("Not Weird")



#Look at the problem again:
#Odd → Weird
#Even:
#2–5 → Not Weird
#6–20 → Weird
#20 → Not Weird
#👉 Notice something?
#You only care about:
#Odd → always Weird
#Even → depends on range

#this is a new one

n = int(input().strip())

print("Weird" if (n % 2 == 1 or 6 <= n <= 20) else "Not Weird")

# value_if_true if condition else value_if_false  this when only one line is allowed.



# 2026-04-01 | if/elif hackerank(hr) | solved | 1hrs | edge case solved | narvin.