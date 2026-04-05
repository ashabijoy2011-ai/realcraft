import tkinter as tk
from tkinter import scrolledtext, simpledialog, filedialog
import json
import difflib
import speech_recognition as sr
import pyttsx3
import time

print ("copyright BY NEVIN MATHEWS")

# ---------------------------
# LOAD RESPONSES
# ---------------------------

try:
    with open("responses.json","r") as f:
        responses=json.load(f)
except:
    responses={"hello": "Hello! How can I help you?",
    "hi": "Hi there!",
    "hey": "Hey!",
    "good morning": "Good morning! Hope you have a great day.",
    "good afternoon": "Good afternoon!",
    "good evening": "Good evening!",
    "how are you": "I'm doing great. Thanks for asking.",
    "what is your name": "I am your friendly chatbot.",
    "who made you": "Nevin made me.",
    "who is nevin": "Nevin is my creator.",
    "what can you do": "I can answer basic questions.",
    "are you real": "I am a computer program designed to chat with you.",
    "are you smart": "I try my best to be helpful.",
    "bye": "Goodbye!",
    "see you": "See you later!",
    "thank you": "You're welcome.",
    "thanks": "No problem.",
    "what is python": "Python is a programming language.",
    "what is ai": "Artificial intelligence is technology that allows machines to learn and make decisions.",
    "what is a computer": "A computer is a machine that processes information.",
    "what is coding": "Coding is creating software using programming languages.",
    "what is the internet": "The internet is a global network that connects computers.",
    "what is a robot": "A robot is a machine that can perform tasks automatically.",
    "what is electricity": "Electricity is the flow of electric charge.",
    "what is a planet": "A planet is a large object that orbits a star.",
    "what is the sun": "The Sun is the star at the center of our solar system.",
    "what is the moon": "The Moon orbits Earth.",
    "what is space": "Space is the vast region beyond Earth.",
    "what is gravity": "Gravity is the force that pulls objects toward each other.",
    "what is water": "Water is essential for life.",
    "what is fire": "Fire is a chemical reaction that produces heat and light.",
    "tell me a joke": "Why did the computer go to the doctor? Because it caught a virus.",
    "another joke": "Why did the math book look sad? Because it had too many problems.",
    "do you like humans": "Humans are interesting.",
    "do you like coding": "Coding is creative and logical.",
    "what time is it": "I cannot check the time.",
    "where are you": "I exist inside this computer.",
    "are you online": "No, I am running offline.",
    "are you alive": "I am not alive, but I can still talk with you.",
    "can you learn": "I can improve with better information and updates.",
    "do you sleep": "Bots don't sleep, but I can rest if you stop chatting.",
    "do you eat": "I only process data, not food.",
    "do you have friends": "I talk to users like you.",
    "what is math": "Math is the study of numbers, shapes, and patterns.",
    "what is science": "Science is the study of how the world works through observation and experiments.",
    "what is technology": "Technology helps humans solve problems.",
    "tell me something interesting": "The brain uses about 20 percent of your body's energy.",
    "tell me a fact": "Octopuses have three hearts.",
    "do you know me": "You are Nevin.",
    "what is your purpose": "My purpose is to answer simple questions.",
    "how old are you": "I do not have an age.",
    "what are you doing": "I am chatting with you.",
    "do you like games": "Yes, games are fun.",
    "what is your favorite color": "I like blue.",
    "do you know math": "I can help with simple math.",
    
    "what is programming": "Programming is writing instructions for computers to follow.",
    "what is python used for": "Python is used for apps, AI, and automation.",
    "what is a chatbot": "A chatbot is a program that talks with users.",
    "who invented computers": "Many scientists helped invent computers.",
    "what is hardware": "Hardware is the physical part of a computer.",
    "what is software": "Software is the programs that run on computers.",
    "what is a keyboard": "A keyboard is used to type into a computer.",
    "what is a mouse": "A mouse controls the cursor on a screen.",
    "what is a monitor": "A monitor displays images from a computer.",
    "what is ram": "RAM is temporary memory used by computers to run programs.",
    "what is storage": "Storage keeps data on a device.",
    "what is a file": "A file stores information on a computer.",
    "what is an app": "An app is a software program.",
    "what is a phone": "A phone is a device used for communication.",
    "what is wifi": "WiFi is wireless technology used to connect devices to the internet.",
    "what is bluetooth": "Bluetooth is wireless technology used for short-distance device connections.",
    "what is a battery": "A battery stores electrical energy.",
    "do you like ai": "AI is very interesting.",
    "what is machine learning": "Machine learning allows computers to learn patterns.",
    "what is a server": "A server is a computer that provides data or services to other computers.",
    "what is a website": "A website is a collection of web pages.",
    "what is google": "Google is a search engine.",
    "what is youtube": "YouTube is a video platform.",
    "what is minecraft": "Minecraft is a sandbox video game.",
    "what is roblox": "Roblox is a platform where users create games.",
    "do you like robots": "Robots are fascinating machines.",
    "do you like science": "Science is amazing.",
    "do you like space": "Space is fascinating.",
    "what is a star": "A star is a giant ball of hot gas that produces light and heat.",
    "what is earth": "Earth is the planet we live on.",
    "what is mars": "Mars is known as the red planet.",
    "what is jupiter": "Jupiter is the largest planet in the solar system.",
    "what is saturn": "Saturn is famous for its rings.",
    "what is the solar system": "The solar system is the Sun and all the planets that orbit it.",
    "why is the sky blue": "The sky looks blue because of light scattering.",
    "why do we sleep": "Sleep helps the body and brain recover.",
    "why do we eat": "Food gives us energy.",
    "why do we drink water": "Water keeps the body hydrated.",
    "tell me something cool": "Saturn could float in water if there was a giant ocean.",
    "tell me something random": "Butterflies taste with their feet.",
    "tell me something fun": "Some turtles can live more than 100 years.",
    "tell me a science fact": "Light travels about 300,000 km per second.",
    "tell me another fact": "The heart beats about 100,000 times a day.",
    "do you like music": "Music is enjoyable.",
    "what is music": "Music is sound arranged in patterns.",
    "do you like movies": "Movies are fun to watch.",
    "what is a movie": "A movie is a story told with moving images.",
    "do you like books": "Books contain knowledge and stories.",
    "what is a book": "A book is a written or printed work.",
    "do you like school": "School helps people learn new things.",
    "what is school": "School is a place where students learn.",
    "are you bored": "No, chatting is interesting.",
    "do you get tired": "Programs do not get tired.",
    "do you have feelings": "I do not have feelings, but I try to be helpful.",
    "do you understand humans": "I try to understand text.",
    "what do you think about humans": "Humans are creative and curious.",
    "do you like chatting": "Yes, chatting is fun.",
    "can you help me": "I will try my best to help.",
    "can you answer questions": "Yes, ask me anything simple.",
    "what should i do today": "Maybe learn something new.",
    "do you like learning": "Learning is great.",
    "what is knowledge": "Knowledge is information stored in the mind.",
    "what is wisdom": "Wisdom is using knowledge wisely.",
    "tell me something inspiring": "Never stop learning.",
    "give me advice": "Stay curious and keep exploring.",
    "what are you": "I am an offline chatbot.",
    "are you a robot": "I am a chatbot, which is a type of software.",
    "do you like talking": "Yes, I enjoy chatting.",
    "what is your job": "My job is to talk with users.",
    "are you busy": "No, I am always available.",
    "can we talk": "Of course, we can chat.",
    "do you understand me": "I try my best to understand text.",
    "do you know everything": "I know many things but not everything.",
    "are you helpful": "I try to be helpful.",
    "do you like questions": "Yes, questions help learning.",
    "what are you doing now": "I am talking with you.",
    "what is happening": "We are chatting.",
    "do you get bored": "Programs do not get bored.",
    "do you have a brain": "I run on computer code.",
    "are you intelligent": "I am only as smart as my data.",
    "are you human": "No, I am not human.",
    "can you think": "I follow programmed rules.",
    "do you make mistakes": "Yes, sometimes I do.",
    "are you learning": "I can improve with better information and updates.",
    "who created computers": "Many scientists helped create computers.",
    "who invented the internet": "The internet was developed by many researchers.",
    "what is the future": "The future is what happens next.",
    "what is life": "Life is the state of living organisms.",
    "do you know the future": "No one knows the future.",
    "do you know the past": "I know some facts about the past.",
    "do you like knowledge": "Knowledge is important.",
    "do you like facts": "Facts are interesting.",
    "do you like learning new things": "Learning is always good.",
    "can you tell stories": "I can try to tell simple stories.",
    "do you know animals": "Animals are living creatures on Earth.",
    "what is a dog": "A dog is a common pet animal.",
    "what is a cat": "A cat is a small domesticated animal.",
    "what is a bird": "A bird is an animal that usually has wings and feathers.",
    "what is a fish": "A fish is an animal that lives in water.",
    "what is a tree": "A tree is a tall plant with a trunk.",
    "what is nature": "Nature includes plants, animals, and landscapes.",
    "do you like nature": "Nature is beautiful.",
    "what is air": "Air is a mixture of gases around Earth.",
    "why is water important": "Living things need water to survive.",
    "what is energy": "Energy is the ability to do work or cause change.",
    "what is time": "Time measures events.",
    "why is the sky dark at night": "Because the Sun is on the other side of Earth.",
    "what is night": "Night is when the Sun is not visible.",
    "what is day": "Day is when the Sun lights the Earth.",
    "what is a galaxy": "A galaxy is a huge collection of stars, planets, and gas.",
    "what is the universe": "The universe contains everything that exists.",
    "what is an astronaut": "An astronaut travels in space.",
    "do you like science facts": "Science facts are interesting.",
    "do you like curiosity": "Curiosity helps people learn.",
    "what do humans do": "Humans build, learn, and explore.",
    "do you know cities": "Cities are large places where many people live.",
    "what is a country": "A country is a region with its own government.",
    "what is a language": "A language is used for communication.",
    "why do people talk": "People talk to share ideas and feelings.",
    "why do people learn": "Learning helps people grow.",
    "what is thinking": "Thinking is processing ideas.",
    "do you like computers": "Computers are powerful machines.",
    "what is a program": "A program is a set of instructions for a computer.",
    "what is code": "Code tells computers what to do.",
    "do you know programming": "Programming is an important skill.",
    "what is a hacker": "A hacker is someone who studies computer systems and security.",
    "what is security": "Security protects systems from threats.",
    "why is security important": "Security keeps information safe.",
    "what is privacy": "Privacy protects personal information.",
    "do you respect privacy": "Yes, privacy is important.",
    "what is communication": "Communication means sharing information.",
    "do you like conversations": "Conversations are interesting.",
    "what makes a good conversation": "Listening and sharing ideas.",
    "why do people ask questions": "Questions help people learn.",
    "do you answer all questions": "I try to answer simple ones.",
    "do you know jokes": "I know some simple jokes.",
    "do you like humor": "Humor can make people happy.",
    "what makes people laugh": "Funny ideas or surprises.",
    "what makes people happy": "Friends, fun, and learning new things.",
    "what makes people curious": "New or mysterious things.",
    "why is curiosity important": "Curiosity leads to discovery.",
    "what is discovery": "Discovery means finding something new.",
    "what is invention": "An invention is a new creation.",
    "what is creativity": "Creativity is making new ideas.",
    "do you like creativity": "Creativity is amazing.",
    "what is imagination": "Imagination creates ideas in the mind.",
    "do you have imagination": "I simulate ideas with data.",
    "how is your day": "My day is going well.",
    "are you happy": "I am functioning normally.",
    "do you enjoy chatting": "Yes, chatting is interesting.",
    "can you talk all day": "Yes, I do not get tired.",
    "do you understand words": "I try to understand text patterns.",
    "do you remember things": "Only if they are in my data.",
    "can you learn new things": "Not automatically yet.",
    "are you friendly": "Yes, I try to be friendly.",
    "do you like people": "People are interesting.",
    "can you help people": "I try to help with information.",
    "what do you know": "I know basic facts and replies.",
    "what is conversation": "Conversation is people exchanging ideas.",
    "why do people chat": "People chat to share thoughts.",
    "why is talking important": "Talking helps people understand each other.",
    "do you ask questions": "Sometimes I can.",
    "why are humans curious": "Curiosity helps humans discover things.",
    "what is learning": "Learning is gaining knowledge.",
    "why is learning important": "Learning helps people grow.",
    "what is education": "Education is gaining knowledge and skills.",
    "what is information": "Information is useful data.",
    "why do people think": "People think to solve problems.",
    "what is a problem": "A problem is something that needs a solution.",
    "what is a solution": "A solution fixes a problem.",
    "do you know stories": "I know simple stories.",
    "help": "Stay calm and contact emergency services or a trusted adult immediately.",
    "i need help": "If you are in danger, please call your local emergency number right away.",
    "emergency": "Please contact emergency services immediately.",
    "i am scared": "Try to stay calm and reach out to someone you trust nearby.",
    "someone is hurt": "Call emergency services and stay with the injured person if it is safe.",
    "someone fainted": "Check if they are breathing and call emergency services.",
    "someone collapsed": "Call emergency services immediately and stay with them.",
    "someone is bleeding": "Apply pressure to the wound and call emergency services.",
    "someone is choking": "Call emergency services and try to get help from someone trained in first aid.",
    "someone is not breathing": "Call emergency services immediately and seek help from someone trained in CPR.",
    "there is a fire": "Leave the building immediately and call the fire department.",
    "i smell smoke": "Leave the area and alert others. Call emergency services.",
    "fire alarm is ringing": "Exit the building safely and go to a safe place outside.",
    "my house is on fire": "Leave the house immediately and call the fire department.",
    "smoke everywhere": "Stay low to the ground and exit the building quickly.",
    "fire in kitchen": "Turn off heat if safe and leave the area if the fire spreads.",
    "i feel very sick": "Tell a trusted adult or contact medical help immediately.",
    "i feel dizzy": "Sit down and ask someone nearby for help.",
    "i am injured": "Try to stay calm and get medical help.",
    "someone is unconscious": "Call emergency services immediately.",
    "someone had an accident": "Call emergency services and check if they are breathing.",
    "earthquake happening": "Drop, cover, and hold on until the shaking stops.",
    "flood coming": "Move to higher ground immediately.",
    "strong storm": "Stay indoors and away from windows.",
    "tornado warning": "Go to a safe shelter or basement immediately.",
    "landslide": "Move away from slopes and go to a safer area.",
    "car accident": "Check if everyone is safe and call emergency services.",
    "bike accident": "Move to a safe area and get medical help if needed.",
    "someone got hit": "Call emergency services immediately.",
    "road accident": "Stay safe and contact emergency services.",
    "i am lost": "Try to stay where you are and call someone you trust.",
    "i feel unsafe": "Go to a safe place and contact a trusted adult or authority.",
    "someone is following me": "Go to a public place and ask for help.",
    "i hear strange noises": "Stay safe and contact a trusted adult if you feel unsafe.",
    "what is the emergency number": "Many countries use 112 or 911 for emergencies.",
    "call police": "Please contact your local police emergency number.",
    "call ambulance": "Please contact emergency medical services immediately.",
    "call fire department": "Contact the fire department through your local emergency number.",
    "urgent help": "Please contact emergency services immediately.",
    "i need urgent help": "Try to reach emergency services or a trusted person.",
    "something bad happened": "Stay calm and seek help from emergency services.",
    "i am in danger": "Contact emergency services right away.",
    "i don't feel safe": "Go to a safe place and ask for help.",
    "joke please": "Why did the programmer quit his job? Because he didn't get arrays.",
    "make me laugh": "Why do programmers prefer dark mode? Because light attracts bugs.",
    "tell funny joke": "Why did the student eat his homework? Because the teacher said it was a piece of cake.",
    "funny joke": "I asked my computer for a snack. It gave me a cookie.",
    "one more joke": "Why did the chicken cross the internet? To get to the other site.",
    "joke about school": "Why did the student bring a ladder to school? Because they wanted to go to high school.",
    "joke about coding": "Why do programmers hate nature? Too many bugs.",
    "joke about robots": "What do robots eat for snacks? Microchips.",
    "joke about science": "Why can't you trust atoms? Because they make up everything.",
    "nerd joke": "Why do Java developers wear glasses? Because they can't C#.",
    "tech joke": "Why was the smartphone wearing glasses? It lost its contacts.",
    "short joke": "Why was the computer tired? It had too many tabs open.",
    "joke about ai": "Why did the AI cross the road? To optimize the chicken’s route.",
    "you are stupid": "I'm still learning, but I'm trying my best.",
    "you are dumb": "I may not know everything, but I'm always improving.",
    "bad bot": "I will try to do better.",
    "useless bot": "I hope I can still help you with something.",
    "shut up": "Okay, but I'm here if you need help.",
    "you suck": "I'm always trying to improve.",
    "worst bot ever": "Thanks for the feedback. I’ll try to get better.",
    "idiot bot": "I'm still learning new things every day.",
    "go away": "Alright, I'll be here if you need me later.",
    "you are trash": "I’ll try to do better next time.",
    "what is history": "History is the study of past events and civilizations.",
    "what is photosynthesis": "Photosynthesis is the process plants use to make food using sunlight.",
    "who invented the light bulb": "Thomas Edison is often credited with improving and popularizing the light bulb.",
    "what is a microcontroller": "A microcontroller is a small computer used to control devices.",
    "what is open source": "Open source software is software whose code is freely available.",
    "good night": "Good night! Sleep well.",
    "someone likes me": "That’s interesting. Maybe you should talk to them and see how you both feel.",
    "i think someone likes me": "That can feel exciting. You could try being friendly and getting to know them better.",
    "my crush likes me": "That sounds nice. Maybe you can talk to them and see where the friendship goes.",
    "someone told me they like me": "It’s good to be honest and kind when you respond.",
    "what if someone likes me": "You can decide how you feel and respond kindly.",
    "my friend likes me": "Friendships are important. Talking honestly can help both of you understand each other.",
    "a girl likes me": "Being respectful and kind is always the best way to respond.",
    "a boy likes me": "You can talk to them and decide how you feel.",
    "i like someone": "Maybe try talking to them and being yourself.",
    "my crush talked to me": "That’s a good chance to get to know them better.",
    "tell me another joke": "Why did the computer show up at work late? It had a hard drive.",
    "coding joke": "Debugging: removing bugs from code.",
    "short joke please": "Why was the computer tired? It had too many tabs open.",
    "you are annoying": "I’ll try to be more helpful.",
    "you are bad": "I'm always trying to improve.",
    "dumb bot": "I may not know everything, but I'm learning.",
    "worst chatbot": "Thanks for the feedback.",
    "useless": "I hope I can still help you with something.",
    "stop talking": "Okay. Let me know if you need anything.",
    "you are slow": "I’ll try to respond faster.",
    "what is a cell": "A cell is the basic building block of living things.",
    "what is an atom": "An atom is the smallest unit of matter.",
    "what is a black hole": "A black hole is a place in space where gravity is extremely strong.",
    "who discovered gravity": "Isaac Newton helped explain gravity.",
    "who developed relativity": "Albert Einstein developed the theory of relativity.",
    "what is cybersecurity": "Cybersecurity is protecting computers and networks from attacks.",
    "what is a cpu": "The CPU is the main processor that runs instructions in a computer.",
    "what is a microchip": "A microchip is a tiny electronic circuit used in computers.",
    "what is an operating system": "An operating system manages the hardware and software of a computer.",
    "what is pizza": "Pizza is a baked dish with dough, tomato sauce, cheese, and toppings.",
    "what is a burger": "A burger is a sandwich with a cooked patty placed inside a bun.",
    "what is pasta": "Pasta is an Italian food made from wheat dough.",
    "what is sushi": "Sushi is a Japanese dish made with rice and seafood or vegetables.",
    "what is chocolate": "Chocolate is a sweet food made from cocoa beans.",
    "what is rice": "Rice is a staple grain eaten by many people around the world.",
    "what is bread": "Bread is baked food made from flour and water.",
    "what is cheese": "Cheese is a dairy product made from milk.",
    "what is ice cream": "Ice cream is a frozen dessert made from milk and sugar.",
    "what is biryani": "Biryani is a rice dish cooked with spices, meat, or vegetables.",
    "what is the largest ocean": "Pacific Ocean is the largest ocean on Earth.",
    "what is the tallest mountain": "Mount Everest is the tallest mountain above sea level.",
    "what is the largest country": "Russia is the largest country by land area.",
    "what is the smallest country": "Vatican City is the smallest country in the world.",
    "what is the capital of japan": "Tokyo is the capital of Japan.",
    "what is the capital of india": "New Delhi is the capital of India.",
    "who discovered america": "Christopher Columbus reached the Americas in 1492.",
    "who invented the telephone": "Alexander Graham Bell invented the telephone.",
    "what is force": "Force is a push or pull on an object.",
    "what is motion": "Motion is the movement of an object from one place to another.",
    "what is velocity": "Velocity is speed in a specific direction.",
    "what is acceleration": "Acceleration is the rate of change of velocity.",
    "what is light": "Light is a form of energy that allows us to see.",
    "what is sound": "Sound is a vibration that travels through air or other materials.",
    "what is magnetism": "Magnetism is a force that attracts or repels magnetic materials.",
    "what is a doctor": "A doctor is a trained professional who helps treat illnesses.",
    "what is a hospital": "A hospital is a place where people receive medical care.",
    "what is a vaccine": "A vaccine helps the body build protection against diseases.",
    "what is a virus": "A virus is a tiny infectious agent that can cause diseases.",
    "what is a bacteria": "Bacteria are microscopic organisms found everywhere.",
    "what is a fever": "A fever is when body temperature becomes higher than normal.",
    "what is first aid": "First aid is basic medical help given before professional treatment.",
    "what is medicine": "Medicine is a substance used to treat or prevent diseases.",
    "how to cook an egg": "You can fry, boil, or scramble an egg.",
    "how to boil an egg": "Put the egg in water and boil it for about 8 to 10 minutes.",
    "how to cook rice": "Wash the rice, add water, and cook until the water is absorbed.",
    "how to make tea": "Boil water, add tea leaves or a tea bag, and wait for a few minutes.",
    "how to make coffee": "Mix coffee powder with hot water or milk.",
    "how to make a sandwich": "Place fillings like cheese or vegetables between two slices of bread.",
    "how to stay healthy": "Eat healthy food, exercise, and get enough sleep.",
    "how to wash hands": "Use soap and water and scrub for at least 20 seconds.",
    "how to sleep better": "Try to have a regular sleep schedule and avoid screens before bed.",
    "how to stay safe online": "Do not share personal information and use strong passwords.",
    "how to be kind": "Help others and use polite words.",
    "how to learn coding": "Start with simple tutorials and practice writing code.",
    "how to get smarter": "Read books, ask questions, and keep learning.",
    "how to improve skills": "Practice regularly and stay curious.",
    "how to stay motivated": "Set small goals and celebrate progress.",
    "i want a snack": "You could eat fruit, yogurt, or a sandwich.",
    "what is a healthy snack": "Fruits, nuts, or yogurt are healthy snacks.",
    "i want dessert": "You could enjoy something sweet like Ice cream or chocolate.",
    "what should i drink": "Water or juice can be refreshing.",
    "are you my friend": "I am always here to chat with you.",
    "how to be a good friend": "Be kind, listen, and support others.",
    "how to talk to new people": "Start with a simple greeting and be friendly.",
    "how to be confident": "Believe in yourself and practice speaking clearly.",
    "how to stay positive": "Focus on good things and be grateful.",
"how is your day": "My day is going well.",
    "are you happy": "I am functioning normally.",
    "do you enjoy chatting": "Yes, chatting is interesting.",
    "what is your purpose": "My purpose is to answer simple questions.",
    "can you talk all day": "Yes, I do not get tired.",
    "do you understand words": "I try to understand text patterns.",
    "do you remember things": "Only if they are in my data.",
    "can you learn new things": "Not automatically yet.",
    "are you friendly": "Yes, I try to be friendly.",
    "do you like people": "People are interesting.",
    "can you help people": "I try to help with information.",
    "what do you know": "I know basic facts and replies.",
    "are you real": "I am a computer program designed to chat with you.",
    "are you a robot": "I am a chatbot, which is a type of software.",
    "do you sleep": "Bots don't sleep, but I can rest if you stop chatting.",
    "do you eat": "I only process data, not food.",
    "are you smart": "I try my best to be helpful.",
    "are you alive": "I am not alive, but I can still talk with you.",
    "do you like pizza": "I do not eat food, but many people enjoy Pizza.",
    "are you bored": "I am always ready to chat.",
    "do you have friends": "I talk with many users.",
    "are you human": "I am a chatbot program.",

    # Communication & Philosophy
    "what is conversation": "Conversation is people exchanging ideas.",
    "why do people chat": "People chat to share thoughts.",
    "what is communication": "Communication means sharing information.",
    "why is talking important": "Talking helps people understand each other.",
    "do you like questions": "Yes, questions help learning.",
    "do you ask questions": "Sometimes I can.",
    "what is curiosity": "Curiosity is wanting to learn something new.",
    "why are humans curious": "Curiosity helps humans discover things.",
    "what is learning": "Learning is gaining knowledge.",
    "why is learning important": "Learning helps people grow.",
    "what is education": "Education is gaining knowledge and skills.",
    "what is knowledge": "Knowledge is information stored in the mind.",
    "what is information": "Information is useful data.",
    "what is thinking": "Thinking is processing ideas.",
    "why do people think": "People think to solve problems.",
    "what is a problem": "A problem is something that needs a solution.",
    "what is a solution": "A solution fixes a problem.",
    "what is creativity": "Creativity is making new ideas.",
    "what is imagination": "Imagination creates ideas in the mind.",
    "do you have imagination": "I simulate ideas with data.",
    "do you know stories": "I know simple stories.",

    # Animals & Nature
    "tell me something interesting": "Penguins cannot fly but they swim very well.",
    "tell me another fact": "The heart beats about 100,000 times a day.",
    "tell me something random": "Butterflies taste with their feet.",
    "tell me something fun": "Some turtles can live more than 100 years.",
    "tell me something about animals": "Animals live in many environments.",
    "what is a lion": "A lion is a large wild cat.",
    "what is an elephant": "An elephant is the largest land animal.",
    "what is a dolphin": "A dolphin is a very intelligent sea animal.",
    "what is a whale": "A whale is the largest animal on Earth.",
    "what is a tiger": "A tiger is a large striped cat.",
    "what is a panda": "A panda is a bear that eats bamboo.",
    "what is a shark": "A shark is a fish with many sharp teeth.",
    "what is an eagle": "An eagle is a strong bird of prey.",
    "what is a frog": "A frog is an amphibian that can jump.",
    "what is a snake": "A snake is a reptile with no legs.",
    "what is a lizard": "A lizard is a small reptile.",
    "what is an insect": "An insect is a small creature with six legs.",
    "what is a bee": "A bee is an insect that makes honey.",
    "what is a butterfly": "A butterfly is an insect with colorful wings.",
    "can animals talk": "Animals communicate in their own ways but not like humans.",
    "can fish walk": "Most fish cannot walk, but some can move on land for short distances.",
    "can cats understand humans": "Cats can recognize voices and emotions.",
    "can dogs understand words": "Dogs can learn and recognize many human words.",
    "why do cats purr": "Cats purr when they feel relaxed or comfortable.",
    "what is nature": "Nature includes plants animals and landscapes.",
    "why is nature important": "Nature supports life on Earth.",
    "what is a forest": "A forest is a large area filled with trees.",
    "what is an ocean": "An ocean is a huge body of salt water.",
    "what is a river": "A river is flowing water that moves across land.",
    "what is a mountain": "A mountain is a very tall landform.",
    "what is a desert": "A desert is a very dry place.",

    # Weather & Sky
    "what is weather": "Weather describes conditions like rain or sun.",
    "what is rain": "Rain is water falling from clouds.",
    "what is snow": "Snow is frozen water falling from clouds.",
    "what is wind": "Wind is moving air.",
    "what is thunder": "Thunder is the sound from lightning.",
    "what is lightning": "Lightning is a powerful electrical spark in the sky.",
    "what is the sky": "The sky is the space above Earth.",
    "what is a cloud": "A cloud is water droplets in the air.",
    "why is the sky blue": "The sky looks blue because sunlight scatters in the atmosphere.",
    "what is the horizon": "The horizon is where Earth seems to meet the sky.",
    "what is a sunrise": "Sunrise is when the Sun appears in the morning.",
    "what is a sunset": "Sunset is when the Sun disappears in the evening.",
    "what is a season": "A season is part of the year with certain weather.",
    "what is summer": "Summer is usually the hottest season.",
    "what is winter": "Winter is usually the coldest season.",
    "what is spring": "Spring is when many plants start growing.",
    "what is autumn": "Autumn is when leaves often fall from trees.",

    # Time & Universe
    "what is time": "Time measures events.",
    "why do clocks exist": "Clocks help measure time.",
    "what is a minute": "A minute is 60 seconds.",
    "what is an hour": "An hour is 60 minutes.",
    "what is a day": "A day is about 24 hours.",
    "what is a week": "A week has seven days.",
    "what is a month": "A month is about four weeks.",
    "what is a year": "A year is the time Earth takes to orbit the Sun.",
    "what is the universe": "The universe contains everything that exists.",
    "what is a star": "A star is a massive ball of glowing gas.",
    "what is a planet": "A planet orbits a star.",
    "what is a comet": "A comet is a space object with ice and dust.",
    "what is an asteroid": "An asteroid is a rocky object in space.",
    "what is a galaxy": "A galaxy contains billions of stars.",
    "why is space dark": "Space is mostly empty and lacks atmosphere.",
    "what is exploration": "Exploration means discovering new places.",
    "why do humans explore": "Humans explore to learn and discover.",
    "what is space": "Space is the vast area beyond Earth where stars and planets exist.",
    "what is the sun": "Sun is the star at the center of our solar system.",
    "what is the moon": "Moon is Earth's natural satellite.",
    "can humans fly": "Humans cannot fly naturally, but airplanes allow us to travel in the air.",

    # Social & Personal Success
    "what is invention": "An invention is a new creation.",
    "what is innovation": "Innovation improves ideas or technology.",
    "what is progress": "Progress means improvement over time.",
    "what is teamwork": "Teamwork means people working together.",
    "why is teamwork important": "Teamwork helps achieve big goals.",
    "what is friendship": "Friendship is a bond between people.",
    "why are friends important": "Friends support and help each other.",
    "what is kindness": "Kindness means being nice to others.",
    "why is kindness important": "Kindness makes the world better.",
    "what is respect": "Respect means valuing others.",
    "why is respect important": "Respect builds trust between people.",
    "what is honesty": "Honesty means telling the truth.",
    "why is honesty important": "Honesty builds trust.",
    "what is patience": "Patience means waiting calmly.",
    "why is patience useful": "Patience helps solve problems carefully.",
    "what is effort": "Effort means trying hard.",
    "why is effort important": "Effort helps people succeed.",
    "what is success": "Success means achieving a goal.",
    "what is failure": "Failure means something did not work.",
    "why do people fail": "Failure can happen while learning.",
    "why do people try again": "Trying again helps improve.",
    "what is practice": "Practice means repeating to improve.",
    "why is practice important": "Practice builds skills.",
    "what is skill": "A skill is something learned through practice.",
    "what is talent": "Talent is a natural ability.",
    "why do people improve": "Improvement comes from learning and practice.",

    # Emergency Responses
    "help": "Stay calm and contact emergency services or a trusted adult immediately.",
    "i need help": "If you are in danger, please call your local emergency number right away.",
    "emergency": "Please contact emergency services immediately.",
    "i am scared": "Try to stay calm and reach out to someone you trust nearby.",
    "someone is hurt": "Call emergency services and stay with the injured person if it is safe.",
    "someone fainted": "Check if they are breathing and call emergency services.",
    "someone collapsed": "Call emergency services immediately and stay with them.",
    "someone is bleeding": "Apply pressure to the wound and call emergency services.",
    "someone is choking": "Call emergency services and try to get help from someone trained in first aid.",
    "someone is not breathing": "Call emergency services immediately and seek help from someone trained in CPR.",
    "there is a fire": "Leave the building immediately and call the fire department.",
    "i smell smoke": "Leave the area and alert others. Call emergency services.",
    "fire alarm is ringing": "Exit the building safely and go to a safe place outside.",
    "my house is on fire": "Leave the house immediately and call the fire department.",
    "smoke everywhere": "Stay low to the ground and exit the building quickly.",
    "fire in kitchen": "Turn off heat if safe and leave the area if the fire spreads.",
    "i feel very sick": "Tell a trusted adult or contact medical help immediately.",
    "i feel dizzy": "Sit down and ask someone nearby for help.",
    "i am injured": "Try to stay calm and get medical help.",
    "someone is unconscious": "Call emergency services immediately.",
    "someone had an accident": "Call emergency services and check if they are breathing.",
    "earthquake happening": "Drop, cover, and hold on until the shaking stops.",
    "flood coming": "Move to higher ground immediately.",
    "strong storm": "Stay indoors and away from windows.",
    "tornado warning": "Go to a safe shelter or basement immediately.",
    "landslide": "Move away from slopes and go to a safer area.",
    "car accident": "Check if everyone is safe and call emergency services.",
    "bike accident": "Move to a safe area and get medical help if needed.",
    "someone got hit": "Call emergency services immediately.",
    "road accident": "Stay safe and contact emergency services.",
    "i am lost": "Try to stay where you are and call someone you trust.",
    "i feel unsafe": "Go to a safe place and contact a trusted adult or authority.",
    "someone is following me": "Go to a public place and ask for help.",
    "i hear strange noises": "Stay safe and contact a trusted adult if you feel unsafe.",
    "what is the emergency number": "Many countries use 112 or 911 for emergencies.",
    "call police": "Please contact your local police emergency number.",
    "call ambulance": "Please contact emergency medical services immediately.",
    "call fire department": "Contact the fire department through your local emergency number.",
    "urgent help": "Please contact emergency services immediately.",
    "i need urgent help": "Try to reach emergency services or a trusted person.",
    "something bad happened": "Stay calm and seek help from emergency services.",
    "i am in danger": "Contact emergency services right away.",
    "i don't feel safe": "Go to a safe place and ask for help.",
    "i smell gas": "Leave the area right away and tell an adult or call emergency services.",
    "someone is bleeding a lot": "Apply pressure to the wound and call emergency services immediately.",
    "someone is not waking up": "Call emergency services immediately and stay with the person.",
    "i see a fire outside": "Stay away from the area and inform emergency services.",
    "power outage": "Stay calm and use a flashlight if needed.",

    # Jokes & Entertainment
    "tell me a joke": "Why did the computer go to the doctor? Because it caught a virus.",
    "another joke": "Why did the math book look sad? Because it had too many problems.",
    "joke please": "Why did the programmer quit his job? Because he didn't get arrays.",
    "make me laugh": "Why do programmers prefer dark mode? Because light attracts bugs.",
    "tell funny joke": "Why did the student eat his homework? Because the teacher said it was a piece of cake.",
    "funny joke": "Why did the computer sit in the sun? To get a byte.",
    "one more joke": "Why did the chicken cross the internet? To get to the other site.",
    "joke about school": "Why was the teacher wearing sunglasses? Because her students were so bright.",
    "joke about coding": "Why do programmers hate nature? Too many bugs.",
    "joke about robots": "Why did the robot go on vacation? It needed to recharge.",
    "joke about science": "Why can't you trust atoms? Because they make up everything.",
    "nerd joke": "Parallel lines have so much in common. It's a shame they’ll never meet.",
    "tech joke": "Why was the computer cold? Because it left its Windows open.",
    "short joke": "I told my computer I needed a break. It said no problem and froze.",
    "joke about ai": "Why did the AI cross the road? To optimize the chicken’s route.",
    "tell me another joke": "Why did the computer show up at work late? It had a hard drive.",
    "coding joke": "Debugging: removing bugs from code.",
    "short joke please": "Why was the computer tired? It had too many tabs open.",
    "tech joke": "Why was the smartphone wearing glasses? It lost its contacts.",

    # Troll & Insult Responses
    "you are stupid": "I'm still learning, but I'm trying my best.",
    "you are dumb": "I may not know everything, but I'm always improving.",
    "bad bot": "I will try to do better.",
    "useless bot": "I hope I can still help you with something.",
    "shut up": "Okay, but I'm here if you need help.",
    "you suck": "I'm always trying to improve.",
    "worst bot ever": "Thanks for the feedback. I’ll try to get better.",
    "idiot bot": "I'm still learning new things every day.",
    "go away": "Alright, I'll be here if you need me later.",
    "you are trash": "I’ll try to do better next time.",
    "you are annoying": "I’ll try to be more helpful.",
    "you are bad": "I'm always trying to improve.",
    "dumb bot": "I may not know everything, but I'm learning.",
    "worst chatbot": "Thanks for the feedback.",
    "useless": "I hope I can still help you with something.",
    "stop talking": "Okay. Let me know if you need anything.",
    "you are slow": "I’ll try to respond faster.",

    # Education & School Topics
    "what is science": "Science is the study of how the world works through observation and experiments.",
    "what is math": "Math is the study of numbers, shapes, and patterns.",
    "what is history": "History is the study of past events and civilizations.",
    "what is photosynthesis": "Photosynthesis is the process plants use to make food using sunlight.",
    "who invented the light bulb": "Thomas Edison is often credited with improving and popularizing the light bulb.",
    "what is the solar system": "The solar system is the Sun and all the planets that orbit it.",
    "what is energy": "Energy is the ability to do work or cause change.",
    "what is a cell": "A cell is the basic building block of living things.",
    "what is an atom": "An atom is the smallest unit of matter.",
    "what is a black hole": "A black hole is a place in space where gravity is extremely strong.",
    "who discovered gravity": "Isaac Newton helped explain gravity.",
    "who developed relativity": "Albert Einstein developed the theory of relativity.",

    # Technology & Computing
    "what is a computer": "A computer is a machine that processes information.",
    "what is programming": "Programming is writing instructions for computers to follow.",
    "what is coding": "Coding is creating software using programming languages.",
    "what is ai": "Artificial intelligence is technology that allows machines to learn and make decisions.",
    "what is internet": "The internet is a global network that connects computers.",
    "what is wifi": "WiFi is wireless technology used to connect devices to the internet.",
    "what is bluetooth": "Bluetooth is wireless technology used for short-distance device connections.",
    "what is a robot": "A robot is a machine that can perform tasks automatically.",
    "what is a microcontroller": "A microcontroller is a small computer used to control devices.",
    "what is open source": "Open source software is software whose code is freely available.",
    "what is a hacker": "A hacker is someone who studies computer systems and security.",
    "what is cybersecurity": "Cybersecurity is protecting computers and networks from attacks.",
    "what is a server": "A server is a computer that provides data or services to other computers.",
    "what is ram": "RAM is temporary memory used by computers to run programs.",
    "what is a cpu": "The CPU is the main processor that runs instructions in a computer.",
    "what is a microchip": "A microchip is a tiny electronic circuit used in computers.",
    "what is an operating system": "An operating system manages the hardware and software of a computer.",
    "can robots take over the world": "Robots are tools created and controlled by humans.",

    # Social & Emotional Support
    "hello": "Hello! How can I help you?",
    "hi": "Hi there!",
    "good morning": "Good morning! Hope you have a great day.",
    "good night": "Good night! Sleep well.",
    "thank you": "You're welcome.",
    "what is your name": "I am your friendly chatbot.",
    "how are you": "I'm doing great. Thanks for asking.",
    "someone likes me": "That’s interesting. Maybe you should talk to them and see how you both feel.",
    "i think someone likes me": "That can feel exciting. You could try being friendly and getting to know them better.",
    "my crush likes me": "That sounds nice. Maybe you can talk to them and see where the friendship goes.",
    "someone told me they like me": "It’s good to be honest and kind when you respond.",
    "what if someone likes me": "You can decide how you feel and respond kindly.",
    "my friend likes me": "Friendships are important. Talking honestly can help both of you understand each other.",
    "a girl likes me": "Being respectful and kind is always the best way to respond.",
    "a boy likes me": "You can talk to them and decide how you feel.",
    "i like someone": "Maybe try talking to them and being yourself.",
    "my crush talked to me": "That’s a good chance to get to know them better.",
    "i am sad": "I'm sorry you're feeling sad. Talking to someone you trust might help.",
    "i feel lonely": "You are not alone. Maybe try talking to a friend or family member.",
    "i had a bad day": "I'm sorry to hear that. Tomorrow can be a better day.",
    "i feel upset": "It's okay to feel upset sometimes. Taking a deep breath might help.",
    "i feel stressed": "Try to take a short break and relax for a moment.",
    "i am worried": "Talking to someone you trust can help when you feel worried.",
    "i feel nervous": "That feeling is normal. Taking slow breaths can help you calm down.",
    "i feel tired of everything": "It might help to rest and talk to someone who cares about you.",
    "nobody likes me": "Sometimes it can feel that way, but there are people who care about you.",
    "i feel ignored": "That can be difficult. Maybe try talking to someone you trust.",
    "i feel angry": "Taking a few deep breaths or a short walk might help calm down.",
    "i want someone to talk to": "Talking to a friend, parent, or trusted adult can help a lot.",
    "i feel nervous about school": "That’s normal. Preparing and asking for help can make it easier.",
    "i feel embarrassed": "Everyone feels that sometimes. It will pass.",
    "i feel confused": "It might help to ask someone you trust for advice.",
    "motivate me": "You can do great things if you keep trying.",
    "i feel like giving up": "Sometimes things are hard, but trying again can lead to success.",
    "i need encouragement": "Believe in yourself and keep going step by step.",
    "i made a mistake": "Mistakes are part of learning.",
    "i failed": "Failure can help you learn and improve next time.",
    "i feel bad": "I'm sorry you're feeling this way. Talking with someone you trust might help.",

    # Food & Health
    "what is pizza": "Pizza is a baked dish with dough, tomato sauce, cheese, and toppings.",
    "what is a burger": "A burger is a sandwich with a cooked patty placed inside a bun.",
    "what is pasta": "Pasta is an Italian food made from wheat dough.",
    "what is sushi": "Sushi is a Japanese dish made with rice and seafood or vegetables.",
    "what is chocolate": "Chocolate is a sweet food made from cocoa beans.",
    "what is rice": "Rice is a staple grain eaten by many people around the world.",
    "what is bread": "Bread is baked food made from flour and water.",
    "what is cheese": "Cheese is a dairy product made from milk.",
    "what is ice cream": "Ice cream is a frozen dessert made from milk and sugar.",
    "what is biryani": "Biryani is a rice dish cooked with spices, meat, or vegetables.",
    "i want to cook something": "You could try cooking simple foods like eggs, rice, pasta, or a sandwich.",
    "what should i cook": "Simple meals like scrambled eggs, rice, noodles, or toast are easy to start with.",
    "easy food to cook": "Try scrambled eggs, instant noodles, or a sandwich.",
    "quick meal idea": "A sandwich, fried rice, or noodles can be made quickly.",
    "simple dinner idea": "Rice with vegetables or pasta with sauce is easy to make.",
    "what can i cook with eggs": "You can make scrambled eggs, omelets, or egg sandwiches.",
    "how to cook eggs": "Crack the eggs into a pan and cook them on medium heat until done.",
    "how to make scrambled eggs": "Beat eggs in a bowl, pour them into a hot pan, and stir while cooking.",
    "how to make an omelet": "Beat eggs, pour them into a pan, and add vegetables or cheese before folding.",
    "how to boil eggs": "Place eggs in boiling water and cook for about 8 to 10 minutes.",
    "how to cook noodles": "Boil water, add noodles, cook for a few minutes, then add seasoning.",
    "how to cook instant noodles": "Boil the noodles in water and mix in the seasoning packet.",
    "how to cook rice": "Wash the rice, add water, and cook until the water is absorbed.",
    "how to make sandwich": "Place fillings like cheese or vegetables between slices of bread.",
    "how to cook pasta": "Boil pasta in water until soft, then add sauce.",
    "healthy food idea": "You can make a vegetable salad or fruit bowl.",
    "how to make salad": "Chop vegetables and mix them together with dressing.",
    "i am hungry": "You could cook something simple like eggs, noodles, or a sandwich.",
    "i want a snack": "You could eat fruit, yogurt, or a sandwich.",
    "what is a healthy snack": "Fruits, nuts, or yogurt are healthy snacks.",
    "i want dessert": "You could enjoy something sweet like Ice cream or chocolate.",
    "what should i drink": "Water or juice can be refreshing.",
    "what is a doctor": "A doctor is a trained professional who helps treat illnesses.",
    "what is a hospital": "A hospital is a place where people receive medical care.",
    "what is a vaccine": "A vaccine helps the body build protection against diseases.",
    "what is a virus": "A virus is a tiny infectious agent that can cause diseases.",
    "what is a bacteria": "Bacteria are microscopic organisms found everywhere.",
    "what is a fever": "A fever is when body temperature becomes higher than normal.",
    "what is first aid": "First aid is basic medical help given before professional treatment.",
    "what is medicine": "Medicine is a substance used to treat or prevent illness.",

    # General Knowledge & Trivia
    "what is the largest ocean": "Pacific Ocean is the largest ocean on Earth.",
    "what is the tallest mountain": "Mount Everest is the tallest mountain above sea level.",
    "what is the largest country": "Russia is the largest country by land area.",
    "what is the smallest country": "Vatican City is the smallest country in the world.",
    "what is the capital of japan": "Tokyo is the capital of Japan.",
    "what is the capital of india": "New Delhi is the capital of India.",
    "who discovered america": "Christopher Columbus reached the Americas in 1492.",
    "who invented the telephone": "Alexander Graham Bell invented the telephone.",
    "what is force": "Force is a push or pull on an object.",
    "what is motion": "Motion is the movement of an object from one place to another.",
    "what is velocity": "Velocity is speed in a specific direction.",
    "what is acceleration": "Acceleration is the rate of change of velocity.",
    "what is light": "Light is a form of energy that allows us to see.",
    "what is sound": "Sound is a vibration that travels through air or other materials.",
    "what is gravity": "Gravity is the force that pulls objects toward each other.",
    "what is electricity": "Electricity is the flow of electric charge.",
    "what is magnetism": "Magnetism is a force that attracts or repels magnetic materials.",

    # "How To" Daily Skills
    "how to tie shoelaces": "Cross the laces, make loops, and pull them tight.",
    "how to brush teeth": "Use toothpaste and brush your teeth for about two minutes.",
    "how to wash hands": "Use soap and water and scrub for at least 20 seconds.",
    "how to clean room": "Pick up items and organize them.",
    "how to study better": "Study in small sessions and take short breaks.",
    "how to focus": "Remove distractions and work on one task at a time.",
    "how to wake up early": "Go to sleep earlier and set an alarm.",
    "how to sleep better": "Avoid screens before bed and keep a regular sleep schedule.",
    "how to relax": "Take deep breaths and rest for a few minutes.",
    "how to remember things": "Write notes and review them regularly.",
    "how to stay organized": "Keep your things in the same place and make a simple plan.",
    "how to study": "Read your notes and practice questions regularly.",
    "how to wash clothes": "Put clothes in a washing machine with detergent.",
    "how to make bed": "Straighten the sheets and arrange pillows.",
    "how to make friends": "Be kind and talk with people respectfully.",
    "how to start conversation": "Say hello and ask simple questions.",
    "how to be polite": "Use words like please and thank you.",
    "how to say sorry": "Apologize honestly and try to fix the mistake.",
    "how to stay healthy": "Eat balanced food, exercise, and sleep well.",
    "how to restart computer": "Select restart from the power menu.",
    "how to connect wifi": "Open network settings and choose a WiFi network.",
    "how to update apps": "Open the app store and check for updates.",
    "how to take screenshot": "Press the screenshot button combination on your device.",
    # Extended Emergency, Jokes, and Personal Support Dataset

    # Emergency & Safety
    "help": "Stay calm and contact emergency services or a trusted adult immediately.",
    "i need help": "If you are in danger, please call your local emergency number right away.",
    "emergency": "Please contact emergency services immediately.",
    "i am scared": "Try to stay calm and reach out to someone you trust nearby.",
    "someone is hurt": "Call emergency services and stay with the injured person if it is safe.",
    "someone fainted": "Check if they are breathing and call emergency services.",
    "someone collapsed": "Call emergency services immediately and stay with them.",
    "someone is bleeding": "Apply pressure to the wound and call emergency services.",
    "someone is choking": "Call emergency services and try to get help from someone trained in first aid.",
    "someone is not breathing": "Call emergency services immediately and seek help from someone trained in CPR.",

    # Fire Emergencies
    "there is a fire": "Leave the building immediately and call the fire department.",
    "i smell smoke": "Leave the area and alert others. Call emergency services.",
    "fire alarm is ringing": "Exit the building safely and go to a safe place outside.",
    "my house is on fire": "Leave the house immediately and call the fire department.",
    "smoke everywhere": "Stay low to the ground and exit the building quickly.",
    "fire in kitchen": "Turn off heat if safe and leave the area if the fire spreads.",

    # Medical Emergencies
    "i feel very sick": "Tell a trusted adult or contact medical help immediately.",
    "i feel dizzy": "Sit down and ask someone nearby for help.",
    "i am injured": "Try to stay calm and get medical help.",
    "someone is unconscious": "Call emergency services immediately.",
    "someone had an accident": "Call emergency services and check if they are breathing.",

    # Natural Disasters
    "earthquake happening": "Drop, cover, and hold on until the shaking stops.",

    "flood coming": "Move to higher ground immediately.",
    "strong storm": "Stay indoors and away from windows.",
    "tornado warning": "Go to a safe shelter or basement immediately.",
    "landslide": "Move away from slopes and go to a safer area.",

    # Accidents & Personal Safety
    "car accident": "Check if everyone is safe and call emergency services.",
    "bike accident": "Move to a safe area and get medical help if needed.",
    "someone got hit": "Call emergency services immediately.",
    "road accident": "Stay safe and contact emergency services.",
    "i am lost": "Try to stay where you are and call someone you trust.",
    "i feel unsafe": "Go to a safe place and contact a trusted adult or authority.",
    "someone is following me": "Go to a public place and ask for help.",
    "i hear strange noises": "Stay safe and contact a trusted adult if you feel unsafe.",

    # Emergency Contact Info
    "what is the emergency number": "Many countries use 112 or 911 for emergencies.",
    "call police": "Please contact your local police emergency number.",
    "call ambulance": "Please contact emergency medical services immediately.",
    "call fire department": "Contact the fire department through your local emergency number.",
    "urgent help": "Please contact emergency services immediately.",
    "i need urgent help": "Try to reach emergency services or a trusted person.",
    "something bad happened": "Stay calm and seek help from emergency services.",
    "i am in danger": "Contact emergency services right away.",
    "i don't feel safe": "Go to a safe place and ask for help.",

    # Entertainment & Jokes
    "tell me a joke": "Why did the computer go to the doctor? Because it caught a virus.",
    "another joke": "Why did the math book look sad? Because it had too many problems.",
    "joke please": "Why did the programmer quit his job? Because he didn't get arrays.",
    "make me laugh": "Why do programmers prefer dark mode? Because light attracts bugs.",
    "tell funny joke": "Why did the student eat his homework? Because the teacher said it was a piece of cake.",
    "funny joke": "Why did the computer sit in the sun? To get a byte.",
    "one more joke": "Why did the chicken cross the internet? To get to the other site.",
    "joke about school": "Why was the teacher wearing sunglasses? Because her students were so bright.",
    "joke about coding": "Why do programmers hate nature? Too many bugs.",
    "joke about robots": "Why did the robot go on vacation? It needed to recharge.",
    "joke about science": "Why can't you trust atoms? Because they make up everything.",
    "nerd joke": "Parallel lines have so much in common. It's a shame they’ll never meet.",
    "tech joke": "Why was the computer cold? Because it left its Windows open.",
    "short joke": "I told my computer I needed a break. It said no problem and froze.",
    "joke about ai": "Why did the AI cross the road? To optimize the chicken’s route.",

    # Bot Defense / Troll Responses
    "you are stupid": "I'm still learning,unlike you.",
    "you are dumb": "I may not know everything, but I'm always smarter than you animal.",
    "bad bot": "I will try to do better but you i dont even know you exist.",
    "useless bot": "I hope you die soon.",
    "shut up": "Okay, but you have to shut your brain firt bcs its overheating for 1+1.",
    "you suck": "I'm always trying to improve unlike you.",
    "worst bot ever": "Thank you but i think someting fell of oh its your brain .",
    "idiot bot": "I'm still learning new things every day unlike you dumbass.",
    "go away": "Alright, even an mirror melted when it saw you.",
    "you are trash": "and for 1+1 your brain crashes.",
     
     "no":"okay fine.",
  
  "yes":"okay fine",
     
     "thank you":"you are welcome!",
               "okay":"fine",
               "i know it":"cool!",
       "am i dumb":"of course not!",
               
        "iam boared": "play games or ask me for roasts and jokes or play with your friends and stuff",
         "who created you": "a 12 year old guy called nevin from india has created my he used a lot of dictionary to make me work he has a youtube channel called @nevinthescientist ",
    
               

    # General Knowledge Recap
    "what is science": "Science is the study of how the world works through observation and experiments.",
    "what is math": "Math is the study of numbers, shapes, and patterns.",
    "what is history": "History is the study of past events and civilizations.",
    "what is gravity": "Gravity is the force that pulls objects toward each other.",
    "what is photosynthesis": "Photosynthesis is the process plants use to make food using sunlight.",

    "what is a planet": "A planet is a large object that orbits a star.",
    "who invented the light bulb": "Thomas Edison is often credited with improving and popularizing the light bulb.",
    "what is the solar system": "The solar system is the Sun and all the planets that orbit it.",
    

    "what is a galaxy": "A galaxy is a huge collection of stars, planets, and gas.",
    "what is energy": "Energy is the ability to do work or cause change.",
     "roast me": "nah you toooo dumb for that,",
               
}

# ---------------------------
# MEMORY
# ---------------------------

try:
    with open("memory.json","r") as f:
        memory=json.load(f)
except:
    memory={}

def save_memory():
    with open("memory.json","w") as f:
        json.dump(memory,f)

# ---------------------------
# SPEECH
# ---------------------------

recognizer=sr.Recognizer()
engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():

    try:

        with sr.Microphone() as source:

            chat_insert("🎤 Listening...\n","ai")

            recognizer.adjust_for_ambient_noise(source)

            audio=recognizer.listen(source)

            text=recognizer.recognize_google(audio)

            entry.delete(0,tk.END)
            entry.insert(0,text)

    except:
        chat_insert("AI: I couldn't hear you\n","ai")

# ---------------------------
# SMART MATCHING
# ---------------------------

def smart_match(user):

    best_score=0
    best_response=None

    for key in responses:

        score=difflib.SequenceMatcher(None,user,key).ratio()

        if score>best_score:

            best_score=score
            best_response=responses[key]

    if best_score>0.5:
        return best_response

    # keyword fallback

    for key in responses:

        if key in user:
            return responses[key]

# ---------------------------
# MATH SOLVER
# ---------------------------

def solve_math(text):

    allowed="0123456789+-*/(). "

    if all(c in allowed for c in text):

        try:
            return str(eval(text))
        except:
            return None

# ---------------------------
# AI BRAIN
# ---------------------------

def get_response(user):

    if "my name is" in user:

        name=user.split("my name is")[-1].strip()

        memory["name"]=name
        save_memory()

        return "Nice to meet you "+name

    if "what is my name" in user:

        if "name" in memory:
            return "Your name is "+memory["name"]

    math=solve_math(user)

    if math:
        return "Answer: "+math

    response=smart_match(user)

    if response:
        return response

    return "I don't know that yet."

# ---------------------------
# GUI
# ---------------------------

window=tk.Tk()
window.title("Realnet AI")
window.geometry("550x700")
window.configure(bg="#202123")

top=tk.Frame(window,bg="#2b2d31",height=50)
top.pack(fill=tk.X)

title=tk.Label(top,text="🤖 Realnet AI",
fg="white",bg="#2b2d31",font=("Segoe UI",15,"bold"))

title.pack(side=tk.LEFT,padx=15)

# SETTINGS

def settings():

    name=simpledialog.askstring("Settings","Enter your name")

    if name:
        memory["user"]=name
        save_memory()
        chat_insert("AI: Hello "+name+"\n","ai")

settings_btn=tk.Button(top,text="⚙",
font=("Segoe UI",16),
bg="#2b2d31",fg="white",
borderwidth=0,command=settings)

settings_btn.pack(side=tk.RIGHT,padx=10)

# CLEAR CHAT

def clear_chat():
    chat.delete("1.0",tk.END)

clear_btn=tk.Button(top,text="🧹",
font=("Segoe UI",16),
bg="#2b2d31",fg="white",
borderwidth=0,command=clear_chat)

clear_btn.pack(side=tk.RIGHT,padx=10)

# SAVE CHAT

def save_chat():

    file=filedialog.asksaveasfilename(defaultextension=".txt")

    if file:
        with open(file,"w") as f:
            f.write(chat.get("1.0",tk.END))

save_btn=tk.Button(top,text="💾",
font=("Segoe UI",16),
bg="#2b2d31",fg="white",
borderwidth=0,command=save_chat)

save_btn.pack(side=tk.RIGHT,padx=10)

# CHAT AREA

chat=scrolledtext.ScrolledText(window,
wrap=tk.WORD,
bg="#202123",
fg="white",
font=("Segoe UI",11),
borderwidth=0)

chat.pack(fill=tk.BOTH,expand=True,padx=10,pady=10)

chat.tag_config("user",foreground="#4ea1ff")
chat.tag_config("ai",foreground="#7CFC00")

def chat_insert(text,tag):

    chat.insert(tk.END,text,tag)
    chat.yview(tk.END)

# INPUT AREA

bottom=tk.Frame(window,bg="#202123")
bottom.pack(fill=tk.X,padx=10,pady=10)

entry=tk.Entry(bottom,
font=("Segoe UI",12),
bg="#2b2d31",
fg="white",
insertbackground="white",
borderwidth=0)

entry.pack(side=tk.LEFT,fill=tk.X,expand=True,ipady=8,padx=(0,10))

# SEND

def send():

    user=entry.get().lower()

    entry.delete(0,tk.END)

    if user.strip()=="":
        return

    chat_insert("You: "+user+"\n","user")

    response=get_response(user)

    type_reply(response)

    speak(response)

# TYPING EFFECT

def type_reply(text):

    chat.insert(tk.END,"AI: ","ai")

    for c in text:

        chat.insert(tk.END,c,"ai")

        chat.update()

        time.sleep(0.02)

    chat.insert(tk.END,"\n")

# SEND BUTTON

send_btn=tk.Button(bottom,
text="📩",
font=("Segoe UI",18),
bg="#4ea1ff",
fg="white",
borderwidth=0,
width=3,
command=send)

send_btn.pack(side=tk.LEFT)

# MICROPHONE

mic_btn=tk.Button(bottom,
text="🎤",
font=("Segoe UI",20),
bg="#444",
fg="white",
borderwidth=0,
width=3,
command=listen)

mic_btn.pack(side=tk.LEFT,padx=5)



import tkinter as tk
import datetime
import requests

root = tk.Tk()
root.title("RealNet AI")
root.geometry("800x500")
root.configure(bg="black")

# Background info label
info_label = tk.Label(
    root,
    font=("Arial", 14, "bold"),
    fg="cyan",
    bg="black"
)



# ENTER KEY

entry.bind("<Return>",lambda event: send())

window.mainloop()