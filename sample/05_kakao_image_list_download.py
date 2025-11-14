import requests
import json

def download_image(image_url, filename):
    response = requests.get(image_url)

    print(response)
    if response.status_code == 200:
        with open(filename, "wb") as fp:
            fp.write(response.content)

#download_image("https://blog.kakaocdn.net/dn/nrYgY/btssALnr3yc/u155kAGHjX3ksJtFmKjiak/img.jpg", "mytest.jpg")

# 이미지 검색
search_url = "https://dapi.kakao.com/v2/search/image"
kakaoRestAPI = "이곳에 Kakao REST API키를 넣어 주세요"
headers = {
    # 카카오 개발자 REST API 키를 입력한다.
    "Authorization": "KakaoAK "+ kakaoRestAPI
}

data = {
    "query": "기차"
}

# 이미지 검색 요청하여 다운로드
response = requests.post(search_url, headers=headers, data=data)
if response.status_code != 200:
    print("requests 응답 에러: ", response.json())
else:
    count = 0
    for info in response.json()['documents']:
        count = count + 1
        filename = "test_%d.jpg" %(count)
        print(f"[{count}] url =", info['image_url'], ", filename =", filename)
        download_image(info['image_url'], filename)

     
