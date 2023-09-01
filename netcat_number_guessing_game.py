# Gerar números aleatórios e mostrar a flag se acertar o número
# Importando as bibliotecas necessárias
import os  # Importa o módulo 'os' para interagir com o sistema operacional
import random  # Importa o módulo 'random' para gerar números aleatórios
import subprocess  # Importa o módulo 'subprocess' para executar comandos externos

# Função para gerar uma lista de 3 números inteiros aleatórios entre 1 e 100
def generate_random_numbers():
    return [random.randint(1, 100) for _ in range(3)]

# Função para enviar números via 'nc' (netcat) para um endereço e porta específicos
def send_numbers_via_nc(numbers):
    # Inicializa um processo 'nc' com entrada e saída de texto
    nc_process = subprocess.Popen(['nc', 'endereço', 'porta'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    # Gera uma string com os números aleatórios separados por quebras de linha
    input_data = '\n'.join(map(str, numbers)) + '\n'
    # Envia os números para o processo 'nc'
    nc_process.stdin.write(input_data)
    nc_process.stdin.flush()
    # Lê a saída do processo 'nc'
    output = nc_process.stdout.read()
    # Fecha os canais de entrada e saída do processo 'nc'
    nc_process.stdin.close()
    nc_process.stdout.close()
    return output

# Função principal
def main():
    flag_found = False  # Inicializa uma variável para verificar se a flag foi encontrada
    while not flag_found:  # Entra em um loop até que a flag seja encontrada
        random_numbers = generate_random_numbers()  # Gera números aleatórios
        response = send_numbers_via_nc(random_numbers)  # Envia os números e obtém a resposta

        # Verifica se a resposta contém a string 'ALQ{'
        if 'ALQ{' in response:
            flag_start = response.index('ALQ{')  # Encontra o início da flag
            flag_end = response.index('}', flag_start)  # Encontra o fim da flag
            flag = response[flag_start:flag_end+1]  # Extrai a flag
            flag_found = True  # Define a flag como encontrada
            print("Flag encontrada:", flag)  # Imprime a flag encontrada
        else:
            print("Tentativa:", random_numbers, "Resposta:", response)  # Imprime informações da tentativa

if __name__ == "__main__":
    main()  # Chama a função principal se o programa for executado diretamente