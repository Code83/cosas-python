## Bot para seguir a seguidores de una cuenta X
## Lo primero es instalar instabot (pip install instabot)

from instabot import bot

v_bot = bot()
#Acá van los datos de la cuenta que se usará para aumentar las cuentas seguidas
v_bot.login(username='',password='')
#acá va la cuenta de los usuarios que queremos seguir
v_bot.follow_followers('')
