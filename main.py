from cores import RESET, TITULO, FIZZ, BUZZ, FIZZBUZZ, NUMERO, DETALHE

print()
print(f"{TITULO}╭──────────────────────────────╮{RESET}")
print(f"{TITULO}│         F I Z Z  B U Z Z      │{RESET}")
print(f"{TITULO}╰──────────────────────────────╯{RESET}")
print(f"{DETALHE}  Contagem de 1 a 101{RESET}\n")

for numero in range(1, 101):
    if numero % 3 == 0 and numero % 5 == 0:
        resultado = f"{FIZZBUZZ}FIZZBUZZ{RESET}"
    elif numero % 3 == 0:
        resultado = f"{FIZZ}FIZZ{RESET}"
    elif numero % 5 == 0:
        resultado = f"{BUZZ}BUZZ{RESET}"
    else:
        resultado = f"{NUMERO}{numero}{RESET}"

    print(f"{DETALHE}{numero:>3}{RESET}  {resultado}")

print(f"\n{DETALHE}Regra: múltiplos de 3 = FIZZ · de 5 = BUZZ · de ambos = FIZZBUZZ{RESET}")
