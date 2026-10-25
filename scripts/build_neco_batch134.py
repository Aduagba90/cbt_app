"""Batch 134 - WAEC Islamic Studies round 5 (WAEC top-up, Round 25).

Lifts WAEC IRS from 158 toward ~196 with angles not yet in any bank:
asbab al-nuzul, Makki surahs, Zayd ibn Thabit's first compilation;
isnad vs matn, sahih/da'if grades, al-Muwatta of Imam Malik; ijma and
qiyas, the Hanafi eponym, Maliki dominance in Nigeria's north;
tayammum conditions, ghusl occasions, the four wudu obligations;
jumu'ah replacing zuhr, qiblah as a condition, iqamah, janazah's
structure; traveller's fast deferral, i'tikaf, suhur; zakat al-fitr,
the eight asnaf, gold nisab 85 grams; Arafat on 9 Dhul-Hijjah, seven
pebbles, ihram restrictions, tawaf al-ifadah; Aminah, Halimah,
Khadijah, Abu Talib, Fatimah; Quba, the Ansar and the mu'akhah
brotherhood. Scanned against WAEC rounds 1-4, NECO IRS (all rounds)
and the JAMB pool.

    python3 scripts/build_neco_batch134.py -> content/batch_134_waec_irs5.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Islamic Studies"

T_QUR = "Ulum al-Quran"
T_HAD = "Hadith Science"
T_FIQH = "Fiqh and Its Sources"
T_TAH = "Taharah Further"
T_SAL = "Salah Further"
T_SIYAM = "Fasting Further"
T_ZAK = "Zakat and Sadaqah Further"
T_HAJJ = "Hajj Further"
T_SEERAH = "The Prophet's Household and Early Life"
T_MAD = "Madinan Institutions"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- ulum al-quran
    (T_QUR, "Hard", "The circumstances that occasioned the revelation of a verse are called",
     "asbab al-nuzul", "naskh", "muhkam", "tanzil", "A",
     "Every verse has its moment."),
    (T_QUR, "Medium", "Surahs revealed before the migration to Madinah are described as",
     "Makki", "Madani", "Mathani", "Mufassal", "A",
     "They came down in Makkah's years."),
    (T_QUR, "Medium", "Makki surahs chiefly dwell on",
     "tawhid and the last day", "detailed trade laws", "inheritance shares", "battlefield strategy", "A",
     "Faith first, law followed later."),
    (T_QUR, "Hard", "The scribe who led the first compilation of the Quran under Abu Bakr was",
     "Zayd ibn Thabit", "Umar ibn al-Khattab", "Ali ibn Abi Talib", "Uthman ibn Affan", "A",
     "He gathered the leaves with care."),

    # ------------------------------------------------------------- hadith
    (T_HAD, "Medium", "The chain of transmitters through which a hadith reaches us is its",
     "isnad", "matn", "sahih", "da'if", "A",
     "Names carry the report down."),
    (T_HAD, "Medium", "The actual wording or content of a hadith is called its",
     "matn", "isnad", "riwayah", "ijma", "A",
     "The text itself is the matn."),
    (T_HAD, "Hard", "The collection Muslims rank most rigorously authentic is",
     "Sahih al-Bukhari", "Sunan Abu Dawud", "Muwatta Malik", "Musnad Ahmad", "A",
     "Its tests were the strictest."),
    (T_HAD, "Medium", "A hadith failing the tests of authenticity is graded",
     "da'if", "sahih", "hasan", "mashhur", "A",
     "A weak chain weakens the word."),
    (T_HAD, "Hard", "The early collection known as al-Muwatta was compiled by",
     "Imam Malik", "Imam Bukhari", "Imam Muslim", "Imam Tirmidhi", "A",
     "Madinah's imam wrote it first."),

    # ------------------------------------------------------------- fiqh
    (T_FIQH, "Medium", "Agreement of qualified scholars on a matter of law is",
     "ijma", "qiyas", "ijtihad", "taqlid", "A",
     "One voice of the learned settles it."),
    (T_FIQH, "Hard", "Extending a known ruling to a new similar case by analogy is",
     "qiyas", "ijma", "ijtihad", "taqlid", "A",
     "Like cases are judged alike."),
    (T_FIQH, "Medium", "The Hanafi school of law takes its name from",
     "Abu Hanifah", "Malik ibn Anas", "Muhammad al-Shafi'i", "Ahmad ibn Hanbal", "A",
     "The school wears its teacher's name."),
    (T_FIQH, "Hard", "The school of law dominant in Nigeria's far north follows",
     "Imam Malik", "Imam Shafi'i", "Imam Abu Hanifah", "Imam Ahmad", "A",
     "Madinah's way crossed the Sahara."),

    # ------------------------------------------------------------- taharah
    (T_TAH, "Hard", "Tayammum becomes lawful when water is",
     "unavailable or harmful", "cheap and close by", "warm and plentiful", "bought from vendors", "A",
     "Earth answers when water cannot."),
    (T_TAH, "Medium", "A full ritual bath, ghusl, becomes due after",
     "marital relations", "cutting the nails", "deep sleep at night", "removing the shoes", "A",
     "Major impurity needs full washing."),
    (T_TAH, "Medium", "The number of compulsory acts in wudu is",
     "4", "3", "5", "6", "A",
     "Face, arms, head and feet.", "4"),

    # ------------------------------------------------------------- salah
    (T_SAL, "Medium", "On Fridays, the congregational jumu'ah prayer takes the place of",
     "zuhr", "fajr", "asr", "maghrib", "A",
     "Midday becomes the great gathering."),
    (T_SAL, "Hard", "Which of these is a condition for a valid salah?",
     "facing the qiblah", "eating a full meal", "washing the shoes", "counting the rows", "A",
     "Direction binds every worshipper."),
    (T_SAL, "Medium", "The second, shorter call made just before the prayer begins is the",
     "iqamah", "adhan", "talbiyah", "du'a", "A",
     "It rises when rows are filled."),
    (T_SAL, "Hard", "Salat al-janazah differs from other prayers because it contains",
     "no bowing or prostration", "extra prostrations", "five prostrations", "long silent qiyam", "A",
     "Standing takbirs carry it through."),

    # ------------------------------------------------------------- fasting
    (T_SIYAM, "Medium", "A traveller on a hard journey during Ramadan may",
     "defer it to later days", "abandon it entirely", "fast half a day only", "send money instead", "A",
     "The debt of days is repaid later."),
    (T_SIYAM, "Hard", "Devout seclusion in the mosque during the last ten nights of Ramadan is",
     "i'tikaf", "ihsan", "ijma", "istikharah", "A",
     "The mosque becomes home and hearth."),
    (T_SIYAM, "Medium", "The meal taken before dawn to prepare for the fast is",
     "suhur", "iftar", "walimah", "sadaqah", "A",
     "Blessed eating before the light."),

    # ------------------------------------------------------------- zakat
    (T_ZAK, "Medium", "The charity every Muslim household pays out before the Eid al-Fitr prayer is",
     "zakat al-fitr", "zakat al-mal", "kaffarah", "fidyah", "A",
     "It buys the poor a festival meal."),
    (T_ZAK, "Hard", "Which pair is among the eight heads of zakat spending?",
     "the poor and the needy", "kings and their guards", "mosque builders only", "the rich and the proud", "A",
     "The Quran names them clearly."),
    (T_ZAK, "Hard", "Zakat becomes due on gold once it reaches",
     "85 grams", "50 grams", "100 grams", "200 grams", "A",
     "Twenty dinars of old measure.", "85"),

    # ------------------------------------------------------------- hajj
    (T_HAJJ, "Medium", "The great standing of hajj at Arafat falls on",
     "9 Dhul-Hijjah", "1 Dhul-Hijjah", "10 Dhul-Hijjah", "13 Dhul-Hijjah", "A",
     "Hajj is Arafat, as the saying runs.", "9"),
    (T_HAJJ, "Hard", "Each of the jamrah pillars is stoned with",
     "7 pebbles", "3 pebbles", "10 pebbles", "20 pebbles", "A",
     "Seven stones, seven declarations.", "7"),
    (T_HAJJ, "Medium", "A male pilgrim in the state of ihram is barred from putting on",
     "stitched clothes", "leather sandals", "an umbrella", "a ring", "A",
     "Two unsown sheets are his dress."),
    (T_HAJJ, "Hard", "The main tawaf of hajj, tawaf al-ifadah, is performed",
     "on the day of sacrifice", "before leaving home", "during the ihram only", "after returning home", "A",
     "It follows the Arafat standing."),

    # ------------------------------------------------------------- seerah
    (T_SEERAH, "Medium", "The mother of the Prophet was",
     "Aminah bint Wahb", "Halimah as-Sa'diyyah", "Khadijah bint Khuwaylid", "Fatimah bint Asad", "A",
     "She nursed him before her early death."),
    (T_SEERAH, "Medium", "The Bedouin wet nurse who nursed the young Muhammad in the desert was",
     "Halimah", "Aminah", "Khadijah", "Fatimah", "A",
     "Desert air made him strong."),
    (T_SEERAH, "Medium", "The noble widow the Prophet married at twenty-five was",
     "Khadijah", "Aisha", "Hafsah", "Zaynab", "A",
     "She traded with him, then trusted him."),
    (T_SEERAH, "Hard", "After Abdul-Muttalib died, the young Prophet was protected by his uncle",
     "Abu Talib", "Abu Lahab", "Hamza", "Abbas", "A",
     "He shielded him though he stayed unblessed."),
    (T_SEERAH, "Medium", "The Prophet's youngest and most famous daughter was",
     "Fatimah", "Zaynab", "Ruqayyah", "Umm Kulthum", "A",
     "She was the mother of Hasan and Husayn."),

    # ------------------------------------------------------------- madinah
    (T_MAD, "Medium", "The first mosque in Islam was built at",
     "Quba", "Mina", "Arafat", "Makkah", "A",
     "It rose on the road into Madinah."),
    (T_MAD, "Medium", "The Madinan helpers who housed the Makkan migrants were the",
     "Ansar", "Muhajirun", "Munafiqun", "Quraysh", "A",
     "They shared their homes and farms."),
    (T_MAD, "Hard", "The Prophet's pact pairing each migrant with a Madinan brother is known as",
     "mu'akhah", "bay'ah", "hilf", "wala'", "A",
     "Brotherhood was sworn, not born."),
]

build_batch(
    S,
    "batch_134_waec_irs5.json",
    "134",
    "WAEC Islamic Studies round 5 (Round 25 top-up): asbab al-nuzul, "
    "Makki surah themes, Zayd ibn Thabit's compilation; isnad, matn, "
    "Sahih al-Bukhari, da'if grade, al-Muwatta of Imam Malik; ijma, "
    "qiyas, Abu Hanifah's school, Maliki north; tayammum when water "
    "fails, ghusl after marital relations, 4 wudu obligations; jumu'ah "
    "replacing zuhr, qiblah condition, iqamah, janazah without ruku or "
    "sujud; traveller's deferral, i'tikaf, suhur; zakat al-fitr, the "
    "poor and needy among the asnaf, gold nisab 85 grams; Arafat on 9 "
    "Dhul-Hijjah, 7 pebbles per jamrah, no sewn garments in ihram, "
    "tawaf al-ifadah on the day of sacrifice; Aminah bint Wahb, "
    "Halimah, Khadijah, Abu Talib, Fatimah; Quba mosque, the Ansar, "
    "mu'akhah brotherhood. Scanned against WAEC rounds 1-4, NECO IRS "
    "(all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
