"""Batch 200 - WAEC Christian Religious Studies round 7 (WAEC top-up, R39).

Grows WAEC CRS from 248 toward ~269 with angles not yet in the
bank: the tower of Babel; Hagar and Ishmael; Rebekah at the well;
Esau's birthright; Joseph's dreams; Jacob wrestling at Peniel;
Joshua and Caleb among the spies; Balaam's donkey; Ruth gleaning
in Boaz's field; Dinah at Shechem; Zachariah and Elizabeth;
Peter's vision at Joppa; Saul on the Damascus road; Paul at
Athens; Paul before Agrippa; the viper at Malta; the fruit of the
Spirit; the widow's mite; Nicodemus; Barabbas; the Lord's Prayer
opening. Scanned against the whole CRS pool (WAEC, NECO and JAMB
stems, 1,548 items).

    python3 scripts/build_neco_batch200.py -> content/batch_200_waec_crs7.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Christian Religious Studies"

T_GEN = "Themes from the Creation to the Patriarchs"
T_EXO = "Moses and the Exodus"
T_SET = "Settlement in Canaan"
T_KIN = "Kings and the Monarchy"
T_MIN = "The Ministry of Jesus"
T_PAS = "The Passion and Resurrection"
T_ACT = "The Apostles and the Early Church"

PASSAGES = []
PQ = []

Q = [
    (T_GEN, "Medium", "The people who set out to build a tower reaching to heaven at Babel were scattered because God",
     "confused their language", "burnt the tower down",
     "sent a great flood", "sent them into Egypt", "A",
     "Suddenly no worker understood another."),
    (T_GEN, "Medium", "When Hagar fled from Sarah's harsh treatment in the wilderness, God",
     "sent her back with a promise", "delivered her to Pharaoh",
     "took Ishmael from her", "struck her with blindness", "A",
     "Ishmael too would father a nation."),
    (T_GEN, "Medium", "At the well outside Nahor, the damsel who watered a stranger's camels without being asked was",
     "Rebekah", "Rachel",
     "Leah", "Miriam", "A",
     "Her kindness watered a whole household's future."),
    (T_GEN, "Easy", "In Joseph's first dream, the sheaves in the field that bowed down to his own sheaf belonged to",
     "his brothers", "the Egyptians",
     "his father's servants", "the Pharaoh's guards", "A",
     "Even in sleep the brothers were angry."),
    (T_GEN, "Hard", "Jacob wrestled with a mysterious man through the night at a place he later named",
     "Peniel", "Bethel",
     "Beersheba", "Shechem", "A",
     "There he saw God face to face."),
    (T_SET, "Hard", "The donkey that refused to move and finally spoke belonged to the seer who was travelling to curse Israel. He was",
     "Balaam", "Balak",
     "Balaam's servant", "Eli's son", "A",
     "The beast saw what the seer could not."),
    (T_SET, "Medium", "The Moabite widow who stayed with Naomi and gleaned in the fields of her future husband was",
     "Ruth", "Orpah",
     "Rahab", "Tamar", "A",
     "Her loyalty led her into David's line."),
    (T_SET, "Hard", "The outrage committed against Jacob's daughter Dinah happened in the city of",
     "Shechem", "Jericho",
     "Shiloh", "Gibeon", "A",
     "Her brothers answered with the sword."),
    (T_KIN, "Medium", "The elderly couple Zechariah and Elizabeth were the parents of",
     "John the Baptist", "Jesus",
     "James and John", "Simon Peter", "A",
     "The forerunner came from a barren womb."),
    (T_MIN, "Medium", "While praying on a housetop in Joppa, Peter saw a great sheet let down from heaven filled with",
     "all kinds of animals", "burning coals of fire",
     "wheat and grapes", "shining angels", "A",
     "What God has cleansed, call not common."),
    (T_MIN, "Medium", "The Pharisee who came to Jesus by night and was told he must be born again was",
     "Nicodemus", "Joseph of Arimathea",
     "Gamaliel", "Simon the leper", "A",
     "A ruler of the Jews sought the truth in secret."),
    (T_MIN, "Medium", "In the temple treasury, Jesus commended a poor widow who gave",
     "two small coins", "one tenth of her harvest",
     "a silver shekel", "nothing but prayers", "A",
     "She gave all she had to live on."),
    (T_PAS, "Medium", "The prisoner whom Pilate released to the crowd instead of Jesus was",
     "Barabbas", "Bartimaeus",
     "Zacchaeus", "Lazarus", "A",
     "A murderer walked free in the Master's place."),
    (T_PAS, "Easy", "The prayer Jesus taught his disciples begins with the words",
     "Our Father who art in heaven", "Holy, holy, holy Lord",
     "Give us this day our bread", "Thy kingdom come first", "A",
     "It opens by hailing God as Father."),
    (T_ACT, "Medium", "The light that flashed around Saul on the road to Damascus left him",
     "blind for three days", "mute for three years",
     "lame in both feet", "white as snow", "A",
     "The persecutor was led away by the hand."),
    (T_ACT, "Hard", "In Athens, Paul began his sermon at the Areopagus from an altar he had seen bearing the inscription,",
     "To the unknown god", "To Zeus the protector",
     "To the goddess of wisdom", "To the spirit of Athens", "A",
     "He preached the God they worshipped unknowingly."),
    (T_ACT, "Hard", "After his shipwreck on the island of Malta, Paul was unharmed when",
     "a viper fastened on his hand", "a lion charged at him",
     "he was stoned by the crowd", "the sea swallowed him", "A",
     "He shook the creature into the fire."),
    (T_ACT, "Hard", "Paul defended himself before King Agrippa, who afterwards remarked that Paul almost",
     "persuaded him to be a Christian", "escaped from his chains",
     "converted the whole court", "won his freedom by cunning", "A",
     "The king heard the word and hesitated."),
    (T_ACT, "Medium", "The first fruit of the Spirit listed by Paul in his letter to the Galatians is",
     "love", "joy",
     "peace", "patience", "A",
     "Love heads the harvest of the Spirit."),
]

build_batch(
    S,
    "batch_200_waec_crs7.json",
    "200",
    "WAEC CRS round 7 (R39 top-up): Babel's confused language; "
    "Hagar's promise; Rebekah at the well; Esau's birthright; "
    "Joseph's dream of sheaves; Peniel; Joshua and Caleb; Balaam's "
    "donkey; Ruth gleaning; Dinah at Shechem; Zechariah and "
    "Elizabeth; Peter's sheet at Joppa; Nicodemus; the widow's "
    "mite; Barabbas; the Lord's Prayer opening; Saul blinded at "
    "Damascus; the unknown god at Athens; the Malta viper; "
    "Agrippa's almost-persuasion; love the first fruit of the "
    "Spirit. Scanned against the whole CRS pool (WAEC, NECO and "
    "JAMB stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
