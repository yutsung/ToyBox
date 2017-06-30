module fortran_dll
use iso_c_binding
contains

subroutine fortran_sub(a_int, some_floats, a_string) bind(c, name="sub01")
! DEC$ ATTRIBUTES DLLEXPORT, ALIAS: "sub01" :: sub01
    implicit none
    integer(c_int) :: i
    integer(c_int), intent(inout) :: a_int
    real(c_double), intent(inout) :: some_floats(a_int)
    character(c_char), intent(in) :: a_string(a_int)
    character(len=80) :: test


    do i = 1, a_int
        some_floats(i) = some_floats(i)+i
    enddo

    a_int = a_int**2

    print *, a_string

end subroutine fortran_sub

end module fortran_dll
