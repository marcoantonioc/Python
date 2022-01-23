def frase(msg):
    tam=len(msg)+4
    print(f"="*tam)
    print(f"  {msg}")
    print(f"="*tam)


ok=str(input("Indique uma frase: "))

frase(ok)

