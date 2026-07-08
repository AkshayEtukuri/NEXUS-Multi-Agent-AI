import json
import os

NOTES_FILE = "notes_data.json"

def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, "r") as f:
        return json.load(f)

def save_note(note_text):
    notes = load_notes()
    notes.append(note_text)
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=2)

def get_all_notes():
    notes = load_notes()
    if not notes:
        return "You have no saved notes yet."
    formatted = "\n".join(f"{i+1}. {note}" for i, note in enumerate(notes))
    return formatted