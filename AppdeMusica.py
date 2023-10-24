from pygame import mixer
from playMusica import playMusica

cores = {'limpa': '\033[m',
         'ciano': '\033[0;0m',
         'verde': '\033[1;32m',
         'vermelho': '\033[0;31m',
         'vermelhoBold': '\033[1;31m',
         'azul': '\033[0;36m',
         'amarelo': '\033[1;33m',
         'branco': '\033[1;97m'
         }
mixer.init()
playlist = []
playlist_queue = []
pasta = 'musicas/'


class MP3:
    def __init__(self, opcao):
        self.opcao = opcao

    def adicionarMusica(self):
        playlist.append(input('Escolha a música para ser adicionada: '))

    def pausar(self):
        mixer.music.pause()

    def despausar(self):
        mixer.music.unpause()


def titulos(titulo):
    print(
        f'{cores["azul"]}-=-' * 15 + f'{cores["amarelo"]}{titulo}{cores["limpa"]}' + f'{cores["azul"]}-=-{cores["limpa"]}' * 15)


def bemVindo():
    print(
        f'\n{cores["vermelho"]}Seja Bem-Vindo a Playlist de música! Espero que se divirta com as músicas em catálogo =) '
        f'Em breve terá mais músicas...{cores["limpa"]}')


def menu():
    print(f"""
{cores["verde"]}1  {cores["ciano"]}MeuCafofo-JoãoGomes               {cores["verde"]}6  {cores["ciano"]}WIU - Oração               {cores["verde"]}11 {cores["ciano"]}Coldplay - A Sky Full Of Stars       
{cores["verde"]}2  {cores["ciano"]}Dengo-JoãoGomes                   {cores["verde"]}7  {cores["ciano"]}Lil Whind - Tempo
{cores["verde"]}3  {cores["ciano"]}FarWay-Nickelback                 {cores["verde"]}8  {cores["ciano"]}Lil Whind - Mó Tristeza 
{cores["verde"]}4  {cores["ciano"]}NeverGonnaBeAlone-Nickelback      {cores["verde"]}9  {cores["ciano"]}Lil Whind - Mãe  
{cores["verde"]}5  {cores["ciano"]}IronMan-BlackSabbath              {cores["verde"]}10 {cores["ciano"]}Tô sem você - João Gomes
""")

    titulos('Comandos do programa')
    print(f"""
{cores["verde"]}Pausar {cores["limpa"]}- Pausar a música
{cores["verde"]}Despausar {cores["limpa"]}- Voltar a reproduzir a música
{cores["verde"]}Adicionar {cores["limpa"]}- Adicionar uma música na fila    
{cores["verde"]}Play {cores["limpa"]}- Começar a música
{cores["verde"]}Fim {cores["limpa"]}- Finalizar o programa
""")


bemVindo()
titulos('Playlist de música')
menu()
while True:
    print(f'{cores["vermelho"]}Fila de Reprodução:{cores["limpa"]} {playlist}')
    mp3 = MP3(input(f'\n{cores["branco"]}Digite sua escolha: {cores["limpa"]}').strip().upper())
    if mp3.opcao == 'ADICIONAR':
        mp3.adicionarMusica()
    if mp3.opcao == 'PAUSAR':
        mp3.pausar()
    if mp3.opcao == 'DESPAUSAR':
        mp3.despausar()
    if mp3.opcao == 'FIM':
        print(f'{cores["vermelhoBold"]}Programa finalizado com sucesso!'
              f'\n{cores["amarelo"]}Espero que tenha gostado da playlist =)')
        break
    if mp3.opcao == 'PLAY':
        playMusica(playlist)

    if mp3.opcao == '1':
        playlist.append(f"{pasta}MeuCafofo-JoãoGomes.mp3")
    if mp3.opcao == '2':
        playlist.append(f"{pasta}Dengo-JoãoGomes.mp3")
    if mp3.opcao == '3':
        playlist.append(f"{pasta}FarWay-Nickelback.mp3")
    if mp3.opcao == '4':
        playlist.append(f"{pasta}NeverGonnaBeAlone-Nickelback.mp3")
    if mp3.opcao == '5':
        playlist.append(f"{pasta}IronMan-BlackSabbath.mp3")
    if mp3.opcao == '6':
        playlist.append(f"{pasta}WIU - Oração.mp3")
    if mp3.opcao == '7':
        playlist.append(f"{pasta}Lil Whind - Tempo.wav")
    if mp3.opcao == '8':
        playlist.append(f"{pasta}Lil Whind - Mó Tristeza.wav")
    if mp3.opcao == '9':
        playlist.append(f"{pasta}Lil Whind - Mãe.wav")
    if mp3.opcao == '10':
        playlist.append(f"{pasta}Tô sem você  - João Gomes.mp3")
    if mp3.opcao == '11':
        playlist.append(f"{pasta}Coldplay - A Sky Full Of Stars.mp3")
