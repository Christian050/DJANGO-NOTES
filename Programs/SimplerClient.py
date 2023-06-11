import urllib.request

FileHandle = urllib.request.urlopen('http://127.0.0.1:9000/romeo.txt')
for line in FileHandle:
    print(line.decode().strip())