import sys
import telepot
from pprint import pprint
import keyword
from telepot.loop import MessageLoop
from random import randint
#keyword.iskeyword("print")

bot = telepot.Bot("335422547:AAHU-CG3xGWRZYg7wwbRy8Zg37j2smTTgr4")

def trasforma(s):
    a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    b=""
    i=1
    while i<len(s):
        b+=s[i]
        i=i+1
    if s[0] in a:
        return s[0].upper()+""+b
    else:
        return s[0].lower()+""+b



def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    pprint(msg)

    a=['goodmorning','ola','ou','good morning','guten morgen','morgen','ciao','hola','buongiorno','hasta']
    b=['ciao','Buongiorno. Ci vorrebbe una sveglia che rilascia profumo di cornetto.','buongiornissimo kafèéèééé','ciaone', 'buongiorno un cazzo', 'Saluti a mammt', 'Aò','Buongiorno principessina','Popolo finalmente si è svegliato','Sei così gentile da salutare']
    
    d=['tette','tits','zinne','minne','bocce','escile','minnazze']
    e=['http://boobsnbuns.com/wp-content/uploads/2015/10/hot-tits-and-buns-compilation-by-untitled1.jpeg', 'https://s-media-cache-ak0.pinimg.com/736x/f0/f8/a9/f0f8a9d5d88b2003af64f28eb6d0dded.jpg', 'http://www.pandesiaworld.com/wp-content/uploads/Cara-Steel-sexy-model-3.jpg', 'http://4.bp.blogspot.com/-8jn6qa8My3w/UaePh6o7SII/AAAAAAAAB0Q/sRSEumkTNXE/s1600/suicide-girls-cute-sexy-boobs-tits-nipples-topless-naked-tattoos-18-751800.jpg', 'https://s-media-cache-ak0.pinimg.com/736x/28/1a/1b/281a1b3d7f00edd2ad1741beaf40f3b3.jpg', 'http://www.nudelas.com/posts/gypsyy-suicide-girl/gypsyy-suicide-girl-15.jpg', 'http://www.pandesiaworld.com/wp-content/uploads/2014/11/suicide-girls-a1-mille-266x400.jpg', 'http://redbust.com/stuff/gypsyy/gypsyy-red-bra-bedroom-suicide-girls-18-800x1200.jpg', 'http://cdn4.images.motherlessmedia.com/images/15100C6.jpg?fs=opencloud','http://68.media.tumblr.com/552aba3514f86e846ec025da42f42f2b/tumblr_nx3cszU03z1regb1io8_500.jpg','http://bustybigtits8.com/wp-content/uploads/2013/07/Big-Tits-0071.jpg','https://s-media-cache-ak0.pinimg.com/736x/0c/8e/50/0c8e50639fadd05d5e736bebd7b06ce0--toples-sexy-women.jpg']
    

    f=['culo','culi','sedere']
    g=['http://orig01.deviantart.net/69a7/f/2013/299/3/5/6_by_darkressxx-d6rynfe.jpg','http://data.whicdn.com/images/59559418/original.jpg','http://i.ytimg.com/vi/ThQ-hP7k7BE/maxresdefault.jpg','http://cdn.niketalk.com/5/54/496x744px-LL-545a6dbd_tumblr_mj72bg4W9F1rf0k9co1_500.jpeg','http://68.media.tumblr.com/45f800d219f9ac489887a76dc682bd25/tumblr_n449dn4AjQ1rt0nvgo1_1280.jpg', 'http://cdn4.images.motherlessmedia.com/images/17264D4.jpg?fs=opencloud', 'http://www.nudelas.com/posts/fishball-and-ladyviolet-suicide-girls-passo-a-due/fishball-and-ladyviolet-suicide-girls-54.jpg','https://s-media-cache-ak0.pinimg.com/originals/45/d9/ec/45d9ecccc6d7099050ebaf984306fc20.jpg','http://allswalls.com/images/hot-brunette-wallpaper-5.jpg','http://www.fraccata.com/wp-content/uploads/2015/04/5_big.jpg']
    
    h=['dio','cristo','madonna','gesù','gesu','bestemmio','bestemmia']
    j=['MADONNA ACCHIAPPAFANTASMI','DIO LUPO','Signor Magi son tartufi questi?','Buttana Buttarazzi','SE NON BESTEMMIO GUARDA...','Gesù non fa l amore, che fa Gesù?', 'PORCACCIO IDDIO', 'DIO SERPENTE', 'Gesù Cristo ara cruci','Inculo a tutti i santi', 'MADONNA SCATENATA']

    lion=['Prego','Ma Pornhub è chiuso?','Ma XVideos è chiuso?','Chapa qui','Here we are...','Che originalità in questo gruppo madonna laida. Ringraziate','Belle minne e culi per voi buzzurri','Non è troppo presto per le seghe?','Me la scoperei...'+'\n'+'Ma volentieri!','Ma quanto è bella la figa','Di birra e di legn...No! Il baffo di legna s impregna di fregn...Cristo vabbè avete capito']

    Aiuto=['help']
    info=['info']
    
    name = msg["from"]["first_name"]

    c=randint(0,len(b)-1)
    x=randint(0,len(e)-1)
    w=randint(0,len(g)-1)
    y=randint(0,len(j)-1)
    lion2=randint(0,len(lion)-1)
    #if content_type == 'text' and msg['text'] in a or content_type == 'text' and trasforma(msg['text']) in a:
    #    bot.sendMessage(chat_id, b[c]+" " +name+" "+sur)
    #elif content_type == 'document':
    #    bot.sendMessage(chat_id, 'Sei un ribellino')
    #elif content_type == 'text' and msg['text'] == 'ciao' or content_type == 'text' and msg['text'] == trasforma('ciao'):
    #   bot.sendMessage(chat_id, 'ciao '+name+" "+sur)

    ok=False
    for i in a:
        if i in msg['text'] or trasforma(i) in msg['text']:
            ok=True
    if ok is True:
        bot.sendMessage(chat_id, b[c]+" " +name)
        
#####TETTE###########
    ok2=False
    for i in d:
        if i in msg['text'] or trasforma(i) in msg['text']:
            ok2=True
    if ok2 is True:
        bot.sendPhoto(chat_id,e[x])
        bot.sendMessage(chat_id,lion[lion2])
        
#####CULI###########
    ok3=False
    for i in f:
        if i in msg['text'] or trasforma(i) in msg['text']:
            ok3=True
    if ok3 is True:
        bot.sendPhoto(chat_id,g[w])
        bot.sendMessage(chat_id,lion[lion2])
        
####BESTEMMIE####
    ok4=False
    for i in h:
        if i in msg['text'] or trasforma(i) in msg['text']:
            ok4=True
    if ok4 is True :
        bot.sendMessage(chat_id, j[y])
####AIUTO####
    ok5=False
    for i in Aiuto:
        if i in msg['text'] or trasforma(i) in msg['text']:
            ok5=True
    if ok5 is True :
        bot.sendMessage(chat_id, 'Madonna se è semplice:'+'\n'+'per informazioni scrivi info;'+'\n'+ 'scrivi tette ed avrai tette;'+'\n'+ 'scrivi culo ed avrai culo;'+'\n'+ 'salutami e sarò garbato con te tanto da salutarti;'+'\n'+ 'non nominare il nome di dio o la sua famigliola invano sennò...')
####INFO####
    ok6=False
    for i in info:
        if i in msg['text'] or trasforma(i) in msg['text']:
            ok6=True
    if ok6 is True :
        bot.sendMessage(chat_id,'Alessandro Ascione 29/11/1992 matricola:XXXX a.ascione2@gmail.com')
        bot.sendMessage(chat_id,'Michele Angelo Perrone 11/09/1992 matricola:478396 mikangelo.perrone@gmail.com')
        bot.sendMessage(chat_id,'Massimiliano Palumbo 23/05/1992 matricola:478406 m.palumbo92@gmail.com')
        bot.sendMessage(chat_id,'Diego Rizzardini 08/06/1991 matricola:XXXX rizzardini.diego.8.6.91@gmail.com')
        bot.sendMessage(chat_id,'Vincenzo Zotti 27/04/1992 matricola:XXXX vincenzozotti@msn.com ')

                





bot.message_loop(handle)
#if content_type == 'text':
 #       name = msg["from"]["first_name"]
 #      txt = msg['text']
   #     bot.sendMessage(chat_id, 'ciao %s, sono un bot molto stupido!')







import time
while 1:
    time.sleep(2)

