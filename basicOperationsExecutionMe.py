def opfun(number,e):
  if e==1:
    main()
  if number==1:
    x,y=map(int,input("Enter two numbers:").split())
    opfun1(x,y)
    return
  else:
    exitw=int(input("Enter 10 to exit and 11 to try again:"))
    if exitw==10:
      print("Program terminated.")
      exit()
    elif exitw==11: 
      e+=1
      opfun(number,e)
def opfun1(x,y):
  n=int(input("""Enter 1 for addition, 2 for subtraction, 3 for mulitiplication and 4 for division:"""))
  if(n==1):print("Addition={}".format(x+y))
  elif(n==2):print("Subtraction={}".format(x-y))
  elif(n==3):print("Multiplication={}".format(x*y))
  elif(n==4):print("Division={}".format(x/y))
  else:print("Entered an incorrect number.")
def main():
  number=int(input("Enter 1 to enter 2 numbers:"))
  opfun(number,e=0)
main()