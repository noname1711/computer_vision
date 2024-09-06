import numpy as np

#tạo mảng 1 chiều
a = np.array([1,2,3])
#in mảng
print(a)
#in ra phần tử bất kì
element = a[1]
print(element)    #vị trí số 1 của mảng là 2


#tạo mảng 2 chiều
matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])
#in mảng
print(matrix)
#in phần tử bất kì
element = matrix[1,2]   #vị trí hàng thứ 1 và cột thứ 2(tính từ 0)
print(element)    #có giá trị là 6


#cách tạo mảng

#tạo mảng toàn số 0
a = np.zeros((3,5))    #3 hàng và 5 cột
print(a)

#tạo mảng toàn số 1
a = np.ones((3,5))
print(a)

#tạo mảng rỗng
a = np.empty((3,5))   #lưu ý mảng rỗng nó sẽ mặc định hiển thị là 1
print(a)

#tạo mảng từ 1 đến 100, bước nhảy 1
a = np.arange(1,101,1)   
print(a)

#tạo mảng gồm các phần tử với khoảng cách đều nhau
a = np.linspace(0,10,5)     #mảng start 0 end là 10 và có 5 phần tử cách đều nhau
print(a)     #[ 0.   2.5  5.   7.5 10. ]

#xác định kiểu dữ liệu
a = np.ones(5, dtype= np.int64)
print(a.dtype)    #int64


#thêm, xóa, sắp xếp các bảng
#tạo mảng ban đầu
arr = np.array([3,1,2,4,5])   #3,1,2,4,5
print(arr)

#sắp xếp
arr = np.sort(arr)
print(arr)    #[1 2 3 4 5]
#sắp xếp ngược (sắp xếp nhưng in theo chiều ngược lại)
arr = np.sort(arr)[::-1]
print(arr)    #[5 4 3 2 1]

# thêm phần tử vào mảng
arr = np.append(arr, 6)   #thêm 6 vào mảng
print(arr)    #[5 4 3 2 1 6]

#xóa 1 vị trí nào đó trong mảng
arr = np.delete(arr, 3)   #xóa vị trí thứ 3
print(arr)    #[5 4 3 1 6]  mất số 2

#tạo mảng 2 chiều
arr = np.array([[3,1,2],[4,6,8],[9,7,5]])
#sắp xếp tăng dần
sap_xep_theo_hang = np.sort(arr, axis=1)  #theo hàng thì axis =1
print(sap_xep_theo_hang)    #[[1 2 3] [4 6 8]  [5 7 9]]
sap_xep_theo_cot = np.sort(arr, axis =0)  #theo cột thì axis =0
print(sap_xep_theo_cot)    #[[3 1 2] [4 6 5] [9 7 8]]
#sắp xếp giảm dần(thên dấu -)
sap_xep_theo_hang = -np.sort(-arr, axis=1)  #theo hàng thì axis =1
print(sap_xep_theo_hang)    #[[3 2 1] [8 6 4] [9 7 5]]
sap_xep_theo_cot = -np.sort(-arr, axis =0)  #theo cột thì axis =0
print(sap_xep_theo_cot)    #[[9 7 8] [4 6 5] [3 1 2]]


#đưa ra các thông số về mảng
#tạo mảng 2 chiều
arr = np.array([[1,2,3], [4,5,6]])
#sử dụng các thuộc tính để lấy thông tin về chúng
so_chieu = arr.ndim   #số chiều
kich_thuoc = arr.size   #kích thước = tổng số phần tử
hinh_dang = arr.shape    #hình dạng (số hàng x số cột)
#in ra các thông số
print("Số chiều: ", so_chieu)    #Số chiều:  2
print("Kích thước: ", kich_thuoc)    #Kích thước: 6
print("Hình dạng: ", hinh_dang)    #Hình dạng: (2,3)


#chuyển đổi kiểu dữ liệu
arr = np.array([1,2,3,4,5])
#chuyển sang kiểu float
arr_float = arr.astype(float)
print(arr_float)    #[1. 2. 3. 4. 5.]


#thay đổi hình dạng của mảng
#từ 1 chiều thành nhiều chiều
arr = np.array([1,2 ,3 ,5 ,0,6])
reshaped_arr = arr.reshape(2,3)
print(reshaped_arr)    #[[1 2 3] [5 0 6]]
reshaped_arr =arr.reshape(3,2)
print(reshaped_arr)    #[[1 2] [3 5] [0 6]
#từ nhiều chiều thành 1 chiều
reshaped_arr = reshaped_arr.flatten()   
print(reshaped_arr)    #[1 2 3 5 0 6]


#cắt lát mảng
arr = np.array([1,2,3,4,5,6,7,8])
#cắt từ vị trí 3 đến 5
arr_cut = arr[3:5]
print(arr_cut)    #[4 5]
#cắt từ phần tử đầu tiên đến -1 (python cho phép duyệt lùi)
arr_cut = arr[:-1]    #từ ptu 0 (là 1) đếm lùi lại thì ptu -1 là 7
print(arr_cut)  #[1 2 3 4 5 6 7]
#cắt từ phần -3 đến hết 
arr_cut = arr[-3:]   #từ phần tử 0 (là 1)đếm lùi lại thành -1 -2 -3 thì -3 là số 6
print(arr_cut)    #[6 7 8]


#chuyển vị (hàng thành cột, cột thành hàng) -> lật mảng lại
arr = np.array([[1,2,3],[4,5,6]])
print(arr)    #[[1,2,3],[4,5,6]]
transposed_arr = arr.T   #T là chuyển vị
print(transposed_arr)    #[[1 4] [2 5] [3 6]]


#nối mảng
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr= np.concatenate((arr1, arr2))    #nối arr1 và arr2
print(arr)    #[1 2 3 4 5 6]


# tính toán
arr = np.array([1,2,3,4,5])
#tính tổng
sum_arr = np.sum(arr)
print(sum_arr)    #15
#tính trung bình
avg_arr = np.mean(arr)
print(avg_arr)    #3.0
#tính max
max_arr = np.max(arr)
print(max_arr)    #5
#tính min
min_arr = np.min(arr)
print(min_arr)    #1
#tính độ lệch chuẩn, đo lường mức độ phân tán của dữ liệu
std_arr = np.std(arr)
print(std_arr)    #1.4142135623730951
#tính phương sai, đo lường mức độ biến thiên của dữ liệu
var_arr = np.var(arr)
print(var_arr)    #2.0
#tính tổng tích chập
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
dot_product = np.dot(arr1, arr2)
print(dot_product)    #32