from collections import deque


def verificar_simbolos_balanceados(expressao):
    pilha_abre = deque()

    for caracter in expressao:
        if caracter in ("(", "[", "{"):
            pilha_abre.append(caracter)

        if caracter in (")", "]", "}"):
            if len(pilha_abre) > 0:
                aberto = pilha_abre.pop()
                if aberto == "(" and caracter != ")":
                    return "Expressao mal formada"
                elif aberto == "[" and caracter != "]":
                    return "Expressao mal formada"
                elif aberto == "{" and caracter != "}":
                    return "Expressao mal formada"
            else:
                return "Expressao mal formada"

    if len(pilha_abre) > 0:
        return "Expressao mal formada"
    else:
        return "Expressao bem formada"

if __name__ == "__main__":
    expressao = "(((())))"
    print(verificar_simbolos_balanceados(expressao))
    expressao = "{[()]}"
    print(verificar_simbolos_balanceados(expressao))
    expressao = "{}"
    print(verificar_simbolos_balanceados(expressao))
    expressao = "[][]{}"
    print(verificar_simbolos_balanceados(expressao))
    expressao = "{[][]{}"
    print(verificar_simbolos_balanceados(expressao))
    expressao = "[][]{}}}}"
    print(verificar_simbolos_balanceados(expressao))
    expressao = "{[(()]}"
    print(verificar_simbolos_balanceados(expressao))
    expressao = "[2 * (3 + 4)]"
    print(verificar_simbolos_balanceados(expressao))

