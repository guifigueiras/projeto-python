#Guilherme Figueiras
#+351 927 321 694
base_tab=15
abecedario = 'ABCÇDEFGHIJLMNOPQRSTUVXZ'
tamanho_do_abecedario=24

saco = {
'A': 14, 'B': 3, 'C': 4, 'Ç': 2, 'D': 5, 'E': 11,
'F': 2, 'G': 2, 'H': 2, 'I': 10, 'J': 2, 'L': 5,
'M': 6, 'N': 4, 'O': 10, 'P': 4, 'Q': 1, 'R': 6,
'S': 8, 'T': 5, 'U': 7, 'V': 2, 'X': 1, 'Z': 1 }

pontos = {
'A': 1, 'B': 3, 'C': 2, 'Ç': 3, 'D': 2, 'E': 1,
'F': 4, 'G': 4, 'H': 4, 'I': 1, 'J': 5, 'L': 2,
'M': 1, 'N': 3, 'O': 1, 'P': 2, 'Q': 6, 'R': 1,
'S': 1, 'T': 1, 'U': 1, 'V': 4, 'X': 8, 'Z': 8 }

def ordena_letras(let):
    res = []
    for l in abecedario:
        for ch in list(let):
            if ch == l:
                res.append(l)
    return res

def ord_lexi_palavra(palavra):
    tuplo = ()
    for letra in palavra:
        tuplo+=(len(abecedario) - abecedario.index(letra),)
    return tuplo

def ordena_palavras(lista_de_palavras):              
    return sorted(lista_de_palavras, key=lambda x: (len(x), x[1], ord_lexi_palavra(x[0])), reverse=True)


def aux_direcao(i, f):
    return "H" if obtem_lin(i) == obtem_lin(f) else "V" 


###################################################################################################################################################################

#2.1.1
def cria_casa(l, c):
    if type(l) != int or type(c) != int:
        raise ValueError ("cria_casa: argumentos inválidos")
    if l>base_tab or c>base_tab:
       raise ValueError ("cria_casa: argumentos inválidos")
    if l<=0 or c<=0:
        raise ValueError ("cria_casa: argumentos inválidos")
    return (l,c)


def obtem_col(c):
    return c[1]


def obtem_lin(c):
    return c[0]


def eh_casa(arg):
    if type(arg)!=tuple:
        return False
    for num in arg:
        if type(num)!=int:
            return False
    if obtem_col(arg)>base_tab or obtem_col(arg)<1:
        return False
    if obtem_lin(arg)>base_tab or obtem_lin(arg)<1:
        return False
    else:
        return True


def casas_iguais(c1, c2):
    if eh_casa(c1) and eh_casa(c2):
        if c1==c2:
            return True
    return False


def casa_para_str(casa):
    string_casa="" 
    string_casa+="("+str(obtem_lin(casa))+","+str(obtem_col(casa))+")"
    return string_casa


def str_para_casa(s):
    tuplo_casa=() 
    indice=s.find(",") 
    tuplo_casa+=(int(s[1:indice]),int(s[indice+1:-1]))                        
    return tuplo_casa


def incrementa_casa(c, d, s):
    if d =="H":
        if obtem_col(c)+s>base_tab:
            return c
        return cria_casa(obtem_lin(c), obtem_col(c)+s)
    if d =="V":
        if obtem_lin(c)+s>base_tab:
            return c
        return cria_casa(obtem_lin(c)+s, obtem_col(c))



#2.1.2
def cria_humano(nome):
    if type(nome)!=str:
        raise ValueError ("cria_humano: argumento inválido")
    if nome=="":
        raise ValueError ("cria_humano: argumento inválido")                   
    perfil={}
    perfil["id"]=nome
    perfil["pontos"]=0
    perfil["letras"]={}
    return perfil


def cria_agente(nivel):
    if nivel!="FACIL" and nivel!="MEDIO" and nivel!="DIFICIL":
        raise ValueError ("cria_agente: argumento inválido")
    perfil={}
    perfil["id"]=nivel
    perfil["pontos"]=0
    perfil["letras"]={}
    return perfil


def jogador_identidade(j):
    return j["id"]


def jogador_pontos(j):
    return j["pontos"]


def jogador_letras(j):
    lista_letras=[]
    for i in j["letras"]:
        lista_letras+=[i]*j["letras"][i]
    lista_letras=ordena_letras(lista_letras)
    resultado="".join(lista_letras)    
    return resultado


def recebe_letra(j, l):
    j["letras"][l]=j["letras"].get(l, 0)+1
    return j


def usa_letra(j, l):
    j["letras"][l]+=-1
    return j


def soma_pontos(j, p):
    j["pontos"]+=p
    return j


def eh_jogador(arg):
    if type(arg)!=dict:
        return False
    if arg.keys()!=["id","pontos","letras"]:
        return False
    return True


def eh_humano(arg):
    if type(arg)!=dict:
        return False
    if jogador_identidade(arg)== "FACIL" or jogador_identidade(arg)== "MEDIO" or jogador_identidade(arg)== "DIFICIL":
        return False
    return True


def eh_agente(arg):
    if type(arg)!=dict:
        return False
    if eh_humano(arg):
        return False
    return True


def jogadores_iguais(j1, j2):
    if eh_jogador(j1) and eh_jogador(j2):
        if j1.keys()==j2.keys() and j1.values()==j2.values():
            return True
    if eh_agente(j1) and eh_agente(j2):
        if j1.keys()==j2.keys() and j1.values()==j2.values():
            return True
    return False


def jogador_para_str(t):
    letras=jogador_letras(t)
    final=""
    letras=ordena_letras(letras)
    for j in letras:
        final+=j
    letras=" ".join(final)
    letras=" "+letras
    if eh_humano(t):
        return t["id"] + " " + "(" + "{:>3}".format(str(jogador_pontos(t))) + ")" + ":" + letras
    if eh_agente(t):
        return "BOT(" + t["id"] + ")"+ " " + "(" + "{:>3}".format(str(jogador_pontos(t))) + ")" + ":" + letras
 
    
def distribui_letras(jog, saco, num):
    if saco==[]:
        return jog
    for n_letras in range(num):
        a=saco.pop()
        recebe_letra(jog, a)
        if saco==[]:
            return jog
    ordena_letras(jogador_letras(jog))
    return jog

#2.1.3
def cria_vocabulario(v):
    vocab={}
    if type(v)!=tuple:
        raise ValueError ("cria_vocabulario: argumento inválido")
    if v==():
        raise ValueError ("cria_vocabulario: argumento inválido")
    for palavra in v:
        if type(palavra) != str or len(palavra)<2 or len(palavra)>base_tab:
            raise ValueError ("cria_vocabulario: argumento inválido")
        for letra in palavra:
            if letra not in abecedario:
                raise ValueError ("cria_vocabulario: argumento inválido")
    for palavra in v:
        inicial=palavra[0]
        comprimento = len(palavra)
        if comprimento not in vocab:
            vocab[comprimento]={}
        if inicial not in vocab[comprimento]:
            vocab[comprimento][inicial]=[]
        vocab[comprimento][inicial].append(palavra)
        
    return vocab
 
            
def obtem_pontos(vocabulario, palavra):
    Pontos=0
    if len(palavra)<2:
        return 0
    for p in vocabulario[len(palavra)][palavra[0]]:
        if p==palavra:
            letras=list(palavra)
            for letra in letras:
                Pontos+=pontos[letra]
    return Pontos


def obtem_palavras(vocabulario, comp, letra):
    palavra_pontos=[]
    if letra not in vocabulario[comp]:
        return()
    for palavra in vocabulario[comp][letra]:
        palavra_pontos.append((palavra,obtem_pontos(vocabulario, palavra)),)
    final=ordena_palavras(palavra_pontos)
    return  tuple(final)
 
  
def testa_palavra_padrao(vocabulario, palavra, padrao, letras):
    if len(palavra) not in vocabulario:
        return False
    if palavra[0] not in vocabulario[len(palavra)]:
        return False
    if palavra not in vocabulario[len(palavra)][palavra[0]]:
        return False
    if len(palavra) != len(padrao):
        return False
    letras_copia = list(letras)

    for i in range(len(padrao)):
        if padrao[i] != '.':
            if padrao[i] != palavra[i]:
                return False
        else:
            if palavra[i] in letras_copia:
                letras_copia.remove(palavra[i])
            else:
                return False
    return True


def ficheiro_para_vocabulario(nome_ficheiro):
    with open(nome_ficheiro, "r", encoding="utf-8") as f:
        linhas = f.readlines()
    palavras_validas = []
    for linha in linhas:
        palavra = linha.strip().upper()
        if 2 <= len(palavra) <= 15 and all(j in abecedario for j in palavra):
            palavras_validas.append(palavra)
    vocab = cria_vocabulario(tuple(palavras_validas))
    return vocab
 
        
def vocabulario_para_str(vocabulario):
    lista_palavras=[]
    for comp in vocabulario:                                                       
        for inicial in vocabulario[comp]:
            for palavra in vocabulario[comp][inicial]:
                lista_palavras.append(palavra)
    lista_tuplos=[(p, obtem_pontos(vocabulario, p)) for p in lista_palavras]
    organizada=ordena_palavras(lista_tuplos)
    quase_final=[]
    for palavra in organizada:
        quase_final.append(palavra[0])
    quase_final=sorted(quase_final, key=lambda x: (len(x), x[0]))
    final="\n".join(quase_final)
    return final


def procura_palavra_padrao(vocabulario, padrao, letras, min_pontos):
    if padrao[0] != ".":
        pal_pont = obtem_palavras(vocabulario, len(padrao), padrao[0])
        for tentativa in pal_pont:
            if testa_palavra_padrao(vocabulario, tentativa[0], padrao, letras) and tentativa[1] >= min_pontos:
                return tentativa
        return ("", 0)
    else:
        possibilidades=[]
        for i in range(tamanho_do_abecedario):
            pal_pont=obtem_palavras(vocabulario, len(padrao), abecedario[i])
            for tentativa in pal_pont:
                if tentativa[1]>=min_pontos:
                    if testa_palavra_padrao(vocabulario, tentativa[0], padrao, letras):
                        possibilidades.append(tentativa)
        if possibilidades==[]:
            return ("", 0)
        ordenado=ordena_palavras(possibilidades)
        return ordenado[0]
  
    
#2.1.4
def cria_tabuleiro():                                                  
    tab=[]
    for i in range(base_tab):
        tab.append(["."]*base_tab)
    return tab


def obtem_letra(t, c):
    return t[c[0]-1][c[1]-1]


def insere_letra(t, c, l):
    t[c[0]-1][c[1]-1]=l
    return t


def eh_tabuleiro(arg):
    if type(arg)!=list:
        return False
    for linha in arg:
        if type(linha) != list:
            return False
        for casa in linha:
            if type(casa) != str:
                return False
            if casa not in abecedario and casa != ".":
                return False
    return True


def eh_tabuleiro_vazio(arg):
    if eh_tabuleiro(arg):
        for linha in arg:
            for casa in linha:
                if casa != ".":
                    return False
    return True


def tabuleiros_iguais(t1, t2):
    if eh_tabuleiro(t1) and eh_tabuleiro(t2):
        for linha in range(base_tab):
            for casa in range(base_tab):
                if t1[casa] != t2[casa]:
                    return False 
                return True
    return False


def tabuleiro_para_str(tab):
    tab_jogo=""
    tab_jogo+="                       1 1 1 1 1 1"
    tab_jogo+="\n"
    tab_jogo+="     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5"
    tab_jogo+="\n"
    tab_jogo+="   +-------------------------------+"
    tab_jogo+="\n"
    for i in range(len(tab)):
        tab_jogo+="{:>2}".format(str(i+1))
        tab_jogo+=(" ")
        tab_jogo+=("| ")
        for j in range(len(tab)):
            tab_jogo+="{:^2}".format(tab[i][j])
        tab_jogo+=("|")
        tab_jogo+="\n"
    tab_jogo+="   +-------------------------------+"
    return tab_jogo


def obtem_padrao(t, i, f):
    direcao = aux_direcao(i, f)
    letras = []
    if direcao == "H":
        for col in range(obtem_col(i), obtem_col(f)+1):
            letras.append(obtem_letra(t, (obtem_lin(i), col)))
    else:
        for lin in range(obtem_lin(i), obtem_lin(f)+1):
            letras.append(obtem_letra(t, (lin, obtem_col(i))))
    return "".join(letras)


def insere_palavra(t, c, d, p):
    if d == "H":
        lin=obtem_lin(c)
        for i in range(len(p)):
            insere_letra(t, (lin, obtem_col(c)+i), p[i])
    if d == "V":
        col=obtem_col(c)
        for i in range(len(p)):
            insere_letra(t, (obtem_lin(c)+i, col), p[i])
    return t


def filtra_padrao(tab, padr, l, casa_i, casa_f, d):
    soma_p = 0
    soma_l = 0
    for elemento in padr:
        if elemento==".":
            soma_p+=1
        else:
            soma_l+=1
    if soma_l==len(padr) or soma_p>l or soma_l<1:
        return False
    
    lin_i=obtem_lin(casa_i)
    col_i=obtem_col(casa_i)
    lin_f=obtem_lin(casa_f)
    col_f=obtem_col(casa_f)
    
    if d == "V":
        if lin_f==15:
            if lin_i==1:
                return True
            if obtem_letra(tab, cria_casa(lin_i-1, col_i))== ".":
                return True
            return False
        if lin_i==1:
            if lin_f==15:
                return True
            if obtem_letra(tab, cria_casa(lin_f+1, col_i)) == ".":
                return True
            return False
        if obtem_letra(tab, cria_casa(lin_f+1, col_i)) != ".":
            return False
        if obtem_letra(tab, cria_casa(lin_i-1, col_i))!= ".":
            return False
    if d == "H":
        if col_i==1:
            if col_f==15:
                return True
            if obtem_letra(tab, cria_casa(lin_i, col_f+1)) == ".":
                return True
            return False
        if col_f==15:
            if col_i==1:
                return True
            if obtem_letra(tab, cria_casa(lin_i, col_i-1))== ".":
                return True
            return False 
        if obtem_letra(tab, cria_casa(lin_i, col_f+1)) != ".":
            return False
        if obtem_letra(tab, cria_casa(lin_i, col_i-1))!= ".":
            return False
    return True
    
    
def obtem_subpadroes(t, i, f, l):
    direc = aux_direcao(i, f)
    padroes = []
    casas = []
    if direc == "H":
        for inicio in range(obtem_col(i), obtem_col(f)+1):
            for fim in range(obtem_col(f), inicio-1, -1):
                casa_i = cria_casa(obtem_lin(i), inicio)
                casa_f = cria_casa(obtem_lin(i), fim)
                padrao = obtem_padrao(t, casa_i, casa_f)
                if padrao and filtra_padrao(t, padrao, l, casa_i, casa_f, direc):
                    padroes.append(padrao)
                    casas.append(casa_i)
    else: 
        for inicio in range(obtem_lin(i), obtem_lin(f)+1):
            for fim in range(obtem_lin(f), inicio-1, -1):
                casa_i = cria_casa(inicio, obtem_col(i))
                casa_f = cria_casa(fim, obtem_col(i))
                padrao = obtem_padrao(t, casa_i, casa_f)
                if padrao and filtra_padrao(t, padrao, l, casa_i, casa_f, direc):
                    padroes.append(padrao)
                    casas.append(casa_i)
    return tuple(padroes), tuple(casas)


def gera_todos_padroes(t, l):
    padroes_list = []
    casas_list = []
    direcoes_list = []
    limite = base_tab + 1  
    for linha in range(1, limite):
        casa_i = cria_casa(linha, 1)
        casa_f = cria_casa(linha, base_tab)
        padroes, casas = obtem_subpadroes(t, casa_i, casa_f, l)
        padroes_list.extend(padroes)
        casas_list.extend(casas)
        direcoes_list.extend(("H",) * len(padroes)) 
    for coluna in range(1, limite):
        casa_i = cria_casa(1, coluna)
        casa_f = cria_casa(base_tab, coluna)
        padroes, casas = obtem_subpadroes(t, casa_i, casa_f, l)
        padroes_list.extend(padroes)
        casas_list.extend(casas)
        direcoes_list.extend(("V",) * len(padroes))
    return tuple(padroes_list), tuple(casas_list), tuple(direcoes_list)


#2.2.1
def baralha_saco(seed):
    def gera_numero_aleatorio(estado):
        estado ^= ( estado << 13 ) & 0xFFFFFFFF
        estado ^= ( estado >> 17 ) & 0xFFFFFFFF
        estado ^= ( estado << 5  ) & 0xFFFFFFFF
        return  estado
    def permuta_letras(letras, state):
        for i in range(len(letras) - 1, 0, -1):
            state = gera_numero_aleatorio(state)
            j = state % (i + 1)
            letras[i], letras[j] = letras[j], letras[i]
        return 
    def baralha_conjunto(conj, estado):  
        letras=[]
        for i in conj.items():
            letras+=[i[0]]*i[1]
        permuta_letras(letras, estado)
        return letras
    return baralha_conjunto(saco, seed)


def jogada_humano(tab, jog, vocab, pilha):
    while True:
        resposta = input("Jogada " + jogador_identidade(jog) + ": ")
        resposta = resposta.split()
        while True:
            if len(resposta)!=0:
                break
        if resposta[0] == 'P':
            if len(resposta) != 1:
                continue
            return False
        if resposta[0] == "T":
            if not all(l in jogador_letras(jog) for l in resposta[1:]):
                continue
            for elemento in resposta[1:]:  
                usa_letra(jog, elemento)
            distribui_letras(jog, pilha, len(resposta)-1)
            return True
        if resposta[0]=="J":
            if len(resposta)!=5:
                continue
            d=resposta[3]
            palavra=resposta[4]
            casa_i=cria_casa(int(resposta[1]), int(resposta[2]))
            if eh_tabuleiro_vazio(tab):
                if d=="H" and obtem_lin(casa_i) != 8:
                    continue
                if d=="V" and obtem_col(casa_i) != 8:
                    continue
                if d=="H" and obtem_lin(casa_i)+len(palavra) > 15:
                    continue
                if d=="V" and obtem_col(casa_i)+len(palavra) > 15:
                    continue
                if not all(l in jogador_letras(jog) for l in palavra):
                    continue
                for elemento in palavra:  
                    usa_letra(jog, elemento)
                distribui_letras(jog, pilha, len(palavra))
                insere_palavra(tab, casa_i, d, palavra)
                soma_pontos(jog, obtem_pontos(vocab, palavra))
                return True
            padrao=obtem_padrao(tab, casa_i, incrementa_casa(casa_i, d, len(palavra)-1))
            if not testa_palavra_padrao(vocab, palavra, padrao,jogador_letras(jog)):
                    continue
            soma=0
            for i in range(len(palavra)):                
                if palavra[i] != padrao[i]:
                    usa_letra(jog, palavra[i])
                    soma+=1
            distribui_letras(jog, pilha, soma)
            insere_palavra(tab, casa_i, d, palavra)
            soma_pontos(jog, obtem_pontos(vocab, palavra))
            return True


def jogada_agente(tab, jog, vocab, pilha):                               
    m_palavra=""
    m_casa=()
    direcao=""
    m_padrao=""
    letras=jogador_letras(jog)
    pontos=obtem_pontos(vocab, m_palavra)
    if eh_tabuleiro_vazio(tab):
        print("Jogada " + jogador_identidade(jog) + ": P")
        return False
    if jogador_identidade(jog)=="FACIL":
        padroes, casas, direcoes = gera_todos_padroes(tab, len(letras))
        padroes = padroes[::100]
        casas = casas[::100]
        direcoes = direcoes[::100]
    if jogador_identidade(jog)=="MEDIO":
        padroes, casas, direcoes = gera_todos_padroes(tab, len(letras))
        padroes = padroes[::50]
        casas = casas[::50]
        direcoes = direcoes[::50]
    if jogador_identidade(jog)=="DIFICIL":
        padroes, casas, direcoes = gera_todos_padroes(tab, len(letras))
        padroes = padroes[::10]
        casas = casas[::10]
        direcoes = direcoes[::10]
        
    for padrao in padroes:
        palavra_pontos=procura_palavra_padrao(vocab, padrao, letras, pontos+1)
        if testa_palavra_padrao(vocab, palavra_pontos[0], padrao, letras):
            if palavra_pontos[1]>obtem_pontos(vocab, m_palavra):
                m_palavra=palavra_pontos[0]
                indice = padroes.index(padrao)
                m_casa=casas[indice]
                direcao=direcoes[indice]
                m_padrao=padrao
    #jogar
    if m_palavra != "":
        soma=0
        for i in range(len(m_palavra)):                
                if m_palavra[i] != m_padrao[i]:
                    usa_letra(jog, m_palavra[i])
                    soma+=1
        distribui_letras(jog, pilha, soma)
        insere_palavra(tab, m_casa, direcao, m_palavra)
        soma_pontos(jog, obtem_pontos(vocab, m_palavra))
        print("Jogada " + jogador_identidade(jog) + ": J" + " " +str(obtem_lin(m_casa)) + " " + str(obtem_col(m_casa)) + " " + direcao + " " + m_palavra)
        return True
    #Trocar
    if len(pilha) >=7:
        print("Jogada " + jogador_identidade(jog) + ": T " + " ".join(letras))
        for letra in letras:
            usa_letra(jog, letra)
        distribui_letras(jog, pilha, 7)
        return True
    #Passar
    else:
        print("Jogada " + jogador_identidade(jog) + ": P")
        return False


def scrabble2(jogadores, nome_fich, seed):                              
    vocab=ficheiro_para_vocabulario(nome_fich)
    lista_jogadores=[]
    saco_jogo= baralha_saco(seed)
    if type(jogadores) != tuple:
        raise ValueError ("scrabble2: argumentos inválidos")
    if type(nome_fich) != str:
        raise ValueError ("scrabble2: argumentos inválidos")
    if type(seed) != int or seed<1:
        raise ValueError ("scrabble2: argumentos inválidos")
    if 2>len(jogadores)>4:
        raise ValueError ("scrabble2: argumentos inválidos")
    for nome in jogadores:
        if nome[0]=="@":
            lista_jogadores.append(cria_agente(nome[1:]))
            
        else:
            lista_jogadores.append(cria_humano(nome))   
    tab=cria_tabuleiro()
    print("Bem-vindo ao SCRABBLE2.")
    print(tabuleiro_para_str(tab))
    for jog in lista_jogadores:
        distribui_letras(jog, saco_jogo, 7)
        print(jogador_para_str(jog))
    soma_passagens=0
    jogo=True
    while jogo:
        for jog in lista_jogadores:
            if eh_agente(jog):
                jogada=jogada_agente(tab, jog, vocab, saco_jogo)
                if not jogada:
                    soma_passagens+=1
            else:
                jogada=jogada_humano(tab, jog, vocab, saco_jogo)
                if not jogada:
                    soma_passagens+=1
            if soma_passagens==len(lista_jogadores) or jogador_letras(jog)==[]:
                jogo=False
                break
            else:
                soma_passagens=0
            print(tabuleiro_para_str(tab))
            for jog in lista_jogadores:
                print(jogador_para_str(jog))
    pontos = ()
    for j in lista_jogadores:
        pontos += (jogador_pontos(j),)
    return pontos           
