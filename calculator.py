def add(x,y):
	return(x+y)
def sub(x,y):
	return(x-y)
def multi(x,y):
	return(x*y)
def div(x,y):
	return(x/y)
while True:
 print("\n select operation \n 1.addition \n 2.subraction \n 3.multiplication \n 4.divition\n 5.Exit \n")
 try:
  choice=int(input('enter choice(1,2,3,4,5)'))
  if choice==5:
      print("Exit")
      break
  
  x=int(input('enter the number:'))
  y=int(input('enter the number:'))
 
  if(choice== 1):
	  print(x,'+',y,'=',add(x,y))
  elif(choice== 2):
	  print(x,'-',y,'=',sub(x,y))
  elif(choice== 3):
	  print(x,'x',y,'=',multi(x,y))
  elif(choice== 4):
	  print(x,'/',y,'=',div(x,y))
        
  else:
	  print('invalid choice')
 except Exception as e:
     print("something wrong",e)
