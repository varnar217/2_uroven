import logging
import settings
import ephem as ephe
import datetime
from pprint import pprint
from telegram.ext import Updater , CommandHandler , MessageHandler, Filters
logging.basicConfig(filename='bot.log', level=logging.INFO)

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)



def wordcount_to_me(update, context):
    print('wordcount_rub')
    user_text = str(update.message.text)
    print(user_text)
    if len(user_text)==0:
        update.message.reply_text("Пустая строка")
    else:
        numbrt_text=user_text[1:]
        numbrt_text_2=numbrt_text.split(' ')

        nummber_Col=0
        for i in range(1,len(numbrt_text_2),1):
            if numbrt_text_2[i].isnumeric()==False:
                if len((numbrt_text_2[i]))>1:
                    nummber_Col=nummber_Col+1
                elif numbrt_text_2[i] =='Я' or numbrt_text_2[i] =='я'  :

                    nummber_Col=nummber_Col+1
        if nummber_Col==1:
            update.message.reply_text(f"В строке одно слово")
        elif 2<=nummber_Col and 2<=nummber_Col<5:
            update.message.reply_text(f"В строке {nummber_Col} слова")
        elif nummber_Col!=0:
            update.message.reply_text(f"В строке {nummber_Col} слов")
        else:
            update.message.reply_text(f"В строке нет слов")


def next_full_moon_to_me(update, context):
    user_text = str(update.message.text)
    user_text_2=user_text.split()
    user_text_3=user_text_2[1:]
    if len(user_text_3)==0:
        update.message.reply_text("Пустая строка")
    else:
        for strok in user_text_3:
            strokk=strok.split('-')
        if len(strokk)!=3:
            update.message.reply_text("Не правельная дата")
        if len(strokk[0])!=4:
            update.message.reply_text("Не правелььный год")
            if len(strokk[2])>2:
                update.message.reply_text("Не правелььный месяц")
            if len(strokk[1])>2:
                update.message.reply_text("Не правелььный день")


        user_text_4=''
        for strok in user_text_3:

            user_text_4=strok.replace('-','/')

        data_1=ephe.date(user_text_4)

        update.message.reply_text(ephe.next_full_moon(data_1))





def get_plane(update, context):
    print('planet_rub')
    user_text = str(update.message.text)


    #user_text_2=user_text.split(' ')


    now= datetime.datetime.now()
    a =str(now.year)+'/'+str(now.month)+'/'+str(now.day)
    print('data =',a)
    if user_text_2[1]== 'Mars':
        mars=ephe.Mars(a)
        constellation =  ephe.constellation (mars)
        update.message.reply_text((constellation))

    elif user_text_2[1]== 'Mercury':
        mars=ephe.Mercury(a)
        constellation =  ephe.constellation (mars)
        update.message.reply_text((constellation))

    elif user_text_2[1]== 'Venus':
        mars=ephe.Venus(a)
        constellation =  ephe.constellation (mars)
        update.message.reply_text((constellation))

    elif user_text_2[1]== 'Jupiter':
        mars=ephe.Jupiter(a)
        constellation =  ephe.constellation (mars)
        update.message.reply_text((constellation))

    elif user_text_2[1]== 'Saturn':
        mars=ephe.Saturn(a)
        constellation =  ephe.constellation (mars)
        update.message.reply_text((constellation))

    elif user_text_2[1]== 'Uranus':
        mars=ephe.Uranus(a)
        constellation =  ephe.constellation (mars)
        update.message.reply_text((constellation))


    elif user_text_2[1]== 'Neptune':
        mars=ephe.Neptune(a)
        constellation =  ephe.constellation (mars)
        update.message.reply_text((constellation))

    elif user_text_2[1]== 'Pluto':
        mars=ephe.Pluto(a)
        constellation =  ephe.constellation (mars)
        update.message.reply_text((constellation))

    elif user_text_2[1]== 'Sun':
        #print('the Sun_rubb',a)

        mars=ephe.Sun(a)
        #print(dir(ephe))
        constellation =  ephe.constellation (mars)#ephem.constellation(mars)
        #print(constellation,'\t ' ,type(constellation) )

        update.message.reply_text((constellation))


    elif user_text_2[1]== 'Moon':
        mars=ephe.Moon(a)
        constellation = ephem.constellation(mars)
        update.message.reply_text(constellation)
    else:
        update.message.reply_text('я не знаю это планеты ')


    #a_name_palnet=ephem.star(str(user_text_2[1]))
    #print(a_name_palnet.name)


    #bb=getattr(ephem, str(user_text_2[1]))
    #a1=(bb)
    #print(a)

    #bb_new=bb(a)

    #pprint('!!!!=',[name for _0, _1, name in ephem._libastro.builtin_planets()])
    #b=(ephem._libastro.builtin_planets())


    #print(a)
    #for ar in b:
        #print(ar)

    #if user_text_2 == 'Mars':
        #mars = ephem.Mars(a)
    #elif user_text_2 == 'Mars':





    #pprint('!!!!=',ephem._libastro.builtin_planets())
    #update.message.reply_text('user_text=',user_text)


    #pass

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')


def main():
    print('run bbot')
    #print(dir(ephe))


    mybot=Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_plane))
    dp.add_handler(CommandHandler("wordcount", wordcount_to_me))
    dp.add_handler(CommandHandler("next_full_moon", next_full_moon_to_me))


    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info("Бот стартовал")

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":

    main()
