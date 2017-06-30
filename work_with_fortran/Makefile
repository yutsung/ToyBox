# fortran dll demo01 Makefile

FC = gfortran

demo01:
	$(FC) -shared -fPIC -o demo01.so demo01.f90

.PHONY:clean
clean:
	rm ./*.mod
