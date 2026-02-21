# FAQ

**Why not a phone app?**  
I water plants with wet hands. A JSON file and a laptop on the counter works fine.

**Can I track outdoor garden beds?**  
Yes, but it's aimed at pots indoors. For field trips see fieldlog.

**Does it remind me to water?**  
It tracks schedules and overdue counts — no push notifications.

**Attachment paths?**  
Care logs store relative paths; photos stay on disk.

**Plugins?**  
Drop a `.py` in `~/.plantcare/plugins/` with a `register()` function.

**Windows paths?**  
JSON uses forward slashes internally; CLI accepts backslashes.

**Multi-user?**  
No locking. One file, one apartment — like my sticky notes were.

**Export to Excel?**  
`plantcare export excel rooms.xlsx` — minimal xlsx via zip/xml stdlib hack.

**Schema downgrade?**  
Not supported. Backup first.

**Tests offline?**  
Yes. Fixtures are local under `tests/fixtures/`.
