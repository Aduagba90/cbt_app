"""Batch 106 - WAEC Islamic Studies round 3 (WAEC top-up, Round 21).

Lifts WAEC IRS from 104 toward ~150 with fresh angles: hadith science
and compilers, taharah details, salah conditions and invalidators,
zakat computation, sawm exemptions, hajj rites in order, nikah and
family life, inheritance shares, seerah milestones, the khulafa
ar-rashidun, the Islamic calendar and aqidah. Scanned against WAEC
rounds 1-2, NECO IRS and the JAMB pool.

    python3 scripts/build_neco_batch106.py -> content/batch_106_waec_irs3.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Islamic Studies"

T_HAD = "Hadith and Sunnah"
T_IBAD = "Ibadah: Taharah and Salah"
T_ZAK = "Zakah and Sawm"
T_HAJJ = "Hajj and Umrah"
T_FAM = "Marriage and Family Life"
T_INH = "Inheritance and Transactions"
T_SEER = "Seerah and the Khulafa"
T_AQID = "Aqidah and Islamic Life"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- hadith
    (T_HAD, "Medium", "Checking the reliability of a hadith's chain of narrators is the work of",
     "isnad criticism", "fiqh", "tafsir", "balaghah", "A",
     "Each narrator in the chain is checked."),
    (T_HAD, "Medium", "Scholars call the wording or body of a hadith its",
     "matn", "sanad", "tafsir", "rafi", "A",
     "The matn is the message itself."),
    (T_HAD, "Hard", "The scholar famed for the most authentic hadith collection is",
     "Imam al-Bukhari", "Imam al-Shafii", "Imam Malik", "Imam Ahmad", "A",
     "His Sahih is the most rigorously checked."),
    (T_HAD, "Medium", "Sahih al-Bukhari is paired in authenticity with the collection of",
     "Imam Muslim", "Imam al-Tirmidhi", "Imam al-Nasai", "Imam Ibn Majah", "A",
     "The two Sahihs stand together."),
    (T_HAD, "Hard", "The four books termed the Sunan works include the collections of Abu Dawud, al-Tirmidhi, al-Nasai and",
     "Ibn Majah", "Imam Malik", "Ahmad ibn Hanbal", "al-Bukhari", "A",
     "Together with the Sahihs they make six."),
    (T_HAD, "Medium", "Al-Arba'in, a famous collection of forty hadith, was compiled by",
     "Imam al-Nawawi", "Imam al-Ghazali", "Ibn Khaldun", "Ibn Taymiyyah", "A",
     "His forty selections are memorised widely."),
    (T_HAD, "Medium", "The Sunnah of the Prophet means his",
     "way of life and example", "written letters only", "family tree", "battles alone", "A",
     "Sayings, deeds and approvals."),

    # ------------------------------------------------------------- ibadah
    (T_IBAD, "Medium", "Wudu is invalidated by using the toilet and by",
     "sleeping deeply", "walking to the mosque", "eating dates", "reading Quran", "A",
     "Deep sleep breaks the purity."),
    (T_IBAD, "Hard", "Wiping over the leather socks in wudu is allowed for a traveller for up to",
     "three days and nights", "one full day only", "seven days", "half a day", "A",
     "The traveller enjoys three days."),
    (T_IBAD, "Medium", "Tayammum is performed with",
     "clean earth", "sea water", "sand and soap", "warm stone oil", "A",
     "Pure soil replaces water."),
    (T_IBAD, "Medium", "Salah is not valid without first facing the",
     "qiblah", "minbar", "qunut", "mihrab of steel", "A",
     "Makkah fixes the direction."),
    (T_IBAD, "Hard", "How many fard rak'ahs does the sunset prayer contain?",
     "three", "two", "four", "five", "A",
     "Only Maghrib has three rak'ahs."),
    (T_IBAD, "Hard", "The Friday congregational prayer replaces which salah?",
     "Zuhr", "Asr", "Fajr", "Isha", "A",
     "Jumu'ah stands in for Zuhr."),
    (T_IBAD, "Medium", "What is the name of the address given before the Friday prayer?",
     "khutbah", "adhan", "iqamah", "talbiyah", "A",
     "It is preached from the minbar."),
    (T_IBAD, "Hard", "The eclipse prayer, salat al-kusuf, is an example of",
     "a nafl prayer", "a fard prayer", "janazah prayer", "istisqa only", "A",
     "It is voluntary and urged."),

    # ------------------------------------------------------------- zakah and sawm
    (T_ZAK, "Medium", "Zakah becomes due on wealth that has been held for",
     "one full lunar year", "six months", "two years", "one month", "A",
     "A hawl must pass over it."),
    (T_ZAK, "Hard", "The nisab for gold on which zakah is due is",
     "85 grams", "50 grams", "100 grams", "200 grams", "A",
     "Twenty mithqal make the threshold.", "85"),
    (T_ZAK, "Hard", "The rate of zakah on saved money is",
     "2.5 per cent", "10 per cent", "5 per cent", "20 per cent", "A",
     "A fortieth of the savings.", "2.5"),
    (T_ZAK, "Medium", "Zakat al-fitr is paid",
     "before the Eid prayer", "after Eid day", "on Ashura", "in Muharram", "A",
     "It must reach the poor before the feast."),
    (T_ZAK, "Medium", "Sadaqah differs from zakah because it is",
     "voluntary at any time", "fixed by law", "paid to the sultan", "only for the rich", "A",
     "Any amount, any day, any giver."),
    (T_ZAK, "Hard", "The sick and travellers who cannot fast must",
     "make up the days later", "feed one person per day forever", "skip fasting entirely", "pay gold instead only", "A",
     "Qada restores the missed days."),
    (T_ZAK, "Hard", "The pre-dawn meal before a fast begins is called",
     "suhur", "iftar", "imsak", "fidyah", "A",
     "It is a blessing before dawn."),
    (T_ZAK, "Medium", "Breaking the fast at sunset is called",
     "iftar", "suhur", "qada", "tawaf", "A",
     "Dates and water traditionally open it."),

    # ------------------------------------------------------------- hajj
    (T_HAJJ, "Medium", "The first rite of hajj on entering ihram is the",
     "intention and talbiyah", "stoning", "sa'y", "qurbani", "A",
     "The pilgrim declares his purpose."),
    (T_HAJJ, "Hard", "The great standing at Arafat falls on which date?",
     "ninth of Dhul-Hijjah", "tenth of Dhul-Hijjah", "first of Muharram", "eighth of Ramadan", "A",
     "The day of Arafat is the hajj's heart."),
    (T_HAJJ, "Medium", "The night spent in the open after Arafat is at",
     "Muzdalifah", "Mina", "Marwah", "Safa", "A",
     "Pilgrims rest there before Mina."),
    (T_HAJJ, "Medium", "The seven circuits around the Ka'bah are called",
     "tawaf", "sa'y", "rami", "ihram", "A",
     "The circumambulation rounds the House."),
    (T_HAJJ, "Medium", "Running between Safa and Marwah is the rite of",
     "sa'y", "tawaf", "qasr", "jamrat", "A",
     "It recalls Hajar's desperate search."),
    (T_HAJJ, "Hard", "Stoning the three pillars at Mina is known as",
     "rami al-jamarat", "tawaf al-wida", "sa'y al-safa", "wuquf al-arafah", "A",
     "Pebbles are cast at each jamrah."),
    (T_HAJJ, "Hard", "Umrah differs from hajj because it",
     "can be done any time of year", "needs no ihram", "excludes tawaf", "is obligatory for all", "A",
     "No fixed season binds umrah."),

    # ------------------------------------------------------------- family
    (T_FAM, "Medium", "A valid nikah requires the consent of both parties and",
     "two witnesses", "ten witnesses", "a written contract only", "a judge alone", "A",
     "Two just witnesses suffice."),
    (T_FAM, "Medium", "The gift the groom gives the bride at marriage is the",
     "mahr", "sadaqah al-fitr", "zakat al-mal", "hadiyah", "A",
     "It is hers by right, not the family's."),
    (T_FAM, "Hard", "The waiting period a wife observes after divorce is called",
     "iddah", "qada", "khulu", "muhallil", "A",
     "Its length varies by circumstance."),
    (T_FAM, "Hard", "A wife may return her mahr to end the marriage through",
     "khul", "talaq", "zihar", "lian", "A",
     "She buys her release from it."),
    (T_FAM, "Medium", "Kindness to parents is commanded in the Quran immediately after",
     "worship of Allah", "payment of zakah", "fasting in Ramadan", "performance of hajj", "A",
     "Right after the duty to God."),
    (T_FAM, "Medium", "Aqiqah, the sacrifice for a newborn, involves",
     "two sheep for a boy, one for a girl", "one sheep for a boy only", "a camel in every case", "no animal at all", "A",
     "The infant's head is also shaved."),

    # ------------------------------------------------------------- inheritance and transactions
    (T_INH, "Hard", "A wife whose husband dies leaving a child inherits",
     "one-eighth of the estate", "one-fourth of the estate", "one-half of the estate", "one-third of the estate", "A",
     "The Quran fixes her share."),
    (T_INH, "Hard", "When children survive them, parents of the deceased each take",
     "one-sixth", "one-eighth", "one-fourth", "one-third", "A",
     "Their share is a sixth each."),
    (T_INH, "Medium", "The shares of heirs in faraid are calculated only from the estate after",
     "debts and bequests are settled", "the family meeting", "the burial only", "taxes at the bank", "A",
     "The dead's obligations come first."),
    (T_INH, "Medium", "Riba, forbidden in the Quran, means",
     "interest on loans", "trade profit", "rent on houses", "wages for work", "A",
     "Any predetermined excess is banned."),
    (T_INH, "Hard", "A sale is invalid in shariah if the seller",
     "conceals a defect in the goods", "offers a fair discount", "shows the goods first", "accepts bargaining", "A",
     "Honesty must govern trade."),

    # ------------------------------------------------------------- seerah
    (T_SEER, "Medium", "The Prophet received his first revelation in the cave of",
     "Hira", "Thawr", "Uhud", "Badr", "A",
     "The cave lies above Makkah."),
    (T_SEER, "Hard", "The first words revealed to the Prophet began with",
     "Iqra", "Alhamdu", "Qul huwa", "Yaa ayyuha", "A",
     "Read, in the name of your Lord."),
    (T_SEER, "Medium", "The migration to Madinah took place in the year",
     "622 CE", "610 CE", "632 CE", "630 CE", "A",
     "It marks the start of the hijri calendar.", "622"),
    (T_SEER, "Hard", "At Hudaybiyyah the Prophet signed with the Makkans a treaty that proved",
     "a peaceful victory", "a military defeat", "a broken truce at once", "a trade pact only", "A",
     "The Quran called it a clear win."),
    (T_SEER, "Hard", "The rightly guided caliphs, in order, are Abu Bakr, Umar, Uthman and",
     "Ali", "Muawiyah", "Umar II", "Yazid", "A",
     "The fourth succeeded in 656."),
    (T_SEER, "Medium", "Who led the community as caliph immediately after the Prophet passed?",
     "Abu Bakr", "Umar", "Uthman", "Ali", "A",
     "The close friend led first."),
    (T_SEER, "Hard", "The caliph under whose rule the Quran was compiled into one book was",
     "Uthman", "Ali", "Umar", "Abu Bakr", "A",
     "He standardised the copies."),

    # ------------------------------------------------------------- aqidah
    (T_AQID, "Medium", "The doctrine of Allah's absolute oneness is termed",
     "tawhid", "risalah", "akhirah", "taqwa", "A",
     "The first pillar of faith."),
    (T_AQID, "Hard", "Ascribing partners to Allah is the sin of",
     "shirk", "nifaq", "bid'ah", "kufr only", "A",
     "It is the unforgiven if unrepented."),
    (T_AQID, "Medium", "Belief in the prophets, books, angels, the last day and destiny are the articles of",
     "iman", "islam", "ihsan", "ijma", "A",
     "Faith's pillars are listed as these."),
    (T_AQID, "Medium", "Ihsan, the highest degree of religion, means to worship Allah",
     "as if you see Him", "only in Ramadan", "with the tongue only", "inside the mosque only", "A",
     "He sees you though you see Him not."),
    (T_AQID, "Medium", "Which month opens the hijri year?",
     "Muharram", "Ramadan", "Shawwal", "Dhul-Hijjah", "A",
     "The new year opens with it."),
    (T_AQID, "Hard", "Laylat al-qadr, better than a thousand months, is sought in the last ten nights of",
     "Ramadan", "Shaban", "Dhul-Hijjah", "Muharram", "A",
     "It falls in the odd nights."),
]

build_batch(
    S,
    "batch_106_waec_irs3.json",
    "106",
    "WAEC Islamic Studies round 3 (Round 21 top-up): hadith science "
    "(isnad and matn, Bukhari and Muslim, the Sunan works, Nawawi's "
    "Forty), wudu invalidators, khuff wiping, tayammum, qiblah, Maghrib "
    "rak'ahs, Jumu'ah and khutbah, salat al-kusuf, zakah hawl, nisab "
    "85 g, 2.5% rate, zakat al-fitr timing, sadaqah, qada for the sick "
    "and traveller, suhur and iftar, hajj rites in order (ihram and "
    "talbiyah, Arafat on 9 Dhul-Hijjah, Muzdalifah, tawaf, sa'y, rami "
    "al-jamarat), umrah's open season, nikah witnesses, mahr, iddah, "
    "khul, parents next to worship, aqiqah, faraid shares (wife 1/8, "
    "parents 1/6), debts before shares, riba, defect-free sales, cave "
    "Hira, Iqra, 622 CE, Hudaybiyyah, the four caliphs, Uthman's "
    "compilation, tawhid, shirk, articles of iman, ihsan, Muharram and "
    "laylat al-qadr. Scanned against WAEC rounds 1-2, NECO IRS and the "
    "JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
