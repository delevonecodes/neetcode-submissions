class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        evaluation = []
        operands = ["-", "+", "/", "*"]
        for token in tokens:
            if token not in operands:
                evaluation.append(int(token))
            elif token == "-":
                num2 = evaluation.pop()
                num1 = evaluation.pop()
                evaluation.append(num1-num2)
            elif token == "+":
                num2 = evaluation.pop()
                num1 = evaluation.pop()
                evaluation.append(num1+num2)
            elif token == "*":
                num2 = evaluation.pop()
                num1 = evaluation.pop()
                evaluation.append(num1*num2)
            elif token == "/":
                num2 = evaluation.pop()
                num1 = evaluation.pop()
                evaluation.append(int(num1/num2))
        return evaluation[-1]