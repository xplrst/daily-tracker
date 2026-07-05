import os
from datetime import datetime, timedelta

# --- CONFIGURATION & PATH RESOLUTION ---
DATE_FORMAT = "%Y-%m-%d"
FILE_EXTENSION = ".md"  # Change to '.txt' for MS Notepad if desired

# 1. Identify the script's current directory (Daily Tracker/Script)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. Target the parent folder (Daily Tracker) for reading and saving logs
TARGET_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
#TARGET_DIR = r"C:\Users\Lenovo\Documents\Notes\Daily Tracker\"

def get_yesterday_unfinished_tasks():
    """Looks for yesterday's tracker in the parent folder and extracts unfinished items."""
    yesterday_str = (datetime.now() - timedelta(days=1)).strftime(DATE_FORMAT)
    yesterday_filename = f"{yesterday_str}{FILE_EXTENSION}"
    yesterday_filepath = os.path.join(TARGET_DIR, yesterday_filename)
    
    unfinished_items = []
    
    if os.path.exists(yesterday_filepath):
        with open(yesterday_filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
            
        inside_unfinished_section = False
        
        for line in lines:
            if "### 🛑 Friction Points / Unfinished Items:" in line:
                inside_unfinished_section = True
                continue
            elif inside_unfinished_section and (line.startswith("###") or line.startswith("---")):
                inside_unfinished_section = False
                break
            
            if inside_unfinished_section:
                cleaned_line = line.strip()
                if cleaned_line.startswith("-") and len(cleaned_line) > 1:
                    task_content = cleaned_line.lstrip("- ").strip()
                    if task_content:
                        unfinished_items.append(task_content)
                        
    return unfinished_items

def create_today_tracker():
    today = datetime.now()
    today_str = today.strftime(DATE_FORMAT)
    day_name = today.strftime("%A")
    
    today_filename = f"{today_str}{FILE_EXTENSION}"
    # Explicitly direct the save file to the parent folder
    today_filepath = os.path.join(TARGET_DIR, today_filename)
    
    if os.path.exists(today_filepath):
        print(f" [!] Today's tracker ({today_filename}) already exists in the target directory.")
        return

    carried_tasks = get_yesterday_unfinished_tasks()
    
    p1 = carried_tasks[0] if len(carried_tasks) > 0 else ""
    p2 = carried_tasks[1] if len(carried_tasks) > 1 else ""
    p3 = carried_tasks[2] if len(carried_tasks) > 2 else ""
    
    overflow_tasks_str = ""
    if len(carried_tasks) > 3:
        for extra_task in carried_tasks[3:]:
            overflow_tasks_str += f"- [ ] {extra_task}\n"

    template_content = f"""# DAILY FOCUS & ACTIVITY TRACKER
Date: {today_str} | Day: {day_name}

---

## 🎯 TOP PRIORITIES FOR TODAY
*Identify the 1-3 high-impact outcomes that will make today a success. Do these first.*
- [ ] 1. {p1}
- [ ] 2. {p2}
- [ ] 3. {p3}

---

## 📥 INPUTS & PROCESSING
*Protect your cognitive bandwidth by processing communication in dedicated blocks.*
- [ ] Morning Inbox Sweep (Urgent flags & triage only)
- [ ] Midday Clear (Respond to key items, archive/file)
- [ ] End-of-Day Zero (Clear, delegate, or schedule for tomorrow)

---

## 🔨 TASKS & EXECUTION
*Break major tasks down into actionable steps. Mark 'X' when complete.*
{overflow_tasks_str}- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 

---

## ⏱️ TIME BLOCKS & FLOW
*Use this space to map out deep work sessions, meetings, or time-blocked intervals.*
- [ ] Block 1 (Deep Work): 
- [ ] Block 2 (Collaborative/Meetings): 
- [ ] Block 3 (Admin/Routine): 

---

## 🧠 END-OF-DAY REFLECTION & ALIGNMENT
*Spend 5 minutes here to transition mindfully out of "work mode" and clear your mental RAM.*

### 📈 Wins & Highlights:
- 

### 🛑 Friction Points / Unfinished Items:
*(What got stuck? Move these to tomorrow's tracker or long-term backlog)*
- 

### 🔋 Energy & Focus Check:
- [ ] High  |  [ ] Balanced  |  [ ] Depleted

---
*Template version 1.3 | Auto-directory initialization fix.*
"""

    # FIX: Ensure the parent 'Daily Tracker' directory exists before creating the file
    os.makedirs(TARGET_DIR, exist_ok=True)

    with open(today_filepath, "w", encoding="utf-8") as f:
        f.write(template_content)
        
    print(f" [📝] Success! Saved today's log in parent folder: {today_filepath}")
    if carried_tasks:
        print(f" [🔄] Carried over {len(carried_tasks)} unfinished item(s).")

if __name__ == "__main__":
    create_today_tracker()