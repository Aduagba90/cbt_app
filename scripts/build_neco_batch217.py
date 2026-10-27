"""Batch 217 - WAEC English round 7 (WAEC top-up, R43).

Grows WAEC English from 268 toward ~293 with angles not yet in
the bank: synonyms abortive, brittle, concise, eradicate,
feasible, grievous, immense, perilous, vivid; scenario antonyms
weary, mediocre, amicable, lengthy; idioms take after, keep body
and soul together, on the spur of the moment, red-letter day,
rainy day, up in arms; structure would rather, had better, put
off, run into; orals silent s in island, noun stress in record.
Scanned against the whole English pool (WAEC and NECO stems, 536
items).

    python3 scripts/build_neco_batch217.py -> content/batch_217_waec_english7.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "English"

T_SYN = "Lexis — Synonyms"
T_ANT = "Lexis — Antonyms"
T_IDM = "Lexis — Idioms"
T_STR = "Structure"
T_ORA = "Test of Orals"

PASSAGES = []
PQ = []

Q = [
    (T_SYN, "Medium", "All their attempts to repair the broken bridge proved ABORTIVE. ABORTIVE means",
     "unsuccessful", "expensive",
     "hasty", "secret", "A",
     "Nothing came of the effort."),
    (T_SYN, "Medium", "Old rubber bands become BRITTLE and snap easily. BRITTLE means",
     "easily broken", "soft and bent",
     "stretched far", "newly bought", "A",
     "Brittle things shatter at a touch."),
    (T_SYN, "Medium", "The examiner asked for a CONCISE summary of the passage. CONCISE means",
     "brief", "detailed",
     "spoken", "written out", "A",
     "Few words, all of them working."),
    (T_SYN, "Medium", "The new health campaign aims to ERADICATE malaria from the region. ERADICATE means",
     "wipe out completely", "reduce slightly",
     "study closely", "treat kindly", "A",
     "Not one case is to be left standing."),
    (T_SYN, "Medium", "The committee judged the plan FEASIBLE within the budget. FEASIBLE means",
     "practicable", "impossible",
     "costly", "popular", "A",
     "It can actually be carried out in practice."),
    (T_SYN, "Medium", "The flood caused GRIEVOUS damage to the farms. GRIEVOUS means",
     "very serious", "slight",
     "sudden", "expected", "A",
     "The loss cut deep into the farmers' season."),
    (T_SYN, "Medium", "The stadium was filled with an IMMENSE crowd. IMMENSE means",
     "huge", "noisy",
     "cheerful", "orderly", "A",
     "An immense sea of heads stretched to the gates."),
    (T_SYN, "Medium", "The road through the forest is PERILOUS at night. PERILOUS means",
     "dangerous", "narrow",
     "lonely", "muddy", "A",
     "Travellers risk their lives on it."),
    (T_SYN, "Medium", "The witness gave a VIVID account of the accident. VIVID means",
     "clear and lively", "doubtful",
     "short", "second-hand", "A",
     "The hearer could almost see it happen."),
    (T_ANT, "Medium", "After trekking for six hours under the sun, the farmers were WEARY. A word opposite in meaning to WEARY is",
     "energetic", "hungry",
     "sleepy", "worried", "A",
     "The weary have no strength left at all."),
    (T_ANT, "Medium", "Critics called the team's performance MEDIOCRE. A word opposite in meaning to MEDIOCRE is",
     "excellent", "delayed",
     "crowded", "friendly", "A",
     "Mediocre is neither poor nor praiseworthy."),
    (T_ANT, "Medium", "After months of quarrelling, the two chiefs finally reached an AMICABLE agreement. A word opposite in meaning to AMICABLE is",
     "hostile", "profitable",
     "written", "quick", "A",
     "Amicable talks are friendly talks."),
    (T_ANT, "Medium", "The chairman's opening remarks were LENGTHY. A word opposite in meaning to LENGTHY is",
     "brief", "formal",
     "amusing", "serious", "A",
     "The lengthy speech ran on and on."),
    (T_IDM, "Medium", "Everyone says Chidi TAKES AFTER his father. This means Chidi",
     "resembles his father", "obeys his father",
     "follows his father to work", "supports his father", "A",
     "The likeness shows in face and manner."),
    (T_IDM, "Hard", "With his tiny salary, the watchman could barely KEEP BODY AND SOUL TOGETHER. This means he could barely",
     "survive", "pay his rent",
     "feed his family", "keep his job", "A",
     "Life itself was hard to sustain."),
    (T_IDM, "Medium", "The family left the village ON THE SPUR OF THE MOMENT. This means they left",
     "suddenly, without planning", "late in the night",
     "after packing fully", "with their neighbours", "A",
     "The impulse alone moved them."),
    (T_IDM, "Medium", "The day she won the scholarship was a RED-LETTER DAY for Ada. This means it was",
     "a memorable day", "a sad day",
     "an ordinary work day", "a public holiday", "A",
     "Red ink marks the days worth remembering."),
    (T_IDM, "Medium", "The trader saves part of her profit every week FOR A RAINY DAY. This means she saves for",
     "a time of need", "the farming season",
     "her children's school fees", "her annual trip", "A",
     "The rainy day is the hard day that comes."),
    (T_IDM, "Medium", "The villagers were UP IN ARMS over the new tax. This means they were",
     "strongly protesting", "ready to fight a war",
     "collecting weapons", "silent and worried", "A",
     "Their anger stood up and shouted."),
    (T_STR, "Medium", "I would rather ___ at home than go out in this rain.",
     "stay", "to stay",
     "staying", "stayed", "A",
     "'Would rather' takes the bare infinitive."),
    (T_STR, "Medium", "You have been coughing for a week; you ___ see a doctor without delay.",
     "had better", "would rather",
     "must have", "should have", "A",
     "'Had better' gives strong advice."),
    (T_STR, "Medium", "The council has decided to ___ the ceremony until the rains are over.",
     "put off", "put on",
     "put up", "put in", "A",
     "The phrasal verb means to postpone."),
    (T_STR, "Medium", "At the market I ___ an old classmate I had not seen for ten years.",
     "ran into", "ran over",
     "ran through", "ran out", "A",
     "The meeting was quite by chance."),
    (T_ORA, "Easy", "The word 'island' contains a letter that is written but never pronounced. That letter is",
     "s", "l",
     "d", "a", "A",
     "The s lies silent inside the word."),
    (T_ORA, "Medium", "When 'record' is used as a noun, as in 'a record of sales', the strong stress falls on its",
     "first syllable", "second syllable",
     "final syllable", "consonant cluster", "A",
     "The verb reCORD becomes the noun RECord."),
]

build_batch(
    S,
    "batch_217_waec_english7.json",
    "217",
    "WAEC English round 7 (R43 top-up): synonyms abortive, "
    "brittle, concise, eradicate, feasible, grievous, immense, "
    "perilous, vivid; antonyms weary, mediocre, amicable, "
    "lengthy; idioms take after, keep body and soul together, on "
    "the spur of the moment, red-letter day, rainy day, up in "
    "arms; would rather, had better, put off, run into; orals "
    "silent s in island, noun stress in record. Scanned against "
    "the whole English pool (WAEC and NECO stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
