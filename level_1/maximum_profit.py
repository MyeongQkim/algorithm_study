'''
maximum_profit for 1 dollar Exchange Rate
22.02.19

'''

rates = [1200, 1000, 1100, 1200, 900, 1000, 1500, 900, 750, 1100]	

rate = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
k = 1000
dollars = 0 
n = len(rate)
max_profit =0

for i in range(len(rates)-1):

  if rates[i] > k and dollars == 0 :
    print("거래못함")
  else:
    if dollars ==0 :
      if rates[i+1]>rates[i]:
        dollars += 1
        k = k - rates[i]
    else : 
      if rates[i+1]<rates[i]:
        dollars -=1
        k = k+ rates[i]
  print(i,rates[i], dollars, k)
if dollars == 1 :
  k = k+ rates[len(rates)-1]

print(k)




'''
for i in range(0,n-1):
  for j in range(i+1,n):
    profit = rate[j]-rate[i]
    if profit > max_profit:
      max_profit = profit
print (max_profit)
'''