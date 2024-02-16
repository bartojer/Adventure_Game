'''
3 Level Adventure Game

Jeremy Barton
CSC 110
'''
'''how about now?'''
# - - - - - - - - - - - #
# LEVEL 1
choice_1_dialog = '''You wake up in a dimly lit room with your hands bound. 
You are cold and hungry, and feel a rising need to escape.
Do you go out the open [WINDOW] or the unlocked [DOOR]?'''

# - - LEVEL 2 - - #

# window
choice_2a_dialog = '''You fall to the ground. 
Once your eyes adjust, you see that you are on the edge of a great orchard.
Realizing your great hunger, you begin to ravenously eat the fruit of these trees.
An old sounding voice calls out to you, but in your frenzy you don't make out what it said.
Do you [CALL] back, [HIDE], or [RUN]?
'''
else_2 = 'You are frozen in place, and the crazy old man cuts you down in his rage.'
# alt: eat the fruit, but don't taste anything.
# door
choice_2b_dialog = '''On your way out, you find a flashlight and a knife, and cut the rope from your wrists.
It is dark outside and you stumble down the front steps.
There is a small scrape on one arm, but you are otherwise unharmed.
After a moment, you can make out a pathway through a forest.
Do you continue with your flashlight [ON] or [OFF]?
'''
else_3 = '''Determining that you don't need a flashlight, you continue in the darkness'''
# - - LEVEL 3 - - #

# window - call
choice_3a_dialog = '''"Hey! Who goes there?" - old voice
"I mean no harm, I'm just trying to get home!"
"Well you're eating all my fruit dang it" - old voice
"I'm sorry, I'll stop right away"
As the voice comes closer, you see an old man stalking toward you, carrying an axe.
Do you [RUN] or [TRY] to talk him down?:
'''
else_4 = 'He comes closer and takes pity on your pathetic form. A few minutes later he sends you away with a basket of fruit.'
# window - hide
choice_3b_dialog = '''He comes lumbering toward you, searching for the phantom thief.
He gets close and you know it's too late. Do you [RUN] or [FIGHT]?
'''
else_5 = 'Somehow he never finds you. After a tense 5 minutes, he leaves, grumbling as he walks.'
# window - run (potential lore - you eventually find a path through trees. You don't tire, and feel a little funny. You can't find your voice. Something is happening. It's all coming back to you. You see yourself - but it's the real you. you aren't yourself...
choice_3c_dialog = '''He races after you, warning you to stop.
Your breath grows ragged as you barely stay ahead of him. 
Suddenly you stumble and lose consciousness.
You wake in the still dark forest, feeling perfectly fine. Finding a well worn path, you begin to walk down it. 
You spy a small building in the distance. Do you go [TOWARD] it or [AWAY] from it?
'''
else_6 = 'You are suddenly carried away by giant eagles to a land of terf and electric vehicles. You are very happy.'
# door - on
choice_3d_dialog = '''Walking down the path, you see someone who looks eerily familiar. 
As (s)he comes closer, you realize why - they are identical to you!
Do you [SPEAK] or [FIGHT]?:
'''
else_6 = '(S)he speaks in a robotic voice, asking you what is going on. (S)he is very confused. Together, you find your way out of the forest and vow to get to the bottom of it.'
# door - off
choice_3e_dialog = '''You see someone walking toward the building and hide behind a tree.
You feel a eeriness and decide not to say anything.
Do you [SNEAK] away or [SLAY] the foe?
'''
else_7 = '''You are stunned as a giant eagle comes down from the sky and carries the figure away. 
You walk away in disbelief, eventually finding your way back to your nice warm bed.'''

# - - AFTERMATH - - #

# window - call - run
end_1 = '''He continues to chase you, but you are faster and manage to get away.'''

#window - call - try
end_2 = '''You manage to talk him down and offer a day's labor in exchange for the fruit. You become friends and visit each other from time to time.'''

# window - hide - run
end_3 = '''You manage to slip into the dark night, the old voice disappearing behind you.'''

# window - hide - fight
end_4 = '''He swings for you. You dodge, laying him low with a blow to the gut.
After cutting the rope from your wrists you stand above him, holding his own axe. 
Just before finishing the old tyrant, your blood cools and you have a change of heart, sparing his life.'''

# window - run - toward
end_5 = '''You see a figure walking toward you. You recognize it and begin to feel funny.
As the figure draws near, you realize that they are you - you are not'''

# window - run - away
end_6 = '''After a few hours walking the path, you find a nearby city.
A few days later you find your way home.'''

# door - on - speak
end_7 = '''You ask him/her who (s)he is.
After a moment, (s)he speaks in your own voice.
"Finally, the last piece."
They are the last words you ever hear...'''

# door - on - fight
end_8 = '''You take out your knife and lunge for the neck, only to have your enemy swat it out of your hand, breaking your wrist.
After struggling for a few horrifying moments, you are on the ground, being dragged
by hands that are to strong to be human.

You wake up in a bed you almost recognize, go to a job you nearly remember, 
and come home to a family who's names you hardly know.
You live an entirely ordinary life, never to remember that night.'''

# door - off - sneak
end_9 = '''You find your way back to civilization, trying to forget it ever happened
Sometimes you still feel prickling sensation that you are being watched...'''

# door - off - slay
end_10 = '''You take out your knife and bury it 3 times in your enemy's guy, catching him/her by surprise.
You hear a crack as your knife cuts through something that's not quite flesh.
A few blows later, you stand above your fallen enemy. (S)he never made a sound as (s)he died.
As you look closer at what you have done, you find wires where there should be blood.

You are never bothered again, except by the haunting nightmares.'''

print(choice_1_dialog)
choice_1 = input('> ').lower()

if choice_1.lower() == 'window':
    print(choice_2a_dialog)
elif choice_1.lower() == 'door':
    print(choice_2b_dialog)
else:
    print("You couldn't make up your mind and are fed to the volcano gods. Game Over")

print('does this work?')