import random


# DADOS DO SISTEMA
usuario = {
    "nome": "",
    "habilidades": [],
    "interesses": [],
    "estilo": ""
}
carreira_escolhida = None
plano = []

# DICIONÁRIO COMPLETO DE CARREIRAS
carreiras = {

        "Desenvolvedor Backend": ["Python", "APIs", "Git", "Banco de Dados"],
        "Desenvolvedor Frontend": ["HTML", "CSS", "JavaScript", "Design Responsivo"],
        "Desenvolvedor Fullstack": ["HTML", "CSS", "JavaScript", "Python", "APIs"],
        "Cientista de Dados": ["Python", "Estatística", "Machine Learning", "Pandas"],
        "Analista de Dados": ["Excel", "SQL", "Python", "Dashboard"],
        "Engenheiro de Dados": ["Python", "SQL", "Pipelines", "Cloud"],
        "UX/UI Designer": ["Figma", "Design Thinking", "Prototipação"],
        "QA / Tester": ["Testes Automatizados", "Selenium", "Lógica"],
        "Cybersegurança": ["Redes", "Pentest", "Criptografia"],
        "DevOps": ["Cloud", "CI/CD", "Containers"],
        "Técnico de Informática": ["Hardware", "Manutenção", "Redes"],
        "Suporte Técnico": ["Atendimento", "Sistemas", "Resolução de Problemas"],
    }

# MENTORES

mentores = [
    {"nome": "Mateus Oliveira", "area": "Desenvolvedor Frontend"},
    {"nome": "Rogerio Nakata", "area": "Desenvolvedor Backend"},
    {"nome": "Camila Silva", "area": "Analista de Dados"},
    {"nome": "Pedro Costa", "area": "Cybersegurança"},
    {"nome": "Laura Puglli", "area": "Cientista de Dados"},
    {"nome": "Paulo Andrade", "area": "DevOps"},
    {"nome": "Marina Rossi", "area": "UX/UI Designer"},
]
mentores.extend(mentores_padrao)

# FUNÇÕES

def criar_perfil():
    usuario["nome"] = input("\nDigite seu nome: ")
    usuario["habilidades"] = [h.strip().title() for h in input("Habilidades (separadas por vírgula): ").split(",")]
    usuario["interesses"] = [i.strip().title() for i in input("Interesses: ").split(",")]
    usuario["estilo"] = input("Como você se define? (analítico, criativo, comunicador): ")

    print("\nPerfil criado com sucesso!\n")


def sugerir_carreira():
    global carreira_escolhida

    habilidades = usuario["habilidades"]
    opcoes = []

    # varre categorias
    for categoria, areas in carreiras.items():
        for carreira, skills in areas.items():
            for h in habilidades:
                if h in skills:
                    opcoes.append(carreira)
                    break

    if not opcoes:
        print("\nNenhuma carreira compatível encontrada.\n")
        return None

    print("\nCarreiras compatíveis com você:\n")
    for i, c in enumerate(opcoes, 1):
        print(f"{i}. {c}")

    escolha = int(input("\nEscolha sua carreira pelo número: ")) - 1

    if escolha < 0 or escolha >= len(opcoes):
        print("Opção inválida!\n")
        return None

    carreira_escolhida = opcoes[escolha]
    print(f"\n✔ Carreira escolhida: {carreira_escolhida}\n")

    return carreira_escolhida


def gerar_plano():
    global plano

    if not carreira_escolhida:
        print("\n⚠ Sugira e escolha uma carreira primeiro.\n")
        return

    # recuperar habilidades específicas dessa carreira
    habilidades = None
    for categoria, areas in carreiras.items():
        if carreira_escolhida in areas:
            habilidades = areas[carreira_escolhida]

    if habilidades is None:
        print("Erro ao encontrar habilidades da carreira.\n")
        return

    if not plano:
        tarefas_iniciais = random.sample(habilidades, k=min(2, len(habilidades)))
        plano = [{"tarefa": t, "feito": False} for t in tarefas_iniciais]

    print("\nSeu plano de ação:")
    for i, item in enumerate(plano, 1):
        status = "✔️" if item["feito"] else "❌"
        print(f"{i}. {item['tarefa']} [{status}]")

    if input("\nDeseja marcar tarefa como concluída? (s/n): ").lower() == "s":
        indice = int(input("Digite o número: ")) - 1
        if 0 <= indice < len(plano):
            plano[indice]["feito"] = True
            print("Tarefa concluída!")

            concluidas = all(t["feito"] for t in plano)
            ainda_faltam = len(plano) < len(habilidades)

            if concluidas and ainda_faltam:
                restantes = [h for h in habilidades if h not in [t["tarefa"] for t in plano]]
                nova = random.choice(restantes)
                plano.append({"tarefa": nova, "feito": False})
                print(f"\n🎉 Nova tarefa desbloqueada: {nova}")
        else:
            print("Número inválido!")


def ver_progresso():
    if not plano:
        print("\n⚠ Gere um plano primeiro.\n")
        return

    total = len(plano)
    feitos = sum(1 for t in plano if t["feito"])

    barra = "#" * feitos + "-" * (total - feitos)
    print(f"\nProgresso: [{barra}] {feitos}/{total} tarefas concluídas.\n")


def conectar_mentor():
    if not carreira_escolhida:
        print("\nEscolha uma carreira primeiro.\n")
        return

    print(f"\nMentores disponíveis para {carreira_escolhida}:\n")

    encontrados = [ m for m in mentores if carreira_escolhida.lower() in m["area"].lower()]

    if not(encontrados):
        print("\nNenhum mentor disponível para esta área\n")
        return
    for mento in encontrados:
        print(f"- {m['nome']} ({m['area']})")

    print()


def cadastrar_mentor():
    nome = input("\nDigite o nome do mentor: ")
    area = input("\nDigite o area do mentor: ")

    mentores.append({"nome": nome, "area": area})
    print("\nMentoria cadastrada com sucesso!\n")


# MENU


while True:
    print("=== LEVEL UP – ASSISTENTE DE CARREIRA ===")
    print("1. Criar Perfil")
    print("2. Sugestão de Carreira")
    print("3. Gerar Plano de Ação")
    print("4. Ver Progresso")
    print("5. Conectar com Mentor")
    print("6. Cadastrar Voluntariado Mentoria")
    print("7. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        criar_perfil()
    elif opcao == "2":
        sugerir_carreira()
    elif opcao == "3":
        gerar_plano()

    elif opc == "6":
        print("Saindo...")
        break
    else:
        print("Opção inválida!\n")
