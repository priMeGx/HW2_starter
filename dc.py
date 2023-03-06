            

""" starter file for hw2: dogcat """

import search       # AIMA module for search problems
import gzip         # read from a gzip'd file

# file name for the dictionary, with one word per line.  Each line
# will have a word followed by a tab followed by a number, e.g.
#   and     0.07358445
#   for     0.18200336

#REMEMBER TO CHANGE THIS BACK TO .txt.gz!
dict_file = "words34.txt"

# dictionary is a dict to hold legal 3 and 4 letter words with their
# frequencies based on a sample of a large text corpus. The dict's
# keys are the words and its values are their frequencies

# load words into the dictionary dict
dictionary = {}
for line in gzip.open(dict_file, 'rt'):
#for line in open(dict_file, 'rt'):
    word, n = line.strip().split('\t')
    n = float(n)
    dictionary[word] = n

class DC(search.Problem):
    """DC is a subclass of the AIMA search files's Problem class. Its init
       method takes three arguments: the initial word, goal word, and cost method.
       A state is represented as a lowercase string of three or four
       ascii characters.  Both the initial and goal states must be
       words of the same length and they must be in the dict
       dictionary. The cost argument specifies how to measure the
       cost of an action and can be 'steps', 'scrabble' or 'frequency'
       """

    def __init__(self, initial='dog', goal='cat', cost='steps'):
        initialInList = False
        goalInList = False
        passed = True
        # make sure arguments are legal, raising an error if any are bad.
        if (len(initial) != 3 and len(initial) != 4):
            print("The initial word is not the right length (3 or 4)!")
            passed = False
        if (len(goal) != 3 and len(goal) != 4):
            print("The goal word is not the right length (3 or 4)!")
            passed = False
        if (len(goal) != len(initial)):
            print("The words are of different lengths!")
            passed = False
        if (cost != "steps" and cost != "scrabble" and cost != "frequency"):
                print("The cost could not be intepreted (steps, scrabble, or frequency.")
                passed = False;
        if (passed):
            for word in dictionary:
                if (word == initial):
                    initialInList = True
                if (word == goal):
                    goalInList = True
        # set instance attributes ...
        if (initialInList and goalInList):
            self.initial = initial;
            self.goal = goal;
            self.cost = cost;

    def actions(self, state):
        """ Given a state (i.e., a word), return a list or iterator of
        all possible next actions.  An action is defined by position
        in the word and a character to put in that position.  But the
        result must be a legal word, i.e., in our dictionary, and it
        should not be the same as the state, i.e., don't replace a
        character with the same character """
        
        nextOptions = {}
        iterator_next = iter(state)
        for wordIndex in range(0, len(state)):
            for letterIndex in range(0,26):
                newWord = state;
                newWord = newWord[:wordIndex] + chr(letterIndex + 97) + newWord[wordIndex+1:]
                if newWord in dictionary and newWord != state:
                    nextOptions[newWord] = dictionary[newWord]
        return nextOptions

    def result(self, state, action):
        """ takes a state and an action and returns a new state """
        return action

    def goal_test(self, state):
        """ returns True if state is a goal state for this problem instance """
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal

    def path_cost(self, c, state1, action, state2):
        """ Returns the cost to get to state2 by applying action in
        state1 given that c is the cost to get from the state state to
        state1. For the the dc problem, you will have to check what
        cost metric (self.cost) is being used for this problem instance,
        i.e., is it steps, scrabble or frequency """
        wordsDiff = False;
        for index in range(0, len(state1)):
            if (state1[index] != state2[index]):
                wordsDiff = True
        if not wordsDiff:
            return 0
        if (self.cost == 'steps'):
            #print("It's steps!")
            return c + 1
        elif (self.cost == 'scrabble'):
            for index in range(0, len(state1)):
                if (state1[index] != state2[index]):
                    if (state2[index] in {'a','e','i','o','u','r','s','t','l','n'}):
                        return c + 1
                    elif (state2[index] in {'d', 'g'}):
                        return c + 2
                    elif (state2[index] in {'b','c','m','p'}):
                        return c + 3
                    elif (state2[index] in {'f','h','v','w','y'}):
                        return c + 4
                    elif (state2[index] in {'k'}):
                        return c + 5
                    elif (state2[index] in {'j','x'}):
                        return c + 6
                    elif (state2[index] in {'z','q'}):
                        return c + 10
                    
        elif (self.cost == 'frequency'):
            #print("It's frequency!")
            return c + 1 + dictionary[action]
        

    def __repr__(self):
        """" return a suitable string to represent this problem instance """
        return f"dc({self.initial},{self.goal},{self.cost}"
        #Print out the list? Example does it with spaces instead of line break

    def h(self, node):
        """Heuristic: returns an estimate of the cost to get from the
        state of this node to the goal state. The heuristic's value should
        depend on the Problem's cost parameter, self.cost (i.e., steps, scrabble
        or frequency), as this will effect the estimate cost to get to
        the nearest goal. """
        if (self.cost == 'steps'):
            #print("It's steps! in H")
            diffCount = 0;
            for index in range(len(self.goal)):
                if(node.state[index] != self.goal[index]):
                    diffCount += 1;
            return diffCount;
        elif (self.cost == 'scrabble'):
            #print("It's scrabble! in H")
            diffCount = 0;
            for index in range(len(self.goal)):
                if(node.state[index] != self.goal[index]):
                    if (self.goal[index] in {'a','e','i','o','u','r','s','t','l','n',}):
                        diffCount += 1
                    elif (self.goal[index] in {'d', 'g'}):
                        diffCount += 2
                    elif (self.goal[index] in {'b','c','m','p'}):
                        diffCount += 3
                    elif (self.goal[index] in {'f','h','v','w','y'}):
                        diffCount += 4
                    elif (self.goal[index] in {'k'}):
                        diffCount += 5
                    elif (self.goal[index] in {'j','x'}):
                        diffCount += 6
                    elif (self.goal[index] in {'z','q'}):
                        diffCount += 10    
            return diffCount
        elif (self.cost == 'frequency'):
            diffCount = 0;
            for index in range(len(self.goal)):
                if(node.state[index] != self.goal[index]):
                    diffCount += 1;
            return diffCount + dictionary[self.goal]
