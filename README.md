<div align="center">
  <img src="data/icons/hicolor/scalable/apps/io.github.lloura.DuelPy.svg" width="192" height="192" alt="Duel! Icon"/>
  
  # Duel! (DuelPy)
  
  A Rock, Paper, Scissors, Lizard, Spock game built with GTK4 and Libadwaita
  
  <img src="data/screenshots/main_paper_x_spock.png" alt="Main • Paper x Spock"/>
</div>

---

## About

This project is a modern GNOME port of the concept presented in [ByteSebs's tutorial video](https://www.youtube.com/watch?v=WtvObZHhdf0), originally built with older technologies. Since that tutorial is now outdated (which demonstrates how fast these technologies can evolve!), I decided to recreate it using current GNOME ecosystem tools.

Instead of the classic Rock-Paper-Scissors, I implemented the **Rock-Paper-Scissors-Lizard-Spock** variant (popularized by The Big Bang Theory), as a spiritual reimplementation of a [project I made early in college](https://github.com/lloura/jokenpo).

This is a study project focused on learning GTK4, Libadwaita, and Python integration with GNOME, keeping the code simple and readable.

---

## How to Play

The rules are simple:

- **Rock** crushes Scissors and Lizard
- **Paper** covers Rock and disproves Spock
- **Scissors** cuts Paper and decapitates Lizard
- **Lizard** eats Paper and poisons Spock
- **Spock** vaporizes Rock and smashes Scissors

Choose your move and see if you can beat the computer!

---

## Technologies

- Python 3.14+
- GTK 4
- Libadwaita 1.8+ (GNOME 49)
- Blueprint Compiler
- Meson build system

---

## Installation & Running

### GNOME Builder (Recommended for Development)

1. Install [GNOME Builder](https://flathub.org/apps/org.gnome.Builder)
2. Clone this repository:
```bash
   git clone https://github.com/lloura/DuelPy.git
```
3. Open the project in GNOME Builder
4. Click the **Run** button at the top

### Flatpak

Pre-built Flatpak packages are available in the [Releases](../../releases) section.

---

## Screenshots

<details>
<summary>Click to see more screenshots</summary>

<img src="data/screenshots/lizard_x_rock_paper_x_spock.png" alt="Lizard x Rock • Paper x Spock"/>
<img src="data/screenshots/paper_x_lizard_rock_x_scissors.png" alt="Paper x Lizard • Rock x Scissors"/>

</details>

---

## What I Learned

This project was an excellent opportunity to:

- Experiment with GTK4/Libadwaita principles and design patterns
- Get hands-on experience with GNOME Builder as an IDE
- Learn Python-GObject integration and PyGObject bindings
- Understand the Meson build system and Flatpak packaging
- Apply GNOME Human Interface Guidelines to create a modern UI

I chose Python because I plan to use it for similar projects in the future, and this served as a solid foundation for understanding the GNOME development ecosystem.

---

## Roadmap

- [x] Basic game functionality
- [x] Persistence with GSettings
- [ ] **Next:** Implementation of David C. Lovelace's **RPS-7** mode
- [ ] Implementation of a visual 'How to Play' guide for the different variants
- [ ] Flathub submission (😳👉️👈️)

**Contributions are welcome!** Feel free to open issues or submit pull requests.

---

## Credits & References

**Game Variants:**

- **RPSLS** created by [Sam Kass and Karen Bryla](https://www.samkass.com/theories/RPSSL.html).
- **RPS-7** and others created by [David C. Lovelace](https://umop.com/rps7.htm).

**Inspiration:**

- Originally inspired by [ByteSeb's Duel](https://github.com/byteseb/Duel) & [Tutorial Video](https://www.youtube.com/watch?v=WtvObZHhdf0) and a previous [college project](https://github.com/lloura/jokenpo).

---

## License

This project is licensed under the [GNU General Public License v3.0](COPYING).
