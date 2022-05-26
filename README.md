# tony-calculator

The tool for Tony to add some automation to his buisness.

## Prerequisites

- Python 3+ installed: https://www.python.org/downloads/
- Tesseract=ocr installed: https://github.com/UB-Mannheim/tesseract/wiki

## How to build

Install dependencies. Run it for several times if there are errors due to missning files.

```
pip install -r requirements.txt
```

or use ```runBuild.bat``` file.

## How to run

Go to the ```/config``` directory and set the position of panels with values in the ```cfg.json``` file (where x1,y1 - top left corner, x2,y2 - bottom right corner).

Then run the script
```
python calculate.py
```

or use ```runCalculation.bat``` file.

The captured images can be checked in the ```/tmp``` folder.

## Usefull tools

Mouse Position Tracker: https://github.com/Bluegrams/MPos