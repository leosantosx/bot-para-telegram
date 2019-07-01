from googletrans import Translator

def traduzirTexto(texto, lang='pt'):
    translate = Translator()
    t_text = translate.translate(texto,dest=lang).text.capitalize()
    resp =  "*Tradução encontrada:* \n\n" + t_text
    return resp