def inicializar_cache(tamanho_cache):
    cache = {}
    for i in range(tamanho_cache):
        cache[i] = -1
    return cache

def imprimir_cache(cache):
    print("Tamanho da Cache:".ljust(15), len(cache))
    print("Pos Cache | Posição Memória")
    for posicao, valor in cache.items():
        print(f"         {posicao}|             {valor}")

def mapeamento_direto(tamanho_cache, posicoes_memoria_acessar):
    cache = inicializar_cache(tamanho_cache)
    hits = 0
    misses = 0

    print("Estado Inicial da Cache:")
    imprimir_cache(cache)

    for posicao_memoria in posicoes_memoria_acessar:
        posicao_cache = posicao_memoria % tamanho_cache #item 4.d, da atividade
        if cache[posicao_cache] == posicao_memoria:
            hits += 1
            print(f"Hit! Endereço {posicao_memoria} já está na Cache.")
        else:
            misses += 1
            print(f"Miss! Endereço {posicao_memoria} não está na Cache. Adicionando...")

        cache[posicao_cache] = posicao_memoria
        print("Cache Atualizada:")
        imprimir_cache(cache)

    total_acessos = hits + misses
    taxa_hit = hits / total_acessos if total_acessos > 0 else 0

    print("\nResumo:")
    print("Total de posições de memória acessadas:", total_acessos)
    print("Total de hits:", hits)
    print("Total de misses:", misses)
    print("Taxa de cache hit:", taxa_hit)

# linha de testes luis
posicoes_memoria_acessar = [33,3,11,5]
tamanho_cache = 5
#posicoes_memoria_acessar =[0,1,2,2,22,32,42,20,1,10,11,12,13]
#tamanho_cache = 5
mapeamento_direto(tamanho_cache, posicoes_memoria_acessar)

#posicoes_memoria_acessar = [33,3,11,5]
#tamanho_cache = 5

#posicoes_memoria_acessar = [1,6,1,11,1,16,1,21,1,26]
#tamanho_cache = 5