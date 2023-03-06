# HW2 Questions
## UMBC CMSC 471 02 spring 2023

Please answer the following questions using the git [markdown syntax](https://guides.github.com/features/mastering-markdown/).  You should view this file on your repo on GitHub after pushing it to make sure it looks the way you want.  You can also use a browser extension (like [this one](https://chrome.google.com/webstore/detail/markdown-preview-plus/febilkbfcbhebfnokafefeacimjdckgl) for Chrome) to view your local file.

### (1) Describe in words the heuristic you used for the **steps cost** and explain why it is admissable

... My Heuristic for Steps cost is based on the amount of different letters between goal and the current state. This is admissable because it will always be either equal to the total amount of steps in best case or lower if it takes more than one word change to get a letter to the correct position. ...

### (2) Describe in words the heuristic you used for the **scrabble cost** and explain why it is admissable

... My Heuristic for steps cost is the Steps Cost heuristic but with different counts based on the weight of each word. It would also be admissiable because it only estimates to the extent of the missing letters and their values. This would indicate it to underestimate in the case where more letters or higher value letters are needed to complete the puzzle.   ...

### (3) Describe in words the heuristic you used for the **frequency cost** and explain why it is admissable

... My frequency cost heuristic is the number of different characters between the current and goal state and the goal's frequency value. This will always underestimate the cost because it would calculate the previously admissable steps cost heuristic which finds the lowest cost estimate for changing letters. This is added to the frequency cost of goal which is less or equal than the costs of the words that it would take to get to the goal....

### (4) Given an initial word W1 and goal word W2, if there is a shortest path with N steps from W1 to W2, will there also be a shortest path of N steps from W2 to W1?  Explain why or why not.

... Yes, the words used to create the shortest path of N steps from word 1 to word 2 can be used in reverse to get from word 2 to word 1 in N steps. ...

### (5) Using the steps cost, what is the longest path for a pair of three- and four-letter words you found?

... For Four letter words, I found a long path of Oxer to Chiz which cost 9. For Three Letter words, I found a long path of urb to kex which took 6...
