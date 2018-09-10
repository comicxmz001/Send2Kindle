Send2Kindle

A lazy script to push files to your kindle deveices.

Steps:
1. Open "Automator" -> "Application"
2. Choose "Utilities" ->  "Run Shell Script"
3. Drag "Run Shell Script" into workflow window.
4. For "Shell" option, choose "/usr/bin/python"
5. For "Pass Input", choose "as arguments"
6. Copy and past python code (`Send2Kindle_Automator.py`), replace email addresses and account login info, then save as an app.
7. To send a file, drag and drop the file onto the app.
