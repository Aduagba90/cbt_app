"""Batch 109 - WAEC Christian Religious Studies round 3 (WAEC top-up,
Round 21).

Lifts WAEC CRS from 116 toward ~160 with fresh angles: the patriarchs,
Joseph in Egypt, Moses and the exodus, the judges and kings, Elijah and
Elisha, prophets of justice, the parables, the miracles, the passion
week, the resurrection and the early church. Scanned against WAEC
rounds 1-2, NECO CRS and the JAMB pool.

    python3 scripts/build_neco_batch109.py -> content/batch_109_waec_crs3.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Christian Religious Studies"

T_PAT = "The Patriarchs"
T_EXO = "Moses and the Exodus"
T_KING = "Judges and Kings"
T_PROPH = "The Prophets"
T_PAR = "The Parables of Jesus"
T_MIR = "The Miracles of Jesus"
T_PASS = "The Passion and Resurrection"
T_CHURCH = "The Early Church"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- patriarchs
    (T_PAT, "Easy", "God asked Abraham to offer his son Isaac on Mount",
     "Moriah", "Sinai", "Carmel", "Nebo", "A",
     "The place was named for seeing."),
    (T_PAT, "Medium", "The boy whose name recalls a laugh, born to aged Sarah, was",
     "Isaac", "Ishmael", "Jacob", "Esau", "A",
     "His very name means laughter."),
    (T_PAT, "Medium", "Jacob received his father's blessing while disguised as",
     "Esau", "Laban", "Reuben", "Levi", "A",
     "Goat skins and a savoury dish."),
    (T_PAT, "Hard", "Jacob's favourite son, sold by his brothers for twenty pieces of silver, was",
     "Joseph", "Benjamin", "Dan", "Naphtali", "A",
     "His coat of many colours was seized."),
    (T_PAT, "Hard", "Pharaoh raised Joseph to high office after Joseph read the meaning of his",
     "dreams", "handwriting", "star chart", "tax records", "A",
     "Seven fat and seven lean years."),
    (T_PAT, "Medium", "During the famine, Jacob's family found food in Egypt by sending to",
     "Joseph", "Pharaoh", "Hagar", "Abimelech", "A",
     "The brother they sold saved them."),

    # ------------------------------------------------------------- exodus
    (T_EXO, "Medium", "Moses fled to Midian after killing an Egyptian whom he found",
     "beating a Hebrew", "stealing a goat", "insulting Pharaoh", "worshipping an idol", "A",
     "He looked this way and that first."),
    (T_EXO, "Medium", "God called Moses at the burning bush which",
     "burned without being consumed", "turned into a river", "spoke in thunder", "floated skyward", "A",
     "The fire did not eat the bush."),
    (T_EXO, "Hard", "Which last plague made Pharaoh let Israel go?",
     "the firstborn", "the livestock", "the Nile fish", "the crops", "A",
     "Blood on the doorposts spared Israel."),
    (T_EXO, "Medium", "Israel crossed the Red Sea when God",
     "parted the waters with a wind", "froze it into solid ice", "dried it with great heat", "built a bridge of rock", "A",
     "The wall of water stood on both sides."),
    (T_EXO, "Hard", "Besides manna, the wandering Israelites were also given",
     "quails", "locusts", "figs", "barley loaves", "A",
     "Birds covered the camp at evening."),
    (T_EXO, "Medium", "Water flowed from the rock at Horeb when Moses",
     "struck it with his rod", "sang to it", "prayed silently", "dug around it", "A",
     "He was told to speak to it later."),
    (T_EXO, "Hard", "The tenth plague led Israel to institute the feast of",
     "Passover", "Pentecost", "Tabernacles", "Firstfruits", "A",
     "The destroying angel passed over."),

    # ------------------------------------------------------------- judges and kings
    (T_KING, "Medium", "Israel demanded a king to be like other nations, and Samuel anointed",
     "Saul", "David", "Solomon", "Gideon", "A",
     "He stood head and shoulders above all."),
    (T_KING, "Medium", "David's victory over Goliath was won with",
     "a sling and a stone", "a sword and shield", "an army of archers", "a chariot of iron", "A",
     "One smooth stone found the brow."),
    (T_KING, "Hard", "David's great sin concerning Bathsheba led the prophet Nathan to tell him the parable of",
     "the ewe lamb", "the lost coin", "the sower", "the talents", "A",
     "'You are the man', said Nathan."),
    (T_KING, "Medium", "At Gibeon, young Solomon's request to God was for",
     "a wise and understanding heart", "long life alone", "riches and war", "the death of his foes", "A",
     "Other gifts followed the wisdom."),
    (T_KING, "Hard", "Solomon's temple was built on Mount",
     "Moriah", "Gerizim", "Tabor", "Hermon", "A",
     "The threshing floor of Ornan."),
    (T_KING, "Hard", "After Solomon's death the kingdom split, with Jeroboam ruling the",
     "ten northern tribes", "two southern tribes", "priestly clan only", "whole of Israel", "A",
     "Rehoboam kept Judah and Benjamin."),
    (T_KING, "Medium", "The judge who defeated the Midianites with three hundred men was",
     "Gideon", "Deborah", "Samson", "Jephthah", "A",
     "Torches, trumpets and broken jars."),

    # ------------------------------------------------------------- prophets
    (T_PROPH, "Hard", "How did Elijah answer the prophets of Baal on Carmel?",
     "fire on a soaked sacrifice", "rain of falling stones", "a great earthquake", "a mighty whirlwind", "A",
     "The people fell on their faces."),
    (T_PROPH, "Medium", "Elisha healed the Syrian commander Naaman of",
     "leprosy", "blindness", "paralysis", "madness", "A",
     "Seven dips in the Jordan."),
    (T_PROPH, "Hard", "Amos thundered most against",
     "injustice to the poor", "long and vain prayers", "marching foreign armies", "the noise of temple music", "A",
     "Let justice roll down like waters."),
    (T_PROPH, "Medium", "Isaiah's call vision happened in the year King",
     "Uzziah died", "Hezekiah fell ill", "Josiah reformed", "Ahab married Jezebel", "A",
     "Who will go for us? Here am I."),
    (T_PROPH, "Hard", "Hosea's marriage to Gomer symbolised",
     "Israel's unfaithfulness to God", "Judah's wealth", "the temple's glory", "the exile's end", "A",
     "A faithless wife, a covenant God."),
    (T_PROPH, "Medium", "Why do readers call Jeremiah the weeping prophet?",
     "mourned Judah's coming ruin", "lost his eyesight", "wept at his wedding", "cried for a child", "A",
     "His book holds many laments."),

    # ------------------------------------------------------------- parables
    (T_PAR, "Medium", "Thorny-ground hearers, in the sower's story, are choked by",
     "worries and wealth", "birds", "sunlight", "footpaths", "A",
     "Cares of this world choked it."),
    (T_PAR, "Hard", "The neighbour who helped the robbed traveller on the Jericho road was a",
     "Samaritan", "Levite", "priest", "Roman soldier", "A",
     "Mercy crossed the old hatred."),
    (T_PAR, "Medium", "The father who welcomed his returning son killed the fatted calf; the elder brother",
     "refused to join the feast", "danced with joy", "left home too", "asked for his share", "A",
     "He stood outside grumbling."),
    (T_PAR, "Hard", "The one-talent man who dug a hole for it earned his master's word",
     "wicked and slothful", "faithful and wise", "poor but honest", "brave but rash", "A",
     "His one talent was taken away."),
    (T_PAR, "Medium", "The rich man and Lazarus teaches that",
     "comfort now may cost later", "wealth is always sinful", "the poor never rise", "heaven has no rest", "A",
     "A great gulf fixed between."),
    (T_PAR, "Hard", "The ten virgins were divided by whether they had",
     "enough oil for their lamps", "white garments", "money for the feast", "musical instruments", "A",
     "The bridegroom came at midnight."),

    # ------------------------------------------------------------- miracles
    (T_MIR, "Medium", "Jesus' first recorded miracle, at Cana, was",
     "turning water into wine", "healing a leper", "walking on water", "raising Lazarus", "A",
     "The master of the feast tasted it."),
    (T_MIR, "Medium", "Five loaves and two fish fed five thousand and the leftovers filled",
     "twelve baskets", "seven baskets", "two baskets", "no basket at all", "A",
     "They gathered up the fragments."),
    (T_MIR, "Medium", "Jesus walked on the water of the Sea of",
     "Galilee", "Salt", "Red", "Dead", "A",
     "Peter stepped out to meet him."),
    (T_MIR, "Hard", "Jesus called Lazarus out of the tomb after he had lain dead for",
     "four days", "one day", "three hours", "seven days", "A",
     "Martha warned of the smell."),
    (T_MIR, "Medium", "Bartimaeus, whom Jesus healed near Jericho, was",
     "blind", "deaf", "lame", "leprous", "A",
     "He threw off his cloak and came."),
    (T_MIR, "Hard", "The paralytic lowered through the roof was first told,",
     "Your sins are forgiven", "Rise and be baptised", "Go show yourself to the priest", "Take up your mat quietly", "A",
     "The scribes murmured at this."),

    # ------------------------------------------------------------- passion and resurrection
    (T_PASS, "Medium", "Jesus rode into Jerusalem to shouts of Hosanna on",
     "a donkey's colt", "a war horse", "a royal chariot", "foot with the twelve", "A",
     "Palm branches lined the way."),
    (T_PASS, "Medium", "The betrayer who kissed Jesus in Gethsemane was",
     "Judas Iscariot", "Peter", "Thomas", "Nicodemus", "A",
     "Thirty pieces of silver paid."),
    (T_PASS, "Hard", "Which follower three times said he never knew Jesus before the cock crowed?",
     "Peter", "John", "Andrew", "Philip", "A",
     "He went out and wept bitterly."),
    (T_PASS, "Hard", "Who was the Roman ruler who passed the death sentence on Jesus?",
     "Pontius Pilate", "Herod Antipas", "Caiaphas", "Felix", "A",
     "He washed his hands of it."),
    (T_PASS, "Medium", "The Roman centurion at the cross declared,",
     "Truly this was the Son of God", "Crucify him again", "Release Barabbas instead", "Let his blood be on us", "A",
     "Even a soldier saw the truth."),
    (T_PASS, "Medium", "The women found the tomb empty on",
     "the first day of the week", "the third year", "the Day of Atonement", "the Passover eve", "A",
     "Early, while it was still dark."),
    (T_PASS, "Hard", "What opened the two Emmaus travellers' eyes at the table?",
     "in the breaking of bread", "by his voice alone", "through a vision of angels", "only after he vanished", "A",
     "Their hearts burned as he taught."),
    (T_PASS, "Medium", "Before his ascension, Jesus promised his disciples power when the",
     "Holy Spirit came upon them", "Roman armies fled", "temple was rebuilt", "teachers arrived", "A",
     "They would be his witnesses."),

    # ------------------------------------------------------------- early church
    (T_CHURCH, "Medium", "The Holy Spirit fell on the disciples at Pentecost with",
     "tongues of fire and wind", "a bright noonday star", "rain and loud thunder", "a still small voice", "A",
     "Fire sat on each while wind rushed."),
    (T_CHURCH, "Hard", "Which offence cost Ananias and Sapphira their lives?",
     "lied about their offering", "missed the prayer meeting", "sold the wrong field", "refused to fast", "A",
     "They kept back part of the price."),
    (T_CHURCH, "Hard", "Stoned after a speech the council could not answer, the first martyr was",
     "Stephen", "James", "Philip", "Barnabas", "A",
     "He saw heaven opened above."),
    (T_CHURCH, "Medium", "A blinding light stopped Saul of Tarsus as he neared",
     "Damascus", "Antioch", "Jericho", "Joppa", "A",
     "A light from heaven struck him down."),
    (T_CHURCH, "Hard", "The disagreement over Gentile circumcision was settled at the council of",
     "Jerusalem", "Antioch", "Ephesus", "Corinth", "A",
     "Peter and James both spoke."),
    (T_CHURCH, "Medium", "In Joppa, Peter raised the disciple Tabitha, whose name in Greek was",
     "Dorcas", "Lydia", "Priscilla", "Phoebe", "A",
     "She was full of good works."),
]

build_batch(
    S,
    "batch_109_waec_crs3.json",
    "109",
    "WAEC Christian Religious Studies round 3 (Round 21 top-up): Mount "
    "Moriah and Isaac, Sarah's laughter, Jacob's disguise, Joseph sold "
    "and raised, Moses' flight and call, the tenth plague and Passover, "
    "Red Sea crossing, manna and quails, water from Horeb, Saul, David "
    "and Goliath, Nathan's ewe-lamb parable, Solomon's request and "
    "temple site, the kingdom split, Gideon's three hundred, Carmel "
    "fire, Naaman's cleansing, Amos on justice, Isaiah's call, Hosea's "
    "Gomer, the weeping Jeremiah, sower's thorns, the good Samaritan, "
    "prodigal's elder brother, talents, rich man and Lazarus, ten "
    "virgins, Cana, five thousand fed, walking on Galilee, four-day "
    "Lazarus, Bartimaeus, the paralytic's forgiveness, triumphal entry, "
    "Judas' kiss, Peter's denial, Pilate, the centurion's word, empty "
    "tomb, Emmaus bread, ascension promise, Pentecost, Ananias and "
    "Sapphira, Stephen, Damascus road, the Jerusalem council and "
    "Dorcas. Scanned against WAEC rounds 1-2, NECO CRS and the JAMB "
    "pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
