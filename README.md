# Phats

![phats](https://user-images.githubusercontent.com/78803192/187493022-f933e903-e08a-49f2-b169-b6c182cee2b2.png)

Wise exports an excel document, this excel document gets cleaned up and properly formatted so it can then be exported to a .txt file that can later be used with PHATS software.

.xlsx to .txt

openpyxl, pandas, tkinter, os

Make an executable later as so - https://www.youtube.com/watch?v=UZX5kH72Yx4&t

## Things to consider
- proper name for this thing
- names of the folders
- location of the folders
- desktop shortcut
- all trash inside one trash file(otherwise phats won't work. Virgis)
- all chassi files in one folder, easy to reach
- output files in one place
- all output files must be in one dir, which is shared and read by phats tablet(domain?)

# README UPDATE:

* Intro

Clean up exported excel document up and properly format it so it can then be
exported to a .txt file that can later be used with PHATS software.

* What is it for

- A program called Wise exports an excel document with lots of part numbers.
- My script takes this excel document, removes unnecessary part numbers(defined
  in another file) and outputs a .txt file that I can later use for software
  called PHATS. This tool is crucial, prevents a lot of manual labor.

Making functions.py file as an executable so it is more convenient for
operators to use this script(double click it and go).

* Libraries used

- openpyxl
- pandas
- tkinter
- os
