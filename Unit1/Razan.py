#ask the user for their name
print("There's been a murder! We need your help, detective… wait, sorry-")
name = input("What's your name? ")
final_name = name.lower().capitalize()
print("Right, yes! We need your help, Detective", final_name + "!")

#present the case to user
print('''
Now, the murder took place in the Cunningham mansion, owned by Samuel Cunningham. Police observed that the murder victim, Ernest Cunningham, appears to have been stabbed in the back.

Police also shared that there are six possible suspects: Dexter Cunningham (the victim's son), Pippa Cunningham (the victim's daughter), Audrey Parker (the victim's mother), Naomi Watson (the maid), Sebastian Parker (the victim's step-father), and Samuel Cunningham (the victim's grandfather)
''')

#present user w first scenario and the choice (a, b, c)
choice1 = input("Are you going to a) inspect the body, b) interrogate the suspects, or c) investigate the mansion for clues? ")
answer1 = choice1.lower()

#output results of their first choice
if answer1 == "a":
  score1 = 1
  print('''
After a careful examination of the body, you've noticed a peculiar bruise on Ernest Cunningham's left arm. It appears to be a defensive wound, suggesting that he might have tried to fight off his attacker.
''')
elif answer1 == "b":
  score1 = 2
  print('''
After interrogating the suspects, you have learned the following information:
- Dexter said the family gathered up to celebrate Samuel's 78th birthday, and Samuel shared a private announcement
- Pippa insisted that no one would purposefully kill Ernest, and shared her theory that whoever killed him intended to kill Samuel instead
- Naomi reported that she observed Dexter and Ernest arguing the night before his murder (Pippa backed up this information, admitting that her brother and father never really got along)
- Sebastian disclosed that the possible motive for the murder was Samuel announcing that he adjusted his will, changing the heir of his wealth from Audrey to Ernest (When mentioned to Audrey, she froze up but claimed that she would never hurt her baby boy, no matter what)
- Samuel shared his concerns that Sebastian had a grudge against Ernest (Sebastian claimed that Ernest was like a son to him)
- Audrey offered that Dexter possibly killed his father in a rage, due to the recent divorce between Ernest and Erin (Dexter's mother)

However, while you were interrogating the suspects, the police decided to take Ernest's dead body back to the station. Despite your pleading, the police refused to share their notes on the investigation, claiming that if the body mattered so much you should've just done that first.
''')
else:
  score1 = 3
  print('''
 While searching through Samuel's study, you discover a hidden compartment behind a loose panel on the wall. Inside, you find a diary that contains cryptic entries about a financial fraud and a potential threat to Ernest's life.
  ''')