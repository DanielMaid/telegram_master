from telethon.sync import TelegramClient, errors
from time import sleep
from telethon.errors.rpcerrorlist import MessageTooLongError, PeerIdInvalidError
import dbm
from colorama import init, Fore, Back, Style 

print('Наш telegram канал - https://t.me/slivmenss')

init(autoreset=True)



def dbm_base():
	file = dbm.open( 'api.dbm' ,'c')
	try:
		file['api_id']
	except:
		file['api_id'] = input('Введите api_id:')
		file['api_hash'] = input('Введите api_hash:')
	file.close()
	return dbm.open( 'api.dbm' ,'r')
file = dbm_base()
api_id = int(file['api_id'].decode())
api_hash = file['api_hash'].decode()
client = TelegramClient('client', api_id, api_hash)


def dialog_sort(dialog):
    return dialog.unread_count
    
    
def spammer(client):
    def create_groups_list(groups=[]):
        for dialog in client.iter_dialogs():
            if dialog.is_group:
                if dialog.unread_count >= 5:
                    groups.append(dialog) 
        return groups

    with client:
        try:
	        timer = int(input('@slivmenss - Введите время сна между циклами сообщений(в секундах): '))
        except:
        	print(Fore.RED + '@slivmenss - Вводите цифрами, время должно быть в секундах!')
        for m in client.iter_messages('me', 1):
            msg = m
        print(Fore.GREEN + '@slivmenss - Сообщение выбрано:\n', msg)
        while True:
            groups = create_groups_list()
            groups.sort(key=dialog_sort, reverse=True)
            for g in groups[:90]:
                try:
                    client.forward_messages(g, msg, 'me')
                    print(Fore.GREEN + g.name + ' сообщение отправлено! - @slivmenss')
                    
                except errors.ForbiddenError as o:
                    client.delete_dialog(g)
                    if g.entity.username != None:
                        print(Fore.RED + f'Error: {o.message} Аккаунт покинул @{g.entity.username}')
                    else:
                        print(Fore.RED + f'Error: {o.message} Аккаунт покинул {g.name}')
                except errors.FloodError as e:
                	print(Fore.RED + f'Error: {e.message} Ожидание {e.seconds} секунд')
                	sleep(e.seconds)
                except PeerIdInvalidError:
                    client.delete_dialog(g)
                except MessageTooLongError:
                    print(Fore.RED + f'Message was too long ==> {g.name}')                                     
                except errors.BadRequestError as i:
                	print(Fore.RED + f'Error: {i.message}')
                except errors.RPCError as a:
                	print(Fore.RED + f'Error: {a.message}')
            print(Fore.GREEN + 'Рассылка закончена!')
            print(Fore.GREEN + 'Следущая рассылка через: ' + str(timer) + 'сек.' )
            sleep(timer)
            groups.clear()
if __name__ == '__main__':
	spammer(client)
