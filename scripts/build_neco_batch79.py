"""Batch 079 - WAEC Islamic Studies, Paper 1 Objective round 1.

WASSCE Islamic Studies Paper 1 (Objective) is a 50-item paper (50 min;
official 2026 second-series timetable, paper 2081). This batch covers the
WASSCE syllabus with FRESH angles and phrasings - numeric answers (610 CE,
23 years, 114 surahs, 17 rak'ahs, one-fortieth, 9th Dhul-Hijjah, 8 AH),
named rites and people (Sa'y, Wuquf, Badr, Hudaybiyyah, Khadijah,
al-Jilani, tahnik), West African Islam (Kanem-Borno, Qadiriyyah) and
question-form stems - because the near-dup scan checks every item against
the JAMB, WAEC and NECO banks, including the large JAMB IRS banks (batches
004, 032-033) and our 70-item NECO IRS bank.

    python3 scripts/build_neco_batch79.py -> content/batch_079_waec_irs.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Islamic Studies"

T_QUR = "The Qur'an and Hadith"
T_TAW = "Tawhid and the Articles of Faith"
T_IBA = "Ibadat: Worship and Devotion"
T_HIS = "The Prophet, the Caliphs and Islamic History"
T_MUA = "Muamalat and Islamic Ethics"
T_FAM = "Family Life and the Islamic Calendar"

PASSAGES = []
PQ = []

Q = [
    # ---------------------------------------------------------------- qur'an and hadith
    (T_QUR, "Medium", "The first revelation came to Prophet Muhammad in the year",
     "610 CE", "622 CE", "570 CE", "632 CE", "A",
     "It began in the cave of Hira."),
    (T_QUR, "Easy", "Which angel delivered Allah's messages to the Prophet?",
     "Jibril", "Mikail", "Israfil", "Izra'il", "A",
     "Jibril brought down the revelation."),
    (T_QUR, "Medium", "Surah Al-'Alaq opens with a command to",
     "read", "write", "pray", "fast", "A",
     "The command to read came first."),
    (T_QUR, "Easy", "How many chapters does the Qur'an contain?",
     "114", "99", "104", "124", "A",
     "One hundred and fourteen chapters."),
    (T_QUR, "Medium", "The uniform master copy of the Qur'an sent to the provinces was ordered by",
     "Uthman b. Affan", "Abu Bakr", "Umar b. Khattab", "Ali b. Abi Talib", "A",
     "Uthman unified the recitation text."),
    (T_QUR, "Easy", "Which surah has 286 verses, making it the longest?",
     "Al-Baqarah", "Al-Fatihah", "Yasin", "Al-Ikhlas", "A",
     "It has two hundred eighty-six verses."),
    (T_QUR, "Medium", "Surah Al-Fatihah is recited in every",
     "rak'ah of the prayer", "circuit of the tawaf", "khutbah of Jumu'ah", "nikah ceremony", "A",
     "No prayer stands without it."),
    (T_QUR, "Medium", "Revelation came to the Prophet over about",
     "23 years", "10 years", "40 years", "63 years", "A",
     "It began at forty and ended at sixty-three."),
    (T_QUR, "Medium", "Muslims turn first to the Qur'an because it is",
     "the final guide from Allah", "an Arab history book", "a book of old poems", "a collection of tales", "A",
     "It is the last revealed guidance."),
    (T_QUR, "Medium", "The chapters revealed at Madinah mostly deal with",
     "laws and community life", "stories of past prophets", "hymns of praise alone", "tales of the jinn", "A",
     "Madinan surahs legislate for society."),
    (T_QUR, "Easy", "A hafiz is one who has",
     "memorised the whole Qur'an", "translated the Qur'an", "written a complete tafsir", "led all the tarawih", "A",
     "Huffaz carry the Book by heart."),
    (T_QUR, "Medium", "The most trusted collector of hadith is",
     "Imam al-Bukhari", "Imam al-Shafi'i", "Imam Malik", "Imam Abu Hanifah", "A",
     "His Sahih ranks highest of all."),
    (T_QUR, "Hard", "A hadith qudsi is a report in which",
     "Allah speaks through the Prophet", "the Prophet quotes a companion", "a companion describes a battle", "a caliph lays down a law", "A",
     "The wording is the Prophet's, meaning Allah's."),
    # ---------------------------------------------------------------- tawhid and articles
    (T_TAW, "Easy", "La ilaha illa Allah declares Allah's",
     "oneness and sole worship", "mercy to all sinners", "power over wealth", "knowledge of the future", "A",
     "The kalimah denies all other gods."),
    (T_TAW, "Medium", "Belief in the angels of Allah is",
     "the second article of Iman", "the first pillar of Islam", "an optional devotion", "a later addition to faith", "A",
     "Iman lists angels after Allah."),
    (T_TAW, "Medium", "Shirk in Islam means",
     "associating partners with Allah", "giving alms in secret", "fasting on Mondays", "travelling for Hajj", "A",
     "It is the unforgivable wrong."),
    (T_TAW, "Medium", "Belief in the Last Day includes belief in",
     "the resurrection and judgment", "the birth of the Prophet", "the first revelation at Hira", "the building of the Ka'bah", "A",
     "All souls rise to be judged."),
    (T_TAW, "Hard", "The Qur'an calls Allah Al-'Alim, meaning the",
     "All-Knowing", "All-Providing", "The Compeller", "The Forgiver", "A",
     "His knowledge touches all things."),
    (T_TAW, "Easy", "The beautiful names of Allah commonly number",
     "99", "40", "70", "114", "A",
     "Ninety-nine names are counted."),
    (T_TAW, "Hard", "Nuh, Ibrahim, Musa, Isa and Muhammad are together known as",
     "Ulul-'Azm, the steadfast prophets", "the four rightly guided caliphs", "the scribes of Madinah city", "the companions at the battle of Badr", "A",
     "They bore the great burdens of message."),
    (T_TAW, "Medium", "Entering Islam requires declaring",
     "the Shahadah with conviction", "the Talbiyah at the Hajj", "the Takbir in the Salah", "the Tashahhud every day", "A",
     "Witness comes before every rite."),
    # ---------------------------------------------------------------- ibadat
    (T_IBA, "Hard", "The five daily prayers contain a total of",
     "17 rak'ahs", "10 rak'ahs", "20 rak'ahs", "12 rak'ahs", "A",
     "Fajr two, Zuhr four, Asr four, Maghrib three, Isha four."),
    (T_IBA, "Medium", "Wudu is broken by",
     "answering the call of nature", "sneezing during du'a", "walking to the mosque", "reciting the Qur'an", "A",
     "Such acts cancel the purity."),
    (T_IBA, "Easy", "A Muslim turning to face the Ka'bah in Salah is facing the",
     "qiblah", "miqat", "minbar", "sahih", "A",
     "The qiblah unifies all prayers."),
    (T_IBA, "Medium", "Salat al-Jumu'ah replaces which prayer?",
     "Zuhr", "Fajr", "Asr", "Isha", "A",
     "The Friday sermon stands in for it."),
    (T_IBA, "Medium", "How much zakat is due on money kept for a full year?",
     "one-fortieth (2.5%)", "one-tenth (10%)", "one-twentieth (5%)", "one-hundredth (1%)", "A",
     "A fortieth share purifies savings."),
    (T_IBA, "Hard", "The zakat on farm produce watered by rain alone is",
     "one-tenth", "one-twentieth", "one-fortieth", "one-hundredth", "A",
     "Rain-fed crops owe the ushr tithe."),
    (T_IBA, "Medium", "Fasting is obligatory on every Muslim who is",
     "mature and healthy", "a young child", "critically ill", "on a long journey", "A",
     "Children, the sick and travellers are excused."),
    (T_IBA, "Medium", "Travellers and the sick who miss Ramadan days",
     "make up the days later", "pay only extra zakat", "are exempt for ever", "fast half-days instead", "A",
     "The fast is repaid day for day."),
    (T_IBA, "Medium", "The rite of hurrying between Safa and Marwah is called",
     "Sa'y", "Tawaf", "Wuquf", "Rami", "A",
     "It remembers Hajar's running."),
    (T_IBA, "Medium", "Pilgrims spend the ninth day of Dhul-Hijjah standing at",
     "Arafat", "Mina", "Muzdalifah", "Marwah", "A",
     "The Hajj is the day at Arafat."),
    (T_IBA, "Easy", "Circling the Ka'bah seven times on arrival in Makkah is called",
     "tawaf", "sa'y", "ihram", "nafrah", "A",
     "Seven circuits welcome the pilgrim."),
    (T_IBA, "Easy", "Id al-Adha falls on the 10th of",
     "Dhul-Hijjah", "Shawwal", "Ramadan", "Muharram", "A",
     "It marks the day of sacrifice."),
    (T_IBA, "Easy", "The call to prayer is made by the",
     "mu'adhdhin", "imam", "qadi", "khatib", "A",
     "His voice summons the faithful."),
    # ---------------------------------------------------------------- history
    (T_HIS, "Medium", "The Muslim calendar counts its years from",
     "the Hijrah of 622 CE", "the birth of the Prophet", "the first revelation at Hira", "the conquest of Makkah", "A",
     "The migration to Madinah is year one."),
    (T_HIS, "Medium", "In the second year after the Hijrah, the Muslims won the battle of",
     "Badr", "Uhud", "Khandaq", "Hunayn", "A",
     "Three hundred and thirteen faced the hosts."),
    (T_HIS, "Medium", "The battle in which the Prophet himself was wounded was",
     "Uhud", "Badr", "Tabuk", "Khaybar", "A",
     "The archers' withdrawal cost them dear."),
    (T_HIS, "Hard", "The treaty the Prophet signed with the Makkans in 6 AH was concluded at",
     "Hudaybiyyah", "Aqabah", "Tabuk", "Khaybar", "A",
     "Its terms looked like loss but opened Makkah."),
    (T_HIS, "Medium", "The peaceful conquest of Makkah happened in",
     "8 AH", "2 AH", "6 AH", "11 AH", "A",
     "The city opened without a battle."),
    (T_HIS, "Easy", "Who led the Muslims as caliph immediately after the Prophet?",
     "Abu Bakr", "Umar", "Uthman", "Ali", "A",
     "The Siddiq stood first after him."),
    (T_HIS, "Medium", "The caliph under whose rule the Muslims entered Egypt and Persia was",
     "Umar b. al-Khattab", "Uthman b. Affan", "Ali b. Abi Talib", "Mu'awiyah b. Abi Sufyan", "A",
     "His decade doubled the realm."),
    (T_HIS, "Medium", "The first gathering of the Qur'an into one volume was ordered by",
     "Abu Bakr", "Umar", "Uthman", "Ali", "A",
     "He heeded Umar's advice after Yamamah."),
    (T_HIS, "Medium", "Muslim traders and scholars from the north first planted Islam in",
     "Kanem-Borno", "Bonny", "Lagos", "Onitsha", "A",
     "Traders and scholars carried the faith."),
    (T_HIS, "Hard", "The Qadiriyyah order in Nigeria traces its chain to",
     "Shaykh Abd al-Qadir al-Jilani", "Usman dan Fodio of Sokoto", "Nana Asma'u the poetess", "Ibn Battuta the traveller", "A",
     "The Baghdad master heads the chain."),
    (T_HIS, "Medium", "Which wife of the Prophet was the first to accept his message?",
     "Khadijah", "A'ishah", "Fatimah", "Hafsah", "A",
     "She comforted him after Hira."),
    (T_HIS, "Hard", "The Farewell Pilgrimage sermon of the Prophet stressed",
     "sanctity of life and property", "the taxes owed to Madinah", "the wars soon to come", "the building of war fleets", "A",
     "He declared blood and wealth sacred."),
    # ---------------------------------------------------------------- muamalat and ethics
    (T_MUA, "Medium", "Riba in transactions means",
     "charging interest on loans", "giving sadaqah openly", "sharing profits justly", "deferring a due payment", "A",
     "Increase without work is forbidden."),
    (T_MUA, "Easy", "Halal earnings forbid",
     "bribery and cheating", "trade in foodstuffs", "farming in its season", "rearing of cattle", "A",
     "Clean gain must come clean."),
    (T_MUA, "Medium", "A Muslim must speak the truth even when",
     "it is against a relative", "fasting in Ramadan", "travelling on a Friday", "facing the qiblah", "A",
     "Truth outweighs family ties."),
    (T_MUA, "Medium", "Zina is forbidden because it",
     "destroys family honour", "wastes time at night", "reduces trade income", "breaks the state of wudu", "A",
     "It tears the fabric of lineage."),
    (T_MUA, "Medium", "Kindness to parents in Islam ranks",
     "next to the worship of Allah", "below ties of friendship", "after the care of animals", "beneath community service", "A",
     "The Qur'an pairs both duties."),
    (T_MUA, "Medium", "The property of orphans must be",
     "guarded and handed over", "spent by their guardians", "invested for the ruler", "shared among the poor", "A",
     "Their wealth waits for their age."),
    (T_MUA, "Hard", "Ghibah, backbiting, is likened in the Qur'an to",
     "eating a dead brother's flesh", "drinking stale well water", "walking barefoot on thorns", "carrying heavy millstones", "A",
     "The image stings the conscience."),
    (T_MUA, "Medium", "Moderate spending is commanded to guard against",
     "israf, wastefulness", "saving in the banks", "lending to relatives", "trading with foreigners", "A",
     "Waste is the devil's way."),
    (T_MUA, "Medium", "A good word spoken to a neighbour counts as",
     "sadaqah, a charity", "a debt to be repaid", "a favour to be owed", "an oath to be kept", "A",
     "Even speech can be giving."),
    # ---------------------------------------------------------------- family and calendar
    (T_FAM, "Medium", "Marriage in Islam is contracted through",
     "ijab and qabul", "a court lawsuit alone", "a written diary entry", "an inheritance clause", "A",
     "Offer and acceptance bind the nikah."),
    (T_FAM, "Medium", "The mahr paid at marriage belongs to",
     "the wife herself", "her father's estate", "the groom's family", "the community fund", "A",
     "It is her exclusive right."),
    (T_FAM, "Easy", "Id al-Fitr comes right after",
     "the month of Ramadan", "the month of Hajj", "the month of Rajab", "the day of Arafat", "A",
     "It breaks the fast with joy."),
    (T_FAM, "Easy", "The first month of the Islamic calendar is",
     "Muharram", "Ramadan", "Shawwal", "Dhul-Hijjah", "A",
     "The year opens with Muharram."),
    (T_FAM, "Medium", "Ashura, the tenth of Muharram, is kept by",
     "voluntary fasting", "forced public mourning", "the compulsory Hajj rite", "collecting the zakat dues", "A",
     "Fasting marks the great day."),
    (T_FAM, "Hard", "Tahnik performed for a newborn means",
     "sweetening the baby's mouth", "shaving the head at once", "naming after seven days", "circumcision on the first day", "A",
     "Dates are chewed and given."),
    (T_FAM, "Medium", "Complete breastfeeding and weaning, per the Qur'an, span",
     "two full years", "six months only", "three full years", "one full year", "A",
     "Thirty months are mentioned."),
]

build_batch(
    S,
    "batch_079_waec_irs.json",
    "079",
    "WAEC Islamic Studies Paper 1 round 1 (Round 16e): the WASSCE syllabus "
    "with FRESH angles - numeric answers (610 CE, 23 years, 114 surahs, 17 "
    "rak'ahs, one-fortieth zakat, 9th Dhul-Hijjah, 8 AH), named rites and "
    "people (Sa'y, Wuquf, Hudaybiyyah, Khadijah, al-Jilani, tahnik), West "
    "African Islam (Kanem-Borno routes, Qadiriyyah chain) and question-form "
    "stems - because the near-dup scan checks every item against the JAMB, "
    "WAEC and NECO banks INCLUDING the large JAMB IRS banks (004, 032-033) "
    "and the 70-item NECO IRS bank. Topics: the Qur'an and Hadith, Tawhid "
    "and the articles of faith, Ibadat, the Prophet and the caliphs, "
    "Muamalat and ethics, family life and the Islamic calendar.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
