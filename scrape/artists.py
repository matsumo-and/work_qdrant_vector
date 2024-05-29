import csv
from bs4 import BeautifulSoup

# HTMLの解析
bsObj = BeautifulSoup(open('sample.html', encoding='utf-8'),"html.parser")

# 要素の抽出
content_list = bsObj.find_all("li", {'class': 'listItem_main__gsJuN'})


csv_list = [
    ["rank", "title", "detail"]
]
# 必要な要素の取り出し
for content in content_list:
    
    anchor = content.find("h2").find("a")
    if anchor == None:
        continue
    
    # artist name
    title = anchor.get("title")
    
    # ranking
    rank = content.find("strong", class_='RankBox_main__YJnmM').find("div").text
    
    # text
    text_block = content.find("div", class_='richText_container__Kvtj0')
    text = ""
    if text_block.find("p") == None:
        text = text_block.find("span").text
    else:
        text = text_block.find("p").text
        
    # append to list
    csv_list.append([rank, title, text])

# export
csv_path = r"output.csv"

with open(csv_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(csv_list)