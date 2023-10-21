import pygame

print('\n\033[0;31mSeja Bem-Vindo a Playlist de música! Espero que se divirta com as músicas em catálogo =) '
      'Em breve terá mais músicas...')
print('\033[0;36m-=-' * 15 + '\033[1;33mPlaylist de música\033[m' + '\033[0;36m-=-\033[m' * 15)
pygame.init()
pygame.mixer.init()
cores = {'limpa': '\033[m',
         'ciano': '\033[0;0m',
         'verde': '\033[1;32m'}


def adicionarmusica():
    if adicionar == '1':
        pygame.mixer.music.queue("musica/MeuCafofo-JoãoGomes.mp3")
    if adicionar == '2':
        pygame.mixer.music.queue("musica/Dengo-JoãoGomes.mp3")
    if adicionar == '3':
        pygame.mixer.music.queue("musica/FarWay-Nickelback.mp3")
    if adicionar == '4':
        pygame.mixer.music.queue("musica/NeverGonnaBeAlone-Nickelback.mp3")
    if adicionar == '5':
        pygame.mixer.music.queue("musica/IronMan-BlackSabbath.mp3")
    if adicionar == '6':
        pygame.mixer.music.queue("musica/WIU - Oração.mp3")
    if adicionar == '7':
        pygame.mixer.music.queue("musica/Lil Whind - Tempo.wav")
    if adicionar == '8':
        pygame.mixer.music.queue("musica/Lil Whind - Mó Tristeza.wav")
    if adicionar == '9':
        pygame.mixer.music.queue("musica/Lil Whind - Mãe.wav")
    if adicionar == '10':
        pygame.mixer.music.queue("musica/Tô sem você  - João Gomes.mp3")
    if adicionar == '11':
        pygame.mixer.music.queue("musica/Coldplay - A Sky Full Of Stars.mp3")


def pausar():
    pygame.mixer.music.pause()


def despausar():
    pygame.mixer.music.unpause()


def menu():
    print(f'{cores["verde"]}1  {cores["ciano"]}MeuCafofo-JoãoGomes', end=' ' * 5)
    print(f'{cores["verde"]}2  {cores["ciano"]}Dengo-JoãoGomes', end=' ' * 16)
    print(f'{cores["verde"]}11 {cores["ciano"]}Coldplay - A Sky Full Of Stars')
    print(f'{cores["verde"]}3  {cores["ciano"]}FarWay-Nickelback', end=' ' * 7)
    print(f'{cores["verde"]}4 {cores["ciano"]} NeverGonnaBeAlone-Nickelback')
    print(f'{cores["verde"]}5  {cores["ciano"]}IronMan-BlackSabbath', end=' ' * 4)
    print(f'{cores["verde"]}6  {cores["ciano"]}WIU - Oração')
    print(f'{cores["verde"]}7  {cores["ciano"]}Lil Whind - Tempo', end=' ' * 7)
    print(f'{cores["verde"]}8  {cores["ciano"]}Lil Whind - Mó Tristeza')
    print(f'{cores["verde"]}9  {cores["ciano"]}Lil Whind - Mãe', end=' ' * 9)
    print(f'{cores["verde"]}10 {cores["ciano"]}Tô sem você - João Gomes')

    print('\033[0;36m-=-' * 15 + '\033[1;33mComandos do programa' + '\033[0;36m-=-\033[m' * 15)
    print(f'{cores["verde"]}Pausar {cores["limpa"]}- Pausar a música'
          f'\n{cores["verde"]}Despausar {cores["limpa"]}- Voltar a reproduzir a música'
          f'\n{cores["verde"]}Adicionar {cores["limpa"]}- Adicionar uma música na fila'
          f'\n{cores["verde"]}Fim {cores["limpa"]}- Finalizar o programa')


menu()
while True:
    op = input('\n\033[1;97mDigite sua escolha: \033[m').strip().upper()
    if op == 'ADICIONAR':
        adicionar = input('Escolha a música para ser adicionada: ')
        adicionarmusica()
    if op == 'PAUSAR':
        pausar()
    if op == 'DESPAUSAR':
        despausar()
    if op == '1':
        pygame.mixer.music.load("musica/MeuCafofo-JoãoGomes.mp3")
        pygame.mixer.music.play(0)
    if op == '2':
        pygame.mixer.music.load("musica/Dengo-JoãoGomes.mp3")
        pygame.mixer.music.play(0)
    if op == '3':
        pygame.mixer.music.load("musica/FarWay-Nickelback.mp3")
        pygame.mixer.music.play(0)
    if op == '4':
        pygame.mixer.music.load("musica/NeverGonnaBeAlone-Nickelback.mp3")
        pygame.mixer.music.play(0)
    if op == '5':
        pygame.mixer.music.load("musica/IronMan-BlackSabbath.mp3")
        pygame.mixer.music.play(0)
    if op == '6':
        pygame.mixer.music.load("musica/WIU - Oração.mp3")
        pygame.mixer.music.play(0)
    if op == '7':
        pygame.mixer.music.load("musica/Lil Whind - Tempo.wav")
        pygame.mixer.music.play(0)
    if op == '8':
        pygame.mixer.music.load("musica/Lil Whind - Mó Tristeza.wav")
        pygame.mixer.music.play(0)
    if op == '9':
        pygame.mixer.music.load("musica/Lil Whind - Mãe.wav")
        pygame.mixer.music.play(0)
    if op == '10':
        pygame.mixer.music.load("musica/Tô sem você  - João Gomes.mp3")
        pygame.mixer.music.play(0)
    if op == '11':
        pygame.mixer.music.load("musica/Coldplay - A Sky Full Of Stars.mp3")
        pygame.mixer.music.play(0)
    if op == 'FIM':
        print('\033[1;31mPrograma finalizado com sucesso!'
              '\n\033[1;33mEspero que tenha gostado da playlist =)')
        break
