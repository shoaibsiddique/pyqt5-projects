This code contains the gui with pyqt5 for fetching the serial com port details, and display the info for particular port.


1. First make the front end GUI in Qt-Designer.
2. Save the file with the name serial_gui.ui
3. Open the command prompt in the same directory and run the following command:
			pyuic5 -x serial_gui.ui -o serialgui.py
			This will generate a python file for the .ui file
			
4. Open the file serialgui.py with any python editor. Now you must be able to run the python file and see the GUI (non-functional) on your screen.

5. Now create a new file and name it as function.py to add and define your functions
