# **Thông Tin Vô Tuyến (140928 - ET3901)**
  **Phùng Phú Cường 20190084**
## **Nội dung bài tập lớn: Truyền file giữa 2 máy tính sử dụng cổng loa và mic**
 Truyền 1 file văn bản - Chuyển thành số nhị phân - Điều chế số - Truyền đi bằng sóng âm thanh- Thu lại và giải mã trở lại đúng file ban đầu

## Các bước truyền và nhận tin

| Bên phát | Bên thu |
|---|---|
|1. Mã hoá file văn bản gửi đi thành mã nhị phân (sử dụng RLE)| 1. Thu âm thanh và lọc các tần số khác với các tần số sóng mang  |
|2. Thêm mã phát hiện lỗi CRC|2. Giải điều chế BFSK âm thanh thu được về mã nhị phân|
|3. Thêm bit tiền tố và hậu tố|3. Xoá bỏ các bit 0 dư thừa và các bit tiền tố, hậu tố|
|4. Điều chế tần số bằng phương pháp BFSK|4.  Giải mã CRC để phát hiện lỗi tín hiệu nhận|
|5. Truyền âm thanh đi|5. Giải mã RLE mã nhị phân về văn bản gốc|

# Yêu cầu
## Cài đặt môi trường
- Python 3.10 

- Jupyter Notebook

## Thư viện bổ sung bên máy phát và máy thu
- numpy
- scipy
- sounddevice
```
pip install numpy sounddevice scipy
```

# Thử nghiệm
## *Thử nghiệm trong môi trường độ ồn thấp*
Văn bản truyền đi là file text.txt có nội dung "hello".

File âm thanh trong thư mục test/
- test/transmitter/audio_signal.wav là file âm thanh lý tưởng bên phát tạo ra được ghi vào 
- test/receiver/rec.wav là file âm thanh bên thu ghi lại được
- test/receiver/filtered_rec.wav là file âm thanh sau khi đã lọc
## *Kết quả thử nghiệm máy phát*