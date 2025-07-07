# Formats

## Native JSON (schema 3)

Top-level keys: `schema_version`, `plants`, `rooms`, `care_logs`, `schedules`,
`pots`, `fertilizers`, `sessions`, `notes`, `goals`, `tags`, `collections`, `audit_log`.

## CSV import

Columns: `plant_name`, `species`, `action`, `date`, `soil_moisture`, `notes`.

## Plantly export

CSV with `plant_name`, `species`, `watered_on`, `notes` (subset supported).

## Blossom / GardenPad

Plain-text and CSV care diaries — date-prefixed lines and comma rows.
