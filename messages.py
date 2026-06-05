def show_help():
    print("""
Uso:
    python minimum_platforms.py
    ou
    python minimum_platforms.py <arquivo>
    ou
    python minimum_platforms.py -a 

Descrição:
    Calcula o número mínimo de plataformas necessárias
    a partir de um arquivo de horários de ônibus. Se nenhum arquivo for passado como paramêtro, calcula a solução para ./tests/test_0.txt
                  
Formato do arquivo:
    Cada linha deve conter:
    <horario_entrada> <horario_saida>
                  
Exemplo:
    06:10 06:45
    06:00 06:25
                  
Comandos:
    -h, --help      Mostra essa mensagem
    -a, --all       Calcula a solução para todos os arquivos de ./tests
""")
    

def show_exced_arguments_error(args: int):
    print(f"""
Erro: Número de argumentos excedeu o esperado. Esperava no máximo 1, recebeu {args}.
Para mais informações, execute minimum_platforms.py --help
""")
    

def show_solution_title():
    print('---------------------------- MINIMUM PLATFORMS SOLUTION ----------------------------\n')
