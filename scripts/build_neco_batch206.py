"""Batch 206 - WAEC Islamic Studies round 8 (WAEC top-up, R41).

Grows WAEC Islamic Studies from 261 toward ~286 with angles not
yet in the bank: amanah; shukr; hijab; the strong man who
controls anger; Luqman's counsel; prohibited degrees of marriage;
khul; Masjid al-Aqsa; the miqat; the talbiyah; the Muhajirun; the
Pledge of Ridwan; Umar's conversion; Abu Hurayrah; al-Firdaus;
Munkar and Nakir; the Tijaniyya; Yathrib renamed; Abu Bakr the
first man; al-Buraq; fifty prayers reduced to five; the Queen of
Sheba; Surah al-Fil; Maryam; shafa'ah. Scanned against the whole
Islamic Studies pool (WAEC and NECO stems, 513 items).

    python3 scripts/build_neco_batch206.py -> content/batch_206_waec_irs8.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Islamic Studies"

T_SIR = "The Life of the Prophet (Sirah)"
T_SAH = "The Companions"
T_TAW = "At-Tawhid and the Articles of Faith"
T_HAJ = "Hajj and Umrah"
T_MUA = "Muamalat and Family Life"
T_AKH = "Belief in the Last Things"
T_NIG = "Islam in Nigeria"
T_PRO = "The Prophets"

PASSAGES = []
PQ = []

Q = [
    (T_TAW, "Medium", "Any property or duty left in a person's care, which he must guard faithfully and render back, is called",
     "amanah", "waqf",
     "rizq", "sadaqah", "A",
     "Every trust must be delivered to its owner."),
    (T_TAW, "Easy", "Thanking Allah with the tongue, the heart and the deeds for His countless favours is called",
     "shukr", "sabr",
     "tawakkul", "zuhd", "A",
     "A grateful servant counts his blessings."),
    (T_MUA, "Medium", "The modest dress Islam directs a believing woman to draw over herself when she appears in public is the",
     "hijab", "ihram of women",
     "amamah", "jubbah", "A",
     "Modesty is the mark of her dressing."),
    (T_MUA, "Medium", "In a famous hadith, the strong man is not the good wrestler but the one who",
     "controls himself when angry", "wins every wrestling bout",
     "shouts down his rivals", "never forgives a wrong", "A",
     "True strength is mastery of the self."),
    (T_PRO, "Medium", "In Surah Luqman, the wise sage counsels his son to worship Allah alone and afterwards to be kind and obedient to",
     "his parents", "his teachers",
     "the wealthy", "the ruler of the land", "A",
     "Kindness to parents stands next to worship."),
    (T_MUA, "Hard", "A Muslim man may lawfully marry any of these women EXCEPT his",
     "own mother or sister", "cousin's daughter",
     "widow of another man", "divorced woman of the Book", "A",
     "Mothers, sisters and aunts are forever forbidden."),
    (T_MUA, "Hard", "The divorce that a wife herself may seek, returning her mahr to obtain her release, is called",
     "khul", "talaq",
     "li'an", "zihar", "A",
     "She gives back the gift to be set free."),
    (T_SIR, "Medium", "On the night journey, the Prophet (S.A.W.) was carried from Makkah to the distant mosque of Jerusalem, honoured in the Qur'an as",
     "Masjid al-Aqsa", "Masjid an-Nabawi",
     "Masjid al-Quba", "Masjid al-Haram", "A",
     "Glory be to Him who carried His servant by night."),
    (T_NIG, "Hard", "The reform movement founded at Jos in 1978, devoted to wiping out bid'ah and restoring pure Sunnah practice, is",
     "the Izala movement", "the Maitatsine sect",
     "the Muridiyya brotherhood", "the Nasrullah group", "A",
     "Its preachers rose against innovation in worship."),
    (T_HAJ, "Medium", "The pilgrim's ringing cry of Labbayk Allahumma Labbayk, answering the call of Allah, is known as the",
     "talbiyah", "takbir",
     "tahlil", "tahmid", "A",
     "Here I am, O Allah, here I am."),
    (T_SIR, "Easy", "The Makkan Muslims who left their homes and wealth to migrate with the Prophet (S.A.W.) to Madinah are honoured as",
     "the Muhajirun", "the Ansar",
     "the Sahabah of Badr", "the Tabi'un", "A",
     "They abandoned everything for the faith."),
    (T_SIR, "Hard", "Under a tree at Hudaybiyyah, the companions pledged to stand by the Prophet (S.A.W.) to the death. That oath is remembered as",
     "the Pledge of Ridwan", "the Pledge of Aqabah",
     "the first Pledge of Makkah", "the Pledge of the women", "A",
     "Allah was pleased with them as they swore."),
    (T_SAH, "Medium", "The stern young Qurayshite who set out to harm the Prophet (S.A.W.), heard the Qur'an at his sister's house and embraced Islam, was",
     "Umar ibn al-Khattab", "Khalid ibn al-Walid",
     "Abu Jahl", "Utbah ibn Rabi'ah", "A",
     "The persecutor became a mighty defender."),
    (T_SAH, "Medium", "The companion remembered for narrating the largest number of hadith from the Prophet (S.A.W.) is",
     "Abu Hurayrah", "Abu Bakr",
     "Anas ibn Malik", "Abdullah ibn Umar", "A",
     "Three years of constant company filled his memory."),
    (T_AKH, "Medium", "The highest garden of Paradise, whose roof is the Throne of Allah, is called",
     "al-Firdaus", "ar-Rawdah",
     "al-Ma'wa", "an-Na'im", "A",
     "Above every other garden it stands."),
    (T_AKH, "Hard", "The two angels who question the dead in the grave about their Lord, their faith and their prophet are",
     "Munkar and Nakir", "Israfil and Mikail",
     "Kiraman and Katibin", "Harut and Marut", "A",
     "Every soul is questioned soon after burial."),
    (T_NIG, "Medium", "The Sufi order founded in the late eighteenth century by Shaykh Ahmad at-Tijani, widespread in West Africa, is the",
     "Tijaniyya", "Qadiriyya",
     "Muridiyya", "Shadhiliyya", "A",
     "Its litanies spread across the western Sudan."),
    (T_SIR, "Medium", "Before the hijrah, the city that received the Prophet (S.A.W.) and later took his name was known as",
     "Yathrib", "Ta'if",
     "Khaybar", "Tabuk", "A",
     "Yathrib became the City of the Prophet."),
    (T_SAH, "Easy", "After Khadijah, the first man to accept the Prophet's message without hesitation was",
     "Abu Bakr", "Uthman",
     "Umar", "Ali", "A",
     "He believed on the very day he heard."),
    (T_SIR, "Hard", "The white, swift riding beast that carried the Prophet (S.A.W.) on the night journey is called",
     "al-Buraq", "as-Sidrah",
     "al-Isra", "al-Mi'raj", "A",
     "Its stride reached as far as the eye could see."),
    (T_SIR, "Hard", "At the Mi'raj the daily prayers were first commanded as fifty, and were reduced to five after the Prophet (S.A.W.) was advised by",
     "Musa (A.S.)", "Ibrahim (A.S.)",
     "Isa (A.S.)", "Nuh (A.S.)", "A",
     "Musa counselled him to seek easing for the people."),
    (T_PRO, "Hard", "The queen who was won to the worship of one Allah by the letter and wisdom of Sulaiman (A.S.) ruled over",
     "Sheba", "Abyssinia",
     "Egypt", "Persia", "A",
     "She surrendered her throne and her gods."),
    (T_PRO, "Medium", "The elephant army of Abraha that marched on Makkah was destroyed by flights of stone-carrying birds, as told in Surah",
     "al-Fil", "al-Ma'un",
     "Quraysh", "al-Humazah", "A",
     "The year of the elephant is its lesson."),
    (T_PRO, "Easy", "The mother of Prophet Isa (A.S.), honoured above the women of her time, was",
     "Maryam", "Asiya",
     "Hajar", "Amina", "A",
     "A whole surah of the Qur'an bears her name."),
    (T_AKH, "Medium", "The right granted to the Prophet (S.A.W.) to plead for sinful believers on the Day of Judgement is called",
     "shafa'ah", "shahadah",
     "shari'ah", "sadaqah", "A",
     "His pleading will lighten the reckoning."),
]

build_batch(
    S,
    "batch_206_waec_irs8.json",
    "206",
    "WAEC Islamic Studies round 8 (R41 top-up): amanah; shukr; "
    "hijab; the strong man controls anger; Luqman's counsel to "
    "honour parents; prohibited degrees of marriage; khul; Masjid "
    "al-Aqsa; the miqat stations; the talbiyah; the Muhajirun; the "
    "Pledge of Ridwan; Umar's conversion; Abu Hurayrah the great "
    "narrator; al-Firdaus; Munkar and Nakir; the Tijaniyya of "
    "Shaykh Ahmad at-Tijani; Yathrib renamed; Abu Bakr the first "
    "man; al-Buraq; fifty prayers reduced to five on Musa's "
    "advice; the Queen of Sheba; Surah al-Fil; Maryam; shafa'ah. "
    "Scanned against the whole Islamic Studies pool (WAEC and NECO "
    "stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
