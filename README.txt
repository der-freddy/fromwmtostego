############
#README.txt#
############

****english version below****

Zum Ausführungen der Demonstrationsdateien (encode_demo.py und decode_demo.py),
werden einige Python-Paket (libROSA, bitarray usw.) benötigt, welche aus der requirments.txt zu entnehmen sind.

Für die Implementierung wurde Python 3.8.5 genutzt.

encode_demo.py
##############

Zum Einbetten von Informationen können mehrere Audiosignale oder einzenlne Dateien verarbeitet werden. Dafür werden die entsprechenden Datei in den Ordner 'import' gelegt. In der python-Datei kann die einzubettenden Information in dem Objekt msg hinterlegt werden. Anschließenden muss die Datei ausgefüht werden. Die maniplulierten Dateien werden im Ordner 'export' gespeichert.

decode_demo.py
##############

Datei, die dekodiert werden sollen, müssen in den Ordner 'export' hinterlegt werden. Anschließend kann die Python-Datei 'decode_demo.py' ausgeführt werden. Im Terminal wird die Information angezeigt.


****english****
To execute the demonstration files (encode_demo.py and decode_demo.py),
some Python packages (libROSA, bitarray etc.) are required, which can be found in the requirments.txt.

Python 3.8.5 was used for the implementation.

encode_demo.py
##############
Multiple audio signals or individual files can be processed to embed information. To do this, the corresponding files are placed in the 'import' folder. In the python file, the information to be embedded can be stored in the msg object. The file must then be executed. The manipulated files are saved in the 'export' folder.

decode_demo.py
##############
Files that are to be decoded must be stored in the 'export' folder. Then the Python file 'decode_demo.py' can be executed. The information is displayed in the terminal.