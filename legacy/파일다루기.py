# try-catch 대신 with를 쓰자
import json
with open('test_file.txt', 'r') as f:
    read_data = f.read()
    print(read_data)
print(f.closed)
