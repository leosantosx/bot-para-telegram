import requests, sys, re

def get_str(string, inicio, fim):
    text = string.split(inicio)[1]
    text = text.split(fim)[0]
    return text
    
def requestUrl(ip):
    url = 'https://www.localizaip.com.br/localizar-ip.php?ip={0}'.format(ip)
    headers = {'Host':'www.localizaip.com.br', 'Connection':'keep-alive', 'Upgrade-Insecure-Requests':'1', 
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; LG-K430) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36', 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
        'Referer':'https://www.localizaip.com.br/localizar-ip.php?ip=172.217.28.4', 'Accept-Encoding':'gzip, deflate, br', 'Accept-Language':'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7', 'Cookie':'mobile=1'}
    resp = requests.get(url, headers=headers)
    return resp
 
    
def locapIp(ip):
         
    resp = requestUrl(ip) 
    if resp.status_code == requests.codes.ok:
        if re.search('Invalid', resp.text):
            data = '*Endereço de IP inválido!*'
            return data        
        else:
            resp = resp.text
            ip_site = get_str(resp, 'id="ip" value="', '"') 
            latitude = get_str(resp, "'latitude' =>", ",") 
            longitude = get_str(resp, "'longitude' =>", ",") 
            country = get_str(resp,"'countryName' => '","'")
            region = get_str(resp,"'region' => '","'") 
            city = get_str(resp,"'city' => '","'")
            src = get_str(resp,"'src' => '","'")
            isp = get_str(resp,"'isp' => '","'")
            ip_reverso = get_str(resp,'IP-Reverso:<b>','</b>')              
            data = ['*IP: *'+ip_site+'\n*País:* '+country+'\n*Estado: *'+region+'\n*Cidade:* '+city+'\n*Provedor:* '+isp+'\n*IP reverso:* '+ip_reverso+'\n*Latitude: *'+latitude+'\n*Longitude: *'+longitude+'\n*Src: *'+src]
            if re.search('maps.googleapis',resp):
                img = get_str(resp, '<img style="border-radius: 15px;" src="', '"') 
                data.append(img)
            return data
    else:
        data = '*Ops temos um erro de conexão!*' 
        return data
    