ASSUME:CS:CODE,DS:DATA
DATA SEGMENT
    org 2000h
        LIST DB 23h,45h,98h,68h,0A2H
    org 3000h
       positive DB 05H DUP(0)
DATA ENDS
CODE SEGMENT
    START:MOV AX,DATA
          MOV DS,AX
          MOV SI,OFFSET LIST
          MOV DI,OFFSET positive
          MOV CL,05H
BACK:
          MOV AL,[SI]
          ADD AL,01H
          JC REJECT
          SHR AL,1
          MOV [DX],AL
          INC DI
REJECT:
         INC CL   
          INC SI
          JNZ BACK
          HLT
CODE ENDS
END START                                               