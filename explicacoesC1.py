def mostrar_explicacoes(letra, nivel):
    if nivel == 5:
        match letra:
            case "A":
                print("INVERSION PARA ÊNFASE (ex: Never have I seen...)")
            case "B":
                print("CLEFT SENTENCES PARA FOCAR INFORMAÇÃO (ex: What I need is...)")
            case "C":
                print("SUBJUNCTIVE MOOD FORMAL (ex: I insist that he be here)")
            case "D":
                print("MODAIS AVANÇADOS E DE ARREPENDIMENTO (ex: Should have, Would rather)")
            case "E":
                print("PARTICIPLE CLAUSES PARA SINTETIZAR FRASES (ex: Having finished, she left)")
            case "F":
                print("CLÁUSULAS CONCESSIVAS AVANÇADAS (ex: Albeit, In spite of the fact that)")
            case "G":
                print("MIXED CONDITIONALS COMPLEXOS (passado influenciando o presente e vice-versa)")
            case "H":
                print("ESTRUTURAS DE WISHES E REGRETS AVANÇADA (ex: It’s high time...)")
            case "I":
                print("PASSIVA IMPESSOAL E CAUSATIVA AVANÇADA (ex: It is rumored that..., Get something done)")
            case "J":
                print("DIFERENÇAS SUTIS DE GERÚNDIO E INFINITIVO COM MUDANÇA DE SIGNIFICADO")
            case "K":
                print("DISTINÇÃO DE NUANCES (ex: Quite, Rather, Fairly, Somewhat)")
            case "L":
                print("EXPRESSÕES IDIOMÁTICAS AVANÇADAS E METÁFORAS LITERÁRIAS")
            case "M":
                print("DISCURSO FORMAL, ACADÊMICO E TÉCNICAS DE PERSUASÃO/DEBATE")
            case "N":
                print("COLLOCATIONS AVANÇADAS E PHRASAL VERBS DE NÍVEL NATIVO")
            
    