loop do
  hora = Time.now.strftime("%H:%M:%S")
  
  print "\r#{hora}"
  
  sleep 1
end