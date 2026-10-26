"""Batch 211 - NECO Christian Religious Studies round 6 (NECO top-up, R42).

Grows NECO CRS from 243 toward ~268 with angles not yet in the
bank: the serpent's punishment; Cain's mark; Noah's wine; the
covenant between the pieces; the butler and the baker; Gideon's
three hundred; Delilah; Hophni and Phinehas; Solomon's dream at
Gibeon; Daniel's great statue; the magi's gifts; the flight to
Egypt; Jesus walking on the water; the Gadarene swine; the lost
sheep; feed my sheep; the Beautiful Gate; the widow's oil; the
Canaanite woman; the choosing of the Seven; Herod Agrippa's
death; faith without works; living stones. Scanned against the
whole CRS pool (WAEC, NECO and JAMB stems, 1,567 items).

    python3 scripts/build_neco_batch211.py -> content/batch_211_neco_crs6.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Christian Religious Studies"

T_GEN = "Themes from the Creation to the Patriarchs"
T_EXO = "Moses and the Exodus"
T_SET = "Settlement and the Judges"
T_KIN = "Kings and the Monarchy"
T_MIN = "The Ministry of Jesus"
T_ACT = "The Apostles and the Early Church"
T_EPI = "Letters and Teachings"

PASSAGES = []
PQ = []

Q = [
    (T_GEN, "Medium", "For leading Eve into disobedience, the serpent was punished by being condemned to",
     "crawl on its belly and eat dust", "serve the woman forever",
     "live in the river Nile", "guard the tree of life", "A",
     "Dust became its food all its days."),
    (T_GEN, "Medium", "To keep anyone from killing the wandering Cain, God placed on him",
     "a mark of protection", "a crown of thorns",
     "a yoke of iron", "a garment of skin", "A",
     "The fugitive carried God's own seal."),
    (T_GEN, "Medium", "After the flood, Noah's drunkenness in his tent brought a curse upon",
     "his son Ham", "his son Shem",
     "the whole earth again", "the vineyard's keeper", "A",
     "What Ham saw and told brought trouble."),
    (T_GEN, "Hard", "When Abraham asked how he would know that the land would be his, God sealed the promise with",
     "a covenant between the pieces", "a tablet of stone",
     "a feast of unleavened bread", "a dream of a ladder", "A",
     "The smoking fire pot passed between the halves."),
    (T_GEN, "Medium", "In prison, Joseph interpreted the dreams of two fellow prisoners, who were Pharaoh's",
     "butler and baker", "captain and guard",
     "magician and astrologer", "cupbearer and soldier", "A",
     "One dreamed of a vine, the other of birds."),
    (T_SET, "Hard", "From the great host that answered his trumpet, Gideon led into the night battle only",
     "three hundred men", "three thousand men",
     "thirty thousand men", "the whole army of Israel", "A",
     "Lapping water marked them out."),
    (T_SET, "Medium", "The woman who was bribed to discover the secret of Samson's strength was",
     "Delilah", "Deborah",
     "Dinah", "Damaris", "A",
     "She sold his sleep for silver."),
    (T_KIN, "Medium", "The corrupt sons of Eli who despised the offerings at Shiloh were",
     "Hophni and Phinehas", "Joel and Abijah",
     "Nadab and Abihu", "Elimelech and Mahlon", "A",
     "Worthless men profaned the holy place."),
    (T_KIN, "Medium", "Soon after becoming king, Solomon asked and received the wisdom he prayed for at",
     "the high place of Gibeon", "the ark in Jerusalem",
     "Mount Sinai", "the Jordan ford", "A",
     "There God appeared to him in a dream."),
    (T_KIN, "Hard", "The frightening dream that Nebuchadnezzar could not remember, but Daniel both recalled and interpreted, was of",
     "a great statue destroyed by a stone", "a tree cut down to its stump",
     "four beasts rising from the sea", "a hand writing on a wall", "A",
     "The stone not cut by hands filled the earth."),
    (T_MIN, "Medium", "When the wise men set out from Jerusalem, the star they had seen went before them until it stopped over",
     "the place where the child was", "the inn of the village",
     "the temple in Jerusalem", "the hill of Bethlehem", "A",
     "The star itself became their last guide."),
    (T_MIN, "Easy", "Warned in a dream about Herod's plot, Joseph took Mary and the child and fled to",
     "Egypt", "Nazareth at once",
     "Syria", "the wilderness", "A",
     "Out of Egypt God called his Son."),
    (T_MIN, "Medium", "During the storm on the lake, the disciples saw Jesus walking on the water and cried out in fear, thinking he was",
     "a ghost", "a fisherman",
     "Peter's shadow", "an angel of death", "A",
     "He calmed both the sea and their hearts."),
    (T_MIN, "Hard", "After the unclean spirits at Gadara begged to enter them, the herd of swine",
     "rushed down the bank into the sea", "scattered quietly into the hills",
     "turned and attacked the keepers", "fell asleep by the roadside", "A",
     "About two thousand drowned in the water."),
    (T_MIN, "Easy", "In the parable of the lost sheep, the shepherd who finds the one stray sheep",
     "rejoices over it", "beats it for wandering off",
     "sells it at the market", "leaves it to find its way", "A",
     "One rescued soul sets heaven singing."),
    (T_KIN, "Hard", "When a borrowed axe head sank into the Jordan, the man of God made it float by casting",
     "a stick into the water", "a stone beside it",
     "his mantle over it", "salt upon the bank", "A",
     "The iron swam at the prophet's word."),
    (T_ACT, "Medium", "The lame beggar who leapt and praised God after Peter and John healed him sat daily at the gate called",
     "Beautiful", "Golden",
     "Eastern", "Sheep", "A",
     "Silver and gold they had none to give."),
    (T_ACT, "Hard", "When Elisha came to the widow whose sons were to be taken for debt, the only thing of value in her house was",
     "a jar of oil", "a piece of land",
     "a flock of geese", "a ring of gold", "A",
     "The oil flowed until every vessel filled."),
    (T_MIN, "Hard", "The Canaanite woman whose daughter was tormented won Jesus' praise for her faith when she said that even the dogs eat",
     "the crumbs under the table", "the bread of the children",
     "the harvest of the field", "the firstfruits", "A",
     "Great faith can wait on crumbs."),
    (T_ACT, "Medium", "To free the apostles for prayer and preaching, the church chose seven men full of the Spirit to serve at tables, among them",
     "Stephen and Philip", "Barnabas and Silas",
     "Peter and John", "Paul and Timothy", "A",
     "The first deacons served food and fire."),
    (T_ACT, "Hard", "Herod Agrippa, who killed James and imprisoned Peter, died a dreadful death because he",
     "did not give God the glory", "worshipped idols in the temple",
     "refused to free Peter", "taxed the poor", "A",
     "Worms ended the boastful king."),
    (T_EPI, "Medium", "James teaches that faith without works is",
     "dead", "complete",
     "living and active", "sufficient", "A",
     "Faith shows itself in what it does."),
    (T_EPI, "Hard", "Peter urges believers to come to Christ and be built up, like living stones, into",
     "a spiritual house", "a city on a hill",
     "an ark of safety", "a tower of strength", "A",
     "Christ himself is the chosen cornerstone."),
    (T_EXO, "Medium", "When Israel lacked water at Marah and murmured, Moses cried to God, who showed him",
     "a tree to cast into the waters", "a rock to strike with his rod",
     "a well hidden in the sand", "a cloud full of rain", "A",
     "The bitter waters were made sweet."),
    (T_KIN, "Medium", "Nathan's parable of the poor man's only lamb was told to convict",
     "David of his sin", "Saul of his disobedience",
     "Ahab of his greed", "Solomon of his pride", "A",
     "The king's own mouth passed his sentence."),
]

build_batch(
    S,
    "batch_211_neco_crs6.json",
    "211",
    "NECO CRS round 6 (R42 top-up): the serpent's punishment; "
    "Cain's protective mark; Noah's wine and Ham; the covenant "
    "between the pieces; the butler and the baker; Gideon's three "
    "hundred; Delilah; Hophni and Phinehas; Solomon's dream at "
    "Gibeon; Nebuchadnezzar's forgotten dream of the statue; the "
    "magi's myrrh; the flight to Egypt; Jesus walking on the "
    "water; the Gadarene swine; the lost sheep's joy; feed my "
    "sheep; the gate called Beautiful; the widow's jar of oil; the "
    "Canaanite woman's crumbs; the choosing of the Seven; Herod "
    "Agrippa's death; faith without works; living stones; the "
    "tree at Marah; Nathan's parable of the lamb. Scanned against "
    "the whole CRS pool (WAEC, NECO and JAMB stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
