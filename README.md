# Text3D Renderer

## Giới thiệu  
**Text3D Renderer** là một dự án Python sử dụng thư viện **Pygame** để tạo và hiển thị mô hình 3D từ các đoạn văn bản ngắn. Điểm đặc biệt của dự án là toàn bộ logic hiển thị 3D, bao gồm phép chiếu (projection) và xử lý hiển thị, đều được xây dựng thủ công mà không phụ thuộc vào thư viện dựng hình 3D nào khác.  

## Demo  
![Demo Gif](demo/demo.gif)  
*Hình minh họa mô hình 3D của text trong dự án(Sorry for bad FPS since my monitor is quite weak)*  

---

## Tính năng chính  
- Hiển thị văn bản dưới dạng mô hình 3D xoay, phóng to, và thu nhỏ.  
- Logic hiển thị 3D hoàn toàn thủ công, bao gồm xử lý phép chiếu và phối cảnh.  
- Giao diện trực quan và đơn giản nhờ sử dụng **Pygame**.  

---

## Cách cài đặt  
1. **Clone dự án**  
   ```bash  
   git clone https://github.com/HoangAnhEm/3D_Text_Generater
   cd 3D_text_maker
   ```  

2. **Cài đặt các thư viện cần thiết**  
   Yêu cầu Python 3.10 trở lên. Cài đặt các thư viện phụ thuộc bằng lệnh:  
   ```bash  
   pip install pygame  
   ```  

3. **Chạy chương trình**  
   ```bash  
   python main.py  
   ```  

---

## Hướng dẫn sử dụng  
- **Nhập văn bản**: Người dùng có thể thay đổi văn bản được hiển thị bằng cách nhập trong giao diện (không được quá dài)
- **Tùy chỉnh góc nhìn**:  
  - **Trỏ chuột**: Xoay mô hình 3D theo các góc nhìn.  
  - **Phím di chuyển**: Di chuyển diểm nhìn.  
  - **Esc**: Tạm thời thoát chế độ điểm nhìn.  
---



