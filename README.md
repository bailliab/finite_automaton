# Finite Automaton

## Installation
### Ubuntu:
```
sudo apt install git python3 python3-pip python3-pytest
git clone https://github.com/bailliab/finite_automaton.git
cd finite_automaton
pip3 install -r requirements.txt
pytest-3 -s
```

Result:
```
============================= test session starts ==============================
platform linux -- Python 3.x.x, pytest-3.x.x, py-1.x.x, pluggy-0.x.0
rootdir: /home/finite_automaton, inifile:
collected 3 items

test/test_finite_state.py
For: 110 Result: 0
.
For: 1010 Result: 1
.
For: 1010 Result: the DFA stopped on a non-final state (S1)
.                                            [100%]

=========================== 3 passed in 0.02 seconds ===========================
```
