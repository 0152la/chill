# Extractiong data dependence relations of outer most loop
# for Gauss-Seidel CSR code

from chill import *

source('dep_extraction_gs_csr.c')
destination('dep_extraction_gs_csrmodified.c')
procedure('gs_csr')

loop(0)
original()
print_dep_ufs(1,1)

