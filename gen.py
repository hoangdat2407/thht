import os

folder_path = "."  # Thay bằng đường dẫn thư mục của bạn
file_names = os.listdir(folder_path)

for file in file_names:
    print(f'<a href="{file}">{file}</a>')  # Dùng f-string để format chuỗi
    print('<br>')  # Xuống dòng
