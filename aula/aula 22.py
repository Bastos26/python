
from aula.pacotes.módulos.funçõs import fatorial
num = int(input("Digite um valor: "))
fat=fatorial(num)
print(f'O fatorial de {num} é {fat}')

# não necessáriamente o módulo que deseja importar deve estar em um folder diferente , podem estar na mesma , basta ser files diferentes
#mas esse caso somete se não houver pacotes
#para o python ,todo arquivo .py pode ser um módulo , basta ter funções nele
#estou tendo um certo tipo de problema para efetuar a inportação
#como visto lá em cima , existe muitas camadas para se lidar, creio que há maneiras para reduzir ese caminho
