"""Batch 097 - WAEC Islamic Studies round 2 (WAEC lift, Round 19).

WAEC Islamic Studies Paper 1 draws 50 items; the bank stood at 62. This
lift adds fresh items - janazah, qiblah from Nigeria, tayammum, ghusl,
zakat al-fitr and asnaf, fidyah, miqat, jamarat, umrah, talbiyah, ihram
rules, sacrifice, Umm al-Kitab, ayat, isnad, tawhid categories, riya,
istighfar, tawbah, Halimah, Abdul Muttalib, Year of the Elephant, Black
Stone, Ta'if, Isra wal-Mi'raj, ridda wars, Hijri calendar, mudarabah,
full measure, hasad, Tijaniyyah - scanned against WAEC r1, NECO rounds
1-2 and the JAMB banks.

    python3 scripts/build_neco_batch97.py -> content/batch_097_waec_irs2.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Islamic Studies"

T_IBA = "Ibadat"
T_QUR = "The Qur'an and Hadith"
T_AQI = "Aqidah"
T_SEE = "Sirah"
T_KHU = "The Khulafa"
T_MUA = "Muamalat and Ethics"
T_NIG = "Islam in Nigeria"

PASSAGES = []
PQ = []

Q = [
    # ---------------------------------------------------------------- ibadat
    (T_IBA, "Hard", "Salat al-janazah, the funeral prayer, is unique because it contains no",
     "ruku or sujud", "du'a for the dead", "takbir at all", "standing position", "A",
     "It is offered standing with four takbirs."),
    (T_IBA, "Medium", "Muslims in Nigeria face the north-east in prayer because the Ka'bah lies",
     "north-east of Nigeria", "due north of Nigeria", "north-west of Nigeria", "east of Nigeria", "A",
     "The qiblah from Nigeria is the north-east."),
    (T_IBA, "Medium", "When no water is available or one is ill, wudu is replaced by",
     "tayammum with clean earth", "ghusl with sand water", "salah without purification", "two extra rak'ahs", "A",
     "Clean dust serves the purpose."),
    (T_IBA, "Medium", "The full-body purification required after marital relations is",
     "ghusl", "wudu", "tayammum", "istinja", "A",
     "Nothing less than the full bath."),
    (T_IBA, "Medium", "The charity of food given to the poor before the Eid al-Fitr prayer is",
     "zakat al-fitr", "zakat al-mal", "sadaqat al-fitr", "kaffarah", "A",
     "No Eid prayer passes before it."),
    (T_IBA, "Hard", "The eight groups of people entitled to receive zakat are collectively called the",
     "asnaf", "fuqaha", "khummas", "ahl al-dhimmah", "A",
     "The Qur'an lists them eight."),
    (T_IBA, "Hard", "The feeding of a poor person in place of a fast one cannot keep is called",
     "fidyah", "qada'", "kaffarah", "i'tikaf", "A",
     "The weak are fed instead."),
    (T_IBA, "Hard", "The fixed stations beyond which a pilgrim may not pass without ihram are the",
     "miqat", "masar", "mawaqit al-salah", "maqam Ibrahim", "A",
     "Five stations ring the Haram."),
    (T_IBA, "Hard", "Casting pebbles at the three pillars in Mina during Hajj is called",
     "rami al-jamarat", "sa'y", "tawaf", "wuquf", "A",
     "The pebbles recall Ibrahim's stand."),
    (T_IBA, "Medium", "The lesser pilgrimage that can be performed at any time of year is",
     "umrah", "hajj", "ziyarah", "tawaf al-wada", "A",
     "Umrah is the lesser visit."),
    (T_IBA, "Medium", "The pilgrim's cry of 'Labbayk Allahumma Labbayk' is known as the",
     "talbiyah", "takbir", "tahlil", "tasbih", "A",
     "The answer to the call is Labbayk."),
    (T_IBA, "Medium", "While in ihram, a male pilgrim may NOT",
     "cut his hair or nails", "drink cold water", "walk in the shade", "eat cooked food", "A",
     "Even a hair waits till release."),
    (T_IBA, "Medium", "The Eid sacrifice commemorates the willingness of",
     "Ibrahim to sacrifice his son", "Musa to cross the sea", "Yusuf to forgive his brothers", "Isa to endure hardship", "A",
     "The ram replaced the boy."),
    (T_IBA, "Hard", "The meat of the Eid sacrifice is customarily shared into",
     "three parts", "two equal parts", "five parts", "seven parts", "A",
     "Home, relatives and the poor share."),
    # ---------------------------------------------------------------- qur'an and hadith
    (T_QUR, "Medium", "Al-Fatihah is also known as Umm al-Kitab, meaning",
     "the mother of the Book", "the gate of the Book", "the end of the Book", "the light of the Book", "A",
     "The whole Book sums in it."),
    (T_QUR, "Easy", "A single verse of the Qur'an is called an",
     "ayah", "surah", "sajdah", "juz", "A",
     "Ayah means a sign and a verse."),
    (T_QUR, "Hard", "In hadith science, the chain of narrators is called the",
     "isnad", "matn", "sahih", "da'if", "A",
     "The chain carries the text."),
    (T_QUR, "Medium", "The companions of the Prophet who transmitted his reports are called the",
     "sahabah", "tabi'un", "salaf", "huffaz", "A",
     "They saw and handed on the sunnah."),
    # ---------------------------------------------------------------- aqidah
    (T_AQI, "Hard", "Scholars divide tawhid into lordship, worship and",
     "names and attributes", "fear and hope", "law and ethics", "faith and works", "A",
     "Three branches complete tawhid."),
    (T_AQI, "Hard", "Doing good deeds only to be seen by people is the minor shirk called",
     "riya'", "nifaq", "kufr", "bid'ah", "A",
     "Showing off hollows worship."),
    (T_AQI, "Medium", "Seeking Allah's forgiveness for one's sins is called",
     "istighfar", "istikharah", "istikbara", "inabah", "A",
     "The tongue repeats 'Astaghfirullah'."),
    (T_AQI, "Medium", "Returning to Allah with sincere regret and abandoning the sin is",
     "tawbah", "tamattu'", "tawaf", "taqsir", "A",
     "Repentance mends the bond."),
    (T_AQI, "Medium", "Belief in Allah's foreknowledge of all things brings a believer",
     "patience in hardship", "fear of the future alone", "reliance on charms", "contempt for planning", "A",
     "What Allah wrote cannot undo him."),
    # ---------------------------------------------------------------- sirah
    (T_SEE, "Hard", "The Prophet's foster mother who nursed him in the desert was",
     "Halimah", "Aminah", "Fatimah", "Khadijah", "A",
     "Banu Sa'd nursed him in the desert."),
    (T_SEE, "Hard", "After his mother Aminah died, the young Muhammad was cared for by his grandfather",
     "Abdul Muttalib", "Abu Talib", "Hamzah", "Abbas", "A",
     "The old chief loved him dearly."),
    (T_SEE, "Medium", "The Prophet was born in the year of the elephant, which was",
     "570 CE", "610 CE", "622 CE", "632 CE", "A",
     "Abraha's failed march named the year."),
    (T_SEE, "Hard", "Before prophethood, Muhammad settled a dispute over the Black Stone by",
     "having all clans lift a cloak together", "drawing lots among the elders", "buying it with his wealth", "letting the oldest clan place it", "A",
     "Wisdom averted a clan war."),
    (T_SEE, "Medium", "At Ta'if, the Prophet was rejected and",
     "stoned by the town's youth", "crowned by its chiefs", "given a house and land", "married into its nobility", "A",
     "He left bleeding but patient."),
    (T_SEE, "Hard", "The night journey to Jerusalem and ascent through the heavens is called",
     "al-Isra wal-Mi'raj", "al-Hijrah", "al-Fath", "al-Fil", "A",
     "Jerusalem was the midway station."),
    (T_SEE, "Medium", "The Prophet's last military expedition, against the Romans, was to",
     "Tabuk", "Khaybar", "Uhud", "Hunayn", "A",
     "The northern march tested faith."),
    (T_SEE, "Medium", "The Prophet died in 632 CE, which was the year",
     "11 AH", "10 AH", "13 AH", "6 AH", "A",
     "Eleven years after the Hijrah."),
    # ---------------------------------------------------------------- khulafa
    (T_KHU, "Hard", "Abu Bakr's caliphate was consumed by campaigns against the",
     "apostate tribes in Arabia", "Persian empire first", "Roman empire first", "Berber tribes of the west", "A",
     "The ridda wars held Arabia."),
    (T_KHU, "Hard", "The Hijri calendar was introduced under the caliphate of",
     "Umar", "Abu Bakr", "Uthman", "Ali", "A",
     "Umar ordered the years counted."),
    (T_KHU, "Medium", "Ali, the fourth caliph, moved his capital from Madinah to",
     "Kufah", "Damascus", "Makkah", "Basra", "A",
     "Kufah in Iraq hosted him."),
    # ---------------------------------------------------------------- muamalat and ethics
    (T_MUA, "Hard", "A partnership in which one partner gives capital and the other labour is",
     "mudarabah", "musharakah", "murabahah", "muzara'ah", "A",
     "Capital and toil share profit."),
    (T_MUA, "Medium", "The Qur'an commands merchants to",
     "give full measure and weight", "hide defects in goods", "take the largest profit", "swear oaths to close sales", "A",
     "Short measure invited destruction."),
    (T_MUA, "Medium", "Envying others their blessings is the spiritual disease of",
     "hasad", "hirs", "bukhl", "ghadab", "A",
     "Envy eats goodness as fire eats wood."),
    (T_MUA, "Easy", "Spreading tales to set friends against one another is",
     "namimah", "najwah", "nasiha", "nikah", "A",
     "Tale-bearing breaks homes."),
    (T_MUA, "Medium", "Animals slaughtered without invoking Allah's name are",
     "haram to eat", "halal to eat", "mubah", "makruh only", "A",
     "The name of Allah sanctifies meat."),
    # ---------------------------------------------------------------- nigeria
    (T_NIG, "Medium", "Besides the Qadiriyyah, the other Sufi order widespread in Nigeria is the",
     "Tijaniyyah", "Shadhiliyyah", "Naqshbandiyyah", "Chishtiyyah", "A",
     "It spread widely from the nineteenth century."),
    (T_NIG, "Medium", "Some northern states enlarged the role of Sharia courts in",
     "1999 to 2000", "1914 to 1915", "1960 to 1961", "1983 to 1984", "A",
     "The reforms began after 1999."),
    (T_NIG, "Easy", "The Eid congregational prayer is commonly held in",
     "an open prayer ground", "the market square stall", "the emir's bedroom", "inside private homes only", "A",
     "The musalla takes the crowd."),
]

build_batch(
    S,
    "batch_097_waec_irs2.json",
    "097",
    "WAEC IRS round 2 (Round 19 lift): janazah without ruku, Nigeria's "
    "north-east qiblah, tayammum, ghusl, zakat al-fitr, asnaf, fidyah, "
    "miqat, rami al-jamarat, umrah, talbiyah, ihram prohibitions, Eid "
    "sacrifice and its three shares, Umm al-Kitab, ayah, isnad, sahabah, "
    "tawhid's three branches, riya, istighfar, tawbah, trust in qadar, "
    "Halimah, Abdul Muttalib, 570 CE, Black Stone arbitration, Ta'if, "
    "Isra wal-Mi'raj, Tabuk, 11 AH, ridda campaigns, Hijri calendar under "
    "Umar, Ali's Kufah, mudarabah, full measure, hasad, namimah, "
    "slaughter in Allah's name, Tijaniyyah, Sharia courts 1999-2000, Eid "
    "ground. Scanned against WAEC r1, NECO rounds 1-2 and the JAMB banks.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
