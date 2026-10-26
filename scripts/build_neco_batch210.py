"""Batch 210 - NECO English round 6 (NECO top-up, R42).

Grows NECO English from 243 toward ~268 with angles not yet in
the bank: synonyms (lucid, meagre, naive, obstinate, placid,
prudent, sluggish, zealous); antonyms (callous, consent,
optional, superior); idioms (at daggers drawn, let sleeping dogs
lie, pull my leg, throw in the towel, tighten our belts);
structure (third conditional, wish + past perfect, high time +
past, among, unless); orals with unique phrasings (silent b in
comb, verb stress in increase, ch in chemistry). Scanned against
the whole English pool (WAEC and NECO stems, 511 items).

    python3 scripts/build_neco_batch210.py -> content/batch_210_neco_english6.json
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
    (T_SYN, "Medium", "The nurse gave a LUCID account of how the accident happened. LUCID means",
     "clear", "doubtful",
     "lengthy", "quiet", "A",
     "A lucid account is easily followed."),
    (T_SYN, "Medium", "Farmers harvested a MEAGRE crop after the poor rains. MEAGRE means",
     "scanty", "plentiful",
     "healthy", "early", "A",
     "A meagre harvest barely fills a basket."),
    (T_SYN, "Medium", "The NAIVE young man believed every promise the trickster made. NAIVE means",
     "unsuspecting", "careless",
     "clever", "stubborn", "A",
     "Inexperience left him an easy prey."),
    (T_SYN, "Medium", "The child was OBSTINATE and refused to take his medicine. OBSTINATE means",
     "stubborn", "obedient",
     "grateful", "fearful", "A",
     "No pleading could move him."),
    (T_SYN, "Medium", "The PLACID waters of the lake reflected the evening sky. PLACID means",
     "calm", "rough",
     "shallow", "muddy", "A",
     "Not a ripple disturbed the surface."),
    (T_SYN, "Medium", "A PRUDENT housewife buys foodstuff in bulk when prices are low. PRUDENT means",
     "wise and careful", "proud and distant",
     "quick-tempered", "over-generous", "A",
     "She plans today for tomorrow's pot."),
    (T_SYN, "Medium", "The old engine made a SLUGGISH start on the cold morning. SLUGGISH means",
     "slow", "noisy",
     "sudden", "smooth", "A",
     "It coughed before it crawled."),
    (T_SYN, "Medium", "The ZEALOUS youth leader cleaned the whole church compound alone. ZEALOUS means",
     "passionate", "gentle",
     "reluctant", "cheerless", "A",
     "His fire for the work never cooled."),
    (T_ANT, "Medium", "The chief was so CALLOUS that he ignored the widow's cries. The opposite of CALLOUS is",
     "kind-hearted", "brave-hearted",
     "hard-working", "high-minded", "A",
     "The callous feel no pity at all."),
    (T_ANT, "Medium", "The elders CONSENTED to the building of the new market. The opposite of CONSENTED is",
     "objected", "agreed at once",
     "postponed it", "prayed over it", "A",
     "To consent is to say yes; the opposite refuses."),
    (T_ANT, "Medium", "Attendance at the tutorial is OPTIONAL. The opposite of OPTIONAL is",
     "compulsory", "occasional",
     "morning-only", "free of charge", "A",
     "You may skip what is optional; the other you must attend."),
    (T_ANT, "Medium", "The principal's office is SUPERIOR to the clerk's in rank. The opposite of SUPERIOR is",
     "inferior", "senior",
     "equal always", "modern", "A",
     "Rank climbs up or steps down."),
    (T_IDM, "Medium", "The two co-tenants have been AT DAGGERS DRAWN since the water dispute. This means they are",
     "openly hostile to each other", "secretly in agreement",
     "very close friends", "afraid of each other", "A",
     "Their quarrel is ready for the blade."),
    (T_IDM, "Medium", "The new headmaster decided to LET SLEEPING DOGS LIE. This means he",
     "avoided stirring up old quarrels", "sent the troublesome boys away",
     "locked the school gates early", "forgave every offender at once", "A",
     "Some troubles are best left undisturbed."),
    (T_IDM, "Easy", "When Tola said she had won a lottery, I thought she was PULLING MY LEG. This means I thought she was",
     "teasing me", "insulting me",
     "praising me", "helping me", "A",
     "A leg-puller plays a joke, not a trick for gain."),
    (T_IDM, "Medium", "After failing the paper twice, Bode THREW IN THE TOWEL. This means Bode",
     "gave up the struggle", "washed his kit",
     "sat the paper again", "prayed for help", "A",
     "The fighter's towel flies into the ring in surrender."),
    (T_IDM, "Medium", "With food prices rising, the family has had to TIGHTEN ITS BELT. This means the family has",
     "cut down its spending", "bought new clothes",
     "sold its car", "borrowed money", "A",
     "A tighter belt survives a leaner purse."),
    (T_STR, "Hard", "If I had known you were coming, I ___ a room for you.",
     "would have prepared", "would prepare",
     "will prepare", "prepared", "A",
     "The closed past condition takes the perfect conditional."),
    (T_STR, "Hard", "I wish I ___ harder for last year's examination.",
     "had studied", "studied",
     "would study", "have studied", "A",
     "Regret over the past calls for the past perfect."),
    (T_STR, "Hard", "It is high time the government ___ the inner roads.",
     "repaired", "repairs",
     "will repair", "has repaired", "A",
     "'High time' is followed by the simple past."),
    (T_STR, "Medium", "The teacher shared the oranges ___ the ten pupils who came first.",
     "among", "between",
     "in", "across", "A",
     "'Among' serves three or more; 'between' serves two."),
    (T_STR, "Medium", "You will certainly miss the bus unless you ___ at once.",
     "leave", "will leave",
     "left", "would leave", "A",
     "'Unless' keeps the present simple after it."),
    (T_ORA, "Easy", "The word 'comb' ends with a letter that is never pronounced. That letter is",
     "b", "e",
     "m", "o", "A",
     "The b lies silent at the end."),
    (T_ORA, "Medium", "When 'increase' is used as a verb rather than a noun, the strong stress falls on its",
     "second syllable", "first syllable",
     "third syllable", "final consonant", "A",
     "The noun INcrease becomes the verb inCREASE."),
    (T_ORA, "Hard", "The 'ch' at the beginning of 'chemistry' carries exactly the same sound as the 'ch' in",
     "stomach", "church",
     "chef", "machine", "A",
     "Both hide the hard /k/ sound."),
]

build_batch(
    S,
    "batch_210_neco_english6.json",
    "210",
    "NECO English round 6 (R42 top-up): synonyms lucid, meagre, "
    "naive, obstinate, placid, prudent, sluggish, zealous; "
    "antonyms callous, consented, optional, superior; idioms at "
    "daggers drawn, let sleeping dogs lie, pull my leg, throw in "
    "the towel, tighten one's belt; third conditional, wish + past "
    "perfect, high time + past, among vs between, unless + "
    "present; orals - silent b in comb, verb stress in increase, "
    "ch in chemistry vs stomach. Scanned against the whole English "
    "pool (WAEC and NECO stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
