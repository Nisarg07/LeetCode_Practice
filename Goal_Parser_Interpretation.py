class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        for i in range(len(command)):
            if command[i] == 'G':
                ans += 'G'
            elif command[i] == '(':
                continue
            elif command[i] == ')' and command[i-1] == 'l':
                ans += 'al'
            elif command[i] == ')':
                ans += 'o'
        return ans