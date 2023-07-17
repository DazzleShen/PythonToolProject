
#把文件按照列表的方式读取 file_path为全路径
def read_file_to_list(file_path):
    print(file_path)
    with open(file_path, 'r', -1, 'utf-8') as file:
        content = file.read().splitlines()
    return content
