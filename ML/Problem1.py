import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as ax

# data = numpy.genfromtxt('girls_age_weight_height_2_8.csv', delimiter=',')
# print data[0]

file = open('girls_age_weight_height_2_8.csv', 'r')
age = []
weight = []
height = []
for line in file:
	row = line.strip().split(',')
	age.append(float(row[0]))
	weight.append(float(row[1]))
	height.append(float(row[2]))

meanAge = np.mean(age)
std_devAge=np.std(age)
meanWeight = np.mean(weight)
std_devWeight=np.std(weight)
print "Mean age:", meanAge
print "Std deviation of Age:", std_devAge
print "Mean Weith:",meanWeight
print "Std deviation of weight:", std_devWeight

# plt.scatter(age,weight)
# plt.title('Scatter plot')
# plt.xlabel('age')
# plt.ylabel('weight')
# plt.show()


ageScaled = []
weightScaled = []
for i in range(len(age)):
	ageScaled.append((age[i] - meanAge)/std_devAge)
	weightScaled.append((weight[i]-meanWeight)/std_devWeight)

print "======================================= scaled age ======================================="
print ageScaled
print "======================================= scaled weight ======================================="
print  weightScaled



def GradientDescent(alpha):
	global Beta0, Beta1, Beta2
	Beta0 = 0
	Beta1 = 0
	Beta2 = 0
	riskVal = []
	h = lambda beta0, beta1, beta2, i: (beta0 + beta1*ageScaled[i] + beta2*weightScaled[i] - height[i])

	for iterations in range(50):
		beta0_total = 0
		beta1_total = 0
		beta2_total = 0
		riskTotal = 0
		for x in range(len(age)):
			beta0_total += h(Beta0, Beta1, Beta2, x)
			beta1_total += h(Beta0, Beta1, Beta2, x)*ageScaled[x]
			beta2_total += h(Beta0, Beta1, Beta2, x)*weightScaled[x]
			riskTotal += ( h(Beta0, Beta1, Beta2, x) * h(Beta0, Beta1, Beta2, x) )

		Beta0 -= alpha*(beta0_total/len(age))
		Beta1 -= alpha*(beta1_total/len(age))
		Beta2 -= alpha*(beta2_total/len(age))
		riskVal.append(riskTotal/(2*len(age)))
		# print (beta0_total/len(age))
	print "=========== Alpha:",alpha, "==========="
	print "beta 0:", Beta0
	print "beta 1:", Beta1
	print "beta 2:", Beta2
	return riskVal

riskValues = [[],[],[],[],[],[]]
riskValues[0].extend(GradientDescent(0.005))
riskValues[1].extend(GradientDescent(0.001))
riskValues[2].extend(GradientDescent(0.05))
riskValues[3].extend(GradientDescent(0.1))
riskValues[4].extend(GradientDescent(0.5))
riskValues[5].extend(GradientDescent(1.0))

linArray = list(range(50))
plt.figure("Convergence Rate")
for i in range(len(riskValues)):
	plt.plot(linArray, riskValues[i])
plt.xlabel('iterations')
plt.ylabel('Risk Values')
plt.legend(['Alpha:0.005','Alpha:0.001','Alpha:0.05','alpha:0.1','Alpha:0.5','Alpha:1'])
plt.show()

print "==================================== Best Alpha===================================="
print "Alpha:", 1
print "Beta 0:",Beta0
print "Beta 1:", Beta1
print "Beta 2:", Beta2

predictAge = (5.0 - meanAge)/std_devAge
predictWeight = (20.0 - meanWeight)/std_devWeight
predictedHeight = Beta0 + (Beta1*predictAge) + (Beta2*predictWeight)
print "Predicted Height", predictedHeight


