import requests



def get_str(string, inicio, fim):    
    text = string.split(inicio)[1]
    text = text.split(fim)[0]
    return text

def PegarPost(headers):
    url = 'http://www.naoentreaki.com.br/api/v1/posts/top/?order=semana&allowNsfw=false&limit=20&random=true'
    resp = requests.get(url, headers=headers).text
    image = get_str(resp, '{"url":"', '?') 
    return image

headers = {'Host':'www.naoentreaki.com.br', 
'Connection':'keep-alive', 
'X-Requested-With':'XMLHttpRequest', 
'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; LG-K430) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36', 
'Referer':'http://www.naoentreaki.com.br/top/', 
'Accept-Encoding':'gzip,deflate'} 





