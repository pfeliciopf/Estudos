require 'securerandom'

senha_simples=SecureRandom.alphanumeric(8)
puts "senha: #{senha_simples}"