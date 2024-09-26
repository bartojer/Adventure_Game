'''
Trial game
'''
import random

resource = ['Wheat', 'Sheep', ' Ore ', 'Brick', ' Wood']

r = (random.choice(resource))

r1 = (random.choice(resource))
r2 = (random.choice(resource))
r3 = (random.choice(resource))
r4 = (random.choice(resource))
r5 = (random.choice(resource))
r6 = (random.choice(resource))
r7 = (random.choice(resource))
r8 = (random.choice(resource))
r9 = (random.choice(resource))
r10 = (random.choice(resource))
r11 = (random.choice(resource))
r12 = (random.choice(resource))
r13 = (random.choice(resource))
r14 = (random.choice(resource))
r15 = (random.choice(resource))
r16 = (random.choice(resource))
r17 = (random.choice(resource))
r18 = (random.choice(resource))
r19 = (random.choice(resource))




# Create a list of variables named p1 to p19 and assign them random values between 1 and 6
for i in range(1, 20):
  globals()[f"p{i}"] = random.randint(1, 6) + random.randint(1, 6)


print(f'''
       _____________________________
     /    {r1 }    {r2 }       {r3 }    
    /      {p1 }   (1)   {p2 }    (2)    {p3 }
   /  {r4}    {r5}    {r6}    {r7}
  /     {p4}  (3)   {p5}  (4)   {p6}  (5)   {p7}
 /{r8 }    {r9 }    {r10}    {r11}    {r12}  
   {p8}  (6)   {p9}  (7)   {p10}  (8)   {p11}  (9)    {p12} 
     {r13}    {r14}    {r15}    {r16}      
       {p13}  (10)  {p14}  (11)  {p15}  (12)  {p16}      
          {r17}    {r18}    {r19}       
            {p17}        {p18}       {p19}         /
      _________________________________/
''')

player_1_1 = input('Where do you place your first town? (1-12):')
player_2_1 = input('Where do you place your first town? (1-12):')

player_1_2 = input('Where do you place your second town? (1-12):')
player_2_2 = input('Where do you place your second town? (1-12):')

game = 'going'



while game == 'going':
  pass