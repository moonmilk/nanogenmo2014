nanogenmo2014
=============

project for DariusK's National Novel Generation Month: https://github.com/dariusk/NaNoGenMo-2014/

The novel idea: scraping twitter for tweets about #NaNoWriMo and assembling them into a book.

This stuff uses the Pattern library from http://www.clips.uantwerpen.be/pattern - really simple twitter scraping and linguistic analysis!

## wrimo-titler.py ##
Can't think of a title for your novel? Let wrimo-titler steal one for you. Searches twitter for people posting title ideas for #nanowrimo and extracts the ideas. Sample run:

```
Here's your title - choose one:
"How to Find a Husband"
"Double-Edged Sword"
"Justice for Katie"
"Promises Made/Debts Paid."
"You can't write if you can't relate."
"Infinite Sky"
"character listing"
"Main Title"
```

## wrimo-grabber.py ##
Will grab tweets with the hashtag #NaNoWriMo (or whatever you change it to) until it gets the number of words you asked for, or you hit Twitter's search rate limit. It'll download tweets, split them into sentences, throw away the sentences that contain the hashtag, and save them in a json file called sentences.json. If you want to do another search and don't want the results to overlap with earlier searches, put the most recent search result's tweet ID into the STOP_AT variable and it'll quit searching when it hits that one. If you're doing multiple searches, rename the output file so it doesn't get overwritten.

The grabber also runs Pattern's sentiment analysis tool on each sentence, because why not?

## wrimo-writer.py ##
Give it the json files from grabber and it will write your novel for you. Use wrimo-titler to steal a title (or make up your own, if you must), and edit it into the TITLE variable. The output is in markdown format. Example usage: `python wrimo-writer.py sentences.json sentences2.json > mynovel.md` 

## novelette1.md and novelette2.md ##
Sample output from wrimo-writer. It's not a full novel, only 32,000 words, because I haven't collected enough tweets yet to make a full 50K.

## novelette3.md, .html, .pdf and wrimo.css ##
Learning how to use print css to make the PDF look more like a cheap paperback and less like the printout from a web browser. css @page object and widows, orphans, and page-break-before properties allow some simple but effective page formatting. I also added a slightly tacky free google font to further distance the resulting look from default browser printouts.

I learned my css paged meda tricks from http://www.tutorialspoint.com/css/css_paged_media.htm

I used multimarkdown <http://fletcherpenney.net/multimarkdown/> to turn wrimo-writer's markdown output into html, edited the html slightly to add the font, stylesheet, and title page, opened the html in Chrome and printed to PDF to make the output file.

## novel.md, .html, and .pdf ##
The finished novel, 50500 words.