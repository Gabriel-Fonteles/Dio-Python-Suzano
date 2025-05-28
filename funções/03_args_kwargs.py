def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n" .join(args)
    meta_dados = "\n".join([f"{chave.title()} : {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)
    
    
    exibir_poema(
        "Sexta-Feira, 26 de Agosto de 2022",
        "Zen of Python",
        "Beautiful is better than ugly.",
        "Explicit is better than implicit.",
        "Simple is better than complex.",
        "Complex is better than complicated.",
        "Flat is better than nested.",
        "Sparse is better than dense.",
        "Readability counts.",
        "Special cases aren't special enough to break the rules.",
        "Although practicality beats purity.",
        "Erors should never pass silently.",
        "Unless explicitly silenced.",
        "In the face of ambiguity, refuse the temptation to guess.",
        autor="Tim Peters",
        ano=1999,
    )