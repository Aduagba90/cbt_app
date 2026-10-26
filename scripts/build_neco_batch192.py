"""Batch 192 - WAEC Islamic Studies round 7 (WAEC top-up, R37).

Grows WAEC Islamic Studies from 234 toward ~261 with angles not
yet in the bank: the Prophet's work as shepherd and trader; his
marriage to Khadijah; Ali the first youth to accept Islam; his
death in 11 AH; the first qiblah of Jerusalem; Mikail; the
ninety-nine beautiful names; shirk; mahr; talaq; iddah; the
justice condition on four wives; the Qadiriyya order of dan
Fodio; tayammum; Bilal the first muezzin; sa'y; the stoning at
Mina; umrah at any time; nikah; sadaqah; the poor first in the
zakat list; ihram restrictions; the Constitution of Madinah;
Jumu'ah in place of Zuhr; Zamzam; the traveller's deferred fast;
Zakat al-Fitr before the Eid prayer. Scanned against the whole
Islamic Studies pool (WAEC and NECO stems, 461 items).

    python3 scripts/build_neco_batch192.py -> content/batch_192_waec_irs7.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Islamic Studies"

T_SIR = "The Life of the Prophet (Sirah)"
T_SAH = "The Companions"
T_TAW = "At-Tawhid and the Articles of Faith"
T_IBD = "Ibadat — Salat"
T_HAJ = "Hajj and Umrah"
T_FAS = "Sawm and Zakat"
T_MUA = "Muamalat — Marriage and Divorce"
T_NIG = "Islam in Nigeria"

PASSAGES = []
PQ = []

Q = [
    (T_SIR, "Easy", "Before he began to receive revelation, the Prophet (S.A.W.) earned his living as a",
     "shepherd and trader", "soldier and smith",
     "farmer and scribe", "physician of Makkah", "A",
     "He kept flocks as a boy, then led caravans."),
    (T_SIR, "Medium", "The wealthy Makkah widow whom the Prophet (S.A.W.) married, and who remained his only wife while she lived, was",
     "Khadijah", "Aisha",
     "Hafsat", "Zaynab", "A",
     "She was also the first to believe his message."),
    (T_SIR, "Hard", "The first youth to embrace Islam was",
     "Ali ibn Abi Talib", "Zayd ibn Harithah",
     "Usamah ibn Zayd", "Abdullah ibn Umar", "A",
     "He was a boy being raised in the Prophet's house."),
    (T_SIR, "Hard", "After his death, the Prophet (S.A.W.) was laid to rest in the room of his wife",
     "Aisha", "Khadijah",
     "Hafsat", "Sawdah", "A",
     "Madinah's mosque grew around his resting place."),
    (T_SIR, "Hard", "The document the Prophet drew up in Madinah to govern relations between the Muslims, the Jews and other communities is known as the",
     "Constitution of Madinah", "Treaty of Hudaybiyyah",
     "Charter of Makkah", "Pledge of Aqabah", "A",
     "It set out duties and rights for every group."),
    (T_IBD, "Medium", "For some months after the hijrah the Muslims prayed facing a city other than Makkah. That first qiblah was",
     "Jerusalem", "Damascus",
     "Ta'if", "Yemen", "A",
     "The command to turn to the Ka'bah came later."),
    (T_IBD, "Medium", "The Jumu'ah prayer of Friday is held in place of which of the five daily prayers?",
     "Zuhr", "Asr",
     "Fajr", "Maghrib", "A",
     "The midday prayer becomes the Friday congregation."),
    (T_IBD, "Medium", "When no water can be found, a Muslim may purify for prayer with clean earth in place of wudu. This is called",
     "tayammum", "ghusl",
     "janabah", "wudu of dust", "A",
     "Clean dust lawfully stands in for water."),
    (T_HAJ, "Hard", "The rite of sa'y honours the woman who ran between Safa and Marwah searching for water for her son. She was",
     "Hajar", "Amina",
     "Halima", "Fatimah", "A",
     "Her running is re-enacted by every pilgrim."),
    (T_HAJ, "Hard", "The pebbles a pilgrim throws at the pillars in Mina recall the stand of",
     "Ibrahim (A.S.) against temptation", "Musa (A.S.) at the sea",
     "Nuh (A.S.) in the flood", "Yusuf (A.S.) in prison", "A",
     "Each throw repeats his rejection of the tempter."),
    (T_HAJ, "Medium", "The lesser pilgrimage, which may be performed at any season of the year, is",
     "umrah", "hajj",
     "tamattu", "iqram", "A",
     "It omits the great standing at Arafat."),
    (T_HAJ, "Hard", "While in the state of ihram, a pilgrim is forbidden to",
     "cut his hair and nails", "drink Zamzam water",
     "sleep in a tent", "greet his family", "A",
     "The state of consecration leaves him untrimmed."),
    (T_FAS, "Medium", "Islam gives ease to the sick and the traveller in Ramadan by allowing them to",
     "repay the missed fast later", "skip fasting forever",
     "fast only half days", "pay others to fast", "A",
     "Allah intends ease, not hardship."),
    (T_FAS, "Medium", "Zakat al-Fitr should reach the poor",
     "before the Eid prayer", "after the Eid prayer",
     "on the night of Eid", "at the next Ramadan", "A",
     "It arrives in time for the festival feast."),
    (T_FAS, "Hard", "Of the eight groups the Qur'an names as entitled to zakat, the first two are",
     "the poor and the needy", "wayfarers and debtors",
     "slaves and officials", "new Muslims and scholars", "A",
     "The fuqara and the masakin head the list."),
    (T_FAS, "Easy", "A voluntary act of charity given freely at any time, beside the compulsory zakat, is called",
     "sadaqah", "mahr",
     "kaffarah", "fidyah", "A",
     "Every good gift to a neighbour counts as sadaqah."),
    (T_MUA, "Medium", "The marriage contract by which a man and a woman are lawfully joined in Islam is the",
     "nikah", "talaq",
     "khul", "mahr", "A",
     "Consent and witnesses seal the contract."),
    (T_MUA, "Easy", "The gift of money or goods which a groom settles on his bride under the marriage contract is the",
     "mahr", "sadaqah",
     "hadiyyah", "riba", "A",
     "It belongs to the wife alone, not her family."),
    (T_MUA, "Hard", "The form of divorce that lies in the hands of the husband is called",
     "talaq", "khul",
     "li'an", "zihar", "A",
     "It is lawful but disliked, and follows set steps."),
    (T_MUA, "Hard", "The waiting period a woman must observe after divorce or widowhood before she may remarry is the",
     "iddah", "talaq",
     "hijab", "aqqiqah", "A",
     "It establishes certainty before a new union."),
    (T_MUA, "Medium", "A Muslim man may marry up to four wives on one strict condition: that he",
     "deals justly with all of them", "is wealthy beyond measure",
     "obtains the ruler's consent", "weds them in one day", "A",
     "Justice is the hinge of plural marriage."),
    (T_TAW, "Hard", "Besides Jibril who brought the revelation, the angel Allah charged with sending down the rain is",
     "Mikail (A.S.)", "Israfil (A.S.)",
     "Izra'il (A.S.)", "Malik (A.S.)", "A",
     "Jibril brings the word; Mikail brings the rain."),
    (T_TAW, "Medium", "The beautiful names of Allah, of which Ar-Rahman is often called the greatest, number",
     "99", "40",
     "70", "100", "A",
     "To Him belong the most beautiful names.", "99"),
    (T_TAW, "Hard", "Associating partners with Allah, which Islam counts the gravest of all sins, is called",
     "shirk", "nifaq",
     "kufr of pride", "bid'ah", "A",
     "No sin is weighed heavier than this."),
    (T_SAH, "Medium", "The companion, once a slave of Abyssinia, whom the Prophet chose as the first muezzin, was",
     "Bilal ibn Rabah", "Zayd ibn Thabit",
     "Salman al-Farisi", "Suhayb ar-Rumi", "A",
     "His ringing voice gave the first call to prayer."),
    (T_SIR, "Easy", "The sacred well that gushed forth for Hajar and her son Ismail in the valley of Makkah is",
     "Zamzam", "Silwan",
     "Marwah spring", "Arafat well", "A",
     "Its water is drawn by pilgrims to this day."),
    (T_NIG, "Medium", "The Sufi order to which Shaykh Usman dan Fodio belonged is the",
     "Qadiriyya", "Tijaniyya",
     "Muridiyya", "Shadhiliyya", "A",
     "It traces its line to Shaykh Abdul-Qadir al-Jilani."),
]

build_batch(
    S,
    "batch_192_waec_irs7.json",
    "192",
    "WAEC Islamic Studies round 7 (R37 top-up): shepherd-and-trader "
    "years; Khadijah the first wife; Ali the first youth; death in "
    "11 AH; Constitution of Madinah; Jerusalem the first qiblah; "
    "Jumu'ah replacing Zuhr; tayammum; sa'y between Safa and "
    "Marwah; the pebbles of Mina; umrah in any season; ihram "
    "restrictions; the traveller's deferred fast; Zakat al-Fitr "
    "before Eid prayer; the poor and needy first in the zakat "
    "list; sadaqah; nikah; mahr; talaq; iddah; the justice "
    "condition on four wives; Mikail; the ninety-nine names; "
    "shirk; Bilal the first muezzin; Zamzam; the Qadiriyya of dan "
    "Fodio. Scanned against the whole Islamic Studies pool (WAEC "
    "and NECO stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
