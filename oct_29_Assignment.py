#   1."WORD COUNT" Problem 
# that return the top N frequet words

def word_count(sen,N):
    sen=sen.lower() #first convert the string to lowercase (bcz python is case-sensitive)
    final_sen=""
    for i  in range(len(sen)):
        if(sen[i]>='a' and sen[i]<='z'):
            final_sen+=sen[i]  #it add only a-z 
        else:
            final_sen+=" "    #it only stores a-z

            """
            If input = "Hello, world! hello"
            Then final_sen = "hello world hello"
            """

    sen_list=final_sen.split()  #it splits into list of words ["hello", "world", "hello"]
    dict_sen={}
    output={}
    for i in sen_list:
        if dict_sen.get(i) != None:
            dict_sen[i]+=1      #here word count happens
        else:
            dict_sen[i]=1 
    for i in dict_sen:
        if dict_sen[i]==N:
            output[i]=N
    return output        

sen=input("enter a sentence :")  #  hello world,hello [hello:2,world:1]
N=int(input("enter the count :")) #I enter count as 2
print("output: ")   #{'hello': 2}
print(word_count(sen,N))

#2.Mini interpreter that reads a string like "5+2*(3-1)" and evaluates it using loops,if-else,and functions


def evaluates(s):
    def precedence(op):
        if op in ('+', '-'):
            return 1
        elif op in ('*', '/'):
            return 2
        return 0

    def operation(a, b, op):
        if op == '+': return a + b
        elif op == '-': return a - b
        elif op == '*': return a * b
        elif op == '/': return a / b

    stack_num = []  # Stack for numbers
    stack_op = []   # Stack for operators
    idx = 0

    while idx < len(s):
        # Case 1: If it's a space, skip it
        if s[idx] == ' ':
            idx += 1
            continue

        # Case 2: If it's a number (handles multi-digit)
        if s[idx].isdigit():
            num = ""
            while idx < len(s) and s[idx].isdigit():
                num += s[idx]
                idx += 1
            stack_num.append(int(num))
            continue

        # Case 3: If it's '('
        elif s[idx] == '(':
            stack_op.append(s[idx])

        # Case 4: If it's ')'
        elif s[idx] == ')':
            while stack_op and stack_op[-1] != '(':
                op = stack_op.pop()
                val2 = stack_num.pop()
                val1 = stack_num.pop()
                stack_num.append(operation(val1, val2, op))
            stack_op.pop()  # remove '('

        # Case 5: If it's an operator
        else:
            while (stack_op and precedence(stack_op[-1]) >= precedence(s[idx])):
                op = stack_op.pop()
                val2 = stack_num.pop()
                val1 = stack_num.pop()
                stack_num.append(operation(val1, val2, op))
            stack_op.append(s[idx])

        idx += 1

    # Apply remaining operators
    while stack_op:
        op = stack_op.pop()
        val2 = stack_num.pop()
        val1 = stack_num.pop()
        stack_num.append(operation(val1, val2, op))

    return stack_num[-1]


# ---- Main code ----
s = input("Enter the expression: ")
result = evaluates(s.replace(" ", ""))
print("Result:", result)
