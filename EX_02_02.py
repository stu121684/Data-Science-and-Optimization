import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#a)
def compress(img, qual):
	img_ft = np.fft.fftn(img)
	flat_img=img_ft.flatten()
	#take the indices that produce the quality% biggest coefficients
	ix = np.flip(np.argsort(np.abs(flat_img)))[0:int(qual*0.01*len(flat_img))]
	result = np.zeros(len(flat_img),dtype=complex)
	for x in ix:
              result[x]=flat_img[x]
	result = np.reshape(result, img_ft.shape)
	result = np.fft.ifftn(result).real
	return result


img = plt.imread('./easter.png')

for x in [100,50,10,1,0.1]:
	com_img = compress(img, x)
	plt.figure()
	plt.imshow(com_img)
	plt.title('compressed using {}% of coefficients'.format(x))
	plt.savefig('pic{}.png'.format(x))
plt.show()

#b)
#all my compressions look bad so my compromise would be not to compress the picture at all
