import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import datetime

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

def preprocess_input(user_input):
    tokens = word_tokenize(user_input.lower())
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in tokens if word.isalnum() and word not in stop_words]
    return filtered_words

def restaurant_chatbot():
    print("Welcome to the K's Restaurant!")
    print("You can ask me about the menu, cost, contact details or reservations!")

    while True:
        user_input = input("\nYou: ")
        processed_input = preprocess_input(user_input)

        if any(word in processed_input for word in ["menu", "item", "food"]):
            print("Chatbot: Which type of menu do you need? \n1) Starters \n2) Non Veg \n3) Veg \n4) Dessert \n5) Exit Menu")
            while True:
                try:
                    ch = int(input("Chatbot: Enter your choice: "))
                    if ch == 1:
                        print("Chatbot: Here are the starters available:")
                        print("Salad - 150 rs\nMasala Papad - 70 rs\nPaneer Rolls - 120 rs\nSoup - 160 rs")
                    elif ch == 2:
                        print("Chatbot: Here are the non-veg items available:")
                        print("Chicken 65 - 140 rs\nFried Chicken - 90 rs\nChicken Tandoori - 110 rs\nChicken Biryani - 120 rs")
                    elif ch == 3:
                        print("Chatbot: Here are the veg items available:")
                        print("Paneer Handi - 150 rs\nPulaw - 70 rs\nMix Veg - 120 rs\nRoti - 20 rs")
                    elif ch == 4:
                        print("Chatbot: Here are the dessert items available:")
                        print("Cake - 150 rs\nIce Cream - 70 rs\nCold Coffee - 120 rs\nFaluda - 160 rs")
                    elif ch == 5:
                        print("Hope you found something yummy!")
                        break
                    else:
                        print("Only options 1 to 5 are available.")
                except ValueError:
                    print("Please enter a valid number.")
        
        elif any(word in processed_input for word in ["contact", "phone", "number", "call"]):
            print("Chatbot: You can contact us at +91-1234567890")

        elif any(word in processed_input for word in ["reservation", "book", "reserve", "table"]):
            print("Chatbot: To make a reservation, please call +91-1234567890 or visit https://k-rest.io")

        elif any(word in processed_input for word in ["hours", "time", "open", "closing"]):
            print("Chatbot: We are open from 11 AM to 10 PM, Monday to Sunday.")

        elif any(word in processed_input for word in ["location", "address", "where"]):
            print("Chatbot: Our location is: K's Restaurant, Downtown Street.")

        elif any(word in processed_input for word in ["how", "sup"]):
            print("Chatbot: I'm just a bot, but I'm here to help! How can I assist you today?")

        elif "meow" in processed_input:
            print("Meow meow meow!")

        elif any(word in processed_input for word in ["exit", "quit", "bye"]):
            print("Chatbot: Thank you for chatting with us! Have a great day!")
            break

        else:
            print("Chatbot: I'm sorry, I didn't understand that. Can you ask something else?")

# Run the chatbot
restaurant_chatbot()
