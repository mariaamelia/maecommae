FAQS = {
    # Pergunta: Resposta
    "O que é o MãecomMãe?": (
        "MãecomMãe é um aplicativo que conecta mães para trocar serviços como cuidado com crianças, aulas e caronas. "
        "Ele cria uma rede de apoio confiável, permitindo que as usuárias ganhem créditos ao oferecer serviços e "
        "usem esses créditos dentro do sistema ou transfiram via Pix."
    ),
    "Como funciona o sistema de créditos?": (
        "Cada hora de serviço prestado gera créditos, que podem ser:\n"
        "1. Usados para pagar por outros serviços dentro do app\n"
        "2. Transferidos para dinheiro via Pix"
    ),
    "O MãecomMãe é gratuito?": (
        "Sim, o cadastro e o uso básico são gratuitos. "
        "Funcionalidades extras podem ter custos ou ser financiadas por apoiadores."
    ),
    "Quais serviços posso oferecer/solicitar?": (
        "Serviços disponíveis:\n"
        "- Cuidado com crianças\n"
        "- Reforço escolar\n"
        "- Aulas de dança/música\n"
        "- Caronas escolares\n"
        "- Outros serviços úteis entre mães"
    ),
    "Como confiar nas outras usuárias?": (
        "Garantimos segurança através de:\n"
        "✔ Verificação de perfis\n"
        "✔ Sistema de avaliações\n"
        "✔ Histórico de serviços prestados"
    ),
    "Como faço para me cadastrar?": (
        "Processo simples:\n"
        "1. Baixe o app\n"
        "2. Crie uma conta com dados básicos\n"
        "3. Complete seu perfil"
    ),
    "Como cancelar um serviço?": (
        "Você pode cancelar, mas:\n"
        "• Avise com antecedência\n"
        "• Cancelamentos em cima da hora podem afetar sua pontuação"
    ),
    "Empresas podem apoiar?": (
        "Sim! Empresas podem:\n"
        "• Financiar créditos para mães\n"
        "• Oferecer cashback\n"
        "• Tornar-se apoiadoras com selo social"
    ),
    "Disponibilidade no Brasil?": (
        "Estamos em expansão!\n"
        "Verifique a cobertura atual durante o cadastro no app."
    ),
    "Como falar com o suporte?": (
        "Dentro do app:\n"
        "→ Acesse 'Ajuda'\n"
        "→ Selecione 'Fale conosco'"
    )
}

def buscar_resposta_faq(pergunta_usuaria):
    """Busca a melhor correspondência para a pergunta do usuário"""
    pergunta_usuaria = pergunta_usuaria.lower().strip("?")
    
    # Verifica correspondência exata primeiro
    for pergunta, resposta in FAQS.items():
        if pergunta_usuaria == pergunta.lower():
            return resposta
    
    # Busca por palavras-chave se não encontrar exata
    palavras_chave = {
        "o que é": "O que é o MãecomMães?",
        "créditos": "Como funciona o sistema de créditos?",
        "gratuito": "O MãescomMães é gratuito?",
        "serviços": "Quais serviços posso oferecer/solicitar?",
        "confiar": "Como confiar nas outras usuárias?",
        "cadastrar": "Como faço para me cadastrar?",
        "cancelar": "Como cancelar um serviço?",
        "empresa": "Empresas podem apoiar?",
        "disponível": "Disponibilidade no Brasil?",
        "suporte": "Como falar com o suporte?",
    }
    
    for palavra, pergunta_faq in palavras_chave.items():
        if palavra in pergunta_usuaria:
            return FAQS[pergunta_faq]
    
    return None