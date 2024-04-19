# Debugging Practice in VSCode with Python

## The Debugging Console and Breakpoints

Video: [The Debugging Console and Breakpoints](https://drive.google.com/file/d/1GCUiaOjYhK3REEU1ywytY16y1EN99GFX/view?usp=sharing)

To start debugging, find the "Run & Debug" tab, or press cmd + shift + D.

Then, click "Run & Debug" with the file you want to debug. Try this with the file `task0.py`.

The debugger will stop exceptions and show you the values of the variables at the current step. For example, you can see that there's an exception where the value of `result` is not 120. 

You can see the values on the debugging console to the left. This console shows you the values of the variables, as well as the call stack, which are the functions currently in process. Here, the `result` is 24.

The next step in debugging your program is to set a breakpoint. A breakpoint is a point in your code where the debugger will stop. Set a breakpoint on line 9.

To set a breakpoint, click in the left margin of the line you want to break at. This will create a red dot.

Now rerun your debugger. You'll see that the debugger has stopped at your breakpoint. On the debugger console, you can see the values of the variables, as well as the call stack, at this step. Here, check that the value of `result` is 1, `i` is 1, and `n` is 5. The breakpoint helps you stop the program at precisely the right line, and you can then navigate through your code step by step. 

## Navigating your code using the Debugger Controls
Video:

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/-tAK8EvjamE/0.jpg)](https://youtu.be/-tAK8EvjamE)

In this video, I review the important debugging controls available in VSCode. Specifically, Continue, Step Over, Step Into, Step Out, and Restart buttons. I then proceeded to use these tools to fix an error in the sample program called simple.py. (Code provided in this directory) 

Their basic functionalities are as follows: 

### Continue:
This helps you execute your code "normally" from your current breakpoint until you hit another one or if your program reaches the end and terminates. This is helpful in cases where you want to cycle through your breakpoints in your program quickly instead of stepping over every single line.

### Step Over:
By far the most important feature of the debugger. This button helps you navigate your program line by line. With the help of the debugger console, you can see how your different variables in the local memory are being affected and how they are being updated with every execution of a line. This is particularly helpful in narrowing down your search space for where you could be having potential problems or bugs. 

### Step Into:
This feature is helpful in lines of code where you have function calls. Instead of stepping over these function calls, you can step INTO these functions to further investigate and narrow your search space to finding the problem. This helps navigate nested function calls in complex programs. NOTE: You can only step into functions that are written and present in the file you are debugging. By default, you cannot step into functions and methods that are already provided by the Python libraries. If you would like to do so, then you would have to re-configure your launch.json file which is a tad bit complex so I would suggest you avoid doing it. In any case, there is no reason to debug functions and methods provided by the library as it is very unlikely that they would have any errors.

### Step Out:
The opposite of step into. You can step out of the function you are currently debugging at any moment and return to the location where the function was called.

### Restart:
Helps you restart the debugger from your first breakpoint if you think you messed up or need to debug again.

## TO-DO: DEBUGGING EXERCISE IN PYTHON
Now that you know how to use a debugger, [here is a 30-minute exercise](https://docs.google.com/document/d/19LYyjmFTa6E4lpxX-TTJ6gPrdu4rs0CPuxoHGVHuay0/edit?usp=sharing) that will help you practice and improve your skills in debugging while also improving your skills in code readability, problem-solving skills, and keeping you on top of important Python-specific concepts.
 
# Todo

- [ ] Topics (Videos)
  - [ ] What is a debugger + How to setup a debugger
  - [ ] Adding breakpoints
  - [ ] Debug Console (+ hover over variables)
  - [ ] Step through
  - [ ] Step into
  - [ ] Step back
  - [ ] Help explain call by ref vs call by value
- [ ] Create videos
- [ ] Add text
- [ ] Add exercise
  - [ ] Add tasks
  - [ ] Add solution
  - [ ] Add tests
- [ ] Develop code for the videos
