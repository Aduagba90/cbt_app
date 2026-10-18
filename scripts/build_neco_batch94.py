"""Batch 094 - WAEC Christian Religious Studies round 2 (WAEC lift, R19).

WAEC CRS Paper 1 draws 50 items; the bank stood at 69. This lift uses
episodes not yet in any bank - Babel, binding of Isaac, Rebekah, Jethro's
advice, bronze serpent, Rahab, Ruth and Boaz, Psalm 23, two mothers,
Shadrach, Belshazzar, shepherds and Simeon, temptations, Nicodemus,
Samaritan woman, lost coin, ten virgins, mustard seed, Legion, Jairus,
centurion, 3,000 baptized, Cornelius, Mars Hill, Malta, Psalm 51,
Ecclesiastes - plus sayings of Jesus.

    python3 scripts/build_neco_batch94.py -> content/batch_094_waec_crs2.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Christian Religious Studies"

T_GEN = "Creation and the Early Patriarchs"
T_EXO = "Moses and the Exodus"
T_SET = "Settlement and the Kingdom"
T_PRO = "Exile and the Prophets"
T_GOS = "The Birth and Early Ministry of Jesus"
T_PAR = "Parables and Miracles"
T_ACT = "The Acts of the Apostles"
T_QU = "Quotations and Sayings"

PASSAGES = []
PQ = []

Q = [
    # ---------------------------------------------------------------- genesis
    (T_GEN, "Easy", "God confused human language and scattered builders at",
     "Babel", "Bethel", "Babylon", "Beersheba", "A",
     "The tower project ended in confusion."),
    (T_GEN, "Hard", "On which mountain was Isaac bound for sacrifice before the ram appeared?",
     "Moriah", "Sinai", "Hebron", "Gerizim", "A",
     "A ram replaced the boy there."),
    (T_GEN, "Easy", "Rebekah was chosen as Isaac's wife at the well where she",
     "watered the servant's camels", "was washing clothes", "hid from strangers", "sold her bracelet", "A",
     "Her kindness answered the prayer."),
    (T_GEN, "Medium", "Hagar, the maid who bore Ishmael, was sent away with her son after",
     "Sarah grew jealous", "Abraham lost his flocks", "she stole from the tents", "Isaac dismissed her", "A",
     "Tension in the tent led to it."),
    (T_GEN, "Medium", "In Potiphar's house, Joseph was jailed because of",
     "Potiphar's wife's false charge", "stolen silver cups", "a failed harvest plan", "a dream he retold", "A",
     "She accused him unjustly."),
    (T_GEN, "Medium", "In prison, Joseph interpreted the dreams of Pharaoh's butler and",
     "baker", "guard", "driver", "goldsmith", "A",
     "One dream meant restoration, the other death."),
    # ---------------------------------------------------------------- exodus
    (T_EXO, "Medium", "The Israelites who were bitten by snakes in the wilderness were healed by looking at a",
     "bronze serpent on a pole", "river of Jordan water", "pillar of cloud", "brazen altar", "A",
     "Looking up in faith healed them."),
    (T_EXO, "Hard", "When Moses grew weary of judging alone, Jethro advised him to",
     "appoint able men as judges", "judge only on market days", "leave the camp for Midian", "build more courts at Shiloh", "A",
     "Delegating shared the load."),
    (T_EXO, "Hard", "Of the twelve spies sent into Canaan, only Joshua and",
     "Caleb", "Hur", "Eleazar", "Phinehas", "A",
     "The two brought back courage."),
    (T_EXO, "Hard", "Balaam's donkey spoke when the angel of the Lord blocked the road to stop",
     "Balaam's journey to curse Israel", "Balaam's flight from Midian", "the king's messengers", "Balak's sacrifice", "A",
     "The beast saw what the seer missed."),
    # ---------------------------------------------------------------- settlement and kingdom
    (T_SET, "Medium", "Rahab, who hid the Israelite spies, lived in",
     "Jericho", "Ai", "Gibeon", "Hebron", "A",
     "Her scarlet cord spared her house."),
    (T_SET, "Hard", "Ruth, the loyal Moabite, gleaned in the fields of",
     "Boaz", "Elimelech", "Mahlon", "Kilion", "A",
     "Boaz later became her husband."),
    (T_SET, "Easy", "'The LORD is my shepherd' opens the psalm numbered",
     "23", "1", "51", "100", "A",
     "Psalm 23 is the shepherd psalm."),
    (T_SET, "Hard", "Solomon's wisdom was first shown when he settled the case of",
     "two women claiming one baby", "two farmers quarrelling over land", "two soldiers over booty", "two traders over weights", "A",
     "The sword threatened to divide the child."),
    (T_SET, "Medium", "The queen who came to test Solomon with hard questions was the Queen of",
     "Sheba", "Egypt", "Ethiopia", "Persia", "A",
     "She left overwhelmed by his wisdom."),
    (T_SET, "Hard", "At the temple dedication, Solomon prayed and fire came down from heaven and",
     "consumed the sacrifices", "split the altar stones", "lit the lamps only", "melted the bronze sea", "A",
     "God's glory approved the house."),
    (T_SET, "Hard", "David spared Saul's life inside the cave at",
     "En Gedi", "Endor", "Ephesdammim", "Ziklag", "A",
     "He cut the royal robe, not the king."),
    (T_SET, "Medium", "David's words to Goliath before the fight spoke of his trust in",
     "the name of the LORD", "his own mighty arm", "Saul's armour", "the armies around him", "A",
     "The battle belonged to the Lord."),
    # ---------------------------------------------------------------- prophets and exile
    (T_PRO, "Hard", "Elijah heard God not in the wind or fire but in a",
     "still small voice", "loud thunder", "shout of angels", "song of Levites", "A",
     "The whisper carried the word."),
    (T_PRO, "Hard", "The widow of Zarephath's jar of flour and oil never ran dry because she",
     "fed Elijah first", "sold her last meal", "hid food in the field", "borrowed from Jezebel", "A",
     "Her little became plenty."),
    (T_PRO, "Hard", "In the fiery furnace, Nebuchadnezzar saw a fourth figure walking with",
     "Shadrach, Meshach and Abednego", "Daniel and his friends", "the wise men of Babylon", "the king's guards", "A",
     "The son of God walked the flames."),
    (T_PRO, "Hard", "The writing on the wall at Belshazzar's feast was read and explained by",
     "Daniel", "Nebuchadnezzar", "Nathan", "Ezra", "A",
     "MENE MENE TEKEL counted the kingdom's end."),
    (T_PRO, "Medium", "At the potter's house, God taught Jeremiah that nations, like clay, are",
     "shaped as the potter pleases", "baked beyond changing", "beyond repair always", "worthless without glaze", "A",
     "The potter's hands moulded the lesson."),
    (T_PRO, "Hard", "During Josiah's temple repairs, the book of the Law was found and read, and the king",
     "tore his robes in grief", "burned the scrolls", "banned public reading", "jailed the priests", "A",
     "He mourned the nation's neglect."),
    (T_PRO, "Medium", "Elisha asked for a double portion of the spirit that rested on",
     "Elijah", "Moses", "Elisha himself", "Gehazi", "A",
     "The heir asked his master's share."),
    # ---------------------------------------------------------------- birth and early ministry
    (T_GOS, "Easy", "The angels first announced the birth of Jesus to",
     "shepherds near Bethlehem", "priests in the temple", "traders in Jerusalem", "soldiers of Herod", "A",
     "The fields heard the good news."),
    (T_GOS, "Hard", "The old man in the temple who blessed the baby Jesus and spoke of 'a light for revelation' was",
     "Simeon", "Zechariah", "Nicodemus", "Joseph of Arimathea", "A",
     "He had waited for the consolation."),
    (T_GOS, "Medium", "To escape Herod's massacre, the holy family fled to",
     "Egypt", "Nazareth", "Syria", "the wilderness", "A",
     "They returned after Herod died."),
    (T_GOS, "Easy", "At his temptation, Jesus answered 'Man shall not live by bread alone' when told to",
     "turn stones into bread", "jump from the temple", "worship the tempter", "call down angels", "A",
     "The first temptation met the word."),
    (T_GOS, "Hard", "'Unless one is born anew, he cannot see the kingdom of God' was said to",
     "Nicodemus", "the rich ruler", "Zacchaeus", "Caiaphas", "A",
     "The night visitor heard it."),
    (T_GOS, "Hard", "The woman of Samaria met Jesus at Jacob's well near",
     "Sychar", "Bethany", "Cana", "Capernaum", "A",
     "He asked her for a drink."),
    # ---------------------------------------------------------------- parables and miracles
    (T_PAR, "Medium", "The woman who lit a lamp and swept the house in Jesus' parable was searching for",
     "a lost coin", "a lost sheep", "a lost son", "a lost ring", "A",
     "Her neighbours shared the joy."),
    (T_PAR, "Hard", "In the parable of the ten virgins, the foolish five ran out of",
     "oil for their lamps", "bread for the feast", "money for the door", "water for the jars", "A",
     "Their lamps went dark at midnight."),
    (T_PAR, "Easy", "The smallest of seeds that grows into a great tree, in Jesus' parable, is the",
     "mustard seed", "wheat grain", "cedar seed", "fig seed", "A",
     "Little becomes great in the kingdom."),
    (T_PAR, "Hard", "The demons that Jesus cast out at Gadara entered a herd of",
     "pigs", "cattle", "goats", "sheep", "A",
     "The herd rushed down the steep bank."),
    (T_PAR, "Medium", "While Jesus went to raise Jairus' daughter, the woman with a flow of blood was healed by",
     "touching his garment", "washing in the pool", "anointing his feet", "calling his name", "A",
     "Her faith stopped the flow."),
    (T_PAR, "Hard", "The centurion whose servant was healed had told Jesus he was not worthy to have him",
     "come under his roof", "speak to a Gentile", "touch the sick boy", "enter the barracks", "A",
     "Jesus marvelled at such faith."),
    # ---------------------------------------------------------------- acts
    (T_ACT, "Hard", "After Peter's Pentecost sermon, about how many believers were baptised that day?",
     "3,000", "120", "5,000", "300", "A",
     "Three thousand joined at once."),
    (T_ACT, "Medium", "The lame beggar healed by Peter at the gate called Beautiful walked and",
     "leapt and praised God", "ran to the temple treasury", "followed Peter home", "sat at the gate still", "A",
     "His leaping told the city."),
    (T_ACT, "Hard", "In the vision at Joppa, Peter learned that the gospel was also for the household of",
     "Cornelius", "Philip", "Lydia", "Barnabas", "A",
     "A Roman centurion received the Spirit."),
    (T_ACT, "Hard", "In Athens, Paul preached about the 'unknown God' at",
     "the Areopagus", "the agora market", "the synagogue gate", "Caesar's palace", "A",
     "Mars Hill heard the sermon."),
    (T_ACT, "Medium", "After his shipwreck, Paul was unharmed though a viper fastened on his hand at",
     "Malta", "Crete", "Cyprus", "Samos", "A",
     "The islanders expected him to fall."),
    # ---------------------------------------------------------------- quotations
    (T_QU, "Medium", "'Create in me a clean heart, O God' is the prayer of Psalm",
     "51", "23", "1", "121", "A",
     "David prayed it after his sin."),
    (T_QU, "Medium", "'To everything there is a season' comes from",
     "Ecclesiastes", "Proverbs", "Job", "Psalms", "A",
     "The preacher wrote of times."),
    (T_QU, "Medium", "'Pride goes before destruction' is a saying from",
     "Proverbs", "Ecclesiastes", "Isaiah", "Genesis", "A",
     "The book of wisdom warns the proud."),
    (T_QU, "Easy", "'Seek first the kingdom of God and his righteousness' was taught by",
     "Jesus", "Peter", "Paul", "James", "A",
     "Everything else follows the kingdom."),
    (T_QU, "Medium", "'It is more blessed to give than to receive' were the words of",
     "Jesus", "Paul", "John the Baptist", "Stephen", "A",
     "He quoted them at Miletus too."),
]

build_batch(
    S,
    "batch_094_waec_crs2.json",
    "094",
    "WAEC CRS round 2 (Round 19 lift): episodes new to all banks - Babel, "
    "binding of Isaac at Moriah, Rebekah's camels, Hagar and Ishmael, "
    "Mrs Potiphar's charge, butler and baker, bronze serpent, Jethro's "
    "advice, Joshua and Caleb among the spies, Balaam's donkey, Rahab, Ruth "
    "and Boaz, Psalm 23, Solomon's baby judgment, Queen of Sheba, temple-"
    "dedication fire, En Gedi cave, David's trust words, still small voice, "
    "widow of Zarephath, fiery furnace fourth figure, Belshazzar's writing, "
    "potter's house, Josiah's torn robes, Elisha's double portion, the "
    "shepherds, Simeon, flight to Egypt, stones-to-bread, Nicodemus, "
    "Sychar woman, lost coin, ten virgins' oil, mustard seed, Gadara pigs, "
    "Jairus and the bleeding woman, the centurion's roof, 3,000 baptised, "
    "gate Beautiful, Cornelius, Areopagus, Malta viper, Psalm 51, "
    "Ecclesiastes seasons, Proverbs on pride, seek-first kingdom, blessed "
    "to give. Scanned against WAEC r1, NECO rounds 1-2 and the JAMB banks.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
