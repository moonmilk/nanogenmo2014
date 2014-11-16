nanogenmo2014
=============

project for DariusK's National Novel Generation Month: https://github.com/dariusk/NaNoGenMo-2014/

This stuff uses the Pattern library from http://www.clips.uantwerpen.be/pattern - really simple twitter scraping and linguistic analysis!

* wrimo-titler.py: Can't think of a title for your novel? Let wrimo-titler steal one for you. Searches twitter for people posting title ideas for #nanowrimo and extracts the ideas. Sample run:

> Here's your title - choose one:
> "How to Find a Husband"
> "Double-Edged Sword"
> "Justice for Katie"
> "Promises Made/Debts Paid."
> "You can't write if you can't relate."
> "Infinite Sky"
> "character listing"
> "Main Title"

* wrimo-grabber.py: Will grab tweets with the hashtag #NaNoWriMo (or whatever you change it to) until it gets the number of words you asked for, or you hit Twitter's search rate limit. It'll download tweets, split them into sentences, throw away the sentences that contain the hashtag, and save them in a json file called sentences.json. If you want to do another search and don't want the results to overlap with earlier searches, put the most recent search result's tweet ID into the STOP_AT variable and it'll quit searching when it hits that one. If you're doing multiple searches, rename the output file so it doesn't get overwritten.

The grabber also runs Pattern's sentiment analysis tool on each sentence, because why not?

