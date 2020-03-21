import random

print("Hi, let's setup a new password!")

while True:
    try:
        total_len = int(input("How many characters would you like your password to be?: "))
        letters = int(input("Out of that, how many characters are letters?: "))
        nums = int(input("And how many would be numbers or symbols?: "))
        
        while type(total_len) != int or type(letters) != int or type(nums) != int or ((letters + nums) != total_len):
            print("Please make sure all three values entered are integers, and the letters and numbers add up to the total.")
            total_len = int(input("How many characters would you like your password to be?: "))
            letters = int(input("Out of that, how many characters are letters?: "))
            nums = int(input("And how many would be numbers or symbols?: "))
        
        password = ""
        letter_temp = ""
        nums_temp = ""
        
        letter_key = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
                      "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        num_key = ["0","1","2","3","4","5","6","7","8","9","!","@","#","$","%","^","&","*"]
        
        for i in range(letters):
            letter_temp += random.choice(letter_key)
        
        for i in range(nums):
            nums_temp += random.choice(num_key)
        
        pw_temp = letter_temp + nums_temp
        pw_temp2 = random.sample(pw_temp, k=len(pw_temp))
        password = ""
        
        for i in pw_temp2:
            password += i
            
        print("Your newly generated password is:", password)

        break
    
    except ValueError:
        print("Please make sure you enter integer values.")
        