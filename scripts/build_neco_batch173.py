"""Batch 173 - NECO English round 5 (NECO top-up, R32).

Grows NECO English from 208 toward ~243 with angles not yet in the
bank. Lexis: synonyms DILIGENT, DWINDLED, ALLEVIATED, CANDID,
IMPARTIAL; antonyms BOLD, GENEROUS, HUMBLE, ANCIENT, BARREN; idioms
blessing in disguise, turn a deaf ear, at the eleventh hour, make
ends meet, white elephant, pull strings; collocations took effect,
raised an objection, accepted defeat, took off; meanings in context
high spirits, figurehead, in the red. Structure: the future
perfect; hardly ... when; the quality of ... is; However hard;
Each of the two; stemmed from. Test of Orals: the vowel /ae/ as in
cat; the vowel /o-slash/ as in pot; the silent 'l' of salmon; 'x'
as /gz/; a rhyme for 'beard'; the diphthong /aie/ as in fire.
Scanned against NECO rounds 1-4, WAEC English (all rounds) and the
JAMB pool.

    python3 scripts/build_neco_batch173.py -> content/batch_173_neco_english5.json
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
T_WMC = "Lexis — Word Meaning in Context"
T_TEN = "Structure — Tense & Aspect"
T_SVA = "Structure — Subject-Verb Agreement"
T_CON = "Structure — Conjunctions & Linkers"
T_DET = "Structure — Determiners & Pronouns"
T_PRE = "Structure — Prepositions"
T_VOW = "Test of Orals — Vowels and Diphthongs"
T_LET = "Test of Orals — Letters and Letter Groups"
T_RHY = "Test of Orals — Rhymes"

PASSAGES = []
PQ = []

Q = [
    (T_SYN, "Medium", "The new clerk is DILIGENT; she arrives before everyone and leaves last. The word 'diligent' means",
     "hardworking", "careless", "slow-moving", "cheerful", "A",
     "Diligence is steady, careful hard work."),
    (T_SYN, "Medium", "The town's water supply DWINDLED as the dry season wore on. The word 'dwindled' means",
     "decreased", "multiplied", "improved", "froze over", "A",
     "To dwindle is to shrink little by little."),
    (T_SYN, "Medium", "The ointment ALLEVIATED the farmer's back pain within minutes. The word 'alleviated' means",
     "relieved", "worsened", "spread about", "healed completely", "A",
     "Alleviation eases pain without curing it."),
    (T_SYN, "Hard", "The referee later gave a CANDID account of the disputed goal. The word 'candid' means",
     "frank", "biased", "lengthy", "reluctant", "A",
     "A candid speaker hides nothing."),
    (T_SYN, "Medium", "The panel was praised for remaining IMPARTIAL throughout the hearing. The word 'impartial' means",
     "unbiased", "strict", "hasty", "generous", "A",
     "An impartial judge favours neither side."),
    (T_ANT, "Easy", "The word BOLD is the opposite of",
     "cowardly", "brave", "rude", "strong", "A",
     "A bold man dares; a cowardly one trembles."),
    (T_ANT, "Easy", "The word GENEROUS is the opposite of",
     "stingy", "kind", "wealthy", "gentle", "A",
     "The generous hand opens; the stingy one shuts."),
    (T_ANT, "Medium", "The word HUMBLE is the opposite of",
     "arrogant", "modest", "gentle", "famous", "A",
     "Humility bows; arrogance lifts the nose."),
    (T_ANT, "Easy", "The word ANCIENT is the opposite of",
     "modern", "very old", "historic", "ruined", "A",
     "Ancient walls belong to ages long past."),
    (T_ANT, "Medium", "The word BARREN is the opposite of",
     "fertile", "dry", "empty", "harsh", "A",
     "Barren land bears nothing; fertile land bears much."),
    (T_IDM, "Medium", "Losing that contract turned out to be a blessing in disguise for the firm. This means the loss",
     "brought unexpected good fortune", "ruined the firm completely",
     "was celebrated by rivals", "was quickly forgotten", "A",
     "What looked like bad luck hid a benefit."),
    (T_IDM, "Medium", "The principal turned a deaf ear to the students' plea. This means he",
     "refused to listen to it", "listened to it carefully",
     "lost his hearing suddenly", "punished them for it", "A",
     "The plea fell on ears that chose not to hear."),
    (T_IDM, "Medium", "The school fees were paid at the eleventh hour. The fees were paid",
     "at the last possible moment", "eleven months in advance",
     "on the eleventh of the month", "in eleven instalments", "A",
     "The eleventh hour is the final minute before it is too late."),
    (T_IDM, "Medium", "With eight children, the widow could hardly make ends meet. This means she",
     "struggled to cover basic needs", "was extremely wealthy",
     "kept her money in the bank", "refused to work at all", "A",
     "Income and needs barely touch finger tips."),
    (T_IDM, "Hard", "The stadium the council built has become a white elephant. The stadium",
     "costs much but serves little use", "attracts many tourists",
     "houses a famous zoo", "makes huge profits yearly", "A",
     "A white elephant is a costly, useless burden."),
    (T_IDM, "Hard", "The senator pulled strings to get his nephew the job. This means the senator",
     "used his influence secretly", "pulled a rope at the office",
     "sat for the test himself", "advertised the vacancy", "A",
     "Quiet wires are pulled behind the scenes."),
    (T_COL, "Easy", "The new traffic law ___ effect last Friday.",
     "took", "made", "did", "put", "A",
     "Laws take effect; they do not make it."),
    (T_COL, "Easy", "The coach ___ objection to the referee's decision.",
     "raised", "spoke", "talked", "said", "A",
     "English raises an objection to a ruling."),
    (T_COL, "Medium", "The champions ___ defeat gracefully and shook hands.",
     "accepted", "received", "admitted", "allowed", "A",
     "Defeat is accepted, admitted only with shame."),
    (T_COL, "Easy", "The aircraft ___ off from the runway despite the harmattan haze.",
     "took", "flew", "went", "moved", "A",
     "A plane takes off; it never flies off."),
    (T_WMC, "Easy", "After lifting the trophy, the players were in high spirits. The players were",
     "cheerful", "drunk", "exhausted", "frightened", "A",
     "High spirits mean bright, joyful mood."),
    (T_WMC, "Hard", "Although he wears the crown, the king of the town is only a figurehead. The king",
     "rules only in name", "is greatly feared",
     "holds all real power", "was crowned last year", "A",
     "Another hand rules behind the crowned head."),
    (T_WMC, "Medium", "The auditor reported that the business was in the red. The business was",
     "running at a loss", "making large profits",
     "owing nothing to anyone", "closed by the bank", "A",
     "In the red is the debt side of the ledger."),
    (T_TEN, "Hard", "By this time next year, the masons ___ the new bridge.",
     "will have completed", "have completed",
     "will be completing it", "completed", "A",
     "The future perfect looks back from a future date."),
    (T_CON, "Hard", "Hardly had the thieves entered the bank ___ the alarm rang.",
     "when", "than", "that", "then", "A",
     "Hardly pairs with when; scarcely pairs with when too."),
    (T_SVA, "Medium", "The quality of the mangoes in the basket ___ poor.",
     "is", "are", "were", "have been", "A",
     "The head-noun is quality, not mangoes."),
    (T_CON, "Medium", "___ hard the boy tried, the knot would not loosen.",
     "However", "Although", "Whatever", "Whenever", "A",
     "However hard means no matter how hard."),
    (T_DET, "Medium", "___ of the two boys was given a prize.",
     "Each", "Both", "Every", "All", "A",
     "Each takes one of two, with a singular verb."),
    (T_PRE, "Medium", "The quarrel between the two traders stemmed ___ a minor debt.",
     "from", "of", "at", "with", "A",
     "Trouble stems from its root, never of it."),
    (T_VOW, "Medium", "The short vowel of the word 'cat' also appears in",
     "batch", "palm", "want", "major", "A",
     "The short a of cat rings in batch."),
    (T_VOW, "Medium", "The same short vowel heard in 'pot' occurs in",
     "bother", "sword", "food", "mute", "A",
     "The short o of pot lives in bother."),
    (T_VOW, "Hard", "The gliding sound that ends 'fire' is also heard in",
     "choir", "chair", "core", "car", "A",
     "Choir glides through the same fire sound."),
    (T_LET, "Medium", "Though the letter 'l' is written out, it is not pronounced at all in",
     "salmon", "melon", "lesson", "pillow", "A",
     "The l of salmon melts into the m."),
    (T_LET, "Hard", "The letter 'x' answers to the consonant /gz/ in the word",
     "exact", "axe", "next", "fox", "A",
     "Between vowels the x buzzes as gz."),
    (T_RHY, "Medium", "Pick the option that ends with the same sound as 'beard'.",
     "weird", "heard", "bear", "bead", "A",
     "Weird shares the beard's gliding sound."),
]

build_batch(
    S,
    "batch_173_neco_english5.json",
    "173",
    "NECO English round 5 (R32 top-up): synonyms diligent, dwindled, "
    "alleviated, candid, impartial; antonyms bold, generous, humble, "
    "ancient, barren; idioms blessing in disguise, deaf ear, "
    "eleventh hour, make ends meet, white elephant, pull strings; "
    "collocations took effect, raised objection, accepted defeat, "
    "took off; in-context high spirits, figurehead, in the red; "
    "future perfect, hardly-when, quality-of agreement, However "
    "hard, Each of the two, stemmed from; orals /ae/, /o/ short, "
    "silent l in salmon, x as /gz/, rhyme for beard, diphthong of "
    "fire. Scanned against NECO rounds 1-4, WAEC English (all "
    "rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
