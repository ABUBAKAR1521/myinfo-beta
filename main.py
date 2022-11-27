import telebot as t
import time as ti
tok = "5826163474:AAGqJ9DAsMPEBQAkUXaqWndNTxH_9Rp_0SQ"

bot = t.TeleBot(tok)

@bot.message_handler(commands =  ['start'])
def reply_to(message):
    hb = message.from_user.first_name
    nm = "ʜᴇʟʟᴏ {} ᴍʏsᴇʟғ ɪɴғᴏᴍʏ ẞ ɪᴍ ʟɪᴋᴇ ʏᴏᴜʀ ᴘᴇʀsᴏɴᴀʟ ᴀssɪsᴛᴀɴᴛ ᴄʜᴇᴀᴋ ʜᴇʟᴘ /help ғᴏʀ ᴅᴇᴛᴀɪʟs ᴡʜᴀᴛ ᴄᴀɴ ɪ ᴅᴏ ".format(hb)
    bot.reply_to(message, nm)
    
@bot.message_handler(commands = ['myinfo'])
def reply_to(message):
    fn = message.from_user.first_name
    id = message.from_user.id
    ln = message.from_user.last_name
    fun = message.from_user.first_name
    un = message.from_user.username
    fg = "YOUR PERSONAL INFORMATION PROVIDED BY @Infomy_robot \n \n first name = {}. \n last name = {}. \n username = @{} \n user id = {} \n fullname = {}. \n \n \n ɪғ ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴀ ᴜsᴇʀɴᴀᴍᴇ ʏᴏᴜ ᴄᴀɴɴᴏᴛ ᴜsᴇ ᴛʜɪs ʟɪɴᴋ 👇\n YOUR LINK 🔗 = https://telegram.me/{}   ".format(fn ,ln ,un ,id,  fun , un)
    bot.reply_to(message , fg)
@bot.message_handler(commands = ["pim" , "pin" , "p"])
def pinning(message):
        f = message.reply_to_message.message_id
        cid = message.chat.id
        bot.pin_chat_message(cid , f)
    
@bot.message_handler(commands = ["unpim" , "unpin" , "up"])
def unpinning(message):
    f = message.reply_to_message.message_id
    cid = message.chat.id
    bot.unpin_chat_message(cid , f)
    
@bot.message_handler(commands = ["help"])

def helping(message):
   ggutu = "   нєℓρ ѕє¢тισи \n PIN \n \n pin command works for everyone present in group pin command has three options /p /pim /pin all 3 work same function \n \n similarly UNPIN \n \n unpin command works opposite to ° pin ° when message is pinned bot can unpin the replied message - /unpin /up /unpim \n \n /myinfo gives your all information based on Telegram functions ex - id username name etc \n \n TIME \n as it's a common feature as you know just type /time or /t to cheak current time."
   bot.reply_to(message , ggutu)
   
@bot.message_handler(commands = ["time" ,  "t"])
def time(message):
    tm = ti.ctime()
    tim = " current time in your country #{}".format(tm)
    bot.reply_to(message , tim)
        
bot.polling()

