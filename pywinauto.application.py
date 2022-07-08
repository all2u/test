from pywinauto.application import Application
app = Application().start("notepad.exe")

app.UntitledNotepad.menu_select("Aide->A propos de Bloc-notes")
app.Dialog.OK.click()
app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces = True)

app.UntitledNotepad.menu_select("Fichier -> Quitter")
app.Notepad.DontSave.click()