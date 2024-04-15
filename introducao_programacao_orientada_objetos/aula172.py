# os.path.getsize e os.stat para dados dos arquivos

import math

def formata_tamanho(tamanho_em_bytes: int, base: int = 1024) -> str:
    """Formata um tamanho, de bytes para o tamanho apropriado"""

    # Se o tamnho for menor ou igual a 0, 0B.
    if tamanho_em_bytes <= 0:
        return "0B"
    
    # Tupla com os tamanhos
    #                      0    1     2     3     4     5
    abreviacao_tamanhos = "B", "KB", "MB", "GB", "TB", "PB"

    # math.log vai retornar o logaritmo do tamanho_em_bytes
    # com base (1024 por padrão), isso deve bater
    # com o nosso índice na abreviação dos tamanhos
    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))
    # Por quanto nosso tamanho deve ser dividido para 
    # gerar o tamanho correto.
    potencia = base ** indice_abreviacao_tamanhos
    # Nosso tamanho final
    tamanho_final = round(tamanho_em_bytes / potencia, 2)
    # A abreviação que queremos
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final} {abreviacao_tamanho}'

print(formata_tamanho(1000))
print(formata_tamanho(1000000))
print(formata_tamanho(1000000000))