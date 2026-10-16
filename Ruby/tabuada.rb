numero = gets.chomp.to_i

puts "Tabuada do #{numero}:"

for i in 1..10
  puts "#{numero} x #{i} = #{numero * i}"
end