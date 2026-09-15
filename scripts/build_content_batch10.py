"""Builds content/batch_010_english_round3.json — Use of English, round 3.

Follows the official UTME Use of English structure: comprehension passages (5 questions each),
cloze passages (10 numbered gaps each), sentence interpretation, synonyms/antonyms set inside
sentences, grammar/sentence completion, and oral forms (vowels, consonants, rhymes, word stress,
emphatic stress). Passages are original, Nigerian in setting, ~180-230 words.

Run:  python3 scripts/build_content_batch10.py
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_content_batch1 import _balance  # noqa: E402
from distractor_fixes import apply_fixes  # noqa: E402

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "content", "batch_010_english_round3.json")

# ---------------------------------------------------------------------------
# Comprehension passages: (key, title, text)
# ---------------------------------------------------------------------------
COMP_P = [
    ("C3", "The borehole at Umuahia Road",
     "When the borehole at the end of Umuahia Road finally broke down, nobody was surprised. For eleven years it had "
     "served four hundred households, coughing up water at dawn and dusk while the council's own scheme lay rusting "
     "behind a locked gate. What surprised people was what happened next. Within a week, a committee of women had "
     "collected two hundred naira from every compound, hired a technician from Aba and replaced the pump. The council "
     "chairman, arriving with a camera crew to commission the 'repaired' borehole, was politely told that his help was "
     "no longer required.\n\n"
     "The episode illustrates a pattern that development workers have observed across the country: communities are "
     "quickest to maintain what they have paid for themselves. Projects handed down from above, however generous, are "
     "treated as somebody else's property. When they fail, people wait for the giver to return. When a community's own "
     "money is at stake, the response is immediate.\n\n"
     "This does not mean that government should abandon its responsibilities. It means, rather, that the manner of "
     "giving matters as much as the gift. A borehole that a community has helped to plan, fund and manage is far "
     "more likely to be pumping water in ten years' time than one that simply appeared one morning, complete with "
     "a plaque bearing a politician's name."),
    ("C4", "Mr Bassey's mathematics class",
     "Mr Bassey never announced a test. He simply walked in, wrote a single problem on the board and sat down to read "
     "his newspaper. The first time this happened, the class panicked; by the third week, it had become a ritual. "
     "Students learnt to arrive early, to check their previous night's work, and — most unusually — to explain their "
     "reasoning to one another in the minutes before he arrived, because whoever was called to the board would have "
     "to defend every line.\n\n"
     "His methods were not universally admired. Parents complained that he set no homework in the conventional sense; "
     "the vice-principal noted that his lesson notes were never up to date. Yet when the results came, his classes "
     "outperformed every other in the zone, and had done so for nine consecutive years.\n\n"
     "Asked once to explain his approach, he shrugged. 'I don't teach them mathematics,' he said. 'I make them "
     "uncomfortable enough to teach themselves.' Behind the modesty lay a firm conviction: that understanding is not "
     "something a teacher can transfer like a parcel, but something a learner must build, often painfully, by "
     "getting things wrong in front of others and discovering why."),
    ("C5", "The market for second-hand clothes",
     "Every Thursday, bales of used clothing arrive at the Katangowa market from ports in Lagos and Cotonou. Traders "
     "call them okrika, after the Rivers State town through which the first shipments reportedly passed decades ago. "
     "A single bale, bought unopened for a fixed price, may contain a fortune or a loss: the trader does not know until "
     "the ties are cut whether the contents are designer jackets or shapeless rags.\n\n"
     "Critics argue that the trade has destroyed Nigeria's textile industry. In the 1980s the mills of Kaduna and Kano "
     "employed hundreds of thousands; today most stand silent. Cheap imported clothing, they say, made local cloth "
     "uncompetitive. Defenders of the trade reply that the mills were already failing from power shortages and "
     "smuggling, and that okrika now feeds more families than the mills ever did — the porters, sorters, menders, "
     "launderers and hawkers who form a chain from the bale to the buyer.\n\n"
     "Both sides may be right. What is beyond dispute is that a poor family can clothe its children decently for a "
     "fraction of the cost of new garments, and that a government which bans the trade without providing an "
     "alternative will punish the poorest twice: once as workers and again as consumers."),
    ("C6", "Grandmother and the mobile phone",
     "My grandmother refused to own a mobile phone until she was seventy-six. Telephones, she maintained, were for "
     "people who had something urgent to say and nobody nearby to say it to. She had neither problem. Her compound "
     "was never empty; her news travelled by the older networks of church, market and the women who came to plait "
     "her hair.\n\n"
     "What changed her mind was not persuasion but a funeral. Her sister died in Kaduna on a Tuesday; the letter "
     "announcing it reached her the following Monday, two days after the burial. She wept, not only for her sister "
     "but for the six days during which she had gone about her business, laughing and bargaining, while her sister "
     "lay in a mortuary eight hundred kilometres away.\n\n"
     "The phone my uncle bought her was the simplest available. She learnt to answer it within a week and to make "
     "calls within a month. She never sent a text message in her life. But she kept the phone under her pillow at "
     "night, charged and switched on, and when it rang after dark she would answer it before the second ring, with "
     "the voice of a woman who had once been late for a death."),
    ("C7", "Why the plastics ban stalled",
     "In January the state government announced, with considerable fanfare, that single-use plastic bags would be "
     "banned within six months. Environmental groups applauded. Market women shrugged. By July nothing had changed: "
     "the bags still fluttered from every stall, still blocked every drain, still burned in every heap of refuse.\n\n"
     "The failure was not one of intention but of preparation. No alternative had been made available at a price "
     "traders could afford; a paper bag cost five times as much as the plastic one it was meant to replace. The "
     "agency charged with enforcement had forty inspectors for a state of eight million people. And the two factories "
     "that produced the bags, employing three thousand workers between them, had not been consulted at all — a "
     "silence they answered with a court injunction.\n\n"
     "None of this was unforeseeable. Countries that have curbed plastic waste successfully did so gradually, "
     "beginning with a small levy, funding cheap alternatives, and bringing manufacturers into the process early "
     "enough to retool rather than resist. A ban is a headline; a transition is a plan. The state had produced the "
     "first and mistaken it for the second."),
    ("C8", "The apprentice",
     "Emeka was fourteen when his father handed him to Oga Cletus, a spare-parts dealer at Ladipo, with the words "
     "that every Igbo apprentice hears: 'He is your son now. Whatever he does, do to him.' For six years Emeka "
     "would not be paid. He would sweep the shop, carry goods, learn the names and prices of ten thousand parts, "
     "and, if he served faithfully, be 'settled' at the end with capital to open his own stall.\n\n"
     "Foreign economists who have studied the system call it the largest business incubator in the world, and they "
     "are not exaggerating. It transfers skills, credit and customers from one generation of traders to the next "
     "without banks, business schools or government agencies. Its weakness is the same as its strength: everything "
     "depends on the character of the master. A fair one produces a fair trader; a cruel one produces a young man "
     "who has learnt only that power is to be abused.\n\n"
     "Emeka was fortunate. At twenty he received a shop, a supplier's introduction and two hundred thousand naira. "
     "His first act as a trader was to travel home and ask his cousin's son whether he would like to learn a "
     "business."),
]

# (passage, difficulty, question, A, B, C, D, answer, explanation)
COMP = [
    ("C3", "Medium", "The women's committee told the council chairman that his help was no longer required because", "the borehole had been closed permanently", "they had already repaired it with their own money", "the council's scheme had started working", "the technician from Aba had refused his money", "B", "They had collected money, hired a technician and replaced the pump within a week, before the chairman arrived."),
    ("C3", "Medium", "The expression 'coughing up water' suggests that the borehole", "was poisoned", "produced water with difficulty", "made a lot of noise", "produced clean water", "B", "'Coughing up' pictures a struggling, unreliable supply."),
    ("C3", "Hard", "According to the passage, projects handed down from above fail to last mainly because", "they are poorly built", "communities see them as someone else's property", "politicians steal the money", "they are too expensive to repair", "B", "The second paragraph says such projects are 'treated as somebody else's property' and people wait for the giver to return."),
    ("C3", "Medium", "The writer's attitude to the council chairman can best be described as", "admiring", "gently mocking", "furious", "indifferent", "B", "The chairman arrives 'with a camera crew' to commission a borehole he did not repair, and the plaque remark ridicules such gestures without anger."),
    ("C3", "Medium", "The writer concludes that", "government should stop building boreholes", "how a gift is given matters as much as the gift", "communities should fund all their own projects", "politicians' names should not appear on plaques", "B", "The final paragraph states this directly and denies that government should abandon its duties."),

    ("C4", "Medium", "Mr Bassey read his newspaper during tests in order to", "show he did not care about the class", "avoid helping students and let them work independently", "keep up with current affairs", "annoy the vice-principal", "B", "His method rested on making students 'teach themselves'; the newspaper signalled that no help would come."),
    ("C4", "Medium", "The word 'ritual' as used in the passage means", "a religious ceremony", "a familiar, expected routine", "a form of punishment", "a secret practice", "B", "The surprise tests became a regular, predictable pattern the class prepared for."),
    ("C4", "Medium", "Students explained their work to one another before class because", "the teacher rewarded those who worked in teams", "whoever was called to the board had to defend every step", "they had no textbooks and had to share notes", "the teacher usually arrived very late", "B", "The passage links the habit to having to 'defend every line' at the board."),
    ("C4", "Hard", "'understanding is not something a teacher can transfer like a parcel' means that", "teachers should not send lesson notes by post", "knowledge cannot simply be handed over; learners must build it", "understanding is too heavy a load for one teacher to carry", "parcels sent within Nigeria are frequently unreliable", "B", "The simile contrasts passive receiving with active construction of understanding."),
    ("C4", "Medium", "Which of the following did the passage give as a criticism of Mr Bassey?", "his classes performed poorly", "his lesson notes were never up to date", "he was frequently absent", "he punished students physically", "B", "The vice-principal 'noted that his lesson notes were never up to date'; parents complained about homework."),

    ("C5", "Medium", "The name 'okrika' comes from", "a port in Cotonou", "a town in Rivers State", "a textile mill in Kaduna", "a market in Lagos", "B", "The passage says traders named the goods after the Rivers State town through which early shipments passed."),
    ("C5", "Medium", "Buying a bale unopened is compared to a gamble because", "the price of a bale changes every Thursday", "the trader cannot know its contents until it is opened", "customs officers may seize it at the port", "the bale may be stolen before it reaches the market", "B", "'A fortune or a loss ... the trader does not know until the ties are cut.'"),
    ("C5", "Medium", "Defenders of the trade argue that the textile mills collapsed mainly because of", "cheap imported clothing", "power shortages and smuggling", "poor management", "high wages", "B", "They say the mills 'were already failing from power shortages and smuggling'."),
    ("C5", "Hard", "The writer says a ban without an alternative would punish the poor 'twice' because they would", "pay more tax and lose their shops", "lose jobs in the trade and pay more for clothes", "be arrested and fined", "lose both okrika and the mills", "B", "'Once as workers and again as consumers' — jobs in the chain and cheap clothing."),
    ("C5", "Medium", "The writer's position on the debate is that", "the critics are completely wrong", "the defenders are completely wrong", "both sides have a point", "the government should ban the trade at once", "C", "'Both sides may be right' introduces the conclusion."),

    ("C6", "Medium", "Grandmother originally refused a phone because she", "could not afford to buy one for herself", "felt she had no urgent news and no shortage of company", "did not trust the uncle who offered to buy one", "preferred writing letters to her relations", "B", "Telephones were 'for people who had something urgent to say and nobody nearby' — she had 'neither problem'."),
    ("C6", "Medium", "The 'older networks' referred to in the passage are", "the old telephone cables in the village", "church, market and hair-plaiting women", "the postal services of the colonial era", "the local radio stations she listened to", "B", "The passage names these as the channels through which her news travelled."),
    ("C6", "Medium", "Grandmother wept partly because", "she had missed the burial by two days", "her uncle had bought her a cheap phone", "the letter had been lost", "she had quarrelled with her sister", "A", "The letter arrived 'two days after the burial', and she grieved the six days she spent unaware."),
    ("C6", "Hard", "The final sentence suggests that grandmother answered the phone quickly at night because she", "expected calls from her uncle", "feared missing important news again", "enjoyed late conversations", "wanted to stop the noise", "B", "'The voice of a woman who had once been late for a death' links her promptness to the funeral she missed."),
    ("C6", "Medium", "Which statement about grandmother is TRUE according to the passage?", "She learnt to text within a month.", "She never sent a text message.", "She bought the phone herself.", "She kept the phone switched off at night.", "B", "The passage says she never sent a text; she kept the phone charged and on under her pillow."),

    ("C7", "Medium", "The phrase 'with considerable fanfare' suggests that the announcement was made", "quietly", "with a great deal of publicity", "reluctantly", "by the courts", "B", "Fanfare means showy publicity."),
    ("C7", "Medium", "Which of the following was NOT given as a reason for the ban's failure?", "paper bags were too expensive", "there were too few inspectors", "manufacturers had not been consulted", "market women protested in the streets", "D", "Market women merely 'shrugged'; the three reasons listed are price, enforcement and the factories' injunction."),
    ("C7", "Medium", "The factories responded to the ban by", "closing down", "obtaining a court injunction", "producing paper bags", "sacking their workers", "B", "The 'silence they answered with a court injunction'."),
    ("C7", "Hard", "'A ban is a headline; a transition is a plan' means that", "newspapers oppose bans but support transitions", "announcing a ban is easy; managing change needs careful planning", "plans should be published as headlines in the newspapers", "bans work better than transitions in developing countries", "B", "The sentence contrasts publicity with the detailed preparation that successful countries carried out."),
    ("C7", "Medium", "The writer's tone in the passage is", "celebratory", "critical but constructive", "bitterly abusive", "uncertain", "B", "The writer criticises the failure but explains how it could have been done properly."),

    ("C8", "Medium", "The words 'He is your son now' indicate that the master", "adopts the boy legally as his own child", "takes full responsibility for the boy, including discipline", "must pay the boy a salary like a son", "will send the boy to school at his own expense", "B", "'Whatever he does, do to him' hands the father's authority to the master."),
    ("C8", "Medium", "In the passage, to be 'settled' means to be", "given a house in the city", "given capital to start one's own business", "paid a monthly salary at last", "sent back to one's village with gifts", "B", "The passage explains that a faithful apprentice is settled 'with capital to open his own stall'."),
    ("C8", "Medium", "Economists call the system 'the largest business incubator in the world' because it", "is run by the government at very low cost", "creates new traders by passing on skills, credit and customers", "operates in Ladipo, the largest market in Africa", "trains more engineers than the universities", "B", "The passage lists exactly these transfers, made 'without banks, business schools or government agencies'."),
    ("C8", "Hard", "According to the passage, the system's greatest weakness is that", "it lasts too long for most young men", "it depends entirely on the character of the master", "it pays no salary for six years", "it excludes girls from the trade", "B", "'Everything depends on the character of the master.'"),
    ("C8", "Medium", "Emeka's first act as a trader shows that he", "wanted revenge on Oga Cletus for the six years", "intended to continue the tradition that had helped him", "did not trust strangers with his new shop", "wished to leave Ladipo and return home", "B", "He went home to offer his cousin's son the same opportunity."),
]

# ---------------------------------------------------------------------------
# Cloze passages: gaps as [n]; questions (n, A, B, C, D, answer, explanation) with correct letter varied later
# ---------------------------------------------------------------------------
CLOZE_P = [
    ("Z3", "Cloze passage: The traffic warden",
     "Every morning at the Ojuelegba junction, a traffic warden named Bola takes up her [1] before the first buses "
     "arrive. Drivers who [2] her signals soon learn that she has an excellent memory for number plates. She does "
     "not shout; she simply [3] the offending vehicle to the side and asks, very politely, whether the driver is in "
     "a hurry to reach the hospital or the [4]. Most drivers laugh and apologise. A few [5] to argue, and these "
     "she deals with by writing slowly in a small notebook while the traffic behind them grows [6]. Nobody knows what "
     "she writes. Her colleagues say the notebook is [7]; she says it is her most effective weapon. Either way, "
     "the junction that was once [8] for its daily chaos now flows more smoothly than any other in the district, "
     "and commuters have [9] to greeting her by name. When she was transferred last year, a petition signed by four "
     "hundred drivers brought her back within a [10]."),
    ("Z4", "Cloze passage: Studying for the examination",
     "Preparing for a major examination is less about the number of hours spent than about how those hours are "
     "[1]. Many candidates read the same chapter several times and mistake familiarity for [2]. A better approach is "
     "to close the book and attempt to [3] what has just been read, because the effort of retrieval is what fixes "
     "knowledge in the memory. Past questions are [4] for this purpose, provided they are attempted under timed "
     "conditions and marked honestly. Sleep, too, is part of study: a brain that has been [5] of rest cannot store "
     "new material efficiently, [6] long it is kept awake. Candidates should therefore [7] the temptation to "
     "read through the night before the examination. Finally, it helps to study in a group occasionally, since "
     "explaining a topic to someone else quickly [8] the gaps in one's own understanding. Those who follow these "
     "principles usually find that they [9] less time than their friends and yet arrive in the examination hall "
     "calmer and better [10]."),
    ("Z5", "Cloze passage: The flood",
     "The rains came early that year and did not stop. By the third week of July the river had [1] its banks and "
     "was creeping across the farmlands towards the village. The elders, who had seen floods before, [2] the "
     "younger men to move the animals to higher ground at once, but many [3], convinced that the water would go "
     "down as it always had. It did not. On the night of the twenty-fourth the dam upstream was opened without "
     "[4], and by morning the lower half of the village was under two metres of water. Families [5] on rooftops "
     "waited for the canoes that came from neighbouring towns. Remarkably, no lives were [6], though hundreds of "
     "goats and the entire cassava harvest were swept away. When the waters finally [7], the village faced a "
     "choice: rebuild on the same ground or move to the ridge, a decision that divided households for months. In "
     "the end most families moved, [8] by the memory of that night. The old site is farmland again now, and the "
     "elders point to it when they [9] the young about the folly of ignoring [10] that has been earned the hard way."),
    ("Z6", "Cloze passage: A letter to the editor",
     "Sir, I write to [1] my disappointment at the state of the public library on Broad Street. When it opened in "
     "1978 it was the [2] of the town; today its roof leaks, half its shelves are empty and the reading room is "
     "[3] by pigeons. It is true that the council has [4] funds, but that is precisely why the library matters: "
     "for a child whose parents cannot afford books, it is the only door to a wider world. I therefore [5] the "
     "council to do three things. First, it should repair the roof before the rains, since every downpour destroys "
     "books that can never be [6]. Second, it should invite the town's professionals to donate books they no "
     "longer need, [7] the shelves at no cost. Third, it should employ one qualified librarian rather than the "
     "three [8] clerks who currently ignore the readers. None of this requires a large [9]. It requires only that "
     "those who were themselves educated in that building remember what they [10] it."),
    ("Z7", "Cloze passage: The football academy",
     "The academy sits on a patch of red earth [1] the expressway, with two goalposts, a borehole and a container "
     "that serves as office, store and changing room. Its founder, a former league player, started it with [2] "
     "more than a bag of balls and a conviction that talent is [3] distributed than opportunity. Boys train at "
     "six in the morning, before school, because he [4] on it: any boy who fails an examination is [5] from "
     "training until his grades improve. The rule has cost him several gifted players, but it has also [6] the "
     "trust of parents who once feared that football was a road to nowhere. In twelve years the academy has sent "
     "four players to clubs in Europe, and their transfer fees, a [7] of which returns to the academy by agreement, "
     "now pay for the coaches' salaries. Yet the founder measures success [8]. 'Four went to Europe,' he says. "
     "'Two hundred went to university. Which number [9] you think matters more?' Visitors [10] expect an answer "
     "soon discover that he does not intend to give one."),
    ("Z8", "Cloze passage: Mobile money in the village",
     "Until three years ago, sending money to my mother in the village meant [1] a bus driver to carry an envelope "
     "and hoping he was honest. The nearest bank was forty kilometres away, and the [2] of the journey often "
     "exceeded the sum she needed. Then a young man opened a mobile-money kiosk beside the market, and everything "
     "changed. Now I [3] the money from my phone in Lagos and she collects it ten minutes later, [4] a code that "
     "arrives by text message. The kiosk owner earns a small [5] on every transaction and has become, in effect, "
     "the village banker. Traders who once kept their savings under mattresses now deposit them with him; women "
     "who [6] had access to credit now borrow small sums against their savings history. The system is not without "
     "[7]. When the network fails, as it often does during storms, business stops. Fraudsters sometimes send false "
     "messages [8] to be from the operator. And the kiosk owner himself is a single point of failure: [9] he fall "
     "ill or leave, the village would be cut off again. Even so, few people would willingly [10] to the days of "
     "the envelope and the bus driver."),
]

CLOZE = {
    "Z3": [
        (1, "position", "posture", "residence", "seat", "A", "A warden takes up a position (place of duty) at a junction."),
        (2, "ignore", "neglect", "avoid", "refuse", "A", "Drivers 'ignore' (pay no attention to) her signals."),
        (3, "waves", "throws", "kicks", "pulls", "A", "A warden waves a vehicle to the side of the road."),
        (4, "mortuary", "bank", "office", "market", "A", "The joke pairs 'hospital' with its grim companion, the mortuary — where reckless speed leads."),
        (5, "attempt", "refuse", "manage", "decide", "A", "'A few attempt to argue' — try to dispute the matter."),
        (6, "longer", "louder", "slower", "faster", "A", "A queue of traffic grows longer while the driver is delayed."),
        (7, "empty", "stolen", "valuable", "official", "A", "The colleagues' claim contrasts with hers: nothing is written in it; the threat alone works."),
        (8, "notorious", "famous", "popular", "responsible", "A", "'Notorious' means well known for something bad — daily chaos."),
        (9, "taken", "grown", "started", "learnt", "A", "'Have taken to' means have formed the habit of."),
        (10, "month", "moment", "minute", "second", "A", "A petition producing a transfer reversal within a month is realistic; the others are too short."),
    ],
    "Z4": [
        (1, "used", "spent", "counted", "wasted", "A", "'How those hours are used' — the quality of use, not quantity."),
        (2, "understanding", "memory", "knowledge", "intelligence", "A", "Re-reading makes text familiar; the trap is mistaking that feeling for real understanding."),
        (3, "recall", "copy", "summarise", "revise", "A", "Closing the book and trying to recall is retrieval practice."),
        (4, "invaluable", "worthless", "unnecessary", "optional", "A", "'Invaluable' means extremely useful (not 'without value')."),
        (5, "deprived", "relieved", "robbed", "cured", "A", "'Deprived of rest' is the correct collocation."),
        (6, "however", "whatever", "whenever", "wherever", "A", "'However long it is kept awake' means no matter how long it stays awake."),
        (7, "resist", "accept", "consider", "remember", "A", "One resists a temptation."),
        (8, "exposes", "closes", "widens", "hides", "A", "Explaining to others 'exposes' (reveals) gaps in understanding."),
        (9, "spend", "waste", "lose", "save", "A", "They spend less time yet are better prepared — the sentence contrasts effort with outcome."),
        (10, "prepared", "dressed", "informed", "rested", "A", "'Better prepared' completes the contrast with 'calmer'."),
    ],
    "Z5": [
        (1, "burst", "broken", "crossed", "flooded", "A", "A river 'bursts its banks' is the standard expression."),
        (2, "urged", "forced", "allowed", "advised", "A", "The elders urged (strongly encouraged) the young men to act at once."),
        (3, "hesitated", "agreed", "hurried", "refused", "A", "They hesitated, 'convinced that the water would go down'."),
        (4, "warning", "reason", "delay", "permission", "A", "The dam was opened 'without warning', hence the sudden overnight flooding."),
        (5, "stranded", "sleeping", "standing", "trapped", "A", "'Stranded on rooftops' — unable to leave."),
        (6, "lost", "saved", "taken", "wasted", "A", "'No lives were lost' is the fixed expression."),
        (7, "receded", "returned", "dried", "stopped", "A", "Flood waters recede (go back)."),
        (8, "persuaded", "prevented", "frightened", "forced", "A", "'Persuaded by the memory' — the memory convinced them to move."),
        (9, "warn", "teach", "punish", "remind", "A", "The elders warn the young about the folly of ignoring hard-won wisdom."),
        (10, "wisdom", "money", "advice", "knowledge", "A", "'Wisdom that has been earned the hard way' — through bitter experience."),
    ],
    "Z6": [
        (1, "express", "explain", "announce", "declare", "A", "'I write to express my disappointment' is the standard letter-opening formula."),
        (2, "pride", "centre", "envy", "gift", "A", "'The pride of the town' — something the town was proud of."),
        (3, "occupied", "visited", "damaged", "attacked", "A", "The reading room is occupied (taken over) by pigeons."),
        (4, "limited", "wasted", "no", "adequate", "A", "'It is true that the council has limited funds, but...' concedes a point before arguing."),
        (5, "urge", "beg", "order", "advise", "A", "'I urge the council to do three things' — the formal verb of a letter to the editor."),
        (6, "replaced", "repaired", "returned", "read", "A", "Damaged books 'that can never be replaced'."),
        (7, "filling", "emptying", "building", "cleaning", "A", "Donated books would fill the shelves at no cost."),
        (8, "idle", "senior", "busy", "trained", "A", "'Three idle clerks who currently ignore the readers' — contrast with one qualified librarian."),
        (9, "budget", "building", "library", "committee", "A", "'None of this requires a large budget' — a large sum of money."),
        (10, "owe", "left", "gave", "built", "A", "They should remember what they owe the building that educated them."),
    ],
    "Z7": [
        (1, "beside", "besides", "above", "beneath", "A", "'Beside the expressway' — next to. 'Besides' means 'in addition to'."),
        (2, "little", "nothing", "much", "anything", "A", "'With little more than a bag of balls' — hardly anything more."),
        (3, "more evenly", "less widely", "more rarely", "less fairly", "A", "Talent is more evenly distributed than opportunity — the founder's conviction."),
        (4, "insists", "depends", "relies", "decides", "A", "'He insists on it' — demands it as a rule."),
        (5, "suspended", "expelled", "dismissed", "removed", "A", "'Suspended from training until his grades improve' — a temporary exclusion."),
        (6, "earned", "lost", "won", "kept", "A", "The rule has 'earned the trust of parents'."),
        (7, "percentage", "number", "quantity", "piece", "A", "A percentage of the transfer fees returns to the academy."),
        (8, "differently", "carefully", "quickly", "rarely", "A", "'Yet' signals contrast: he measures success differently from visitors."),
        (9, "do", "will", "did", "can", "A", "'Which number do you think matters more?' — present simple question."),
        (10, "who", "whom", "which", "whose", "A", "'Visitors who expect an answer' — subject relative pronoun."),
    ],
    "Z8": [
        (1, "begging", "paying", "asking", "trusting", "A", "'Begging a bus driver to carry an envelope' — pleading with him."),
        (2, "cost", "length", "time", "danger", "A", "The cost of the journey often exceeded the sum she needed."),
        (3, "send", "transfer", "post", "deposit", "A", "'I send the money from my phone' — the general verb; 'transfer' is possible but 'send ... from my phone' is the idiomatic pairing used in the passage's register."),
        (4, "using", "showing", "reading", "typing", "A", "She collects it 'using a code' that arrives by text."),
        (5, "commission", "salary", "profit", "interest", "A", "An agent earns a commission on each transaction."),
        (6, "never", "always", "rarely", "once", "A", "Women who 'never had access to credit' — contrast with 'now borrow'."),
        (7, "problems", "customers", "success", "costs", "A", "'The system is not without problems' — the standard litotes."),
        (8, "claiming", "pretending", "hoping", "appearing", "A", "'Messages claiming to be from the operator'."),
        (9, "should", "if", "when", "would", "A", "'Should he fall ill' — inverted conditional."),
        (10, "return", "go", "agree", "compare", "A", "'Return to the days of the envelope' — go back."),
    ],
}

# ---------------------------------------------------------------------------
# Sentence-based lexis and structure
# ---------------------------------------------------------------------------
SI_STEM = "Choose the option that best explains the information conveyed in the sentence: "
SI = [
    ("Kunle's excuses cut no ice with the principal.", "The principal was not persuaded by Kunle's excuses", "The principal punished Kunle for giving excuses", "Kunle gave the principal a cold reception", "Kunle refused to explain himself", "A", "'To cut no ice with someone' means to have no influence on them."),
    ("The new manager is a chip off the old block.", "The manager is very old", "The manager closely resembles his father in character", "The manager was promoted from the workshop", "The manager is stubborn and unreasonable", "B", "A 'chip off the old block' is a person very like one parent."),
    ("Ada would not hear of her daughter dropping out of school.", "Ada was deaf to her daughter's request", "Ada refused to allow her daughter to drop out", "Ada did not know her daughter had dropped out", "Ada's daughter did not tell her she had dropped out", "B", "'Would not hear of' = would not allow or consider."),
    ("The senator's promise turned out to be a pie in the sky.", "The senator kept his promise generously", "The promise was pleasant but impossible to achieve", "The senator promised to feed the people", "The promise was fulfilled late", "B", "'Pie in the sky' is a pleasant idea that will never happen."),
    ("Bimpe has a bone to pick with her landlord.", "Bimpe wants to eat with her landlord", "Bimpe has a complaint to raise with her landlord", "Bimpe owes her landlord money", "Bimpe and her landlord are good friends", "B", "'A bone to pick with someone' is a grievance to discuss."),
    ("The coach told the players to pull their socks up.", "The players were told to dress properly", "The players were told to improve their performance", "The players were told to stop playing", "The players were told to warm up", "B", "'Pull your socks up' means make an effort to improve."),
    ("For all his wealth, Chief Okonkwo is a very lonely man.", "Chief Okonkwo is lonely because he is wealthy", "Although he is wealthy, Chief Okonkwo is lonely", "Chief Okonkwo spends all his wealth on friends", "Chief Okonkwo's wealth has made him unpopular", "B", "'For all' here means 'in spite of'."),
    ("Hardly had the rain stopped when the traders returned to their stalls.", "The traders returned before the rain stopped", "The traders returned immediately after the rain stopped", "The traders barely returned because of the rain", "The rain hardly stopped, so the traders did not return", "B", "'Hardly ... when' expresses one event following another immediately."),
    ("The minister was economical with the truth.", "The minister spent little money", "The minister deliberately left out important facts", "The minister spoke briefly and honestly", "The minister told the whole truth", "B", "A polite way of saying someone was misleading by omission."),
    ("Ngozi's application fell through at the last minute.", "Ngozi submitted her application late", "Ngozi's application failed at the final stage", "Ngozi dropped her application form", "Ngozi's application was accepted late", "B", "'Fall through' means fail to be completed."),
    ("Uche could not make head or tail of the instructions.", "Uche did not know where the instructions began", "Uche could not understand the instructions at all", "Uche lost the first and last pages", "Uche refused to read the instructions", "B", "'Cannot make head or tail of' = cannot understand."),
    ("The candidate's speech was met with stony silence.", "The audience listened attentively", "The audience showed cold disapproval by saying nothing", "The audience threw stones at the candidate", "The audience was too tired to react", "B", "'Stony silence' is a hostile, unresponsive silence."),
    ("Musa passed the examination by the skin of his teeth.", "Musa passed easily", "Musa passed only narrowly", "Musa cheated in the examination", "Musa failed by one mark", "B", "'By the skin of one's teeth' = only just."),
    ("No sooner had the lights gone out than the generator came on.", "The generator came on before the lights went out", "The generator came on immediately after the lights went out", "The generator failed when the lights went out", "The lights went out because of the generator", "B", "'No sooner ... than' = immediately after."),
    ("The two brothers do not see eye to eye on the inheritance.", "The brothers cannot look at each other", "The brothers disagree about the inheritance", "The brothers have not seen the inheritance", "The brothers share the inheritance equally", "B", "'See eye to eye' = agree."),
]

SYN_STEM = "Choose the option nearest in meaning to the word in capitals: "
SYN = [
    ("The council's decision to demolish the market was widely CONDEMNED.", "criticised", "welcomed", "discussed", "ignored", "A", "To condemn is to express strong disapproval."),
    ("The old man gave a LUCID account of the accident.", "lengthy", "clear", "confused", "emotional", "B", "Lucid means clearly expressed and easy to understand."),
    ("The witness was RELUCTANT to name the attackers.", "eager", "unwilling", "unable", "forbidden", "B", "Reluctant means hesitant or unwilling."),
    ("The drug has a DETRIMENTAL effect on the liver.", "beneficial", "harmful", "mild", "temporary", "B", "Detrimental means causing harm."),
    ("His answers were so AMBIGUOUS that nobody knew what he meant.", "loud", "unclear", "brief", "rude", "B", "Ambiguous means open to more than one interpretation."),
    ("The committee will SCRUTINISE every receipt.", "destroy", "examine closely", "approve", "photocopy", "B", "To scrutinise is to inspect in detail."),
    ("The principal's decision was FINAL and could not be appealed.", "harsh", "conclusive", "sudden", "fair", "B", "Final here means conclusive, allowing no further argument."),
    ("The team showed remarkable RESILIENCE after losing the first match.", "weakness", "ability to recover", "anger", "confidence", "B", "Resilience is the capacity to recover quickly from difficulties."),
    ("The hall was filled to CAPACITY.", "the roof", "the fullest extent", "overflowing", "half", "B", "Capacity is the maximum amount a space can hold."),
    ("The governor's remarks INCENSED the youths.", "calmed", "angered", "surprised", "amused", "B", "To incense is to make very angry."),
    ("Her argument was so COGENT that the panel changed its mind.", "loud", "convincing", "long", "emotional", "B", "Cogent means clear, logical and convincing."),
    ("The doctor prescribed a PROLONGED course of treatment.", "expensive", "lengthy", "painful", "simple", "B", "Prolonged means continuing for a long time."),
    ("The company was accused of FLOUTING the safety regulations.", "obeying", "openly disregarding", "writing", "studying", "B", "To flout is to openly disobey."),
    ("The village was left DESOLATE after the flood.", "crowded", "deserted and bleak", "wealthy", "noisy", "B", "Desolate means empty, bleak and abandoned."),
    ("The principal spoke to the parents in a CONCILIATORY tone.", "angry", "peace-making", "commanding", "mocking", "B", "Conciliatory means intended to reduce anger and restore goodwill."),
]

ANT_STEM = "Choose the option opposite in meaning to the word in capitals: "
ANT = [
    ("The mechanic gave a very PESSIMISTIC assessment of the car.", "gloomy", "hopeful", "expensive", "careful", "B", "Pessimistic (expecting the worst) is opposed by optimistic/hopeful."),
    ("The new road has made the village more ACCESSIBLE.", "reachable", "cut off", "prosperous", "populated", "B", "Accessible (easy to reach) is the opposite of cut off / inaccessible."),
    ("The judge was known for his LENIENT sentences.", "severe", "gentle", "short", "fair", "A", "Lenient (merciful) is the opposite of severe/harsh."),
    ("The two partners were in complete HARMONY over the plan.", "agreement", "discord", "silence", "doubt", "B", "Harmony is the opposite of discord (disagreement)."),
    ("The committee's report was remarkably CONCISE.", "brief", "long-winded", "accurate", "confusing", "B", "Concise (short and to the point) is opposed by long-winded/verbose."),
    ("The senator gave a VAGUE answer to the question.", "unclear", "precise", "polite", "lengthy", "B", "Vague is the opposite of precise/specific."),
    ("The shop sells only GENUINE spare parts.", "authentic", "fake", "imported", "expensive", "B", "Genuine is the opposite of fake/counterfeit."),
    ("The soldiers showed great COURAGE under fire.", "bravery", "cowardice", "discipline", "patience", "B", "Courage is the opposite of cowardice."),
    ("The workers were praised for their DILIGENCE.", "hard work", "laziness", "honesty", "punctuality", "B", "Diligence (careful hard work) is opposed by laziness/negligence."),
    ("The price of tomatoes has been very STABLE this year.", "steady", "fluctuating", "high", "low", "B", "Stable is the opposite of fluctuating/unsteady."),
    ("The chairman gave a TERSE reply to the reporter.", "curt", "lengthy", "angry", "polite", "B", "Terse (brief and abrupt) is opposed by lengthy/wordy."),
    ("The witness's account was entirely CREDIBLE.", "believable", "unbelievable", "detailed", "brief", "B", "Credible is the opposite of incredible/unbelievable."),
    ("The land was FERTILE and produced two harvests a year.", "productive", "barren", "flat", "wet", "B", "Fertile is the opposite of barren/infertile."),
    ("It is COMPULSORY for all students to attend the assembly.", "obligatory", "optional", "difficult", "usual", "B", "Compulsory is the opposite of optional/voluntary."),
    ("The minister's speech was full of OPTIMISM about the economy.", "hope", "despair", "figures", "promises", "B", "Optimism is the opposite of pessimism/despair."),
]

GR_STEM = "Choose the option that best completes the gap: "
GR = [
    ("Neither the principal nor the teachers ____ aware of the change in the timetable.", "was", "were", "is", "has been", "B", "With 'neither ... nor', the verb agrees with the nearer subject ('teachers' — plural)."),
    ("The committee ____ divided in its opinion on the matter.", "are", "is", "were", "have been", "B", "Here the committee acts as one body ('its opinion'), so a singular verb is used."),
    ("If I ____ the minister, I would resign immediately.", "am", "was", "were", "be", "C", "The subjunctive 'were' is used for an unreal present condition."),
    ("Each of the boys ____ given a prize.", "were", "was", "have been", "are", "B", "'Each' is singular and takes a singular verb."),
    ("The news ____ so shocking that she fainted.", "were", "was", "are", "have been", "B", "'News' is an uncountable noun and takes a singular verb."),
    ("She insisted that he ____ the money before Friday.", "returns", "returned", "return", "will return", "C", "After 'insisted that', the bare subjunctive 'return' is used."),
    ("By the time the police arrived, the thieves ____.", "escaped", "had escaped", "have escaped", "were escaping", "B", "The past perfect shows the earlier of two past actions."),
    ("The man ____ car was stolen has reported to the police.", "who", "whom", "whose", "which", "C", "'Whose' shows possession (the man's car)."),
    ("Ngozi is ____ than any other girl in the class.", "more taller", "tallest", "taller", "the tallest", "C", "Comparative 'taller' is used with 'than'."),
    ("I would rather you ____ the truth now.", "tell", "told", "will tell", "have told", "B", "'Would rather + subject' takes the past tense for a present wish."),
    ("The students, as well as their teacher, ____ present at the ceremony.", "were", "was", "is", "has been", "A", "'As well as' does not change the number of the subject; 'students' is plural."),
    ("There ____ a lot of furniture in the room.", "are", "were", "is", "have been", "C", "'Furniture' is uncountable and takes a singular verb."),
    ("Scarcely had he sat down ____ the phone rang.", "than", "when", "then", "that", "B", "'Scarcely ... when' (not 'than', which follows 'no sooner')."),
    ("The teacher, together with the students, ____ to the museum.", "have gone", "has gone", "are going", "were going", "B", "'Together with' does not make the subject plural; 'teacher' is singular."),
    ("This is the house ____ my father was born.", "which", "where", "that", "whom", "B", "'Where' introduces a relative clause of place."),
    ("Adamu is one of the students who ____ selected for the competition.", "was", "were", "is", "has been", "B", "The relative clause refers to 'the students' (plural): 'who were selected'."),
    ("Everybody ____ to bring ____ own writing materials.", "is / their", "are / their", "is / his or her", "are / his", "C", "'Everybody' is singular: 'is ... his or her'."),
    ("The government has ____ a new policy on education.", "brought about", "brought up", "brought out", "brought down", "C", "To 'bring out' a policy is to publish or introduce it; 'bring up' is to raise a child or topic."),
    ("The driver was charged ____ dangerous driving.", "for", "with", "of", "on", "B", "One is 'charged with' an offence."),
    ("She is very good ____ mathematics but poor ____ English.", "in / in", "at / at", "at / in", "in / at", "B", "'Good at' and 'poor at' a subject."),
    ("The doctor advised him to abstain ____ alcohol.", "of", "for", "from", "on", "C", "'Abstain from' is the correct preposition."),
    ("I look forward to ____ from you soon.", "hear", "hearing", "have heard", "be hearing", "B", "'Look forward to' is followed by a noun or gerund."),
    ("____ the heavy rain, the match went ahead.", "Despite", "Although", "Because", "In spite", "A", "'Despite' takes a noun phrase; 'in spite' needs 'of'; 'although' needs a clause."),
    ("The twins are so alike that I cannot tell one from ____.", "another", "other", "the other", "each other", "C", "With two, 'one ... the other'."),
    ("The old man has lived in this village ____ over forty years.", "since", "for", "from", "during", "B", "'For' introduces a length of time; 'since' would need a starting point such as a year."),
]

STRESS_STEM = "In the following word, choose the option that has the correct stress pattern (the stressed syllable is written in capitals): "
STRESS = [
    ("geography", "GE-o-gra-phy", "ge-O-gra-phy", "ge-o-GRA-phy", "ge-o-gra-PHY", "B", "Words ending in '-graphy' are stressed on the syllable before it: ge-O-gra-phy."),
    ("electricity", "E-lec-tri-ci-ty", "e-LEC-tri-ci-ty", "e-lec-TRI-ci-ty", "e-lec-tri-CI-ty", "C", "Words ending in '-ity' are stressed on the syllable before it: e-lec-TRI-ci-ty."),
    ("photograph", "PHO-to-graph", "pho-TO-graph", "pho-to-GRAPH", "photo-GRAPH", "A", "PHO-to-graph — stress on the first syllable (compare pho-TO-gra-phy)."),
    ("understand", "UN-der-stand", "un-DER-stand", "un-der-STAND", "UN-DER-stand", "C", "un-der-STAND — final-syllable stress."),
    ("vegetable", "VE-ge-ta-ble", "ve-GE-ta-ble", "ve-ge-TA-ble", "ve-ge-ta-BLE", "A", "VE-ge-ta-ble is stressed on the first syllable (three syllables in speech: VEG-ta-ble)."),
    ("communication", "com-MU-ni-ca-tion", "com-mu-NI-ca-tion", "com-mu-ni-CA-tion", "com-mu-ni-ca-TION", "C", "Words ending in '-tion' are stressed on the syllable before it: com-mu-ni-CA-tion."),
    ("politician", "PO-li-ti-cian", "po-LI-ti-cian", "po-li-TI-cian", "po-li-ti-CIAN", "C", "Words ending in '-cian' are stressed on the syllable before it: po-li-TI-cian."),
    ("advertisement", "AD-ver-tise-ment", "ad-VER-tise-ment", "ad-ver-TISE-ment", "ad-ver-tise-MENT", "B", "British English: ad-VER-tise-ment."),
    ("The word 'record' as a VERB is stressed", "on the first syllable", "on the second syllable", "equally on both syllables", "on neither syllable", "B", "Noun RE-cord, verb re-CORD — a common noun/verb stress shift."),
    ("The word 'present' as a NOUN is stressed", "on the second syllable", "on the first syllable", "equally on both syllables", "on the last letter", "B", "Noun PRE-sent (a gift); verb pre-SENT."),
    ("interesting", "IN-te-res-ting", "in-TE-res-ting", "in-te-RES-ting", "in-te-res-TING", "A", "IN-te-res-ting — first-syllable stress."),
    ("thermometer", "THER-mo-me-ter", "ther-MO-me-ter", "ther-mo-ME-ter", "ther-mo-me-TER", "B", "Words ending in '-meter' (instruments) are stressed on the syllable before: ther-MO-me-ter."),
]

RHYME_STEM = "Choose the word that rhymes with the word in capitals: "
RHYME = [
    ("PEAR", "fear", "hair", "here", "peer", "B", "'Pear' is /peə/, rhyming with 'hair'; the others have /ɪə/."),
    ("WEIGHT", "height", "gate", "wit", "wheat", "B", "'Weight' is /weɪt/, rhyming with 'gate'."),
    ("TOMB", "bomb", "comb", "room", "thumb", "C", "'Tomb' is /tuːm/, rhyming with 'room'; the 'b' is silent."),
    ("DOUGH", "cough", "though", "rough", "tough", "B", "'Dough' is /dəʊ/, rhyming with 'though'; the others end in /f/."),
    ("QUAY", "day", "key", "way", "guy", "B", "'Quay' is pronounced /kiː/, rhyming with 'key'."),
    ("DEBT", "bet", "boat", "beat", "bit", "A", "'Debt' is /det/ (silent 'b'), rhyming with 'bet'."),
]

SOUND = [
    ("Choose the word that has the same vowel sound as the one represented by the letters in capitals: pOOl", "wool", "food", "book", "good", "B", "'Pool' has the long /uː/, as in 'food'; the others have short /ʊ/."),
    ("Choose the word that has the same vowel sound as the one represented by the letters in capitals: bIRd", "beard", "word", "bread", "bird", "B", "'Bird' has /ɜː/, as in 'word'."),
    ("Choose the word that has the same vowel sound as the one represented by the letters in capitals: cOAt", "cot", "caught", "note", "cat", "C", "'Coat' has /əʊ/, as in 'note'."),
    ("Choose the word that has the same vowel sound as the one represented by the letters in capitals: shIP", "sheep", "seat", "sit", "seen", "C", "'Ship' has short /ɪ/, as in 'sit'; the others have long /iː/."),
    ("Choose the word that has the same vowel sound as the one represented by the letters in capitals: cAUght", "cat", "cut", "court", "coat", "C", "'Caught' has /ɔː/, as in 'court'."),
    ("Choose the word that has the same consonant sound as the one represented by the letters in capitals: baTH", "bathe", "breathe", "cloth", "those", "C", "'Bath' ends in voiceless /θ/, as in 'cloth'; the others have voiced /ð/."),
    ("Choose the word that has the same consonant sound as the one represented by the letters in capitals: CHemist", "church", "chair", "school", "cheese", "C", "'Chemist' begins with /k/, as in 'school'; the others have /tʃ/."),
    ("Choose the word that has the same consonant sound as the one represented by the letters in capitals: naTIon", "nature", "station", "question", "native", "B", "'Nation' has /ʃ/ in '-tion', as in 'station'; 'nature' and 'question' have /tʃ/."),
    ("Choose the word that has the same consonant sound as the one represented by the letters in capitals: laUGH", "though", "cough", "through", "dough", "B", "'Laugh' ends in /f/, as in 'cough'; the others have a silent 'gh'."),
    ("Choose the word that has the same consonant sound as the one represented by the letters in capitals: Cell", "call", "city", "cup", "come", "B", "'Cell' begins with /s/, as in 'city'; the others have /k/."),
    ("Choose the word in which the letter 'p' is SILENT.", "pneumonia", "pencil", "public", "pepper", "A", "In 'pneumonia' the 'p' is not pronounced (/njuːˈməʊniə/)."),
    ("Choose the word in which the letter 'h' is SILENT.", "house", "honest", "horse", "happy", "B", "'Honest' is pronounced /ˈɒnɪst/ — the 'h' is silent."),
]

EMPH_STEM = "Choose the option to which the given sentence relates when the word in capitals is stressed: "
EMPH = [
    ("MY father bought the car last year.", "Did your father buy the car last year?", "Did your mother buy the car last year?", "Did his father buy the car last year?", "Did your father sell the car last year?", "C", "Stress on MY contrasts whose father it was."),
    ("The students WALKED to the stadium.", "Did the students drive to the stadium?", "Did the teachers walk to the stadium?", "Did the students walk to the school?", "Did the students walk to the stadium yesterday?", "A", "Stress on WALKED contrasts the manner of going."),
    ("Amaka bought THREE textbooks yesterday.", "Did Amaka buy three textbooks today?", "Did Amaka buy two textbooks yesterday?", "Did Amaka buy three notebooks yesterday?", "Did Ngozi buy three textbooks yesterday?", "B", "Stress on THREE contrasts the number."),
    ("The doctor examined the patient in the MORNING.", "Did the nurse examine the patient in the morning?", "Did the doctor examine the patient in the evening?", "Did the doctor examine the visitor in the morning?", "Did the doctor discharge the patient in the morning?", "B", "Stress on MORNING contrasts the time."),
    ("Tunde gave his SISTER the money.", "Did Tunde give his brother the money?", "Did Tunde lend his sister the money?", "Did Segun give his sister the money?", "Did Tunde give his sister the book?", "A", "Stress on SISTER contrasts the receiver."),
    ("The farmers planted MAIZE on the new land.", "Did the farmers plant maize on the old land?", "Did the farmers plant cassava on the new land?", "Did the traders plant maize on the new land?", "Did the farmers harvest maize on the new land?", "B", "Stress on MAIZE contrasts the crop."),
    ("We watched the match at HOME.", "Did you watch the match at the stadium?", "Did you watch the film at home?", "Did they watch the match at home?", "Did you play the match at home?", "A", "Stress on HOME contrasts the place."),
    ("The principal PRAISED the students for their behaviour.", "Did the teacher praise the students for their behaviour?", "Did the principal scold the students for their behaviour?", "Did the principal praise the teachers for their behaviour?", "Did the principal praise the students for their results?", "B", "Stress on PRAISED contrasts the action."),
]


def build():
    questions = []
    passages = [{"key": k, "title": t, "text": x} for k, t, x in COMP_P] + [{"key": k, "title": t, "text": x} for k, t, x in CLOZE_P]
    for key, diff, q, a, b, c, d, ans, exp in COMP:
        questions.append({"subject": "Use of English", "topic": "Comprehension", "passage": key, "difficulty": diff, "q": q, "A": a, "B": b, "C": c, "D": d, "answer": ans, "explanation": exp})
    titles = {k: t for k, t, _ in CLOZE_P}
    for key, rows in CLOZE.items():
        short = titles[key].split(": ", 1)[1]
        for n, a, b, c, d, ans, exp in rows:
            questions.append({"subject": "Use of English", "topic": "Cloze Tests", "passage": key, "difficulty": "Medium",
                              "q": f"In the cloze passage above ('{short}'), choose the most appropriate option to fill gap [{n}].",
                              "A": a, "B": b, "C": c, "D": d, "answer": ans, "explanation": exp})
    for stem, topic, rows in ((SI_STEM, "Lexis and Structure", SI), (SYN_STEM, "Synonyms", SYN), (ANT_STEM, "Antonyms", ANT), (GR_STEM, "Sentence Completion", GR), (EMPH_STEM, "Oral English", EMPH), (RHYME_STEM, "Oral English", RHYME)):
        for q, a, b, c, d, ans, exp in rows:
            questions.append({"subject": "Use of English", "topic": topic, "difficulty": "Medium", "q": stem + q, "A": a, "B": b, "C": c, "D": d, "answer": ans, "explanation": exp})
    for q, a, b, c, d, ans, exp in STRESS:
        text = q if q.startswith("The word") else STRESS_STEM + q
        questions.append({"subject": "Use of English", "topic": "Oral English", "difficulty": "Medium", "q": text, "A": a, "B": b, "C": c, "D": d, "answer": ans, "explanation": exp})
    for q, a, b, c, d, ans, exp in SOUND:
        questions.append({"subject": "Use of English", "topic": "Oral English", "difficulty": "Medium", "q": q, "A": a, "B": b, "C": c, "D": d, "answer": ans, "explanation": exp})

    # every cloze gap must exist in its passage
    ptext = {k: x for k, _, x in CLOZE_P}
    for key, rows in CLOZE.items():
        for n, *_ in rows:
            assert f"[{n}]" in ptext[key], (key, n)
    apply_fixes(questions)
    # cloze options are rotated deterministically so the key is spread over A-D
    cloze = [q for q in questions if q["topic"] == "Cloze Tests"]
    for i, q in enumerate(cloze):
        opts = [q[k] for k in "ABCD"]
        shift = (i * 3 + 1) % 4
        opts = opts[-shift:] + opts[:-shift] if shift else opts
        new_ans = "ABCD"[("ABCD".index(q["answer"]) + shift) % 4]
        for k, v in zip("ABCD", opts):
            q[k] = v
        q["answer"] = new_ans
    rest = [q for q in questions if q["topic"] != "Cloze Tests"]
    _balance(rest)
    questions = cloze + rest
    texts = [(x["q"], x.get("passage")) for x in questions]
    assert len(texts) == len(set(texts)), "duplicate question text"
    assert all(x["answer"] in "ABCD" and all(x[k] for k in "ABCD") for x in questions)
    for x in questions:
        assert len(x["explanation"]) >= 25, x["q"]
        if "stress pattern" not in x["q"]:
            assert len({x[k].strip().lower() for k in "ABCD"}) == 4, x["q"]
    batch = {
        "batch_id": "batch_010_english_round3",
        "exam_type": "JAMB",
        "note": "Use of English round 3: 6 comprehension passages, 6 cloze passages, sentence interpretation, synonyms/antonyms in sentences, grammar, oral forms.",
        "passages": passages,
        "questions": questions,
        "deactivate": [],
    }
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(batch, fh, ensure_ascii=False, indent=1)
    from collections import Counter
    print(f"wrote {OUT}: {len(questions)} questions, {len(passages)} passages")
    print("answer letters:", dict(Counter(x['answer'] for x in questions)))
    print("per topic:", dict(Counter(x['topic'] for x in questions)))


if __name__ == "__main__":
    build()
