import requests

url = "https://img1.daumcdn.net/thumb/R658x0.q70/?fname=https://t1.daumcdn.net/news/202105/24/forsnap/20210524161320162kywf.jpg"
# 서버에게 요청
response = requests.get(url)

if response.status_code == 200:
    print("======= 이미지 다운로드 ========")
    with open("mytest.jpg", "wb") as fp:
        fp.write(response.content)


# reuests 모듈 설치:  pip install requests
