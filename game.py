order = input('> ').lower().strip()
while order in ['help', 'start', 'stop', 'quit']:
  if order == 'help':
    print(' start - to start the car\n stop - to stop the car\n quit - to exit') 
  elif order == 'start':
    print("Car started ... Ready to go!")
  elif order == 'stop':
    print("Car stopped")
  elif order == 'quit':
    print("engine is exit")
  break
else:
  print("I don't understand that ...")