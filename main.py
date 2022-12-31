import threading

def get_input():
  global input_string
  input_string = input("Enter the string: ")

def reverse_string(input_string):
  print("Reversed String: ",input_string[::-1])

def capital_string(input_string):
  print("Capatalized String: ", input_string.upper())

def shift_string(input_string, a):
  shifted_string = ""
  for c in input_string:

    shifted_char = chr(ord(c) + a)

    shifted_string += shifted_char
  print("Shifted String: ",shifted_string)

input_thread = threading.Thread(target=get_input)

input_thread.start()

input_thread.join()

reverse_thread = threading.Thread(target=reverse_string, args=(input_string,))
capital_thread = threading.Thread(target=capital_string, args=(input_string,))
shift_thread = threading.Thread(target=shift_string, args=(input_string, 2))


reverse_thread.start()
capital_thread.start()
shift_thread.start()


reverse_thread.join()
capital_thread.join()
shift_thread.join()