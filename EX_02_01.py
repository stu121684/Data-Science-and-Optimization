import numpy as np
import matplotlib
import matplotlib.pyplot as plt

data = open(r"dax_data.txt","r")
s = np.genfromtxt(data,delimiter=None, dtype=complex)
t = np.arange(0,s.size,1)
# x-axis as dates
t2 = np.arange('2001-04-10','2020-04-10',dtype='datetime64[D]')

ffts = np.fft.fft(s)
#arguments sorted descending in size of amplitude
argsor = np.flip(np.argsort(np.abs(ffts)))

##a)
approximations = []
for a in range(0,11):
	approx = argsor.take(range(0,a))
	iffts = np.zeros(s.size,dtype=complex)
	for x in range(0,approx.size):
		iffts[approx[x]]=ffts[approx[x]]
	approximations.append(np.fft.ifft(iffts))

fig1,ax = plt.subplots()
ax.plot(t2,s,label='data')
for x in range(0,11):
	if x in [1,5,10]:
		ax.plot(t2,approximations[x],label=str(x)+" biggest amplitudes")
ax.set(xlabel='day', ylabel='DAX value', title='plot the day')
ax.legend()
ax.grid()

##b)
diff = np.inf
amount = 0
iffts = np.zeros(s.size,dtype=complex)
while diff > 100 :
	iffts[argsor[amount]]=ffts[argsor[amount]]
	diff = np.linalg.norm(s-np.fft.ifft(iffts),1)/s.size
	amount+=1
print("You need " + str(amount+1) + " coefficients.")

##c)
fig3,ax=plt.subplots()
ax.plot(t2,s,label='data')
for a in range(0,5):
	iffts = np.zeros(s.size,dtype=complex)
	iffts[argsor[a]]=ffts[argsor[a]]
	ax.plot(t2,np.fft.ifft(iffts),label=str(a+1)+" biggest amplitude")
ax.legend()
ax.grid()

##test
iffts = np.zeros(s.size,dtype=complex)
iffts[argsor[1]]=ffts[argsor[1]]
iffts1=np.copy(iffts)
iffts1=np.fft.ifft(iffts1)
iffts = np.zeros(s.size,dtype=complex)
iffts[argsor[2]]=ffts[argsor[2]]
iffts2=np.copy(iffts)
iffts2=np.fft.ifft(iffts2)
#for x in iffts2:
	#print(x)

###example 246
fig4,ax=plt.subplots()
ax.plot(t2,s,label='data')
approx = argsor.take(range(0,246))
iffts = np.zeros(s.size,dtype=complex)
for x in range(0,approx.size):
	iffts[approx[x]]=ffts[approx[x]]
ax.plot(t2,np.fft.ifft(iffts),label=str(100)+" biggest amplitudes")
ax.legend()
ax.grid()

fig1.savefig("1a.png")
fig3.savefig("1c.png")
fig4.savefig("test.png")
plt.show()

data.close()
