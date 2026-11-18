---
title: "Devlog 03: Adventurers and Equipment"
description: "Overview of Adventurers, and what each stat represents."
date: 2026-07-05
toc: true
hide-sidebar: true
tags: [gamedev]
---

## Introduction

Some notes on the systems I've built so far for the game.

## Jobs

A unit's `Job` is extremely important, essentially defining their function on the battlefield; it determines the following things:

- *Abilities*: the `Abilities` the unit has access to. 
    - Each unit has access to two "sets" of abilities: their current job's abilities, and a secondary set of abilities, which they can choose from any jobs they have lear

### Overview

### Examples

## Attributes

### Guiding Principles
- Broadly, a unit's stats are between $0$ and $1,000$, with the latter being reached only under ideal conditions, and when near max level.
    - This means that a stat growth per level growth of $1-3$ is abysmal, a growth of $4-6$ is about average, and a growth of $7$ or more (typically capping at $~10$) is excellent.
    - The heuristic here is: only a unit with near-max growth (i.e., a growth of $10$) in some stat, should be able to have $999$ of that stat at level $99$.
- Damage and hit rates are split across `Physical` vs. `Magical`, for example:
    1. a unit that is very tough to `Physical` attacks but not `Magical` attacks, should be good at resisting physical `Debuffs` (like `Stun`) but not magical Debuffs (like `Charm`).
    2. A unit that is good at dealing `Physical` damage should be a bit better at inflicting `Physical` `Debuffs`, but not magical ones.

### General Info
- Unit max level is $99$, main quest is generally scaled towards levels $1-50$ with post-game content oriented to the final levels.
- Stat growth per level is determined by the `Adventurer`'s `Job`, or the `Monster` type.
- Each unit, `Monster` and `Adventurer` alike, has an `Aptitude` between $-2$ and $2$: roughly, this corresponds to how much "potential" they have, or how much "natural aptitude" they have (e.g. they're good at learning?).
    - Baseline is $0$, and the majority of units will fall between $-1$ and $1$.
- Each `Job` and `Monster` type also has an `Aptitude`: with the most common value being $0$. This can be thought of like a "karma" type quality, where "immoral" jobs like `Necromancer` have low `Aptitude`, while `Paladin`s have high `Aptitude`.
- `Attribute` growth per level is not deterministic: there is a random fluctuation that depends on the unit's total `Aptitude` (the sum of their individual `Aptitude` and the aptitude of their `Job`/`Monster` type).
    - Units with high `Aptitude` are likely to receive bonuses to stat growth, and the opposite is true for units with low aptitude. 
    - The baseline is as follows: a unit with $0$ `Aptitude` has a $50\%$ chance of zero fluctuation, and $25\%$ chance each of $\pm 1$.
    - This variance is scaled based on the `Attribute`'s base growth: low growth will fluctuate less, higher growth can fluctuate more.

### Stats

#### Strength
Physical damage.

- Primarily dictates the unit's damage done with basic attacks and physical skills
- Plays a minor role in determining hit rate of physical Debuffs

#### Toughness
Physical defense.

- Primarily dictates the unit's resistance to basic attacks and physical skills
- Primarily dictates the unit's likelihood of resisting physical Debuffs

#### Dexterity
Chance to hit physical attacks and abilities.

- Primarily dictates the unit's hit chance with basic attacks, DamageSkills, physical Debuffs

#### Agility
Chance to dodge things.

- Primarily dictates the unit's likelihood of dodging DamageSkills
- Plays a minor role in determining the unit's likelihood of resisting physical Debuffs

#### Intellect
Offensive magic power.

- Primarily dictates the unit's damage done with magical spells
- Plays a minor role in determining hit rate of magical Debuffs

#### Wisdom
Heal power.

- Primarily dictates the strength of heals cast by the unit
- Plays a minor role in determining the unit's likelihood of resisting magical Debuffs

#### Speed
How often the unit acts.

- Determines the unit's turn order and rate of turn recovery: units with higher speed go first, and more often

#### Tenacity
Magic defense.

- Primarily determines the unit's magic defense
- Primarily determines the unit's likelihood of resisting magical Debuffs

#### Charisma
Buff power.

- Primarily dictates the strength of buffs cast by the unit
- Plays a minor role in determining magic defense

#### Cunning
Debuff power.

- Primarily dictates the strength and hit rate of Debuffs cast by the unit
- Plays a minor role in determining magic attack

#### Luck
Enhances everything.

- Plays a small role in everything: increased damage, increased hit rate, increased dodge rate, etc.

## Equipment

