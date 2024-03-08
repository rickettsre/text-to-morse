# Day 82 - 100 DAYS OF PYTHON COURSE

===========================================================

# _Task_

Create a text-based Python program to convert Strings into Morse Code.

# Rough Notes

Create a virtual environment:

# Linux

mkdir my-code
cd my-code
python3 -m venv .venv
source .venv/bin/activate

.venv/bin/python3 -m pip install --upgrade pip

e.g. pip3 install requirements:

pip3 install jupyter pandas matplotlib plotly.express

python -m pip freeze > requirements.txt

# Windows

md my-code
cd my-code
py -3 -m venv .venv

.venv\Scripts\activate.bat
.venv\Scripts\python.exe -m pip install --upgrade pip
e.g. pip3 install requirements:

pip3 install jupyter pandas matplotlib plotly.express
python -m pip freeze > requirements.txt

1. Create a text base logo using an ascii art generator e.g. https://patorjk.com/software/taag/#p=display&v=1&f=Modular&t=Text2Morse

cat logo.py

logo = """

---

| || || |_| || || || |_| || || _ | | || |
|_ \_|| **_|| ||_ \_||\_\_** || || \_ || | || | **\_**|| **_|
| | | |_** | | | | \_**_| || || | | || |_||\_ | |\_\_\_** | |**_
| | | _**| | | | | | **\_\_**|| || |\_| || ** ||\_\_\_** || **_|
| | | |_** | \_ | | | | |**\_** | ||\_|| || || | | | **\_**| || |**_
|_**| |**\_\_\_**||**| |**| |**\_| |**\_\***\*||_| |_||**\_\_\_**||**_| |_||**\_\*\***||**\_\_\_**|

"""

cat ghost*logo.py
logo = """
.-') * ('-. ) (`-.      .-') _            _   .-')                _  .-')    .-')      ('-.
(  OO) )  _(  OO)  ( OO ).   (  OO) )          ( '.( OO )_             ( \( -O )  ( OO ).  _(  OO)
/     '._(,------.(_/.  \_)-./     '._  .-----. ,--.   ,--.).-'),-----. ,------. (_)---\_)(,------.
|'--...__)|  .---' \  `.' / |'--...**)/ ,-. \| `.'   |( OO'  .-.  '|   /`. '/ _ | | .---'
'--. .--'| | \ /\ '--. .--''-' | || |/ | | | || / | |\ :` `. | |
| | (| '--. \ \ | | | .' / | |'.'| |\_) | |\| || |_.' | '..`''.)(| '--.
| | | .--' .' \_) | | .' /** | | | | \ | | | || . '.'.-.\_) \ | .--'
| | | `---. /  .'.  \    |  |   |       ||  |   |  |   `' '-' '| |\ \ \ / | `---.
   `--' `------''--'   '--'   `--' `-------'`--' `--'     `-----' `--' '--' `-----' `------'
"""

2. Import a dictionary of text to morse

3. Ask user for text they want to convert to morse code.

4. Create a function text to morse

5. Error handling

6. Print Output and userr if they would like to continue.
