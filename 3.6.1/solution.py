import requests
print(len(requests.get('https://stepic.org/media/attachments/course67/3.6.2/699.txt').text.splitlines()))