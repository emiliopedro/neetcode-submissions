class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i].isnumeric() or ((len(tokens[i]) > 1) and (tokens[i][0] == '-')):
                stack.append(int(tokens[i]))

            else:
                a = stack.pop()
                b = stack.pop()

                if tokens[i] == "+":
                    result = b + a

                elif tokens[i] == "-":
                    result = b - a

                elif tokens[i] == "*":
                    result = b * a

                elif tokens[i] == "/":
                    result = abs(b) // abs(a)
                    if b / a < 0:
                        result *= -1
                
                stack.append(result)

        return stack[0]

        