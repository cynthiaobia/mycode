# what is a prime number
# 1 <= 50
# for i in range (1-50)
# if x divisible by x+1 , so if % == 0

num = 1 
while num <= 50:
    for i in range(1, 51):
        if (num % i) != (num or 1):
            print(num)
            num += 1
        else:
            num += 1
            