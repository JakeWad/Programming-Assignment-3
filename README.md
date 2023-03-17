Lewis University SP23-CPSC-46000-LT1-Programming Languages

Programming-Assignment-3

Design a Polynomial Class so that

	1.The constructor can take an arbitrary number of coefficients starting from a0 to an.
	No-arg constructor will create an polynomial 0  (only a0=0).  

	2.__doc__ string of the class can be shown
	
	3.Each Polynomial object p can be used to evaluate with different value of x: 
		e.g.

		x = 3

		p = Polynomial(1, 2, 3)

		print(p(3))     # 34   

	4.Dimension: p.dim()  
		# In p’s case, it should be 2.

	5.Addition and Subtraction of polynomials

	6.Conversion of a polynomial to a string. (implement __str__ and __repr__ methods)
