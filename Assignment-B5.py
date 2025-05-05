# Assignment-B5 (Chatbot)
import datetime

def restaurant_chatbot():
    print("Welcome to the K's Restaurant!")
    print("You can ask me about the menu, cost, contact details or reservations!")
    
    while True:
        user_input = input("\nYou: ").lower()
        
         
        if "menu" in user_input or "item" in user_input:
            print("Chatbot: Which type of of menu you need \n1)Starters \n2)Non Veg \n3)Veg \n4)Dessert")
            while True:
                ch=int(input("Chatbot: Enter your choice : "))
                if ch==1:
                    print("Chatbot: Here are the starters available:")
                    print("Starters------------------------------")
                    print("Salad------------------------------150 rs")
                    print("Masala Papad------------------------70 rs")
                    print("Panner Rolls-----------------------120 rs")
                    print("Soup-------------------------------160 rs")
                   
                elif ch == 2:
                    print("Chatbot: Here are the non-veg items available:")
                    print("Non Veg------------------------------")
                    print("Chicken 65-----------------------------140 rs")
                    print("Fried Chiken----------------------------90 rs")
                    print("Chicken Tandoori-----------------------110 rs")
                    print("Chicken biryani------------------------120 rs")
                    
                elif ch == 3:
                    print("Chatbot: Here are the veg items available:")
                    print("Veg-----------------------------------")
                    print("Panner handi--------------------------150 rs")
                    print("Pulaw----------------------------------70 rs")
                    print("Mix veg-------------------------------120 rs")
                    print("Roti-----------------------------------20 rs")
                    
                elif ch == 4:
                    print("Chatbot: Here are the dessert items available:")
                    print("Dessert------------------------------")
                    print("Cake-----------------------------150 rs")
                    print("Iceceam------------------------70 rs")
                    print("Cold coffee-----------------------120 rs")
                    print("Faluda-------------------------------160 rs")
                    
                elif ch == 5:

                    print("Hope you finds something yummy !!!")
                    break
                else:
                    print("Only above item are available")
       
        
        elif "contact" in user_input or "phone" in user_input:
            print("Chatbot: You can contact us at +91-1234567890")
        
        elif "reservation" in user_input or "book" in user_input:
            print("Chatbot: To make a reservation, please call us at +91-1234567890 or visit our website at https://k-rest.io")
        
        elif "hours" in user_input:
            print("Chatbot: We are open from 11 AM to 10 PM, Monday to Sunday.")
        
        elif "location" in user_input or "address" in user_input:
            print("Chatbot: Our location is: K'Resturant.")
        
        elif "how are you" in user_input or "how's it going" in user_input or "sup" in user_input:
            print("Chatbot: I'm just a bot, but I'm here to help you! How can I assist you today?")
        
        elif "meow" in user_input:
            print("Meow meow meow!")

        elif "exit" in user_input or "quit" in user_input:
            print("Chatbot: Thank you for chatting with us! Have a great day!")
            break
        
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Can you ask something else?")

restaurant_chatbot()

