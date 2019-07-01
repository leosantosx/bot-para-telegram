import requests, json

def BinChecker(text):
    
    if len(text) == 11:
        bin = text[5:]
        url = 'https://binlist.io/lookup/'+bin
        resp = requests.get(url).json()         
        success = resp['success']
        
        if success:    
            bandeira = resp['scheme']
            tipo = resp['type']
            nivel = resp['category']
            banco = resp['bank']['name']
            pais = resp['country']['name']
            emoji = resp['country']['emoji']
            data = ' *Bin*: '+bin+'\n*Bandeira:* '+bandeira+'\n*Tipo:* '+tipo+'\n*Nível:* '+nivel+'\n*Banco:* '+banco+'\n*País:* '+pais+' '+emoji 
        else:
            data = '*Bin não encontrada!!*'    
    else:
        data = '*BIN Checker* - Verifica as informações do Cartão atráves dos 6 primeiros digítos do mesmo.\n*Formato:* \n  • /bin 552300' 
    
    return data



