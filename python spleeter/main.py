from spleeter.separator import Separator

# Cria o separador com o modelo de 2 stems (vocais e acompanhamento)
separator = Separator('spleeter:2stems')

# Caminho do arquivo de entrada e pasta de saída
entrada = 'musica.mp3'
saida = 'output/'

# Realiza a separação
separator.separate_to_file(entrada, saida)

print("Separação concluída!")
