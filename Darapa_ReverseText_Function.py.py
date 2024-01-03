def reverse_text():
    while True:
        user_input = input("Enter a string: ")
        
        if user_input.isalpha():
            print("Output:", user_input[::-1])
            break
        else:
            print("Error Reported! Enter text only.")

reverse_text()
