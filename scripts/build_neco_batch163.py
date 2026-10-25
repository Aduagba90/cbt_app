"""Batch 163 - NECO Islamic Studies round 6 (NECO top-up, R30).

Grows NECO IRS from 192 toward ~230 with angles not yet in the bank:
the five rulings of actions (fard, sunnah, mustahabb, mubah,
makruh, haram); hadith grades further (mutawatir, mashhur, gharib);
Ibn Abbas the interpreter; silver nisab and the 2.5% rate; umrah
rites (tawaf, sa'y between Safa and Marwah, halq, Zamzam); Uhud's
archers' lesson, Salman's trench idea, Hudaybiyyah's ten-year truce,
Hunayn and Tabuk; the Rashidun order; Umar's Hijri calendar; the
qiblah change in 2 AH; Laylat al-Qadr; the six articles of faith;
Aisha and Khadija; riba al-fadl vs nasi'ah; inheritance shares
(son double the daughter). Scanned against NECO rounds 1-4, WAEC IRS
(all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch163.py -> content/batch_163_neco_irs6.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Islamic Studies"

T_FIQH = "The Five Rulings of Actions"
T_HAD = "Hadith Grades Further"
T_IBAD = "Worship Detail Further"
T_SIR = "Battles and Treaties Further"
T_KHUL = "The Khulafa Further"
T_AQID = "Articles of Faith"
T_WOM = "Notable Women of Islam"
T_FIN = "Riba and Inheritance"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- five rulings
    (T_FIQH, "Medium", "An act commanded so firmly that omitting it earns blame, like the five prayers, is",
     "fard", "sunnah", "mubah", "makruh", "A",
     "Its neglect is answerable."),
    (T_FIQH, "Medium", "An act the Prophet did regularly though not commanded, such as the witr prayer, is",
     "sunnah", "fard", "haram", "mubah", "A",
     "Following it earns reward."),
    (T_FIQH, "Hard", "An act whose doing or leaving is equally permitted, like eating yam or rice, is",
     "mubah", "mustahabb", "fard", "makruh", "A",
     "The scale of law rests level."),
    (T_FIQH, "Hard", "An act better avoided though not sinful, such as drinking while standing, is",
     "makruh", "haram", "mubah", "fard", "A",
     "Disliked, but not forbidden."),
    (T_FIQH, "Medium", "An act whose doing earns punishment, like stealing, is",
     "haram", "makruh", "mustahabb", "mubah", "A",
     "The prohibition is absolute."),

    # ------------------------------------------------------------- hadith grades
    (T_HAD, "Hard", "A hadith reported by so many transmitters in every generation that collusion is impossible is",
     "mutawatir", "ahad", "gharib", "mursal", "A",
     "Countless tongues carry it."),
    (T_HAD, "Medium", "A hadith known from three or more narrators but not reaching the mutawatir crowd is",
     "mashhur", "gharib", "mursal", "munqati", "A",
     "Famous among the scholars."),
    (T_HAD, "Hard", "A hadith reported at some stage by a single narrator is graded",
     "gharib", "mutawatir", "mashhur", "sahih by unanimity", "A",
     "One lone link in the chain."),
    (T_HAD, "Hard", "The companion remembered as the Quran's interpreter, cousin of the Prophet, is",
     "Ibn Abbas", "Ibn Umar", "Ibn Mas'ud", "Ibn Zubayr", "A",
     "The Prophet prayed for his wisdom."),

    # ------------------------------------------------------------- worship detail
    (T_IBAD, "Hard", "Zakat becomes due on silver once its weight reaches",
     "200 dirhams", "100 dirhams", "85 grams of gold", "1,000 dirhams", "A",
     "Five wasq is not its measure; two hundred dirhams is.", "200"),
    (T_IBAD, "Medium", "On savings held for a full year, the rate of zakat is",
     "2.5%", "5%", "10%", "20%", "A",
     "A fortieth part of the hoard.", "2.5"),
    (T_IBAD, "Medium", "The running between the hills of Safa and Marwah during umrah or hajj is called",
     "sa'y", "tawaf", "rami", "wuquf", "A",
     "Hajar's search for water is honoured."),
    (T_IBAD, "Hard", "The ritual shaving or trimming of hair that ends ihram is",
     "halq or taqsir", "talbiyah", "istilam", "idtiba", "A",
     "The pilgrim leaves his consecrated state."),
    (T_IBAD, "Medium", "The sacred well that sprang for Hajar and Isma'il in Makkah is",
     "Zamzam", "Silsilah", "Kawthar", "Maryam", "A",
     "Its water still flows today."),
    (T_IBAD, "Hard", "The qiblah was changed from Jerusalem to the Ka'bah in the year",
     "2 AH", "1 AH", "5 AH", "10 AH", "A",
     "The congregation turned mid-prayer.", "2"),
    (T_IBAD, "Hard", "Worshippers seek it in the odd nights of the last ten of Ramadan, when the Quran first came down. That honoured night is",
     "Laylat al-Qadr", "Laylat al-Isra", "Laylat al-Bara'ah", "Yaum al-Arafah", "A",
     "The Quran descended in it."),

    # ------------------------------------------------------------- battles & treaties
    (T_SIR, "Hard", "The battle of Uhud was nearly won, then nearly lost, chiefly because the",
     "archers left the hill", "cavalry fled at dawn", "army ran out of water", "enemy used elephants", "A",
     "Their posting was their trust."),
    (T_SIR, "Hard", "The idea of digging a great trench to defend Madinah came from",
     "Salman al-Farisi", "Umar ibn al-Khattab", "Bilal ibn Rabah", "Khalid ibn al-Walid", "A",
     "Persia's wisdom served Islam."),
    (T_SIR, "Hard", "The truce of Hudaybiyyah provided for peace between the Muslims and Quraysh for",
     "ten years", "three years", "one year", "fifty years", "A",
     "War rested for a full decade."),
    (T_SIR, "Medium", "The battle fought in a valley after Makkah's fall, where numbers first deceived the Muslims, was",
     "Hunayn", "Tabuk", "Badr", "Khaybar", "A",
     "Many troops, early panic, late victory."),
    (T_SIR, "Hard", "The last army the Prophet personally led, marched in the heat toward Syria's border, was that of",
     "Tabuk", "Hunayn", "Uhud", "Mu'tah", "A",
     "The hard summer march tested hearts."),

    # ------------------------------------------------------------- khulafa
    (T_KHUL, "Medium", "The rightly-guided caliphs, listed first to last, begin with",
     "Abu Bakr, then Umar", "Umar, then Abu Bakr", "Uthman, then Ali", "Ali, then Uthman", "A",
     "The order follows the pledges."),
    (T_KHUL, "Hard", "The Hijri calendar, counting from the migration, was introduced under",
     "Umar ibn al-Khattab", "Abu Bakr", "Uthman ibn Affan", "Ali ibn Abi Talib", "A",
     "His reign ordered the years."),
    (T_KHUL, "Medium", "The caliph under whom the Quran's text was standardised into one dialect for all provinces was",
     "Uthman ibn Affan", "Umar", "Ali", "Mu'awiyah", "A",
     "He sent copies to the cities."),

    # ------------------------------------------------------------- articles of faith
    (T_AQID, "Hard", "Belief in Allah, His angels, His books, His messengers, the Last Day and",
     "destiny (qadar)", "the saints alone", "the caliphs only", "the scholars' councils", "A",
     "Six pillars hold the faith."),
    (T_AQID, "Medium", "To believe that both good and evil occur by Allah's knowledge is belief in",
     "qadar", "qiyas", "qunut", "qira'ah", "A",
     "Nothing escapes the divine decree."),
    (T_AQID, "Medium", "The phrase La ilaha illallah affirms chiefly",
     "the oneness of Allah", "the finality of prophethood", "the duty of pilgrimage", "the reality of angels", "A",
     "No god deserves worship but Him."),

    # ------------------------------------------------------------- notable women
    (T_WOM, "Hard", "The first person to believe in the Prophet's message was",
     "Khadijah", "Aisha", "Fatimah", "Sumayyah", "A",
     "She comforted him at the cave's return."),
    (T_WOM, "Hard", "The wife renowned as a great scholar of law and narrator of over two thousand hadiths is",
     "Aisha", "Khadijah", "Hafsah", "Zaynab", "A",
     "The companions consulted her memory."),
    (T_WOM, "Medium", "The first martyr of Islam, killed for her faith in Makkah, was",
     "Sumayyah", "Khadijah", "Fatimah", "Umm Salamah", "A",
     "Her steadiness cost her life."),

    # ------------------------------------------------------------- riba & inheritance
    (T_FIN, "Hard", "Excess demanded in an exchange of the same kind of goods, like gold for gold unequally, is",
     "riba al-fadl", "riba al-nasi'ah", "mudarabah", "murabaha", "A",
     "Equal measure is the rule."),
    (T_FIN, "Hard", "Interest charged for delaying repayment, the pre-Islamic increase on loans, is",
     "riba al-nasi'ah", "riba al-fadl", "qard hasan", "sadaqah", "A",
     "The waiting itself was priced."),
    (T_FIN, "Hard", "In inheritance, a son's share compared to a daughter's share is",
     "double", "equal", "half", "triple", "A",
     "Two shares stand beside one."),
    (T_FIN, "Medium", "A daughter who is the only child inherits from her father",
     "half the estate", "the whole estate", "a third", "a quarter", "A",
     "Half is hers; the rest goes to the wider family."),
    (T_FIN, "Medium", "A loan advanced purely to help, with no increase sought, is called",
     "qard hasan", "riba al-fadl", "maysir", "gharar", "A",
     "The good loan returns only itself."),
]

build_batch(
    S,
    "batch_163_neco_irs6.json",
    "163",
    "NECO Islamic Studies round 6 (R30 top-up): five rulings (fard, "
    "sunnah, mubah, makruh, haram); mutawatir, mashhur, gharib grades; "
    "Ibn Abbas; silver nisab 200 dirhams, 2.5% rate; sa'y between Safa "
    "and Marwah, halq, Zamzam, qiblah change 2 AH, Laylat al-Qadr; "
    "Uhud's archers, Salman's trench, Hudaybiyyah ten-year truce, "
    "Hunayn, Tabuk; Rashidun order, Umar's Hijri calendar, Uthman's "
    "standardisation; six articles with qadar; Khadijah first "
    "believer, Aisha the scholar, Sumayyah first martyr; riba al-fadl "
    "vs nasi'ah, son's double share, only daughter's half, qard "
    "hasan. Scanned against NECO rounds 1-4, WAEC IRS (all rounds) "
    "and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
