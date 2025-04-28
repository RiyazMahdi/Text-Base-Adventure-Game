# 🧭 Text-Based Adventure Game

Welcome to the **Text-Based Adventure Game**!  
Explore mysterious rooms, meet friends (and foes), find treasures, and make choices that determine your fate. 🗝️⚔️

---

## 📂 Project Structure

| File | Description |
|:-----|:------------|
| `room.py` | Defines the `Room` class to represent different rooms in the game, including their properties and interactions. |
| `main.py` | The core game loop: navigate rooms, interact with characters, and engage in battles. (Now modular with class-based structure!) |
| `item.py` | Defines the `Item` class to handle game items with `name` and `description` attributes. |
| `character.py` | Contains character classes: `Character` (base), `Enemy` (subclass), and `Friend` (friendly NPCs). |
| `character_test.py` | A test script demonstrating how the `Enemy` class works by creating an enemy and interacting with it. |
| `flowchart.drawio` | A rough flowchart (⚠️ not fully saved) for visualizing the game's flow and mechanics. |

---

## ✨ New Features

- 🏃 **Run Away System** — flee from battles if things get too heated!
- 🗺️ **Two New Rooms** — explore even more areas.
- 🧑‍🤝‍🧑 **Friendly NPCs** — not everyone you meet is hostile.
- 🧰 **Chest and Key Mechanic** — find keys to unlock hidden treasures!
- 🎒 **Inventory System** — collect, store, and use items.

---

## 🚀 Future Plans (If Time Permits)

- ❤️ **Health and Damage System** — add hit points and combat mechanics.
- 🗺️ **Map System** — visualize explored areas of the game world.

---

## 🛠️ How to Run

1. Clone the repository or download the files.
2. Make sure you have **Python 3.6+** installed.
3. Run the game using:

```bash
python main.py
