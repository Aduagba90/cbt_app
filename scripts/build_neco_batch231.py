"""Batch 231 - WAEC Christian Religious Studies round 10 (WAEC top-up, R47).

Grows WAEC CRS from 267 toward ~292 with angles verified absent from
the whole CRS pool (1,592 items across JAMB, WAEC and NECO): Mary
and Martha (the good portion); anointing at Bethany; the two thieves
at the cross; Jonathan and David's covenant; hidden treasure and
pearl of great price; the great supper; the miraculous draught of
fishes; the widow of Nain's son; John's prologue (the Word was God);
Rachel weeping for the children; 1 Corinthians 15 on the
resurrection body; Philippians 'press toward the goal'; Alpha and
Omega; Sennacherib before Jerusalem; Simon the Pharisee's sinful
woman; the woman with the issue of blood; James on the tongue; new
heaven and new earth; I AM WHO I AM; the year of Jubilee; Solomon's
judgement between two mothers; render to Caesar; 'Jesus wept';
pearls before swine; ask, seek, knock. Checked and avoided (already
banked - the pool is the deepest scanned this round): transfiguration
(22), Cornelius, Peter's prison, Pentecost, Ananias and Sapphira,
Ethiopian eunuch, Emmaus, Thomas (17), triumphal entry, cleansing of
the temple, Gethsemane, Peter's denial, Judas' bargain, Simon of
Cyrene, Ascension, baptism/temptation, centurion, Jairus,
Bartimaeus, ten lepers, five loaves, storm calmed, paralytic, Cana,
Samaritan woman, Lazarus (14 incl. resurrection-saying to Martha),
Nathanael, Matthew's call, Zacchaeus, Joseph of Arimathea, Mary
Magdalene, Caiaphas, Pilate's handwashing, Herodias, Stephen,
Barnabas, Paul and Silas, armour of God, justification, wise
builder, daily-bread petition, Pharisee and tax collector, eleventh
hour, wicked tenants, barren fig tree, John the Baptist's dress,
Messiah's meaning, Psalm 23, sheep and goats, unforgiving servant,
true vine, bread of life, good shepherd, rich young ruler, foot
washing, grace items, Hebrews 11, potter's house, give-us-a-king,
Solomon's foreign wives, Rehoboam, Jeroboam's calves, Naboth, Gehazi,
Jonah (31), Amos justice, Micah swords, Malachi tithes, Jacob's
disguise as Esau, Jacob's ladder, silver cup, Jethro, Korah's rod,
Bathsheba, Nehemiah (22), Esther, Job, Ezra, burning bush,
Passover, Red Sea, manna, water from rock, golden calf, Ten
Commandments, tabernacle, Jericho, Rahab, Achan, Deborah, Samson,
Samuel at Shiloh, Goliath, Absalom, Elijah ravens/Carmel/still
voice, Shunammite, Naaman, Hezekiah, Josiah, Isaiah's coal,
Jeremiah's call, dry bones, fiery furnace, lion's den, Belshazzar,
Boaz-gleaning, I-am-the-resurrection-to-Martha, foxes-have-holes,
take-up-cross, speck-and-beam, love-your-enemies, Talitha, Didymus,
Beatitude items, salt-and-light (10), prodigal son, good Samaritan
family, rich fool, talents, ten virgins, mustard seed, lost coin,
unjust judge, Melchizedek, Ishmael, birthright-pottage, Tamar,
Leah, Immanuel, Simeon/Anna (35), nativity family (42), image of
God, fear-of-the-Lord, 1 Cor 13, thief-in-the-night, new creation.

    python3 scripts/build_neco_batch231.py -> content/batch_231_waec_crs10.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Christian Religious Studies"

T_MIN = "The Ministry of Jesus"
T_PASS = "The Passion and Resurrection"
T_PAR = "Parables and Miracles"
T_OT = "Old Testament Characters and Events"
T_MOSES = "Moses and the Exodus"
T_THEME = "Biblical Themes and Teachings"
T_QUOTE = "Quotations and Sayings"
T_BIRTH = "The Birth and Early Ministry of Jesus"
T_TFA = "Things Fall Apart" if False else "The Patriarchs"

PASSAGES = []
PQ = []

Q = [
    (T_MIN, "Medium", "When Jesus visited the home of Martha in Bethany, Martha busied herself with serving while her sister Mary sat at his feet listening. Jesus told Martha that",
     "Mary had chosen the good portion", "Mary was lazy and careless",
     "Martha had chosen wrongly forever", "both should work in the kitchen", "A",
     "The one thing needful cannot be taken away."),
    (T_PASS, "Medium", "In the house of Simon the leper at Bethany, a woman poured costly ointment on Jesus' head. When the disciples grumbled at the waste, Jesus said",
     "she had anointed him for burial", "she owed the poor an apology",
     "the ointment should have been sold", "Simon had planned it badly", "A",
     "The fragrance of her deed still fills the gospel."),
    (T_PASS, "Easy", "Two criminals were crucified with Jesus, one on his right and one on his left. One of them mocked him, but the other",
     "asked to be remembered in his kingdom", "begged to be taken down",
     "cursed the soldiers also", "promised to repay his debt", "A",
     "'Today you will be with me in Paradise.'"),
    (T_OT, "Easy", "The friendship covenant between David and Jonathan, in which Jonathan stripped himself of his robe, sword and bow and gave them to David, showed that Jonathan",
     "loved David as his own soul", "feared David's army",
     "planned to seize the throne", "was leaving his father's house for ever", "A",
     "The heir gave his all to his friend."),
    (T_PAR, "Hard", "In one short pair of parables, Jesus likened the kingdom of heaven to treasure hidden in a field and to a merchant seeking",
     "fine pearls", "lost sheep",
     "new wineskins", "barley loaves", "A",
     "Both men sold everything to gain the one thing."),
    (T_PAR, "Medium", "In the parable of the great supper, the invited guests all made excuses, so the master ordered his servant to",
     "bring in the poor and maimed", "close the doors forever",
     "postpone the feast for a year", "sell the food in the market", "A",
     "The empty places were filled from the streets."),
    (T_PAR, "Medium", "When Jesus taught from Simon's boat and then told Peter to let down the nets, the catch of fish was so great that the nets began to break. Peter's reaction was to",
     "fell at Jesus' knees, a sinner", "bargain over the price of the fish",
     "send for his partners at once", "ask Jesus to leave the boat", "A",
     "A fisherman knelt before the Lord of the sea."),
    (T_PAR, "Medium", "As Jesus approached the gate of Nain with his disciples, a widow was carrying out her only son to burial. Jesus",
     "touched the bier and raised the young man", "walked on the other side of the road",
     "asked the crowd for a collection", "told the widow to wait for Peter", "A",
     "'Young man, I say to you, arise.'"),
    (T_BIRTH, "Medium", "The Gospel of John opens by declaring that in the beginning was the Word, and the Word was with God, and",
     "the Word was God", "the Word became a scroll",
     "the Word was John", "the Word was light only", "A",
     "The same Word became flesh and dwelt among us."),
    (T_BIRTH, "Hard", "When Herod sought the child Jesus, an angel warned Joseph to flee to Egypt, and Herod, in his rage, killed all the male children of Bethlehem. The sorrow is described as",
     "Rachel weeping for her children", "Leah mourning at Machpelah",
     "Miriam singing a lament", "Hannah refusing to eat", "A",
     "The voice was heard in Ramah, weeping and loud lamentation."),
    (T_THEME, "Hard", "In 1 Corinthians 15, Paul explains that what is sown in the ground is a perishable body, and what is raised is",
     "imperishable and glorious", "exactly the same body that died",
     "a spirit with no body at all", "a body subject to decay again", "A",
     "The seed dies; the harvest is glorious."),
    (T_QUOTE, "Medium", "'Forgetting what lies behind and straining forward to what lies ahead, I press on toward the goal.' Paul wrote these words in his letter to the",
     "Philippians", "Colossians",
     "Thessalonians", "Philemon", "A",
     "The runner keeps his eye on the prize."),
    (T_QUOTE, "Medium", "In the book of Revelation, the risen Christ describes himself as",
     "the Alpha and the Omega", "the Alpha and Delta",
     "the beginning without end", "the first of the seven", "A",
     "The first and last letters own the whole story."),
    (T_OT, "Hard", "During the reign of Hezekiah, the Assyrian king who mocked the God of Judah and whose army was destroyed by the angel of the Lord in a single night was",
     "Sennacherib", "Nebuchadnezzar",
     "Pharaoh Necho", "Shalmaneser the fifth", "A",
     "In the morning, the camp held only dead men."),
    (T_MIN, "Medium", "When a woman known as a sinner washed Jesus' feet with her tears, wiped them with her hair and anointed them with ointment in the house of Simon the Pharisee, Jesus declared that",
     "her many sins were forgiven, for she loved much", "she must first repay all she owed",
     "Simon had shown greater love", "her tears were unnecessary", "A",
     "Love answered where the Pharisee saw only fault."),
    (T_PAR, "Medium", "A woman who had suffered a flow of blood for twelve years came up behind Jesus in the crowd and touched the fringe of his garment, and",
     "her flow of blood stopped at once", "she fell into a fever",
     "the crowd rebuked her loudly", "Jesus sent her to the priests", "A",
     "'Your faith has made you well.'"),
    (T_THEME, "Medium", "James compares the tongue to a small rudder that steers a great ship, and to a small fire that sets a forest ablaze, in order to teach that",
     "the tongue, though small, can do great harm or great good", "ships are safer than horses",
     "speech should never be used at all", "big things are always better than small ones", "A",
     "A tiny helm turns a huge vessel."),
    (T_QUOTE, "Hard", "In the book of Revelation, John sees 'a new heaven and a new earth', and God declares that",
     "he will wipe away every tear, and death shall be no more", "the sea will cover the whole earth",
     "the old city will be rebuilt on the old site", "the nations will be scattered for ever", "A",
     "The former things have passed away."),
    (T_MOSES, "Medium", "When Moses asked God's name at the burning bush, to tell the people of Israel who had sent him, God answered",
     "'I AM WHO I AM'", "'I WILL BE WHO I CHOOSE'",
     "'I AM THE GOD OF ABRAHAM ONLY'", "'MY NAME IS HIDDEN'", "A",
     "The self-existing One needs no other name."),
    (T_MOSES, "Hard", "The law of Moses provided that every fiftieth year, liberty should be proclaimed throughout the land and every Israelite should return to his own property. That year was the",
     "year of Jubilee", "year of firstfruits",
     "year of atonement", "year of Passover", "A",
     "The trumpet sounded, and the land rested."),
    (T_OT, "Medium", "When two women both claimed the same living child, Solomon ordered that the child be divided in two with a sword. The true mother was revealed because she",
     "chose to give up the child", "clung to the baby's clothes",
     "wept louder than her rival", "offered the king a bribe", "A",
     "Real love would rather lose than see harm."),
    (T_MIN, "Medium", "When the Pharisees asked Jesus whether it was lawful to pay taxes to Caesar, he asked whose image was on the coin, and then said",
     "'Render to Caesar the things that are Caesar's'", "'Pay no tax at all to any foreign king'",
     "'Give all that you have to Caesar first'", "'The coin belongs wholly to the temple'", "A",
     "The image on the coin settles the coin's duty."),
    (T_PAR, "Easy", "At the tomb of his friend Lazarus, when Jesus saw Mary weeping, the shortest verse of the gospels records that",
     "Jesus wept", "Jesus slept",
     "Jesus smiled", "Jesus prayed", "A",
     "Two words carry the whole heart of the Lord."),
    (T_MIN, "Easy", "'Do not give dogs what is holy, and do not throw your pearls before pigs.' In this saying, the pearls stand for",
     "what is precious and holy", "money given to the poor at the gate",
     "jewellery worn by the disciples", "the harvest of the sea of Galilee", "A",
     "Some gifts are trampled by those who cannot value them."),
    (T_MIN, "Easy", "'Ask, and it will be given to you; seek, and you will find; knock, and it will be opened to you.' This promise teaches that",
     "persistent prayer is answered", "prayer must be made only once",
     "God's door is shut to all", "asking is forbidden to children", "A",
     "The door opens to the hand that keeps knocking."),
]

build_batch(
    S,
    "batch_231_waec_crs10.json",
    "231",
    "WAEC CRS round 10 (R47 top-up): Mary and Martha's good portion; "
    "anointing at Bethany; the two thieves; Jonathan and David's "
    "covenant; hidden treasure and pearl; the great supper; draught "
    "of fishes; the widow of Nain; the Word was God; Rachel weeping; "
    "1 Corinthians 15 resurrection body; press toward the goal; "
    "Alpha and Omega; Sennacherib; Simon the Pharisee's sinful woman; "
    "the issue of blood; James on the tongue; new heaven and new "
    "earth; I AM WHO I AM; Jubilee; Solomon's judgement; render to "
    "Caesar; Jesus wept; pearls before swine; ask, seek, knock. "
    "Scanned against the whole CRS pool (JAMB, WAEC and NECO stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
