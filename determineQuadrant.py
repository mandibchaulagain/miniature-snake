def main():
  x,y=map(int,input("Enter x, y coordinates: ").split())
  if (x==0 and y==0):print("At origin.")
  elif(x>=0 and y>=0):print("In the first quadrant.")
  elif (x<=0 and y>=0):print("In the second quadrant.")
  elif (x<=0 and y<=0):print("In the third quadrant.")
  elif (x>=0 and y<=0):print("In the fourth quadrant.")
main()