"""Batch 187 - NECO CRS round 5 (NECO top-up, R36).

Grows NECO CRS from 217 toward ~243 with angles not yet in the
bank: Eve from Adam's rib; Abel's accepted offering; Methuselah's
969 years; Lot rescued from Sodom; Jacob's twelve sons; Joseph's
ornate robe; Joshua succeeding Moses; Gideon's fleece; Saul
searching for donkeys; Absalom's hair; Solomon's foreign wives;
Gehazi's greed; Jonah's worm; Haggai and Zechariah rebuilding;
Matthew leaving the tax booth; the fishermen first called; the
meek inheriting the earth; the Last Supper as Passover; Pilate
washing his hands; Father, forgive them; Joseph of Arimathea's
tomb; the ascension from the Mount of Olives; Philip preaching in
Samaria; Philippians the prison letter; Psalm 119's lamp; Train up
a child in Proverbs. Scanned against NECO rounds 1-4, WAEC CRS
(all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch187.py -> content/batch_187_neco_crs5.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Christian Religious Studies"

T_GEN = "Themes from the Creation to the Patriarchs"
T_EXO = "Moses and the Exodus"
T_SET = "Settlement and the Judges"
T_KIN = "Kings and the Divided Monarchy"
T_PRO = "The Prophets"
T_EXI = "Exile and Restoration"
T_MIN = "The Ministry of Jesus"
T_PAS = "The Passion and Resurrection"
T_ACT = "The Apostles and the Early Church"
T_EPI = "Letters and Teachings"

PASSAGES = []
PQ = []

Q = [
    (T_GEN, "Easy", "God formed the first woman, Eve, out of Adam's",
     "rib", "clay",
     "bone of a beast", "shadow", "A",
     "Bone of his bone, flesh of his flesh."),
    (T_GEN, "Medium", "God accepted Abel's offering while rejecting Cain's because Abel brought",
     "the best of his flock in faith", "a larger quantity of grain",
     "an animal of the field unasked", "fire from the altar", "A",
     "The firstling and the fat portions pleased the Lord."),
    (T_GEN, "Hard", "The man who lived longer than every other person in the Bible, reaching 969 years, was",
     "Methuselah", "Adam",
     "Noah", "Enoch", "A",
     "The oldest patriarch of them all."),
    (T_GEN, "Medium", "The nephew Abraham rescued from the destruction of Sodom was",
     "Lot", "Isaac",
     "Eliezer", "Ishmael", "A",
     "Angels dragged him out of the doomed city."),
    (T_GEN, "Easy", "The sons of Jacob who became the ancestors of Israel's tribes numbered",
     "12", "10",
     "7", "14", "A",
     "Twelve tribes grew from twelve sons.", "12"),
    (T_GEN, "Medium", "The ornate robe Jacob gave his favourite son signalled his",
     "special love for the boy", "intention to sell him",
     "appointment as a priest", "wealth in cattle", "A",
     "The many-coloured coat fed the brothers' envy."),
    (T_EXO, "Medium", "After Moses died on Mount Nebo, leadership of Israel into the promised land passed to",
     "Joshua", "Caleb",
     "Aaron", "Eleazar", "A",
     "Moses' servant carried the mission across Jordan."),
    (T_SET, "Hard", "To be sure of God's call, Gideon twice asked for a sign involving a piece of",
     "fleece of wool", "loaf of bread",
     "iron floating on water", "sand counted by angels", "A",
     "The fleece alone drank the night's dew."),
    (T_SET, "Medium", "Young Saul first met the prophet Samuel while searching for his father's lost",
     "donkeys", "camels",
     "sheep", "silver", "A",
     "The missing beasts led him to a kingdom."),
    (T_SET, "Hard", "Absalom met his death in the battle of the forest of Ephraim when his long",
     "hair caught in the branches of an oak", "spear broke in half",
     "horse threw him into a river", "armour slipped off", "A",
     "The glory of his head hanged him."),
    (T_KIN, "Medium", "In his old age, Solomon was led into idol worship chiefly by his many",
     "foreign wives", "officials of the palace",
     "horses from Egypt", "trading partners", "A",
     "His heart turned after the gods of his strange women."),
    (T_PRO, "Hard", "The greedy servant of Elisha who was struck with Naaman's leprosy was",
     "Gehazi", "Obadiah",
     "Micaiah", "Baruch", "A",
     "He ran after the gifts his master had refused."),
    (T_PRO, "Medium", "God taught Jonah pity by raising a shady plant overnight and then sending a",
     "worm to eat it", "wind to dry it",
     "goat to browse it", "flood to drown it", "A",
     "Jonah grieved for a gourd he never planted."),
    (T_EXI, "Hard", "The two prophets who stirred the returned exiles to finish rebuilding the temple in Jerusalem were",
     "Haggai and Zechariah", "Amos and Hosea",
     "Ezekiel and Daniel", "Joel and Obadiah", "A",
     "Their preaching put the builders back on the walls."),
    (T_MIN, "Medium", "The tax collector who left his customs booth at Capernaum to follow Jesus was",
     "Matthew", "Thomas",
     "Simon the Zealot", "Philip", "A",
     "He rose from the receipt table and followed."),
    (T_MIN, "Easy", "The first disciples Jesus called beside the Sea of Galilee were the fishermen",
     "Simon Peter and Andrew", "James and John",
     "Philip and Bartholomew", "Thomas and Matthew", "A",
     "He found them casting nets by the shore."),
    (T_MIN, "Medium", "In the Sermon on the Mount, Jesus promised that the meek shall inherit the",
     "earth", "temple",
     "kingdom of Israel", "city of David", "A",
     "The gentle receive the whole world."),
    (T_PAS, "Medium", "The Last Supper that Jesus shared with his disciples was the Jewish feast of",
     "Passover", "Pentecost",
     "Tabernacles", "Purim", "A",
     "The lamb was eaten on the night of deliverance."),
    (T_PAS, "Hard", "Before the shouting crowd, Pilate washed his hands in water to declare himself",
     "innocent of the blood of Jesus", "ready to free Barabbas",
     "the new king of the Jews", "unwilling to judge at all", "A",
     "The water could not wash away the verdict."),
    (T_PAS, "Hard", "From the cross, Jesus prayed for his executioners with the words, Father,",
     "forgive them, for they know not what they do", "my God, why have you forsaken me",
     "why have you forsaken me here", "let this cup pass from me", "A",
     "Even nails could not close the prayer of mercy."),
    (T_PAS, "Medium", "The council member from Arimathea who laid the body of Jesus in his own new tomb was",
     "Joseph", "Nicodemus",
     "Zacchaeus", "Lazarus", "A",
     "The rich man gave his own resting place away."),
    (T_PAS, "Medium", "Jesus ascended into heaven from the mount named",
     "of Olives", "of Transfiguration",
     "Sinai", "of Temptation", "A",
     "From Bethany's hillside he was taken up."),
    (T_ACT, "Medium", "After Stephen's death, the deacon who first carried the gospel into Samaria was",
     "Philip", "Barnabas",
     "Silas", "Timothy", "A",
     "The city received his preaching with joy."),
    (T_EPI, "Medium", "Paul's letter overflowing with rejoicing, written while he was a prisoner, was addressed to the church at",
     "Philippi", "Corinth",
     "Rome", "Colossae", "A",
     "Chains could not silence the joy."),
    (T_EPI, "Medium", "Thy word is a lamp unto my feet, and a light unto my path is a verse of the psalm numbered",
     "119", "23",
     "51", "100", "A",
     "The longest psalm honours the law.", "119"),
    (T_EPI, "Medium", "Train up a child in the way he should go is a well-known saying from the book of",
     "Proverbs", "Psalms",
     "Ecclesiastes", "Job", "A",
     "The wisdom book guides the raising of children."),
]

build_batch(
    S,
    "batch_187_neco_crs5.json",
    "187",
    "NECO CRS round 5 (R36 top-up): Eve from Adam's rib; Abel's "
    "accepted offering; Methuselah's 969 years; Lot rescued; "
    "Jacob's twelve sons; Joseph's ornate robe; Joshua succeeding "
    "Moses; Gideon's fleece; Saul's donkeys; Absalom's hair; "
    "Solomon's foreign wives; Gehazi's greed; Jonah's worm; Haggai "
    "and Zechariah; Matthew at the customs booth; Peter and Andrew "
    "first called; the meek inheriting the earth; the Last Supper "
    "as Passover; Pilate's washed hands; Father, forgive them; "
    "Joseph of Arimathea; ascension from Olivet; Philip in Samaria; "
    "Philippians the prison letter; Psalm 119's lamp; Train up a "
    "child. Scanned against NECO rounds 1-4, WAEC CRS (all rounds) "
    "and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
