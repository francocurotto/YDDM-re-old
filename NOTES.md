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
After that we can go with the player object, the dice pool, 
and the "dice hand" (maybe change name).

# 2020-12-30
Finish tests if ddm-dice object. Of course, the object will
continue to have new functionalities as the game development
progress. 

Now the next steps is a little bit more funny: player, 
dice pool and dice hand (for now is dice hand). The real fun 
will start when we start to program the dungeon place.

# 2021-01-01
Happy new year! I finished my implementation of the dice hand 
but I haven't test it yet. I think is better to switch into
making the real ddm database just so I don't have to make up
many fake dice for the test. It won't include special 
abilities for now just because it is to difficult and to 
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

# 2021-01-06
I thought it a lot and I think it is a good idea to implement
actual summon (monsters and items) before the dungeon board.
I decided to do some renaming because summon make more sense
as the actual piece that is in the game rather that the 
information that is in the ddm dice. For that information,
I decided to rename the class Card, as the card with all the
information that will be summoned. Since this is a little bit
scary, I created a new branch.

# 2021-01-14
Al lot of progress. I implemented the cards and merge it to 
master, now I'm making the player_test script. When finish a
simple game of who can summon more will be tested. I'm almost 
done. After that I plan to do 2 things: implement monsters 
that can fight each other, using the corresponding crests of
attack and defense, and so a more sophisticated game state 
logic to track the state of the game, that will be the 
skeleton of the actual game. Also a command class that parse 
generic user text commands. With that we'll actually have a
funny little game.

# 2021-01-21
I've got really delayed with the test_player script, mainly
because I refactored dice_pool and player so that it is
player that handles used dice and dimensioned dice (make 
more sense). Now I'm really almost ready. The game is 
actually functional, it's just that I have to transfer 
functionalities from test_player to player, in order to make
test scripts as simple as possible. Aside of the next steps
mentioned on 2021-01-14, I want to also add a Dungeon Master
so you can actually attack it and win the game in the same 
way as the actual YDDM game. That is a lot of work, I must
be sure to implement in progressively. I think I should start 
with the game states and reimplement test_player.

# 2021-01-22
Finally done with test player. Now to the next, the roadmap
is something like this:
- implement states and command_prompt and commands
- reimplement test_player (as test_player2)
- implement attacks
- implement dungeon master
- implement the basic game (without the dungeon yet)
Why I'm doing this list here? I should paste it in the TODO
file.

# 2021-01-27
Forgot to mention but in 2021-01-25 I finish the
implementation of the commands and command prompt, and
refactor test player in order to use game states (roll_state,
summon_state). Now I'm implementing attacks, but I realized
that I need to implement a summon_set, similar to dice_set,
in order to easily select monsters from the already summoned.
This means that most likely I will have to refactor dice_set
and dice_library, and do some regresion test commenting some
of my progress of today.

# 2021-02-01
Finish the implementation of summon_set as wel as the 
refactor previously mentioned. Now hoping to finish the 
attack logic soon. For now I will implement the GBA game 
rules for attacks (use of type advantages and retaliation 
damage for attacking defending monsters), but in the furute 
one should be able to modifiy these rules (in this case, 
disable them). Not sure how I'll implement it though.

# 2021-02-02
Minor modification. Now print_type is defined as a global 
variable, or game parameter.

# 2021-02-03
Finished attack state in a rush, but it will need 
considerable testing to remove all the eventual errors. I'll 
report when that is done.
