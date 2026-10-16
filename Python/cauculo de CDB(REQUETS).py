# CDI anual (exemplo)
cdi = 0.15  # 15% ao ano

valor = float(input("Valor investido: R$ "))
percentual = float(input("Percentual do CDB (% do CDI): "))

# Taxa anual do CDB
taxa = (percentual / 100) * cdi

# Rendimentos
ano = valor * taxa
mes = ano / 12
semana = ano / 52
dia = ano / 365

print("\n===== RESULTADO =====")
print(f"Taxa anual: {taxa*100:.2f}%")
print(f"Por dia: R$ {dia:.2f}")
print(f"Por semana: R$ {semana:.2f}")
print(f"Por mês: R$ {mes:.2f}")
print(f"Por ano: R$ {ano:.2f}")