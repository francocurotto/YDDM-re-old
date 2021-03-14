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
and dice_library, and do some regression test commenting some
of my progress of today.

# 2021-02-01
Finish the implementation of summon_set as well as the 
refactor previously mentioned. Now hoping to finish the 
attack logic soon. For now I will implement the GBA game 
rules for attacks (use of type advantages and retaliation 
damage for attacking defending monsters), but in the future 
one should be able to modify these rules (in this case, 
disable them). Not sure how I'll implement it though.

# 2021-02-02
Minor modification. Now print_type is defined as a global 
variable, or game parameter.

# 2021-02-03
Finished attack state in a rush, but it will need 
considerable testing to remove all the eventual errors. I'll 
report when that is done.

# 2021-02-10
FINALLY finished testing attack state. It got pretty polished
if you ask me. You can basically play a simple DDM game that
only involves summons, attacks and defenses, it is pretty 
simple but you can play! Before I move to implementing the 
dungeon (uff), I want to refactor the game_states (fuuun) so
that I completely separates the game logic with the inputs 
and outputs, that way it should be easy to replace the basic
command line interface with something like urwid (one day, 
hopefully).

# 2021-02-21
Oh my god. I had to do so much refactoring, and I basically 
had to do it twice, because I didn't like the first 
implementation, but I finally did it! Funnily enough the game 
looks exactly the same, buuut, I was able to separate logic 
and display, so in theory it should be easier to implement a
decent UI later. I'm very happy with the results for now, and
I only want to check for display errors like consecutive new
lines. But after that, the dungeon implementation starts.

# 2021-02-27
Start implementing the dungeon! And for now is looking pretty
good. I run a test for dimensioning dice nets and it works
like a charm. Next step: implement dungeon_state and 
integrate the dungeon into the duel. At first the dungeon 
will not serve any prupose but it will be good to see that
the players are dimensioning properly and the dungeon is 
displayed correctly.

After that I have to implement monster movement. I have no 
ideaaaa how I'll do it. I need to implement an algorithm that
computes the shortest path between two points in the dungeon
path, taking into account impossible cases and obstacles 
(opponent monsters, items, monster lords). I know that I'll
have to implement some type of well known shortest path 
algorithm, but I'm not sure which one will be the simplest to
do (Breadth-first search?). Also I don't remember if player's
own monsters count as obstacles or if monsters can move 
through them. I have to check that out. Maybe I'll have to
finally download and play the game again?? Hahah.

# 2021-02-28
Okay so I had to download the game and play it again to 
remember the movements mechanics, here is my summary:

- Normal monsters cannot move through other monsters (from 
same player or opponent). They cannot move through item also
but they can step into them to activate them.
- Tunnel monsters can move through other monsters (from same
player or opponent), but cannot move through items. Their 
movement crest cost is 1 per square.
- Flying monsters can move through others monsters and 
monsters can move through them, but cannot move through 
items. They can only be attacked by other flying monsters or
archer monsters. They can attack any monster though. Their 
movement crest is 2 per square.
- Warp vortex is a special item that summons a vortex, and
other monsters can move thourgh the vortex.

# 2021-03-01
To celebrate the start of the month, dungeon state 
implemented! Tried summoning dice and is looking pretty good.
Now it comes the hardest challenge yet, implement monster 
movement, and then proper attack at 1 square distance. I 
still have no idea how in the world I'm gonna implemented it.
This could be a good breaking point to work in minor changes
that I have listed in TODO. Anyways, really excited about how
the game is turning out, and also a little afraid on how I'll
continue.

Just thinking right now, maybe I could start simple and 
implement monster teleportation were I allow monster to move
whereever they want, and so I can test proper attack easier 
too. Good ideas!

# 2021-03-06
I have jsut finished testing teleport movement with 1 
movement crest cost, and proper attack between monsters at
correct range. All that is left is to implement proper 
movement and I'll have a proper game, that it will only be 
missing monster and items abilities. So close!

# 2021-03-09
OMG! The proper movement has been implemented. In the end, 
the only thing that I had to do is implement my version of
Breadth-first search, and it worked perfectly. Even I didn't
optimized it, it works really fast, it acuatally make sense, 
because the maximum path of the game are actually not that 
long. The game is just so fun. 

The next step is to implement a simple curses interface, just
so that you don't have to print the necessary information all
the time. It will still work with prompt commands though,
better controls are for future work.

# 2021-03-14
Impresingly enough, it didn't take too much to implement the
curses interface (it still requires some fixes, but very 
minor ones). It's acutally really simple and it leverages 
most of the work from the command prompt interface.In any 
case, it is still really imresive, and it is a joy to play.
It still lacks items/monsters abilities and you have to input
commands via text, but still, to looks like an acutal game!

The roadmap from now it should be to implement the abilities
and to implement a better interface qith urwid. However, at
this point I should think if I should do some promotion, I
was thinking to start simple with a short video in reddit,
and a simple explanation in the title. While I think about it
I'll fix the issues that I mentioned earlier.
