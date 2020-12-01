############
#README.txt#
############

Zum Ausführungen der Demonstrationsdateien (encode_demo.py und decode_demo.py),
werden einige Python-Paket (libROSA, bitarray usw.) benötigt, welche aus der requirments.txt zu entnehmen sind.

Für die Implementierung wurde Python 3.8.5 genutzt.

encode_demo.py
##############

Zum Einbetten von Informationen können mehrere Audiosignale oder einzenlne Dateien verarbeitet werden. Dafür werden die entsprechenden Datei in den Ordner 'import' gelegt. In der python-Datei kann die einzubettenden Information in dem Objekt msg hinterlegt werden. Anschließenden muss die Datei ausgefüht werden. Die maniplulierten Dateien werden im Ordner 'export' gespeichert.

decode_demo.py
##############

Datei, die dekodiert werden sollen, müssen in den Ordner 'export' hinterlegt werden. Anschließend kann die Python-Datei 'decode_demo.py' ausgeführt werden. Im Terminal wird die Information angezeigt.