"""Batch 112 - NECO Islamic Studies round 3 (NECO top-up, Round 22).

Lifts NECO IRS from 110 toward ~160 with angles not yet in any bank:
ulum al-Quran (makki and madani, asbab al-nuzul, tafsir), sources of
fiqh (ijma, qiyas, ijtihad), the five rulings (wajib to haram), halal
and haram foods, ghusl obligations, janazah and eid prayers, i'tikaf,
zakat recipients, waqf, seerah battles (Badr, Uhud, Khandaq, the
conquest of Makkah, the farewell pilgrimage), the khulafa (apostasy
wars, Umar's administration, Ali's fitnah), tawhid categories, Islamic
finance (mudarabah, murabahah) and zakat vs tax. Scanned against NECO
rounds 1-2, WAEC IRS (all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch112.py -> content/batch_112_neco_irs3.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Islamic Studies"

T_QUR = "Ulum al-Quran"
T_FIQH = "Sources of Fiqh and Rulings"
T_IBAD = "Further Ibadah"
T_SIR = "The Sirah: Battles and Milestones"
T_KHUL = "The Khulafa and After"
T_AQID = "Tawhid and Beliefs"
T_ECON = "Islamic Economy"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- ulum al-Quran
    (T_QUR, "Medium", "Surahs revealed before the hijrah are classified as",
     "makki", "madani", "mursal", "mutashabih", "A",
     "Makkah gave them their name."),
    (T_QUR, "Medium", "The occasions on which particular verses were revealed are studied under",
     "asbab al-nuzul", "ilm al-rijal", "qira'at", "tajwid", "A",
     "Context explains the verse."),
    (T_QUR, "Hard", "The science of interpreting the Quran correctly is",
     "tafsir", "hadith", "fiqh", "nahw", "A",
     "The mufassir unlocks meanings."),
    (T_QUR, "Medium", "Reciting the Quran with proper pronunciation rules is",
     "tajwid", "tawil", "tanzil", "taqlid", "A",
     "Every letter finds its right place."),
    (T_QUR, "Hard", "The longest surah of the Quran, containing the verse of the Throne, is",
     "al-Baqarah", "al-Fatihah", "Yusuf", "al-Kahf", "A",
     "Its pages cover the laws most."),
    (T_QUR, "Medium", "The Quran was revealed to the Prophet over a period of about",
     "23 years", "10 years", "40 years", "13 years", "A",
     "From the first call to the last verse.", "23"),

    # ------------------------------------------------------------- fiqh
    (T_FIQH, "Hard", "The agreement of qualified scholars on a ruling is called",
     "ijma", "qiyas", "ra'y", "taqlid", "A",
     "Consensus carries weight."),
    (T_FIQH, "Hard", "Deriving a new ruling by analogy with an existing one is",
     "qiyas", "ijma", "istikharah", "istislah", "A",
     "Like cases take like rulings."),
    (T_FIQH, "Medium", "Independent legal reasoning by a qualified scholar is known as",
     "ijtihad", "taqlid", "bid'ah", "shura", "A",
     "The mujtahid strives to decide."),
    (T_FIQH, "Medium", "Among the five rulings, the act a Muslim is rewarded for doing but not punished for skipping is",
     "mandub", "wajib", "mubah", "haram", "A",
     "Recommended but never forced."),
    (T_FIQH, "Easy", "An act every Muslim must perform is",
     "wajib", "mandub", "mubah", "makruh", "A",
     "Fard is its twin in meaning."),
    (T_FIQH, "Easy", "An act strictly forbidden by shariah is",
     "haram", "mubah", "mandub", "wajib", "A",
     "Doing it earns a grave sin."),
    (T_FIQH, "Hard", "An act disliked but not sinful when done is",
     "makruh", "haram", "wajib", "mubah", "A",
     "It is better left undone."),
    (T_FIQH, "Medium", "Permissible acts that carry neither reward nor punishment are",
     "mubah", "wajib", "makruh", "haram", "A",
     "The neutral middle ground."),
    (T_FIQH, "Hard", "Swine is forbidden in Islam chiefly because the Quran declares it",
     "impure", "costly", "rare", "unprofitable", "A",
     "The text bans it outright."),
    (T_FIQH, "Medium", "For an animal to be halal, it must be slaughtered while invoking",
     "the name of Allah", "the name of the buyer", "no name at all", "the name of the market", "A",
     "Bismillah precedes the cut."),

    # ------------------------------------------------------------- further ibadah
    (T_IBAD, "Hard", "Ghusl becomes obligatory after marital relations and after",
     "menstruation ends", "cutting nails", "eating a feast", "long travel", "A",
     "Major impurity demands the full bath."),
    (T_IBAD, "Medium", "The janazah prayer is performed",
     "without ruku or sujud", "with four rakahs", "only at Eid", "only in Makkah", "A",
     "Standing du'a carries it."),
    (T_IBAD, "Medium", "The Eid al-Fitr prayer is offered",
     "on the morning after Ramadan", "on the Day of Arafat", "on the 10th of Muharram", "every Friday", "A",
     "It opens the festival of breaking."),
    (T_IBAD, "Hard", "A worshipper who camps in the mosque through Ramadan's final ten nights is observing",
     "i'tikaf", "itikhad", "ihsan", "ihram", "A",
     "The worshipper cuts off the world."),
    (T_IBAD, "Medium", "Tarawih prayers are special congregational prayers held in",
     "Ramadan nights", "Muharram days", "Shawwal mornings", "Rajab evenings", "A",
     "After isha through the holy month."),
    (T_IBAD, "Hard", "Sujud as-sahw, the prostration of forgetfulness, compensates for",
     "an error made in prayer", "a missed fast", "unpaid zakah", "a broken oath", "A",
     "It mends the slip at once."),

    # ------------------------------------------------------------- sirah
    (T_SIR, "Medium", "The first major battle in Islam, fought in 2 AH, was",
     "Badr", "Uhud", "Khandaq", "Hunayn", "A",
     "Three hundred faced a thousand."),
    (T_SIR, "Hard", "At Uhud, Muslim archers left their post and the army suffered because the enemy was led by",
     "Khalid ibn al-Walid", "Abu Sufyan", "Abu Jahl", "Amr ibn al-As", "A",
     "His cavalry turned the flank."),
    (T_SIR, "Medium", "The Khandaq battle is also called the battle of the",
     "trench", "camel", "garden", "banner", "A",
     "A great ditch guarded Madinah."),
    (T_SIR, "Hard", "The peaceful capture of Makkah happened in the year",
     "8 AH", "6 AH", "2 AH", "10 AH", "A",
     "The city fell without battle.", "8"),
    (T_SIR, "Hard", "During the farewell pilgrimage the Prophet delivered a sermon at",
     "Arafat", "Mina", "Muzdalifah", "Marwah", "A",
     "His last great address rang out."),
    (T_SIR, "Medium", "The Prophet's first wife, a successful merchant whom he trusted deeply, was",
     "Khadijah", "Aisha", "Hafsa", "Zaynab", "A",
     "She believed him at the very start."),

    # ------------------------------------------------------------- khulafa
    (T_KHUL, "Hard", "Abu Bakr's caliphate is most remembered for suppressing",
     "the apostasy movement", "the Mongols", "the Crusaders", "the Qarmatians", "A",
     "False prophets rose and fell."),
    (T_KHUL, "Hard", "Umar's administration introduced the court system and the",
     "hijri calendar", "first mosque", "first coin with his image", "navy of fifty ships", "A",
     "Dating began from the hijrah."),
    (T_KHUL, "Medium", "Umar extended the two holy mosques and was famously",
     "strict and just", "fond of luxury", "silent in council", "absent from Madinah", "A",
     "He was stern with himself, just to all."),
    (T_KHUL, "Hard", "The civil strife (fitnah) that marked Ali's caliphate began with the battle of",
     "the Camel", "Badr", "Tabuk", "Hunayn", "A",
     "Basra's plain saw the clash."),

    # ------------------------------------------------------------- aqid
    (T_AQID, "Hard", "Affirming Allah as the only Creator and Sustainer is tawhid",
     "rububiyyah", "uluhiyyah", "asma wa sifat", "tanzih only", "A",
     "Lordship belongs to the One."),
    (T_AQID, "Hard", "Directing all worship to Allah alone is tawhid",
     "uluhiyyah", "rububiyyah", "asma wa sifat", "khuluq", "A",
     "Only He deserves worship."),
    (T_AQID, "Medium", "Belief in the angels includes the conviction that Jibril",
     "delivered revelation", "blows the trumpet", "records deeds", "guards hell", "A",
     "He carried down the messages."),
    (T_AQID, "Medium", "Israfil, at the end of time, is the angel who will",
     "blow the trumpet", "take souls", "bring rain", "guard paradise", "A",
     "One blast ends the world."),
    (T_AQID, "Hard", "The belief that Allah knows all things, past and future, covers the doctrine of",
     "qadar (destiny)", "qiyas", "qunut", "qudsi", "A",
     "Nothing escapes His knowledge."),

    # ------------------------------------------------------------- economy
    (T_ECON, "Hard", "In mudarabah, the bank provides capital while the entrepreneur provides",
     "labour and skill", "an equal capital sum", "land and buildings", "government licence", "A",
     "Profit is shared by agreement."),
    (T_ECON, "Hard", "Murabahah, a halal financing mode, is essentially a",
     "cost-plus sale contract", "loan at interest", "gift transfer", "insurance policy", "A",
     "A known mark-up replaces interest."),
    (T_ECON, "Hard", "What separates zakah from an ordinary tax?",
     "a fixed worship on wealth", "a voluntary gift to family", "a fine for offences", "a levy on foreigners only", "A",
     "It purifies both wealth and soul."),
    (T_ECON, "Medium", "The eight categories entitled to zakah are listed in the Quran's surah",
     "at-Tawbah", "al-Fatihah", "al-Baqarah", "an-Nur", "A",
     "The verse of zakah recipients sits there."),
    (T_ECON, "Medium", "Property dedicated for a public good, such as a mosque or school, is a",
     "waqf", "wasiyyah", "mahr", "fadl", "A",
     "Its benefit never stops flowing."),
    (T_ECON, "Medium", " extravagance and waste are checked by the Islamic principle of",
     "moderation in spending", "maximum saving only", "borrowing freely", "hoarding wealth", "A",
     "The middle way governs wealth."),
]

build_batch(
    S,
    "batch_112_neco_irs3.json",
    "112",
    "NECO Islamic Studies round 3 (Round 22 top-up): makki vs madani, "
    "asbab al-nuzul, tafsir, tajwid, al-Baqarah and the 23-year "
    "revelation, ijma, qiyas, ijtihad, the five rulings from wajib to "
    "haram, halal slaughter, ghusl obligations, janazah, Eid al-Fitr, "
    "i'tikaf, tarawih, sujud as-sahw, Badr, Uhud's archers and Khalid, "
    "Khandaq, the conquest of Makkah (8 AH), the Arafat sermon, "
    "Khadijah, Abu Bakr's apostasy wars, Umar's calendar and justice, "
    "Ali's fitnah and the Camel, tawhid rububiyyah and uluhiyyah, "
    "Jibril, Israfil, qadar, mudarabah, murabahah, zakah vs tax, the "
    "at-Tawbah recipients, waqf and moderation. Scanned against NECO "
    "rounds 1-2, WAEC IRS (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
