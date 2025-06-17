def get_welcome_message():
    # Ask for the user's name
    name = input("Please enter your name: ")
    
    # Create and return the personalized welcome message
    welcome_message = f"Welcome, {name}! We're glad to have you here."
    return welcome_message

if __name__ == "__main__":
    # Get and print the welcome message
    message = get_welcome_message()
    print("\n" + message) 