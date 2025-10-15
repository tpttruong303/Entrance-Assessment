# Dự án vòng sơ khảo của công ty Kyanon Digital

Dự án này là một chương trình nhỏ bằng Python dùng để đọc dữ liệu email từ file `.csv`, tự động lọc ra các email có nội dung xin nghỉ phép (leave request) và xuất kết quả ra file `.json` theo một định dạng có cấu trúc.

## Tính năng

-   **Đọc dữ liệu**: Đọc và phân tích cú pháp file `emails.csv`.
-   **Lọc dữ liệu**: Lọc các email dựa trên danh sách từ khóa (`leave`, `day off`, `sick`,...) có trong trường `subject` hoặc `body`.
-   **Xuất kết quả**: Xuất danh sách các email đã lọc ra file `leave_request.json` với các trường `id`, `sender`, và `type`.

## Yêu cầu

-   `uv` (công cụ quản lý gói và môi trường ảo cho Python)

## Hướng dẫn cài đặt và sử dụng

### 1. Tải dự án về máy

Clone repository này về máy.

```bash
git clone https://github.com/tpttruong303/Entrance-Assessment.git
cd Entrance-Assessment
```

### 2. Cài đặt và thực thi chương trình

Khi thực hiện lệnh uv run, các packages cần thiết và phiên bản Python phù hợp sẽ được tự động cài đặt. Sau đó logic của chương trình trong file `main.py` sẽ được thực thi. Dữ liệu cần thiết cho việc chạy dự án đã được thêm vào ở file `emails.csv`

```bash
uv run ./main.py
```
### 3. Xem kết quả

Sau khi chương trình chạy thành công, một file mới tên là `leave_request.json` sẽ được tạo ra trong thư mục dự án. File này chứa danh sách các email xin nghỉ phép đã được lọc.

**Ví dụ file `leave_request.json`:**

```json
[
    {
        "id": 1,
        "sender": "alice@company.com",
        "type": "leave_request"
    },
    {
        "id": 3,
        "sender": "charlie@client.com",
        "type": "leave_request"
    }
]
```

## Cách hoạt động

Chương trình sử dụng thư viện `pandas` để thực hiện các công việc sau:
1.  Đọc file `emails.csv` vào một DataFrame.
2.  Lọc email thông qua hàm `is_leave_request` (kiểm tra trong trường `subject` và `body` có tồn tại keywords thuộc về leave_request).
3.  Giữ lại 2 cột `id` và `sender` và loại bỏ những cột còn lại.
4.  Thêm cột `type` với nội dung `leave_request` ở mỗi dòng.
5.  Xuất kết quả qua `file leave_request.json`
