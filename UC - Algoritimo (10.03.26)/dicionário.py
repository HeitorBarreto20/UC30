#sem dicionario
matricula1 = 2026001
nome = "Ana Silva"
telefonei1 = "9999 - 8888"

#com dicionario
aluno = {
    "matricula": 2026001,
    "nome": "Ana Silva",
    "telefone": "9999 - 8888"
}

print (aluno)

contato = {
    "@camila": "Camila",
    "@paola": "Paola",
    "@sheron": "Sheron",
    "@bruna": "Bruna",
    "@joao": "João"
}

print (contato)
print (type(contato))

#acesso direto ao dicionario
print (contato("@camila"))

#acesso seguro com get()
print (contato.get("@paola"))
print (contato.get("@inexistente"))
print (contato.get("@inexistente", "Não encontrado"))

print ("Original: ", contato) #acessando a lista original

#add novo elemento
contato ["@giovanna"] = "Giovanna"
print ("Após add: ", contato)

#atualizando elemnto existente
contato ["@paola"] = "Paola Oliveira"
print ("Após add: ", contato)

contato.update (
    {
        "@bruna": "Bruna Marquezine",
        "@camila": "Camila Q."
    }
)

print ("Após atualização: ", contato)

#pop: remova e retorna 
removido = contato.pop("@sheron")
print (f"Removido: {removido}")
print ("Após o pop: ", contato)

#del remove sem retornar
del contato ["@paola"]
print ("Após o del: ", contato)

#clear esvazia tudo
copia = dict (contato)
contato.clear()
print ("Após clear:", contato)
print ("Cópia: ", copia)

print ("Número de conato: ", len(contato))

contato.pop("@camila")
print ("Após remover um: ", len(contato))

#verificar existencia
if "@joao" in contato:
    print (f"Encontrado: {contato['"@joao']}")

if "@inexistnte" in contato:
    print ("Existe")
else: 
    print ("Não existe")

#dicionario vazio
vazio = {}

#dicionario com tipos mistos
dados = {
    "nome": "João",
    "idade": 25,
    "altura": 1.70,
    "ativo": True
}

print


("Vazio: ", vazio)
print ("Vazio: ", dados)

