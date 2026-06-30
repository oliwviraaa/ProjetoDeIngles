import explicacoesA1
print("                     EXPLICADOR DE CONTÉUDO DE INGLÊS    ")
print("--" *40)
nome_aluno=str(input("Olá! Qual é seu nome? ")).strip().title()


print("Welcome, {}".format(nome_aluno))
print("     Este programa te ajudará a entender conteúdos de inglês de forma simples")
print("     Basta selecionar o seu  nível de inglês e escolher o conteúdo que deseja")
print("--" *40)

while True:
    print("                         MENU DE OPÇÕES")
    print("--" *40)
    print("     1. Iniciante (NÍVEL A1)")
    print("     2. Básico (NÍVEL A2)")
    print("     3. Intermediário (NÍVEL B1)")
    print("     4. Intermediário Avançado (NÍVEL B2)")
    print("     5. Avançado (NÍVEL C1)")
    print("     6. Fluência (NÍVEL C2)")
    print("     7. Sair do programa")

    try:
        op =int(input("Escolha a opção (1 a 6): "))
    except ValueError:
        print("\n[!] Digite um número válido!")
    if op == 7:
        print("See you later, {}".format(nome_aluno))
        break
    
    if op == 1:
        while True:
            print("\n" + "--" * 40)
            print("                    CONTEÚDOS DISPONÍVEIS: Iniciante")
            print("--" * 40)
                
            print("A. VERB TO BE")
            print("B. PRESENT SIMPLE")            
            print("C. PRESENT CONTINUOUS")            
            print("D. MODAL CAN/CAN'T")            
            print("E.PRONOMES PESSOAIS")            
            print("F. PRONOMES E ADJETIVOS POSSESSIVOS")            
            print("G. PRONOMES DEMONSTRATIVOS")            
            print("H. WH-QUESTIONS")            
            print("I. ARTIGOS")            
            print("J. SUBSTANTIVOS PLURAIS")            
            print("K. PREPOSIÇÕES DE LUGAR BÁSICAS")           
            print("L. IMPERATIVOS")            
            print("M. ADJETIVOS DE INTENSIDADE")            
            print("N. VOCABULARIOS ESSENCIAIS")
            print("     X. Voltar ao Menu Principal")
            print("--" * 40)
                
            sub_op = str(input("Escolha a letra do conteúdo: ")).strip().upper()
                
            if sub_op == "X":
                break
                    
            if sub_op in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]:
                # Vai lá no outro arquivo e busca a explicação da letra escolhida
                explicacoesA1.mostrar_conteudos(sub_op, nivel=1)
            else:
                print("\n[!] Letra inválida! Escolha de A a N ou X para voltar.")

    elif op == 2:
        while True:
            print("\n" + "--" * 40)
            print("                    CONTEÚDOS DISPONÍVEIS: BÁSICO")
            print("--" * 40)
                
            print("A. VERB TO BE")
            print("B. PRESENT SIMPLE")            
            print("C. PRESENT CONTINUOUS")            
            print("D. MODAL CAN/CAN'T")            
            print("E.PRONOMES PESSOAIS")            
            print("F. PRONOMES E ADJETIVOS POSSESSIVOS")            
            print("G. PRONOMES DEMONSTRATIVOS")            
            print("H. WH-QUESTIONS")            
            print("I. ARTIGOS")            
            print("J. SUBSTANTIVOS PLURAIS")            
            print("K. PREPOSIÇÕES DE LUGAR BÁSICAS")           
            print("L. IMPERATIVOS")            
            print("M. ADJETIVOS DE INTENSIDADE")            
            print("N. VOCABULARIOS ESSENCIAIS")
            print("     X. Voltar ao Menu Principal")
            print("--" * 40)
                
            sub_op = str(input("Escolha a letra do conteúdo: ")).strip().upper()
                
            if sub_op == "X":
                break
                    
            if sub_op in ["A", "B", "C", "D", "E", "F"]:
                # Vai lá no outro arquivo e busca a explicação da letra escolhida
                explicacoesA1.mostrar_conteudos(sub_op, nivel=2)
            else:
                print("\n[!] Letra inválida! Escolha de A a F ou X para voltar.")