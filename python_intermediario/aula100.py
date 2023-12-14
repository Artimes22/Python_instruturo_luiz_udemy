# Exercícios
# Aumente os preçõs dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# Ordene os produtos por nome decrescente (do maior para o menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preço crescente ( do menor para o maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
from dados import produtos
import copy

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)} 
    for p in copy.deepcopy(produtos)

    
    ]
print('Produtos originais')
print(*produtos, sep='\n')
print()
print('Produtos com acrescimo de 10%')
print(*novos_produtos, sep='\n')
#-=-=-=PRONTO=-=-=-
produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos), 
    key=lambda item: item['nome'],
    reverse = True
    )
print()    
produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos), 
    key=lambda item: item['preco']
)
print('Produtos por ordem de nome')
print(*produtos_ordenados_por_nome, sep='\n')
print()
print('Produtos por ordem de preço')
print(*produtos_ordenados_por_preco, sep='\n')