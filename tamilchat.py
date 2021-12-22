import sys,os
import time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
import dictionary as d
from translate import Translator as t
#if any changes in import update in requirements.txt



def translateToTamil(content):
    translator=t(from_lang="english",to_lang="tamil")
    print("translating.....")
    translation=translator.translate(content)
    return translation



TOKEN =''#enter your bot token here

bot = telepot.Bot(TOKEN)

diction_voice={

  'hi':open('hi baymax.aac','rb'),
'hello':open('hello baymax.aac','rb'),
'hey':open('hey baymax.aac','rb'),
'bye':open('end wishes.aac','rb')
}




photo_url='https://dejpknyizje2n.cloudfront.net/svgcustom/clipart/preview/cute-smile-emoji-sticker-29786-300x300.png'
sticker_url='https://thumbs.gfycat.com/SpotlessGrippingEyas-small.gif'
#audio=open('bad_guy_remix_bgm.mp4','rb')



def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    if content_type == 'text':
        if(msg['text']=='send me a pic' or msg['text']=='send me a photo'):
            bot.sendPhoto(chat_id,photo_url)
        elif(msg['text'] == '/links_4'):
            bot.sendMessage(chat_id, 'select class',
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                    [KeyboardButton(text="hi"), KeyboardButton(text="hello"),KeyboardButton(text="bye")]]))
        
        

        elif(msg['text'] == '/voice_hi'):
            bot.sendMessage(chat_id,'uploading')
            bot.sendVoice(chat_id,diction_voice['hi'])
            print("voice upload success")
        elif(msg['text'] == '/voice_hello'):
            bot.sendMessage(chat_id,'uploading')
            bot.sendVoice(chat_id,diction_voice['hello'])
            print("voice upload success")
        elif(msg['text'] == '/voice_hey'):
            bot.sendMessage(chat_id,'uploading')
            bot.sendVoice(chat_id,diction_voice['hey'])
            print("voice upload success")
        elif(msg['text'] == '/voice_bye'):
            bot.sendMessage(chat_id,'uploading')
            bot.sendVoice(chat_id,diction_voice['bye'])
            print("voice upload success")
        elif(msg['text']=='/help'):
            bot.sendMessage(chat_id,'welcome to the help section')
            bot.sendMessage(chat_id,'i was certainly programmed for some commands')
            bot.sendMessage(chat_id,'commands like:hi\n hello\n bye\n hey\n what is your name?\nhow r u\niam also fine\nhow are you?\nwho is your admin\nwho is ur boss\n who is no 45\n hey whats up!! ')
            bot.sendMessage(chat_id,'who is rollno \n class details-4 \n class details-5 \n /links_4 \n')
            bot.sendMessage(chat_id,'EXTRA COMMANDS LIKE \n /voice_hi\n/voice_hello\n/voice_hey\n/voice_bye\n send me a pic\n send me a photo')
          #  bot.sendMessage(chat_id,'currently voice command is in progress so pls try again later')
        



        else:
            a=str(msg['text'])
            print(str(a))
            if(str(msg['text'].lower()) in str(d.dictionary)):
                res=d.dictionary[msg['text'].lower()]
                print(res)
                res=translateToTamil(res)
                print(res)
                bot.sendMessage(chat_id,res)
            else:
                bot.sendMessage(chat_id,"sorry i couldn't understand")
                value=input("enter the value")
                ans=","+"'"+a+"'"+":"+"'"+value+"'"
                print(ans)
                
                file=open('updates.txt','a')
                file.write(ans+"\n"+"\n")
                file.close



                bot.sendMessage(chat_id,"the word has been updated")

                print("please restart the server to take action of the changes made")
                #exit(0)


            
    if content_type =='sticker':
        bot.sendVideo(chat_id,sticker_url)
        bot.sendMessage(chat_id,"cool and be happy i'm here to help")

    if content_type =='document':
        my_id='1080110325'
        bot_msg=bot.sendMessage(chat_id,'msg forwarded')
        bot.forwardMessage(my_id,chat_id['from']['id'],bot_msg['message_id'])

    #print(msg['text'])

MessageLoop(bot,handle).run_as_thread()


print ('Listening ...')


# Keep the program running
while True:
    time.sleep(10)

