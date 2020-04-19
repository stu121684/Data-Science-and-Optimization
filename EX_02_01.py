import numpy as np
import matplotlib
import matplotlib.pyplot as plt


#s_hat is the fourier transformed array. this way we have to call rfft only once globally.
#indices the argsort blabla. same reason as in line above
def approx(s_hat,indices,a):
	ix = indices[0:a]
	res = np.zeros(len(s_hat),dtype=complex)
	for x in ix:
		res[x]=s_hat[x]
	return np.fft.irfft(res).real

data = open(r"dax_data.txt","r")
s = np.genfromtxt(data,delimiter=None, dtype=complex)
t = np.arange(0,s.size,1)
# x-axis as dates
t2 = np.arange('2001-04-10','2020-04-10',dtype='datetime64[D]')

#compute these once
s_hat = np.fft.rfft(s)
ix = np.flip(np.argsort(np.abs(s_hat)))

##a)
fig1,ax = plt.subplots()
ax.plot(t2,s,label='data')
for x in [1,5,10]:
	ax.plot(t2,approx(s_hat,ix,x),label=str(x)+" biggest amplitudes")
ax.set(xlabel='day', ylabel='DAX value', title='plot the day')
ax.legend()
ax.grid()

##b)
diff = np.inf
c = 0
while diff > 100 :
	diff = np.linalg.norm(s-approx(s_hat,ix,c),1)/len(s)
	c+=1
print("You need " + str(c) + " coefficients.")
fig2,ax = plt.subplots()
ax.plot(t2,s,label='data')
ax.plot(t2,approx(s_hat,ix,c),label=str(c)+" biggest amplitudes")
ax.set(xlabel='day', ylabel='DAX value', title='plot the day')
ax.legend()
ax.grid()

##c)
fig3,ax=plt.subplots()
ax.plot(t2,s,label='data')
for a in range(0,5):
	res = np.zeros(len(s_hat),dtype=complex)
	res[ix[a]]=s_hat[ix[a]]
	ax.plot(t2,np.fft.irfft(res).real,label=str(a+1)+" biggest amplitude")
ax.legend()
ax.grid()

fig1.savefig("1a.png")
fig2.savefig("1b.png")
fig3.savefig("1c.png")
plt.show()

data.close()
