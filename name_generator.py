#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Silly name generator and Pylint

import sys
import random

def name_generator():
    """Choose names at random from a pair of tuples and print to screen."""
    print('Welcome to the name generator')
    
    first = ('Baby Oil', 'Bad news', 'Big burps', "Bill 'Bennie-Weeine'", "Bob 'Stinkbug'",
            'Bowl Noises', 'Boxelder', "Bud 'Lite'", 'Butterbean', 'Buttermilk',
            'Buttocks', 'Chad', 'Chesterfield', 'Chewy', 'Chigger', 'Cinnabuns',
            'Cleet', 'Cornbread', 'Crabmeat', 'Figgs', 'Lil Debby', 'Oil-Can'
            'Rock Candy', 'Schlomo', 'Scut', 'Skidmarks', "Winston 'Jaz Hands'")
    
    last = ('Appleyard', 'Bigmeat', 'Boogerbottom', 'Butterbaugh', 'Clovenhoof',
           'Clutterbuck', 'Cocktoasten', 'Gooberdapple', 'Guster', 'Henderson',
           'Hooperbag', 'Goodpasture', 'Jefferson', 'Jensen', 'Kingfish', 'Listenbee',
           'McFadden', 'Moonshine', 'Noseworthy', 'overtuft', 'Overpeck', 'Pealike', 'Rainwater',
           'Pinkerton', 'Putney', 'Quakenbush', 'Sackrider', 'Stevens', 'Weiners', 'Woolysocks')
    
    while True:
        first_name = random.choice(first)
        las_name = random.choice(last)
        
        print(f'{firstname} {lastname}', file=sys.stderr)
        
        try_again= input(f"\nTry again? (Press Enter else 'n' to quit)\n")
        
        if try_again.lower() == 'n':
            break 
            
if __name__ == '__name_generator__':
    name_generator()


# In[ ]:




