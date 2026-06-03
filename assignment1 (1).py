## Question 1 explain the difference between the following data types with examples:
## 1. integer(int) = An integer is a numeric data type which stores whole number that can be positive ,negative or zero.
# example :
a=10
b=-20
print(a)
print(type(a))
print(b)
print(type(b))
 
## 2. Float(float) = A float is a numeris data type used to store numbers which have decimal point or is in exponential form.

# example:
d = 12.324
print(d)
print(type(d))

## 3. String(str) = A string is a sequence which is enclosed in the quotes{ single,duoble,triple}.
c = 'hello'
print(c)
print(type(c))
 
e =" Hello python"
print(e)
print(type(e))

f =""" Multiples qoutation string"""
print(f)
print(type(f))
 
## 4. Boolean(bool) = A boolean data type represent one of two values : True or False.
#example
a=True
print(a)
print(type(a))
b = False
print(b)
print(type(b))

##Question 2 Write a python program to create 3 variables: name,age,city
name = "Priya"
age =19
city ="Pilani"
print(" my name is:" ,name)
print(" my age is:" ,age)
print(" I lives in :" ,city)


## Question 3 Write a python program that: Takes a user name as input.
# Print the name into upper case.
# print the total number of characters in the name.
Name =input("enter your name:")
print(Name.upper())
print(len(Name))


### Question 4 Explain any 5 commonly used string methods in the python with example.

## 1.upper() : This method is used to Converts all characters in a string to uppercase.
#Example: 
text = "hello"
print(text.upper()) 

## 2. lower(): This method is used to Converts all characters in a string to lowercase.

# Example:
text = "HELLO"
print(text.lower())


### 3.swapcase() :This method is used to converts all lowercasse into uppercase and the uppercase into the lowercase.
# Example:
text ="India Is A Country"
print(text.swapcase())


## 4. replace() : This method is used to Replaces one part of a string with another.
# Example: 
text = "I like tea"
print(text.replace("tea", "coffee"))

## 5. strip(): This method is used to removes spaces from the beginning and end of a string. It does not remove spaces from the middle.
#Example:
subject="     Python    "
print(subject.strip())


###Question 5 Create a list containing the names of 5 fruits.
# print the complete list.
# print the first and lst element.
# print the total number of items in the list. 

F=["apple","mango","banana","orange","date"]
print(F)   # for complete list
print(F[0])     # for 1st element 
print(F[-1])      # for last element 
print(len(F))    # for length of list    


###Question 6 Write a puthon program to:
# create a list of numbers[10,20,30,40,50]
# add 60 to list
# remove 20 from list
# print the updated list

num=[10,20,30,40,50]
print(num)
num.append(60)   # to add 60
num.remove(20)     # to remove 20
print(num)

### Question 7 what is Artifical Intelligence(AI)? Expalin its importance and mention any 4 real life application of AI.

# Artifical Intelligence(AI) is an ability of the machines to simulates human like thinking such as learning ,reasoning ,problem solving ,and decision making etc.

# In the common terms : AI makes machine "smart "enoughnto perform tasks tha normally requires the human brain.
 
 ###👉👉 key technology that power AI :
 #1. Machine Learning (ML): This is the base of AI. It allows computers to learn from data and improve over time without being directly programmed for every task.
 
# 2. Deep Learning: A more advanced form of machine learning that uses multiple layers of models to handle complex tasks like image and speech recognition.

# 3. Neural Networks:These are mathematical models designed to mimic how the human brain processes information.

# 4. Natural Language Processing (NLP): Helps AI understand, interpret, and generate human language.

# 5. Computer Vision:Used in facial recognition, self-driving cars, and medical imaging.

### 👉👉 importance of AI: 

#  1. Strengthens safety and security: AI is widely used in fraud detection, cybersecurity, surveillance systems, and identity verification to improve safety in digital and physical spaces.
 
 # 2. Saves time and increases efficiency: AI can do repetitive and time-consuming tasks much faster than humans. This helps in offices, industries, and even daily life apps.

 # 3. Makes work faster and smarter: AI can handle repetitive and time-consuming tasks quickly and accurately, which increases productivity and reduces human effort.

# 4. Helps in better decision-making: By analyzing large amounts of data, AI finds patterns and insights that help businesses, governments, and organizations make more accurate and informed decisions.

# 5. Drives business and economy: Businesses use AI to understand customer needs, improve services, automate operations, and increase profits, which supports overall economic growth.

###👉👉four real time application of AI:

# 1. Healthcare: AI helps doctors detect diseases early by analyzing medical scans like X-rays and MRI, and supports faster, more accurate treatment decisions.

# 2. Navigation & Transport:AI is used in apps like Google Maps to track live traffic, suggest the fastest routes, and reduce travel time in real time.

# 3. Social Media & Entertainment : AI studies user behavior and recommends personalized videos, posts, and movies on platforms like YouTube, Instagram, and Netflix.

# 4.  Banking & Finance : AI detects fraud in transactions, monitors unusual activity, and improves security and customer service in online banking systems.


###Question 8 Identify whether the folloeing are ex of AI and expalin why:
  # 1️⃣. chatgpt :Yes ChatGPT is an example of Artificial Intelligence (AI).

# It is a type of AI called a large language model (LLM) developed to understand and generate human-like text.  
# ## Why it is AI: ChatGPT uses machine learning and natural language processing to:

#understand questions typed by users
# generate meaningful and relevant responses
# learn patterns from large amounts of text data (during training)


#2️⃣ Google Maps Route Prediction :Yes, Google Maps Route Prediction is an example of Artificial Intelligence (AI)


### Why it is considered AI : It uses AI techniques such as machine learning and data analysis to:

# Analyze traffic conditions in real time
# Study past traffic patterns (like rush hours)
#Predict travel time and congestion
# Suggest the fastest or most efficient route

# So, it is AI because it mimics human-like decision-making to solve navigation problems more efficiently.


##3️⃣ Calculator: no, calculator is not an AI
# A calculator is a conventional computing device that performs mathematical operations like addition, subtraction, multiplication, and division.

### Why it is NOT AI:

#It follows **fixed, pre-programmed rules**
# It does not learn from experience or data
# It cannot make decisions or predictions
# It only gives outputs based on exact inputs and formulas


# So, a calculator is automation, not intelligence.

##4️⃣  Netflix recommendations : Yes, Netflix recommendations are an example of Artificial Intelligence (AI).

# They are used in Netflix to suggest movies and shows you might like.

### Why this is AI:  Netflix uses machine learning algorithms to:

# Study what you watch, pause, or skip.
# Compare your behavior with millions of other users.
# Predict what content you are most likely to enjoy.
# Continuously improve recommendations over time.


##5️⃣ Voice Assistants(Alexa,Siri):Yes, Voice Assistants like Alexa and Siri are examples of Artificial Intelligence (AI).

###Why this is AI: They use speech recognition and natural language processing to:

# understand human voice commands
#  convert speech into text
#  find the correct answer or action
#  respond in a human-like voice