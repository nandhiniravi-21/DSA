class Solution:
    def interpret(self, command: str) -> str:
        s=command.replace('()','o')
        t=s.replace('(al)','al')
        return t
        