# ProjetoFP2 - O Prado

# TAD Posicao:
""""
Os TADS de posição são os responsáveis por definir as posições do prado taic como as posições dos rochedos,
das montanhas, dos predadores e das presas. Estes TADS também são os responsáveis por calcular a próxima posição
que um animal pode tomar consoante a ordem de leitura do prado, seja por valoor númerico ou pelos ponteiros do
relógio.

cria posicao: int × int --> posicao
cria copia posicao: posicao --> posicao
obter pos x : posicao --> int
obter pos y: posicao --> int
eh posicao: universal --> booleano
posicoes iguais: posicao × posicao --> booleano
posicao para str : posicao --> str

Funções de Alto Nível:

obter posicoes adjacentes: posicao --> tuplo
ordenar posicoes: tuplo --> tuplo
"""""

# CONSTRUTORES
def cria_posicao(x, y):                                                    #Esta função cria uma posição, enquanto que
    if isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0:    #a função seguinte cria uma copia dessa posição
        return x, y
    raise ValueError('cria_posicao: argumentos invalidos')


def cria_copia_posicao(p):
    return p[0], p[1]


# SELETORES                                 #Os seletores são as TADS mais fáceis, pois apenas requerem um elemento da posição
def obter_pos_x(p):
    return p[0]


def obter_pos_y(p):
    return p[1]


# RECONHECEDOR                    #Os reconhecedores avaliam o argumento para verificar se está dentro dos paramentros de uma posição.
def eh_posicao(arg):
    if isinstance(arg, tuple) and len(arg) == 2 and isinstance(arg[0], int) and isinstance(arg[1], int) \
            and arg[0] >= 0 and arg[1] >= 0:
        return True
    else:
        return False


# TESTE                           #O Teste compara duas posições, verificando se estas mesmas são iguais ou não, devolvendo se sim e Falso em contrário
def posicoes_iguais(p1, p2):
    if eh_posicao(p1) and eh_posicao(p2) and p1 == p2:
        return True
    return False


# TRANSFORMADOR                   #O Transformador está apenas responsável por transformar a posição em si para string
def posicao_para_str(p):
    return str(p)


# Funções de Alto nível para TAD posicao:

"""""
Estas são as funçõies que tiram partido das TADs anteriormente estabelecidas e usam nas para definir as posicoes 
adjacentes no sentido horário e para ordenar as mesmas em sentido de leitura pelo seu valor numerico/sentido de leitura do prado
"""""

def obter_posicoes_adjacentes(p):
    if eh_posicao(p) and obter_pos_x(p) - 1 >= 0 and obter_pos_y(p) - 1 >= 0:
        return (((obter_pos_x(p), (obter_pos_y(p) - 1)), ((obter_pos_x(p) + 1), (obter_pos_y(p))),
                 ((obter_pos_x(p)), (obter_pos_y(p) + 1)), ((obter_pos_x(p) - 1), obter_pos_y(p))))
    elif eh_posicao(p) and obter_pos_x(p) == 0 and obter_pos_y(p) - 1 >= 0:
        return (((obter_pos_x(p)), (obter_pos_y(p) - 1)), ((obter_pos_x(p) + 1), (obter_pos_y(p))),
                ((obter_pos_x(p)), (obter_pos_y(p) + 1)))
    elif eh_posicao(p) and obter_pos_x(p) - 1 >= 0 and obter_pos_y(p) == 0:
        return (((obter_pos_x(p) + 1), (obter_pos_y(p))), ((obter_pos_x(p)), (obter_pos_y(p) + 1)),
                ((obter_pos_x(p) - 1), obter_pos_y(p)))
    elif eh_posicao(p) and obter_pos_x(p) == 0 and obter_pos_y(p) == 0:
        return (obter_pos_x(p) + 1, obter_pos_y(p)), (obter_pos_x(p), obter_pos_y(p) + 1)


def ordenar_posicoes(tuppos):
    return tuple(sorted(tuppos, key=lambda pos: (pos[1], pos[0])))


# TAD Animal
"""""
Os TADs Animal são os Tipos de Abstração de Dados responsáveis por deefinir os elementos do prado que são avaliados como
animais sendo eles predadores ou presas. Estas funções criam animais, predadores ou presas; verificam se são realmente
animais/presas/predadores; aumentam ou dão reset nas suas características específicas e verificam se são férteis, etc.

cria animal: str × int × int --> animal
cria copia animal: animal --> animal
obter especie: animal --> str
obter freq reproducao: animal --> int
obter freq alimentacao: animal --> int
obter idade: animal --> int
obter fome: animal --> int
aumenta idade: animal --> animal
reset idade: animal --> animal
aumenta fome: animal --> animal
reset fome: animal --> animal
eh animal: universal --> booleano
eh predador: universal --> booleano
eh presa: universal --> booleano
animais iguais: animal × animal --> booleano
animal para char: animal --> str
animal para str : animal --> str
eh animal fertil : animal -->booleano
eh animal faminto: animal --> booleano
reproduz animal: animal --> animal
"""""

# CONSTRUTORES                #Os contrutores controem um animal com vários argumentos e características e copiam um animal novo com as mesmas coisas que o argumento

def cria_animal(especie, frep, falim):
    if not len(especie) >= 1:
        raise ValueError('cria_animal: argumentos invalidos')
    if isinstance(especie, str) and isinstance(frep, int) and isinstance(falim, int) and frep > 0 and falim >= 0:
        idade, fome = 0, 0
        return [especie, frep, falim, idade, fome]
    else:
        raise ValueError('cria_animal: argumentos invalidos')


def cria_copia_animal(animal):
    return [animal[0], animal[1], animal[2], animal[3], animal[4]]


# SELETORES    #Os seletores apenas retiram características dos argumentos respetivos sendo eles: a espécie, a fome, a frq. de reprodução, a frq. de alimentação e a idade

def obter_especie(animal):
    return animal[0]


def obter_freq_reproducao(animal):
    return animal[1]


def obter_freq_alimentacao(animal):
    return animal[2]


def obter_idade(animal):
    return animal[3]


def obter_fome(animal):
    return animal[4]


# MODIFICADORES      #Os modificadores apenas alteram algumas das características dos animais incrementando +1 ou dando reset

def aumenta_idade(animal):
    if isinstance(animal, list) and len(animal) == 5 and isinstance(animal[0], str) and \
            len(animal[0]) >= 1 and [x for x in animal[1:5] if type(x) == int]:
        animal[3] += 1
        return animal
    else:
        pass


def reset_idade(animal):
    if isinstance(animal, list) and len(animal) == 5 and isinstance(animal[0], str) and \
            len(animal[0]) >= 1 and [x for x in animal[1:5] if type(x) == int]:
        animal[3] = 0
        return animal
    else:
        pass


def aumenta_fome(animal):
    if isinstance(animal, list) and len(animal) == 5 and isinstance(animal[0], str) and len(animal[0]) >= 1 \
            and [x for x in animal[1:5] if type(x) == int] and animal[2] > 0:
        animal[4] += 1
        return animal
    else:
        pass


def reset_fome(animal):
    if isinstance(animal, list) and len(animal) == 5 and isinstance(animal[0], str) and len(animal[0]) >= 1 \
            and [x for x in animal[1:5] if type(x) == int] and animal[2] > 0:
        animal[4] = 0
        return animal
    else:
        pass


# RECONHECEDORES #Estes apenas verificam se o argumento do animal corresponde ddentro das regras que o argumento tem de seguir para ser avaliado como um animal

def eh_animal(arg):
    if isinstance(arg, list) and len(arg) == 5 and isinstance(arg[0], str) and \
            len(arg[0]) >= 1:
        for i in range(1, len(arg)):
            if type(arg[i]) == int and arg[i] >= 0:
                pass
            else:
                return False
        return True
    else:
        return False

def eh_predador(arg):
    if isinstance(arg, list) and len(arg) == 5 and isinstance(arg[0], str) and len(arg[0]) >= 1 \
            and [x for x in arg[1:5] if type(x) == int] and arg[2] > 0:
        return True
    else:
        return False


def eh_presa(arg):
    if isinstance(arg, list) and len(arg) == 5 and isinstance(arg[0], str) and len(arg[0]) >= 1 and \
            [x for x in arg[1:5] if type(x) == int] and arg[2] == 0:
        return True
    else:
        return False


# TESTE   # O Teste verifica se dados dois argumentos de animais são iguais ou não retornando True se sim e False se não

def animais_iguais(a1, a2):
    if eh_animal(a1) and eh_animal(a2) and a1 == a2:
        return True
    else:
        return False


# TRANSFORMADORES # Estes Transformadores transformam os argumentos de forma a ser mais fácil identificar os animais, uma apenas a retirar a primeira letra e a metê-la maiscula se é um predador,
                  # e a outra a transformar o argumento para um formato em str
def animal_para_char(animal):
    if eh_presa(animal):
        return animal[0][0].lower()
    else:
        return animal[0][0].upper()


def animal_para_str(animal):
    if eh_presa(animal):
        return animal[0] + ' ' + '[' + str(animal[3]) + '/' + str(animal[1]) + ']'
    elif eh_predador(animal):
        return animal[0] + ' ' + '[' + str(animal[3]) + '/' + str(animal[1]) + ';' \
               + str(animal[4]) + '/' + str(animal[2]) + ']'
    else:
        pass


# Funções de Alto nível

"""""
Estas são as funçõies que tiram partido das TADs anteriormente estabelecidas e usam nas para definir se um animal é 
fértil ou não, para verificar se um animal está faminto ou não e para reproduzir um animal se o animal for fértil
"""""

def eh_animal_fertil(animal):
    if eh_animal(animal):
        if obter_idade(animal) / obter_freq_reproducao(animal) == 1:
            return True
        else:
            return False
    else:
        return False


def eh_animal_faminto(animal):
    if eh_predador(animal):
        if obter_fome(animal) >= obter_freq_alimentacao(animal):
            return True
        else:
            return False
    else:
        return False


def reproduz_animal(animal):
    if eh_animal(animal) and eh_animal_fertil(animal):
        reset_idade(animal)
        return (obter_especie(animal), obter_freq_reproducao(animal), obter_freq_alimentacao(animal),
                obter_idade(reset_idade(animal)), obter_fome(reset_fome(animal)))
    else:
        pass


# TAD PRADO

"""""
Estes são os TADs que misturam tudo o que foi definido anteriormente e comeca a deinir a 'arena' do +rado por inteiro

cria prado: posicao × tuplo × tuplo × tuplo  --> prado
cria copia prado: prado --> prado
obter tamanho x: prado --> int
obter tamanho y: prado --> int
obter numero predadores: prado --> int
obter numero presas: prado --> int
obter posicao animais: prado --> tuplo posicoes
obter animal: prado × posicao --> animal
eliminar animal: prado × posicao --> prado
mover animal: prado × posicao × posicao --> prado
inserir animal: prado × animal × posicao --> prado
eh prado: universal --> booleano
eh posicao animal: prado × posicao --> booleano
eh posicao obstaculo: prado × posicao --> booleano
eh posicao livre: prado × posicao --> booleano
prados iguais: prado × prado --> booleano
prado para str : prado --> str
obter valor numerico: prado × posicao --> int
obter movimento: prado × posicao --> posicao
"""""

# CONSTRUTORES                                    #Esta função apenas controi o sistema do prado em si, com os rochedos, a dimensão, os animais e as suas posições correspondentes dentro de uma lista
def cria_prado(d, r, a, p):
    if eh_posicao(d) and isinstance(r, tuple) and len(r) >= 0 and all(x for x in r if eh_posicao(x)) and \
            isinstance(a, tuple) and len(a) >= 1 and all(x for x in a if eh_animal(a)) and isinstance(p, tuple) and \
            len(p) == len(a) and all(x for x in p if eh_posicao(x)):
        listaprado, contador, listalinhas, posicoesanimais = [], 0, [], []
        linhas, colunas = obter_pos_y(d), obter_pos_x(d)
        listaprado.append(d)
        listaprado.append(list(r))
        for e in range(0, len(a)):             # len(a) = len(p)
            posicoesanimais.append(a[e])
            posicoesanimais.append(p[e])
        listaprado.append(posicoesanimais)
        return listaprado
    else:
        raise ValueError('cria_prado: argumentos invalidos')


def cria_copia_prado(prado):                 # Esta função apenas copia e retorna o argumento de prado
    return [prado[0], prado[1], prado[2]]


# SELETORES           #Os seletors apenas retornam as características específicas do prado

def obter_tamanho_x(prado):
    return prado[0][0] + 1


def obter_tamanho_y(prado):
    return prado[0][1] + 1


def obter_numero_predadores(prado):
    counter = 0
    for e in prado[2]:
        if eh_predador(e):
            counter += 1
        else:
            pass
    return counter


def obter_numero_presas(prado):
    counter = 0
    for e in prado[2]:
        if eh_presa(e):
            counter += 1
        else:
            pass
    return counter


def obter_posicao_animais(prado):
    tupleres = ()
    for e in prado[2]:
        if eh_posicao(e):
            tupleres += (e,)
        else:
            pass
    return ordenar_posicoes(tupleres)


def obter_animal(prado, pos):
    for i in range(0, len(prado[2]) - 1):
        if eh_animal(prado[2][i]):
            if prado[2][i + 1] == pos:
                return prado[2][i]
            else:
                pass
        else:
            pass


# MODIFICADORES     #Os modificadores são responsáveis por alterar os prados com várias coisas tais como: eliminar animais do prado, mover animais e inserir novos animais dentro do prado.

def eliminar_animal(prado, pos):
    for i in range(0, len(prado[2]) - 2):
        if eh_animal(prado[2][i]):
            if prado[2][i + 1] == pos:
                del prado[2][i: i + 2]
        else:
            pass
    return prado


def mover_animal(prado, pos1, pos2):
    for i in range(0, len(prado[2]) - 1):
        if eh_animal(prado[2][i]) and prado[2][i + 1] == pos1:
            prado[2][i + 1] = pos2
        else:
            pass
    return prado


def inserir_animal(prado, animal, posicao):
    for i in range(0, len(prado[2]) - 1):
        if eh_animal(prado[2][i]) and prado[2][i + 1] == posicao:
            prado[2][i] = animal
            return prado
        else:
            pass
    if eh_animal(animal) and eh_posicao(posicao):
        prado[2].append(animal)
        prado[2].append(posicao)
        return prado
    else:
        pass


# RECONHECEDORES   #Os reconhecedores devolvem False ou True se o argumento respeitar as regras do que está definido por prado

def eh_prado(prado):
    if isinstance(prado, list) and len(prado) == 3 and eh_posicao(prado[0]) \
            and isinstance(prado[1], list):
        for x in prado[1]:
            if eh_posicao(x):
                pass
            else:
                return False
        if isinstance(prado[2], list):
            for x in prado[2]:
                if eh_animal(x):
                    pass
                elif eh_posicao(x):
                    pass
                else:
                    return False
        else:
            return False
        return True
    else:
        return False


def eh_posicao_animal(prado, posicao):               #  Esta função verifica se existe um animal numa dada posição dentro do prado
    if eh_prado(prado):
        for e in prado[2]:
            if eh_posicao(e):
                if posicoes_iguais(e, posicao):
                    return True
                else:
                    pass
            else:
                pass
        return False
    else:
        return False


def eh_posicao_obstaculo(prado, pos):      #sta função verifica se existe um obstáculo seja ele rochedo ou montanha  numa dada posição dentro do prado
    if obter_pos_y(pos) == obter_pos_y(prado[0]) or obter_pos_y(pos) == 0 or obter_pos_x(pos) == obter_pos_x(prado[0]) \
            or obter_pos_y(pos) == 0:
        return True            # Quando o obstáculo é uma montanha
    else:
        pass
    if eh_prado(prado):                        # Quando o obstáculo é um rochedo
        for e in prado[1]:
            if posicoes_iguais(e, pos):
                return True
            else:
                pass
        return False
    else:
        return False

def eh_posicao_livre(prado, pos):  # Esta função verifica se uma dada posição está livre dentro do prado
    if eh_prado(prado):
        if eh_posicao_obstaculo(prado, pos) or eh_posicao_animal(prado, pos):
            return False
        else:
            pass
        return True
    else:
        return False

# TESTES   # Este Teste apenas verifica se os argumentos são prados e se são iguais retornando True se sim e False se não

def prados_iguais(prado1, prado2):
    if eh_prado(prado1) and eh_prado(prado2) and prado1 == prado2:
        return True
    else:
        return False

# TRANSFORMADOR  # O transformador está responsável por transformar a lista que contém o prado num formato que simboliza a 'arena' do prado em si por formato de string

def prado_para_str(prado):
    listaprado = []
    e = 0
    for y in range(obter_pos_y(prado[0]) + 1):
        for x in range(obter_pos_x(prado[0]) + 1):
            listaprado.append((x, y))
    while e in range(len(listaprado)):
        if listaprado[e] == (0, 0) or listaprado[e] == (0, obter_pos_y(prado[0])) or \
                listaprado[e] == (obter_pos_x(prado[0]), 0) or \
                listaprado[e] == (obter_pos_x(prado[0]), obter_pos_y(prado[0])):
                    listaprado[e] = '+'
        elif obter_pos_x(listaprado[e]) == 0 or obter_pos_x(listaprado[e]) == obter_pos_x(prado[0]):
            listaprado[e] = '|'
        elif obter_pos_y(listaprado[e]) == 0 or obter_pos_y(listaprado[e]) == obter_pos_y(prado[0]):
            listaprado[e] = '-'
        else:
            pass
        e += 1
    for i in range(len(listaprado)):
        if listaprado[i] == '+' or listaprado[i] == '|' or listaprado[i] == '-':
            pass
        elif eh_posicao_obstaculo(prado, listaprado[i]):
            listaprado[i] = '@'
        elif eh_posicao_animal(prado, listaprado[i]):
            for x in range(1, len(prado[2]), 2):
                if prado[2][x] == listaprado[i]:
                    listaprado[i] = animal_para_char(prado[2][x - 1])
                else:
                    pass
        else:
            listaprado[i] = '.'
    for x in range(1,len(listaprado)):
        if listaprado[x] == '+':
            if x < ((obter_pos_x(prado[0]) * obter_pos_y(prado[0]) + obter_pos_x(prado[0]) + 1)
                    - obter_pos_x(prado[0])):
                listaprado.insert(x + 1, '\n')
        elif listaprado[x] == '|' and listaprado[x + 1] == '|':
            listaprado.insert(x + 1, '\n')
        elif listaprado[x] == '|' and listaprado[x + 1] == '+':
            listaprado.insert(x + 1, '\n')
        else:
            pass
    return ''.join(listaprado)

# Funções de Alto Nível
"""""
Estas são as funçõies que tiram partido das TADs anteriormente estabelecidas e usam nas para obter um valor numerico de uma dada posição dentro de um prado escolhido
e para também obter o movimento seguinte de um animal dentro do prado
"""""
def obter_valor_numerico(prado, pos):
    contador, listalinhas = 0, []
    if eh_posicao(pos):
        linhas, colunas = obter_pos_y(prado[0]) + 1, obter_pos_x(prado[0]) + 1
        for i in range(0, linhas):
            for i in range(0, colunas):
                listalinhas.append(contador)
                contador += 1
        valornum = (obter_pos_x(pos) + 1) * obter_pos_y(pos) + obter_pos_x(pos)
        if valornum in listalinhas:
            return valornum
        else:
            pass
    else:
        pass

def obter_movimento(prado, pos):
    if eh_posicao_animal(prado, pos):
        listares = obter_posicoes_adjacentes(pos)
        N = obter_valor_numerico(prado,pos)
        possele = N % len(listares)
        for i in range(0, len(listares) - 1):
            if i == possele:
                return listares[i]
            else:
                pass

"""""
Não foi me possível realizar as funções de geração e de ecossistema pelo que qual peço desculpa
"""""
