# Dodecaphonist
Dodecaphonist is an application with which you can generate random [twelve-tone (dodecaphony)](https://en.wikipedia.org/wiki/Twelve-tone_technique) music. 
I wrote it in Python and used PySide 6 to make its user interface.

# Requirements
You need to have Python and [Lilypond](https://lilypond.org) installed to use this program.
It's still a work in progress, so please let me know if you find any bugs.
At the moment, it only works on Linux. I'm planning to add support for other OSes in the future.

# Running the program
Clone the repository to your local computer and run /source files/dodecaphonist.py. 
A window should open, showing the available options to create your twelve-tone piece.
You can choose one of the templates (so far, only the Schoenberg template is working), or customise the settings yourself. 
The application will generate the following files:
* `.ly` file - a Lilypond source file
* `.pdf` file - a PDF of the sheet music
* `.midi` file - a midi file so that you can hear an approximation of what it sounds like
