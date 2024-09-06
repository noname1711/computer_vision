import matplotlib.pyplot as plt

#line chart
x = [1,2,3,4,5]
y = [10,16 ,20, 30, 25]

x1=[1,2,3,4,5]
y1=[20,15,8,9,20]

plt.plot(x,y,'ro-',label='Dữ liệu 1')    #label dán nhãn chú thích cho đường
plt.plot(x1,y1,'gx--',label='Dữ liệu 2')
plt.legend()   #cho phép hiển thị label
plt.xlabel('X')   #label cho trục x
plt.ylabel('Y')   #label cho trục y
plt.title('Biểu đồ đường thẳng')   #tên của biểu đồ
plt.show()


# bar chart
categories = ['A','B', 'C', 'D', 'E']
values = [10, 15, 7, 8, 12]

plt.bar(categories, values, color='b', alpha =0.6)  #hiển thị biểu đồ đường với độ trong suốt alpha là 0.6
#alpha =0 là trong suốt(ko nhìn thấy đường) và =1 là màu đầy đủ
plt.xlabel('Danh mục')
plt.ylabel('giá trị')
plt.title('Biểu đồ cột')
plt.show()


# pie chart
my_labels = ['A', 'B', 'C', 'D']
sizes = [15, 30,45, 10]
my_color =['red', 'green' , 'blue', 'yellow']

plt.pie(sizes, labels = my_labels, colors= my_color, autopct ='%1.1f%%') #vẽ biểu đồ tròn
# autopct ='%1.1f%%' để hiển thị số liệu với 1 chữ số sau dấu phẩy 
plt.title('Biểu đồ tròn')
plt.show()

#scatter plot
x = [1,2,3,4,5]
y = [10,16 ,20, 30, 25]

plt.scatter(x,y,c='r',marker='o', label='Dữ liệu')   #vẽ biểu đồ phân tán
plt.legend()   #cho phép hiển thị label
plt.xlabel('X')   #label cho trục x
plt.ylabel('Y')   #label cho trục y
plt.title('Biểu đồ phân tán')   #tên của biểu đồ
plt.show()

#box plot
data =[15,18,22,30,45,50,55,65]

plt.boxplot(data,vert=False)  #vẽ biểu đồ hộp
#vert=False để biểu đồ hộp nằm ngang, nếu ko có vert mà chỉ plt.boxplot(data) thì sẽ mặc định nằm dọc
plt.ylabel('Giá trị')
plt.title('Biểu đồ hộp')
plt.show()


#violin plot
data = [15,18,22,30,35,45,50,55,65]

plt.violinplot(data,showmeans=True)  #vẽ biểu đồ hình violin
#showmeans=True để hiển thị giá trị trung bình(mean)
plt.title ('Biểu đồ violin')
plt.ylabel('Giá trị')
plt.show()


#wordcloud
from wordcloud import WordCloud

text = "Python is an amazing language for data visualization and word clouds."
wordcloud = WordCloud(width= 800, height=400).generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Biểu đồ đám mây từ văn bản ví dụ')
plt.show()


#radar chart
import numpy as np  # Thư viện numpy được import để thực hiện các phép toán số học, đặc biệt là với mảng (arrays).
# Khởi tạo danh sách các danh mục (categories) và giá trị (values) tương ứng.
categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 4, 3, 7, 6]
N = len(categories)  # Xác định số lượng danh mục (categories), lưu vào biến N.
# Thêm giá trị đầu tiên vào cuối danh sách values để tạo thành một chu kỳ khép kín cho biểu đồ radar.
values += values[:1]
# Tính toán các góc (angles) tương ứng cho mỗi danh mục trên biểu đồ radar.
# Angles được tính toán dựa trên tỷ lệ của số danh mục, với mỗi danh mục cách đều nhau trên vòng tròn 360 độ (2π radians).
angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]  # Thêm góc của danh mục đầu tiên vào cuối để đảm bảo rằng biểu đồ radar khép kín.
# Vẽ biểu đồ radar với các giá trị và góc tương ứng.
# 'o-' chỉ định kiểu đường nối giữa các điểm là đường liền với các điểm tròn, linewidth=2 chỉ định độ dày của đường.
plt.polar(angles, values, 'o-', linewidth=2)
# Tô màu vùng bên trong biểu đồ radar để làm nổi bật diện tích dưới đường biểu diễn.
# 'b' chỉ định màu xanh dương, alpha=0.1 chỉ định độ trong suốt của màu (10% trong suốt).
plt.fill(angles, values, 'b', alpha=0.1)
plt.title('Biểu đồ radar')
plt.show()
