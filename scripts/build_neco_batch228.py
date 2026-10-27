"""Batch 228 - NECO Islamic Studies round 8 (NECO top-up, R46).

Grows NECO IRS from 252 toward ~277 with angles verified absent from
the whole Islamic Studies pool (1,441 items across JAMB, WAEC and
NECO): sajdat al-tilawah; kutub al-sittah; four sacred months;
ruqyah; smiling as charity; removing harm from the road; Abd
al-Muttalib; Abu al-Qasim; adab of the mosque; tawakkul; enjoining
good and forbidding evil; mothers of the believers; Sahih
al-Bukhari's rank; the seedling hadith; Dajjal; Ya'juj and Ma'juj;
punishment of the grave; washing and shrouding the dead; ta'ziyah;
Abu Hurayrah as narrator; eating with the right hand; sajdat
al-shukr; adhkar; salat ad-duha; salawat on the Prophet. Checked
and avoided (already banked): miswak-in-fast, istighfar, Mansa
Musa, Hilf al-Fudul, Bahira, tawakkul-as-option (shukr item),
namimah, hasad/bukhl, visiting-the-sick rights item, Umar-Hijri
calendar (multiple), kutub-adjacent Bukhari items, Dar al-Arqam
(unverified single hit), tahnik, 313-Badr, muakhah (twice), Furqan,
Kawthar, dhikr item, right-hand (unverified single hit - kept,
scanner clean).

    python3 scripts/build_neco_batch228.py -> content/batch_228_neco_irs8.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Islamic Studies"

T_QUR = "The Qur'an"
T_HAD = "Hadith"
T_SIR = "Life of the Prophet (S.A.W.)"
T_IBA = "Further Ibadah"
T_MOR = "Islamic Moral Values"
T_AQD = "At-Tawhid and the Articles of Faith"
T_COMP = "The Companions"
T_FIQ = "Sources of Fiqh and Rulings"
T_CAL = "Islamic Calendar and Festivals"
T_JAN = "Angels and the Unseen"
T_WOM = "Notable Women of Islam"

PASSAGES = []
PQ = []

Q = [
    (T_IBA, "Medium", "Some verses of the Qur'an are marked with a symbol at which the reciter stops and prostrates during recitation. This prostration is called",
     "sajdat al-tilawah", "sajdat al-shukr",
     "sujud as-sahw", "ruku of recitation", "A",
     "The mark in the mushaf tells him to bow at once."),
    (T_HAD, "Medium", "The six most famous collections of hadith — Sahih al-Bukhari, Sahih Muslim, and the four sunan — are together known as",
     "the kutub al-sittah", "the kutub al-tafsir",
     "the suhuf of Ibrahim", "the mushaf collections", "A",
     "Six books stand above all others in the science."),
    (T_CAL, "Medium", "Four months of the Islamic year — Dhul-Qa'dah, Dhul-Hijjah, Muharram and Rajab — in which fighting is forbidden are called",
     "the sacred months", "the fasting months",
     "the months of tashriq", "the forbidden weeks", "A",
     "Even the tribes of old laid down arms in them."),
    (T_MOR, "Medium", "The practice of reciting Qur'anic verses, such as al-Fatihah and the last two surahs, as a prayer for healing from illness is called",
     "ruqyah", "ruku",
     "ribah", "ru'yah", "A",
     "The Prophet himself recited and blew over the sick."),
    (T_MOR, "Easy", "The Prophet (SAW) taught that smiling in the face of your brother is counted as",
     "an act of charity", "an act of pride",
     "a light sin", "a waste of time", "A",
     "Even a cheerful face earns a reward."),
    (T_MOR, "Easy", "Removing a harmful object, such as thorns or broken glass, from the path of people is taught in Islam as a branch of",
     "faith and an act of charity", "trade and commerce",
     "rulership and law", "war and strategy", "A",
     "A clear road is itself a form of kindness."),
    (T_SIR, "Easy", "Long before Islam, the Prophet's grandfather Abdul Muttalib was honoured in Makkah for",
     "rediscovering the buried well of Zamzam", "leading the army at Badr",
     "building the first mosque at Quba", "writing the first book of hadith", "A",
     "He cleared the buried spring and served its water."),
    (T_SIR, "Easy", "The Prophet (SAW) was known in Madinah by his kunya, or filial title,",
     "Abu al-Qasim", "Abu Talib",
     "Abu Bakr", "Abu Hurayrah", "A",
     "He was called after his little son Qasim."),
    (T_MOR, "Medium", "Raising one's voice in search of a lost item, quarrelling loudly or buying and selling inside the mosque go against the",
     "etiquette of the mosque", "rulings of qiyas",
     "rules of inheritance", "customs of the market", "A",
     "The house of Allah is for prayer and quiet counsel."),
    (T_AQD, "Medium", "Reliance on Allah after one has taken the proper lawful means, trusting that His plan is best, is called",
     "tawakkul", "tamakkul",
     "takabbur", "tasawwur", "A",
     "Tie your camel, then commit its safety to Him."),
    (T_MOR, "Medium", "Calling people to what is right and speaking against what is wrong, with wisdom and patience, is the duty known as",
     "enjoining good and forbidding evil", "commanding prayer and fasting only",
     "imposing taxes and levies", "declaring war and peace", "A",
     "The ummah's conscience lives by this duty."),
    (T_WOM, "Medium", "The wives of the Prophet (SAW), whom the Qur'an honours and who are forbidden to any man after him, are called",
     "the mothers of the believers", "the daughters of the Prophet",
     "the women of the Ansar", "the sisters of the Quraysh", "A",
     "Every believer honours them as his mothers."),
    (T_HAD, "Medium", "Among the books of hadith, the collection of Imam al-Bukhari is regarded by the scholars as",
     "the most authentic book after the Qur'an", "a book of law and tafsir only",
     "the earliest book of fiqh known", "a book of early poetry", "A",
     "Its chain-checking set the standard for all."),
    (T_MOR, "Medium", "The Prophet (SAW) said that if the Day of Resurrection comes while one of you holds a seedling, he should plant it if he can. The hadith teaches",
     "the value of work and hope to the very end", "the end of farming",
     "the duty to predict the Last Day", "the rejection of agriculture", "A",
     "Plant even at the end of the world."),
    (T_JAN, "Medium", "Near the end of time, a great deceiver will appear working false wonders and leading many astray. In the hadith he is called",
     "the Dajjal", "the Mahdi",
     "the Munkar", "the Qadar", "A",
     "The Prophet sought refuge from his trials."),
    (T_JAN, "Medium", "The two vast nations of destructiveness that will be released near the end of time and spread corruption are named in the Qur'an as",
     "Ya'juj and Ma'juj", "Sodom and Gomorrah",
     "the Romans and the Persians", "the Quraysh and the Abyssinians", "A",
     "Their breach is one of the great signs."),
    (T_AQD, "Medium", "The belief that the grave may hold questioning and either comfort or punishment for the dead before the Day of Resurrection is called",
     "the punishment of the grave", "the scales of the Mizan",
     "the crossing of the Sirat", "the waiting of Barzakh only", "A",
     "What answers the dead give matters at once."),
    (T_IBA, "Medium", "When a Muslim dies, the community's duty towards the body includes washing it, wrapping it in white cloth and burying it quickly. The white cloth is the",
     "shroud (kafan)", "ihram garment",
     "prayer mat", "burqa", "A",
     "Simple white cloth is the last garment."),
    (T_MOR, "Easy", "Visiting the family of the deceased to console them and pray for their dead, without wailing or extravagance, is called",
     "ta'ziyah", "tajwiz",
     "tamattu", "taqlid", "A",
     "Standing with the bereaved lightens their load."),
    (T_COMP, "Medium", "The companion who narrated the largest number of hadith from the Prophet (SAW), thanks to his constant companionship, is",
     "Abu Hurayrah", "Abu Dharr",
     "Ammar ibn Yasir", "Salman al-Farisi", "A",
     "Over five thousand reports bear his chain."),
    (T_MOR, "Easy", "The Prophet (SAW) commanded that one should eat and drink with the right hand, because the left hand is used by",
     "the Shaytan", "the poor only",
     "the traveller", "the youngest child", "A",
     "Even at table, the right hand leads."),
    (T_IBA, "Easy", "A prostration of gratitude performed outside prayer when a blessing arrives or a calamity is averted is called",
     "sajdat al-shukr", "sajdat al-tilawah",
     "sujud as-sahw", "sujud al-istikharah", "A",
     "The thankful forehead touches the ground at once."),
    (T_IBA, "Medium", "The words of remembrance a Muslim recites at dawn and at dusk, glorifying Allah and seeking His protection, are called",
     "adhkar", "ajr payments",
     "istikharah", "i'tikaf", "A",
     "Morning and evening are the two guarded times."),
    (T_IBA, "Medium", "A voluntary prayer of two or more rak'ahs performed in the forenoon, after the sun has risen high, is called",
     "salat ad-duha", "salat at-tahajjud",
     "salat al-witr", "salat al-istisqa", "A",
     "Its time begins as the morning climbs."),
    (T_MOR, "Medium", "Invoking Allah's blessings and peace upon the Prophet (SAW), as the Qur'an commands the believers to do, is called",
     "salawat (salat alan-Nabi)", "salat al-jumu'ah",
     "salat al-kusuf", "salat al-eid", "A",
     "One blessing from us draws ten from Allah."),
]

build_batch(
    S,
    "batch_228_neco_irs8.json",
    "228",
    "NECO Islamic Studies round 8 (R46 top-up): sajdat al-tilawah; "
    "kutub al-sittah; four sacred months; ruqyah; smiling as "
    "charity; removing harm from the road; Abd al-Muttalib; Abu "
    "al-Qasim; adab of the mosque; tawakkul; enjoining good and "
    "forbidding evil; mothers of the believers; Sahih al-Bukhari's "
    "rank; the seedling hadith; Dajjal; Ya'juj and Ma'juj; "
    "punishment of the grave; washing and shrouding the dead; "
    "ta'ziyah; Abu Hurayrah as narrator; eating with the right "
    "hand; sajdat al-shukr; adhkar; salat ad-duha; salawat on the "
    "Prophet. Scanned against the whole Islamic Studies pool (JAMB, "
    "WAEC and NECO stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
