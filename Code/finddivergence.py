import scipy.stats as scipy
import numpy as np	
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
xaxis =[]

pk=[]
qkb=[]
qkp=[]
qkq=[]
qkw=[]
tempb=[]
def probsumone(a):
	res =[]
	sum =0.0
	for i in range(0, len(a)):
		sum = sum+a[i]
	for i in range(0, len(a)):
		res.append(a[i]/sum)
	return res;
def finddivergence(temp,qk):
	temp = probsumone(temp)
	qk = probsumone(qk)
	sum =0
	pk = temp	
	for i in range(0, len(pk)):
		#print pk[i]/qk[i]
		if(pk[i]!=0 and qk[i]!=0):
			logval = math.log((pk[i]/qk[i]))
			sum = sum+(pk[i]*logval)
		else:
			sum = sum+0
			
	return sum;
def finddivergencearr(temp,qk):
	temp = probsumone(temp)
	qk = probsumone(qk)
	sum =0
	pk = temp
	tempb=[0]*len(temp)
	for i in range(0, len(pk)):
		#print pk[i]/qk[i]
		if(pk[i]!=0 and qk[i]!=0):
			logval = math.log((pk[i]/qk[i]))
			tempb[i] = tempb[i]+(pk[i]*logval)
		else:
			tempb[i] = tempb[i]+0
			
	return tempb;	

pk = [0.023,0.031]

qkb =[0.021,0.027]

qkp=[0.017,0.055]
qkq=[0.022,0.037]
qkw=[0.033,0.032]

pk = probsumone(pk)
#plotvalue = pk
qkb = probsumone(qkb)
qkp = probsumone(qkp)
qkq = probsumone(qkq)

qkw = probsumone(qkw)

for i in range(1, len(pk)):
	if(plotvalue[i]==0):
		print "zero index of pk22 "+ str(i)
print "pk len" + str(len(pk))
print "qkq len" + str(len(qkq))
print "qkp len" + str(len(qkp))
print "qkb len" + str(len(qkb))
print "qkw len" + str(len(qkw))

fig = plt.figure()
ax = fig.add_subplot(111)
temp = []
temp = pk
for i in range(1, len(pk)):
	#if(pk[i]==0):
		#print "zero index of pk"+ str(i)		
	
	if(pk[i]!=0 and qkb[i]==0):
		pk[i]=0
		
	
		
sb = scipy.entropy(pk, qkb, base=None)

sb  = round(sb ,6)

pk= temp;
for i in range(1, len(pk)):
	if(pk[i]==0):
		print "zero index of pk"+ str(i)		
	
	
	if(pk[i]!=0 and qkp[i]==0):
		pk[i]=0
		
	
sp = scipy.entropy(pk, qkp, base=None)
sp  = round(sp ,6)
for i in range(1, len(pk)):	
	if(pk[i]!=0 and qkp[i]==0):
		print "zero unchanged for M index of pk"+ str(i)
print sp
pk= temp;
for i in range(1, len(pk)):
	if(pk[i]==0):
		print "zero index of pk"+ str(i)		
	
	
	if(pk[i]!=0 and qkq[i]==0):
		pk[i]=0
			
sq = scipy.entropy(pk, qkq, base=None)
sq  = round(sq ,6)

pk= temp;
for i in range(1, len(pk)):
	if(pk[i]==0):
		print "zero index of pk"+ str(i)		
	xaxis.append(i)	
	
	if(pk[i]!=0 and qkw[i]==0):
		pk[i]=0
		
	

sw = scipy.entropy(pk, qkw, base=None)
sw  = round(sw ,6)

xaxis.append(len(pk))
print "x-axis length" + str(len(xaxis))
print 'black divergance value' + str(sb)
print 'BHispanic divergance value' + str(sp)
print 'wHispanic divergance value' + str(sq)
print 'white divergance value' + str(sw)
target = open('F:\\UDS\\newresults\\newresults\\corrected\\'+"divergencevaluecs_cloth"+'.txt', 'w')
target.write("divergencevaluestopBcs_casng:"+str(sb)+',')
target.write("divergencevaluestopPcs_casng:"+str(sp)+',')
target.write("divergencevaluestopQBcs_casng:"+str(sq)+',')
target.write("divergencevaluestopWcs_casng:"+str(sw)+',')
target.close()
line1 = 0.0036
line2= 0.0034
ax.annotate('Black divergence :'+str(sb),xy=(10,line1),xytext=(10,line1))
ax.annotate('BHispanic divergence :'+str(sp), xy=(40,line1), xytext=(300,line1))
ax.annotate('WHispanic divergence :'+str(sq), xy=(10,line2), xytext=(10,line2))
ax.annotate('White divergence :'+str(sw), xy=(40,line2), xytext=(300,line2))

plt.plot(xaxis,qkb,color='black')
plt.plot(xaxis,qkp,color='orange')
plt.plot(xaxis,qkq,color='pink')
plt.plot(xaxis,qkw,color='green')
plt.plot(xaxis,plotvalue,color='red')
plt.show()




