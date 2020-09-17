import requests

payload = {'username': 'joe', 'password': 'testing'}
r = requests.post('https://httpbin.org/post', data=payload)

# with open('comic.png', 'wb') as f:
#     f.write(r.content)
# print(r.status_code)
# print(r.headers)
r_dict = r.json()

print(r_dict['form'])
