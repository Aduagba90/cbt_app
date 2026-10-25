"""Batch 174 - WAEC CRS round 6 (WAEC top-up, R33).

Grows WAEC CRS from 212 toward ~248 with angles not yet in the
bank: Melchizedek of Salem; Enoch; Noah's raven; the tree of life
guarded by cherubim; baby Moses in the bulrushes; Aaron's rod that
budded; Achan's devoted spoils; Jephthah's rash vow; Micah's
justice-kindness-humility; Esther; Job; Nehemiah the cupbearer;
Anna the prophetess; John the Baptist's dress and food and Herodias;
the seventy sent out; the rich young ruler; Martha and Mary; the
widow of Nain; the four thousand; the bread of life; the way and
Thomas; the Last Supper bread; Peter sinking; Get behind me Satan;
Nathanael under the fig tree; the cursed barren fig tree; the
Gethsemane cup; Cornelius; the Macedonian call; Eutychus at Troas;
Apollos instructed by Priscilla and Aquila; the sword of the
Spirit; one body many members; Count it all joy; grace sufficient
for the thorn. Scanned against WAEC rounds 1-5, NECO CRS (all
rounds) and the JAMB pool.

    python3 scripts/build_neco_batch174.py -> content/batch_174_waec_crs6.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Christian Religious Studies"

T_CRE = "Creation and the Early Patriarchs"
T_PAT = "The Patriarchs"
T_MOS = "Moses and the Exodus"
T_WIL = "Wilderness Journey"
T_SET = "Settlement and the Kingdom"
T_JUD = "The Judges"
T_PRO = "The Prophets"
T_OTC = "Old Testament Characters and Events"
T_BEM = "The Birth and Early Ministry of Jesus"
T_MIN = "The Ministry of Jesus"
T_MIR = "The Miracles of Jesus"
T_PAR = "The Passion and Resurrection"
T_ACT = "The Acts of the Apostles"
T_ECH = "The Early Church"
T_THM = "Biblical Themes and Teachings"
T_QUO = "Quotations and Sayings"

PASSAGES = []
PQ = []

Q = [
    (T_PAT, "Hard", "Melchizedek, who brought out bread and wine and blessed Abram, was king of",
     "Salem", "Sodom", "Shiloh", "Shechem", "A",
     "Salem's priestly king blessed the patriarch."),
    (T_CRE, "Hard", "Of the early patriarchs, the one who walked with God and then was not, because God took him, was",
     "Enoch", "Methuselah", "Lamech", "Seth", "A",
     "Enoch stepped from earth into God's presence."),
    (T_CRE, "Easy", "To learn whether the flood waters had dried, Noah first sent out from the ark",
     "a raven", "a dove", "a sparrow", "an eagle", "A",
     "The raven flew to and fro while the earth still dripped."),
    (T_CRE, "Medium", "After Adam and Eve left Eden, cherubim and a flaming sword were set to guard",
     "the way to the tree of life", "the tree of knowledge",
     "Eden's southern border", "the altar of Cain", "A",
     "Mortals may not yet seize immortal life."),
    (T_MOS, "Easy", "To hide baby Moses from Pharaoh's decree, his mother placed him in",
     "a basket made of bulrushes", "a fishing canoe",
     "a clay pot sealed with pitch", "the reeds without a covering", "A",
     "The papyrus ark floated him to Pharaoh's daughter."),
    (T_WIL, "Hard", "When Korah's rebellion was judged, the proof that God had chosen Aaron was that Aaron's rod alone",
     "blossomed and bore almonds", "turned into a serpent",
     "struck water from a rock", "blazed with heavenly fire", "A",
     "A dead stick flowered overnight in the tabernacle."),
    (T_SET, "Hard", "Israel's first defeat at the little town of Ai was traced to Achan's sin of",
     "taking devoted spoils from Jericho", "bowing to a Moabite idol",
     "striking the rock in anger", "murmuring against Joshua", "A",
     "The accursed spoils hidden in his tent brought defeat."),
    (T_JUD, "Hard", "The judge who made a rash vow concerning whatever first came out of his house to meet him was",
     "Jephthah", "Gideon", "Samson", "Abimelech", "A",
     "His daughter came out with timbrels to greet him."),
    (T_PRO, "Hard", "To do justice, and to love kindness, and to walk humbly with your God is the divine requirement summed up by",
     "Micah", "Malachi", "Amos", "Joel", "A",
     "Micah distilled the whole duty of man in one line."),
    (T_OTC, "Medium", "The Jewish queen who risked her life to save her people from Haman's plot was",
     "Esther", "Deborah", "Ruth", "Bathsheba", "A",
     "She approached the king unbidden for her people's sake."),
    (T_OTC, "Easy", "The patient man of Uz who lost children, wealth and health, yet did not curse God, was",
     "Job", "Jonah", "Jeremiah", "Joseph", "A",
     "The Lord gave and took away; still he blessed God's name."),
    (T_OTC, "Medium", "The royal cupbearer who returned from Persia to rebuild Jerusalem's broken walls was",
     "Nehemiah", "Ezra", "Zerubbabel", "Mordecai", "A",
     "He left the palace to mend the city's walls."),
    (T_BEM, "Medium", "In the temple, the aged prophetess who also recognised the baby Jesus, beside Simeon, was",
     "Anna", "Elizabeth", "Mary of Nazareth", "Joanna", "A",
     "The widow of eighty-four spoke of him to all who waited."),
    (T_BEM, "Easy", "John the Baptist wore clothing of camel's hair, and his food was",
     "locusts and wild honey", "bread and dried fish",
     "figs and dates", "manna and quail", "A",
     "The desert prophet lived on the desert's own food."),
    (T_MIN, "Medium", "Herod Antipas locked John the Baptist in prison because John had spoken against his marriage to",
     "Herodias, his brother's wife", "Salome the dancer",
     "Mary of Magdala", "Joanna the steward's wife", "A",
     "The prophet paid for telling the truth about a marriage."),
    (T_MIN, "Medium", "Besides the twelve apostles, Jesus once sent out seventy others, and they came back rejoicing that",
     "even the demons obeyed them", "they had been made rich",
     "the Romans had fled the region", "all Israel had repented at once", "A",
     "Their mission bore signs of the kingdom's power."),
    (T_MIN, "Easy", "The rich young ruler walked away sorrowful because Jesus told him to",
     "sell all he had and give to the poor", "preach in the synagogues for a year",
     "fast twice a week like the Pharisees", "leave Galilee and live in Judah", "A",
     "His many possessions held his heart too tightly."),
    (T_MIN, "Easy", "In the home at Bethany, Jesus commended Mary, the sister of Martha, because she",
     "sat at his feet listening to his word", "cooked the finest dishes",
     "washed the feet of the apostles", "sang psalms while others worked", "A",
     "She chose the good portion that cannot be taken."),
    (T_MIR, "Medium", "At the gate of Nain, Jesus stopped a funeral procession and raised",
     "the only son of a widow", "Lazarus of Bethany",
     "Jairus' little daughter", "Eutychus of Troas", "A",
     "He handed the young man back to his weeping mother."),
    (T_MIR, "Hard", "Besides the five thousand, Jesus also fed a great multitude of about",
     "four thousand with seven loaves", "three thousand with two fishes",
     "two thousand with five loaves", "seven thousand with twelve baskets", "A",
     "Seven baskets of fragments were gathered afterwards."),
    (T_THM, "Medium", "After the feeding in John's Gospel, Jesus told the crowd that he himself was",
     "the bread of life", "the light of the world",
     "the good shepherd", "the true vine", "A",
     "Whoever comes to him shall never hunger."),
    (T_QUO, "Medium", "The words I am the way, and the truth, and the life were spoken by Jesus in answer to",
     "Thomas", "Philip", "Peter", "John", "A",
     "Thomas had asked how they could know the way."),
    (T_PAR, "Easy", "At the Last Supper, the bread that Jesus broke and gave to his disciples stood for",
     "his body", "his blood",
     "the new nation of Israel", "the Passover lamb's shelter", "A",
     "Take, eat; this is my body given for you."),
    (T_MIN, "Medium", "Peter began to sink while walking on the water because",
     "he saw the strong wind and was afraid", "he forgot every stroke of swimming",
     "Jesus turned his back for a moment", "the rope from the boat snapped", "A",
     "Faith faltered at the sight of the waves."),
    (T_MIN, "Hard", "The sharp words Get behind me, Satan, spoken after Peter rebuked his Master, mean that Peter",
     "was standing in the way of the suffering to come", "had become a secret follower of Satan",
     "no longer counted among the twelve", "would betray Jesus that very night", "A",
     "Peter's kindness fought against the cross."),
    (T_MIN, "Hard", "Jesus greeted the newcomer still sitting under the fig tree as an Israelite indeed, in whom is no guile. The man was",
     "Nathanael", "Philip", "Andrew", "Thaddaeus", "A",
     "Philip had brought him from Galilee's shadows."),
    (T_MIN, "Hard", "The barren fig tree that Jesus cursed on the road from Bethany stood for",
     "religion that professes without fruit", "the money changers of the temple",
     "the unbelief of the Roman occupiers", "the poverty of the Galilean farms", "A",
     "Leaves without figs drew his dying curse."),
    (T_PAR, "Medium", "In Gethsemane, Jesus prayed, Father, if it be possible, let this",
     "cup pass from me", "cross leave me",
     "hour tarry beyond dawn", "chalice be broken first", "A",
     "Yet not my will, but yours, be done."),
    (T_ACT, "Medium", "The Roman centurion whose prayers and alms God remembered, bringing Peter to Caesarea, was",
     "Cornelius", "Julius", "Claudius", "Felix", "A",
     "A Gentile's devotion opened the door of the church."),
    (T_ACT, "Hard", "Paul first crossed into Europe after a night vision of a man from",
     "Macedonia pleading for help", "Athens quoting the poets",
     "Rome demanding an appeal", "Corinth measuring a temple", "A",
     "Come over and help us, the vision said."),
    (T_ACT, "Hard", "Eutychus, the young man who sank into sleep during Paul's midnight sermon at Troas,",
     "was taken up alive after Paul embraced him", "was buried before the next sunrise",
     "recovered only after three days of prayer", "turned out to be the city's chief magistrate", "A",
     "He fell from the third storey and lived again."),
    (T_ACT, "Hard", "The eloquent preacher of Alexandria whom Priscilla and Aquila took aside and instructed more fully was",
     "Apollos", "Titus", "Silas", "Barnabas", "A",
     "Mighty in the scriptures, he learned the way better still."),
    (T_THM, "Easy", "In Paul's armour of God, the sword of the Spirit stands for",
     "the word of God", "the believer's testimony in court",
     "the protection of angels", "the decrees of church councils", "A",
     "The only weapon of the whole armour is God's word."),
    (T_QUO, "Hard", "I have fought the good fight, I have finished the race, I have kept the faith were Paul's parting words",
     "in his final letter to Timothy", "at his trial before Festus",
     "on the Areopagus in Athens", "in the storm on the Adriatic", "A",
     "The aged apostle looked back on a finished course."),
    (T_QUO, "Medium", "Count it all joy, my brethren, when you meet various trials opens the letter of",
     "James", "Peter", "Paul to the Romans", "John the elder", "A",
     "Trials, the letter says, test and steady our faith."),
    (T_QUO, "Hard", "My grace is sufficient for you was the Lord's answer to Paul concerning",
     "the thorn in his flesh", "his imprisonment at Rome",
     "the storm that wrecked his ship", "the loss of his eyesight in Asia", "A",
     "Strength reaches its full height in weakness."),
]

build_batch(
    S,
    "batch_174_waec_crs6.json",
    "174",
    "WAEC CRS round 6 (R33 top-up): Melchizedek of Salem; Enoch "
    "taken; Noah's raven first; the tree of life guarded; baby "
    "Moses in bulrushes; Aaron's almond rod; Achan's devoted "
    "spoils; Jephthah's vow; Micah's justice-kindness-humility; "
    "Esther; Job; Nehemiah the cupbearer; Anna the prophetess; "
    "John's camel-hair dress and locusts; Herodias behind the "
    "prison; the seventy return; the rich young ruler; Mary at "
    "his feet; the widow of Nain; the four thousand; the bread of "
    "life; the way answered to Thomas; Last Supper bread as his "
    "body; Peter sinking at the wind; Get behind me Satan; "
    "Nathanael under the fig tree; the cursed barren fig tree; "
    "the Gethsemane cup; Cornelius; the Macedonian call; Eutychus "
    "at Troas; Apollos with Priscilla and Aquila; the sword of "
    "the Spirit; one body many members; Count it all joy; grace "
    "sufficient for the thorn. Scanned against WAEC rounds 1-5, "
    "NECO CRS (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
