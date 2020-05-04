#### This manual is for those who would like to use their own host environment instead of the virtual machine. <br/>It also contains tutorials of the two main libraries you will use.
<br/>

## Installation
 ---
1. Make sure you've installed [Python 3.8](https://www.python.org/)
2. Clone this repository.
3. Open a terminal (_PowerShell if you're on Windows, ordinary terminal if on Linux/Ubuntu etc._)
4. Enter the following commands into the terminal one by one
    ```
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py
    pip install -r requirements.txt
    ```

## Usage
 ---
In PowerShell, you should be able to run the files using the command "_py_", like this: `py .\numpytest.py`.
Try this for _numpytest_ as well to make sure it works.
Unfortunately there won't be a tutorial for plotly, because it would give away too much(_yes, it's that easy_). 

## Git
 ---
If you're unsure of how you should be using Git, the basic procedure you will be using mostly is the following:
```
git pull origin master
git add .
git commit -m "some commit message here"
git push origin master
```
If `git push origin master` does not work, try `git push`. Same goes for `git pull`.
You will not need more branches than that for the purposes of this assignment.
If you have merge conflicts, you will see this marked in your code with something like this:

![](https://code.visualstudio.com/assets/docs/editor/versioncontrol/merge-conflict.png?raw=true)

The conflict is marked with "_<<<<_" and "_>>>>_" respectively. This means that you have to remove either the bottom half(below the "_\=\=\=\=\=\=_"), or the upper half(above the "_\=\=\=\=\=\=_"), then save the file. Also remove the markers. Or if you have a fancy-schmancy editor/IDE like the one in the image, you can just click "Accept Current Change" or "Accept Incoming Change".
You then repeat the procedure above with add, but without pull, then you commit and push again.
For more detailed information, see [this reference](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/resolving-a-merge-conflict-using-the-command-line).

If this was helpful, consider clicking this thing to show support for the Windows master race:
![](star.png?raw=true)
