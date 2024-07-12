# plantcare

A houseplant care tracker I wrote because sticky notes on pots fall off and
I wanted one JSON file for watering schedules, rooms, and care history.

Track plants, rooms, watering schedules, soil/light notes, and care logs.
Everything lives in one JSON file — no SQLite, no cloud account.

## What it doesn't do

- Outdoor garden / field journal workflows (see fieldlog for that)
- Photo management beyond attachment paths
- Plant disease ID or ML suggestions
- Mobile app — this is a terminal tool

## Install

```bash
pip install .
plantcare --help
```

## Quick start

```bash
plantcare init ~/plantcare.json
plantcare room add --name "Living room" --light bright
plantcare plant add --name Monstera --species "Monstera deliciosa" --room 1
plantcare care add --plant 1 --action water --date 2025-06-01
plantcare report summary
```

## Storage

JSON with schema migrations (0 → 1 → 2 → 3). See `docs/architecture.md`.

## Author

Shimaa Galal — shimaagalal463@gmail.com
