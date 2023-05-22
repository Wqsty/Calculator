while True:
	def addition():
		s1 = float(input("Enter first number: "))
		s2 = float(input("Enter second number: "))
		print(s1, "+", s2,"=",s1 + s2)
		pass
	def extraction():
		s3 = float(input("Enter first number: "))
		s4 = float(input("Enter second number: "))
		print(s3, "-", s4,"=",s3 - s4)
		pass
	def multiplication():
		s5 = float(input("eEter first number: "))
		s6 = float(input("Enter second number: "))
		print(s5, "*", s6,"=",s5 * s6)
		pass
	def division():
		s7 = float(input("Enter first number: "))
		s8 = float(input("Enter second number: "))
		print(s7, "/", s8,"=",s7 / s8)
		pass

	print("""
	*  1- Addition        *
	*  2- Extraction      *
	*  3- Multiplication  *
	*  4- Division        *
	""")

	election = int(input("Seçim Girin: "))

	if election ==1:
		addition()
		pass

	if election==2:
		extraction()
		pass

	if election==3:
		multiplication()
		pass

	if election==4:
		division()
		pass
	if election>4:
		exit()