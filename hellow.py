useMS = input("메세지를 입력하세요:")

if useMS != ("") :
    OP=open("talk.txt", 'w')
    OP.write(useMS)
    OP.close()
else :
    useMS == ("")
    print("메세지내용이 없습니다.")
    
    
    