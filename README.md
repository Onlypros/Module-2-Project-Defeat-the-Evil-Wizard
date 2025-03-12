# ⚔️🧙 Defeat The Evil Wizard Walkthrough

##  Overview

This is a turn-based RPG battle game where you select a unique hero class and face off against the Evil Dark Wizard.  Your goal is to defeat the Evil Dark Wizard before it's too late.

---

##  How the Game Works

1. You pick one of 5 character classes.
2. You take turns attacking or using special abilities.
3. The wizard fights back using standard and special attacks.
4. You win if the wizard’s HP drops to 0.
5. You lose if your HP drops to 0 first.

---

##  Character Classes

Each class has their own strengths and weaknesses, along with two unique abilities:

### 1. **Warrior Abilities**
- **Warrior’s Resolve:** Increase max health by 15 and +5 attack power.
- **Savage Blow:** +30 bonus damage on next attack.

### 2. **Mage Abilities**
- **Fireball:** Deal 40 direct damage.
- **Sheep:** Force enemy to skip a turn.

### 3. **Archer Abilities**
- **Full Draw:** Deal 40 damage.
- **Evade:** Dodges next incoming attack.

### 4. **Paladin Abilities**
- **Smite:** Adds 25 holy bonus damage to your attack.
- **Divine Protection:** Reduces next incoming damage by 75%.

### 5. **Dark Knight Abilities**
- **Drain Life:** Steal 25 HP from enemy, heal yourself for 20.
- **Blood Pact:** Sacrifice 25 HP for +30 bonus damage.

---

##  Game Mechanics

- Abilities have a **4-turn cooldown**, so use them wisely.
- You also have **Potions (25 HP heal)** with their own 4-turn cooldown.
- Ability descriptions are printed before activation, so you make the best informed decsions.

---

##  Combat System Notes

- Damage is randomized from 0 to your attack power.
- Bonus damage is additive.
- Reduced damage is applied by multiplying opponent’s total damage.
- Status effects are always reset after the turn.

---

##  The Evil Wizard

- Regenerates 5 HP every turn!
- Has a **12.5% chance** to summon minions (deals 35 damage).
- Has a **25% chance** to add **+10 void damage**.

---

##  Game Flow Polish

✔ All turns print clearly:
- “--- Your Turn ---”
- “--- Dark Wizard’s Turn ---”
- “=== End Of Turn ===”

---

##  Planned Expansions

- Adding a Summoner class
- More enemy AI patterns

---

##  File Structure

- `Characters.py`: All character class logic.
- `EvilWizard.py`: EvilWizard behavior and mechanics.
- `M2 Project - Defeat the Evil Wizard.py`: Game flow, UI logic, battle engine.
- `README.md`: This walkthrough.