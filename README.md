# tachidesk-batch-download

Setup: download tachidesk at <https://github.com/Suwayomi/Tachidesk-Server>

Follow installation steps, launch browser version (electron version will work but doesn't tell you the manga id)

Manually install extensions (mangadex, etc)

Process: Search for manga title. When you click into a manga, the url will look something like this:

```
http://127.0.0.1:4567/manga/571/
```

http://127.0.0.1:4567/ is the port, 571 represents the manga ID.

While leaving the browser window open, run

```
python3 tachidesk-batch-download.py --id 571 --start 0 --end 100
```

To download chapters 0-100 of the manga with id 571.

See <https://github.com/Suwayomi/Tachidesk-Server/wiki/Troubleshooting> for where to find downloaded chapters.
