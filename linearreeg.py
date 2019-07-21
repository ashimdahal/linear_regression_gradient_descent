from numpy import *
import matplotlib.pyplot as plt

def error_computer(b,m,pts):
	error = 0
	N = float(len(pts))
	for i in range(0,len(pts)):
		x = pts[i,0]
		y = pts[i,1]
		error += (y- m*x+b)**2
	return error / (2*N)

def gradient_descent_stepper(b_inuse,m_inuse,points):
	
	m_descent =0
	b_descent =0
	learningrate = 0.0001
	N = float(len(points))
	for i in range(0,len(points)):
		x=points[i,0]
		y=points[i,1]

		b_descent += -(1/N) * (y-((m_inuse*x)+b_inuse))
		m_descent += -(1/N) * x * ( y - ((m_inuse * x)+ b_inuse))
	new_b = b_inuse - learningrate * b_descent
	new_m = m_inuse - learningrate * m_descent
	return [new_b,new_m]


def gradient_descent_run(points,iterations):
	b =0
	m=0

	for i in range(iterations):
		b,m = gradient_descent_stepper(b,m,array(points))
	return[b,m]

def main():
	points = genfromtxt('data.csv',delimiter=',')
	iterations = 5000
	[b,m] = gradient_descent_run(points,iterations)

	print (f"Starting gradient descent at b = 0, m = 0, error = {error_computer(0,0,points)}")
	print ("Running...")
	[b, m] = gradient_descent_run(points,iterations)
	print (f"After {iterations} iterations b = {b}, m = {m}, error = {error_computer(b,m,points)}")
	x = linspace(10.,80.)
	fig,ax = plt.subplots()
	ax.plot(x,m*x+b)
	ax.set_xlim((10.,80.))
	plt.scatter(points[:,0], points[:,1])
	plt.show()


if __name__ == '__main__':
	main()