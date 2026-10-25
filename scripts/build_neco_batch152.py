"""Batch 152 - NECO Christian Religious Studies round 4 (NECO top-up, R28).

Grows NECO CRS from 177 toward ~213 with narrative angles not yet in
the bank: the image of God and the Sabbath; the serpent's sentence and
Cain's protective mark; the rainbow covenant; Babel's tongues;
circumcision as covenant sign; Abraham's intercession for Sodom;
Jacob's ladder and his new name; Joseph sold for silver; the Nile's
blood, Jethro's judges, the golden calf and Balaam's donkey; Nebo,
the Jordan crossing and Jericho's march; Samuel's call and the demand
for a king; David's mercy in the cave and Jonathan's covenant;
Solomon's temple; ravens, Zarephath, Amos, Hosea, Jonah's Nineveh and
Daniel's pulse; the shepherds' song, the flight to Egypt, Cana,
Nicodemus, the stilled storm, the cleansed temple, Judas' price and
the promise to the thief; the seven deacons, the Ethiopian eunuch and
the viper at Malta. Scanned against NECO rounds 1-3, WAEC CRS (all
rounds) and the JAMB pool.

    python3 scripts/build_neco_batch152.py -> content/batch_152_neco_crs4.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Christian Religious Studies"

T_EARLY = "Genesis Narratives"
T_PAT = "Patriarchs"
T_EXO = "Moses to the Jordan"
T_KING = "Judges and Kings"
T_PRO = "Prophets Further"
T_GOS = "Gospel Narratives"
T_ACT = "The Acts of the Apostles"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- Genesis
    (T_EARLY, "Medium", "Man's special dignity in creation comes from being made",
     "in the image of God", "from river clay", "on the first day", "without a mate", "A",
     "God's own likeness sets him apart."),
    (T_EARLY, "Medium", "God blessed and hallowed the seventh day because on it He",
     "rested from creation", "planted Eden", "made the animals", "sent the rain", "A",
     "Rest crowned the finished work."),
    (T_EARLY, "Medium", "For deceiving Eve, the serpent was condemned to",
     "crawl on its belly", "drown in the sea", "serve the woman", "guard Eden", "A",
     "Dust became its food for ever."),
    (T_EARLY, "Hard", "The mark placed on Cain was meant to",
     "protect him from being killed", "brand him a king", "heal his wound", "harden his hand", "A",
     "Justice walked with mercy."),
    (T_EARLY, "Medium", "After the flood, God set the rainbow in the clouds as the sign of His",
     "covenant with creation", "anger at sin", "love of colours", "plague on Egypt", "A",
     "Every bow repeats the promise."),
    (T_EARLY, "Medium", "The tower of Babel project collapsed when God",
     "confused their languages", "burned the bricks", "raised the sea", "sent a famine", "A",
     "Words scattered the builders."),

    # ------------------------------------------------------------- patriarchs
    (T_PAT, "Hard", "In His covenant with Abraham, God appointed as its sign the rite of",
     "circumcision", "sacrifice of lambs", "keeping the Sabbath", "burnt incense", "A",
     "Every male child bore the mark."),
    (T_PAT, "Hard", "Pleading for Sodom, Abraham bargained with God from fifty righteous souls down to",
     "ten", "twenty", "five", "one", "A",
     "For ten the city would have stood."),
    (T_PAT, "Medium", "On the run from Esau, Jacob slept at Bethel and dreamed of a stairway to heaven on which were",
     "angels going up and down", "a burning bush", "a river of oil", "seven cows", "A",
     "He woke and named the place God's house."),
    (T_PAT, "Medium", "After wrestling till daybreak, Jacob received the new name",
     "Israel", "Abraham", "Judah", "Peter", "A",
     "He had striven with God and men."),
    (T_PAT, "Hard", "Joseph's jealous brothers sold him to the Ishmaelite traders for",
     "twenty pieces of silver", "thirty pieces of silver", "two camels", "a parcel of land", "A",
     "Twenty coins began his road to Egypt."),

    # ------------------------------------------------------------- exodus to Jordan
    (T_EXO, "Hard", "The first of the ten plagues turned Egypt's river into",
     "blood", "frogs", "darkness", "hail", "A",
     "The Nile itself bore the sign."),
    (T_EXO, "Hard", "Jethro advised his son-in-law Moses to lighten his burden by appointing",
     "able men as judges", "more priests", "stronger soldiers", "temple singers", "A",
     "Rulers of thousands, fifties and tens."),
    (T_EXO, "Hard", "Confronted over the golden calf, Aaron excused himself by saying",
     "the people gave him the gold", "Moses commanded it", "God approved it", "a stranger cast it", "A",
     "He blamed the crowd he led."),
    (T_EXO, "Medium", "On the road to Moab, the angel of the Lord stood in the way, seen first by",
     "Balaam's donkey", "Balaam himself", "Balak's guards", "the sheep dogs", "A",
     "The beast saw what the seer could not."),
    (T_EXO, "Medium", "Moses was allowed only to view the promised land from",
     "Mount Nebo", "Mount Sinai", "Mount Carmel", "the plains of Moab", "A",
     "He saw it and did not enter."),
    (T_EXO, "Medium", "At the crossing of the Jordan, the priests carrying the ark",
     "stood in the riverbed", "stayed behind", "sounded trumpets", "sacrificed first", "A",
     "The waters parted at their feet."),
    (T_EXO, "Medium", "Jericho's wall fell after Israel marched round the city",
     "seven times on the seventh day", "once at midnight", "three days without stopping", "while the priests sang", "A",
     "A shout followed the seventh circuit."),

    # ------------------------------------------------------------- judges and kings
    (T_KING, "Medium", "The boy Samuel answered God's night call with the words",
     "'Speak, for your servant hears'", "'Here am I, send me'", "'Who shall go for us?'", "'My soul magnifies the Lord'", "A",
     "Eli taught him the fitting reply."),
    (T_KING, "Medium", "Israel's demand for a king was rooted in their wish to be",
     "like all the nations", "a holy priesthood", "ruled by judges forever", "free of the law", "A",
     "Samuel warned them of the cost."),
    (T_KING, "Hard", "When David found Saul asleep in the cave at En-Gedi, he only",
     "cut off the corner of his robe", "touched his spear", "woke him gently", "fled in silence", "A",
     "He spared the LORD's anointed."),
    (T_KING, "Medium", "The covenant friendship that endured through Saul's rage bound David to",
     "Jonathan", "Abner", "Joab", "Ahimelech", "A",
     "Their souls were knit together."),
    (T_KING, "Medium", "The permanent house of God in Jerusalem, replacing the tabernacle tent, was the temple built by",
     "Solomon", "David", "Ezra", "Herod", "A",
     "Cedars of Lebanon roofed its halls."),

    # ------------------------------------------------------------- prophets
    (T_PRO, "Hard", "During the drought, God fed Elijah by the brook Cherith through",
     "ravens bringing food", "manna each dawn", "a widow's bread", "an angel's touch", "A",
     "Birds waited on the prophet."),
    (T_PRO, "Hard", "In Zarephath, the widow's jar of flour and cruse of oil",
     "never ran dry", "turned to wine", "were stolen", "fed only her son", "A",
     "A little, blessed, became enough."),
    (T_PRO, "Medium", "The prophet Amos was, by his own account, a",
     "shepherd from Tekoa", "priest of Bethel", "scribe of Jerusalem", "prince of Judah", "A",
     "He followed the flock before the call."),
    (T_PRO, "Hard", "God told His prophet to marry a wife of harlotry and name the children Lo-Ruhamah and Lo-Ammi. Hosea's marriage to Gomer dramatised",
     "Israel's unfaithfulness to God", "the exile of Judah", "the fall of Samaria", "the rise of David", "A",
     "A broken home preached to the nation."),
    (T_PRO, "Medium", "After the fish spat him ashore, Jonah preached in Nineveh and the whole city",
     "repented in sackcloth", "stoned him", "ignored him", "banished him", "A",
     "Even the cattle wore the cloth."),
    (T_PRO, "Hard", "In Babylon, Daniel and his friends kept their purity by refusing the king's food and eating",
     "vegetables and water", "bread and wine", "fish only", "milk and honey", "A",
     "Ten days proved them fairer."),

    # ------------------------------------------------------------- gospel narratives
    (T_GOS, "Medium", "The angels' birth-song over Bethlehem's shepherds began,",
     "'Glory to God in the highest'", "'Fear not, little flock'", "'Blessed is he who comes'", "'Holy, holy, holy'", "A",
     "Peace on earth followed it."),
    (T_GOS, "Medium", "Warned in a dream, Joseph took the child Jesus and Mary and fled into",
     "Egypt", "Nazareth", "Syria", "the wilderness", "A",
     "Herod's sword pursued them."),
    (T_GOS, "Medium", "At the wedding in Cana of Galilee, Jesus performed His first sign by turning",
     "water into wine", "bread into fish", "stones to bread", "sea into dry land", "A",
     "The master of the feast tasted it."),
    (T_GOS, "Hard", "By night Nicodemus learned from Jesus that entry into the kingdom requires being",
     "born again", "circumcised", "baptised by John", "a scribe", "A",
     "Spirit gives birth to spirit."),
    (T_GOS, "Medium", "Christ ended the storm on the Sea of Galilee with the words",
     "'Peace, be still'", "'Follow me', 'Come out of him'", "'Talitha, cumi'", "'Ephphatha'", "A",
     "The wind died into a calm."),
    (T_GOS, "Medium", "Jesus drove the money-changers from the temple because they had made His Father's house",
     "a den of robbers", "a house of prayer", "a school of law", "a market of doves", "A",
     "Tables turned and doves flew."),

    # ------------------------------------------------------------- passion & acts
    (T_ACT, "Hard", "Judas Iscariot agreed to betray Jesus for",
     "thirty pieces of silver", "twenty pieces of gold", "a parcel of land", "a place at table", "A",
     "The price of a slave's life."),
    (T_ACT, "Hard", "To the penitent thief crucified beside Him, Jesus promised",
     "'Today you will be with me in paradise'", "'You will be remembered'", "'Your faith has saved you'", "'Ask and it shall be given'", "A",
     "Mercy reached the cross itself."),
    (T_ACT, "Medium", "To serve tables and free the apostles for prayer, the early church chose",
     "seven men full of the Spirit", "twelve elders", "Levites only", "Roman officers", "A",
     "Stephen was first upon the list."),
    (T_ACT, "Medium", "Philip explained Isaiah's suffering-servant passage to the",
     "Ethiopian eunuch", "Roman centurion", "Samaritan woman", "Greek governor", "A",
     "The chariot became a classroom."),
    (T_ACT, "Medium", "After his shipwreck on Malta, Paul shook off the viper that fastened on his hand and",
     "suffered no harm", "fell dead at once", "lost the finger", "needed prayer at once", "A",
     "The islanders called him a god."),
]

build_batch(
    S,
    "batch_152_neco_crs4.json",
    "152",
    "NECO CRS round 4 (R28 top-up): image of God, Sabbath rest, "
    "serpent's sentence, Cain's mark, rainbow covenant, Babel; "
    "circumcision sign, Sodom's fifty-to-ten, Jacob's ladder and new "
    "name, Joseph's twenty silver; Nile blood, Jethro's judges, Aaron's "
    "calf excuse, Balaam's donkey, Nebo, Jordan priests, Jericho's "
    "seventh circuit; Samuel's 'Speak', the king demand, the cave "
    "mercy, Jonathan's friendship, Solomon's temple; Cherith ravens, "
    "Zarephath, Amos of Tekoa, Hosea's Gomer, Nineveh's sackcloth, "
    "Daniel's pulse; shepherds' song, Egypt flight, Cana, born again, "
    "'Peace, be still', cleansed temple; Judas' thirty silver, paradise "
    "to the thief; seven deacons, Ethiopian eunuch, Malta's viper. "
    "Scanned against NECO rounds 1-3, WAEC CRS (all rounds) and the "
    "JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
