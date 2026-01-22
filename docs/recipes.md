# Recipes

## Sunday watering round

```bash
plantcare init ~/plants.json
plantcare room add --name "Kitchen window" --light bright
plantcare plant add --name Pothos --species "Epipremnum aureum" --room 1
plantcare care add --plant 1 --action water --date 2025-08-12 --moisture dry
plantcare report plant --id 1
```

## Bulk import from CSV

```bash
plantcare import csv care_logs.csv --merge
plantcare stats plants --top 10
plantcare report overdue
```

## Backup before schema bump

```bash
plantcare backup create --label pre-v3
plantcare migrate --check
```
