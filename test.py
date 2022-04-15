import requests, bs4
import pandas as pd
from lxml import html
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote

# 1. URL 파라미터 분리하기.
# Service URL
xmlUrl = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev'

My_API_Key = unquote('EJLx43zIdY6zeRAp7MWg2sTIK0agr8O5fxfhXFOJ1PGw0FNcWk6MQL7oFQyYJlZzv5hPIfRNG9M/eyxJJyc4jg==')    # 아래 내가 받은 인증키가 안 되서 수업용 인증키 사용.
# My_API_Key = unquote('Agq7hySmyMi1FFU9kYibP%2BEnxYepQ%2FB6Dn%2Bw9lsYKVSCDjTwIdvpjmuhJrtyQrhipg3F3a4jbSq%2FLxHi%2FdUIoQ%3D%3D')    # 사용자 인증키
queryParams = '?' + urlencode(    # get 방식으로 쿼리를 분리하기 위해 '?'를 넣은 것이다. 메타코드 아님.
    {
        quote_plus('ServiceKey') : My_API_Key,    # 필수 항목 1 : 서비스키 (본인의 서비스키)
        quote_plus('LAWD_CD') : '11110',          # 필수 항목 2 : 지역코드 (법정코드목록조회에서 확인)
        quote_plus('DEAL_YMD') : '201512'         # 픽수 항목 3 : 계약월
     }
)

response = requests.get(xmlUrl + queryParams).text.encode('utf-8')
xmlobj = bs4.BeautifulSoup(response, 'lxml-xml')
print(xmlobj)