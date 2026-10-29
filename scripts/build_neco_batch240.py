"""Batch 240 - NECO English round 6 (NECO top-up, R49).

Grows NECO English from 268 toward ~293 with angles verified absent
from the whole English pool (561 items across JAMB, WAEC and NECO,
the smallest pool scanned this round - the pool is the union of all
three exams' English). Fresh: synonyms COMMENCE, LUCRATIVE,
DORMANT; antonyms AGILE, GREGARIOUS, ABOLISH; idioms spill the
beans, make hay while the sun shines, beat about the bush, took to
his heels, break the ice; collocations heavy rain, make progress;
word meaning NOVICE, VETERAN; tenses present perfect continuous,
past perfect continuous; preposition insists on; determiner fewer;
passive transformation; orals: vowel pain/reign, stress
CONGRATULATIONS and DEMOCRACY, rhyme weight/freight, homophone
sun/son. Avoided as banked: every classic found in the pool -
midnight oil, piece of cake, nail on head, sleeping dogs, blessing
in disguise, under the weather, blue moon, arm and a leg, daggers
drawn, white elephant, red-letter, towel, body and soul, up in
arms, square peg; words meticulous/frugal/resilient/scarce/
hostile/overjoyed/obsolete/prudent/placid/meagre/robust/vacant/
benevolent/candid/diligent; tense items with will-have/by-next-
year, each-of, the-news, mathematics-SVA, one-of-the-boys, no-
sooner, hardly-had, so-that, due-to/despite; conjunctions family;
superior-to antonym; congratulate-on; good-at; stress
UNDERSTAND/PHOTOGRAPHER; PH pronunciation; rhyme families
caught/taught, night/light, house/mouse, fire/tire, city/pretty,
silly/billy, peach/beach, book/look, came/name, heart/start, BITE/
height; vowel families sheep-seat, chief, truth, idea, ear, work;
tags (have I); watchman; map legend; option-level isoline, Congo
basin, Kalahari, Atlas, Mississippi, Mate's receipt; hole as
distractor.

    python3 scripts/build_neco_batch240.py -> content/batch_240_neco_eng6.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "English"

T_SYN = "Lexis — Synonyms"
T_ANT = "Lexis — Antonyms"
T_ID = "Lexis — Idioms & Figurative Language"
T_COL = "Lexis — Collocations & Usage"
T_CTX = "Lexis — Word Meaning in Context"
T_TEN = "Structure — Tense & Aspect"
T_PREP = "Structure — Prepositions"
T_DET = "Structure — Determiners & Pronouns"
T_WOT = "Structure — Word Order & Transformation"
T_VOW = "Test of Orals — Vowels and Diphthongs"
T_STR = "Test of Orals — Stress"
T_RHY = "Test of Orals — Rhymes"
T_HOM = "Test of Orals — Homophones"

PASSAGES = []
PQ = []

Q = [
    (T_SYN, "Easy", "The new manager decided to COMMENCE trading on the first of the month. A word closest in meaning to COMMENCE is",
     "begin", "close",
     "delay", "cancel", "A",
     "To commence is simply to begin."),
    (T_SYN, "Medium", "Transport business between the two markets proved highly LUCRATIVE for the young trader. LUCRATIVE means",
     "profitable", "dangerous",
     "costly", "lawful", "A",
     "Money comes home from a lucrative trade."),
    (T_SYN, "Medium", "The seeds lie DORMANT in the dry soil until the rains return. DORMANT means",
     "inactive", "dead",
     "active", "rotten", "A",
     "Sleeping, but alive and waiting."),
    (T_ANT, "Medium", "The AGILE athlete leaped over the hurdles with ease. A word opposite in meaning to AGILE is",
     "clumsy", "swift",
     "quick", "nimble", "A",
     "Where the agile leaps, the clumsy stumbles."),
    (T_ANT, "Hard", "Chike is a GREGARIOUS young man who never eats lunch alone. A word opposite in meaning to GREGARIOUS is",
     "unsociable", "cheerful",
     "friendly", "popular", "A",
     "The sociable seek company; his opposite shuns it."),
    (T_ANT, "Medium", "The new government decided to ABOLISH the old levy. A word opposite in meaning to ABOLISH is",
     "establish", "cancel",
     "destroy", "forbid", "A",
     "What is abolished is wiped away; its opposite is set up."),
    (T_ID, "Easy", "The little boy could not keep the secret; he SPILLED THE BEANS before the party. This means that he",
     "revealed the secret", "cooked the beans",
     "spilled the soup", "kept quiet", "A",
     "The beans of the matter poured out of his mouth."),
    (T_ID, "Medium", "Ada decided to MAKE HAY WHILE THE SUN SHONE by selling her yams while prices were high. This means that she",
     "used her opportunity in time", "became a farmer",
     "waited for the rains", "wasted the sunshine", "A",
     "Dry the grass while the weather agrees."),
    (T_ID, "Easy", "The candidate BEAT ABOUT THE BUSH for ten minutes before admitting that he had failed. This means that he",
     "avoided the main point", "tended the garden",
     "spoke plainly", "quarrelled openly", "A",
     "He circled the matter without touching it."),
    (T_ID, "Easy", "When the robbers were spotted, the thief TOOK TO HIS HEELS. This means that he",
     "ran away at once", "removed his shoes",
     "surrendered", "stood still", "A",
     "The heels did the talking."),
    (T_ID, "Medium", "The chairman told a funny story at the start of the meeting to BREAK THE ICE. This means that he",
     "eased the tension", "dropped a block",
     "ended the meeting", "insulted the guests", "A",
     "The first smile melts the frozen room."),
    (T_COL, "Easy", "The farmers were happy because the rainy season brought ____ rain that filled their wells.",
     "heavy", "strong",
     "big", "powerful", "A",
     "English rain is heavy, never strong."),
    (T_COL, "Medium", "After months of steady practice, the choir began to ____ progress in their singing.",
     "make", "do",
     "take", "give", "A",
     "Progress is made, not done."),
    (T_CTX, "Easy", "Being a NOVICE on the job, Uche asked his senior colleagues to show him the way. A NOVICE is",
     "a beginner", "an expert",
     "a supervisor", "a visitor", "A",
     "New to the work, still learning the ropes."),
    (T_CTX, "Medium", "The VETERAN teacher could calm the noisiest class with a single look. A VETERAN is",
     "an experienced person", "a retired soldier only",
     "a new recruit", "a strict disciplinarian", "A",
     "Long years on the job have taught her every trick."),
    (T_TEN, "Medium", "The pupils ____ for the inter-house sports since six o'clock this morning, and the races have not begun.",
     "have been waiting", "are waiting",
     "were waited", "have waited to", "A",
     "It started at six and continues now."),
    (T_TEN, "Hard", "By the time the help finally arrived, the farmers ____ in the sun for three hours.",
     "had been working", "have been working",
     "are working", "will be working", "A",
     "Three hours passed before the help came."),
    (T_PREP, "Medium", "The workers' union insists ____ a pay rise before the unions call off the strike.",
     "on", "for",
     "at", "with", "A",
     "To insist takes 'on', never 'for'."),
    (T_DET, "Medium", "There were ____ students at the morning assembly than the principal expected.",
     "fewer", "less",
     "little", "much", "A",
     "Students can be counted; so 'fewer' is the word."),
    (T_WOT, "Easy", "The play 'The Lion and the Jewel' ____ by Wole Soyinka.",
     "was written", "wrote",
     "has written", "is writing", "A",
     "The play receives the writing; it does not do it."),
    (T_VOW, "Medium", "The 'ai' in 'pain' carries exactly the same vowel sound as the letters 'ei' in one of these words. Which one?",
     "reign", "pine",
     "pin", "said", "A",
     "Rain, reign and pain share one sound."),
    (T_STR, "Medium", "In the word CONGRATULATIONS, the primary stress falls on the",
     "second syllable", "first syllable",
     "third syllable", "fourth syllable", "A",
     "The voice lifts on the second beat: con-GRAT-u-la-tions."),
    (T_STR, "Medium", "In the word DEMOCRACY, the primary stress falls on the",
     "second syllable", "first syllable",
     "third syllable", "fourth syllable", "A",
     "de-MOC-ra-cy — the voice rises on the second beat."),
    (T_RHY, "Easy", "One of these words ends with exactly the same sounds as 'weight', so that the two make a perfect rhyme. It is",
     "freight", "height",
     "width", "gateau", "A",
     "Weight and freight ride in the same sounding wagon."),
    (T_HOM, "Easy", "When spoken aloud, 'sun' sounds exactly like one other word in English, though their spellings differ. That word is",
     "son", "soon",
     "sin", "song", "A",
     "The star and the child answer to one sound."),
]

build_batch(
    S,
    "batch_240_neco_eng6.json",
    "240",
    "NECO English round 6 (R49 top-up): synonyms commence, "
    "lucrative, dormant; antonyms agile, gregarious, abolish; "
    "idioms spill the beans, make hay while the sun shone, beat "
    "about the bush, took to his heels, break the ice; collocations "
    "heavy rain, make progress; word meaning novice, veteran; "
    "tenses present perfect continuous, past perfect continuous; "
    "preposition insists on; determiner fewer; passive "
    "transformation; orals vowel pain/reign, stress "
    "CONGRATULATIONS, DEMOCRACY, rhyme weight/freight, homophone "
    "sun/son. Scanned against the whole English pool (JAMB, WAEC "
    "and NECO stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
