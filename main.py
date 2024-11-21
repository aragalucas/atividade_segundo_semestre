nome = input("Nome: ")

try:
    idade = int(input("Idade: "))
    def idds(idade):
        if idade < 0:
            idade = "===numero negativo==="
        else:
            idade = ""
        return idade
    y = idds(idade)
    print(f"{y}") 
except ValueError:
    print("valuerror")