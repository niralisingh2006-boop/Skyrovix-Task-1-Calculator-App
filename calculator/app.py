from dataclasses import dataclass
@dataclass
class Calculation: expression:str; result:float
class Calculator:
 def __init__(self): self.history=[]
 def calculate(self,a,op,b):
  if op=='+': r=a+b
  elif op=='-': r=a-b
  elif op=='*': r=a*b
  elif op=='/':
   if b==0: raise ZeroDivisionError('Cannot divide by zero.')
   r=a/b
  elif op=='%':
   if b==0: raise ZeroDivisionError('Cannot use modulo with zero.')
   r=a%b
  elif op=='**': r=a**b
  else: raise ValueError('Unsupported operator.')
  self.history.append(Calculation(f'{a} {op} {b}',r)); return r
 def clear_history(self): self.history.clear()
 def show_history(self):
  if not self.history: print('No calculations in history.'); return
  for i,x in enumerate(self.history,1): print(f'{i}. {x.expression} = {x.result:g}')
def num(prompt):
 while True:
  try:return float(input(prompt))
  except ValueError: print('Please enter a valid number.')
def run():
 c=Calculator()
 while True:
  print('\n=== CLI Calculator ===\n1. Calculate\n2. History\n3. Clear history\n4. Exit')
  ch=input('Select an option: ').strip()
  if ch=='1':
   a=num('Enter first number: '); op=input('Enter operator (+, -, *, /, %, **): ').strip(); b=num('Enter second number: ')
   try: print(f'Result: {c.calculate(a,op,b):g}')
   except (ValueError,ZeroDivisionError) as e: print('Error:',e)
  elif ch=='2':c.show_history()
  elif ch=='3':c.clear_history(); print('History cleared.')
  elif ch=='4':break
  else:print('Invalid menu option.')
