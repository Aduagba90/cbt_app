"""Batch 089 - NECO Islamic Studies round 2 (NECO lift, Round 18).

NECO IRS objective draws 60 items; the bank stood at 70. This lift adds
fresh items - Qur'an detail (seven verses of Al-Fatihah, 30 ajza, tajwid,
tafsir, Zayd b. Thabit, at-Tawbah), ibadat (suhur, Laylat al-Qadr, tarawih,
i'tikaf, ihram cloths, nisab, khutbah), seerah (cave Thawr, Quba, Ansar,
Khandaq, Seal of Prophets, Year of Grief, Hasan and Husayn), articles
(Tawrat-Zabur-Injil, Israfil, recording angels, qadar), hadith science
(Sahih Muslim, matn, intentions hadith, da'if), khulafa (As-Siddiq, Umar's
assassination, Ali), morals (maisir, khamr, honest trade, qard hasan),
Nigerian Islam (Sokoto Jihad, Nana Asma'u) and calendar (Mawlid).

    python3 scripts/build_neco_batch89.py -> content/batch_089_neco_irs2.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Islamic Studies"

T_QUR = "The Qur'an"
T_PIL = "The Five Pillars of Islam"
T_SEE = "Life of the Prophet (S.A.W.)"
T_IMA = "Articles of Faith (Iman)"
T_HAD = "Hadith"
T_KHU = "The Khulafa' Rashidun"
T_MOR = "Islamic Moral Values"
T_MUA = "Muamalat (Transactions)"
T_NIG = "Spread of Islam in Nigeria"
T_CAL = "Islamic Calendar and Festivals"

PASSAGES = []
PQ = []

Q = [
    # ---------------------------------------------------------------- qur'an
    (T_QUR, "Easy", "Surah Al-Fatihah consists of how many verses?",
     "seven", "five", "nine", "eleven", "A",
     "Its seven verses open the Book."),
    (T_QUR, "Easy", "The Qur'an is divided for recitation into 30 parts called",
     "ajza", "surahs", "rukus", "manzils", "A",
     "Each juz marks a thirtieth."),
    (T_QUR, "Medium", "The rules guiding correct and beautiful recitation of the Qur'an are called",
     "tajwid", "tafsir", "hadith", "fiqh", "A",
     "Tajwid guards the pronunciation."),
    (T_QUR, "Medium", "The science of explaining the meaning of the Qur'an is",
     "tafsir", "tajwid", "qira'at", "sirah", "A",
     "Scholars of tafsir explain verses."),
    (T_QUR, "Hard", "The young scribe who played a leading part in gathering the Qur'an into one volume was",
     "Zayd b. Thabit", "Mu'awiyah b. Abi Sufyan", "Abdullah b. Umar", "Khalid b. al-Walid", "A",
     "Zayd led the compilation."),
    (T_QUR, "Hard", "Every surah of the Qur'an begins with the basmalah except",
     "Surah at-Tawbah", "Surah al-Fatihah", "Surah Yasin", "Surah al-Ikhlas", "A",
     "At-Tawbah alone lacks it."),
    # ---------------------------------------------------------------- pillars
    (T_PIL, "Easy", "The light meal taken before dawn to begin a day of fasting is called",
     "suhur", "iftar", "qada", "sadaqah", "A",
     "Suhur steadies the faster."),
    (T_PIL, "Easy", "Laylat al-Qadr is described in the Qur'an as better than",
     "a thousand months", "a hundred years", "ten lifetimes", "all the nights of a year", "A",
     "One night outweighs a thousand months."),
    (T_PIL, "Easy", "The extra prayers performed in the nights of Ramadan are called",
     "tarawih", "janazah", "istisqa", "duha", "A",
     "Tarawih follow the isha prayer."),
    (T_PIL, "Hard", "Secluding oneself in the mosque during the last ten nights of Ramadan is called",
     "i'tikaf", "ihram", "tawaf", "ihsan", "A",
     "The devoted sit away in worship."),
    (T_PIL, "Medium", "The male pilgrim's ihram dress is made up of",
     "two white unstitched cloths", "one black embroidered robe", "a green turban and gown", "his finest home clothes", "A",
     "Two seamless wraps level all men."),
    (T_PIL, "Hard", "Zakat becomes obligatory on wealth only when it reaches the",
     "nisab", "hawl", "rabi", "qiblah", "A",
     "Below the nisab no zakat falls due."),
    (T_PIL, "Easy", "The sermon delivered before the Jumu'ah prayer is called the",
     "khutbah", "adhan", "talbiyah", "du'a", "A",
     "The khatib delivers the khutbah."),
    # ---------------------------------------------------------------- seerah
    (T_SEE, "Medium", "On the Hijrah journey, the Prophet and Abu Bakr took refuge in the cave of",
     "Thawr", "Hira", "Uhud", "Jabal al-Rahmah", "A",
     "They hid there from the searchers."),
    (T_SEE, "Easy", "Which mosque did the Prophet himself first raise on reaching Madinah's outskirts?",
     "Quba", "Masjid an-Nabawi", "Masjid al-Qiblatayn", "Masjid al-Haram", "A",
     "Quba was the first he built."),
    (T_SEE, "Easy", "The Madinan helpers who received the Makkan immigrants were called the",
     "Ansar", "Muhajirun", "Quraysh", "Sahifah", "A",
     "The helpers shared their homes."),
    (T_SEE, "Medium", "The Battle of the Trench is so named because the Muslims",
     "dug a ditch round Madinah", "fought inside a dry riverbed", "camped beside a well", "were besieged in a valley", "A",
     "The khandaq barred the cavalry."),
    (T_SEE, "Easy", "The title 'Seal of the Prophets' shows Muhammad as",
     "the final messenger of Allah", "the first of the prophets", "a prophet to the Arabs alone", "a messenger yet to come", "A",
     "No prophet comes after him."),
    (T_SEE, "Hard", "The year in which the Prophet lost both Khadijah and Abu Talib is remembered as",
     "the Year of Grief", "the Year of the Elephant", "the Year of Deputations", "the Year of the Farewell", "A",
     "Sorrow followed sorrow in that year."),
    (T_SEE, "Medium", "The Prophet's grandsons through Fatimah were",
     "Hasan and Husayn", "Hamzah and Abbas", "Talhah and Zubayr", "Abu Talib and Hamzah", "A",
     "Fatimah bore the two boys."),
    # ---------------------------------------------------------------- articles of faith
    (T_IMA, "Medium", "The holy books named in the Qur'an include the Tawrat, the Zabur and the",
     "Injil", "Talmud", "Vedas", "Avesta", "A",
     "The Injil was revealed to Isa."),
    (T_IMA, "Medium", "The angel who will blow the trumpet on the Last Day is",
     "Israfil", "Mikail", "Izra'il", "Malik", "A",
     "Israfil awaits the command."),
    (T_IMA, "Hard", "The two angels who record a person's good and bad deeds are known as",
     "kiraman katibin", "munkar and nakir", "harut and marut", "malak al-mawt", "A",
     "The honourable writers note all."),
    (T_IMA, "Hard", "Belief that Allah has measured and knows all things is belief in",
     "qadar", "qiyamah", "qiblah", "qunut", "A",
     "Qadar is the divine decree."),
    # ---------------------------------------------------------------- hadith
    (T_HAD, "Medium", "After Sahih al-Bukhari, the second most authentic hadith collection is",
     "Sahih Muslim", "Sunan Abu Dawud", "Jami' at-Tirmidhi", "Muwatta Malik", "A",
     "Muslim's collection ranks second."),
    (T_HAD, "Hard", "In hadith science, the text of the report itself is called the",
     "matn", "isnad", "rijal", "takhrij", "A",
     "The matn is what the isnad carries."),
    (T_HAD, "Hard", "The famous hadith 'deeds are judged by intentions' opens which collection?",
     "Sahih al-Bukhari", "Sahih Muslim", "Sunan an-Nasa'i", "Musnad Ahmad", "A",
     "Bukhari begins with intentions."),
    (T_HAD, "Medium", "A hadith graded da'if is one that is",
     "weak", "fully authentic", "sound but not the best", "agreed upon by all", "A",
     "Weakness breaks its chain or text."),
    # ---------------------------------------------------------------- khulafa
    (T_KHU, "Easy", "The title As-Siddiq, meaning 'the truthful', was earned by",
     "Abu Bakr", "Umar", "Uthman", "Ali", "A",
     "He confirmed the truth without doubt."),
    (T_KHU, "Hard", "The caliph murdered in Madinah by a Persian slave was",
     "Umar b. al-Khattab", "Uthman b. Affan", "Ali b. Abi Talib", "Abu Bakr", "A",
     "Umar was stabbed at dawn prayer."),
    (T_KHU, "Easy", "Who completed the line of the four Rightly Guided Caliphs?",
     "Ali b. Abi Talib", "Abu Bakr", "Umar", "Uthman", "A",
     "Ali was the last of the four."),
    # ---------------------------------------------------------------- moral values
    (T_MOR, "Medium", "Maisir, which Islam forbids, means",
     "gambling", "usury", "hoarding", "slander", "A",
     "Games of chance devour wealth."),
    (T_MOR, "Easy", "Khamr, forbidden in the Qur'an, refers to",
     "intoxicants", "pork", "blood", "dead meat", "A",
     "It clouds the mind and judgement."),
    (T_MOR, "Medium", "The Prophet's warning 'whoever cheats us is not one of us' was directed at",
     "dishonest traders", "lazy farmers", "talkative children", "travelling scholars", "A",
     "Short measure has no place in Islam."),
    (T_MOR, "Hard", "A goodly loan given to a needy person without any interest is called",
     "qard hasan", "riba", "mudarabah", "daman", "A",
     "Kind lending pleases Allah."),
    # ---------------------------------------------------------------- muamalat
    (T_MUA, "Hard", "Property set aside forever for a religious or charitable purpose is a",
     "waqf", "mirth", "wasayah", "amanah", "A",
     "Its benefit never stops flowing."),
    (T_MUA, "Easy", "Voluntary giving beyond the obligatory zakat is called",
     "sadaqah", "khums", "fidyah", "urf", "A",
     "Every kind gift counts as sadaqah."),
    # ---------------------------------------------------------------- nigeria
    (T_NIG, "Medium", "The Sokoto Jihad of 1804 was led by",
     "Usman dan Fodio", "Muhammad al-Amin al-Kanemi", "Idris Alooma", "Samori Toure", "A",
     "He raised the jihad from Degel."),
    (T_NIG, "Hard", "The daughter of Usman dan Fodio famed for poetry and women's education was",
     "Nana Asma'u", "A'ishatu", "Maryamma", "Fatimah bint Usman", "A",
     "Her yan taru taught the women."),
    # ---------------------------------------------------------------- calendar
    (T_CAL, "Easy", "Mawlid an-Nabi is the occasion that marks",
     "the birth of the Prophet", "the first revelation", "the Hijrah journey", "the sacrifice of Ibrahim", "A",
     "Muslims celebrate his birth."),
]

build_batch(
    S,
    "batch_089_neco_irs2.json",
    "089",
    "NECO IRS round 2 (Round 18 lift): Qur'an detail (Al-Fatihah's verses, "
    "30 ajza, tajwid, tafsir, Zayd b. Thabit, at-Tawbah's basmalah), "
    "ibadat (suhur, Laylat al-Qadr, tarawih, i'tikaf, ihram cloths, nisab, "
    "khutbah), seerah (cave Thawr, Quba, Ansar, Khandaq, Seal of Prophets, "
    "Year of Grief, Hasan and Husayn), articles (Tawrat-Zabur-Injil, "
    "Israfil, kiraman katibin, qadar), hadith science (Sahih Muslim, matn, "
    "the intentions hadith, da'if), khulafa (As-Siddiq, Umar's martyrdom, "
    "Ali), morals (maisir, khamr, cheating traders, qard hasan), waqf, "
    "sadaqah, Nigerian Islam (Sokoto Jihad, Nana Asma'u) and Mawlid. "
    "Scanned against NECO round 1, the WAEC twin and the JAMB IRS banks.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
