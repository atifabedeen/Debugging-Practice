# Debugging Practice in VSCode with Python

## The Debugging Console and Breakpoints

Video: [The Debugging Console and Breakpoints](https://drive.google.com/file/d/1GCUiaOjYhK3REEU1ywytY16y1EN99GFX/view?usp=sharing)

To start debugging, find the "Run & Debug" tab, or press cmd + shift + D.

The, click "Run & Debug" with the file you want to debug. Try this with the file `task0.py`.

The debugger will stop on exceptions and show you the values of the variables at the current step. For example, you can see that there's an exception where the value of `result` is not 120. 

You can see the values on the debugging console to the left. This console shows you the values of the variables, as well as the call stack, which are the functions currently in process. Here, `result` is 24.

The next step in debugging your program is to set a breakpoint. A breakpoint is a point in your code where the debugger will stop. Set a breakpoint on line 9.

To set a breakpoint, click in the left margin of the line you want to break at. This will create a red dot.

Now run your debugger again. You'll see that the debugger has stopped at your breakpoint. On the debugger console, you can see the values of the variables, as well as the call stack, at this step. Here, check that the value of `result` is 1, `i` is 1, and `n` is 5. The breakpoint helps you stop the program at precisely the right line, and you can then navigate through your code step by step. 

# Todo

- [ ] Topics (Videos)
  - [ ] What is a debugger + How to setup debugger
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
