import jso
import datentime

NOTES_FILE = "notes.json"

def load_notes():
    try:
        with open(NOTES_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=4)

def add_note(title, message):
    notes = load_notes()
    timestamp = datetime.datetime.now().isoformat()
    note = {
        "id": len(notes) + 1,
        "title": title,
        "message": message,
        "timestamp": timestamp
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно сохранена")