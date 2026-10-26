"""Batch 196 - NECO Islamic Studies round 7 (NECO top-up, R38).

Grows NECO Islamic Studies from 227 toward ~253 with angles not
yet in the bank: Malik the guardian of Hell; the Bridge (Sirat);
the Scale (Mizan); the People of the Cave; Yunus and the great
fish; Nuh's ark; Ibrahim the Friend of Allah; Sulaiman and the
ant; Sumayyah the first martyr; Mus'ab the first teacher of
Madinah; four rak'ahs in Isha; the opening takbir; the tashahhud;
suhur; iftar; niyyah; the farewell tawaf; Al-Amin; Abu Talib the
protector; Hamza; the Negus of Abyssinia; Tabuk; Khaybar; the
recording angels; ushr on crops; the Black Stone. Scanned against
the whole Islamic Studies pool (WAEC and NECO stems, 488 items).

    python3 scripts/build_neco_batch196.py -> content/batch_196_neco_irs7.json
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
T_SAW = "Sawm and Zakat"
T_HAJ = "Hajj and Umrah"
T_PRO = "The Prophets"

PASSAGES = []
PQ = []

Q = [
    (T_TAW, "Hard", "The angel appointed by Allah to guard the gate of Hellfire is",
     "Malik (A.S.)", "Mikail (A.S.)",
     "Israfil (A.S.)", "Jibril (A.S.)", "A",
     "He keeps the keepers of the fire."),
    (T_TAW, "Hard", "On the Day of Judgement, every soul must cross the narrow pathway stretched over Hell. It is called",
     "the Sirat", "the Mizan",
     "the Kawthar", "the Barzakh", "A",
     "Only the upright cross it in safety."),
    (T_TAW, "Hard", "The scale on which the good and bad deeds of mankind will be weighed on the Last Day is the",
     "Mizan", "Sirat",
     "Minbar", "Mahshar", "A",
     "Not an atom's weight is lost."),
    (T_TAW, "Hard", "The young believers who fled persecution and slept for many years in a cave, as the Qur'an relates, are known as",
     "the People of the Cave", "the Companions of the Ditch",
     "the Seven Sleepers of Yemen", "the Men of the Cave of Thawr", "A",
     "Surah al-Kahf opens their story."),
    (T_TAW, "Medium", "The record of every person's deeds, kept by the attendant angels, will be given out on the Day of Judgement as",
     "a book of deeds", "a scale of weight",
     "a lamp of light", "a sealed cup", "A",
     "The two scribes never left his side."),
    (T_PRO, "Medium", "The prophet who was swallowed by a great fish after leaving his people in anger was",
     "Yunus (A.S.)", "Yahya (A.S.)",
     "Ilyas (A.S.)", "Idris (A.S.)", "A",
     "He cried out from the belly of the fish."),
    (T_PRO, "Easy", "The prophet who built a great ark to save the faithful from the flood was",
     "Nuh (A.S.)", "Hud (A.S.)",
     "Salih (A.S.)", "Lut (A.S.)", "A",
     "The animals entered two by two."),
    (T_PRO, "Medium", "The prophet honoured with the title Khalilullah, the Friend of Allah, is",
     "Ibrahim (A.S.)", "Musa (A.S.)",
     "Isa (A.S.)", "Dawud (A.S.)", "A",
     "The friend of Allah broke the idols."),
    (T_PRO, "Hard", "The prophet who understood the speech of the ant and the hoopoe was",
     "Sulaiman (A.S.)", "Yusuf (A.S.)",
     "Yaqub (A.S.)", "Harun (A.S.)", "A",
     "He ruled over men and jinn alike."),
    (T_SIR, "Medium", "Before his call to prophethood, the people of Makkah trusted the young Muhammad (S.A.W.) so deeply that they called him",
     "Al-Amin, the trustworthy", "Al-Faruq, the discerner",
     "As-Siddiq, the verifier", "Dhun-Nurayn, the two lights", "A",
     "Even his rivals left their goods with him."),
    (T_SIR, "Medium", "The uncle who stood by the Prophet (S.A.W.) and shielded him from the Quraysh until his death was",
     "Abu Talib", "Abu Lahab",
     "Hamza only in war", "Al-Abbas", "A",
     "His protection bought Islam its early years."),
    (T_SIR, "Hard", "The Muslim emigrants who fled to Abyssinia were received and protected by its just king,",
     "the Negus (Najashi)", "the Byzantine emperor",
     "the Persian king", "the king of Egypt", "A",
     "He wept at the recitation of the Qur'an."),
    (T_SIR, "Hard", "The expedition of Tabuk is remembered as the last campaign the Prophet (S.A.W.) led in person, marched against",
     "the Romans", "the Persians",
     "the Hawazin", "the Jews of Khaybar", "A",
     "The long march to the Syrian border."),
    (T_SIR, "Hard", "The fortress town north of Madinah whose strongholds fell to the Muslims in 7 AH was",
     "Khaybar", "Tabuk",
     "Ta'if", "Hunayn", "A",
     "Its fields of palm became the Muslims'."),
    (T_SAH, "Hard", "The first person to be killed for the sake of Islam, a woman steadfast under torture, was",
     "Sumayyah", "Khadijah",
     "Fatimah", "Aisha", "A",
     "She died under the spears of Quraysh."),
    (T_SAH, "Hard", "The companion the Prophet sent to Madinah as its first teacher of Islam, before the hijrah, was",
     "Mus'ab ibn Umayr", "Abu Ubaydah",
     "Sa'd ibn Abi Waqqas", "Abdur-Rahman ibn Awf", "A",
     "The first envoy of Islam taught the Ansar."),
    (T_SAH, "Medium", "Hamzah ibn Abdul-Muttalib, martyred at Uhud, is honoured with the title",
     "Sayyid ash-Shuhada, master of martyrs", "Asadullah reborn, twice lion of Allah",
     "the Sword of Allah drawn", "the Interpreter of the Qur'an", "A",
     "The lion of Allah fell in the valley."),
    (T_IBD, "Medium", "Four obligatory rak'ahs are observed in which of the five daily prayers?",
     "Isha", "Fajr",
     "Maghrib", "Jumu'ah", "A",
     "The night prayer shares four with Zuhr and Asr."),
    (T_IBD, "Medium", "The prayer is begun by raising the hands and saying Allahu Akbar. This opening takbir is called",
     "takbirat al-ihram", "takbir al-qunut",
     "takbir al-tashriq", "takbir as-sajdah", "A",
     "With it the worshipper enters the state of prayer."),
    (T_IBD, "Medium", "The portion of the prayer recited while sitting, in which the worshipper greets the Prophet, is the",
     "tashahhud", "qunut",
     "du'a of iftitah", "talbiyah", "A",
     "It comes just before the final greeting."),
    (T_SAW, "Easy", "The meal with which a Muslim breaks his fast at sunset is called",
     "iftar", "suhur",
     "aqiqah", "walimah", "A",
     "Dates and water hasten the breaking."),
    (T_SAW, "Medium", "Before every act of worship, the firm intention made in the heart is called",
     "niyyah", "du'a",
     "dhikr", "qasd", "A",
     "Deeds are judged by the intention behind them."),
    (T_SAW, "Hard", "Zakat due on farm produce, one-tenth of the harvest from rain-fed land, is called",
     "ushr", "nisab",
     "sadaqat al-fitr", "kharaj", "A",
     "A tenth returns to the poor from the field."),
    (T_HAJ, "Hard", "The tawaf performed just before a pilgrim finally leaves Makkah is called",
     "tawaf al-wada", "tawaf al-qudum",
     "tawaf al-ifadah", "tawaf al-umrah", "A",
     "The farewell circuit closes the pilgrimage."),
    (T_HAJ, "Medium", "The black stone set into one corner of the Ka'bah, which pilgrims greet during tawaf, is called",
     "Al-Hajar al-Aswad", "Maqam Ibrahim",
     "Rukn al-Yamani", "Hijr Ismail", "A",
     "Pilgrims salute it as they pass."),
]

build_batch(
    S,
    "batch_196_neco_irs7.json",
    "196",
    "NECO Islamic Studies round 7 (R38 top-up): Malik guarding "
    "Hell; the Sirat bridge; the Mizan scale; the People of the "
    "Cave; the book of deeds; Yunus and the fish; Nuh's ark; "
    "Ibrahim Khalilullah; Sulaiman and the ant; Al-Amin; Abu Talib "
    "the protector; the Negus of Abyssinia; Tabuk; Khaybar; "
    "Sumayyah the first martyr; Mus'ab the first teacher of "
    "Madinah; Hamzah master of martyrs; four rak'ahs of Isha; "
    "takbirat al-ihram; the tashahhud; suhur; iftar; niyyah; ushr "
    "on crops; tawaf al-wada; the Black Stone. Scanned against the "
    "whole Islamic Studies pool (WAEC and NECO stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
