# Calculadora Simples em Ruby

puts "=== CALCULADORA ==="

print "Digite o primeiro número: "
num1 = gets.to_f

print "Digite a operação (+, -, *, /): "
operacao = gets.chomp

print "Digite o segundo número: "
num2 = gets.to_f

case operacao
when "+"
  resultado = num1 + num2
  puts "Resultado: #{resultado}"

when "-"
  resultado = num1 - num2
  puts "Resultado: #{resultado}"

when "*"
  resultado = num1 * num2
  puts "Resultado: #{resultado}"

when "/"
  if num2 != 0
    resultado = num1 / num2
    puts "Resultado: #{resultado}"
  else
    puts "Erro: divisão por zero!"
  end

else
  puts "Operação inválida!"
end