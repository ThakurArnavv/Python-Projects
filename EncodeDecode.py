#still learning python and will add more easy commands to this code once i master them ....

va=int(input("Press 1 for Encoding and 2 for Decoding: "))
st=input("Enter the message: ")

if(va==1 and len(st)>=3):
  st_1=st[1:]+st[0]             #will add append command to this 
  st_2="abc"+st_1+"xyz"
  print(st_2)

elif(va==1 and len(st)<3 or va==2 and len(st)<3):
    print(st[::-1])   


else:
  st_3=st[3:-3]
  st_4=st_3[-1]+st_3[:-1]      #will add append here 
  print(st_4)

  