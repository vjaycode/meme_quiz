import random  # Import random for displaying random questions every time
import pygame  # Import pygame for handling music files
import os  # Import os for clearing the console

# Initialize Pygame and the mixer
pygame.init()
pygame.mixer.init()

# Load sound files
start = pygame.mixer.Sound('start.mp3')
q_sound = pygame.mixer.Sound('question.mp3')
win = pygame.mixer.Sound('win.mp3')

# Quiz data with more questions and updated prize money
quiz = {
    1: {
        'question': 'Who is known as the “Iron Man” of India?',
        'options': {
            '1': "Tony Stark",
            '2': "Sardar Vallabhbhai Patel",
            '3': 'Gandhi',
            '4': 'Narendra Modi',
        },
        'answer': '2'  
    },
    2: {
        'question': 'What is the national heritage animal of India?',
        'options': {
            '1': "Lion",
            '2': "Cheetah",
            '3': 'Panther',
            '4': 'Elephant',
        },
        'answer': '4'  
    },
    3: {
        'question': 'Which city is called the Pink City in India?',
        'options': {
            '1': "Jaipur",
            '2': "Jodhpur",
            '3': 'Jalandhar',
            '4': 'Kota',
        },
        'answer': '1'  
    },
    4: {
        'question': 'Who was the author of Ramayana?',
        'options': {
            '1': "Hanuman",
            '2': "Kalidas",
            '3': 'Valmiki',
            '4': 'Ved Vyas',
        },
        'answer': '3'  
    },
    5: {
        'question': 'Who was famously called the Flying Sikh of India?',
        'options': {
            '1': "Mika Singh",
            '2': "Diljit Dosanjh",
            '3': 'Milkha Singh',
            '4': 'Sandeep Singh',
        },
        'answer': '3'  
    },
    6: {
        'question': 'What is the capital of India?',
        'options': {
            '1': "Mumbai",
            '2': "Delhi",
            '3': 'Bangalore',
            '4': 'Kolkata',
        },
        'answer': '2'  
    },
    7: {
        'question': 'Which Indian state is known as the Land of Five Rivers?',
        'options': {
            '1': "Punjab",
            '2': "Haryana",
            '3': 'Uttar Pradesh',
            '4': 'Bihar',
        },
        'answer': '1'  
    },
    8: {
        'question': 'Which festival is known as the Festival of Lights?',
        'options': {
            '1': "Holi",
            '2': "Diwali",
            '3': 'Eid',
            '4': 'Christmas',
        },
        'answer': '2'  
    },
    9: {
        'question': 'Who was the first President of India?',
        'options': {
            '1': "Dr. Rajendra Prasad",
            '2': "Dr. S. Radhakrishnan",
            '3': 'Zakir Husain',
            '4': 'V.V. Giri',
        },
        'answer': '1'  
    },
    10: {
        'question': 'Which is the smallest state in India by area?',
        'options': {
            '1': "Goa",
            '2': "Sikkim",
            '3': 'Delhi',
            '4': 'Tripura',
        },
        'answer': '1'  
    },
    11: {
        'question': 'What is the national flower of India?',
        'options': {
            '1': "Rose",
            '2': "Lotus",
            '3': 'Sunflower',
            '4': 'Jasmine',
        },
        'answer': '2'  
    },
    12: {
        'question': 'Which is the longest river in India?',
        'options': {
            '1': "Ganga",
            '2': "Yamuna",
            '3': 'Brahmaputra',
            '4': 'Godavari',
        },
        'answer': '1'  
    },
    13: {
        'question': 'Which planet is known as the Red Planet?',
        'options': {
            '1': "Earth",
            '2': "Venus",
            '3': 'Mars',
            '4': 'Jupiter',
        },
        'answer': '3'  
    },
    14: {
        'question': 'What is the capital of France?',
        'options': {
            '1': "Berlin",
            '2': "Madrid",
            '3': 'Paris',
            '4': 'Rome',
        },
        'answer': '3'  
    },
    15: {
        'question': 'Which is the tallest mountain in the world?',
        'options': {
            '1': "K2",
            '2': "Kangchenjunga",
            '3': 'Mount Everest',
            '4': 'Lhotse',
        },
        'answer': '3'  
    }
}

def clear_console():
    """Clear the console for better readability."""
    os.system('cls' if os.name == 'nt' else 'clear')

def play(quiz_data):
    start.play()  # Play the starting sound
    pygame.time.wait(int(start.get_length() * 1000))  # Wait for start sound to finish
    questions = list(quiz_data.keys())
    random.shuffle(questions)  # Shuffle questions for randomness

    prize = 0
    prize_money = [
        1000,         # 1st question
        2000,         # 2nd question
        5000,         # 3rd question
        10000,        # 4th question
        20000,        # 5th question
        40000,        # 6th question
        80000,        # 7th question
        160000,       # 8th question
        320000,       # 9th question
        640000,       # 10th question
        1250000,      # 11th question
        2500000,      # 12th question
        5000000,      # 13th question
        10000000,     # 14th question
        20000000,     # 15th question
        40000000,     # 16th question
        70000000      # 17th question (final question for 7 crores)
    ]

    all_correct = True  # Flag to track if all answers are correct

    for i, q in enumerate(questions):
        clear_console()  # Clear console before each question
        question = quiz_data[q]
        
        print(f"\nQuestion {i + 1}: {question['question']}")
        q_sound.play()  # Play question sound

        # Display options
        for o, option in question['options'].items():
            print(f"{o}. {option}")

        pygame.time.wait(4000)  # Wait for 2 seconds after displaying the question and options
        q_sound.stop()  # Stop the question sound after 2 seconds

        user = input("Enter your option (1-4): ").strip()  # Get user input

        # Input validation
        if user not in question['options']:
            print("Invalid option! Please enter a valid option (1-4).")
            all_correct = False
            break

        if user == question['answer']:
            print("Correct!")
            prize += prize_money[i]
            print(f"You won Rs.{prize} so far")
        else:
            print("Incorrect answer")
            all_correct = False  # Set flag to False if answer is incorrect
            break  # Exit loop on incorrect answer

    print(f'\nYour final prize is Rs.{prize}')

    if all_correct:  # Check if all answers were correct
        win.play()  # Play winning sound
        pygame.time.wait(int(win.get_length() * 1000))  # Wait to allow the sound to finish

    pygame.mixer.music.stop()  # Stop any music playing

def main():
    while True:
        play(quiz)  # Start the quiz
        replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if replay != 'yes':
            break  # Exit the loop if user does not want to play again

    pygame.quit()  # Quit Pygame

# Start the program
main()
