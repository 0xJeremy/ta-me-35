import math
import numpy as np
from statistics import mean

def fit_linear(x,y):
	m = (((mean(x)*mean(y))-mean(x*y))/((mean(x)*mean(x))-mean(x*x)))
	return m, mean(y) - m*mean(x)


X = np.array([210, 220, 230, 240, 250, 260, 270, 280, 290, 310, 320, 330, 340, 350, 370, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590])
Y = np.array([50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400])


print(fit_linear(Y, X))

# epochs = 50 
# for i in range(0, 10000000):
# 	L = i/1000000000
# 	m = 0
# 	b = 0
# 	for i in range(epochs): 
# 		Y_pred = m*X + b # The current predicted value of Y

# 		D_m = (-2/n) * sum(X * (Y - Y_pred)) # Derivative wrt m

# 		D_b = (-2/n) * sum(Y - Y_pred) # Derivative wrt b

# 		m = m - (L * D_m) # Update m

# 		b = b - (L * D_b) # Update b
# 	print("L: {},\t m: {:.5f}, b: {:.5f}".format(L, m, b))
