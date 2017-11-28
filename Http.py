import  urllib.request
response = urllib.request.urlopen("https://www.yrw.com/products/queryProjectList?currentPage=1&pageSize=8")
print(response.read())