pause
call py -m venv .venv
call .venv/Scripts/activate
call python -m pip install pip-tools
call python -m pip install jupyter notebook
call python -m ipykernel install --user --name=.venv
pause