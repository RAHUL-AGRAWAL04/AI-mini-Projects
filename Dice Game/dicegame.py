#cell 1
SKIP_GAME = True
if not SKIP_GAME:
    #%run dice_game.py
    import os.system as s
    s('python3 dice_game.py')
 
 
   
#cell2
from dice_game import DiceGame
import numpy as np

# setting a seed for the random number generator gives repeatable results, making testing easier!
np.random.seed(111)

game = DiceGame()
game.get_dice_state()



#Cell 3
reward, new_state, game_over = game.roll((0,))
print(reward)
print(new_state)
print(game_over)


#Cell 4
reward, new_state, game_over = game.roll((0, 1, 2))
print(reward)
print(new_state)
print(game_over)


#Cell 5
print(game.score)

#cell 6
game.reset()

#cell 7
game = DiceGame()
print(f"The first 5 of {len(game.states)} possible dice rolls are: {game.states[0:5]}")
print(f"The possible actions on any given turn are: {game.actions}")


#cell 8
game = DiceGame()
states, game_over, reward, probabilities = game.get_next_states((0,), (2, 3, 4))
for state, probability in zip(states, probabilities):
    print(f"Would get roll of {state} with probability {probability}")


#Cell 9
states, game_over, reward, probabilities = game.get_next_states((0, 1, 2), (2, 2, 5))
print(states)
print(game_over)
print(reward)



#Cell 10
from abc import ABC, abstractmethod


class DiceGameAgent(ABC):
    def __init__(self, game):
        self.game = game
    
    @abstractmethod
    def play(self, state):
        pass


class AlwaysHoldAgent(DiceGameAgent):
    def play(self, state):
        return (0, 1, 2)


class PerfectionistAgent(DiceGameAgent):
    def play(self, state):
        if state == (1, 1, 1) or state == (1, 1, 6):
            return (0, 1, 2)
        else:
            return ()
        
        
def play_game_with_agent(agent, game, verbose=False):
    state = game.reset()
    
    if(verbose): print(f"Testing agent: \n\t{type(agent).__name__}")
    if(verbose): print(f"Starting dice: \n\t{state}\n")
    
    game_over = False
    actions = 0
    while not game_over:
        action = agent.play(state)
        actions += 1
        
        if(verbose): print(f"Action {actions}: \t{action}")
        _, state, game_over = game.roll(action)
        if(verbose and not game_over): print(f"Dice: \t\t{state}")

    if(verbose): print(f"\nFinal dice: {state}, score: {game.score}")
        
    return game.score


if __name__ == "__main__":
    # random seed makes the results deterministic
    # change the number to see different results
    # or delete the line to make it change each time it is run
    np.random.seed(1)
    
    game = DiceGame()
    
    agent1 = AlwaysHoldAgent(game)
    play_game_with_agent(agent1, game, verbose=True)
    
    print("\n")
    
    agent2 = PerfectionistAgent(game)
    play_game_with_agent(agent2, game, verbose=True)
    
    

















    
#Cell 11
class MyAgent(DiceGameAgent):
    def __init__(self, game):
        """
        if your code does any pre-processing on the game, you can do it here
        e.g. you could do the  here once, store the policy, 
        and then use it in the play method
        you can always access the game with self.game
        """
        
        # this calls the superclass constructor (does self.game = game)
        super().__init__(game) 
        
        # YOUR CODE HERE
        
        #Value Iteration Algorithm
        self.theta = 0.0009
        self.gamma = 0.969
        self.value_map = {}
        self.policy = {}
        
        for state in self.game.states:
            self.value_map[state] = game.final_score(state)

        self.saved_data = {}

        delta = self.theta + 1
        while delta > self.theta:
            d = 0
            for state in self.game.states:
                current_best = -1000
                prev_best = self.value_map[state]
                for action in self.game.actions:
                    total_prob = self.total_probability(action, state)
                    if total_prob > current_best:
                        current_best = total_prob
                        optimal_action = action
                self.value_map[state] = current_best
                self.policy[state] = optimal_action
                d = max(d, abs(prev_best - current_best))

            delta = d
    
    def total_probability(self, action, state):
        # Get the values based on the action-states
        if (action, state) not in self.saved_data:
            self.saved_data[(action, state)] = self.game.get_next_states(action, state)

        output_states, game_over, reward, probabilities = self.saved_data.get((action, state))
        total_prob = 0 #state's total probablity.

        # Iterating over probabilities of each state state
        for output_state, probability in zip(output_states, probabilities):
            if not game_over:
                total_prob += probability * (reward + self.gamma * self.value_map.get(output_state))
            else:
                total_prob += probability * (reward + self.gamma * self.game.final_score(state))

        return total_prob
    
    def play(self, state):
        """
        given a state, return the chosen action for this state
        at minimum you must support the basic rules: three six-sided fair dice
        
        if you want to support more rules, use the values inside self.game, e.g.
            the input state will be one of self.game.states
            you must return one of self.game.actions
        
        read the code in dicegame.py to learn more
        """
        # YOUR CODE HERE
        
        return self.policy[state]













#Cell 12
SKIP_TESTS = False

if not SKIP_TESTS:
    import time

    total_score = 0
    total_time = 0
    n = 10

    np.random.seed()

    print("Testing basic rules.")
    print()

    game = DiceGame()

    start_time = time.process_time()
    test_agent = MyAgent(game)
    total_time += time.process_time() - start_time

    for i in range(n):
        start_time = time.process_time()
        score = play_game_with_agent(test_agent, game)
        total_time += time.process_time() - start_time

        print(f"Game {i} score: {score}")
        total_score += score

    print()
    print(f"Average score: {total_score/n}")
    print(f"Total time: {total_time:.4f} seconds")




#Cell 13
TEST_EXTENDED_RULES = True

if not SKIP_TESTS and TEST_EXTENDED_RULES:
    total_score = 0
    total_time = 0
    n = 10

    print("Testing extended rules – two three-sided dice.")
    print()

    game = DiceGame(dice=2, sides=3)

    start_time = time.process_time()
    test_agent = MyAgent(game)
    total_time += time.process_time() - start_time

    for i in range(n):
        start_time = time.process_time()
        score = play_game_with_agent(test_agent, game)
        total_time += time.process_time() - start_time

        print(f"Game {i} score: {score}")
        total_score += score

    print()
    print(f"Average score: {total_score/n}")
    print(f"Average time: {total_time/n:.5f} seconds")
























'''
#cell 14
import sys
import pathlib

fail = False;

if not SKIP_GAME:
    fail = True;
    print("You must set the SKIP_GAME constant to True in the earlier cell.")

if not SKIP_TESTS:
    fail = True;
    print("You must set the SKIP_TESTS constant to True in the earlier cell.")
    
p1 = pathlib.Path('./readme.txt')
p2 = pathlib.Path('./readme.md')
if not (p1.is_file() or p2.is_file()):
    fail = True;
    print("You must include a separate file called readme.txt or readme.md in your submission.")
    
p3 = pathlib.Path('./dicegame.ipynb')
if not p3.is_file():
    fail = True
    print("This notebook file must be named dicegame.ipynb")
    
if "MyAgent" not in dir():
    fail = True;
    print("You must include a class called MyAgent as defined above.")
else:    
    game = DiceGame()
    agent = MyAgent(game)
    action = agent.play((1, 1, 1))

    if action not in game.actions:
        print("Warning:")
        print("Your agent does not seem to produce a valid action with the default rules.")
        print()
        print("Your assignment is unlikely to get any marks from the autograder. While we will")
        print("try to check it manually to assign some partial credit, we encourage you to ask")
        print("for help on the forum or directly to a tutor.")
        print()
        print("Please use the readme file to explain your code anyway.")
        
    if TEST_EXTENDED_RULES:
        print("Info: TEST_EXTENDED_RULES is ON")
        game = DiceGame(dice=2, sides=8)
        agent = MyAgent(game)
        try:
            action = agent.play((7, 8))
        except:
            action = None

        if action not in game.actions:
            fail = True
            print("Your agent does not produce a valid action with the extended rules.")
            print("Turn off TEST_EXTENDED_RULES if you cannot fix this error.")
    else:
        print("Info: TEST_EXTENDED_RULES is OFF (extended rules will not be tested)")
    
if fail:
    print()
    sys.stderr.write("Your submission is not ready! Please read and follow the instructions above.")
else:
    print()
    print("All checks passed. When you are ready to submit, upload the notebook and readme file to the")
    print("assignment page, without changing any filenames.")
    print()
    print("If you need to submit multiple files, you can archive them in a .zip file. (No other format.)")        
    
'''
