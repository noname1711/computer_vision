import numpy as np

#giải hệ phương trình tuyến tính
from scipy import linalg
#định nghĩa hệ phương trình tuyến tính
a = np.array([[2,1],[3,2]])
b = np.array([5,7])
# như vậy ta đã có hệ 2x+y=5, 3x+2y=7 và giải = pp ma trận
#giải hệ pp tuyến tính
kq_hpt= linalg.solve(a,b)  #dùng solve
print("kết quả:", kq_hpt)    #kết quả: [ 3. -1.] -> x=3, y=-1


#tính tích phân của 1 hàm số
from scipy import integrate
#định nghĩa hàm f(x) = x^2
def my_func(x):
    return x**2
#tính tích phân của f(x) từ 0 đến 1
kq_tp= integrate.quad(my_func,0,1)    #dùng quad
print("kết quả:", kq_tp)   #kết quả: (0.33333333333333337, 3.700743415417189e-15) -> 0.333...7(tính đến 10^-15)


#tính giá trị riêng và vector riêng của ma trận
a = np.array([[2,1],[3,2]])
#vẫn sử dụng linalg
evals, evecs= linalg.eig(a)   #dùng eig
print("giá trị riêng:", evals)  #giá trị riêng: [3.73205081+0.j 0.26794919+0.j]
print("vector riêng:", evecs)    #vector riêng: [[ 0.5       -0.5      ]
                                                #[ 0.8660254  0.8660254]]