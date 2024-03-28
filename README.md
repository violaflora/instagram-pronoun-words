<img src="ex.jpg">

# About
Instagram allows you to put 1-4 pronouns on your profile. This program outputs the combinations of pronouns that form valid words in the supported languages that use Latin scripts. The files generated by this program can be viewed in [/words_found/](/words_found/). Each line contains the following information:

`word: ('pronouns', 'in', 'word') ('language', 'of', 'pronoun')`

## How to Use
1. Put one or more of the below .txt dictionaries in [/word_lists/](/word_lists/)
2. `python pronouns_to_words.py`

## Word Lists
🇬🇧 [English](https://raw.githubusercontent.com/Paf1cent/instagram-pronoun-words/master/words_found.txt)

🇪🇸 [Spanish](https://raw.githubusercontent.com/xavier-hernandez/spanish-wordlist/main/text/spanish_words.txt)

🇵🇹 [Portuguese](https://gist.githubusercontent.com/Kasama/b75f8d57432b7e9e18e49843485d69e9/raw/c3d6b644b1ba8acd95cb4775d52d76f05e1eeee8/portuguese-word-list.txt)

🇫🇷 [French](https://raw.githubusercontent.com/Taknok/French-Wordlist/master/francais.txt)

🇩🇪 [German](https://gist.githubusercontent.com/MarvinJWendt/2f4f4154b8ae218600eb091a5706b5f4/raw/36b70dd6be330aa61cd4d4cdfda6234dcb0b8784/wordlist-german.txt)

🇮🇩 [Indonesian](https://raw.githubusercontent.com/fachrurRz/sentiment-analysis/master/indonesian-wordlist.txt)

🇹🇷 [Turkish](https://raw.githubusercontent.com/mertemin/turkish-word-list/master/words.txt)

🇳🇴 [Norwegian](https://raw.githubusercontent.com/Ondkloss/norwegian-wordlist/master/wordlist_20220201_norsk_ordbank_nno_2012.txt)

🇫🇮 [Finnish](https://raw.githubusercontent.com/hugovk/everyfinnishword/master/kaikkisanat.txt)

🇩🇰 [Danish](https://raw.githubusercontent.com/fraabye/Danish-wordlists/master/20200419-Danish-words.txt)

🇳🇱 [Dutch](https://raw.githubusercontent.com/OpenTaal/opentaal-wordlist/master/wordlist.txt)

🇸🇪 [Swedish](https://raw.githubusercontent.com/martinlindhe/wordlist_swedish/master/swe_wordlist)

🇻🇦 [Latin](https://petscan.wmflabs.org/?language=la&project=wiktionary&categories=Lingua%20Latina&ns%5B0%5D=1&sortby=title&interface_language=en&active_tab=tab_output&&doit=)

[Arabic](https://raw.githubusercontent.com/loayamin/arabic-words/master/word-list.txt)

## Changes from forked project
- [x] [pronouns.txt: Change 'faee' to 'faer', add 'faers'](https://github.com/violaflora/instagram-pronoun-words/commit/c299f0ed9770b41deb6855739c023b47597e9d4c)
- [x] [pronouns.txt: Add 'hirs'](https://github.com/violaflora/instagram-pronoun-words/commit/4f0dba218186d33c1fc1630c87a18b39839b294c)
- [x] [pronouns_to_words.py: Add support for 4-pronoun words](https://github.com/violaflora/instagram-pronoun-words/commit/c521a7d2061db0a8db27d1888962a265c3ecf785)
- [x] [words_found/: Add folder for output file in the 12 supported Latin script languages](https://github.com/violaflora/instagram-pronoun-words/tree/master/words_found)
- [x] [word_lists/: Add folder for input files](https://github.com/violaflora/instagram-pronoun-words/commit/86535f16d25b12c7a093fc02b0b60bc793ddddb2)
- [x] [pronouns_to_words.py: Add logic to iterate through word_lists/](https://github.com/violaflora/instagram-pronoun-words/commit/86535f16d25b12c7a093fc02b0b60bc793ddddb2) 

## TODO
- [ ] Look into Arabic and Farsi, see if you can add pronouns to `pronouns.txt` and run it like the rest of the languages.
- [ ] Look into programmatic profanity/sensitive content filtering (e.g. 'nazie', 'viol', 'violer' in French).
