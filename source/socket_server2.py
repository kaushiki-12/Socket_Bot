import socket
from firebase import firebase

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),9999))
s.listen(5)

def fire():
    
    firebases=firebase.FirebaseApplication('https://freeloan-aoyika.firebaseio.com/', None)
    #payment_confirmation= firebase.get('data','')
    
    conversation_data=firebases.get('data','')
    
    for fd in conversation_data.items():
        try:
            if   fd[0] == 'user':
                messg=conversation_data['user']
            elif fd[0] == 'welcome':
                messg  =conversation_data ['welcome'] 
            elif fd[0] == 'bot_call_reason':
                messg  = conversation_data['bot_call_reason']
            elif fd[0] == 'user_name_verification':
                messg  = conversation_data['user_name_verification']
            
                
            elif fd[0] == 'Customer_confirmation_repayment':
                messg  = conversation_data['Customer_confirmation_repayment']
            
                
            
           # print(messg)
            else:
               l=[]
               p=[]
               print(fd[0])
               for i in conversation_data.keys():
                   l.append(i)
               print(l)
               for j in conversation_data.values():
                   p.append(j)
               time=p[1]
               messg=("Sir please make sure that you are making the payment\
                 by the time you had told that is "+time+"  I’m updating the time \
                 to clear your file for next loan ")
                
                
            print(messg)
            
        except Exception as e:
            print(f"Someting went wrong while fetching the data {e}")
            messg = "not found data"
    return messg
out=fire()

while True:
    clientsocket,address=s.accept()
    print(f"Connection from {address}has been established")
    

    clientsocket.send(bytes(out,"utf-8"))
    clientsocket.close()
        

#message_box=firebase_socket()