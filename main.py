import requests
from bs4 import BeautifulSoup
url = "https://stackoverflow.com/questions/tagged/python"
r = requests.get(url)
ques_lst = []
soup = BeautifulSoup(r.text, 'html.parser')
ques_summary = soup.find_all('div', class_='s-post-summary--content')
for summary in ques_summary:
    question = summary.find(class_='s-link').text
    ques_lst.append(question)
print(*ques_lst, sep = "\n")
    


