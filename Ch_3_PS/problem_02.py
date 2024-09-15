Name = input("Enter your name: ")
Date = input("Enter today's date: ")

letter = """Dear <|Name|>,
            You are selected!
            <|Date|>"""
            
print(letter.replace("<|Name|>", Name).replace("<|Date|>", Date))