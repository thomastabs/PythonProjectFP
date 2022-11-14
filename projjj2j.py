#ProjetoFP - Buggy Data Base

#Passo 1 do Projeto: Correção da Documentação
# 1.2.1

def corrigir_palavra(palavra):
    """
    Esta função verifica se argumento possui elementos que devem ser eliminados. Os elementos que devem ser elimiminados são
    a mesma letra seguida em tamanhos diferentes, por exemplo Aa ou aA é apagado da cifra e assim em diante.
    Assim a palavra é transformada em lista para facilitar a alteração e eliminação das partes corrompidas, se existirem.
    E no final o resultado é o join da lista já alterada.
    """
    palavra = list(palavra)
    for i in range(len(palavra) - 1, 0, -1):
        if 97 <= ord(palavra[i]) <= 122 or 65 <= ord(palavra[i]) <= 90:
            if abs(ord(palavra[i - 1]) - ord(palavra[i])) == 32:
                del palavra[i - 1: i + 1]
            else:
                pass
    return ''.join(palavra)


#1.2.2

def eh_anagrama(caracteres, caracteres2):
    """
    Esta é uma função simples que verifica se os dois argumentos da função são anagramas um do outro,
    a função começa por verificar o tamanho dos argumentos e se são iguais,
    depois transforma as strings para letras maiusculas,
    que como é mostrado no exemplo dado no enunciado, seja uma ou outra letra upper ou lower,
    as palavras continuam a ser anagramas,
    então para facilitar, foram as duas transforadas em upper, deu-se sort e verificou-se se os dois sort eram iguais,
    dá return True se todas estas condições forem aceites, ou Falso se falhar apenas uma.
    """
    if not len(caracteres) == len(caracteres2):
        return False
    else:
        anagrama1, anagrama2 = caracteres.upper(), caracteres2.upper()
        if not sorted(anagrama1) == sorted(anagrama2):
            return False
        else:
            return True

#1.2.3

def corrigir_doc(megacifra):
    """
    Esta função reune todas as funções anteriores, e faz com que elas trabalhem juntas para devolverr o resultado.
    Primeiro, são levantados erros na função se o argumento não for string,
    se um elemento da cifra não for elemento do alfabeto ou um espaço
    e se existir dois espaços seguidos tal que '  '. Assim depois de ser aplicada a função corrigir_palavra,
    caso existam anagramas, eles são eliminados,
    sem contar com as palavras literalmente iguais (com letras minuscúlas ou maiúsculas).
    E assim é devolvido o resulltado.
    """
    if not isinstance(megacifra, str):
        raise ValueError('corrigir_doc: argumento invalido')
    for e in megacifra:
        if not (97 <= ord(e) <= 122 or 65 <= ord(e) <= 90 or ord(e) == 32):
            raise ValueError('corrigir_doc: argumento invalido')
    if '  ' in megacifra:
        raise ValueError('corrigir_doc: argumento invalido')
    x = corrigir_palavra(megacifra)
    testeanagrama = x.split()
    for i in range(0, len(testeanagrama)):
        for u in range(0, len(testeanagrama)):
            if not (testeanagrama[i].lower() == testeanagrama[u].lower()):
                if eh_anagrama(testeanagrama[i], testeanagrama[u]):
                    testeanagrama[u] = ''
    if testeanagrama[len(testeanagrama) - 1] == '':
        del testeanagrama[len(testeanagrama) - 1]
    return ' '.join(testeanagrama).replace('  ', ' ')


#Passo 2 do Projeto: Descoberta do PIN da base de dados

#2.2.1

def obter_posicao(caracter, inteiro):
    """
    A função verifica o caracter para ver se é um dos correspondentes às letras: C, B, E e D.
    Dependendo do valor do argumento 'inteiro' e do caractere selecionado, a posição nova pode mudar.
    Para certos números, quando um caracter é escolhido, o inteiro nem sequer muda.
    Um exemplo é se os agrumentos forem (C,3) o que dá 3, pois já não é possível mover-se para cima.
    Por isso, dependendo desses fatores, um inteiro, diferente ou não, é devolvido.
    """
    if not caracter in 'CBED':
        return False
    if caracter == 'C':
        if 9 >= inteiro >= 4:
            inteiro -= 3
            return inteiro
        else:
            return inteiro
    elif caracter == 'B':
        if 6 >= inteiro >= 1:
            inteiro += 3
            return inteiro
        else:
            return inteiro
    elif caracter == 'E':
        if inteiro in (2, 3, 5, 6, 8, 9):
            inteiro -= 1
            return inteiro
        else:
            return inteiro
    else:
        if inteiro in (1, 2, 4, 5, 7, 8):
            inteiro += 1
            return inteiro
        else:
            return inteiro

#2.2.2

def obter_digito(caracteres, inteiro):
    """
    Verifica os caracteres transformando-os em um tuplo
    Verifica as letras com a função obter_posição
    Guarda o novo inteiro que vai mudando graças ao ciclo 'for'
    """
    for letra in caracteres:
        inteiro = (obter_posicao(letra, inteiro))
    return inteiro

#2.2.3

def obter_pin(tup_codigo):
    """
    Crição de um tuplo para guardar o resultado final.
    Como começa no 5 por default, então a posição inicial é o 'inteiro' 5.
    ValueErrors para argumentos inválidos.
    Ciclo 'for' para percorrer os elementos do tuplo.
    Aplicação da função.
    Alteração do elemento 'inteiro', conforme as condições do código são feitas.
    """
    res = ()
    inteiro = 5
    if not isinstance(tup_codigo, tuple):
        raise ValueError('obter_pin: argumento invalido')
    if tup_codigo == ():
        raise ValueError('obter_pin: argumento invalido')
    for e in tup_codigo:
        if e == " " or e == "":
            raise ValueError('obter_pin: argumento invalido')
        for i in range(len(e)):
            if e[i] == " " or e[i] == "":
                raise ValueError('obter_pin: argumento invalido')
            if not e[i] in 'CBED':
                raise ValueError('obter_pin: argumento invalido')
    if not 10 >= len(tup_codigo) >= 4:
        raise ValueError('obter_pin: argumento invalido')
    for digito in range(len(tup_codigo)):
        inteiro = (obter_digito(tup_codigo[digito], inteiro))
        res += (inteiro,)
    return res


#Passo 3 do Projeto: Verificação de dados

#3.2.1

def eh_entrada(tupbdb):
    """
    Esta função analisa o arugmento dado e devolve a sua resposta da verificação como True ou False.
    Como uma série de Ifs e Fors, são verificadas as caracteristicas necessárias se aceitar como True um argumento.
    São avaliadas se o argumento é um dict, a sua length é 3, as chaves do dict, a length do dict dentro do dict, ect.
    """
    if not isinstance(tupbdb, tuple) or not len(tupbdb) == 3:
        return False
    if not isinstance(tupbdb[1], str) or not len(tupbdb[1]) == 7:
        return False
    if tupbdb[0] == '' or tupbdb[1] == '':
        return False
    if not isinstance(tupbdb[2], tuple) or not len(tupbdb[2]) >= 2:
        return False
    if not isinstance(tupbdb[0], str) or not len(tupbdb[0]) >= 1:
        return False
    for i in range(len(tupbdb[0])):
        if tupbdb[0][i] == '-':
            if tupbdb[0][i + 1] == '-':
                return False
        if not 97 <= ord(tupbdb[0][i]) <= 122:
            if not tupbdb[0][i] == '-':
                return False
    if not ord(tupbdb[1][0]) == 91 or not ord(tupbdb[1][len(tupbdb[1]) - 1]) == 93:
        return False
    for i in range(1, len(tupbdb[1]) - 1):
        if not 97 <= ord(tupbdb[1][i]) <= 122:
            return False
    for e in tupbdb[2]:
        if not isinstance(e, int):
            return False
        if e < 0:
            return False
    else:
        return True

#3.2.2

def validar_cifra(cifra, seqcontrolo):
    """
    Esta função verifica se os argumentos correspondem um com o outro,
    devolvendo no final uma avaliação bool de True ou False.
    É criada um dicionário que irá ser útil mais tarde, guardando os valores dos contadores;
    Este dicionário irá conter: as chaves (as letras) e o seu valor correspondente
    que é igual ao numero de vezes que essa letra foi detetada
    e guardado o seu valor no 'contador'. Assim dá-se sort no dict e
    é feito uma lista para guardar os valores das letras mais repetidas na cifra por ordem alfabética.
    E por fim, compara-se o valor obtido ao valor do argumento da sequencia de controlo.
    """
    contador, megadict = 0, {},                            #Caso as variáveis possam ser confusas:
    cifranohif = cifra.replace('-', '')                       #megadict = mega dicionario
    cifralista = list(cifranohif)                             #cifranohif = cifra no hifen
    letras = sorted(cifralista)                               #superdict = super dicionario (apesar de ser uma lista)
    for i in range(len(letras) - 1):
        if letras[i] == letras[i + 1]:
            contador += 1
            if i == (len(letras) - 2):
                megadict[letras[i]] = contador + 1
        else:
            megadict[letras[i]] = contador + 1
            contador = 0
    megadict = sorted(megadict, key=megadict.get, reverse=True)
    superdict = megadict[:5]
    y = str('[' + ''.join(superdict) + ']')
    if y == seqcontrolo:
        return True
    else:
        return False

#3.2.3

def filtrar_bdb(listabdb):
    novalista = []
    if not isinstance(listabdb, list):
        raise ValueError('filtrar_bdb: argumento invalido')
    if listabdb == []:
        raise ValueError('filtrar_bdb: argumento invalido')
    for e in listabdb:
        if not eh_entrada(e):
            raise ValueError('filtrar_bdb: argumento invalido')
        if validar_cifra(e[0], e[1]):
            del e
        else:
            novalista = novalista + [e]
    return novalista

#Passo 4 do Projeto: Desencriptação de Dados

#4.2.1

"""Esta função está definida no 3.2.1"""

#4.2.2

def obter_num_seguranca(num):
    """
    Esta função analisa um tuplo de numéros inteiros positivos
    e dá return da a menor diferenca positiva entre qualquer par de numeros
    É criada uma lista vazia, para conter o resultado no final
    E nessa lista está o valor a diferença absoluta de cada par da lista, e assim sabe-se o seu minímo.
    """
    listanum = []
    num = sorted(num, reverse=True)
    for i in range(0, len(num)):
        for i2 in range(0, len(num)):
            dif = abs(num[i] - num[i2])
            listanum = listanum + [dif, ]
    listanum = sorted(set(listanum))
    listanum.remove(0)
    return min(listanum)

#4.2.3

def decifrar_texto(caracteres, inteiros):
    """
    Esta função faz a transformação dos caracteres dados com os inteiros, de forma a ficar legível.
    A função usa o valor dos inteiros, tirando o seu resto por 26,
    e adicionando-os ao código org da letra de modo a 'avançar' no alfabeto
    E dependendo do indice dos caracteres, é acrescentado mais um valor ou é tirado mais um, se for par ou impar,
    respetivamente. Se um caracter for um hífen '-', a função também o altera, transformando-o para um espaço.
    Assim, é criada uma nova lista vazia onde vai ser armazenado todos os dados que foram alterados
    No final é returnado o resultado que é o 'join' dos elementos dessa lista.
    """
    inteiros2 = inteiros % 26
    listanovacifra = []
    for i, e in enumerate(caracteres):                                      #e é o elemento de indice i
        if e.isalpha():
            if i % 2 == 0:
                newletterord = ord(e) + 1 + inteiros2
                if newletterord > 122:
                    newletterord -= 26
                listanovacifra += [chr(newletterord)]
            if i % 2 == 1:
                newletterord = ord(e) - 1 + inteiros2
                if newletterord > 122:
                    newletterord -= 26
                elif newletterord < 97:
                    newletterord += 26
                listanovacifra += [chr(newletterord)]
        elif e == '-':
            listanovacifra += [' ']
        else:
            raise ValueError('decifrar_texto: argumento invalido')
    return ''.join(listanovacifra)


#4.2.4

def decifrar_bdb(lista):                      #e é um elemento da lista.
    """
    Esta função ao contrário das outras é a mais simples, ela somente cria uma nova lista para guardar os resultados,
    como também usa as outras funções para o argumento ser avaliado, validado, transformado e retornado.
    """
    caixa = []
    if not isinstance(lista, list) or not len(lista) >= 1:
        raise ValueError('decifrar_bdb: argumento invalido')
    for e in lista:
        if not eh_entrada(e):
            raise ValueError('decifrar_bdb: argumento invalido')
        caixa += [decifrar_texto(e[0], obter_num_seguranca(e[2]))]
    return caixa

#Passo 5 do Projeto: Depuração de Senhas

#5.2.1

def eh_utilizador(d):
    """
    A função verifica se as várias propiedades do argumento estão a ser cumpridas ou não.
    Com uma série de 'ifs', é possível verificar se o argumento possui as propriedades para ser correspondido e,
    finalmente, ser declarado como 'True'.
    """
    if d == '' or d == () or d == []:
        return False
    if isinstance(d, float) or isinstance(d, int):
        return False
    if not isinstance(d, dict):
        return False
    if d == {}:
        return False
    if not len(d) == 3:
        return False
    if not all(key in d for key in ('name', 'pass', 'rule')):
        return False
    if not isinstance(d['name'], str) or not isinstance(d['pass'], str):
        return False
    if d['pass'] == '' or d['name'] == '':
        return False
    if not isinstance(d['rule'], dict):
        return False
    if not 'vals' in d['rule'] or not 'char' in d['rule']:
        return False
    if not isinstance(d['rule']['vals'], tuple):
        return False
    if not len(d['rule']['vals']) == 2:
        return False
    if not d['rule']['vals'][0] >= 0 and d['rule']['vals'][1] >= 0:
        return False
    if not d['rule']['vals'][0] <= d['rule']['vals'][1]:
        return False
    if not len(d['rule']['char']) == 1:
        return False
    if not 97 <= ord(d['rule']['char']) <= 122:
        return False
    else:
        return True

#5.2.2

def eh_senha_valida(senha, drules):
    """
    Esta função tem o dever de verificar todas as condições para uma senha ser válida com a ajuda dos 'ifs'.
    Primeiro, são impostas as regras gerais das senhas, e as caracteristicas que elas devem possuir.
    E a seguir, são impostas as condições responsáveis pelas regras individuais das semhas que variam.
    As regras individuais alteram-se devido aos valores do char e do vals, o que foi posto em causa e verificado.
    Assim depois de verificar todas as condições, a funcão dá 'True' ou 'False'
    """
    tup_senha = tuple(senha)
    vogais, contador1, contador2 = 0, 1, 0
    for i in tup_senha:
        if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
            vogais = vogais + 1
    if not vogais >= 3:
        return False
    for i in range(1, len(tup_senha)):
        if tup_senha[i - 1] == tup_senha[i]:
            contador1 = contador1 + 1
    if not contador1 >= 2:
        return False
    for i in range(0, len(tup_senha)):
        if drules['char'] == tup_senha[i]:
            contador2 = contador2 + 1
    if not drules['vals'][0] <= contador2 <= drules['vals'][1]:
        return False
    else:
        return True

#5.2.3

def filtrar_senhas(listadic):
    """
    Esta função recebe uma lista que contém vários dicionários, elimina os dicionários que estão corretos.
    Esta função não só extrai os nomes dos dicionários errados,
    como também os mete numa lista e os ordena por ordem alfabética.
    """
    if not isinstance(listadic, list):
        raise ValueError('filtrar_senhas: argumento invalido')
    if listadic == []:
        raise ValueError('filtrar_senhas: argumento invalido')
    if not len(listadic) >= 1:
        raise ValueError('filtrar_senhas: argumento invalido')
    for dic in range(0, len(listadic) - 1):
        if eh_senha_valida(listadic[dic]['pass'], listadic[dic]['rule']) == True:
            del listadic[dic]
    listapasseserradas = [dic['name'] for dic in listadic if 'name' in dic]
    return sorted(listapasseserradas)
