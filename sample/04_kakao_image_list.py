import requests
import json

# 이미지 검색
url = "https://dapi.kakao.com/v2/search/image"
kakaoRestAPI = "카카오 REST API를 넣는다."
headers = {
    "Authorization": "KakaoAK "+ kakaoRestAPI
}

data = {
    "query": "기차"
}

# 이미지 검색 요청
response = requests.post(url, headers=headers, data=data)
if response.status_code != 200:
    print("requests 응답 에러: ", response.json())
else:
    count = 0
    for info in response.json()['documents']:
        print(f"[{count}] url =", info['image_url'])
        count = count + 1
