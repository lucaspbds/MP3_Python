import pygame

cores = {'limpa': '\033[m',
         'ciano': '\033[0;0m',
         'verde': '\033[1;32m',
         'vermelho': '\033[0;31m',
         'azul': '\033[0;36m',
         'amarelo': '\033[1;33m',
         'branco': '\033[1;97m'
         }
pygame.init()
pygame.mixer.init()
playlist = []
playlist_queue = []


class MP3:
    def __init__(self, opcao):
        self.opcao = opcao

    def adicionarMusica(self):
        playlist.append(input('Escolha a música para ser adicionada: '))

    def pausar(self):
        pygame.mixer.music.pause()

    def despausar(self):
        pygame.mixer.music.unpause()


def titulos(titulo):
    print(
        f'{cores["azul"]}-=-' * 15 + f'{cores["amarelo"]}{titulo}{cores["limpa"]}' + f'{cores["azul"]}-=-{cores["limpa"]}' * 15)


def bemVindo():
    print(
        f'\n{cores["vermelho"]}Seja Bem-Vindo a Playlist de música! Espero que se divirta com as músicas em catálogo =) '
        f'Em breve terá mais músicas...{cores["limpa"]}')


def tocarmusica():
    for music in playlist:
        pygame.mixer.music.load(music)
        pygame.mixer.music.play()
        pygame.mixer.music.set_endevent(pygame.USEREVENT)
        while pygame.mixer.music.get_busy():
            pygame.time.wait(100)


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
    op = MP3(input(f'\n{cores["branco"]}Digite sua escolha: {cores["limpa"]}').strip().upper())
    if op == 'ADICIONAR':
        op.adicionarMusica()
    if op == 'PAUSAR':
        op.pausar()
    if op == 'DESPAUSAR':
        op.despausar()
    if op == '1':
        playlist.append("musica/MeuCafofo-JoãoGomes.mp3")
    if op == '2':
        playlist.append("musica/Dengo-JoãoGomes.mp3")
    if op == '3':
        playlist.append("musica/FarWay-Nickelback.mp3")
    if op == '4':
        playlist.append("musica/NeverGonnaBeAlone-Nickelback.mp3")
    if op == '5':
        playlist.append("musica/IronMan-BlackSabbath.mp3")
    if op == '6':
        playlist.append("musica/WIU - Oração.mp3")
    if op == '7':
        playlist.append("musica/Lil Whind - Tempo.wav")
    if op == '8':
        playlist.append("musica/Lil Whind - Mó Tristeza.wav")
    if op == '9':
        playlist.append("musica/Lil Whind - Mãe.wav")
    if op == '10':
        playlist.append("musica/Tô sem você  - João Gomes.mp3")
    if op == '11':
        playlist.append("musica/Coldplay - A Sky Full Of Stars.mp3")
    if op == 'FIM':
        print('\033[1;31mPrograma finalizado com sucesso!'
              '\n\033[1;33mEspero que tenha gostado da playlist =)')
        break
    if op == 'PLAY':
        tocarmusica()
        pygame.mixer.music.play()
    print(f'\033[0;31mFila de Reprodução:\033[m {playlist}')
