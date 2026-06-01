# setup.py
import os
topics = ["loops","functions","classes","modules","errors",
          "files","lists","dicts","sets","comprehensions"]
os.makedirs("notes", exist_ok=True)
for t in topics:
    open(f"notes/{t}.md", "w").write(f"# {t}\n\nNotes go here.\n")
print("Created 10 note files.")
