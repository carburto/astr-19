import numpy as np

def main():

	def f(x):
		y = np.sin(x)
		return y

	for i in np.linspace (0, 2*np.pi, 1000):
		print('{0:.3f} {1:.3f}'.format(i, f(i)))



if __name__=="__main__":
	main()