import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')
from pyswip import Prolog
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

fd = open("facts.pl", 'w')

print("Hello!! This is an Elective advisory system.")
print()
print("You need to answer a few questions to help us in assisting you better.")
print("This system will suggest you the courses and electives you can take after you have completed semester 4. Before that all the courses are mandatory, so excel in them as they are important pre-requisites.")
print()
print("Please tell if you have completed the 4th semester or not.")
after_sem_4 = input()
ps = PorterStemmer()
# wnl = WordNetLemmatizer()
ansch = word_tokenize(after_sem_4)
ans_list = []
for i in ansch:
    ans_list.append(ps.stem(i))

if 'ye' in ans_list:
    after_sem_4 = 'yes'
elif 'no' in ans_list:
    print("Mandatory courses are need to be fulfilled. Take electives after completing semester 4.")
    after_sem_4 = 'no'
    exit()

def lemm_in(inp):
    pos = PorterStemmer()
    tokens = word_tokenize(inp)
    lemm_list = []
    for i in tokens:
        lemm_list.append(pos.stem(i))
    return lemm_list

# taking inputs for interest
print("From the below suggestions, choose your interest.")
print("1. Machine Learning")
print("2. Information Security")
print("3. Designing")
print("4. Electronics")
print("5. Economics")
print("6. Artificial Intelligence")
interest = input("State your interest: ")
print()
inr_list = lemm_in(interest)
interest = []
dic_in = {'ml':'Machine Learning', 'is':'Information Security', 'des':'Designing', 'ele':'Electronics', 'eco':'Economics', 'ai':'Artificial Intelligence', 'psy':'Psychology', 'cb':'Computational Biology'}

if 'machin' in inr_list:
    if 'learn' in inr_list:
        interest.append('ml')

if 'inform' in inr_list:
    if 'secur' in inr_list:
        interest.append('is')

if 'design' in inr_list:
    interest.append('des')

if 'electron' in inr_list:
    interest.append('ele')

if 'econom' in inr_list:
    interest.append('eco')

if 'artifici' in inr_list:
    if 'intellig' in inr_list:
        interest.append('ai')

if 'psycholog' in inr_list:
    interest.append('psy')

if 'comput' in inr_list:
    if 'biolog' in inr_list:
        interest.append('cb')

print("So, you have an interest in",end = " ")
for i in interest:
    print( "{}".format(dic_in[i]),end = ", ")

print("and this is great.")
print("This field has a lot of career paths. Here are some of them which are suitable for you: -")

for i in interest:
    if i == 'ml':
        print("For interest in machine learning: -")
        print("1. Research      2. Data Analyst     3. ML-Engineer      4. NLP-Scientist")
        print()
        print("Are you interested in pursuing any of the above career paths?")
        career = input()
        print()
        car_list = lemm_in(career)
        if 'ye' or 'research' or 'data' or 'ml' or 'nlp' in car_list:
            fd.write("elective('ML',1).\n")

    if i == 'is':
        print("For interest in information security: -")
        print("1. Network Analyst      2. Information Security Manager")
        print()
        print("Are you interested in pursuing any of the above career paths?")
        career = input()
        print()
        car_list = lemm_in(career)
        if 'ye' or 'network' or 'analyst' or 'inform' or 'secur' in car_list:
            fd.write("elective('IS',1).\n")

    if i == 'des':
        print("For interest in designing: -")
        print("1. Graphic Designer     2. Animations        3. Filming      4. Game Developer")
        print()
        print("Are you interested in pursuing any of the above career paths?")
        career = input()
        print()
        car_list = lemm_in(career)
        if 'ye' or 'graphic' or 'design' or 'anim' or 'film' or 'game' or 'develop' in car_list:
            fd.write("elective('Design',1).\n")

    if i == 'ele':
        print("For interest in electronics: -")
        print("1. Electrical Engineer   2. Iot Engineer")
        print()
        print("Are you interested in pursuing any of the above career paths?")
        career = input()
        print()
        car_list = lemm_in(career)
        if 'ye' or 'electr' or 'iot' in car_list:
            fd.write("elective('Electric',1).\n")

    if i == 'eco':
        print("For interest in economics: -")
        print("1. Trading   2. Finance Consultant       3. Bank Management")
        print()
        print("Are you interested in pursuing any of the above career paths?")
        career = input()
        print()
        car_list = lemm_in(career)
        if 'ye' or 'trade' or 'financ' or 'bank' in car_list:
            fd.write("elective('Eco',1).\n")

    if i == 'ai':
        print("For interest in artificial intelligence: -")
        print("1. Robotics Engineer  2. AI Data Analyst       3. AI Engineer")
        print()
        print("Are you interested in pursuing any of the above career paths?")
        career = input()
        print()
        car_list = lemm_in(career)
        if 'ye' or 'robot' or 'ai' or 'data' in car_list:
            fd.write("elective('AI',1).\n")

fd.close()

print('\n*****************************************************')
print("Here is the list of Electives as per your choices")
print('*****************************************************')

# collaborating assignment-1 prolog elective advisory system
swipl = Prolog()
swipl.consult("newfile.pl")
suggestions = list(swipl.query("induced_facts(X)"))
print(suggestions)











