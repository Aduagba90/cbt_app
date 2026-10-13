"""Batch 078 - WAEC Christian Religious Studies, Paper 1 Objective round 1.

WASSCE Christian Religious Studies Paper 1 (Objective) is a 50-item paper
(1 hr; official 2026 second-series timetable, paper 2021). This batch covers
the WASSCE CRS syllabus with FRESH angles and phrasings - named-episode
details (Judah's surety, Simon of Cyrene, the 153 fish, Matthias), numeric
answers (30 silver pieces, 120 believers, 40 days, 300 men), quotation-
based items and question-form stems - because the near-dup scan checks
every item against the JAMB, WAEC and NECO banks, including the very large
JAMB CRS banks (batches 004, 025-027) and our 88-item NECO CRS bank.

    python3 scripts/build_neco_batch78.py -> content/batch_078_waec_crs.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Christian Religious Studies"

T_OT = "Old Testament Characters and Events"
T_NT = "The Ministry of Jesus"
T_PAR = "Parables and Miracles"
T_PASS = "The Passion and Resurrection"
T_EARLY = "The Early Church and the Apostles"
T_TH = "Biblical Themes and Teachings"
T_QU = "Quotations and Sayings"

PASSAGES = []
PQ = []

Q = [
    # ---------------------------------------------------------------- old testament
    (T_OT, "Medium", "Pharaoh made Joseph his deputy after Joseph explained the meaning of his",
     "dreams", "laws", "taxes", "wars", "A",
     "Pharaoh's dreams lifted Joseph up."),
    (T_OT, "Hard", "The brother of Joseph who offered himself as surety for Benjamin was",
     "Judah", "Reuben", "Levi", "Simeon", "A",
     "Judah pleaded for the boy."),
    (T_OT, "Medium", "When Samuel first heard God's call at Shiloh, he thought the voice was",
     "Eli's", "his mother's", "an angel's", "Saul's", "A",
     "The boy mistook the Lord for Eli."),
    (T_OT, "Easy", "Whom did Samuel anoint as Israel's first king?",
     "Saul", "David", "Solomon", "Gideon", "A",
     "Saul of Benjamin came first."),
    (T_OT, "Medium", "Elijah challenged the prophets of Baal on Mount",
     "Carmel", "Sinai", "Gilgal", "Nebo", "A",
     "Fire fell on Carmel's altar."),
    (T_OT, "Medium", "Ravens bringing food to Elijah by the brook Cherith show God's",
     "care in time of need", "anger at Ahab", "judgment on Israel", "rules about fasting", "A",
     "God fed his hunted servant."),
    (T_OT, "Hard", "Naaman the Syrian army captain was cured of leprosy when he",
     "washed in the Jordan", "touched Elijah's rod", "fasted seven days", "sacrificed on Carmel", "A",
     "Seven dips made him clean."),
    (T_OT, "Medium", "The decree that landed Daniel among the lions forbade",
     "prayer to any god but the king", "eating the royal food", "worship in Jerusalem city", "reading the scrolls of prophets", "A",
     "His daily prayer broke the decree."),
    (T_OT, "Medium", "Nineveh's response to Jonah's warning was to",
     "fast and put on sackcloth", "laugh at his sermon", "chase him from the city", "attack the ships of Tarshish", "A",
     "The whole city turned to God."),
    (T_OT, "Easy", "The boy David's weapon against Goliath was",
     "a sling and a stone", "a sword and shield", "a bronze spear", "a chariot and horse", "A",
     "One smooth stone brought him down."),
    (T_OT, "Hard", "Gideon's army was reduced to 300 men so that",
     "Israel would credit God", "the Midianites would mock", "the war would last longer", "fewer men would eat much", "A",
     "The small force barred all boasting."),
    (T_OT, "Medium", "King Solomon asked God above all for",
     "a wise and understanding heart", "long life and great riches", "victory over his enemies", "fame among the nations", "A",
     "Wisdom was his one request."),
    (T_OT, "Hard", "The exile to Babylon ended when",
     "Cyrus of Persia freed the Jews", "the Assyrians repented", "Egypt invaded Babylon", "the temple was rebuilt", "A",
     "Cyrus decreed the return home."),
    # ---------------------------------------------------------------- ministry of jesus
    (T_NT, "Easy", "Jesus fasted in the wilderness for",
     "40 days", "7 days", "12 days", "70 days", "A",
     "Forty days of testing prepared him."),
    (T_NT, "Easy", "The baptism of Jesus took place in the River",
     "Jordan", "Nile", "Euphrates", "Kishon", "A",
     "John baptised him in the Jordan."),
    (T_NT, "Easy", "The stone jars at Cana were filled with water that became",
     "wine", "blood", "oil", "milk", "A",
     "The water pots held the new wine."),
    (T_NT, "Medium", "How many pieces of silver did Judas receive for betraying Jesus?",
     "30", "20", "40", "100", "A",
     "Thirty silver coins sealed the deal."),
    (T_NT, "Medium", "Peter's denial of Jesus happened in the courtyard of",
     "the high priest", "Pilate's palace", "the temple", "Herod's court", "A",
     "A servant girl challenged him there."),
    (T_NT, "Hard", "'Foxes have holes... but the Son of man has nowhere to lay his head' teaches",
     "the cost of following Jesus", "the need to build houses", "contempt for animals", "wealth for disciples", "A",
     "Discipleship demands sacrifice."),
    (T_NT, "Medium", "Jesus chose the twelve apostles mainly to",
     "be with him and preach", "collect temple taxes", "interpret Roman law", "guard the synagogues", "A",
     "Companionship came first, then mission."),
    (T_NT, "Medium", "Zacchaeus climbed a sycamore tree to see Jesus because he was",
     "small in stature", "blind from birth", "lame in both legs", "carrying water", "A",
     "The short tax collector climbed up."),
    (T_NT, "Medium", "The first miracle of Jesus recorded in John's Gospel occurred at",
     "Cana in Galilee", "Bethany near Jordan", "Capernaum by the lake", "Jericho on the road", "A",
     "John opens the signs at Cana."),
    (T_NT, "Medium", "By wrapping a towel and washing feet, Jesus modelled",
     "humble service", "ritual bathing", "social rank", "foot hygiene", "A",
     "The master took the slave's place."),
    # ---------------------------------------------------------------- parables and miracles
    (T_PAR, "Medium", "In the sower parable, the seed among thorns stands for hearers choked by",
     "worries and wealth", "scorching sunlight", "birds of the air", "hard village paths", "A",
     "Life's cares crowd out the word."),
    (T_PAR, "Medium", "How did the father receive the returning prodigal son?",
     "with a feast and a robe", "with a public trial", "with a bill of debts", "with exile from home", "A",
     "He ran, embraced and clothed him."),
    (T_PAR, "Medium", "The good Samaritan proved neighbourliness by",
     "bandaging and paying his bills", "passing by on the other side", "praying for him at the temple", "reporting the case to priests", "A",
     "Mercy crossed every boundary."),
    (T_PAR, "Medium", "Why did the master rebuke the servant who received one talent?",
     "he hid it in the ground", "he traded it wisely", "he gave it to bankers", "he doubled it quickly", "A",
     "Idle burying earned the rebuke."),
    (T_PAR, "Hard", "The home village of Lazarus, whom Jesus called out of the tomb, was",
     "Bethany", "Bethlehem", "Nazareth", "Capernaum", "A",
     "Bethany sat near Jerusalem."),
    (T_PAR, "Medium", "The great catch of fish came after Jesus told Peter to",
     "let down the nets again", "sail to the other side", "fish alone at midnight", "buy better tackle first", "A",
     "Obedience filled both boats."),
    (T_PAR, "Medium", "When Jesus calmed the storm, the disciples' fear turned to",
     "awed wonder", "open rebellion", "deep sleep", "loud laughter", "A",
     "They asked who he could be."),
    (T_PAR, "Medium", "The widow's two coins pleased Jesus because she gave",
     "all she had to live on", "a tenth of her wealth", "gold coins gladly", "out of her surplus", "A",
     "Her gift cost her everything."),
    (T_PAR, "Hard", "The ten lepers Jesus healed were told to",
     "show themselves to the priests", "wash in the pool of Siloam", "bring water to the master", "wait a week outside camp", "A",
     "The law required priestly cleansing."),
    (T_PAR, "Medium", "The shepherd who left ninety-nine sheep rejoiced over",
     "the one lost sheep found", "the wolves driven away", "the new pasture gained", "the fold's large size", "A",
     "One rescued soul fills heaven's joy."),
    # ---------------------------------------------------------------- passion and resurrection
    (T_PASS, "Easy", "The garden where Jesus prayed before his arrest was",
     "Gethsemane", "Golgotha", "Siloam", "Eden", "A",
     "He prayed in agony at Gethsemane."),
    (T_PASS, "Easy", "Who passed the final death sentence on Jesus?",
     "Pontius Pilate", "Caiaphas the high priest", "Herod Antipas", "Judas Iscariot", "A",
     "Pilate washed his hands but agreed."),
    (T_PASS, "Medium", "Simon of Cyrene was forced to",
     "carry Jesus' cross", "crown Jesus with thorns", "guard the garden tomb", "betray the master", "A",
     "He was seized from the crowd."),
    (T_PASS, "Hard", "The betrayer's kiss in Gethsemane identified Jesus to",
     "the arresting party", "the twelve apostles", "the Roman governor", "the watching women", "A",
     "A kiss was the agreed signal."),
    (T_PASS, "Medium", "'Truly this was the Son of God' was spoken at the cross by",
     "a Roman centurion", "one of the thieves", "Joseph of Arimathea", "Simon Peter", "A",
     "The soldier saw and confessed."),
    (T_PASS, "Hard", "The number of fish in the catch by the risen Jesus' direction was",
     "153", "53", "100", "200", "A",
     "John counts the great fish exactly."),
    (T_PASS, "Medium", "Thomas is called 'doubting' because he demanded to",
     "see and touch the wounds", "hear the voice again", "wait for the Spirit", "walk to Emmaus first", "A",
     "He set his own proof terms."),
    (T_PASS, "Medium", "The risen Jesus appeared to two disciples walking to",
     "Emmaus", "Bethany", "Jericho", "Damascus", "A",
     "He made himself known at table."),
    (T_PASS, "Medium", "The empty tomb was first reported to the disciples by",
     "the women", "Peter himself", "Roman guards", "Joseph of Arimathea", "A",
     "They ran from the garden with news."),
    (T_PASS, "Medium", "The temple curtain tore from top to bottom when",
     "Jesus died on the cross", "the earth was created", "Peter preached at Pentecost", "the tomb was sealed", "A",
     "His death opened the way in."),
    # ---------------------------------------------------------------- early church
    (T_EARLY, "Hard", "At Pentecost the believers in the upper room numbered about",
     "120", "12", "70", "500", "A",
     "Acts counts one hundred twenty."),
    (T_EARLY, "Easy", "At Pentecost the Holy Spirit rested on the believers like tongues of",
     "fire", "water", "wind only", "doves", "A",
     "Flames of fire sat on each head."),
    (T_EARLY, "Medium", "Matthias was chosen by lot to replace",
     "Judas Iscariot", "Thomas Didymus", "Barnabas the Levite", "Stephen the deacon", "A",
     "The vacant place was refilled."),
    (T_EARLY, "Easy", "The first Christian martyr was",
     "Stephen", "James the elder", "Peter", "Philip", "A",
     "His stoning is told in Acts."),
    (T_EARLY, "Medium", "Saul of Tarsus was travelling to Damascus when",
     "a bright light blinded him", "a storm wrecked his ship", "an angel fed him bread", "a prophet anointed him", "A",
     "The risen Lord met him on the road."),
    (T_EARLY, "Hard", "Peter's vision of the sheet let down from heaven taught him that",
     "no person is common or unclean", "all foods were now holy food", "pigs must never be eaten", "Gentiles were excluded still", "A",
     "God cleansed what he had called."),
    (T_EARLY, "Hard", "The Ethiopian official whom Philip baptised had been reading",
     "the book of Isaiah", "the book of Moses", "the psalms of David", "the letters of Peter", "A",
     "He read the suffering servant."),
    (T_EARLY, "Medium", "Barnabas, the 'son of encouragement', showed his generosity by",
     "selling a field for the church", "preaching in Damascus city", "writing an epistle to Rome", "leading a revolt in Jerusalem", "A",
     "Giving marked the early church."),
    (T_EARLY, "Medium", "Paul's trade, by which he earned his keep, was",
     "tent-making", "fishing", "carpentry", "farming", "A",
     "He worked leather with his hands."),
    (T_EARLY, "Hard", "In which city did believers first wear the name 'Christians'?",
     "Antioch", "Jerusalem", "Corinth", "Rome", "A",
     "The Antioch church coined the name."),
    # ---------------------------------------------------------------- themes and teachings
    (T_TH, "Medium", "Which petition comes first in the Lord's Prayer after 'our Father'?",
     "hallowing God's name", "asking for daily bread", "seeking forgiveness of sins", "praying against evil", "A",
     "God's name is hallowed first."),
    (T_TH, "Easy", "'Love your neighbour as yourself' is called",
     "the second great commandment", "the first commandment", "a beatitude", "a psalm of David", "A",
     "Love of neighbour ranks with God."),
    (T_TH, "Medium", "The fruit of the Spirit in Galatians includes",
     "patience and self-control", "silver and fine gold", "fame and long life", "swords and sceptres", "A",
     "Character, not cargo, is fruit."),
    (T_TH, "Medium", "Faith without works, says the letter of James, is",
     "dead", "living", "perfect", "priceless", "A",
     "True faith acts and works."),
    (T_TH, "Medium", "'You shall know the truth, and the truth will make you free' was said by",
     "Jesus", "Peter", "Paul", "James", "A",
     "Jesus promised freedom to hearers."),
    (T_TH, "Easy", "Paul names the greatest of faith, hope and love as",
     "love", "faith", "hope", "knowledge", "A",
     "Love is the greatest of the three."),
    (T_TH, "Medium", "Calling Christians 'the light of the world' demands",
     "a visible good example", "secret worship habits", "night-long prayer vigils", "quiet withdrawal from men", "A",
     "A city on a hill cannot hide."),
    (T_TH, "Hard", "Jesus taught that faithfulness in little things shows a person can be trusted with",
     "much", "nothing", "little", "titles", "A",
     "Small stewardship proves the heart."),
    (T_TH, "Medium", "The early believers' sharing of goods in Acts models",
     "Christian fellowship", "private ownership", "temple taxation", "Roman welfare grants", "A",
     "None lacked among the early believers."),
    (T_TH, "Medium", "Peter teaches that believers who suffer for doing right are",
     "blessed", "cursed", "foolish", "forgotten", "A",
     "Suffering with God's approval wins."),
    # ---------------------------------------------------------------- quotations
    (T_QU, "Hard", "'Before I formed you in the womb I knew you' was God's word to",
     "Jeremiah", "Isaiah", "Ezekiel", "Amos", "A",
     "The young prophet heard his call."),
    (T_QU, "Medium", "'Here am I, the servant of the Lord' was the reply of",
     "Mary", "Elizabeth", "Martha", "Anna", "A",
     "Mary answered the angel Gabriel."),
    (T_QU, "Easy", "'Am I my brother's keeper?' was the question of",
     "Cain", "Abel", "Seth", "Esau", "A",
     "Cain deflected God's question."),
    (T_QU, "Medium", "'As for me and my house, we will serve the LORD' was declared by",
     "Joshua", "Moses", "Caleb", "Gideon", "A",
     "Joshua charged Israel at Shechem."),
    (T_QU, "Hard", "'The fear of the LORD is the beginning of wisdom' is written in",
     "Proverbs", "Psalms", "Job", "Ecclesiastes", "A",
     "Proverbs opens with this key."),
    (T_QU, "Easy", "'Blessed are the peacemakers' is one of the",
     "beatitudes", "commandments", "parables", "epistles", "A",
     "The Sermon lists the beatitudes."),
]

build_batch(
    S,
    "batch_078_waec_crs.json",
    "078",
    "WAEC Christian Religious Studies Paper 1 round 1 (Round 16e): the WASSCE "
    "syllabus with FRESH angles - named-episode details (Judah's surety, "
    "Simon of Cyrene, the 153 fish, Matthias, Antioch), numeric answers (30 "
    "silver pieces, 120 believers, 40 days, 300 men, 153 fish), quotation "
    "items ('Before I formed you...', 'Am I my brother's keeper?') and "
    "question-form stems - because the near-dup scan checks every item "
    "against the JAMB, WAEC and NECO banks INCLUDING the very large JAMB CRS "
    "banks (004, 025-027) and the 88-item NECO CRS bank. Topics: Old "
    "Testament characters and events, the ministry of Jesus, parables and "
    "miracles, the passion and resurrection, the early church, biblical "
    "themes, quotations.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
