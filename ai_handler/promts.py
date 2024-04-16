def prompt_test_task(learning_material):
    return (
        f"Прочитай файл {learning_material} і придумай по одному новому завданню з рівнем easy, middle,"
        f"hard, нічого зайвого не писатию. Завдання мають бути унікальними."
        f"Рівень постав у кінці строчки. Написати тільки ці три строчки і все в такому ж форматі. Кожне питання"
        f"з нової строчки. Всього три строчки! Можеш додавати інщі теми але тільки по мові програмування python"
        f"і в такому самому форматі як у файлі. Не використовуй коми"
    )


def prompt_code_task(learning_material):
    return (
        f"Прочитай файл {learning_material} і придумай по одному новому завданню з рівнем easy, middle,"
        f"hard, нічого зайвого не писатию. Завдання мають бути унікальними. Рівень постав у кінці строчки. Написати"
        f"тільки ці три строчки і все в такому ж форматі. Кожне питання з нової строчки. Всього три строчки! Можеш"
        f"додавати інщі теми але тільки по мові програмування python і в такому самому форматі як у файлі. Зверни"
        f"увагу що кожне поле виділено подвійними кавичками"
    )


def prompt_lessons(learning_material):
    return (
        f"Прочитай файл {learning_material}, в ньому знаходиться три приклади уроків, напиши схожий урок"
        f"на тему по програмуванню мови python. Уроки мають бути унікальними. free постав у кінці строчки як в"
        f"прикладах. Написати в такому ж форматі, щоб можна було легко зберегти в csv файл.  Зверни увагу що кожне"
        f"поле виділено подвійними кавичками"
    )


ai_test_tasks_prompt = (
    f"Number,Topic,Question,Var1,Var2,Var3,Right_answer,Level_relation \n"
    f"1, 'Functions', 'What does the print() function do?', 'Returns the number of elements in the"
    f"collection.', 'Outputs a message to the console.', 'Changes the weather to sunny.',"
    f"'Outputs a message to the console.', easy\n"
    f"2,'Functions', 'What is a lambda function in Python?','This is a function that is called"
    f"when an error occurs.','This is a function that is performed automatically when the program"
    f"starts.','This is an anonymous function that can be declared without a name and is used for"
    f"short calculations.','This is an anonymous function that can be declared without a name and"
    f"is used for short calculations.',middle\n"
    f"3,'Rows', 'How can you convert a string to a list in Python?','By applying the split() method"
    f"on a string.','By applying the convert() method on a string.','By applying the to_list()"
    f"method on a string.',hard\n"
)


ai_code_tasks_prompt = (
    f"""Number,Topic,Question,Var1,Var2,Var3,Right_answer,Level_relation \n"""
    f"""1,Looping,"<code># Task: Fill in the blank to iterate through the string and print each
                        character.
                        input_str  =  ""Python""
                        for _____ in input_str:
                            print(_____)</code>","char, input_str","char, char","input_str, char","char, char",easy \n
                        """
    f"""2,Functions,"<code>def count_vowels(input_str):
                            vowels  =  ""aeiouAEIOU""
                            count  =  0
                            for char in input_str:
                                if char in _____:
                                    Count +=  1
                            return count
                        
                        # Test the function with the provided string
                        input_string  =  ""Hello, how are you?""
                        result  =  count_vowels(input_string)
                        print(result) </code> # Output should be 7
                        Fill in the blank with the correct variable to find the number of vowels in the string.",char,
                        input_string,vowels,vowels,middle \n
                        """
    f"""3,Functions,"<code>def count_vowels(input_str):
                            vowels  =  ""aeiouAEIOU""
                            count  =  0
                            for char in input_str:
                                if char in _____:
                                    Count +=  1
                            return count
                        
                        # Test the function with the provided string
                        input_string  =  ""Hello, how are you?""
                        result  =  count_vowels(input_string)
                        print(result) </code> # Output should be 7
                        Fill in the blank with the correct variable to find the number of vowels in the string.",char,
                        input_string,vowels,vowels,middle \n
                        """
)


ai_lesson_tasks_prompt = f"""Number,Topic,Item,Description,text,status \n"
                        1,Strings and lists,Lists and Operations on Them,"In this lesson, we will continue our
                        exploration of lists in Python. We'll learn about various operations that can be performed on
                        lists, such as appending, removing, and sorting elements.","Appending Elements to a List:
                        
                        You can add elements to the end of a list using the append() method.
                        
                        <code>
                        fruits = ['apple', 'banana', 'orange']
                        
                        fruits.append('grape')
                        print(fruits)  # Output: ['apple', 'banana', 'orange', 'grape']
                        </code>
                        
                        Inserting Elements at a Specific Position:
                        
                        You can insert elements at a specific position in the list using the insert() method.
                        
                        <code>
                        fruits = ['apple', 'banana', 'orange']
                        
                        fruits.insert(1, 'grape')
                        print(fruits)  # Output: ['apple', 'grape', 'banana', 'orange']
                        </code>
                        Removing Elements from a List:
                        
                        You can remove elements from a list using various methods like remove() and pop().
                        
                        <code>
                        fruits = ['apple', 'banana', 'orange']
                        
                        fruits.remove('banana')
                        print(fruits)  # Output: ['apple', 'orange']
                        
                        popped_fruit = fruits.pop()
                        print(popped_fruit)  # Output: 'orange'
                        print(fruits)       # Output: ['apple']
                        </code>
                        Checking the Existence of an Element:
                        
                        You can check if an element exists in a list using the in keyword.
                        
                        <code>
                        fruits = ['apple', 'banana', 'orange']
                        
                        print('apple' in fruits)    # Output: True
                        print('grape' in fruits)    # Output: False
                        </code>
                        Sorting a List:
                        
                        You can sort a list using the sort() method, which arranges the elements in ascending order.
                        
                        <code>
                        numbers = [5, 2, 8, 3, 1]
                        
                        numbers.sort()
                        print(numbers)  # Output: [1, 2, 3, 5, 8]
                        </code>
                        To sort in descending order, you can use the reverse parameter.
                        
                        <code>
                        numbers = [5, 2, 8, 3, 1]
                        
                        numbers.sort(reverse=True)
                        print(numbers)  # Output: [8, 5, 3, 2, 1]
                        </code>
                        Copying Lists:
                        
                        Be cautious when copying lists, as using the assignment operator = does not create a new list
                        but rather creates a reference to the original list.
                        
                        <code>
                        fruits = ['apple', 'banana', 'orange']
                        fruits_copy = fruits  # This creates a reference, not a new list
                        
                        fruits_copy.append('grape')
                        print(fruits)       # Output: ['apple', 'banana', 'orange', 'grape']
                        
                        # To create a new independent copy, use the slice operator[:]
                        fruits = ['apple', 'banana', 'orange']
                        fruits_copy = fruits[:]
                        
                        fruits_copy.append('grape')
                        print(fruits)       # Output: ['apple', 'banana', 'orange']
                        </code>
                        Conclusion:
                        
                        In this lesson, we continued our exploration of lists in Python. We learned how to perform
                        various operations on lists, such as appending, inserting, removing, checking the existence
                        of elements, sorting, and copying. Lists are versatile data structures that allow us to store
                        and manipulate collections of items. In the next lesson, we will explore list slices and list
                        comparison operators, enabling us to work with specific subsets of lists and make comparisons
                        between lists.",free11,Strings and lists,Lists and Operations on Them,"In this lesson, we will
                        continue our exploration of lists in Python. We'll learn about various operations that can be
                        performed on lists, such as appending, removing, and sorting elements.","Appending Elements to
                        a List:
                        
                        You can add elements to the end of a list using the append() method.
                        
                        <code>
                        fruits = ['apple', 'banana', 'orange']
                        
                        fruits.append('grape')
                        print(fruits)  # Output: ['apple', 'banana', 'orange', 'grape']
                        </code>
                        
                        Inserting Elements at a Specific Position:
                        
                        You can insert elements at a specific position in the list using the insert() method.
                        
                        <code>
                        fruits = ['apple', 'banana', 'orange']
                        
                        fruits.insert(1, 'grape')
                        print(fruits)  # Output: ['apple', 'grape', 'banana', 'orange']
                        </code>
                        Removing Elements from a List:
                        
                        You can remove elements from a list using various methods like remove() and pop().
                        
                        <code>
                        fruits = ['apple', 'banana', 'orange']
                        
                        fruits.remove('banana')
                        print(fruits)  # Output: ['apple', 'orange']
                        
                        popped_fruit = fruits.pop()
                        print(popped_fruit)  # Output: 'orange'
                        print(fruits)       # Output: ['apple']
                        </code>
                        Checking the Existence of an Element:
                        
                        You can check if an element exists in a list using the in keyword.
                        
                        <code>
                        fruits = ['apple', 'banana', 'orange']
                        
                        print('apple' in fruits)    # Output: True
                        print('grape' in fruits)    # Output: False
                        </code>
                        Sorting a List:
                        
                        You can sort a list using the sort() method, which arranges the elements in ascending order.
                        
                        <code>
                        numbers = [5, 2, 8, 3, 1]
                        
                        numbers.sort()
                        print(numbers)  # Output: [1, 2, 3, 5, 8]
                        </code>
                        To sort in descending order, you can use the reverse parameter.
                        
                        <code>
                        numbers = [5, 2, 8, 3, 1]
                        
                        numbers.sort(reverse=True)
                        print(numbers)  # Output: [8, 5, 3, 2, 1]
                        </code>
                        Copying Lists:
                        
                        Be cautious when copying lists, as using the assignment operator = does not create a new list
                        but rather creates a reference to the original list.
                        
                        <code>
                        fruits = ['apple', 'banana', 'orange']
                        fruits_copy = fruits  # This creates a reference, not a new list
                        
                        fruits_copy.append('grape')
                        print(fruits)       # Output: ['apple', 'banana', 'orange', 'grape']
                        
                        # To create a new independent copy, use the slice operator[:]
                        fruits = ['apple', 'banana', 'orange']
                        fruits_copy = fruits[:]
                        
                        fruits_copy.append('grape')
                        print(fruits)       # Output: ['apple', 'banana', 'orange']
                        </code>
                        Conclusion:
                        
                        In this lesson, we continued our exploration of lists in Python. We learned how to perform
                        various operations on lists, such as appending, inserting, removing, checking the existence of
                        elements, sorting, and copying. Lists are versatile data structures that allow us to store and
                        manipulate collections of items. In the next lesson, we will explore list slices and list
                        comparison operators, enabling us to work with specific subsets of lists and make comparisons
                        between lists.",free \n"""


#
# import subprocess
# import time
#
# from ai_handler import *
# from file_utils import *
# from promts import *
#
# subprocess.run(["pip", "install", "--upgrade", "g4f"], check=True)
# from time import sleep
# from random import randint
# import g4f
#
#
# '''
# This module generates educational content for the bot using chat gpt with the g4f library. It saves information in
# csv files.
# '''
#
# '''
# This module generates educational content for the bot using chat gpt with the g4f library. It saves information in
# csv files.
# '''
#
# # Global variable for storing a list of available models
# available_models = []
#
#
# # Function to get available models
# def get_available_models():
#     global available_models
#     try:
#         # Getting all attributes of the 'g4f.models' module
#         available_models = dir(g4f.models)
#         # print("+"*30, available_models)
#     except Exception as e:
#         print(f"Помилка при отриманні списку доступних моделей: {e}")
#         available_models = []
#
#
# # Function for selecting and using the model
# def ask_gpt(prompt: str) -> str:
#     global available_models
#     # Check the availability of available models
#     if not available_models:
#         # If the list of available models is empty, return None
#         print("Список доступних моделей порожній.")
#         return None
#
#     # Iterate over available models
#     for model_name in available_models:
#         try:
#             # Get the model by its name
#             model = getattr(g4f.models, model_name)
#             # Generate a response using the current model
#             response = g4f.ChatCompletion.create(
#                 model=model,
#                 messages=[{"role": "user", "content": prompt}]
#             )
#             print(f"Модель {model} працює.")
#             # Return the generated response
#             print("+"*20, response)
#             return response
#         except Exception as e:
#             # If an error occurs, go to the next model
#             print(f"Помилка при використанні моделі {model_name}: {e}")
#             time.sleep(2)  # Add a delay of 1 second between attempts
#             continue
#
#     # If none of the models works
#     print("Не вдалося використати жодну з доступних моделей.")
#     return None
#
#
# ## Check if the script is being run directly
# if __name__ == '__main__':
#     # getting a list of available models
#     get_available_models()
#
#     '''
#     Create test tasks
#     '''
#     # uncomment to create test tasks in ai_test_tasks_csv
#
#     ai_test_tasks_file_path = "ai_test_tasks.csv"
#
#     # Open the 'ai_test_tasks.csv' file in read mode and read its contents as lines if csv file exists
#     try:
#         test_tasks = read_file_splitlines(ai_test_tasks_file_path)
#         # with open(ai_test_tasks_file_path, "r") as test_task_file:
#         #     test_tasks = test_task_file.read().splitlines()
#     except FileNotFoundError:
#         # If the file doesn't exist, create it
#         response_file = write_to_file(ai_test_tasks_file_path)
#         test_tasks = []
#         # with open(ai_test_tasks_file_path, "w") as response_file:
#         #     response_file.write(ai_test_tasks_prompt)
#             # test_tasks = []
#
#     # Open the 'ai_test_tasks.csv' file in read mode and count the number of records (lines)
#     try:
#         response_file = read_file(ai_test_tasks_file_path)
#         record_count = sum(1 for _ in response_file)
#     except Exception as e:
#         print("responce file is None")
#         record_count = 0
#     # response_file = read_file(ai_test_tasks_file_path)
#     # # with open(ai_test_tasks_file_path, "r") as response_file:
#     # record_count = sum(1 for _ in response_file)
#
#     # Define the prompt for generating responses
#     prompt_test_tasks = prompt_test_task(test_tasks)
#
#     # Continue generating responses until the record count reaches 300
#     while record_count < 1000:
#         # Generate responses using the ask_gpt function with a specific prompt
#         responses = ask_gpt(prompt_test_tasks)
#
#         if responses is None:
#             # If the response is empty, print a message indicating that an empty response was received from the model
#             print("Отримано порожню відповідь від моделі.")
#             # Continue to the next iteration of the loop
#             continue
#         else:
#             # Split the response into individual lines
#             response_lines = responses.split("\n")
#
#             # Create a set to store existing lines in the CSV file
#             existing_lines = set()
#             # Open the 'ai_test_tasks.csv' file in read mode and populate the set with its existing lines
#             response_file = read_file(ai_test_tasks_file_path)
#             if response_file:
#                 for existing_line in response_file:
#                     existing_lines.add(existing_line.strip())
#
#             # with open(ai_test_tasks_file_path, "r") as response_file:
#             #     for existing_line in response_file:
#             #         existing_lines.add(existing_line.strip())
#
#             # Open the 'ai_test_tasks.csv' file in append mode to add new responses
#             # with open(ai_test_tasks_file_path, "a") as response_file:
#                 response_file = append_to_file(ai_test_tasks_file_path)
#                 # Iterate over each line in the response
#                 for line in response_lines:
#                     # Split the line into fields using comma as delimiter
#                     field = line.split(",")
#                     # Check if the last field (level) is in the list of valid levels
#                     if field[-1] not in ["easy", "middle", "hard"]:
#                         # If not, skip this line
#                         continue
#                     # Check if the length of the first field (question) is greater than 3 characters
#                     if len(field[0]) > 3:
#                         # If it is, break the loop (assuming the task is invalid)
#                         break
#                     # Check if the line is already present in the existing lines
#                     if line.strip() in existing_lines:
#                         # If it is, skip this line
#                         continue
#
#                     print(responses)
#                     # Write the line to the CSV file
#                     response_file.write(line + "\n")
#                     # Flush the file buffer to ensure that data is written to disk before the delay
#                     response_file.flush()
#                     # Delay for a random number of seconds from 30 to 80
#                     random_delay = randint(30, 80)
#                     print(f"Затримка на {random_delay} секунд")
#                     sleep(random_delay)
#
#         # Open the 'ai_code_tasks.csv' file in read mode and count the number of records (lines)
#         try:
#             response_file = read_file(ai_test_tasks_file_path)
#             record_count = sum(1 for _ in response_file)
#         except Exception as e:
#             print("responce file is None")
#             record_count = 0
#         # response_file = read_file(ai_test_tasks_file_path)
#         # # with open(ai_test_tasks_file_path, "r") as response_file:
#         # record_count = sum(1 for _ in response_file)
#
#     # Print a message indicating that enough records have been obtained and the program is ending
#     print("Достатньо записів. Завершення програми.")

# '''
# Create code tasks
# '''
#
# # uncomment to create code tasks in ai_code_tasks_csv
#
# ai_code_tasks_file_path = "ai_code_tasks.csv"
#
# # # Open the 'code_tasks_file.csv' file in read mode and read its contents as lines
# # code_tasks_file = read_file_splitlines(ai_code_tasks_file_path)
# # with open(ai_code_tasks_file_path, "r") as code_tasks_file:
# #     code_tasks = code_tasks_file.read().splitlines()
# #
# # Open the 'ai_test_tasks.csv' file in read mode and read its contents as lines if csv file exists
# try:
#     code_tasks = read_file_splitlines(ai_code_tasks_file_path)
# except FileNotFoundError:
#     write_to_file(ai_code_tasks_file_path, ai_code_tasks_prompt)
#     code_tasks = []
# # try:
# #     with open(ai_code_tasks_file_path, "r") as code_tasks_file:
# #         code_tasks = code_tasks_file.read().splitlines()
# # except FileNotFoundError:
# #     # If the file doesn't exist, create it
# #     with open(ai_code_tasks_file_path, "w") as response_file:
# #         response_file.write(ai_code_tasks_prompt)
# #
# #         code_tasks = []
#
# # Open the 'ai_code_tasks.csv' file in read mode and count the number of records (lines)
# # with open(ai_code_tasks_file_path, "r") as response_file:
# try:
#     response_file = read_file(ai_code_tasks_file_path)
#     record_count = sum(1 for _ in response_file)
# except Exception as e:
#     print("responce file is None")
#     record_count = 0
#
#
# # Define the prompt for generating responses
# prompt_code_tasks = prompt_code_task(code_tasks)
#
# # Continue generating responses until the record count reaches 300
# while record_count <= 89:
#     # Generate responses using the ask_gpt function with a specific prompt
#     responses = ask_gpt(prompt_code_tasks)
#
#     if responses is None:
#         # If the response is empty, print a message indicating that an empty response was received from the model
#         print("Отримано порожню відповідь від моделі.")
#         # Continue to the next iteration of the loop
#         continue
#     else:
#         # Split the response into individual lines
#         response_lines = responses.split("\n")
#
#         # Create a set to store existing lines in the CSV file
#         existing_lines = set()
#         # Open the 'ai_code_tasks.csv' file in read mode and populate the set with its existing lines
#         # with open(ai_code_tasks_file_path, "r") as response_file:
#         response_file = read_file(ai_code_tasks_file_path)
#         if response_file:
#         # with open(ai_code_tasks_file_path, "r") as response_file:
#             for existing_line in response_file:
#                 existing_lines.add(existing_line.strip())
#
#             # Open the 'ai_code_tasks.csv' file in append mode to add new responses
#             response_file = append_to_file(ai_code_tasks_file_path, responses)
#             # with open(ai_code_tasks_file_path, "a") as response_file:
#             #     if not existing_lines:
#             #         # Add the first line if the file is empty
#             #         response_file.write("Number,Topic,Question,Var1,Var2,Var3,Right_answer,Level_relation\n")
#                 # Iterate over each line in the response
#             for line in response_lines:
#                 # # Split the line into fields using comma as delimiter
#                 field = line.split(",")
#                 # # Check if the last field (level) is in the list of valid levels
#                 # if field[-1] not in ["easy", "middle", "hard"]:
#                 #     # If not, skip this line
#                 #     continue
#                 if not any(line.endswith(level) for level in ["easy", "middle", "hard"]):
#                     # If none of the valid levels is found at the end of the line, skip this line
#                     continue
#                 # Check if the length of the first field (question) is greater than 3 characters
#                 if len(field[0]) > 3:
#                     # If it is, break the loop (assuming the task is invalid)
#                     break
#                 # Check if the line is already present in the existing lines
#                 if line.strip() in existing_lines:
#                     # If it is, skip this line
#                     continue
#
#                 # Write the line to the CSV file
#                 response_file.write(line + "\n")
#                 # Flush the file buffer to ensure that data is written to disk before the delay
#                 response_file.flush()
#                 # Delay for a random number of seconds from 30 to 80
#                 random_delay = randint(30, 80)
#                 print(responses)
#                 print(f"Затримка на {random_delay} секунд")
#                 sleep(random_delay)
#
#     # Open the 'ai_code_tasks.csv' file in read mode and count the number of records (lines)
#     # with open(ai_code_tasks_file_path, "r") as response_file:
#     try:
#         response_file = read_file(ai_code_tasks_file_path)
#         record_count = sum(1 for _ in response_file)
#     except Exception as e:
#         print("responce file is None")
#         record_count = 0
# # Print a message indicating that enough records have been obtained and the program is ending
# print("Достатньо записів. Завершення програми.")


#
# '''
# Create lessons
# '''
# # uncomment to create lessons in ai_lesson_tasks_csv
#
# ai_lessons_tasks_file_path = "ai_lessons.csv"
#
# # # Open the 'lesson_tasks_file.csv' file in read mode and read its contents as lines
# # try:
# #     with open(ai_lessons_tasks_file_path, "r") as lesson_tasks_file:
# #         lesson_tasks = lesson_tasks_file.read().splitlines()
# # except FileNotFoundError:
# #     # If the file doesn't exist, create it
# #     with open(ai_lessons_tasks_file_path, "w") as response_file:
# #         response_file.write(ai_lesson_tasks_prompt)
# #
# #         lesson_tasks = []
# # # Check if 'ai_lesson_tasks.csv' exists
# # try:
# #     # Open the 'ai_lesson_tasks.csv' file in read mode and count the number of records (lines)
# #     with open(ai_lessons_tasks_file_path, "r") as response_file:
# #         record_count = sum(1 for _ in response_file)
# # except FileNotFoundError:
# #     # If the file doesn't exist, create it
# #     with open(ai_lessons_tasks_file_path, "w") as response_file:
# #         response_file.write(ai_lesson_tasks_prompt)
# #     record_count = 0  # Initialize record count
#
# # Open the 'ai_lesson_tasks.csv' file in read mode and read its contents as lines if csv file exists
# try:
#     lesson_tasks = read_file_splitlines(ai_lessons_tasks_file_path)
# except FileNotFoundError:
#     response_file = write_to_file(ai_lessons_tasks_file_path)
#     lesson_tasks = []
# # try:
# #     with open(ai_lessons_tasks_file_path, "r") as lesson_tasks_file:
# #         lesson_tasks = lesson_tasks_file.read().splitlines()
# #     # Open the 'ai_lesson_tasks.csv' file in read mode and count the number of records (lines)
# #     with open(ai_lessons_tasks_file_path, "r") as response_file:
# #         record_count = sum(1 for _ in response_file)
# # except FileNotFoundError:
# #     # If the file doesn't exist, create it
# #     with open(ai_lessons_tasks_file_path, "w") as response_file:
# #         response_file.write(ai_lesson_tasks_prompt)
# #     lesson_tasks = []
# #     record_count = 0  # counter initialization
#
# # Define the prompt for generating responses
# prompt_lesson_tasks = prompt_lessons(lesson_tasks)
#
# # Continue generating responses until the record count reaches 2000
# while record_count <= 2000:
#     # Generate responses using the ask_gpt function with a specific prompt
#     responses = ask_gpt(prompt_lesson_tasks)
#
#     if responses is None:
#         # If the response is empty, print a message indicating that an empty response was received from the model
#         print("Отримано порожню відповідь від моделі.")
#         # Continue to the next iteration of the loop
#         continue
#     else:
#         # Split the response into individual lessons based on the format provided
#         lessons = responses.strip().split("\n\n")
#
#         # Open the 'ai_lessons_tasks.csv' file in append mode to add new responses
#         response_file = append_to_file(ai_lessons_tasks_file_path)
#         # with open(ai_lessons_tasks_file_path, "a") as response_file:
#             for lesson in lessons:
#                 # Check if the lesson already exists in the file
#                 if lesson.strip() in open(ai_lessons_tasks_file_path, "r").read():
#                     continue  # Skip if the lesson already exists
#
#                 # Split the lesson into fields using comma as delimiter
#                 fields = lesson.strip().split(",")
#
#                 # Check if the last field (status) is 'free'
#                 if fields[-1].strip() != "free":
#                     continue  # Skip if the last field is not 'free'
#
#                 # Check if the length of the first field (number) is greater than 3 characters
#                 if len(fields[0]) > 3:
#                     continue  # Skip if the number exceeds 3 characters
#
#                 # Write the lesson to the CSV file
#                 response_file.write(lesson.strip() + "\n")  # Write the lesson
#                 response_file.flush()  # Flush the buffer
#
#                 # Delay for a random number of seconds from 30 to 80
#                 random_delay = randint(30, 80)
#                 print(lesson)
#                 print(f"Затримка на {random_delay} секунд")
#                 sleep(random_delay)
#
#                 # Increment the record count
#                 record_count += 1
#
#     # Open the 'ai_code_tasks.csv' file in read mode and count the number of records (lines)
#     # with open(ai_lessons_tasks_file_path, "r") as response_file:
#     response_file = read_file(ai_lessons_tasks_file_path)
#     record_count = sum(1 for _ in response_file)
#
# # Print a message indicating that enough records have been obtained and the program is ending
# print("Достатньо записів. Завершення програми.")
