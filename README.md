# **Thông Tin Vô Tuyến (140928 - ET3901)**
  **Phùng Phú Cường 20190084**
## **Nội dung bài tập lớn: Truyền file giữa 2 máy tính sử dụng cổng loa và mic**
 Truyền 1 file văn bản - Chuyển thành số nhị phân - Điều chế số - Truyền đi bằng sóng âm thanh- Thu lại và giải mã trở lại đúng file ban đầu

## Các bước truyền và nhận tin

### *Bên phát*
 1. Mã hoá file văn bản đầu vào thành mã nhị phân (sử dụng kĩ thuật nén RLE)
 2. Thêm mã phát hiện lỗi CRC
 3. Thêm bit tiền tố và hậu tố
 4. Điều chế số bằng phương pháp BFSK
 5. Truyền âm thanh đi
### *Bên thu*
 1. Thu âm thanh
 2. Lọc các tần số khác với các tần số sóng mang
 3. Giải điều chế BFSK âm thanh thu được về mã nhị phân
 4. Xoá bỏ các bit 0 dư thừa và các bit tiền tố, hậu tố
 5. Giải mã CRC để phát hiện lỗi tín hiệu nhận
 6. Giải mã RLE mã nhị phân về văn bản gốc

# Yêu cầu
## Cài đặt môi trường
- Python 3.10 

- Jupyter Notebook

## Thư viện bổ sung bên máy phát
- numpy
```
pip install numpy
```
- sounddevice
```
pip install sounddevice
```
- scipy
```
pip install scipy
```

## Thư viện bổ sung bên máy thu 
- pyaudio
```
pip install pyaudio
```

- PyQt6
```
pip install PyQt6
```
- numpy
```
pip install numpy
```
- scipy
```
pip install scipy
```

# Thử nghiệm
## Thử nghiệm trong môi trường độ ồn thấp 