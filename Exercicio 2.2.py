

from functools import reduce
def calcular_expressao(operacoes):

# operacoes é uma lista de tuplas: [(operador, valor), ...]
# Ex: [("+", 5), ("*", 2), ("-", 3)]
    def aplicar_operacao(acumulador, operacao_item):
        operador, valor = operacao_item
        if operador == "+":
           return acumulador + valor
        elif operador == "-":
            return acumulador - valor
    elif operador == "*":
        return acumulador * valor
    elif operador == "/":
        if valor == 0:
          raise ValueError("Divisão por zero!")
return acumulador / valor
else:
raise ValueError(f"Operador desconhecido:
{operador}")
# O valor inicial para reduce é o primeiro operando
if not operacoes:
    return 0
# Assume que o primeiro item da lista é o valor inicial
valor_inicial = operacoes[0][1] if operacoes[0][0] == "="
else 0 # Ou defina uma lógica para o primeiro valor
# Se o primeiro operador for '=', ele define o valor inicial
e as operações começam do segundo item
if operacoes[0][0] == "=":
    return reduce(aplicar_operacao, operacoes[1:],
                  valor_inicial)
else:
# Se não houver '=', assume-se que o primeiro valor é 0 e
a primeira operação é aplicada
return reduce(aplicar_operacao, operacoes, 0)
# Exemplo de uso
print("\n--- Calculadora de Expressões ---")
exp1 = [("=", 10), ("+", 5), ("*", 2), ("-", 3)] # (10 + 5) * 2 -
3 = 27
print(f"Resultado de {exp1}: {calcular_expressao(exp1)}") #
Saída: 27
exp2 = [("=", 20), ("/", 4), ("+", 10)] # 20 / 4 + 10 = 15
print(f"Resultado de {exp2}: {calcular_expressao(exp2)}") #
Saída: 15.0
exp3 = [("+", 5), ("-", 2)] # 0 + 5 - 2 = 3
print(f"Resultado de {exp3}: {calcular_expressao(exp3)}") #
Saída: 3
try:
    exp_div_zero = [("=", 10), ("/", 0)]
print(f"Resultado de {exp_div_zero}:
{calcular_expressao(exp_div_zero)}")
except ValueError as e:
print(f"Erro na expressão: {e}")