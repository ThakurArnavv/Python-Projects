import random

print('Lets Play Snake Water Gun ')

def get_choices(comp,user):  #1=User Win, 0=Draw, -1=UserLose
  if comp==0 and user==0:
    return 0
  if comp==1 and user==0:
    return 1
  if comp==-1 and user==1:
    return -1
  if comp==0 and user==1:
    return 1

comp=random.randint(-1,1)
user=int(input('Enter Your Action: 0 for snake , 1 for water , -1 for gun: '))

score=get_choices(comp,user)
print('You:' ,user)
print('Computer:' ,comp)

if (score==0):                    #Will add more easy commands once i master them 
  print('Draw')    
elif (score==1):
  print('User Wins')
else:
  print('User Loses')