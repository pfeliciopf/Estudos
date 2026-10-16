puts "Qual o valor de a:"
a = gets.to_i

puts "Qual o valor de b:"
b = gets.to_i

puts "Qual o valor de c:"
c = gets.to_i

delta = (b**2) - (4 * a * c)

puts "Delta = #{delta}"

if delta < 0
  puts "A equação não possui raízes reais"
elsif delta == 0
  x = -b.to_f / (2 * a)
  puts "A raiz é: #{x}"
else
  x1 = (-b + Math.sqrt(delta)) / (2 * a)
  x2 = (-b - Math.sqrt(delta)) / (2 * a)

  puts "x1 = #{x1}"
  puts "x2 = #{x2}"
end