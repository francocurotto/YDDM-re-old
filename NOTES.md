# 2020-12-24
Started coding the game. The idea is to start simple and just
with the dice object. At first everything will be just text
printed in the terminal.
 
# 2020-12-27
Finish dice object and test. Should consider in the future a
way to change the crest character at runtime. There is a bug
where pretty unicode characters overlap with other characters,
specifically sword and shield have this problem.

The next step is to implement the ddm-dice object and test it.
After that we can go with the player object, the dicepool, and
the "dice hand" (maybe change name).

# 2020-12-30
Finish tests if ddm-dice object. Of course, the object will
continue to have new funcionalities as the game development
progress. 

Now the next steps is a little bit more funny: player, 
dicepool and dicehand (for now is dice hand). The real fun 
will start when we start to program the dungeon place.

# 2021-01-01
Happy new year! I finished my implementation of the dice hand 
but I haven't test it yet. I think is better to switch into
making the real ddm database just so I don't have to make up
many fake dice for the test. It won't include special 
abilities for now just beacause it is to difficult and to 
early for that.

# 2021-01-05
A lot of progress. I implemented the original dice database,
extracted from Magirus on GameFAQs (https://gamefaqs.gamespot.com/gba/471247-yu-gi-oh-dungeon-dice-monsters/faqs).
Also tested dice hand and implemented and tested crest pool.

Now I'll implement+test player. For this tests I want to make
a little minigame, were two players try to summon as many 
monsters (or items) as possible with random dice pools. The
monsters doesn't really face each other so it doesn't make 
sense bot it will be the first time that the code starts 
looking kinda like a game. Actually, now that I think about it
maybe is a good idea if the monsters can actually fight 
::thinking face::
