# 파일 쓰기
data = "hello world!!!"
with open("test.txt", "w") as fp:
    fp.write(data)

# 파일 읽기
with open("test.txt", "r") as fp:
    print("결과)")
    print(fp.read())


"""
결과)
hello world!!!
"""
