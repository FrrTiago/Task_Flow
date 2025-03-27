from typing import List, Dict, Callable

# Definição de uma tarefa como um dicionário imutável
def criar_tarefa(titulo: str, descricao: str, status: str = "pendente") -> Dict[str, str]:
    return {"titulo": titulo, "descricao": descricao, "status": status}

# Função pura para adicionar uma tarefa a uma lista (imutável)
def adicionar_tarefa(lista: List[Dict[str, str]], tarefa: Dict[str, str]) -> List[Dict[str, str]]:
    return lista + [tarefa]

# Função pura para remover uma tarefa pelo título
def remover_tarefa(lista: List[Dict[str, str]], titulo: str) -> List[Dict[str, str]]:
    return [tarefa for tarefa in lista if tarefa["titulo"] != titulo]

# Função pura para listar todas as tarefas
def listar_tarefas(lista: List[Dict[str, str]]) -> None:
    for tarefa in lista:
        print(f"Título: {tarefa['titulo']}, Descrição: {tarefa['descricao']}, Status: {tarefa['status']}")

# Função pura para marcar uma tarefa como concluída
def concluir_tarefa(lista: List[Dict[str, str]], titulo: str) -> List[Dict[str, str]]:
    return [
        {**tarefa, "status": "concluída"} if tarefa["titulo"] == titulo else tarefa
        for tarefa in lista
    ]

# Função para filtrar tarefas por status
def filtrar_tarefas(lista: List[Dict[str, str]], status: str) -> List[Dict[str, str]]:
    return [tarefa for tarefa in lista if tarefa["status"] == status]

# Exemplo de uso
if __name__ == "__main__":
    tarefas = []
    tarefas = adicionar_tarefa(tarefas, criar_tarefa("Estudar Python", "Revisar programação funcional"))
    tarefas = adicionar_tarefa(tarefas, criar_tarefa("Ler livro", "Terminar capítulo 4"))
    listar_tarefas(tarefas)
    
    print("--- Concluindo tarefa ---")
    tarefas = concluir_tarefa(tarefas, "Estudar Python")
    listar_tarefas(tarefas)
    
    print("--- Tarefas pendentes ---")
    pendentes = filtrar_tarefas(tarefas, "pendente")
    listar_tarefas(pendentes)
    
    print("--- Removendo tarefa ---")
    tarefas = remover_tarefa(tarefas, "Ler livro")
    listar_tarefas(tarefas)
    
    print("--- Adicionando tarefa ---")
    tarefas = adicionar_tarefa(tarefas, criar_tarefa("Estudar Java", "Revisar programação orientada a objetos"))
    listar_tarefas(tarefas)
    
    print("--- Adicionando tarefa ---")
    tarefas = adicionar_tarefa(tarefas, criar_tarefa("Estudar C++", "Revisar programação orientada a objetos"))
    listar_tarefas(tarefas)
    
    print("--- Adicionando tarefa ---")
    tarefas = adicionar_tarefa(tarefas, criar_tarefa("Estudar C#", "Revisar programação orientada a objetos"))
    listar_tarefas(tarefas)

    print("--- Adicionando tarefa ---")
    tarefas = adicionar_tarefa(tarefas, criar_tarefa("Estudar Kotlin", "Revisar programação orientada a objetos"))
    listar_tarefas(tarefas)