lista = []

# 1. Guarda os 5 nomes na lista
5.times do
  entrada = gets.chomp
  lista << entrada
end

# 2. Mostra os nomes da lista
num = 1
lista.each do |pessoa|
  puts "Pessoa #{num} - #{pessoa}"
  num = num + 1
end
