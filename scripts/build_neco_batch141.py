"""Batch 141 - NECO English round 4 (NECO top-up, Round 26).

Grows NECO English from 169 toward ~205 with fresh items in the
established topic families: Lexis (synonyms, antonyms, idioms,
collocations, meaning in context), Structure (tense and aspect,
subject-verb agreement, prepositions, conjunctions, determiners) and
Test of Orals (vowels and diphthongs, consonants, rhymes, word stress,
homophones, intonation). Every word, idiom, sentence and oral item is
new against batch 052 (the sole earlier NECO English round) and the
WAEC/JAMB English pools. Scanned against NECO English r1, WAEC English
(all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch141.py -> content/batch_141_neco_english4.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "English"

T_SYN = "Lexis — Synonyms"
T_ANT = "Lexis — Antonyms"
T_IDM = "Lexis — Idioms & Figurative Language"
T_COL = "Lexis — Collocations & Usage"
T_CTX = "Lexis — Word Meaning in Context"
T_TEN = "Structure — Tense & Aspect"
T_SVA = "Structure — Subject-Verb Agreement"
T_PRE = "Structure — Prepositions"
T_CON = "Structure — Conjunctions & Linkers"
T_DET = "Structure — Determiners & Pronouns"
T_VOW = "Test of Orals — Vowels and Diphthongs"
T_CONS = "Test of Orals — Consonants and Clusters"
T_RHY = "Test of Orals — Rhymes"
T_STR = "Test of Orals — Stress"
T_HOM = "Test of Orals — Homophones"
T_INT = "Test of Orals — Intonation"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- synonyms
    (T_SYN, "Medium", "The new prefect was DILIGENT, checking every register before assembly.",
     "hardworking", "careless", "cheerful", "popular", "A",
     "A diligent person labours with care."),
    (T_SYN, "Medium", "The villagers gave the strangers a CORDIAL welcome.",
     "warm", "cold", "brief", "formal", "A",
     "Cordial warmth comes from the heart."),
    (T_SYN, "Hard", "Old machinery made the factory OBSOLETE within a decade.",
     "outdated", "powerful", "cheaper", "louder", "A",
     "Obsolete things have been left behind."),
    (T_SYN, "Hard", "Her CANDID reply surprised the interviewers.",
     "frank", "rude", "lengthy", "timid", "A",
     "Candid speech hides nothing."),

    # ------------------------------------------------------------- antonyms
    (T_ANT, "Medium", "In the dry season water becomes scarce. The word OPPOSITE in meaning to scarce is",
     "plentiful", "costly", "rare", "rough", "A",
     "What is scarce is hard to find."),
    (T_ANT, "Medium", "The manager was HUMBLE despite his great wealth. The opposite of HUMBLE is",
     "arrogant", "gentle", "quiet", "steady", "A",
     "Pride is humility's opposite."),
    (T_ANT, "Hard", "Water in that stream is TRANSPARENT. The opposite of TRANSPARENT is",
     "murky", "shallow", "salty", "still", "A",
     "You cannot see through murky water."),

    # ------------------------------------------------------------- idioms
    (T_IDM, "Medium", "To BURN THE MIDNIGHT OIL is to",
     "work late into the night", "waste fuel on a journey", "light the house at dusk", "quarrel at midnight", "A",
     "The lamp of hard work burns late."),
    (T_IDM, "Medium", "Losing that job proved A BLESSING IN DISGUISE because Musa then started his own shop. The phrase means",
     "a hidden piece of good fortune", "a public misfortune", "a religious ceremony", "a sudden illness", "A",
     "Sorrow dressed in tomorrow's favour."),
    (T_IDM, "Hard", "The judge's warning HIT THE NAIL ON THE HEAD. The idiom means",
     "said exactly the right thing", "struck the table in anger", "repaired the courtroom bench", "missed the point badly", "A",
     "One stroke, squarely true."),
    (T_IDM, "Hard", "The twins visit their grandmother ONCE IN A BLUE MOON. This means they visit",
     "very rarely", "every night", "twice weekly", "on market days", "A",
     "Blue moons are rare sights."),

    # ------------------------------------------------------------- collocations
    (T_COL, "Medium", "The correct collocation is: The farmers prayed for ___ rain.",
     "heavy", "strong", "big", "fat", "A",
     "Rain falls heavy, never strong."),
    (T_COL, "Medium", "Choose the correct option: Bala ___ a living by repairing bicycles.",
     "makes", "does", "takes", "gives", "A",
     "English makes a living, never does one."),

    # ------------------------------------------------------------- context
    (T_CTX, "Medium", "The harvest failed because the rainfall was ERRATIC. The word ERRATIC here means",
     "irregular", "steady", "abundant", "early", "A",
     "Erratic rain comes and goes unannounced."),
    (T_CTX, "Hard", "The referee's decision was IMPARTIAL, so both teams accepted it. IMPARTIAL means",
     "fair to both sides", "delayed by hours", "harsh on the loser", "secret", "A",
     "No side is favoured at all."),

    # ------------------------------------------------------------- tense
    (T_TEN, "Medium", "By December, the contractors ___ the new bridge.",
     "will have completed", "have completed", "were completing", "complete", "A",
     "Future perfect looks back from December."),
    (T_TEN, "Medium", "Aunty ___ in Kano since 2019.",
     "has lived", "lived", "is living", "was living", "A",
     "Since demands the perfect tense."),
    (T_TEN, "Hard", "By the time the chief arrived, the drummers ___.",
     "had left", "have left", "were leaving", "leave", "A",
     "Past perfect went before the arrival."),

    # ------------------------------------------------------------- concord
    (T_SVA, "Medium", "Neither of the goalkeepers ___ to blame for the defeat.",
     "was", "were", "are", "have been", "A",
     "Neither takes a singular verb."),
    (T_SVA, "Hard", "Each of the traders ___ a stall at the weekly market.",
     "has", "have", "were given", "are owing", "A",
     "Each always claims a singular verb."),

    # ------------------------------------------------------------- prepositions
    (T_PRE, "Medium", "The little girl is afraid ___ the dark.",
     "of", "from", "with", "at", "A",
     "Fear takes of, never from."),
    (T_PRE, "Medium", "We congratulated the winner ___ her excellent result.",
     "on", "for", "about", "with", "A",
     "Congratulations stand on the achievement."),
    (T_PRE, "Hard", "The wounded traveller insisted ___ paying for his own treatment.",
     "on", "to", "at", "for", "A",
     "Insist is followed by on."),

    # ------------------------------------------------------------- conjunctions
    (T_CON, "Medium", "___ he had fever, Tunde still attended the rehearsal.",
     "Although", "Because", "So", "Unless", "A",
     "Although concedes the fever."),
    (T_CON, "Hard", "The librarian is ___ strict ___ kind to slow readers.",
     "both, and", "either, or", "neither, nor", "not only, but also the", "A",
     "Both always pairs with and."),

    # ------------------------------------------------------------- determiners
    (T_DET, "Medium", "You may travel by ___ of the two roads; both lead to the shrine.",
     "either", "neither", "all", "every", "A",
     "Either chooses one of two."),
    (T_DET, "Hard", "That shiny red bicycle is ___; the twins received it last Christmas.",
     "theirs", "their", "them", "they", "A",
     "The possessive pronoun stands alone."),

    # ------------------------------------------------------------- vowels
    (T_VOW, "Medium", "The vowel sound heard in the word LEAST also rings out in",
     "beast", "bread", "head", "said", "A",
     "The long ee sound rings in both."),
    (T_VOW, "Medium", "The short, flat vowel heard in the word FAN also occurs in",
     "van", "cart", "cut", "cot", "A",
     "The flat a sound lives in van."),
    (T_VOW, "Hard", "The gliding vowel that closes the word TOY also ends the word",
     "noise", "nose", "nurse", "north", "A",
     "The gliding oi sound moves with toy."),

    # ------------------------------------------------------------- consonants
    (T_CONS, "Medium", "When the hairdresser says she will COMB the child's hair, the letter that stays silent in COMB is",
     "b", "c", "o", "m", "A",
     "The b of comb says nothing."),
    (T_CONS, "Hard", "The letter group PH in the word PHOTOGRAPH is pronounced exactly like the letter",
     "f", "p", "v", "s", "A",
     "Greek ph dresses as plain f."),

    # ------------------------------------------------------------- rhymes
    (T_RHY, "Medium", "The word OFF shares its ending sound exactly with",
     "cough", "though", "through", "bough", "A",
     "Cough and off end their sound alike."),
    (T_RHY, "Hard", "The word BITE closes with exactly the same sound as",
     "height", "eight", "weight", "straight", "A",
     "The ending song matches height."),

    # ------------------------------------------------------------- stress
    (T_STR, "Hard", "In the word PHOTOGRAPHER, the stress falls on the",
     "second syllable", "first syllable", "third syllable", "fourth syllable", "A",
     "pho-TO-gra-pher carries it."),
    (T_STR, "Hard", "In the word UNDERSTAND, the stressed syllable is the",
     "third", "first", "second", "fourth", "A",
     "un-der-STAND lifts the voice."),

    # ------------------------------------------------------------- homophones
    (T_HOM, "Medium", "Choose the word that completes the sentence: The hunter saw a ___ in the forest.",
     "bear", "bare", "beer", "bard", "A",
     "Bear the animal sounds like bare."),
    (T_HOM, "Medium", "The baker needs a bag of ___ to bake bread.",
     "flour", "flower", "floor", "flaw", "A",
     "Flour and flower share one sound."),

    # ------------------------------------------------------------- intonation
    (T_INT, "Medium", "A yes-or-no question in English is normally said with a",
     "rising intonation", "falling intonation", "flat tone throughout", "whisper", "A",
     "The voice climbs at the end."),
]

build_batch(
    S,
    "batch_141_neco_english4.json",
    "141",
    "NECO English round 4 (Round 26 top-up): fresh synonyms (diligent, "
    "cordial, obsolete, candid), antonyms (scarce, humble, "
    "transparent), idioms (burn the midnight oil, blessing in disguise, "
    "hit the nail on the head, once in a blue moon), collocations "
    "(heavy rain, make a living), context meanings (erratic, "
    "impartial), tense (future perfect, since-present perfect, past "
    "perfect), concord (neither was, each has), prepositions (afraid "
    "of, congratulate on, insist on), conjunctions (although, "
    "both-and), determiners (either of two, theirs), orals: seat-meat, "
    "cat-bat, boy-noise, silent b in comb, ph as f, cough-off, "
    "height-bite, photographer second-syllable stress, understand "
    "third-syllable stress, bear/flour homophones, rising intonation on "
    "yes-no questions. Scanned against NECO English r1 (batch 052), "
    "WAEC English (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
