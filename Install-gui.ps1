$ErrorActionPreference = "Stop"

if ($null -eq (Get-ChildItem env:VIRTUAL_ENV -ErrorAction SilentlyContinue))
{
    Write-Output "This script requires that the Skynet Python virtual environment is activated."
    Write-Output "Execute '.\venv\Scripts\Activate.ps1' before running."
    Exit 1
}

if ($null -eq (Get-Command node -ErrorAction SilentlyContinue))
{
    Write-Output "Unable to find Node.js"
    Exit 1
}

Write-Output "Running 'git submodule update --init --recursive'."
Write-Output ""
git submodule update --init --recursive

Set-Location skynet-blockchain-gui

$ErrorActionPreference = "SilentlyContinue"
npm install --loglevel=error
npm audit fix
.\node_modules\.bin\electron-rebuild.cmd -f -w node-pty
npm run build
py ..\installhelper.py

Write-Output ""
Write-Output "................................................................................
................................................................................
....................................#%%%%%%%%...................................
..................................#####%%%%%%%%.................................
.................................#######%%%%%%%%................................
................................#########%%%%%%%%...............................
..............................#############%%%%%%%%.............................
.............................#######,#######%%%%%%%%............................
...........................########///########%%%%%%%(..........................
..........................########/////########%%%%%%%%.........................
.........................#######////////.#######%%%%%%%%........................
.......................########////////...########%%%%%%%%......................
......................########///////......,#######%%%%%%%%.....................
....................########////////.........#######*%%%%%%%*...................
...................########////////...........(#######%%%%%%%%..................
.................,########///////%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%.................
................########////////%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...............
...............########///////////////////////////////////////////..............
.................####///////////////////////////////////////////................
..................##///////////////////////////////////////////.................
................................................................................
................................................................................
.....................@..............................................@...........
...........@@@@@@@...@.....@@@..@......@...@@@@@@@...../@@@@@#...@@@@@@@........
..........@@.........@..@@@.....@......@...@@.....@@..@@.....@@.....@...........
.................@&..@...@@.....@......@...@@.....@@..@@............@...........
..........@@@@@@@....@.....@@@...@@@@@.@...@@.....@@....@@@@@@......@...........
.................................@@@@@@@........................................
................................................................................
................................................................................
...............   Skynet blockchain Install-gui.ps1 completed   ................
................................................................................
...  Type 'cd skynet-blockchain-gui', then 'npm run electron' to start GUI   ...
................................................................................
"