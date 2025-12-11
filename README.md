# Week 1 Project: Mini Log 

Mục tiêu: Viết một chương trình Python đọc một file log (giả lập server logs), parse từng dòng thành các Object, lọc dữ liệu và ghi lại các lỗi phát sinh.

Dữ liệu giả lập (server.log): Bạn hãy tạo thủ công một file tên server.log với nội dung sau để làm đầu vào:

Plaintext

INFO:User1 login success
ERROR:Database connection failed
INFO:User2 login success
WARNING:High memory usage
ERROR:Timeout connecting to API
INVALID_LINE_WITHOUT_COLON
INFO:User3 logout
Bước 1: Setup & Git (Áp dụng Day 1)
Khởi tạo dự án:

Tạo thư mục week1_project.

Chạy git init.

Tạo file .gitignore (thêm *.log, __pycache__/ vào để không commit file rác).

Cấu trúc:

Plaintext

week1_project/
├── data/
│   └── server.log     (File dữ liệu mẫu ở trên)
├── src/
│   ├── __init__.py
│   ├── models.py      (Chứa Class)
│   └── main.py        (Chứa logic chính)
└── README.md
Commit đầu tiên: Commit cấu trúc rỗng lên branch main.

Bước 2: Xây dựng Data Model với OOP (Áp dụng Day 1 & 2)
Yêu cầu: Tạo file src/models.py.

Class cha (LogEntry):

Attributes: timestamp (dùng datetime.now() mặc định), message.

Method: display_info() in ra nội dung log cơ bản.

Class con (Kế thừa & Override):

ErrorLog(LogEntry):

Thêm attribute error_code (ví dụ: gán mặc định 500 nếu không có).

Override display_info(): In ra chữ màu đỏ (hoặc thêm prefix [URGENT]).

InfoLog(LogEntry):

Override display_info(): Thêm prefix [NORMAL].

Bước 3: Xử lý Exception & Logging (Áp dụng Day 3)
Yêu cầu: Làm việc trong src/main.py.

Thiết lập module logging:

Cấu hình để ghi logs của chính chương trình vào file pipeline_error.log.

Level: ERROR.

Tạo hàm parse_log_line(line):

Input: 1 dòng text (ví dụ: "ERROR:Database connection failed").

Logic: Tách chuỗi bằng dấu :.

Exception Handling:

Dùng try...except để bắt lỗi nếu dòng không có dấu : (như dòng INVALID_LINE_WITHOUT_COLON).

Nếu lỗi: Ghi vào pipeline_error.log bằng logging.error(), sau đó raise một Custom Exception tên là LogFormatError (bạn tự định nghĩa class này kế thừa từ Exception).

Bước 4: Generator Pipeline (Áp dụng Day 6 & 7)
Yêu cầu: Tối ưu việc đọc file lớn (Lazy Evaluation).

Viết hàm generator read_log_file(file_path):

Dùng Context Manager (with open(...)) để mở file.

Dùng vòng lặp for để đọc từng dòng.

Sử dụng yield để trả về từng dòng (đã loại bỏ khoảng trắng thừa).

Lợi ích: Nếu file log nặng 10GB, RAM máy bạn vẫn không bị tràn.

Bước 5: Xử lý Logic & Clean Code (Áp dụng Day 4 & 5)
Yêu cầu: Hoàn thiện src/main.py.

Hàm main (Entry point):

Sử dụng cấu trúc if __name__ == "__main__":.

Pipeline xử lý:

Khởi tạo một list rỗng processed_logs = [].

Dùng vòng lặp duyệt qua generator read_log_file.

Trong vòng lặp: Gọi parse_log_line. Nếu gặp lỗi (đã catch ở Bước 3), bỏ qua dòng đó và tiếp tục dòng sau (continue).

Nếu parse thành công (ra object ErrorLog hoặc InfoLog), thêm vào list.

Comprehensions (Day 5):

Sau khi có list processed_logs, sử dụng List Comprehension để tạo ra một list mới chỉ chứa các message của ErrorLog.

Ví dụ: error_messages = [log.message for log in processed_logs if isinstance(log, ErrorLog)]

Kết quả:

In ra tổng số log xử lý thành công.

In ra danh sách các lỗi tìm thấy.

Checklist Kiểm Tra Kết Quả (Definition of Done)
[ ] Git: Đã push code lên GitHub.

[ ] OOP: Có class cha, class con, override method.

[ ] Robustness: Chạy chương trình với file server.log chứa dòng lỗi mà chương trình không bị crash (nhờ try/except).

[ ] Log file: Kiểm tra file pipeline_error.log, nó phải chứa dòng báo lỗi về INVALID_LINE_WITHOUT_COLON.

[ ] Generator: Không dùng readlines() (đọc hết vào RAM) mà dùng yield.

[ ] Clean Code: Code chia tách rõ ràng (Model riêng, Logic riêng), đặt tên biến chuẩn snake_case.