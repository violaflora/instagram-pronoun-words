import itertools
import sys
import os

# d[pronoun]: language
d = {'co': 'English', 'cos': 'English', 'e': 'English', 'ey': 'English', 'em': 'English', 'eir': 'English', 'fae': 'English', 'faee': 'English', 'he': 'English', 'him': 'English', 'his': 'English', 'she': 'English', 'her': 'English', 'hers': 'English', 'mer': 'English', 'mers': 'English', 'ne': 'English', 'nir': 'English', 'nirs': 'English', 'nee': 'English', 'ner': 'English', 'ners': 'English', 'per': 'English', 'pers': 'English', 'they': 'English', 'them': 'English', 'theirs': 'English', 'thon': 'English', 'thons': 'English', 've': 'English', 'ver': 'English', 'vis': 'English', 'vi': 'English', 'vir': 'English', 'xe': 'English', 'xem': 'English', 'xyr': 'English', 'ze': 'English', 'zie': 'English', 'zir': 'English', 'hir': 'English', 'hirs': 'English', 'fae': 'English', 'faer': 'English', 'faers': 'English', 'ella': 'Spanish', 'elle': 'Spanish', 'elli': 'Spanish', 'su': 'Spanish', 'a': 'Portuguese', 'ele': 'Portuguese', 'ela': 'Portuguese', 'eles': 'Portuguese', 'elu': 'Portuguese', 'ile': 'Portuguese', 'o': 'Portuguese', 'os': 'Portuguese', 'seu': 'Portuguese', 'sua': 'Portuguese', 'seus': 'Portuguese', 'dele': 'Portuguese', 'dela': 'Portuguese', 'deles': 'Portuguese', 'dile': 'Portuguese', 'delu': 'Portuguese', 'lo': 'Portuguese', 'la': 'Portuguese', 'los': 'Portuguese', 'no': 'Portuguese', 'na': 'Portuguese', 'nos': 'Portuguese', 'elle': 'French', 'ellui': 'French', 'el': 'French', 'ul': 'French', 'ulle': 'French', 'il': 'French', 'iel': 'French', 'ille': 'French', 'ielle': 'French', 'i': 'French', 'ol': 'French', 'olle': 'French', 'ael': 'French', 'al': 'French', 'son': 'French', 'sa': 'French', 'san': 'French', 'saon': 'French', 'lui': 'French', 'er': 'German', 'ersie': 'German', 'el': 'German', 'en': 'German', 'em': 'German', 'enes': 'German', 'eos': 'German', 'et': 'German', 'es': 'German', 'ihn': 'German', 'ihr': 'German', 'ihre': 'German', 'ios': 'German', 'ioi': 'German', 'ihrol': 'German', 'iks': 'German', 'ikses': 'German', 'ind': 'German', 'inds': 'German', 'per': 'German', 'as': 'German', 'sein': 'German', 'sie': 'German', 'sier': 'German', 'sien': 'German', 'soi': 'German', 'sos': 'German', 'seinos': 'German', 'sien': 'German', 'siem': 'German', 'sierer': 'German', 'sim': 'German', 'sin': 'German', 'sel': 'German', 'ser': 'German', 'sey': 'German', 'sif': 'German', 'sir': 'German', 'dey': 'German', 'dem': 'German', 'denen': 'German', 'demm': 'German', 'deren': 'German', 'die': 'German', 'deren': 'German', 'denen': 'German', 'fae': 'German', 'faer': 'German', 'hän': 'German', 'hen': 'German', 'ham': 'German', 'hem': 'German', 'han': 'German', 'hen': 'German', 'zae': 'German', 'ze': 'German', 'zee': 'German', 'zet': 'German', 'zie': 'German', 'zier': 'German', 'xier': 'German', 'xien': 'German', 'xies': 'German', 'xe': 'German', 'xer': 'German', 'xie': 'German', 'xieren': 'German', 'vii': 'German', 'bla': 'German', 'blas': 'German', 'nin': 'German', 'o': 'Turkish', 'onu': 'Turkish', 'ona': 'Turkish', 'onun': 'Turkish', 'dia': 'Indonesian', 'se': 'Norwegian', 'sen': 'Norwegian', 'han': 'Norwegian', 'ham': 'Norwegian', 'hans': 'Norwegian', 'hun': 'Norwegian', 'henne': 'Norwegian', 'hennes': 'Norwegian', 'hen': 'Norwegian', 'hens': 'Norwegian', 'hän': 'Finnish', 'hänet': 'Finnish', 'hänen': 'Finnish', 'han': 'Danish', 'ham': 'Danish', 'hans': 'Danish', 'hun': 'Danish', 'hende': 'Danish', 'hendes': 'Danish', 'ij': 'Dutch', 'die': 'Dutch', 'diens': 'Dutch', 'hij': 'Dutch', 'hem': 'Dutch', 'haar': 'Dutch', 'hen': 'Dutch', 'hun': 'Dutch', 'het': 'Dutch', 'hjin': 'Dutch', 'zji': 'Dutch', 'xe': 'Dutch', 'xem': 'Dutch', 'xir': 'Dutch', 'en': 'Swedish', 'ens': 'Swedish', 'de': 'Swedish', 'dem': 'Swedish', 'deras': 'Swedish', 'den': 'Swedish', 'den': 'Swedish', 'dess': 'Swedish', 'dens': 'Swedish', 'han': 'Swedish', 'honom': 'Swedish'}

# create list of pronouns once outside the loop
raw_pronouns = open("pronouns.txt").readlines()
pronouns = []
for pronoun in raw_pronouns:
    p = pronoun.strip()
    pronouns.append(p)

for filename in os.listdir('word_lists'):
    wordListFileName = os.path.join('word_lists', filename)
    # checking if it is not the readme file
    if os.path.isfile(wordListFileName) and wordListFileName != 'word_lists/readme.txt':
        found = []

        # encoding ensures accented characters are processed correctly
        words = open(wordListFileName, encoding = "ISO-8859-1").readlines()
        dictionary = {}
        for word in words:
            w = word.strip()
            dictionary[w] = True

        # range of 1-5 ensures 4-pronoun words are found
        for L in range(1, 5):
            for subset in itertools.combinations(pronouns, L):
                joined_word = "".join(subset)
                lookup = dictionary.get(joined_word)
                if (lookup):
                    # word: ('pronouns', 'in', 'word') ('languages', 'of', 'pronouns')
                    found.append(joined_word + ": " + subset.__str__() + " " + tuple(d[item] for item in subset).__str__() + "\n")

        found = [*set(found)] # Removes Duplicates
        found.sort() # Alphabetatizes
        # grab file name after folder name
        file = open("words_found/" + wordListFileName.split("/")[1], "w")
        for toWrite in found:
            file.write(toWrite)
        file.close()