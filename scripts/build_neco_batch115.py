"""Batch 115 - NECO Christian Religious Studies round 3 (NECO top-up,
Round 22).

Lifts NECO CRS from 129 toward ~175 with angles not yet in any bank:
creation and the fall, Rebecca at the well, Jacob's ladder, Moses' birth
and the Decalogue, the golden calf, Deborah and Samson, David's
anointing and Jonathan, Naboth's vineyard, Josiah's reform, Daniel,
Jonah and Esther; in the New Testament, the birth narratives, baptism
and temptation, the Beatitudes, the transfiguration, foot washing,
doubting Thomas, Peter's restoration, the gate Beautiful, Cornelius and
Paul's journeys. Scanned against NECO rounds 1-2, WAEC CRS (all rounds)
and the JAMB pool.

    python3 scripts/build_neco_batch115.py -> content/batch_115_neco_crs3.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Christian Religious Studies"

T_GEN = "Creation and Early Stories"
T_PAT = "The Patriarchs Again"
T_EXO = "Moses and the Law"
T_JUD = "Judges and Early Kings"
T_KING = "Later Kings and Exiles"
T_DAN = "Daniel to Esther"
T_LUK = "Birth and Early Ministry of Jesus"
T_CHUR = "Ministry and the Wider Church"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- genesis
    (T_GEN, "Easy", "On which day did God rest from creation?",
     "The seventh day", "The third day", "The first day", "The fifth day", "A",
     "He hallowed it and rested."),
    (T_GEN, "Medium", "The first sin of disobedience was committed in",
     "the garden of Eden", "the land of Ur", "Egypt", "Nineveh", "A",
     "The forbidden fruit was eaten."),
    (T_GEN, "Medium", "Adam and Eve hid from God after eating the fruit because they",
     "were ashamed", "were hungry", "wanted a sacrifice", "had found gold", "A",
     "Nakedness brought them shame."),
    (T_GEN, "Medium", "The first murder in the Bible was committed by",
     "Cain", "Abel", "Seth", "Lamech", "A",
     "His brother's blood cried out."),
    (T_GEN, "Medium", "God destroyed the world in Noah's days by",
     "a great flood", "fire from heaven", "a long drought", "a plague of frogs", "A",
     "The ark carried the remnant."),
    (T_GEN, "Hard", "The tower of Babel was stopped when God",
     "confused their language", "sent an earthquake", "raised a river", "blinded the masons", "A",
     "Work halted amid the babble."),

    # ------------------------------------------------------------- patriarchs
    (T_PAT, "Medium", "At the well of Nahor, Rebekah watered the servant's",
     "camels", "horses", "goats", "sheep alone", "A",
     "Her kindness marked her out."),
    (T_PAT, "Hard", "On the run from Esau, Jacob dreamed at Bethel of a",
     "ladder reaching heaven", "river of oil", "wall of fire", "field of wheat", "A",
     "Angels climbed up and down."),
    (T_PAT, "Medium", "Jacob served Laban seven extra years after being given",
     "Leah instead of Rachel", "Zilpah instead of Bilhah", "a flock of goats", "a piece of land", "A",
     "The morning surprise tested him."),
    (T_PAT, "Medium", "Jacob wrestled at Peniel with a man until daybreak and won a new name,",
     "Israel", "Abraham", "Peniel", "Edom", "A",
     "He had striven with God himself."),
    (T_PAT, "Hard", "In Egypt, Joseph tested his brothers by demanding that",
     "Benjamin be brought to him", "they pay double price", "they build a city", "each marry an Egyptian", "A",
     "The cup in the sack finished the test."),

    # ------------------------------------------------------------- moses and law
    (T_EXO, "Easy", "The baby Moses was hidden in a basket among the",
     "reeds of the Nile", "hills of Midian", "streets of Goshen", "sands of Sinai", "A",
     "Pharaoh's daughter found him."),
    (T_EXO, "Medium", "The mountain where Israel received the law is",
     "Sinai", "Carmel", "Nebo", "Gerizim", "A",
     "Smoke and trumpet sounded there."),
    (T_EXO, "Hard", "The commandment with a promise attached is: honour your",
     "father and mother", "neighbour's ox", "king and soldiers", "prophet and priest", "A",
     "Long life is its promised reward."),
    (T_EXO, "Medium", "Down in the camp during Moses' absence, Israel moulded a",
     "golden calf", "brazen serpent", "wooden ark", "stone altar to Baal", "A",
     "Aaron yielded to their pressure."),
    (T_EXO, "Hard", "The bronze serpent Moses lifted in the wilderness healed those who",
     "looked at it in faith", "touched the ark", "sang at the altar", "carried the tabernacle", "A",
     "Looking up in faith was living."),
    (T_EXO, "Medium", "The spies sent into Canaan brought back a report of a land",
     "flowing with milk and honey", "empty of water", "without walls", "barren of crops", "A",
     "But giants lived there too."),

    # ------------------------------------------------------------- judges and early kings
    (T_JUD, "Medium", "The only female judge of Israel, a prophetess who led with Barak, was",
     "Deborah", "Jael", "Hannah", "Miriam", "A",
     "Her palm tree was her court."),
    (T_JUD, "Hard", "Sisera, the Canaanite commander, was killed by",
     "Jael driving a tent peg", "Barak's sword", "Deborah's curse", "Gideon's trumpets", "A",
     "The hammer and peg ended him."),
    (T_JUD, "Medium", "Delilah's betrayal cost Samson his strength once his hair was",
     "cut at Delilah's plot", "dyed with henna", "braided by Philistines", "wet in the river", "A",
     "Seven locks fell to the razor."),
    (T_JUD, "Medium", "God told Samuel not to judge by height when he chose",
     "David from Jesse's sons", "Saul from Benjamin", "Jonathan for battle", "Abiathar for priest", "A",
     "The heart, not stature, counts."),
    (T_JUD, "Hard", "Jonathan showed covenant friendship to David by giving him his",
     "robe, sword and bow", "chariot and horses", "kingdom and crown", "fields and flocks", "A",
     "He stripped himself for his friend."),

    # ------------------------------------------------------------- later kings and exiles
    (T_KING, "Hard", "Ahab and Jezebel seized Naboth's",
     "vineyard", "olive grove", "herd of cattle", "house in Jezreel", "A",
     "False witnesses took his life."),
    (T_KING, "Medium", "Elijah was taken up to heaven in",
     "a whirlwind", "a burning bush", "a great fish", "a mild earthquake", "A",
     "Chariots of fire led the whirlwind."),
    (T_KING, "Hard", "Josiah led a great national reform after the book of the law was found while",
     "repairing the temple", "digging a well", "building his palace", "counting the treasury", "A",
     "The king tore his own robes."),
    (T_KING, "Medium", "The southern kingdom of Judah fell to",
     "Babylon", "Assyria", "Egypt", "Persia", "A",
     "Nebuchadnezzar's armies came."),
    (T_KING, "Hard", "The decree that allowed exiles to return home came from Cyrus of",
     "Persia", "Babylon", "Greece", "Rome", "A",
     "Cyrus freed the captives."),

    # ------------------------------------------------------------- daniel to esther
    (T_DAN, "Medium", "Daniel spent a night unharmed in the",
     "lions' den", "fiery furnace", "whale's belly", "palace prison", "A",
     "God shut the mouths of the beasts."),
    (T_DAN, "Hard", "Shadrach, Meshach and Abednego refused to",
     "worship the golden image", "eat the king's meat", "pay the temple tax", "serve in the army", "A",
     "The fourth man walked in the fire."),
    (T_DAN, "Medium", "The writing on the wall at Belshazzar's feast was interpreted by",
     "Daniel", "Nebuchadnezzar", "Esther", "Mordecai", "A",
     "MENE MENE TEKEL UPHARSIN."),
    (T_DAN, "Medium", "Jonah was swallowed by a great fish after trying to flee to",
     "Tarshish", "Nineveh", "Joppa", "Damascus", "A",
     "He ran from the assignment."),
    (T_DAN, "Hard", "Esther risked her life for her people by",
     "entering the king unbidden", "poisoning Haman", "fleeing to Persia", "hiding her faith", "A",
     "The golden sceptre spared her life."),

    # ------------------------------------------------------------- birth and early ministry
    (T_LUK, "Easy", "Which town saw the birth of Jesus?",
     "Bethlehem", "Nazareth", "Jerusalem", "Capernaum", "A",
     "A manger received the child."),
    (T_LUK, "Medium", "The angel Gabriel announced John's birth to Zechariah in the",
     "temple at the hour of incense", "marketplace of Jericho", "court of Herod", "synagogue of Nazareth", "A",
     "He was struck dumb for doubting."),
    (T_LUK, "Hard", "Simeon and Anna met the baby Jesus at his",
     "presentation in the temple", "circumcision in Bethlehem", "baptism at Jordan", "first Passover", "A",
     "The old prophet blessed him."),
    (T_LUK, "Medium", "John the Baptist preached a baptism of",
     "repentance for forgiveness", "wealth and success", "war against Rome", "silence and fasting", "A",
     "Prepare the way, he cried."),
    (T_LUK, "Medium", "At his baptism, Jesus heard a voice calling him",
     "the beloved Son", "the lion of Judah", "the son of David", "the second Moses", "A",
     "The Spirit descended like a dove."),
    (T_LUK, "Hard", "With what words did Jesus parry every wilderness temptation?",
     "It is written", "Get behind me", "My hour has come", "I am the light", "A",
     "Written scripture was his sword."),
    (T_LUK, "Hard", "According to the Beatitudes, the peacemakers shall be called",
     "sons of God", "kings of earth", "lights of the world", "judges of men", "A",
     "The Beatitudes crown them."),
    (T_LUK, "Medium", "At the transfiguration, Jesus spoke with Moses and",
     "Elijah", "Abraham", "Isaiah", "Enoch", "A",
     "The cloud overshadowed them."),

    # ------------------------------------------------------------- ministry and wider church
    (T_CHUR, "Hard", "By washing the disciples' feet, Jesus taught them",
     "humble service", "ritual cleanliness", "priestly hierarchy", "Jewish customs", "A",
     "The Master took the slave's place."),
    (T_CHUR, "Hard", "Thomas, called Didymus, believed only after he",
     "touched the risen Lord's wounds", "saw the empty tomb", "heard the women's report", "received the Spirit", "A",
     "My Lord and my God, he cried."),
    (T_CHUR, "Medium", "After his resurrection, Jesus asked Peter three times,",
     "Do you love me?", "Who do you say I am?", "Will you also leave?", "Can you drink my cup?", "A",
     "Feed my sheep followed each."),
    (T_CHUR, "Medium", "The lame beggar healed at the Beautiful Gate was going there to",
     "ask for alms", "hear Peter preach", "be baptised", "sacrifice a lamb", "A",
     "Silver and gold he wanted; walking he got."),
    (T_CHUR, "Hard", "Peter's vision at Joppa prepared him to visit",
     "Cornelius the centurion", "Saul of Tarsus", "the Ethiopian eunuch", "Simon Magus", "A",
     "No one is common or unclean."),
    (T_CHUR, "Medium", "Paul and Barnabas were set apart for mission at",
     "Antioch", "Jerusalem", "Lystra", "Ephesus", "A",
     "The church fasted and laid hands."),
    (T_CHUR, "Hard", "Shipwrecked on the way to Rome, Paul was bitten harmlessly by",
     "a viper in the firewood", "a scorpion on deck", "a mad dog at Puteoli", "a serpent in the cargo", "A",
     "He shook it off and felt nothing."),
    (T_CHUR, "Medium", "Paul's letter teaching that salvation is by grace through faith was written to the",
     "Romans", "Colossians", "Thessalonians", "Philemon", "A",
     "The just shall live by faith."),
]

build_batch(
    S,
    "batch_115_neco_crs3.json",
    "115",
    "NECO Christian Religious Studies round 3 (Round 22 top-up): the "
    "seventh day, Eden's fall, Cain, the flood and Babel, Rebekah's "
    "camels, Bethel's ladder, Leah and Rachel, Peniel, Joseph's test of "
    "Benjamin, the basket in the Nile, Sinai, the fifth commandment's "
    "promise, the golden calf, the bronze serpent, the spies' report, "
    "Deborah and Jael, Samson's hair, David's anointing, Jonathan's "
    "covenant, Naboth's vineyard, the whirlwind, Josiah's reform, Judah's "
    "exile and Cyrus' decree, the lions' den, the fiery furnace, the "
    "writing on the wall, Jonah's Tarshish, Esther's risk, Bethlehem, "
    "Gabriel and Zechariah, Simeon and Anna, John's baptism message, the "
    "beloved Son, 'It is written', the peacemakers' blessing, "
    "transfiguration, foot washing, Thomas, Peter's restoration, the "
    "Beautiful Gate, Cornelius, Antioch's commission, the Malta viper "
    "and Romans' grace. Scanned against NECO rounds 1-2, WAEC CRS (all "
    "rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
