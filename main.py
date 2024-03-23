
# n = 384916
# l = n//1000; suml=0
# r = n-l*1000;sumr=0
# while l>0:
#     suml+=l%10; l = l//10
#     sumr+=r%10; r = r//10
# if suml==sumr:
#     print("yes")
# else:
#     print ("no")

# a = 2
# b = 6
# c = 10
# if a*b<c or c==a*b:
#     print ('no')
# elif c%a==0 or c%b==0:
#     print ('yes')
# else:
#     print ('no')


# coins = [0, 0, 0, 0, 0, 0, 0]
# orel = 0
# all = len(coins)
# for i in range (all):
#     if coins[i] == 1: orel +=1
# reshka = all-orel
# if orel>reshka: print (reshka)
# else: print (orel)


# s = 4
# p = 4
# x = 0
# for y in range (1000):
#     for x in range (1000):
#         if (x + y) == s and (x * y) == p and x <= y: print (x,y)


# n = 16
# i = 0
# while 2**i <= n:
#     print(2**i)
#     i += 1
