import requests
from bs4 import BeautifulSoup
import re

url = "https://data.gia.edu/RDWB/Captcha.jsp?reportno=1216439808&APIno=1&"

payload = {}
headers = {
    'authority': 'data.gia.edu',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'JSESSIONID=7FD7BC8F71F662FB69C359EF44C56D4E; _gcl_au=1.1.930539773.1698073732; _gid=GA1.2.1701131246.1698073732; notice_behavior=implied,eu; _mkto_trk=id:188-KZV-169&token:_mch-gia.edu-1698073731955-33607; _fbp=fb.1.1698073732026.132429851; www_gia_edu_notice_behavior_session=e596ef3e-9b5f-413d-b7de-0e5a37f00f7b|NEW; bm_mi=8D728C762FD413B0ED934093CAFB81BD~YAAQuxQgF53gz2CLAQAANhjkYBXaXbPrsz/KUhF3WwaB7RI2lh2eCKJQEm61NUtErlRTTn3ZGI7v+Iv/rUTvN+ztTxCKG2nVMrFKban0R5v7WyD0dKCiCOSu8iv/YE1sTkuRQ3X4ZpGZP6QsiJsoyJ7TSkZ4EolyoXQM5kQnqCuSKNuOkd3qNFmk+r/XfdBbclaMYXoXXYpTmcA86u0lg7JVAxXIBjlhqlqlXpsZObzsTYQpPHeRMo9NU0JQzz/EANMZaXDubnpCH/XDr0cz1XBVkjdw1WaDS//QjEDnhiWMBUiE63fXAq3UaMSRZ5xj/PHssp6ckBvKbvs=~1; ak_bmsc=BBBC8CFBEAB9B276A36FE117805D788D~000000000000000000000000000000~YAAQuxQgF6Lgz2CLAQAAzBjkYBWEsVVLd01OyfqD/mB5gyR8y86+JsdaslAFQSJVWsFYCjq6GbENdPb0DhH1nI3WsVwvtQi25wOqSMPG/N/Hq/BkAzElX64r6yiaFFyH4MfaE5apt0yNYbxzbWyAi4sbGEQQNHOjurvqjjrrTt30anbXgFg6uJFIhu4y9bTTGiJyaz/OgrtOeOaI2xgPpREM826PauwgSNrXFv+eEITraXDKSg53W9AWlTI22T4NEd3yY43kJlSl7cyAPOuAKqQg+SdRD4HfiJLPBlgrpaEC3DAh0Nv6Kmpsru0wqdbxA0bbWbo0jI4BiJ/90vWr6kAheQX+wMnvaBArkxC3OBI8x1zon2I8Ezs3r+4SdeYqmyc1TtcdqNCm2QzT7+ktqcnjScPCITkOLuy3i4FRrYPaydmAZUHM1Zvu2oG3YcDCfWO/0cNoSFRRgSc2ZlGp4pz5C2HRGSfADT934wLBSiFVDN+6cUp+kFrCypXjFhTSAHxt4lRi3ggIAa5yETClvERmf2k6cibdSc7PIAHl; www_gia_edu_notice_behavior=2:; www_gia_edu_notice_behavior_gdpr=0,1,2:; cmapi_gtm_bl=; cmapi_cookie_privacy=permit 1,2,3; AWSALBTGCORS=C9E1GoXkFfym2cttPWV34Gsy/yXbhLYqd6DhBPHjWS+voV/F8NItvbYT+kssY5wBgnhUBEYUcb/V3MG0knrzlVXhUUZahklzGVvSFrQAWTp7Td9JOozAS/nbtA6YXK6CsIU4YhYVAnywVpr311/+KV2yf8u5epcyiQ68UO8Y8Y9Q; AWSALBTG=ouK0RAEwkzMqPaTCPTbNaxBD1wh4rh4n4tdKrVLLjCaZJYGtOodXkUz5tDCsFSIlxQqHM8kBKqYRKH7TAFBPjjJJ3oUREDDCXQLDBIvx3R97CCkqB8Sr+Zntez4TkGmIGPf1PDo/nfTJ9J0cF/YDe5YziHq2GiAgAJTAyVJHGFq+1DNP4H06zPzBbO4yiSdjoj0kwYacOFD71Uxm/0XWmNL4DhUaro6v2Add5YHxKfFc9dFED5MOJloT7M/06lXV; AWSALB=7+bwvTsS8sFEJJ7bn/4MOXd4nX7F0997M4WMf0U5Dt5YXG0yq78Kl/ROnTHE6jQmUuv21iWp4JD9ktmEyPe5EPX0Z6ha2XCZ+x1/GvoO/d52NRBJ4TDsyQwngHKI; _ga=GA1.2.929789515.1698073732; _dc_gtm_UA-2003729-8=1; _ga_NGL0Y2XLC8=GS1.2.1698137643.3.1.1698138573.60.0.0; bm_sv=4D7BF6C44ED3EBB0B5265C9F637B6026~YAAQuxQgF6MP0GCLAQAAq9XyYBX6UebNh0sfNRSQ9lD4+lUHPwOLeam+IcJ7+ECzIG5TZZQjv/RIIpDeKcYxCf+glJ+7rgAIh/tFZBfjNuVh8/9McjOtNuJNAip1JcEARcZKVJRGzEyKhgNgfnXFJ8XqeAZgbEX5nQ+VQqX/hYEufbxb5vAPS5963WpmrDdRqDIyd7ckrZ8iRswxOSntK5BoTk3fvJRrozIq+8A2PYMQdvUSG9BzqNGOGQ8yEA==~1; _ga_X9RQF288SJ=GS1.1.1698137643.2.1.1698138608.25.0.0; bm_sv=4D7BF6C44ED3EBB0B5265C9F637B6026~YAAQuxQgF0Ia0GCLAQAAN0P2YBV2Pl1eGsURIZTzMizme3W5SGHvz0K59cvLHYOVUIa58rnPwwV+tdZi4FBYR35vYoNePxTrHwvwvkPWtg687Ml5ANB5JVJDxVgk9DGYoeCQtM4axGOyk75UL3F3xwkv7IB341SmxbrqDwgdkdEc7zKKGg7lyvWW0PTpDDywUfi5+dKzEeQcmUlUJFeBnanjDuo38Vrjt44wAafZ081/+xI3yGI2aHUwv8AFhQ==~1; AWSALB=67/sobzPoXUOkLanN6R2nXoX1W1tHtjzCxuzWKfOBDWSmaHHwmEJ4OOtWD607P5xjgnWKYEcd3yXkFWoSN6jqVSzkyPh2Eyr3fMKDTitBfo467p8Kexz6mmD7kzP; AWSALBCORS=67/sobzPoXUOkLanN6R2nXoX1W1tHtjzCxuzWKfOBDWSmaHHwmEJ4OOtWD607P5xjgnWKYEcd3yXkFWoSN6jqVSzkyPh2Eyr3fMKDTitBfo467p8Kexz6mmD7kzP; AWSALBTG=eyJFq5GU9awii6qcxbkKze6Ar9KpMj4AZlZYzH1nzwE/UjBgclzV72WFD56gIcgPjmr/1Md+h1qWv5tf0DXHX6qmXWKETz5ruUFwhwu6uezzvfhKUDROvVmMsoG2UW58LRRv2WC1XvRv+l6cgKOB/dPcjYxV/cmYHCwksIieImrWIpkJAGSFI640brBLOTbtaXARALdmENyjwdblu6Oo0k+KutHdZrhtQKhPW3nuCuyuWnDvmM1XTxhvpvFi6Jg7; AWSALBTGCORS=eyJFq5GU9awii6qcxbkKze6Ar9KpMj4AZlZYzH1nzwE/UjBgclzV72WFD56gIcgPjmr/1Md+h1qWv5tf0DXHX6qmXWKETz5ruUFwhwu6uezzvfhKUDROvVmMsoG2UW58LRRv2WC1XvRv+l6cgKOB/dPcjYxV/cmYHCwksIieImrWIpkJAGSFI640brBLOTbtaXARALdmENyjwdblu6Oo0k+KutHdZrhtQKhPW3nuCuyuWnDvmM1XTxhvpvFi6Jg7',
    'referer': 'https://www.gia.edu/',
    'sec-ch-ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-site',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61'
}

response = requests.request("GET", url, headers=headers, data=payload)

soup = BeautifulSoup(response.text, 'html.parser')

script = soup.findAll("script")
pattern = "(event.source.postMessage)"

lst = script[1]

print(soup.text)
