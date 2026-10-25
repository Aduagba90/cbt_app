"""Batch 143 - WAEC Christian Religious Studies round 5 (WAEC top-up, R27).

Grows WAEC CRS from 168 toward ~205 with fresh narrative angles:
Joseph in Egypt (dreams, cup, Judah's plea); Moses' call and the
exodus (holy ground, Aaron, Passover blood); wilderness provisions
(manna, Meribah, bronze serpent, the spies); judges (Deborah, Gideon's
300, Samson's fall); the kings (Saul's rejection, David and Goliath,
Nathan's ewe lamb, Solomon's baby verdict, the kingdom divided);
prophets (Elijah at Carmel, Elisha and Naaman, Isaiah's coal,
Jeremiah's call, Ezekiel's dry bones); Daniel and his friends;
Jesus' birth, baptism, temptations, miracles and transfiguration;
the parables of the sower, the good Samaritan and the prodigal son;
Peter's denial and Emmaus; the early church (Pentecost,
Ananias and Sapphira, Stephen, Saul's conversion, Peter and
Cornelius). Scanned against WAEC rounds 1-4, NECO CRS (all rounds)
and the JAMB pool.

    python3 scripts/build_neco_batch143.py -> content/batch_143_waec_crs5.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Christian Religious Studies"

T_JOS = "Joseph in Egypt"
T_EX = "Moses and the Exodus"
T_WIL = "Wilderness Journey"
T_JUD = "The Judges"
T_KIN = "United and Divided Kingdom"
T_PRO = "The Prophets"
T_DAN = "Daniel in Exile"
T_JES = "The Ministry of Jesus"
T_PAR = "Parables of Jesus"
T_CH = "The Early Church"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- Joseph
    (T_JOS, "Medium", "Pharaoh's dreams of seven fat and seven lean cows foretold for Egypt",
     "seven years of plenty then seven of famine", "seven wars in seven years", "seven kings to rise and fall", "a seven-day plague of locusts", "A",
     "Joseph read the double dream as one message."),
    (T_JOS, "Hard", "Hidden by Joseph's order in Benjamin's grain sack, to test his brothers, was",
     "his silver cup", "a purse of gold", "a bundle of myrrh", "a royal signet", "A",
     "The youngest brother's sack held the trap."),
    (T_JOS, "Hard", "When the cup was found, the brother who offered to remain a slave in Benjamin's place was",
     "Judah", "Reuben", "Levi", "Dan", "A",
     "He had once sold Joseph; now he offered himself."),

    # ------------------------------------------------------------- Exodus
    (T_EX, "Hard", "At the burning bush, God told Moses to remove his sandals because the ground was",
     "holy", "hot", "wet", "cursed", "A",
     "Even the earth near God was sacred."),
    (T_EX, "Medium", "Moses' plea that he was 'slow of speech' was answered when God appointed as his spokesman",
     "Aaron", "Joshua", "Caleb", "Hur", "A",
     "His brother's mouth served his mission."),
    (T_EX, "Hard", "On the first Passover night, each Israelite household was to smear lamb's blood on",
     "the lintel and doorposts", "the gate posts only", "the firstborn's forehead", "the courtyard wall", "A",
     "The blood marked houses the destroyer would pass."),

    # ------------------------------------------------------------- wilderness
    (T_WIL, "Medium", "The bread-like food Israel gathered each morning in the wilderness was",
     "manna", "quail", "barley", "locust bread", "A",
     "It fell with the dew at dawn."),
    (T_WIL, "Hard", "At Meribah, Israel's thirst was quenched when Moses",
     "struck the rock with his rod", "dug a well at dawn", "prayed for rain", "boiled desert shrubs", "A",
     "Water gushed from the flint."),
    (T_WIL, "Hard", "Bronze was lifted on a pole in the desert, and whoever looked at it after serpent bites",
     "lived", "died at once", "turned pale", "slept", "A",
     "Looking in faith healed the bitten."),
    (T_WIL, "Medium", "Of the twelve spies sent into Canaan, the two who brought a faithful, hopeful report were",
     "Joshua and Caleb", "Reuben and Simeon", "Levi and Naphtali", "Dan and Asher", "A",
     "Ten saw giants; these two saw God."),

    # ------------------------------------------------------------- judges
    (T_JUD, "Medium", "Israel received justice under her palm tree, and she accompanied Barak against Sisera. This judge was",
     "Deborah", "Huldah", "Miriam", "Jael", "A",
     "She sat under the palm tree judging Israel."),
    (T_JUD, "Hard", "Gideon's army of many thousands was reduced by God's tests to",
     "300 men", "600 men", "70 men", "3,000 men", "A",
     "Torches, trumpets and jars won the night.", "300"),
    (T_JUD, "Medium", "Delilah's persistent probing at last revealed that Samson's consecrated strength was bound up with",
     "his unshaven hair", "his iron chains", "his Nazarite robe", "his father's blessing", "A",
     "Delilah sold the secret of his vow."),

    # ------------------------------------------------------------- kingdom
    (T_KIN, "Hard", "Saul lost the kingdom largely because he spared King Agag and the best sheep, proving that to obey is better than",
     "sacrifice", "fasting", "prayer", "counsel", "A",
     "Partial obedience is disobedience."),
    (T_KIN, "Medium", "David felled Goliath in the Valley of Elah with",
     "a sling and a stone", "a spear and a sword", "a bow at a distance", "his bare hands", "A",
     "One smooth stone and a shepherd's aim."),
    (T_KIN, "Hard", "Confronting David after Bathsheba, the prophet Nathan told the story of a poor man's stolen",
     "ewe lamb", "vineyard", "field", "donkey", "A",
     "'You are the man' closed the story."),
    (T_KIN, "Medium", "Solomon's famous judgment between two women concerned",
     "a living baby", "a family field", "a lost donkey", "a bag of gold", "A",
     "The true mother chose her child's life."),
    (T_KIN, "Hard", "Rehoboam's harsh answer to the elders' plea drove the northern tribes to follow",
     "Jeroboam", "Absalom", "Adonijah", "Baasha", "A",
     "He whipped them with words, so they tore away."),
    (T_KIN, "Hard", "To keep Israel from worshipping at Jerusalem, Jeroboam set up golden calves at",
     "Bethel and Dan", "Shechem and Shiloh", "Gilgal and Mizpah", "Samaria and Jezreel", "A",
     "Two calves anchored his rival worship."),

    # ------------------------------------------------------------- prophets
    (T_PRO, "Hard", "On Mount Carmel, Elijah's sacrifice was answered when",
     "fire fell from heaven", "rain quenched the altar", "the earth split open", "an angel appeared", "A",
     "The Baal prophets got silence; Elijah got fire."),
    (T_PRO, "Medium", "Naaman the Syrian leper was healed when he washed in the Jordan",
     "seven times", "three times", "once at sunrise", "with Elisha beside him", "A",
     "Obedience, not pride, cured him."),
    (T_PRO, "Hard", "Isaiah's sense of unworthiness at his call was healed when a seraph touched his lips with",
     "a live coal from the altar", "a scroll of the law", "oil of anointing", "a cup of wine", "A",
     "The burning coal purged his guilt."),
    (T_PRO, "Hard", "Jeremiah answered God's call, despite his youth, with the words",
     "'Behold, I do not know how to speak'", "'Here am I, send me'", "'Who shall go for us?'", "'My kinsmen will stone me'", "A",
     "God promised to put words in his mouth."),
    (T_PRO, "Medium", "Ezekiel's vision of the valley full of dry bones declared that Israel",
     "would rise again as a nation", "was finished forever", "would move to Egypt", "would forget her God", "A",
     "The breath of God re-fleshed the bones."),

    # ------------------------------------------------------------- Daniel
    (T_DAN, "Medium", "The three Hebrew youths earned Nebuchadnezzar's fury by refusing to",
     "bow to his golden image", "eat the king's food", "serve in his army", "pay his new tax", "A",
     "They would not bow to Nebuchadnezzar's statue."),
    (T_DAN, "Hard", "In the blazing furnace, the astonished king counted",
     "four men walking unhurt", "three men kneeling", "two angels at the door", "one man praying", "A",
     "The fourth looked like a son of the gods."),
    (T_DAN, "Medium", "Daniel spent a night among lions unharmed because",
     "God shut their mouths", "the lions were fed", "he hid in a corner", "the den was empty", "A",
     "Darius found him alive at dawn."),
    (T_DAN, "Hard", "The handwriting on Belshazzar's wall, MENE MENE TEKEL UPHARSIN, meant the king had been",
     "weighed and found wanting", "crowned for life", "forgiven his pride", "exiled to Persia", "A",
     "That night his kingdom fell."),

    # ------------------------------------------------------------- Jesus
    (T_JES, "Medium", "The wise men from the East presented the child Jesus with",
     "gold, frankincense and myrrh", "silver, spices and wine", "a lamb, a dove and grain", "robes, rings and sandals", "A",
     "Three gifts fit a king, a priest and a burial."),
    (T_JES, "Medium", "At Jesus' baptism in the Jordan, the Spirit descended like a dove and a voice called him",
     "the beloved Son", "the lion of Judah", "the branch of Jesse", "the second Moses", "A",
     "Heaven bore witness before his work began."),
    (T_JES, "Hard", "The three temptations of Jesus in the wilderness involved stones for bread, the temple pinnacle and",
     "the kingdoms of the world", "a crown of gold", "water from a rock", "a throne in Jerusalem", "A",
     "Each lure met a written word of God."),
    (T_JES, "Medium", "The five thousand were fed with",
     "five loaves and two fish", "seven loaves alone", "two loaves and five fish", "a boy's lunch of dates", "A",
     "Twelve baskets of pieces remained."),
    (T_JES, "Hard", "Though he had lain dead and buried for four days, the man Jesus called out of the tomb was",
     "Lazarus", "Jairus", "Nicodemus", "Malchus", "A",
     "Martha met him with grief and faith."),
    (T_JES, "Medium", "Moses the lawgiver and Elijah the prophet appeared, speaking with Jesus, on",
     "the Mount of Transfiguration", "Mount Sinai", "Mount Carmel", "the Mount of Olives", "A",
     "Law and prophets flanked the radiant Lord."),

    # ------------------------------------------------------------- parables
    (T_PAR, "Medium", "The seed that fell among thorns in Jesus' parable pictured hearers whose hearts are crowded by",
     "life's worries and wealth", "persecution and fear", "shallow soil", "hardened paths", "A",
     "Worries crowded out the word."),
    (T_PAR, "Medium", "The wounded traveller on the Jericho road was helped by",
     "a Samaritan", "a priest", "a Levite", "a soldier", "A",
     "The outsider proved the true neighbour."),
    (T_PAR, "Hard", "In the parable of the prodigal son, the father ran to meet the returning boy and",
     "killed the fatted calf", "rebuked him at the gate", "set him a trial year", "sent him to the servants", "A",
     "Joy outran judgment at the gate."),

    # ------------------------------------------------------------- passion & early church
    (T_JES, "Hard", "Peter's three denials of Jesus were sealed in the courtyard by",
     "the cock's crow", "the guard's whistle", "the temple bell", "Mary's weeping", "A",
     "The sound broke him and he wept."),
    (T_JES, "Medium", "Walking with a stranger they could not name, the Emmaus pair at last knew the risen Lord when he",
     "broke the bread at table", "spoke their names aloud", "showed his scars", "walked on water before them", "A",
     "Their hearts had burned as he taught."),
    (T_CH, "Medium", "At Pentecost, the Spirit came on the disciples as",
     "tongues of fire", "a rushing river", "a bright cloud", "a windless calm", "A",
     "They preached and every man heard his own tongue."),
    (T_CH, "Hard", "Ananias and Sapphira fell dead because they",
     "lied about the price of their land", "stole from the poor fund", "skipped the communion", "sold to Gentiles", "A",
     "They kept back part and claimed the whole."),
    (T_CH, "Medium", "Stephen, the church's first martyr, died seeing",
     "heaven open and the Son of Man", "an army of angels", "the temple veil torn", "Paul weeping", "A",
     "He prayed for his killers as the stones fell."),
    (T_CH, "Medium", "After his blinding vision on the Damascus road, Saul's sight was restored and he was baptised by",
     "Ananias of Damascus", "Barnabas of Cyprus", "Gamaliel his teacher", "Silas the prophet", "A",
     "The obedient disciple healed and baptised him."),
    (T_CH, "Hard", "After his vision of the great sheet let down from heaven, Peter travelled to Caesarea to receive",
     "the Gentile Cornelius", "the Ethiopian eunuch", "the centurion's servant", "the Samaritan woman", "A",
     "What God cleansed, Peter must not call common."),
]

build_batch(
    S,
    "batch_143_waec_crs5.json",
    "143",
    "WAEC CRS round 5 (R27 top-up): Joseph's dreams/cup/Judah's pledge; "
    "holy ground, Aaron the spokesman, Passover blood; manna, Meribah, "
    "bronze serpent, Joshua and Caleb; Deborah, Gideon's 300, Samson's "
    "hair; Saul's spoils, David's sling, Nathan's ewe lamb, Solomon's "
    "baby, Rehoboam and Jeroboam's calves at Bethel and Dan; fire at "
    "Carmel, Naaman's seven washings, Isaiah's coal, Jeremiah's "
    "reluctance, Ezekiel's dry bones; the fiery furnace and fourth man, "
    "lions' den, MENE TEKEL UPHARSIN; wise men's gifts, the beloved "
    "Son, the three temptations, feeding five thousand, Lazarus after "
    "four days, transfiguration with Moses and Elijah; sower's thorns, "
    "the good Samaritan, prodigal's fatted calf; cock's crow, Emmaus "
    "bread, Pentecost fire, Ananias and Sapphira, Stephen's vision, "
    "Damascus road, Peter's sheet and Cornelius. Scanned against WAEC "
    "rounds 1-4, NECO CRS (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
