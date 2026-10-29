"""Batch 241 - NECO Christian Religious Studies round 7 (NECO top-up, R49).

Grows NECO CRS from 268 toward ~293 with angles verified absent from
the whole CRS pool (1,617 items across JAMB, WAEC and NECO — the
deepest pool scanned). Fresh angles: healing of the withered hand on
the Sabbath; Paul's thorn in the flesh; Demetrius and the silver
shrines at Ephesus; Ehud and Eglon; Athaliah; Ebed-melech's rescue
of Jeremiah; Samson's riddle; Jotham's bramble fable; Stephanas;
Ahithophel; Hiram of Tyre; Elijah and the captains of fifty; Elisha
healing Jericho's water; the widow's oil; Hezekiah's sundial; Job's
miserable comforters; the seven churches; the 144,000 sealed; the
mark of the beast; the four horsemen; the two witnesses; the
Ebenezer stone; Samuel's farewell integrity ("whose ox have I
taken?"); Saul among the prophets; Joash's chest for temple repair.
Avoided as banked: the whole R46/R47 harvest and every classic
verified then — Nicodemus, walking on water, coin in fish's mouth,
Syrophoenician, feeding four thousand, feed my sheep, fruit of the
Spirit, Onesimus, Eutychus, Dorcas, Simon Magus, Malta/Publius,
Hosea/Gomer, Gideon's fleece, Jehoshaphat, Micaiah, Baruch,
Zerubbabel, Jael, Naomi/Orpah, Jerusalem council, James's death,
Agrippa, Gamaliel, Apollos, watchman, cast lots, jailer, yoke, tree
of life, Gibeon, Balaam, Nadab/Abihu, Miriam, bronze serpent,
Gideon's 300, Hannah, Hophni/Phinehas, Endor, Abigail/Nabal,
En-Gedi, Sheba, Ahaziah-line (captains 0 direct), Uzziah, Daniel's
food, Obadiah's prophets, census/Araunah, Simeon/Anna, Damascus,
basket, Barnabas-field, Lydia, Felix-Festus family, elders/living
creatures, marriage supper, and all R46–R48 items.

    python3 scripts/build_neco_batch241.py -> content/batch_241_neco_crs7.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Christian Religious Studies"

T_MIN = "The Ministry of Jesus"
T_LET = "Letters and Teachings"
T_WIDE = "Ministry and the Wider Church"
T_JUD = "Joshua and the Judges"
T_MON = "Kings and the Monarchy"
T_PRO = "The Prophets"
T_KINGS = "The Kings of Israel"
T_LATE = "Later Kings and Exiles"
T_WIS = "Daniel to Esther"
T_THEME = "Themes and Teachings"
T_EARLY = "Judges and Early Kings"

PASSAGES = []
PQ = []

Q = [
    (T_MIN, "Medium", "In the synagogue, Jesus healed a man whose right hand was withered, even though it was the Sabbath and the scribes watched to accuse him. The healing showed that",
     "doing good is lawful on the Sabbath", "the Sabbath forbids all healing",
     "the scribes were right to be angry", "the man had broken the law", "A",
     "Mercy does not check the calendar first."),
    (T_LET, "Hard", "Paul pleaded three times for the removal of the 'thorn in the flesh' given to keep him from being too elated. God's answer was that",
     "his grace was sufficient for Paul", "the thorn would be removed at once",
     "Paul should pray a fourth time", "the thorn was a punishment for sin", "A",
     "Strength, not removal, was the gift."),
    (T_WIDE, "Hard", "At Ephesus, the silversmith who stirred up a riot against Paul because the gospel was ruining the trade in silver shrines was",
     "Demetrius", "Tyrannus",
     "Apollos", "Alexander", "A",
     "His craft, he said, was in danger from the Way."),
    (T_JUD, "Hard", "Ehud, the left-handed judge who delivered Israel from Moab, killed the fat king Eglon by",
     "stabbing him with a hidden dagger", "poisoning his wine",
     "burning his palace", "strangling him at night", "A",
     "A left hand carried what the guards never checked."),
    (T_MON, "Medium", "After Ahaziah's death, his mother destroyed the royal offspring of Judah and reigned herself for six years, until the boy Joash was crowned. This only queen to rule Judah was",
     "Athaliah", "Jezebel",
     "Maacah", "Herodias", "A",
     "She took the throne by blood and lost it the same way."),
    (T_PRO, "Hard", "When Jeremiah was lowered into the muddy cistern to die, the Ethiopian court official who pulled him out with ropes and old rags was",
     "Ebed-melech", "Baruch",
     "Gedaliah", "Zedekiah", "A",
     "A foreigner's kindness saved the prophet of doom."),
    (T_JUD, "Hard", "Samson bet the Philistines thirty garments over a riddle he drew from a lion and honey: 'Out of the eater came something to eat.' The riddle was solved only because",
     "his wife coaxed the answer from him", "the Philistines reasoned it out",
     "he told his companions at once", "a shepherd reported the lion", "A",
     "She pressed him day after day until he told her."),
    (T_JUD, "Hard", "After the men of Shechem made Abimelech king, Jotham stood on Mount Gerizim and told the fable of the trees that chose as their king",
     "the bramble", "the olive",
     "the fig", "the vine", "A",
     "The only tree that offered shadow by burning others."),
    (T_LET, "Hard", "Paul commended the household of Stephanas as the first converts of Achaia, who",
     "devoted themselves to serving the saints", "refused to support the church at all",
     "sided with Paul's opponents in Corinth", "left the faith soon after their baptism", "A",
     "First-fruits of a province, and serving still."),
    (T_KINGS, "Hard", "During Absalom's rebellion, David's counsellor whose wisdom was so trusted that it was said to be as the oracle of God — and who hanged himself when his advice was rejected — was",
     "Ahithophel", "Hushai",
     "Joab", "Abner", "A",
     "The wisest head of the kingdom broke when the king no longer heard it."),
    (T_KINGS, "Medium", "The king of Tyre who supplied cedar trees and craftsmen for the building of Solomon's temple, in exchange for wheat and oil, was",
     "Hiram", "Hadad",
     "Ben-hadad", "Toi", "A",
     "Lebanon's cedar came to Jerusalem by his friendship."),
    (T_KINGS, "Hard", "When King Ahaziah sent a captain with fifty men to arrest Elijah, the prophet called down fire from heaven that consumed them. This happened",
     "twice before the third captain was spared", "only once in the whole story",
     "three times with no sparing", "to the third captain only", "A",
     "Two companies burned; the third captain begged humbly and lived."),
    (T_PRO, "Hard", "The men of Jericho complained that their water was bad and the land unfruitful. Elisha healed the water by",
     "throwing salt into it", "praying over a stone",
     "digging a new well", "pouring oil on the bank", "A",
     "A bowl of salt made the spring sweet to this day."),
    (T_PRO, "Hard", "The widow whose two sons were about to be taken as slaves filled every vessel she could borrow with oil from one small jar, sold the oil and paid her debts, after Elisha told her to",
     "borrow empty vessels from her neighbours", "beg for alms at the city gate",
     "sell her house and land at once", "take her case before the king", "A",
     "The oil flowed as long as a vessel waited to receive it."),
    (T_LATE, "Hard", "As a sign that he would recover, God made the shadow on the steps of Ahaz go back",
     "ten steps", "one step",
     "forty steps", "three steps", "A",
     "The sundial ran backward for the dying king."),
    (T_WIS, "Hard", "Job called his friends who came to comfort him in his suffering",
     "miserable comforters", "faithful companions",
     "heavenly messengers", "silent witnesses", "A",
     "They came to console him and ended accusing him."),
    (T_THEME, "Medium", "In the book of Revelation, the risen Christ instructs John to write to the churches of Asia, among them Ephesus, Smyrna, Sardis, Laodicea and",
     "Philadelphia", "Philippi",
     "Corinth", "Thessalonica", "A",
     "Seven lampstands, seven letters to seven cities."),
    (T_THEME, "Hard", "In the book of Revelation, the servants of God who are sealed on their foreheads before the winds of destruction are released number",
     "144,000", "12,000",
     "7,000", "666", "A",
     "Twelve tribes, twelve thousand from each."),
    (T_THEME, "Hard", "The number 666 in the book of Revelation is",
     "the mark of the beast", "the number of the sealed",
     "the years of exile", "the count of the elders", "A",
     "It marks those who follow the beast instead of the Lamb."),
    (T_THEME, "Hard", "In the book of Revelation, the Lamb opens the seals and four horsemen ride out — white, red, black and pale — carrying conquest, war, famine and",
     "death", "peace",
     "plague of frogs", "wealth", "A",
     "The pale horse and its rider are named Death."),
    (T_THEME, "Hard", "In the book of Revelation, the two olive trees and lampstands who prophesy and cannot be harmed by fire until they finish their testimony are",
     "the two witnesses", "the two angels of Sodom",
     "Moses and Aaron only", "the two thieves", "A",
     "For three and a half days no enemy could silence them."),
    (T_EARLY, "Medium", "After the Lord had helped Israel to victory over the Philistines at Mizpah, Samuel set up a stone between Mizpah and Jeshanah and called its name",
     "Ebenezer, saying 'thus far the Lord has helped us'", "Peniel, saying 'I have seen God'",
     "Bethel, saying 'this is God's house'", "Gilgal, saying 'the reproach is rolled away'", "A",
     "The stone of help remembered every battle past."),
    (T_EARLY, "Medium", "At his farewell, Samuel asked Israel to testify against him: whose ox or donkey had he taken, or whom had he defrauded? The people answered that",
     "he had taken nothing from anyone", "he owed them all compensation",
     "he had robbed the widows", "his sons must repay the people", "A",
     "A lifetime in office without a single petition against him."),
    (T_EARLY, "Hard", "When the people saw Saul prophesying among the prophets, they asked in wonder",
     "'Is Saul also among the prophets?'", "'Who is Saul's father?'",
     "'Have the prophets gone mad?'", "'Is Samuel dead?'", "A",
     "The proverb is repeated to this day."),
    (T_MON, "Medium", "When the temple repairs had long been neglected, the priests were commanded to put a chest with a hole in its lid beside the altar, into which the people",
     "dropped money for the house of the Lord", "placed their sins on paper",
     "threw incense for the king", "kept the scrolls of the law", "A",
     "The chest filled, and the house was repaired."),
]

build_batch(
    S,
    "batch_241_neco_crs7.json",
    "241",
    "NECO CRS round 7 (R49 top-up): withered hand on the Sabbath; "
    "Paul's thorn in the flesh; Demetrius' silver shrines; Ehud and "
    "Eglon; Athaliah; Ebed-melech; Samson's riddle; Jotham's bramble "
    "fable; Stephanas; Ahithophel; Hiram of Tyre; Elijah and the "
    "captains of fifty; Elisha healing Jericho's water; the widow's "
    "oil; Hezekiah's sundial; Job's miserable comforters; seven "
    "churches; the 144,000; the mark of the beast 666; the four "
    "horsemen; the two witnesses; Ebenezer stone; Samuel's farewell "
    "integrity; Saul among the prophets; Joash's chest for temple "
    "repair. Scanned against the whole CRS pool (JAMB, WAEC and "
    "NECO stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
