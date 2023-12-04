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

def list_notes(filter_date=None):
    notes = load_notes()
    if filter_date:
        filtered_notes = [note for note in notes if filter_date in note["timestamp"]]
    else:
        filtered_notes = notes

    for note in filtered_notes:
        print(f"ID: {note['id']}")
        print(f"Title: {note['title']}")
        print(f"Message: {note['message']}")
        print(f"Timestamp: {note['timestamp']}")
        print("=" * 30)

def edit_note(note_id, new_title, new_message):
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            note["title"] = new_title
            note["message"] = new_message
            note["timestamp"] = datetime.datetime.now().isoformat()
            save_notes(notes)
            print("Заметка успешно отредактирована")
            break