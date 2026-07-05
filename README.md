# daily-tracker
🧠 An automated,  organizational psychologist optimized daily focus and activity tracker that seamlessly carries over unfinished tasks from yesterday. Built with Python and os.path for local use in plain text or Markdown.

# 🧠 Daily Focus & Activity Tracker

An automated, minimalist productivity tracking system designed around organizational psychology principles. This script localizes your daily logs, protects your cognitive bandwidth, and ensures continuity by automatically carrying over unfinished tasks from the previous day.

## 📋 Features & Psychological Design

*   **The Rule of 3:** Restricts core daily objectives to prevent decision fatigue and ensure focus on high-impact work.
*   **Time-Batch Processing:** Prompts communication sweeps at distinct intervals to eliminate cognitive switching costs.
*   **End-of-Day Shutdown:** A 5-minute reflection block designed to clear your mental RAM and create a healthy boundary between work and personal time.
*   **Automated Continuity:** Dynamically scans yesterday's log, extracts unfinished friction points, and rolls them directly into today's priority slots.

## 📁 File Structure

For the path resolution to execute flawlessly, maintain the following directory layout:

```text
📁 Daily Tracker/                <-- Daily Markdown logs are generated here (e.g., 2026-07-04.md)
└── 📁 Script/                   <-- Child directory for automation assets
    └── 📄 daily_tracker.py      <-- The automation engine
```

## 🚀 Getting Started

### Prerequisites

* Python 3.x installed locally.
* A basic text editor (MS Notepad, VS Code, Obsidian, etc.).

### Installation & Configuration

1. Clone or download this repository into your chosen notes directory.
2. Open `Script/daily_tracker.py`.
3. Ensure the `TARGET_DIR` string explicitly matches your local machine architecture using standard Windows path strings.

### Execution

Run the script daily from your terminal or via a shortcut:

```bash
python "C:\Users\YourUsername\Documents\Notes\Script\daily_tracker.py"

```

## 🛠️ Troubleshooting & Windows Security Note

### FileNotFoundError / Silent Failures

If you are running Windows 10/11 and encounter a `FileNotFoundError` despite your folder paths being 100% correct, **Controlled Folder Access** may be blocking the script.

Because Windows secretly blocks third-party background applications from writing new files into protected directories like `Documents`, Python will misinterpret this security barrier and throw a misleading `FileNotFoundError: [Errno 2]`.

To resolve this:

1. Open **Windows Security** > **Virus & threat protection**.
2. Under *Ransomware protection*, click **Manage ransomware protection**.
3. If **Controlled folder access** is turned ON, click **Allow an app through Controlled folder access**.
4. Add your local `python.exe` binary to the whitelist to grant it permission to write files in your tracking folder.

---

*Optimized for sustainable high performance and strict path schema enforcement.*

```

```
