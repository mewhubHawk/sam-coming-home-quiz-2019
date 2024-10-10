score = 0
happy=[":)", ":D"]
sad=["):", "D:"]

import random

questions=\
  {
    "When's sam coming home":"today",
    "What today's date":"29th June 2019",
    "are you happy sam's coming home":"Yes"

    
    #add more Qs here
}

for question, answer in questions.items():
    response = input("%s?\n--->" % question)
    if response != answer:
        print(sad[random.randint(1,len(sad))])
    else:
        print(happy[random.randint(1,len(happy))]) 
        score += 1

print("You got %d out of %d!" % (score, len(questions)))

if score < len(questions)/3:
   print("better luck next time")
else:
 print("Well Done!")
