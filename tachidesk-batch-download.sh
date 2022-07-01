#Shamelessly stolen from AvinashReddy3108 at https://github.com/Suwayomi/Tachidesk-Server/issues/181
#Requires tachidesk server running at localhost4567

BASE="http://localhost:4567"; ID="1108"; FROM="3"; TO="4"

# Make cURL go brrrrr
for i in $( seq $FROM $TO ); do
    curl -s "$BASE/api/v1/download/$ID/chapter/$i" \
        -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36' \
        -H 'Accept: application/json, text/plain, */*' \
        -H 'Accept-Language: en-US,en;q=0.5' \
        -H 'Accept-Encoding: gzip, deflate, br' \
        -H 'Connection: keep-alive' \
        -H "Referer: $BASE/manga/$ID" \
        -H 'Sec-Fetch-Dest: empty' \
        -H 'Sec-Fetch-Mode: cors' \
        -H 'Sec-Fetch-Site: same-origin'
    echo "[Download requested] $BASE/manga/$ID -> Chapter $i"
done

#Notes: might get rate limited if you try to do too much at once? Not sure on specifics
#If you try to download a manga that doesn't exist, no errors will appear, it just won't start the process afaik
#Manga ID system as I understand it:
#The first manga loaded is at ID 1, and the next is at 2, 3, etc.
#Manga is loaded when you search for it in sources, or when you view a list by clicking into a source 'latest' or 'browse'
#Basically if the cover page shows up, it'll get loaded, and from now on it's at ID 971 or whatever
#So ids only go from 0 to whatever you've loaded in, which means you have to search for them past a certain point
#Not a big deal if you want specific things or just a few hundred, but hard to find a list of all 100k mangas or something
#Also if you load multiple sources at once the ids will be out of order

#I have no idea what any of these headers are for
