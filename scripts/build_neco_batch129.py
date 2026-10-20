"""Batch 129 - NECO Islamic Studies round 4 (NECO top-up, Round 24).

Lifts NECO IRS from 153 toward ~195 with angles not yet in any bank:
further muamalat (gharar, khiyar, ijarah, musharakah), zakat on
livestock nisab, kaffarah for broken fasts, hajj categories, the
companions' famous titles, the battles in order, prophets' trials, the
great mufassirun, the Year of the Elephant, Isra wal-Mi'raj, the
Abyssinia migration, the Madinah charter, the revealed books and the
angels' duties. Scanned against NECO rounds 1-3, WAEC IRS (all rounds)
and the JAMB pool.

    python3 scripts/build_neco_batch129.py -> content/batch_129_neco_irs4.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Islamic Studies"

T_MUAM = "Further Muamalat"
T_WOR = "Zakat, Sawm and Hajj Detail"
T_COMP = "The Companions and the Battles"
T_PROPH = "The Earlier Prophets"
T_REV = "Revelation Events and Books"
T_ANG = "Angels and the Unseen"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- muamalat
    (T_MUAM, "Hard", "Excessive uncertainty about the subject of a sale, forbidden in shariah, is called",
     "gharar", "mudarabah", "murabaha", "wakalah", "A",
     "A sale must be free of confusion."),
    (T_MUAM, "Hard", "The buyer's right to cancel a sale upon discovering a defect is",
     "khiyar al-ayb", "kharaj", "qisas", "ta'zir", "A",
     "Choice follows a hidden fault."),
    (T_MUAM, "Medium", "Ijarah, permitted in Islamic law, is a contract of",
     "hiring and leasing", "gambling", "usury", "inheritance", "A",
     "Services and use are rented."),
    (T_MUAM, "Hard", "Musharakah, a halal partnership, means partners",
     "share capital, work and profit", "sleep while one works", "hide losses from each other", "lend at interest", "A",
     "Both hands stir the business pot."),
    (T_MUAM, "Medium", "A riba-free bank earns mainly through",
     "trade and partnership profits", "fixed interest on loans", "penalties on the poor", "lottery tickets", "A",
     "Real trade replaces lending."),
    (T_MUAM, "Medium", "Honest weights and measures in trade are commanded in the Quranic story of Prophet",
     "Shu'aib", "Yunus", "Yahya", "Ilyas", "A",
     "His people of Madyan cheated scales."),

    # ------------------------------------------------------------- worship detail
    (T_WOR, "Hard", "The nisab for zakat on sheep is",
     "40 sheep", "20 sheep", "5 sheep", "100 sheep", "A",
     "Below that number nothing is due.", "40"),
    (T_WOR, "Hard", "The nisab for zakat on cattle is",
     "30 head", "40 head", "10 head", "5 head", "A",
     "Thirty cows start the duty.", "30"),
    (T_WOR, "Hard", "One who deliberately breaks a Ramadan fast without excuse owes, besides qada, an expiation called",
     "kaffarah", "sadaqah al-fitr only", "fidyah only", "udhiyah", "A",
     "Sixty poor are fed for it."),
    (T_WOR, "Medium", "Hajj performed together with umrah in one ihram is called",
     "qiran", "tamattu", "ifrad", "umrah al-sunnah", "A",
     "One state carries both rites."),
    (T_WOR, "Medium", "Tamattu means performing umrah, leaving ihram, and then starting hajj",
     "in the same season", "next year", "after ten years", "without ihram", "A",
     "The pilgrim enjoys a break between them."),
    (T_WOR, "Hard", "The farewell hajj led by the Prophet took place in the year",
     "10 AH", "8 AH", "6 AH", "11 AH", "A",
     "His last pilgrimage of all.", "10"),

    # ------------------------------------------------------------- companions and battles
    (T_COMP, "Medium", "Abu Bakr's famous honorific title, earned by his firm belief, is",
     "as-Siddiq", "al-Farouq", "Dhun-Nurayn", "Saifullah", "A",
     "The truthful one believed at once."),
    (T_COMP, "Medium", "Umar ibn al-Khattab is honoured with the title",
     "al-Farouq", "as-Siddiq", "Dhun-Nurayn", "al-Amin", "A",
     "He drew the line between truth and falsehood."),
    (T_COMP, "Hard", "Uthman ibn Affan was called Dhun-Nurayn because he married",
     "two daughters of the Prophet", "two queens of Persia", "two sisters of Ali", "no one at all", "A",
     "Two lights entered one house."),
    (T_COMP, "Hard", "The title Asadullah, lion of Allah, was given to",
     "Hamza", "Bilal", "Khalid", "Zubayr", "A",
     "The Prophet's uncle fell at Uhud."),
    (T_COMP, "Medium", "Badr, the first great battle, was fought in the year",
     "2 AH", "3 AH", "5 AH", "8 AH", "A",
     "Victory came in that Ramadan.", "2"),
    (T_COMP, "Medium", "The battle of the trench, al-Khandaq, came in the year",
     "5 AH", "3 AH", "2 AH", "7 AH", "A",
     "Ditches stopped the confederates.", "5"),
    (T_COMP, "Hard", "The truce signed at Hudaybiyyah in 6 AH was broken by the Quraysh, leading to the conquest of Makkah in",
     "8 AH", "7 AH", "9 AH", "10 AH", "A",
     "Ten thousand entered in peace.", "8"),
    (T_COMP, "Medium", "Khalid ibn al-Walid, once Islam's fiercest foe at Uhud, later earned the title",
     "Sayfullah, sword of Allah", "al-Farouq", "as-Siddiq", "Dhun-Nurayn", "A",
     "His sword served the faith he fought."),

    # ------------------------------------------------------------- earlier prophets
    (T_PROPH, "Medium", "Prophet Yusuf rose to high office in Egypt by interpreting the king's",
     "dreams", "letters", "laws", "maps", "A",
     "Seven lean cows devoured seven fat."),
    (T_PROPH, "Hard", "Prophet Ayyub is remembered chiefly for his",
     "patience in illness", "wealth alone", "army", "voyages", "A",
     "Years of trial never broke him."),
    (T_PROPH, "Medium", "Prophet Musa received the Torah on Mount",
     "Sinai (Tur)", "Carmel", "Nebo", "Gerizim", "A",
     "He fasted forty days there."),
    (T_PROPH, "Hard", "The prophet swallowed by a great fish after fleeing his mission was",
     "Yunus", "Yahya", "Zakariya", "Ilyas", "A",
     "Darkness within darkness taught him."),
    (T_PROPH, "Medium", "Prophet Ibrahim was thrown into fire by Namrud's order, and the fire",
     "became cool and safe", "consumed him", "spread to the city", "was quenched by rain", "A",
     "'We said: O fire, be cool'."),
    (T_PROPH, "Hard", "Isma'il, son of Ibrahim, is honoured for consenting to the sacrifice, and later for helping build the",
     "Ka'bah", "pyramids", "walls of Jericho", "temple at Jerusalem", "A",
     "Father and son raised its walls."),

    # ------------------------------------------------------------- revelation events and books
    (T_REV, "Medium", "The year the Prophet was born is called the Year of the",
     "Elephant", "Sword", "Camels", "Flood", "A",
     "Abraha's army perished with birds."),
    (T_REV, "Hard", "The night journey and ascension, Isra wal-Mi'raj, brought the command of",
     "the five daily prayers", "the hajj", "the zakat", "the fast", "A",
     "Fifty were eased to five."),
    (T_REV, "Medium", "The first hijrah of Muslims seeking refuge went to",
     "Abyssinia", "Madinah", "Ta'if", "Yemen", "A",
     "The just Negus sheltered them."),
    (T_REV, "Hard", "The charter the Prophet drew with the Madinan tribes is known as the",
     "Constitution of Madinah", "Treaty of Versailles", "Pact of Aqabah only", "Covenant of Hudaybiyyah", "A",
     "It governed Muslims, Jews and all."),
    (T_REV, "Medium", "The book revealed to Prophet Dawud is the",
     "Zabur", "Tawrat", "Injil", "Quran", "A",
     "Psalms of praise were given him."),
    (T_REV, "Medium", "The Injil was revealed to Prophet",
     "Isa", "Musa", "Ibrahim", "Nuh", "A",
     "It confirmed what came before."),
    (T_REV, "Hard", "The famous mufassir who wrote a complete commentary on the Quran, born in 701 AH's town of origin, is",
     "Ibn Kathir", "Ibn Khaldun", "Imam Ghazali", "Imam Nawawi", "A",
     "His tafsir is read worldwide."),

    # ------------------------------------------------------------- angels and the unseen
    (T_ANG, "Medium", "The angel assigned to take souls at death is",
     "Izra'il", "Jibril", "Mika'il", "Israfil", "A",
     "None escape his quiet summons."),
    (T_ANG, "Medium", "The angel entrusted with rain and provision is",
     "Mika'il", "Izra'il", "Israfil", "Malik", "A",
     "Nature's storehouse serves him."),
    (T_ANG, "Hard", "The two recording angels seated on each person's right and left are called",
     "kiraman katibin", "munkar nakir", "harut marut", "malikayn al-ard", "A",
     "One writes good, one writes ill."),
    (T_ANG, "Medium", "The angel who guards the gate of hell is",
     "Malik", "Ridwan", "Israfil", "Mika'il", "A",
     "He awaits the appointed day."),
    (T_ANG, "Medium", "Belief in the unseen, including angels and the last day, is described in the Quran as a mark of the",
     "righteous (muttaqin)", "hypocrites", "disbelievers", "travellers", "A",
     "Surah al-Baqarah opens with them."),
    (T_ANG, "Hard", "The questioning of the grave is carried out by the angels",
     "Munkar and Nakir", "Jibril and Mika'il", "Israfil and Malik", "Harut and Marut", "A",
     "Three questions meet the soul."),
]

build_batch(
    S,
    "batch_129_neco_irs4.json",
    "129",
    "NECO Islamic Studies round 4 (Round 24 top-up): gharar, khiyar "
    "al-ayb, ijarah, musharakah, halal banking, Shu'aib's scales, sheep "
    "nisab 40, cattle nisab 30, kaffarah, qiran vs tamattu, farewell "
    "hajj 10 AH, Abu Bakr as-Siddiq, Umar al-Farouq, Uthman "
    "Dhun-Nurayn, Hamza Asadullah, Badr 2 AH, Khandaq 5 AH, Makkah's "
    "fall 8 AH, Khalid the sword of Allah, Yusuf's dreams, Ayyub's "
    "patience, Musa at Sinai, Yunus and the fish, Ibrahim's cool fire, "
    "Isma'il and the Ka'bah, Year of the Elephant, Isra wal-Mi'raj and "
    "the five prayers, Abyssinia's Negus, the Constitution of Madinah, "
    "Zabur and Injil, Ibn Kathir's tafsir, Izra'il, Mika'il, the "
    "recording kiraman katibin, Malik of hell, the muttaqin's unseen and "
    "Munkar-Nakir. Scanned against NECO rounds 1-3, WAEC IRS (all "
    "rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
