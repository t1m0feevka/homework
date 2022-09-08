import requests
def decorator(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('Час виконання : {} секунд.'.format(end-start))
        return return_value
    return wrapper

@decorator
def fetch_webpage(url):
    import requests
    webpage = requests.get(url)
    return webpage.text
webpage = fetch_webpage('https://google.com')
webpage1 = fetch_webpage('https://www.ssconsulting.com.ua')
print(webpage)
print(webpage1)
from googlesearch import search
query = 'news'
for i in search(query, tld='co.in', num=10, stop=10, pause=2):
    print(i)



