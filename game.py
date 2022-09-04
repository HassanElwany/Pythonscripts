order = ""
started = False

while True:
  order = input('> ').lower().strip()
  if order == 'help':
    print(' start - to start the car\n stop - to stop the car\n quit - to exit') 
  elif order == 'start':
    if started:
      print("Car is already started")
    else:
      started = True
      print("Car started ... Ready to go!")
  elif order == 'stop':
    if not started:
       print("Car is already stopped")
    else:
       started = False
       print("Car stopped")
  elif order == 'quit':
    print("engine is exit")
    break
else:
  print("I don't understand that ...")