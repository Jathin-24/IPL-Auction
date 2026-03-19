# 🏏 IPL Auction Arena — College Edition

A premium, real-time **IPL-style cricket auction system** designed for high-stakes college events. Features an **Admin Dashboard** for orchestrating the auction and **Two Professional Live Display** options for your audience.

---

## 🚀 Quick Start (GitHub Ready)

### 1. The Core Repository (REQUIRED)
To keep your project clean for GitHub, you only need these **6 core components**. Everything else is a utility script you can safely delete.

| Component | Purpose |
| :--- | :--- |
| **`ipl_auction_dashboard.html`** | 🎛️ **Admin Control Panel** (The Brain) |
| **`auction_recorder.py`** | 🐍 **Sync Server & Excel Logger** (The Engine) |
| **`live_display.html`** | 📺 **Dynamic Display** (CSS-based, no images needed) |
| **`IPL_slides_ui_and_logic/`** | 📁 **Slide System** (Display, PDF KIT, and Slide Images) |
| **`IPL LIST.xlsx`** | 📋 **Player Data Source** (S.No, Name, Role, Points, Base Price) |
| **`teams.xlsx`** | 📋 **Team List** (Names for automated import) |

### 2. Installation
```bash
pip install pandas openpyxl pymupdf
```

### 3. Running the Auction
1. **Start the Engine**: Run `python auction_recorder.py`
2. **Open the Brain**: Open `ipl_auction_dashboard.html` in Chrome/Edge.
3. **Choose Your Display**:
   - **Option A (Dynamic)**: Open `live_display.html`. Works with any player data.
   - **Option B (Slides)**: Open `IPL_slides_ui_and_logic/live_display.html`. Uses high-quality slide images.

---

## 🖼️ How to Turn PDF into Slides
If you update your **`IPL AUCTION KITS.pdf`**, use the built-in conversion tool to auto-generate the audience slides:

1. Place your PDF in the `IPL_slides_ui_and_logic` folder.
2. Run the script:
   ```bash
   python IPL_slides_ui_and_logic/convert_pdf_to_slides.py
   ```
3. This creates high-quality **`slide_N.jpg`** files in the `slides/` folder for use in the display.

---

## 🧹 Maintenance: Files You Can Delete
To achieve the cleanest GitHub repository, you should **DELETE** these non-essential files:

- **In Root**: `check_excel.py`, `chk_lk.py`, `convert_excel.py`, `fix_leaderboard.py`, `get_data.py`, `inspect_excel.py`, `export_aspose.py`, `RUNNING.txt`, `IPL_LIVE_AUCTION_TRACKER.xlsx`
- **In `IPL_slides_ui_and_logic/`**: `export_aspose.py`, `export_pdf.py`, `export_pdf_pymupdf.py`, `export_slides.py`, `inspect_data.py`

---

## ✨ Feature Highlights

- **Real-time Sync**: Admin actions reflect instantly on audience screens (1s polling).
- **Excel Automation**: Sold/Unsold status, winning prices, and team rosters are automatically logged to a professional Excel tracker.
- **Smart Search & Jump**: Quickly find any player by Name or Serial Number.
- **Auto-Persistence**: Refresh your browser anytime; the auction state is safely stored in `localStorage`.
- **Dual Display Modes**: Choose between a **Dynamic CSS Display** for flexibility or a **Slide-based Display** for a broadcast feel.

---

## 🛠️ Data Management

### Input Format (`IPL LIST.xlsx`)
Requires columns: `S.No`, `Names`, `Role`, `Points`, `Coins`. (Header names are matched flexibly).

### Output Tracker
The server generates `IPL_LIVE_AUCTION_TRACKER_Day_2.xlsx` with:
- **Leaderboard**: Team standings (remaining purse, players bought).
- **Sold History**: Master list of all successful bids.
- **Team Sheets**: Individual rosters for every team.
