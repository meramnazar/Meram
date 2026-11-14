print("Assalam o Alaikum Boss, Me Jarvis Hoon!")

while True:
    hukam = input("Boss, bolo kya karoon? : ")
    
    if "naam" in hukam:
        print("Jarvis: Mera naam Jarvis ha Boss!")
    elif "mausam" in hukam:
        print("Jarvis: Haveli Lakha me aaj mausam acha ha Boss!")
    elif "bye" in hukam:
        print("Jarvis: Allah Hafiz Boss!")
        break
    else:
        print("Jarvis: Samajh gaya Boss, ye kaam kar doon ga!")
