def check_brackets(text):
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    stack = []
    
    print("\nПроверяем строку:", text)
    print("-" * 30)
    
    for i in range(len(text)):
        char = text[i]
        
        if char == '(' or char == '[' or char == '{':
            stack.append(char)
            print("Символ:", char, "| Стек:", stack)
            
        elif char == ')' or char == ']' or char == '}':
            if len(stack) > 0 and stack[-1] == pairs[char]:
                stack.pop()
                print("Символ:", char, "| Стек:", stack)
            else:
                stack.append(char)
                print("Символ:", char, "| Стек:", stack)
                return False
                
    print("-" * 30)
    if len(stack) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    user_input = input("Введи строку со скобками: ")
    
    result = check_brackets(user_input)
    
    if result:
        print("Результат: Строка КОРРЕКТНА!")
    else:
        print("Результат: Строка НЕКОРРЕКТНА!")