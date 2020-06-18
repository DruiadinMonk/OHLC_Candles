# Creating a cndle (OHLC) price chart.



import random



prices_1	= [1.0000]
prices_2 	= []
base_1 		= 100
base_2 		= 10


# Generate random prices in the 10'000's place.
for x in range(100):
	r1 = random.randint(-5, 5) / 10000
	r2 = round(r1 + prices_1[x], 4)
	prices_1.append(r2)



# 2. For loop #2.
a = 0		# MIN
b = 9		# MAX



# Group up candles for their OHLC values.
for x in range(10):

	# Set OHLC values.
	o = prices_1[a]					# o = prices[0]
	h = max(prices_1[a:b]) 			# h = max(prices[0:9])
	l = min(prices_1[a:b]) 			# l = min(prices[0:9])
	c = prices_1[b] 					# c = prices[9]

	ohlc = [o, h, l, c]

	prices_2.append(ohlc)

	# Move range over 10
	a += 10
	b += 10





print(prices_1)
print(' ')
print(prices_2)