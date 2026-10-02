# GAME DESIGN PROPOSAL & PRODUCTION PLAN
**Game Title:** *ComicEscape*  
**Submission Category:** 100-Hour Game Jam  
**Target Platform:** Web (HTML5 / WebGL) & Windows Desktop  
**Target Engine:** Godot Engine 4.x (Forward+ / Compatibility)  
**Development Team:**  
- **G. Suchith Reddy** (gattusuchithreddy999@gmail.com)  
- **Thadikonda N V V D Malleeswari** (thadikondamalleeswari@gmail.com)  
- **Adithya Thakur** (yash007adithya@gmail.com)  
**Status:** Scope-Locked & Jam-Ready  

---

## 1. Executive Summary & Pitch

### 1.1 High Concept
*Panel Escape: Issue #0* is a stylized 3D first-person escape-room puzzler rendered in vibrant, cel-shaded comic book visuals. Players navigate the surreal interior of an in-progress comic strip, utilizing an anti-gravity "Float" mechanic to traverse vertical hazards, solve environmental puzzles, and hunt down the elusive "Comic Book Issue #1"—only to discover a sharp, tongue-in-cheek meta twist: the exit was unlocked from the very start.

### 1.2 Core Pillars
1. **Bold Comic Aesthetics:** Halftone dot overlays, ink outlines, dynamic comic onomatopoeia (`*WHOOSH*`, `*CLICK*`, `*BZZT*`), and speech bubble prompts.
2. **Tactile Vertical Traversal:** Seamless toggle between ground-based first-person exploration and a buoyant, zero-g floating state.
3. **Subversive Meta Narrative:** Subverting classical escape-room friction through humor and self-referential game design tropes.
4. **Feasible & Polished Jam Scope:** A tight 10–15 minute bite-sized experience built entirely from scratch in 100 hours.

---

## 2. Game Overview & Specifications

| Dimension | Specification |
| :--- | :--- |
| **Genre** | 3D First-Person Puzzle / Escape Room |
| **Perspective** | First-Person Perspective (FPP) |
| **Engine** | Godot 4.3+ (GDScript) |
| **Target Playtime** | 10 to 15 minutes |
| **Distribution Target** | Itch.io (HTML5 browser playable + standalone executable) |
| **Input Scheme** | Keyboard + Mouse (WASD, Mouse Look, Space/F to Float, E to Interact) |
| **Aesthetic Direction** | High-contrast Cel-shading, Halftone shading, Comic-book UI/SFX cards |

---

## 3. Core Mechanics & Innovation

```
                     ┌───────────────────────┐
                     │   GROUND STATE        │
                     │  - Walk / Sprint      │
                     │  - Push buttons / Keys│
                     └──────────┬────────────┘
                                │
               Press [SPACE] or │ Toggle Gravity
               [FLOAT BUTTON]   │ (Depletes / Restores)
                                ▼
                     ┌───────────────────────┐
                     │   BUOYANT FLOAT STATE │
                     │  - Gentle upward drift│
                     │  - 3D Air thrusters   │
                     │  - Vertical navigation│
                     └───────────────────────┘
```

### 3.1 The Anti-Gravity / "Light Float" Mechanic
* **Trigger:** Activated via UI Button or designated keybind (`Space` or `F`).
* **Physics & Feel:**
  * When active, normal downward gravity is inverted into a gentle buoyant lift with high linear damping, creating a dreamy, weightless sensation reminiscent of floating off a printed page.
  * Allows the player to ascend shaft hazards, cross wide floor chasms, and reach elevated ducts, rafters, and floating panels.
  * Visual feedback: The screen vignettes with ink sketch lines; floating sound effects accompany motion (`*WHOOSH*` comic popup card floats in 3D space).
* **Constraints:** A balance meter / floating stamina bar prevents indefinite flight, requiring strategic planning between safe landing pads.

### 3.2 Environmental Interaction & Comic Diegesis
* **Inspect & Manipulate:** Standard interact key (`E`) triggers item pickups, terminal switches, and rotary valves.
* **Onomatopoeic Feedback:** Audio cues are mirrored visually with stylized 3D billboarded text sprites (e.g., slamming a locker spawns an animated `*CLANG!*`).
* **Narrative Narration Boxes:** Narrative commentary appears in stylized yellow caption boxes at the top edge of the screen, mimicking classic comic panels.

---

## 4. Narrative Architecture & The Meta-Twist

### 4.1 Narrative Setup
The player awakens trapped inside an abstract, hyper-stylized containment facility labeled **"The Publisher's Vault."** A broadcast terminal chirps:
> *"INTRUDER PROTOCOL ACTIVE: Vault lockdown in effect. Security clearance requires physical insertion of Golden Age Artifact: COMIC BOOK ISSUE #1."*

### 4.2 The Progression Loop
* **Zone 1 (Tutorial - Panel 1: "The Gutter"):** Teaches first-person movement, object grabbing, and the gravity inversion mechanism.
* **Zone 2 (Navigation - Panel 2: "The Grid"):** Multi-level spatial vertical puzzle where players manipulate laser tripwires, draft vents, and weight plates to access a secure safe containing "Issue #1".
* **Zone 3 (Finale - Panel 3: "Splash Page"):** The player carries the coveted comic book back across the chamber to the monolithic Exit Blast Door.

### 4.3 The Climax & Meta-Twist
* Upon approaching the blast door with "Issue #1" ready to insert into the scanner, the player nudges the door or presses `E` to interact.
* The door effortlessly swings open with a tiny, unimpressive wooden squeak (`*CREAK...*`).
* **The Revelation:** The massive vault lock was an elaborate cardboard cutout/prop. The door had no active lock mechanism whatsoever; the player could have pushed it open in the first 5 seconds.
* The screen freezes into a final printed comic back-cover splash:  
  **"CONGRATULATIONS! You spent 15 minutes solving puzzles to open a door that was never locked. Produced in 100 Hours. THE END!"**

---

## 5. Level & Zone Design

```
 [ZONE 1: The Gutter] ──> [ZONE 2: The Grid (Vertical)] ──> [ZONE 3: Splash Page (Exit)]
  * Basic Movement          * Air currents & Float pads      * Monolithic Vault Door
  * Gravity Toggle intro    * Laser grid navigation          * Issue #1 Safe Pedestal
  * Simple Keycard door     * Multi-level switch sequence    * THE UNLOCKED TWIST
```

### Zone 1: Tutorial ("The Gutter")
* **Goal:** Teach fundamentals without intrusive tutorial modals.
* **Layout:** A linear two-story office/archive room.
* **Puzzle:** A switch is located on a high catwalk with no ladder. The player must trigger Float Mode to drift upward and hit the switch, opening the bulkhead into Zone 2.

### Zone 2: Puzzle Navigation ("The Grid")
* **Goal:** Test spatial mastery of the Anti-Gravity mechanic.
* **Layout:** An open, three-tiered atrium with industrial fans, comic printing presses, and moving hazard beams.
* **Puzzles:**
  1. Activating pressure plates using low-gravity carried objects.
  2. Floating across deactivated fan drafts before timers run out.
  3. Reaching the high-security display case to claim **"Comic Book Issue #1"**.

### Zone 3: The Grand Finale ("The Splash Page")
* **Goal:** Deliver theatrical tension and land the punchline.
* **Layout:** A dramatic bridge over a bottomless void leading to a colossal, intimidating vault portal lined with flashing warning lights and caution tape.
* **Resolution:** The player reaches the door, interacts, and discovers the door has no locking latch—merely a classic pull handle. Cue confetti, comic fanfare, and credits roll.

---

## 6. Art & Audio Direction

### 6.1 Visual Styling (Godot 4 Shaders)
* **Outline Post-Process:** Sobel/Laplacian screen-space edge detection shader to produce dynamic black ink outlines around 3D geometry.
* **Cel-Shading:** 3-band stepped ramp lighting with halftone screentone patterns embedded in shadow falloffs.
* **Typography:** Bold comic display fonts (e.g., *Bangers*, *Komika Axis*, or CC0 alternatives) with thick strokes and drop shadows.

### 6.2 Audio Landscape
* **BGM:** Quirky, upbeat lo-fi funk/jazz bassline with muted trumpet hooks, keeping puzzle frustration low.
* **SFX:** Punchy, exaggerated cartoon foley—pressurized pneumatic hisses for gravity shifts, tactile mechanical clicks, and playful spring boings.

---

## 7. 100-Hour Production Schedule

```
 0h         10h                           40h                           70h               90h       100h
 [Phase 1  ] [Phase 2: Controller/Blockout] [Phase 3: Mechanics & Rooms ] [Phase 4: Polish] [Phase 5]
  Scope/Repo   Player FPP + Graybox Zones     Float Scripting + Puzzles    Audio, CC0, UI   QA/Export
```

### Phase 1: Inception & Project Setup (Hours 0 – 10)
* Initialize Git repository with proper Godot 4 `.gitignore`.
* Establish directory architecture (`/scenes`, `/scripts`, `/assets/models`, `/shaders`, `/ui`).
* Scope lock: finalize design document, zone layouts, and win conditions.
* Set up baseline Godot 4 project settings (Input Map, Display Settings, WebGL Compatibility flags).

### Phase 2: Player Controller & Blockout (Hours 10 – 40)
* Implement modular First-Person `CharacterBody3D` controller (smooth mouse look, head bob, acceleration).
* Construct primitive graybox geometry for Zones 1, 2, and 3 using Godot CSG primitives (`CSGBox3D`, `CSGCombiner3D`).
* Implement interaction raycasting system (`Interactable` interface for buttons, doors, pickups).

### Phase 3: Puzzles & Anti-Gravity Scripting (Hours 40 – 70)
* Develop `GravityManager` singleton and state logic for the buoyant float mechanic.
* Implement Float UI gauge and cooldown/recharge parameters.
* Wire logic for Zone 2 puzzles (laser tripwires, weighted pressure plates, lock codes).
* Script the sequence for picking up "Issue #1" and unlocking Zone 3.

### Phase 4: Asset Integration, Shaders & UI (Hours 70 – 90)
* Apply custom cel-shading and ink outline post-processing shaders.
* Replace CSG geometry with optimized CC0 3D modular kit (Kenney.nl assets).
* Integrate sound effects and background music loops.
* Design and animate comic UI: dialogue cards, onomatopoeia billboards, float gauge.
* Implement the climatic gag sequence and end credits splash.

### Phase 5: Testing, Web Export & Submission (Hours 90 – 100)
* Cross-platform optimization: Test HTML5/WebGL export in Chromium/Firefox engines.
* Balance jump heights, float speeds, and puzzle timings based on test runs.
* Produce Itch.io promotional assets (cover banner, screenshots, animated GIFs).
* Draft and package `README.md` and complete CC0 attribution in `CREDITS.md`.
* Final repository release tag and jam submission push before deadline.

---

## 8. Jam Rules Compliance & Asset Provenance

| Compliance Criterion | Strategy & Verification |
| :--- | :--- |
| **Fresh Codebase** | Repository initiated post-jam announcement with clear initial commit timestamp; zero proprietary starter code. |
| **Public Repository** | Hosted publicly on GitHub with continuous commit history demonstrating the 100-hour progression. |
| **Third-Party Assets** | Strictly limited to 100% free / CC0 / Open Source assets (audio from Freesound.org / Sonniss, 3D meshes from Kenney.nl, fonts with SIL Open Font License). |
| **Documentation** | Dedicated `CREDITS.md` maintained throughout development detailing author names, licenses, and source URLs for every imported file. |
| **Standalone & Web Ready**| Export pipelines tested with Godot 4 Web target to ensure instant browser accessibility for jam judges. |

---

## 9. Risk Management & Scoping Contingencies

| Potential Risk | Severity | Contingency Plan |
| :--- | :---: | :--- |
| **WebGL Shader Incompatibilities** | High | Design cel-shader with Godot 4 Compatibility renderer fallback; test web build by Hour 50. |
| **Float Physics Tuning Glitches** | Medium | Use velocity dampening and direct position clamping rather than raw unpredictable impulses. |
| **Time Crunch on Asset Modeling** | Medium | Rely strictly on curated modular CC0 packages (Kenney Retro Urban/Sci-Fi kits) rather than bespoke modeling. |
| **Zone 2 Puzzle Complexity** | Low | Design Zone 2 with modular bypasses: puzzles can be pruned without breaking the narrative flow. |

---

## 10. Conclusion
*Panel Escape: Issue #0* combines a distinct graphic novel presentation with tight, vertical puzzle traversal. Its achievable three-zone structure ensures completion within the 100-hour timeframe, while its comedic meta-twist guarantees high memorability among jam voters and players.
