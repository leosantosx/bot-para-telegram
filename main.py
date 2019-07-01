import telepot, time    
from telepot.loop import MessageLoop
from meme import PegarPost
from bin import BinChecker
from locap import locapIp
from tradutor import traduzirTexto
from image import run

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':        
        text = msg['text'].upper().strip()
        
        if text.startswith('/START') :
            bot.sendMessage(chat_id, '*Digite:*\n /comandos - para ver comandos' , parse_mode='Markdown')
            
        if text.startswith('/COMANDOS'):
            comandos = "🛠 *Lista de Comandos*\n\n• *FOTOS:* /fotos baixar imagens\n\n• *IP:* /find - Consultar ip\n\n• *BIN:* /bin - consultar uma bin\n\n• *TR:* /tr traduzir um texto"
            bot.sendMessage(chat_id, comandos,  parse_mode= 'Markdown') 
            
        if text.startswith('/MEME'):
            image = PegarPost() 
            bot.sendPhoto(chat_id, image)
            
        if text.startswith('/FIND'):
            try:
                ip = text[6:]          
                if ip and '@DARKMINE' not in text:                
                    locap = locapIp(ip)
                    bot.sendMessage(chat_id, locap[0],  parse_mode= 'Markdown')                    
                    bot.sendPhoto(chat_id, locap[1], '@Darkmine_bot')
                else:
                    data = '*Ip Location* - Localizar IP ou Site\n\nFormato:\n/ip ip ou hostname' 
                    bot.sendMessage(chat_id, data,  parse_mode= 'Markdown') 
            except Exception as erro:
                print(erro) 
                data = '*Endereço de IP inválido!*'
                bot.sendMessage(chat_id, data,  parse_mode= 'Markdown') 
                      
        if text.startswith('/BIN'):
            resp = BinChecker(text) 
            bot.sendMessage(chat_id, resp, parse_mode= 'Markdown')
            
            
        if text.startswith('/TR'):
            texto = text[4:]
            if texto and '@DARKMINE' not in text:           
                resp = traduzirTexto(texto)
            else:
                resp = "*Modo de uso:*\n\n /tr *Texto* - Para fazer a tradução de algum texto"
            bot.sendMessage(chat_id, resp, parse_mode= 'Markdown')    
        
              
        if text.startswith('/ID'):
            nome = msg['from']['first_name']
            user = msg['from']['username'] 
            resp = 'Nome: {}\nUsuário: @{}\nId: {}'.format(nome, user, chat_id)
            bot.sendMessage(chat_id,resp)
                    
        if text.startswith('/FOTOS'):
            if text[7:] and '@DARKMINE' not in text:
                text = text[7:].split(' ')
                num = int(text[len(text) - 1]) 
                query = '+'.join(text[0:len(text)-1])
                lista = run(query, num) 
                for line in lista:
                    if line == lista[len(lista) - 1]:
                        bot.sendPhoto(chat_id, line, '@Darkmine_bot') 
                    else:
                        bot.sendPhoto(chat_id, line) 
            else:
                resp = "*Modo de uso:*\n\n/fotos *busca* *quantidade*\n\nEx: /fotos bolsonaro 5"
                bot.sendMessage(chat_id, resp, parse_mode='Markdown') 
         
            
            
            

bot = telepot.Bot('TOKEN') 
MessageLoop(bot, handle).run_as_thread()

while True:
    time.sleep(10)

