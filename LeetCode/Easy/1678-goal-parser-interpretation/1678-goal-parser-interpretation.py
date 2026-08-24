class Solution:
    def interpret(self, command: str) -> str:
        string=""
        if len(command)==1:
            return "G"
        for i in range(len(command)-1):
            if command[i]=="G":
                string+="G"
            elif command[i]=='(' and command[i+1]==')':
                string+='o'
            elif command[i]=='(' and command[i+1]=="a":
                string+="al"
        if command[-1]=="G":
            string+="G"
        return string
        