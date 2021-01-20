Test:
	echo "#!/bin/bash" > Test
	echo "python3 test_strategies.py \"\$$@\"" >> Test
	chmod u+x Test

# MCTS:
# 	echo "#!/bin/bash" > MCTS
# 	echo "python3 mcts.py \"\$$@\"" >> MCTS
# 	chmod u+x MCTS
	
# Connect4:
# 	echo "#!/bin/bash" > Connect4
# 	echo "python3 Connect4.py \"\$$@\"" >> Connect4
# 	chmod u+x Connect4