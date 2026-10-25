"""Batch 166 - WAEC Islamic Studies round 6 (WAEC top-up, R31).

Grows WAEC IRS from 196 toward ~233 with angles not yet in the bank:
why revelation came gradually; what Makkan surahs dwell on; asbab
al-nuzul, tafsir, tajwid; hadith grades sahih and mawdu'; why the
Sunnah follows the Qur'an; Ar-Rahman, Israfil, the recording angels,
the Tawrat; sujud as-sahw, khushu', the iqamah; Ramadan as the month
of the Qur'an; zakah as purifier; hajj's conditions and ihram months;
al-Amin, the Negus of Abyssinia, Umar's open prayer, the Sahifah of
Madinah, mu'akhah, Quba, Yarmuk; Bilal the first muezzin; the fitnah
after Uthman; maisir, ihtikar, bribery, tampered scales, mothers;
Usman dan Fodio; the lunar year's eleven days; fiqh, ijma', qiyas.
Scanned against WAEC rounds 1-5, NECO IRS (all rounds) and the JAMB
pool.

    python3 scripts/build_neco_batch166.py -> content/batch_166_waec_irs6.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Islamic Studies"

T_QUR = "Ulum al-Quran"
T_HAD = "Hadith Science"
T_AQD = "Tawhid and the Articles of Faith"
T_SLH = "Ibadah: Taharah and Salah"
T_ZSW = "Zakah and Sawm"
T_HAJ = "Hajj and Umrah"
T_SIR = "Sirah"
T_KHL = "The Khulafa"
T_MUA = "Muamalat and Islamic Ethics"
T_NIG = "Islam in Nigeria"
T_CAL = "Family Life and the Islamic Calendar"
T_FIQ = "Fiqh and Its Sources"

PASSAGES = []
PQ = []

Q = [
    (T_QUR, "Medium", "The Qur'an was revealed bit by bit over twenty-three years chiefly so that",
     "the hearers could absorb and live each teaching", "the Prophet would not tire of writing",
     "the pagans might copy it slowly", "it could rival the Torah in length", "A",
     "Fresh verses answered real events as they came."),
    (T_QUR, "Easy", "The surahs revealed before the Hijrah keep returning to",
     "shares of inheritance", "Allah's oneness and the Last Day",
     "terms of trade contracts", "duties owed under treaties", "B",
     "Makkan verses first build faith in one Allah."),
    (T_QUR, "Hard", "The reports recording the events that occasioned a verse's sending down are studied under",
     "ahkam al-khamsah", "qawa'id al-fiqh", "asbab al-nuzul", "ilm al-kalam", "C",
     "Knowing the occasion guards against misreading."),
    (T_QUR, "Easy", "The science of explaining the meanings of the Qur'an is called",
     "tafsir", "tajwid", "ta'rikh", "tawhid", "A",
     "Tafsir unfolds what the verses truly mean."),
    (T_QUR, "Easy", "The rules guarding right and beautiful recitation of the Qur'an are gathered under",
     "fiqh", "usul al-din", "balaghah", "tajwid", "D",
     "Tajwid keeps every letter in its proper sound."),
    (T_HAD, "Medium", "A hadith whose chain of narrators is unbroken and trustworthy is graded",
     "da'if", "sahih", "mawdu'", "gharib", "B",
     "Unbroken reliable chains carry sound reports."),
    (T_HAD, "Medium", "A report invented and falsely tied to the Prophet is labelled",
     "hasan", "mutawatir", "mawdu'", "sahih", "C",
     "Fabrications are rejected outright."),
    (T_HAD, "Easy", "After the Qur'an, the Sunnah stands as the next source of law because it",
     "shows how the Qur'an is lived out", "may overrule the Qur'an at will",
     "replaces the Qur'an where they differ", "adds new gods beside Allah", "A",
     "The Prophet's practice is the Book in action."),
    (T_AQD, "Easy", "Of Allah's beautiful names, Ar-Rahman describes Him as",
     "the All-Knowing", "the Self-Sufficient", "the Most Merciful", "the Swift in Reckoning", "C",
     "His mercy embraces every creature."),
    (T_AQD, "Medium", "The angel charged with blowing the trumpet on the Last Day is",
     "Mikail", "Israfil", "Izra'il", "Malik", "B",
     "One blast ends the world; a second raises it."),
    (T_AQD, "Medium", "The two angels seated on each shoulder, writing down a person's deeds, are called",
     "kiraman katibin", "munkar and nakir", "harut and marut", "the bearers of the Throne", "A",
     "Not a word is left unrecorded."),
    (T_AQD, "Easy", "The holy book revealed to Prophet Musa is the",
     "Injil", "Zabur", "Suhuf", "Tawrat", "D",
     "Each messenger carried Allah's word; Musa's is the Tawrat."),
    (T_SLH, "Medium", "Extra prostrations performed to repair a mistake made inside the prayer are called",
     "sajdat at-tilawah", "sujud as-sahw", "sujud ash-shukr", "the ruku' of the funeral prayer", "B",
     "Forgetting in prayer has a built-in repair."),
    (T_SLH, "Easy", "Standing in salah with humble, attentive stillness of heart is called",
     "khushu'", "riya'", "kibr", "ghaflah", "A",
     "The spirit of prayer is presence with Allah."),
    (T_SLH, "Easy", "Immediately before the congregational prayer begins, the caller stands up and makes the",
     "du'a after salah", "takbir al-ihram", "adhan for fajr", "iqamah", "D",
     "The iqamah is the adhan's shorter companion."),
    (T_ZSW, "Easy", "The month of Ramadan holds its special place because",
     "Hajj is performed in that same month", "it closes the Islamic year",
     "the Qur'an began coming down in it", "it is the coldest month", "C",
     "Ramadan honours the Book's first descent."),
    (T_ZSW, "Medium", "Besides relieving the poor, zakah is meant to cleanse the giver of",
     "fear of poverty", "greed and clinging love of wealth",
     "hunger during the fasts", "the love of being praised by people", "B",
     "Parting with wealth washes greed away."),
    (T_HAJ, "Medium", "Hajj becomes obligatory on a Muslim who is adult, sane and",
     "over seventy years of age", "already making a fifth visit",
     "able to meet the journey's cost", "keeping a full year of fasts", "C",
     "Maturity, sense and means open the duty."),
    (T_HAJ, "Hard", "Ihram for hajj is validly entered only in Shawwal, Dhul-Qa'dah and",
     "the first ten days of Dhul-Hijjah", "Muharram, the sacred month",
     "Rajab, another sacred month", "Safar, the month of journeys", "A",
     "The season is fixed by the shariah."),
    (T_SIR, "Easy", "Long before prophethood, the Makkans handed Muhammad their goods for safekeeping and called him",
     "al-Hakam, the judge", "al-Aziz, the mighty", "al-Ghani, the rich", "al-Amin, the trustworthy", "D",
     "His truthfulness won every deposit."),
    (T_SIR, "Medium", "The early Muslims who fled persecution first crossed to Abyssinia, then ruled by",
     "Caesar of Rome", "the Negus, Ashama", "Chosroes of Persia", "the Pharaoh of Egypt", "B",
     "The Negus heard the refugees justly."),
    (T_SIR, "Medium", "The small Muslim community first dared to pray openly near the Ka'bah after",
     "Umar had embraced Islam", "Abu Lahab had died",
     "Hamzah had left Makkah", "Bilal had been freed", "A",
     "Umar's boldness shielded the praying ranks."),
    (T_SIR, "Hard", "Soon after reaching Madinah, the Prophet drew up the charter governing Muslims and the Jewish tribes. That document is the",
     "Covenant of Ta'if, written later", "Pledges of Aqabah before the Hijrah",
     "Constitution (Sahifah) of Madinah", "Treaty of Hudaybiyyah with the Makkans", "C",
     "One city, several communities, one charter."),
    (T_SIR, "Hard", "On arriving in Madinah, the Prophet paired each Makkan migrant with a Madinan host in the bond of brotherhood called",
     "hilf al-fudul", "mu'akhah", "bay'ah of Aqabah", "mawaddah", "B",
     "Muhajir and Ansar stood as brothers."),
    (T_SIR, "Medium", "On the outskirts of Madinah, the Prophet raised the walls of his first mosque at",
     "Quba", "Ta'if", "Badr", "Khaybar", "A",
     "Quba's walls rose before Madinah's own."),
    (T_SIR, "Hard", "In Umar's caliphate, Roman power in Syria was broken at the battle of",
     "Qadisiyyah", "Mu'tah", "Hattin", "Yarmuk", "D",
     "Yarmuk opened Syria's gates to Islam."),
    (T_KHL, "Easy", "The first muezzin of Islam, who called the adhan from atop the Ka'bah after Makkah's fall, was",
     "Zayd ibn Harithah", "Salman al-Farisi", "Bilal ibn Rabah", "Ammar ibn Yasir", "C",
     "His voice rose above the sacred House."),
    (T_KHL, "Medium", "The first civil war among the Muslims broke out after the murder of the caliph",
     "Umar", "Uthman", "Ali", "Abu Bakr", "B",
     "Uthman's killing tore the community."),
    (T_MUA, "Medium", "Staking money on games of chance is forbidden in the Qur'an under the name",
     "maisir", "mudarabah", "musaqah", "muzara'ah", "A",
     "Chance devours wealth without honest work."),
    (T_MUA, "Hard", "A grain merchant who corners the market and stores the grain to resell it dearer commits",
     "sharikah, lawful partnership", "ribh, normal profit",
     "amanah, a trust", "ihtikar, unlawful hoarding", "D",
     "Hiding food while people hunger is sin."),
    (T_MUA, "Easy", "A contractor who slips money to a customs officer to overlook his goods is guilty of",
     "sadaqah given early", "bribery, which is haram",
     "a lawful gift between friends", "zakat paid in advance", "B",
     "A bribe buys injustice for everyone."),
    (T_MUA, "Easy", "In the market verses, Allah warns traders who cheat their buyers by tampering with",
     "shop locations", "prayer times", "weights and measures", "market days", "C",
     "Short scales draw out long punishment."),
    (T_MUA, "Easy", "The Prophet taught that paradise lies beneath the feet of",
     "fathers", "mothers", "scholars", "the wealthy", "B",
     "A mother's service opens her child's way."),
    (T_NIG, "Medium", "The jihad that created the Sokoto Caliphate in the nineteenth century was led by",
     "Usman dan Fodio", "Muhammad al-Amin al-Kanemi", "Samori Toure", "Ahmadu Bello", "A",
     "The Shehu's scholars and riders built Sokoto."),
    (T_CAL, "Easy", "Because it follows the moon, the Islamic year is about",
     "eleven days longer than the solar year", "exactly the same length",
     "six months shorter", "eleven days shorter than the solar year", "D",
     "So Ramadan turns through every season."),
    (T_FIQ, "Medium", "The Islamic science that draws practical rulings from the Qur'an and Sunnah is",
     "nahw, grammar", "fiqh", "kalam, theology", "sarf, word formation", "B",
     "Fiqh turns revelation into daily living."),
    (T_FIQ, "Hard", "When the qualified scholars of an age agree upon one ruling, their agreement is called",
     "ijma'", "qiyas", "ijtihad", "istihsan", "A",
     "Consensus stands beside Book and Sunnah."),
    (T_FIQ, "Hard", "Settling a new matter by comparing it with a case already decided in the shariah is",
     "taqlid, following a scholar", "talfiq, patchwork of views", "qiyas", "istishab", "C",
     "Analogy carries known law to new cases."),
]

build_batch(
    S,
    "batch_166_waec_irs6.json",
    "166",
    "WAEC Islamic Studies round 6 (R31 top-up): gradual revelation and "
    "Makkan themes; asbab al-nuzul, tafsir, tajwid; sahih and mawdu' "
    "grades; Sunnah after the Qur'an; Ar-Rahman, Israfil, kiraman "
    "katibin, Tawrat; sujud as-sahw, khushu', iqamah; Ramadan and the "
    "Qur'an, zakah as cleanser; hajj conditions and ihram months; "
    "al-Amin, Negus of Abyssinia, Umar's open prayer, Sahifah of "
    "Madinah, mu'akhah, Quba, Yarmuk; Bilal first muezzin; fitnah "
    "after Uthman; maisir, ihtikar, bribery, tampered scales, mothers; "
    "Usman dan Fodio and Sokoto; lunar year's eleven days; fiqh, "
    "ijma', qiyas. Scanned against WAEC rounds 1-5, NECO IRS (all "
    "rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
