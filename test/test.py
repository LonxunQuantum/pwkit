import linecache


file_path = "/data/home/liuhanyu/hyliu/code/pwkit/demo/atom.pwmat"
line1 = linecache.getline(file_path, 1)
print(line1.split())