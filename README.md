# obsidian_paperpile
My quest towards making taking/reviewing notes from science papers as painless as possible.

In Obsidian, create a new note in main notes vault (leave name Untitled.md unchanged). Paste in bibtex info with cmd+B from selected paper in paperpile. Save, run code. Obviously, folders will have to be tweaked into user's setup. I have a separate folder called /Paper notes/ into which the processed file is moved after renaming (firstauthor et al year title). The code generates independent pages for each author, and formats keywords as provided by the authors into #compund_tags.

Detailed simple instructions:

1. The  p_crawl.py python script in this github repo can be run without any fuss in Thonny for windows or mac (google it). Load the script in Thonny, change (or input as variable when running script in command line) the folder in the script to _your_ obsidian notes vault address.
2. If you then want to run the script as is, you'll have to make a folder _inside_ your vault called 'Paper notes'. In paperpile, copy the bibtex info from your selected paper (cmd+b on mac). Paste this into the main body of a new Obsidian (cmd+n: automatically named Untitled.md) note in the main vault.
3. Save the Untitled note in Obsidian.
4.  Run python script in Thonny (command line %Run p_crawl.py or push green play button). 

This should process the bibtex info into the note layout I made and rename the Untitled.md note into "firstauthor et al year title" format and move it into the Paper notes folder. Done! 

Caveat: I certainly haven't tested this on a HUGE number of papers. May be that older papers will crash it. I also basically exclusively read neuroscience papers. May differ for humanities. Sooo, give it a try, and tweak to your own style/delight. May improve code in future.

Update: the script now creates the /Paper notes/ folder in the vault if there was none. It also checks that the vault folder (input variable) exists, and that there are no duplicates of the processed note file. Exits if any of these fail.
