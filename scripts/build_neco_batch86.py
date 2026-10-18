"""Batch 086 - NECO Christian Religious Studies round 2 (NECO lift, R18).

NECO CRS objective draws 60 items; the bank stood at 88. This lift uses
named-episode details not yet in any bank - Sarah's laugh, Esau's pottage,
Jacob at Peniel, the silver cup, Aaron and Hur, Achan, Rhoda, Priscilla and
Aquila - plus fresh theme and quotation items. Scanned against NECO round
1, the WAEC twin and the large JAMB CRS banks.

    python3 scripts/build_neco_batch86.py -> content/batch_086_neco_crs2.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Christian Religious Studies"

T_PAT = "The Patriarchs"
T_MOS = "Moses and the Exodus"
T_JOS = "Joshua and the Judges"
T_KING = "The Kings of Israel"
T_PRO = "The Prophets"
T_JES = "The Life and Ministry of Jesus"
T_PASS = "The Passion and the Resurrection"
T_EAR = "The Early Church"
T_TH = "Themes and Teachings"

PASSAGES = []
PQ = []

Q = [
    # ---------------------------------------------------------------- patriarchs
    (T_PAT, "Easy", "When the three visitors promised Sarah a son, she",
     "laughed in disbelief", "danced for joy", "fell on her face", "prayed aloud", "A",
     "Her laugh doubted the promise."),
    (T_PAT, "Easy", "Esau sold his birthright to Jacob for",
     "a bowl of pottage", "thirty pieces of silver", "a flock of sheep", "a piece of land", "A",
     "He traded his right for a meal."),
    (T_PAT, "Medium", "Jacob dreamed of a ladder reaching to heaven at",
     "Bethel", "Peniel", "Beersheba", "Hebron", "A",
     "He anointed the stone at Bethel."),
    (T_PAT, "Hard", "At which place did Jacob wrestle all night and receive the name Israel?",
     "Peniel", "Bethel", "Succoth", "Mahanaim", "A",
     "He struggled with God at Peniel."),
    (T_PAT, "Medium", "To test his brothers, Joseph hid his silver cup in the sack of",
     "Benjamin", "Reuben", "Judah", "Simeon", "A",
     "The youngest brother carried it."),
    # ---------------------------------------------------------------- moses
    (T_MOS, "Easy", "Baby Moses was hidden from Pharaoh's men in",
     "a basket among the reeds", "a cave at Horeb", "the palace kitchen", "a boat on the sea", "A",
     "His mother floated him on the Nile."),
    (T_MOS, "Easy", "God first spoke to Moses from",
     "the burning bush", "Mount Sinai", "the tabernacle", "a still small voice", "A",
     "The bush burned without being consumed."),
    (T_MOS, "Medium", "The last plague that broke Pharaoh's will was the death of",
     "the firstborn", "the livestock", "the crops", "the Nile fish", "A",
     "Egypt's firstborn died in one night."),
    (T_MOS, "Easy", "In the wilderness, God fed Israel with",
     "manna", "barley bread", "roasted lamb", "wild honey only", "A",
     "Bread like frost fell each morning."),
    (T_MOS, "Hard", "During the battle with Amalek, Moses' raised hands were held up by",
     "Aaron and Hur", "Joshua and Caleb", "Eleazar and Ithamar", "Nadab and Abihu", "A",
     "The two held his arms till sunset."),
    # ---------------------------------------------------------------- joshua and judges
    (T_JOS, "Easy", "How did the walls of Jericho come tumbling down?",
     "after seven circuits and a great shout", "by tunnel dug beneath the wall", "by fire set at the gates", "by rams battering the stones", "A",
     "The shout followed the seventh march."),
    (T_JOS, "Hard", "Israel was first defeated at Ai because",
     "Achan took devoted spoil from Jericho", "Joshua prayed on the wrong mountain", "the ark was left at Gilgal", "the spies lied about Ai", "A",
     "Hidden spoil brought defeat."),
    (T_JOS, "Easy", "Samson lost his great strength when",
     "his hair was cut after Delilah's betrayal", "he drank the Philistines' wine", "he left Nazareth for Gaza", "he broke his vow of peace", "A",
     "Delilah sold his secret to the enemy."),
    (T_JOS, "Medium", "The woman who judged Israel and went to battle with Barak was",
     "Deborah", "Jael", "Huldah", "Miriam", "A",
     "She sat under the palm tree judging."),
    # ---------------------------------------------------------------- kings
    (T_KING, "Medium", "David's wrongdoing that drew Nathan's rebuke began with his desire for",
     "Bathsheba", "the throne of Saul", "Naboth's vineyard", "Abigail's flocks", "A",
     "He took another man's wife."),
    (T_KING, "Hard", "Nathan opened David's eyes to his sin with a parable about",
     "a poor man's only lamb", "a lost silver coin", "two sons in a vineyard", "a sower and his seed", "A",
     "'You are the man' closed the parable."),
    (T_KING, "Medium", "Absalom led an armed rebellion against",
     "his father David", "Solomon his brother", "Saul the king", "Jeroboam of Israel", "A",
     "The son rose against the father."),
    (T_KING, "Easy", "Under which king did Israel's first temple rise in Jerusalem?",
     "Solomon", "David", "Ezra", "Zerubbabel", "A",
     "He raised it on Mount Moriah."),
    (T_KING, "Medium", "After Solomon's death, the united kingdom split under his son",
     "Rehoboam", "Jeroboam", "Abijah", "Asa", "A",
     "Ten tribes followed Jeroboam away."),
    (T_KING, "Hard", "Queen Jezebel had Naboth killed so that Ahab could seize his",
     "vineyard", "herds", "silver mines", "city gate", "A",
     "The plot stole Naboth's land."),
    # ---------------------------------------------------------------- prophets
    (T_PRO, "Hard", "At his call, Isaiah felt unclean until a seraph touched his lips with",
     "a burning coal", "river water", "an olive branch", "a scroll", "A",
     "The coal purged his guilt."),
    (T_PRO, "Medium", "Ezekiel's vision of the valley of dry bones promised Israel",
     "restoration to life as a nation", "exile in Babylon forever", "a new temple of gold", "victory over Persia", "A",
     "The bones rose into a vast army."),
    (T_PRO, "Hard", "Hosea's marriage to an unfaithful wife symbolised",
     "Israel's unfaithfulness to God", "Judah's wealth and pride", "the fall of Nineveh", "the coming of the Messiah", "A",
     "The prophet's home mirrored the nation."),
    (T_PRO, "Medium", "Elijah left Elisha as his successor when he was taken up in",
     "the whirlwind", "a fiery chariot alone", "a cloud at noon", "the Jordan flood", "A",
     "Chariots of fire parted them."),
    # ---------------------------------------------------------------- jesus
    (T_JES, "Easy", "The wise men who visited the young Jesus presented",
     "gold, frankincense and myrrh", "bread, wine and oil", "silver, linen and spice", "a lamb, a dove and grain", "A",
     "Three gifts honoured the child."),
    (T_JES, "Easy", "At twelve years old, Jesus amazed the teachers",
     "in the temple at Jerusalem", "by the well of Sychar", "in the synagogue of Nazareth", "on the shores of Galilee", "A",
     "He sat among them, listening and asking."),
    (T_JES, "Easy", "Which food did Jesus bless to feed the five thousand?",
     "five loaves and two fish", "seven loaves alone", "two loaves and five fish", "a boy's lunch of dates", "A",
     "Twelve baskets were left over."),
    (T_JES, "Medium", "Jesus raised the only son of a widow at",
     "Nain", "Bethany", "Capernaum", "Jairus' house", "A",
     "He met the burial procession at the gate."),
    (T_JES, "Medium", "Jesus called himself 'the good shepherd' in which Gospel?",
     "John", "Matthew", "Luke", "Mark", "A",
     "John records the shepherd sayings."),
    # ---------------------------------------------------------------- passion and resurrection
    (T_PASS, "Easy", "The prisoner released in place of Jesus at the trial was",
     "Barabbas", "Bartimaeus", "Nicodemus", "Joseph of Arimathea", "A",
     "The crowd chose him over Christ."),
    (T_PASS, "Medium", "To the penitent thief on the cross, Jesus promised",
     "paradise that same day", "a kingdom on earth", "healing for his legs", "release by Pilate", "A",
     "'Today you will be with me in paradise.'"),
    (T_PASS, "Medium", "The command to make disciples of all nations is known as",
     "the Great Commission", "the new commandment", "the Lord's Prayer", "the Sermon on the Mount", "A",
     "It sent the church to the world."),
    # ---------------------------------------------------------------- early church
    (T_EAR, "Medium", "The couple who died after lying about the price of their land was",
     "Ananias and Sapphira", "Aquila and Priscilla", "Zechariah and Elizabeth", "Philemon and Onesimus", "A",
     "Their lie cost them their lives."),
    (T_EAR, "Medium", "The apostles appointed seven helpers, including Stephen, because",
     "the widows' daily serving caused complaints", "the temple guards had struck them", "the church had no place to meet", "the Gentiles demanded priests", "A",
     "Deacons were chosen to serve tables."),
    (T_EAR, "Hard", "When Peter stood freed at the gate of the prayer house, the maid who announced him was",
     "Rhoda", "Tabitha", "Lydia", "Priscilla", "A",
     "In her joy she left him outside."),
    (T_EAR, "Hard", "In Corinth, Paul stayed and worked at tent-making with",
     "Priscilla and Aquila", "Barnabas and Mark", "Silas and Timothy", "Titus and Luke", "A",
     "The tentmakers hosted him."),
    # ---------------------------------------------------------------- themes
    (T_TH, "Hard", "'Faith is the assurance of things hoped for' is written in",
     "Hebrews", "Romans", "James", "Revelation", "A",
     "Hebrews defines faith this way."),
    (T_TH, "Medium", "Jesus told Peter to forgive his brother",
     "seventy times seven times", "only until the third offence", "as often as the elders judged fit", "whenever repentance was public", "A",
     "Forgiveness knows no limit."),
    (T_TH, "Easy", "'Do to others what you would have them do to you' is popularly called",
     "the Golden Rule", "the great commandment", "the new covenant", "the Lord's Prayer", "A",
     "It sums up fair dealing with others."),
    (T_TH, "Medium", "'We walk by faith, not by sight' was written by",
     "Paul", "Peter", "John", "James", "A",
     "Paul wrote it to the Corinthians."),
    (T_TH, "Medium", "The Bible teaches that pure religion includes caring for",
     "orphans and widows", "priests and Levites", "kings and soldiers", "merchants and farmers", "A",
     "James ties faith to such care."),
]

build_batch(
    S,
    "batch_086_neco_crs2.json",
    "086",
    "NECO CRS round 2 (Round 18 lift): named-episode details new to every "
    "bank - Sarah's laugh, Esau's pottage, Bethel and Peniel, the silver cup "
    "in Benjamin's sack, basket and burning bush, firstborn plague, manna, "
    "Aaron and Hur, Jericho's seven marches, Achan at Ai, Samson and "
    "Delilah, Deborah and Barak, Nathan's ewe-lamb parable, Absalom, "
    "Rehoboam's split, Naboth's vineyard, Isaiah's coal, dry bones, Hosea's "
    "wife, whirlwind, wise men's gifts, temple at twelve, feeding 5000, "
    "widow of Nain, Barabbas, the penitent thief, Great Commission, "
    "Ananias and Sapphira, the seven, Rhoda, Priscilla and Aquila - plus "
    "themes (Hebrews faith, seventy times seven, Golden Rule, walking by "
    "faith, care for widows). Scanned against NECO round 1, the WAEC twin "
    "and the large JAMB CRS banks.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
