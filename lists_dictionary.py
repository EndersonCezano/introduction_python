emails = {"Diego": "diego@gmail.com"}
print(emails['Diego'])

emails2 = {"Diego": "diego@gmail.com", "Abreu": "abreu@gmail", "Goyas": "ecezano@bol.com"}
print(emails2)

# dicionarios em python
dicionario_sites = {"Diego": "diegomariano.com", "Google": "google.com", "Udemy": "udemy.com"}
for chave in dicionario_sites:
    print(dicionario_sites[chave])

# itens separadamente
for i in dicionario_sites.items():
    print(i)

# chaves
for c in dicionario_sites.keys():
    print(c)

# valores 
for v in dicionario_sites.values():
    print(v)
