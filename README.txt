

----------------------------------------------------------------------------------------------------------------------------------------------------------------
Title: Analyzing the Efficacy of Various Agents at Solving Connect4
Name: Hunter Contos
Course: CPSC 474 - Computational Intelligence for Games

Overview:
For my final project I implemented three agents for solving Connect4: Monte-Carlo Tree Search, Minimax with Alpha-Beta Pruning, and Random Algorithms. Connect4
is a game where players take turns dropping discs into a 6x7 grid in an attempt to connect four in a row, either vertically, horizontally, or diagonally. For my
results, winning percents are reported in terms of player 1. For example if player 1 is MCTS and player 2 is Random and the win percent is 100%, that means
MCTS beat random play 100% of the time when it went first. On the other hand, if player 1 is Random and player 2 is MCTS and the win percent is 0% that means 
random beat MCTS going first 0% of the time. This allows us to look at how all algorithms do going first and second. All tests are run with 10% random play and 
100 times. The algorithm I focused on primarily was MCTS as I felt it would do a stronger job of solving Connect4, and Minimax was developed as a means of 
testing MCTS.

Results:                                        Player 1: (Win-Rate)

            |-------------------------------------------------------------------------------------------|
            |   Game   |      MCTS      |       Minimax w/ Alpha Beta        |          Random          |
            | ----------------------------------------------------------------------------------------- |
            |   MCTS   |     0.545      |              0.22                  |          0.01            |
            | ----------------------------------------------------------------------------------------- |
Player 2    |  Minimax |     0.960      |              0.87                  |          0.08            |
            | ----------------------------------------------------------------------------------------- |
            |  Random  |      1.0       |              0.98                  |          0.58            |
            | ----------------------------------------------------------------------------------------- |

How to run the code:
Make the executable test file, run make Test

The most interesting scripts that take ~15 mins to run are as follows:
./Test 100 0 1 3 3 75 - MCTS vs Random, 0% random play - MCTS should win ~100% of the time!
./Test 100 0 2 3 5 75 - Minimax vs Random, 0% random play - Minimax should win ~97% of the time!
./Test 100 0.1 2 1 3 75 - Minimax vs MCTS, 10% random play - MCTS should win ~80% of the time!

If you want to run all 9 results, they can be run by running the bash script:
./test.sh

The test scripts in it are as follows for all of the above results:
./Test 100 0.1 3 3 3 75
./Test 100 0.1 1 1 3 75
./Test 100 0.1 1 2 3 75
./Test 100 0.1 2 1 3 75
./Test 100 0.1 1 3 3 75
./Test 100 0.1 3 1 3 75
./Test 100 0.1 2 2 3 75
./Test 100 0.1 2 3 3 75
./Test 100 0.1 3 2 3 75

If having trouble making, you should also be able to run
python3 test_strategies.py 100 0.1 3 3 3 75
python3 test_strategies.py 100 0.1 1 1 3 75
python3 test_strategies.py 100 0.1 1 2 3 75
python3 test_strategies.py 100 0.1 2 1 3 75
python3 test_strategies.py 100 0.1 1 3 3 75
python3 test_strategies.py 100 0.1 3 1 3 75
python3 test_strategies.py 100 0.1 2 2 3 75
python3 test_strategies.py 100 0.1 2 3 3 75
python3 test_strategies.py 100 0.1 3 2 3 75

Individual test cases can be run in the following format:
./test_strategies.py number_of_games, percent_random_play, strategy_for_p1, strategy_for_p2, depth, MCTS
Where strategies are 1 = MCTS, 2 = Minimax with Alpha-Beta Pruning, 3 = Random Play, and 4 = Player_Input

An example of a call to run is :
./Test 100 0.1 1 2 3 75
Which will play MCTS with 75 iterations as player 1 against Minimax to a depth of 3 as player 2 for a total of 100 games with 10% of moves random

Analysis of Results:
Overall, both MCTS and Minimax yielded very strong results, with MCTS beating random play ~100% of the time and Minimax winning against random ~95% 
of the time! However, when MCTS is run against Minimax, we see that MCTS performs significantly stronger. This makes sense as I spent a majority of my
time working on implementing the MCTS algorithm in addition to the regular gameplay for Connect4. Because the game plays randomly 10% of the time, MCTS
did lose a game while going as player 2 - however, without random play, it consistantly won every time. Similarly, Minimax against random with no random moves
did slightly better ~98% win rate.

Taking the Results Further:
Overall, as mentioned above when MCTS is put up against Minimax, MCTS is much stronger. This is a reflection of the amount of time I put into MCTS
as opposed to Minimax. For further work, the Minimax heuristic can without a doubt be improved. I focused primarily on 2 in a rows and 3 in a rows, 
however, including things in the heuristic such as location on the board and incentive blocking opponent moves can both undoubtedly improve results.
Additionally, it turns out that minimax's success hinged very much on getting the middle move as evidenced by its low win-rate when MCTS moves first. 
Coming up with a heuristic that is less depednent on this would undoubtedly help significantly as many times MCTS would simply take the middle 3 on the
bottom row and make it so that there is a double win move. The current heuristic with minimax focuses much better on the end game, hence MCTS's strong play
early in the game gives it an advantage that is almost impossible for minimax to overcome.

Reflection: Overall, I greatly enjoyed this project as it allowed me to implement a game and its rules for the first time and use some of the techniques
I learned in class to solve it. There were some difficulties forgetting to deepcopy as opposed to shallow copy with python, however, aside from that, the project
went relatively smoothly. Overall, I greatly enjoyed this class and learned alot.
----------------------------------------------------------------------------------------------------------------------------------------------------------------

