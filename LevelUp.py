usuario = {
    "nome": "",
    "habilidades": [],
    "interesses": [],
    "estilo": "",
    "pontos": 0
}

# DICIONÁRIO COMPLETO DE CARREIRAS

carreiras = {
    "Tecnologia": {
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
    },

    "Marketing e Comunicação": {
        "Analista de Marketing": ["SEO", "Copywriting", "Social Media", "Analytics"],
        "Produtor de Conteúdo": ["Roteiro", "Edição de Vídeo", "Storytelling"],
        "Designer Gráfico": ["Photoshop", "Illustrator", "Composição"],
        "Fotógrafo": ["Iluminação", "Edição", "Composição"],
        "Jornalista": ["Redação", "Entrevista", "Investigação"],
        "Publicitário": ["Criação", "Campanhas", "Branding"],
    },

    "Gestão e Negócios": {
        "Administrador": ["Gestão", "Finanças", "Estratégia"],
        "Gerente de Projetos": ["Scrum", "Kanban", "Liderança"],
        "Product Manager": ["Pesquisa", "Roadmap", "Visão de Produto"],
        "Marketing": ["Branding", "SEO", "Redes Sociais"],
        "Vendas / SDR": ["CRM", "Prospecção", "Negociação"],
        "Analista de RH": ["Recrutamento", "Entrevistas", "Treinamento"],
        "Assistente Administrativo": ["Excel", "Organização", "Comunicação"],
        "Auxiliar de Escritório": ["Rotinas Administrativas", "Digitação"],
        "Logística": ["Armazenamento", "Transportes", "Processos"],
        "Administração Pública": ["Políticas Públicas", "Documentação", "Gestão Pública"],
    },

    "Saúde": {
        "Médico": ["Clínica Geral", "Anatomia", "Diagnósticos"],
        "Enfermeiro": ["Cuidados", "Procedimentos", "Medicações"],
        "Técnico de Enfermagem": ["Atendimento", "Procedimentos", "Biossegurança"],
        "Psicólogo": ["Psicologia Clínica", "Atendimento", "Psiquiatria Básica"],
        "Nutricionista": ["Dietas", "Análise Nutricional", "Atendimento"],
        "Farmacêutico": ["Fármacos", "Manipulação", "Regulamentação"],
        "Fisioterapeuta": ["Reabilitação", "Avaliação Física", "Terapias"],
        "Esteticista": ["Limpeza de Pele", "Aparelhos", "Tratamentos", "Cuidados com a Pele"],
    },

    "Engenharias e Exatas": {
        "Engenheiro Civil": ["AutoCAD", "Cálculo", "Estruturas"],
        "Engenheiro Mecânico": ["Termodinâmica", "Materiais", "Projetos 3D"],
        "Engenheiro Elétrico": ["Circuitos", "Potência", "Eletrônica"],
        "Engenheiro de Produção": ["Lean", "Processos", "Gestão"],
        "Engenheiro Químico": ["Processos Industriais", "Termodinâmica"],
        "Analista de Qualidade": ["ISO", "Documentação", "Processos"],
        "Analista de Produção": ["Excel", "Lean", "Otimização"],
        "Engenheiro de Software": ["Cloud", "Arquitetura", "DevOps"],
    },

    "Humanas e Educação": {
        "Advogado": ["Direito Civil", "Penal", "Processos"],
        "Professor": ["Didática", "Planejamento", "Avaliação"],
        "Pedagogo": ["Educação Infantil", "Planejamento", "Psicopedagogia"],
        "Assistente Social": ["Atendimento", "Políticas Públicas", "Relatórios"],
        "Coach de Carreira": ["Escuta Ativa", "Planejamento", "Comunicação"],
        "Mentor Educacional": ["Orientação", "Didática", "Acompanhamento"],
    }
}

# MENTORES

mentores = [
    {"nome": "Mateus Oliveira", "area": "Desenvolvedor ", "categoria": "Tecnologia",
     "experiencia": "Sênior", "disponibilidade": "Manhã"},
    {"nome": "Camila Silva", "area": "Analista de Dados", "categoria": "Tecnologia",
     "experiencia": "Sênior", "disponibilidade": "Manhã"},
    {"nome": "Pedro Costa", "area": "Cybersegurança", "categoria": "Tecnologia",
     "experiencia": "Pleno", "disponibilidade": "Noite"},

    {"nome": "Mariana Akemi", "area": "Analista de Marketing", "categoria": "Marketing e Comunicação",
     "experiencia": "Sênior", "disponibilidade": "Noite"},
    {"nome": "Sophia Ramos", "area": "Designer Gráfico", "categoria": "Marketing e Comunicação",
     "experiencia": "Sênior", "disponibilidade": "Manhã"},

    {"nome": "Carlos Almeida", "area": "Administrador", "categoria": "Gestão e Negócios",
     "experiencia": "Sênior", "disponibilidade": "Manhã"},
    {"nome": "Vanessa Bianco", "area": "Gerente de Projetos", "categoria": "Gestão e Negócios",
     "experiencia": "Sênior", "disponibilidade": "Tarde"},

    {"nome": "Dra. Alice Mendes", "area": "Médico", "categoria": "Saúde",
     "experiencia": "Especialista", "disponibilidade": "Tarde"},
    {"nome": "Dr. Mario Antunes", "area": "Psicólogo", "categoria": "Saúde",
     "experiencia": "Sênior", "disponibilidade": "Noite"},

    {"nome": "Bruno Ferreira", "area": "Engenheiro Civil", "categoria": "Engenharias e Exatas",
     "experiencia": "Sênior", "disponibilidade": "Manhã"},
    {"nome": "Eduardo Toshio", "area": "Engenheiro Mecânico", "categoria": "Engenharias e Exatas",
     "experiencia": "Pleno", "disponibilidade": "Noite"},
    {"nome": "Jefferson Moreira", "area": "Engenheiro de Produção", "categoria": "Engenharias e Exatas",
     "experiencia": "Sênior", "disponibilidade": "Tarde"},

    {"nome": "Dra. Patrícia Kobayashi", "area": "Advogado", "categoria": "Humanas e Educação",
     "experiencia": "Sênior", "disponibilidade": "Noite"},
    {"nome": "Gisele Alves", "area": "Professor", "categoria": "Humanas e Educação",
     "experiencia": "Pleno", "disponibilidade": "Manhã"},
    {"nome": "Renata Pereira", "area": "Assistente Social", "categoria": "Humanas e Educação",
     "experiencia": "Pleno", "disponibilidade": "Tarde"}
]

# FUNÇÕES

def criar_perfil():
    usuario["nome"] = input("Digite seu nome: ")

    habilidades_brutas = input("Liste suas habilidades separadas por vírgula: ").split(",")
    usuario["habilidades"] = [h.strip().title() for h in habilidades_brutas]

    usuario["interesses"] = [i.strip().title() for i in input("Interesses: ").split(",")]
    usuario["estilo"] = input("Como você se define? (analítico, criativo, comunicador): ")

    print("\nPerfil criado com sucesso!\n")

def sugerir_carreira(usuario, carreiras):
    habilidades = usuario["habilidades"]
    opcoes = []

    # VARRE TODAS AS CATEGORIAS
    for categoria, areas in carreiras.items():
        # VARRE TODAS AS CARREIRAS DENTRO DA CATEGORIA
        for carreira, skills in areas.items():
            # Verifica se há pelo menos 1 habilidade em comum
            for h in habilidades:
                if h in skills:
                    opcoes.append(carreira)
                    break

    if not opcoes:
        print("\nNenhuma carreira compatível encontrada.")
        return None

    print("\nCarreiras compatíveis com você:\n")
    for i, c in enumerate(opcoes, 1):
        print(f"{i}. {c}")

    escolha = int(input("\nEscolha sua carreira pelo número: "))
    carreira_escolhida = opcoes[escolha - 1]

    print(f"\nCarreira escolhida: {carreira_escolhida}\n")

    return carreira_escolhida


#MENU

while True:
    print("=== Level Up – Assistente de Carreira ===")
    print("1. Criar Perfil")
    print("2. Sugestão de Carreira")
    print("3. Gerar Plano de Ação")
    print("4. Conectar com Mentor")
    print("5. Ver Progresso")
    print("6. Cadastrar Mentor Voluntário")
    print("7. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        criar_perfil()

    elif opcao == "2":

        carreira = sugerir_carreira(usuario, carreiras)

    elif opcao == "3":
        if 'carreira' in locals():
            gerar_plano(carreira)
        else:
            print("Sugira uma carreira primeiro.\n")

    elif opcao == "4":
        if 'carreira' in locals():
            conectar_mentor(carreira)
        else:
            print("Sugira uma carreira primeiro.\n")

    elif opcao == "5":
        ver_progresso()

    elif opcao == "6":
        cadastrar_mentor(mentores, carreiras)

    elif opcao == "7":
        print("Saindo...")
        break

    else:
        print("Opção inválida!\n")
