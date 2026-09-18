"""Builds content/batch_034_english_round5.json — Use of English, round 5.

Twelve new comprehension passages (5 questions each), eight new cloze passages (10 gaps each),
plus fresh sentence-interpretation, synonym, antonym, grammar and oral-forms items.  None of the
idioms, test words, grammar points or oral items repeats an earlier English batch.

Run:  python3 scripts/build_content_batch34.py
"""
import json
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_content_batch1 import _balance  # noqa: E402
from batch_common import _near_duplicates  # noqa: E402

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_NAME = "batch_034_english_round5.json"
OUT = os.path.join(BASE, "content", OUT_NAME)

# --------------------------------------------------------------------------------------------
# Comprehension passages
# --------------------------------------------------------------------------------------------
COMP_P = [
    ("C15", "The generator next door",
     "For three years the family in the flat below ours ran a generator that sounded like a lorry idling in the "
     "corridor. It came on at dusk, when the public supply failed, and went off at midnight, when they went to bed. "
     "In between, we lived inside its noise. We raised our voices to talk, turned the television up until the "
     "neighbours on the other side complained, and learnt to sleep with pillows over our heads. The fumes came in "
     "through the kitchen window and settled on the curtains as a fine grey film.\n\n"
     "We complained, of course. The man downstairs was polite and immovable. He had children who needed light to "
     "read by, a wife who sold frozen fish and could not afford to let the freezer thaw, and a father-in-law on "
     "oxygen. Everything he said was true, and none of it made the noise quieter. In the end we did what everyone "
     "in the street had done: we bought a generator of our own, and added our roar to his.\n\n"
     "There are, by one estimate, more than twenty million small generators in Nigeria, and together they "
     "produce more electricity than the national grid supplies. Each is a private answer to a public failure. "
     "Nobody chose this arrangement; each household simply did the sensible thing, and the sum of twenty million "
     "sensible things is a country that cannot hear itself think."),
    ("C16", "In defence of the mother tongue",
     "A child who speaks Igbo at home arrives in Primary One and is taught to read in English, a language she has "
     "heard mainly on television. She must learn, at the same time, what a written word is and what the words mean. "
     "Her counterpart in a village school in Finland learns to read in Finnish, the language of her kitchen and her "
     "games, and meets English later, as a subject, when reading itself is no longer a mystery. It should surprise "
     "nobody which of the two reads more fluently at nine.\n\n"
     "The argument for teaching young children in their mother tongue is not sentimental. Fifty years of research, "
     "including a famous six-year experiment in Ife in the 1970s, show that children taught in their own language "
     "in the early years learn to read faster, understand mathematics better and, when they eventually switch, "
     "learn English better too. What they gain is not a language but the habit of understanding.\n\n"
     "The objections are practical rather than educational. Nigeria has more than five hundred languages, "
     "textbooks exist in only a handful, and many urban classrooms contain children from a dozen language groups. "
     "These are real difficulties. But they are reasons to begin carefully, not reasons to continue with a system "
     "in which a six-year-old is asked to climb two staircases at once."),
    ("C17", "The tailor of Sabon Gari",
     "Mallam Idris has sewn in the same shop in Sabon Gari for thirty-one years. The shop is a single room with a "
     "treadle machine, a mirror gone cloudy at the edges and a wall of brown-paper patterns, each labelled in "
     "pencil with a customer's name. He does not use a tape measure on regular customers; he looks at them, notes "
     "whether they have grown thicker or thinner since the last kaftan, and cuts. He is rarely wrong.\n\n"
     "Business is not what it was. The market across the road now sells ready-made clothes from Turkey and China "
     "at prices he cannot match, and the young men who once queued before Sallah for a new babban riga now buy "
     "something off a hanger. Idris does not complain about this; he is a courteous man and, besides, he "
     "understands it. What he regrets is something else. 'A garment that is made for you,' he says, 'knows you. It "
     "knows that your left shoulder is lower. It knows that you sit a great deal. A garment from a hanger knows "
     "nobody.'\n\n"
     "His son works in a bank in Kaduna and will not take over the shop. Idris has accepted this too. He has begun, "
     "in the slow afternoons, to teach a neighbour's boy who has shown an interest, and he cuts the boy's practice "
     "cloth from the paper patterns of customers who are long dead."),
    ("C18", "Why drivers ignore the red light",
     "Stand at any junction in Lagos at seven in the morning and count. In ten minutes you will see the red light "
     "run a dozen times, not by reckless boys on motorcycles but by sober men in company cars and mothers with "
     "children in the back seat. Ask them afterwards and they will not say that the light is unimportant. They will "
     "say that if they had stopped, the car behind would have hit them, or the car beside would have gone through "
     "and taken their place in the queue on the other side. They stop obeying the light because they believe that "
     "nobody else will.\n\n"
     "This is the heart of the matter. A traffic light is not a fence; it cannot physically hold a car back. It "
     "works only as a shared expectation, and an expectation shared by half the drivers is no expectation at all. "
     "Every driver who runs the light teaches the drivers around him that the light is optional, and each of them "
     "teaches a dozen more. The disorder spreads faster than any warden can chase it.\n\n"
     "The cure, then, is not a campaign of posters asking drivers to be patient. It is a short period in which the "
     "light is enforced so consistently, at a few junctions, that drivers come to expect that others will stop. "
     "Once that belief exists, it maintains itself, and the wardens can go elsewhere. Order in traffic, like most "
     "order, is a habit before it is a law."),
    ("C19", "The boy who read on the bus",
     "I noticed him because he was the only person on the bus who was not looking at a phone. He was perhaps "
     "fourteen, in a school uniform two sizes too large, and he was reading a paperback with its cover torn off, "
     "holding it close to his face because the light through the dirty windows was poor. When the bus lurched he "
     "did not look up. When the conductor shouted for fares he found his coins by touch. He turned a page as we "
     "passed the stadium, another at the roundabout, and by the time I got down at Ojota he had read, by my count, "
     "eleven pages in forty minutes of the worst traffic in the city.\n\n"
     "I have thought about him often since, mostly with envy. I was once that boy. I read under the desk in class, "
     "in the bath, by torchlight after the generator went off. Somewhere between then and now, reading became a "
     "thing I did in short bursts between notifications, and I lost the ability to be so far inside a book that a "
     "bus could lurch without my noticing.\n\n"
     "It is fashionable to say that young people no longer read. The boy on the bus is one piece of evidence "
     "against that claim, and I suspect there are many more. What has changed is not the young but the noise "
     "around them, and the boy had found, without anyone teaching him, the oldest defence against noise there is."),
    ("C20", "The cost of a wedding",
     "My cousin's wedding last December cost, by her father's reckoning, eleven million naira. There were two "
     "ceremonies and three outfits for the bride, a hall that seated eight hundred, a live band flown in from "
     "Lagos, and souvenirs - plastic buckets printed with the couple's faces - for every guest. Her father, a "
     "retired civil servant, sold a plot of land to pay for it. The couple began married life in a rented room, "
     "with a car loan and a debt to an uncle.\n\n"
     "Nobody involved thought this strange. In much of Nigeria a wedding is not a private celebration but a public "
     "statement, and the statement is addressed less to the couple than to the community: we are people of "
     "substance; we have not been shamed. The eight hundred guests were the point. A smaller wedding would have "
     "been read as poverty, or quarrel, or worse.\n\n"
     "I do not write this to mock my uncle, who loves his daughter and did what his neighbours would have done. I "
     "write it because the sum he spent would have bought the couple a two-bedroom flat in the same town, and "
     "because I suspect that most of the eight hundred, if they had been asked privately, would have preferred the "
     "couple to have the flat. Extravagance of this kind survives not because everyone wants it but because "
     "everyone believes that everyone else expects it."),
    ("C21", "Rain from the roof",
     "For six months of the year the sky over Calabar delivers, free of charge, more water than any household "
     "could use. It falls on roofs, runs into gutters, floods the streets and drains, unused, into the creeks. "
     "Then, for the other six months, the same households queue at boreholes and pay water vendors by the "
     "jerrycan. It is as if a man stood in a river in the wet season and died of thirst in the dry.\n\n"
     "Harvesting rainwater is not new technology. A roof, a gutter, a pipe and a tank are all that is required, and "
     "our grandparents kept clay pots under the eaves for exactly this purpose. A roof of a hundred square metres "
     "in Calabar can collect more than two hundred thousand litres in a year - enough, with a modest tank and a "
     "little care, to carry a family through the dry months. The water needs only to be kept covered against "
     "mosquitoes and boiled, or filtered, before drinking.\n\n"
     "Why, then, do so few houses do it? Partly because tanks cost money at the moment of building, when money is "
     "scarce, while the vendor's jerrycan costs money later, a little at a time. Partly because water that falls "
     "from the sky is not taken seriously; what is free is assumed to be worthless. And partly because no "
     "regulation requires it. A single clause in the building code - no roof without a tank - would do more for "
     "the city's water supply than another dozen boreholes."),
    ("C22", "The answer sheet",
     "The paper was folded into a square the size of a matchbox and passed to me under the desk during the "
     "Chemistry examination. I knew what it was without unfolding it. Kelechi, two rows in front, had a cousin who "
     "worked at a printing press, and for a week the hostel had talked of nothing else. I held it in my palm and "
     "did not open it, not because I was virtuous but because I was afraid; the invigilator that morning was Mr "
     "Ishola, who was said to be able to see through walls.\n\n"
     "I passed Chemistry with a B. Kelechi and four others were caught in the Physics paper the following day, when "
     "the same cousin's answers turned out to be for a different set of questions, and all five wrote the same "
     "wrong answers in the same order. They were expelled. Kelechi's father, who had sold a cow to pay the fees, "
     "came to the school in a borrowed suit and wept in the principal's office.\n\n"
     "I tell this story to my own students now, and I have learnt to tell it honestly. I did not refuse the paper; "
     "I merely failed to open it. The difference between Kelechi and me was not character but fear, and a school "
     "that relies on fear will produce, at best, students who cheat carefully. What I try to give them instead is "
     "the thing I did not have that morning: the certainty that I could pass on my own."),
    ("C23", "Forty kilometres to a doctor",
     "The nearest doctor to Kwakwa is forty kilometres away, on a road that becomes a river between June and "
     "September. The village has a health post, a two-room building with a nurse who visits on Tuesdays if her "
     "motorcycle is working, and a shelf of drugs that is full in January and empty by March. When a child "
     "convulses with fever at night, the family's choice is between a motorcycle ride in the dark with the child "
     "held between two adults, and a herbalist whose compound is at the end of the street.\n\n"
     "It is easy, from a city, to condemn the choice of the herbalist. It is harder when one has seen the road. The "
     "mothers of Kwakwa are not ignorant; they know what a hospital can do, and they take their children there "
     "when they can. What they lack is not belief in medicine but access to it, and a system that expects a woman "
     "to carry a convulsing child forty kilometres has no right to lecture her about superstition.\n\n"
     "The remedies are known and unglamorous. A community health worker who lives in the village and can give a "
     "first dose of anti-malarial at midnight; a drug supply that is refilled when it runs out rather than once a "
     "year; a road graded before the rains. None of these is a hospital, and none would make a headline. Together "
     "they would save more children in Kwakwa than a teaching hospital in the state capital ever will."),
    ("C24", "Ninety minutes on plastic chairs",
     "The viewing centre on our street is a shed of corrugated iron with sixty plastic chairs, two televisions and "
     "a generator that begins its shift ten minutes before kick-off. Admission is two hundred naira. On a Saturday "
     "evening when a Manchester club is playing, the chairs are full by six and the late-comers stand at the back, "
     "and the shed holds more concentrated emotion than any church in the district.\n\n"
     "I used to regard the viewing centre as a symptom: of unemployment, of a nation watching other people's "
     "leagues because it had neglected its own, of young men with nothing better to do. I still think some of this "
     "is true. But I have sat in the shed often enough now to see something else. The men who fill it work: they "
     "are mechanics, conductors, tailors and hawkers, and the two hundred naira is earned. What they buy for it is "
     "ninety minutes in which the rules are clear, the referee is (mostly) fair, effort is rewarded and the outcome "
     "is not decided in advance by whom you know. It is hard to think of another place in their week where this is "
     "so.\n\n"
     "The shed will empty at the final whistle and the men will go back to a city that is none of these things. "
     "But for ninety minutes they have lived, on plastic chairs, in a fairer world, and I have stopped believing "
     "that this is a waste of their time."),
    ("C25", "Grandfather's barn",
     "My grandfather's yam barn stood at the edge of the compound, a long frame of bamboo poles on which the tubers "
     "were tied in rows, largest at the bottom, so that a visitor could read a man's harvest at a glance. Every "
     "August the whole family gathered to tie the yams, and my grandfather walked the rows afterwards like a "
     "general inspecting troops. He knew, without counting, how many there were. He could tell, from the sound a "
     "tuber made when he tapped it, which would rot before Christmas.\n\n"
     "The barn is gone now. My uncle, who inherited the land, grows cassava, which needs no barn, sells for more "
     "and can be harvested when money is needed rather than when the season says. He is not wrong. Yam is a "
     "demanding crop: it wants a rich soil, a mound for each tuber, a stake for each vine and a year of the "
     "farmer's attention. Cassava will grow in tired ground and wait in it, uncomplaining, for two years.\n\n"
     "Yet something went with the barn that was not measured in naira. The tying of the yams was the one day in "
     "the year when every branch of the family was in the same place at the same time, and the barn was the "
     "family's account book, its pride and its insurance against hunger, standing in the open where anyone could "
     "see it. My uncle's cassava is sold in sacks and his money is in a bank, and neither can be walked along on an "
     "August afternoon."),
    ("C26", "Two wheels",
     "A bicycle costs less than a smartphone, needs no fuel, takes up a tenth of the road space of a car and is, "
     "over any distance under five kilometres in city traffic, faster than either a car or a bus. It produces no "
     "smoke and no noise, and the person riding it arrives having taken the exercise that the doctor keeps "
     "recommending. Given all this, the almost complete absence of bicycles from Nigerian cities requires "
     "explanation.\n\n"
     "Part of the explanation is danger. A cyclist on Ikorodu Road shares the lane with articulated lorries and "
     "drivers who regard anything slower than themselves as an obstacle, and nobody should be surprised that few "
     "try it. Part is climate; nobody wishes to arrive at the office soaked. But the largest part, I suspect, is "
     "status. In much of the country the bicycle is the vehicle of the village messenger and the water seller, and "
     "to be seen on one is to announce that one cannot afford anything better. A young accountant would rather sit "
     "for two hours in a bus than pedal for twenty minutes past his colleagues.\n\n"
     "Status is not permanent. Forty years ago the same was true in Amsterdam and Copenhagen, where the bicycle "
     "was for the poor until a generation decided otherwise, and today bankers cycle to work in suits. What "
     "changed there was not the weather but two things: lanes that made cycling safe, and a small number of "
     "visibly successful people who were seen to prefer it. The first is the government's job. The second is ours."),
]

COMP = [
    ("C15", "Medium", "The generator downstairs is compared to 'a lorry idling in the corridor' in order to stress",
     "its loudness and nearness", "the large size of the flat downstairs", "the terrible smell of its exhaust fumes", "the number of lorries that used the street",
     "A", "The comparison to a lorry engine running inside the building conveys the loudness and nearness of the noise."),
    ("C15", "Medium", "In the end the writer's family",
     "bought a generator of their own", "moved to a quieter flat in another street", "reported the neighbour to the police", "persuaded the neighbour to switch off at ten",
     "A", "'We bought a generator of our own, and added our roar to his.'"),
    ("C15", "Medium", "The neighbour is called 'polite and immovable' because he",
     "listened courteously but changed nothing", "promised to move the machine but never did", "was too heavy to move the generator himself", "refused to speak to the writer's family at all",
     "A", "He answered every complaint politely with reasons, yet nothing changed: 'none of it made the noise quieter'."),
    ("C15", "Medium", "The word 'thaw' as used in the passage means",
     "melt", "spoil and begin to smell", "become much colder", "be sold off cheaply",
     "A", "The frozen fish would thaw (defrost) if the freezer lost power."),
    ("C15", "Hard", "The final sentence suggests that the writer sees the generator problem as",
     "the sum of many reasonable private choices", "the fault of careless and selfish neighbours", "a problem that the government has largely solved", "too small a matter to deserve national attention",
     "A", "'Each household simply did the sensible thing, and the sum of twenty million sensible things is...' - individually reasonable acts add up to a public harm."),

    ("C16", "Medium", "The Finnish child learns to read more easily than the Igbo child mainly because she",
     "reads first in the language she speaks at home", "is taught by teachers with better training", "starts primary school at a much later age", "is never required to learn English at school",
     "A", "She reads first in Finnish, 'the language of her kitchen and her games', and meets English only later."),
    ("C16", "Medium", "The Ife experiment is mentioned in order to show that",
     "the argument rests on evidence, not sentiment", "Nigerian schools have always used the mother tongue", "the experiment failed and was quickly abandoned", "children in Ife speak better English than others",
     "A", "It is cited among 'fifty years of research' supporting the argument, which 'is not sentimental'."),
    ("C16", "Medium", "According to the writer, children taught first in their own language eventually",
     "learn English better as well", "refuse to learn English at all", "forget their mother tongue completely", "perform poorly in mathematics",
     "A", "'When they eventually switch, [they] learn English better too.'"),
    ("C16", "Hard", "The expression 'climb two staircases at once' refers to",
     "learning to read and learning English together", "attending two different schools in a single day", "studying both Igbo and Finnish in Primary One", "moving from primary to secondary school early",
     "A", "The six-year-old must learn 'what a written word is and what the words mean' at the same time - two tasks at once."),
    ("C16", "Medium", "The writer's attitude to the practical objections is that they",
     "are real but do not justify the present system", "prove that mother-tongue teaching is impossible", "are invented by enemies of Nigerian languages", "have already been solved by the new textbooks",
     "A", "'These are real difficulties. But they are reasons to begin carefully, not reasons to continue...'"),

    ("C17", "Medium", "Idris does not measure his regular customers because he",
     "can judge their size by looking at them", "lost his tape measure many years ago", "keeps their old measurements and never changes them", "sews only one size of kaftan for everybody",
     "A", "'He looks at them, notes whether they have grown thicker or thinner... and cuts. He is rarely wrong.'"),
    ("C17", "Medium", "Young men now buy ready-made clothes mainly because such clothes are",
     "cheaper than anything Idris can offer", "better sewn than Idris's garments", "sold at a discount by Idris's own son", "made from finer imported cloth",
     "A", "The market sells imported clothes 'at prices he cannot match'."),
    ("C17", "Hard", "Idris's remark that a garment from a hanger 'knows nobody' means that",
     "factory clothes are not shaped to any wearer", "ready-made clothes are always badly made", "nobody in Sabon Gari buys ready-made clothes", "his own shop has never used hangers",
     "A", "A made-to-measure garment 'knows' the wearer's lower shoulder and habits; a factory garment fits no one in particular."),
    ("C17", "Easy", "The word 'courteous' as used in the passage means",
     "polite", "talkative", "wealthy", "ambitious",
     "A", "Courteous means polite and considerate; it explains why he does not complain."),
    ("C17", "Medium", "The final paragraph suggests that Idris",
     "hopes his craft will outlive him through another boy", "intends to close the shop when his son marries", "is angry with his son for choosing the bank", "has stopped sewing and now only teaches",
     "A", "Having accepted that his son will not take over, he teaches a neighbour's boy who 'has shown an interest'."),

    ("C18", "Medium", "According to the passage, most of those who run red lights are",
     "ordinary, otherwise responsible drivers", "reckless young riders of motorcycles", "drivers who have never learnt the rules", "visitors who do not know the city's roads",
     "A", "'Not by reckless boys on motorcycles but by sober men in company cars and mothers with children.'"),
    ("C18", "Medium", "The reason drivers give for not stopping is that",
     "other drivers would not stop either", "the lights at most junctions are faulty", "they are in a hurry to get to work on time", "the wardens have told them to keep moving",
     "A", "'They stop obeying the light because they believe that nobody else will.'"),
    ("C18", "Hard", "The statement that 'a traffic light is not a fence' means that the light",
     "cannot stop a car unless drivers choose to obey it", "should be replaced by barriers at every junction", "is much smaller and cheaper than a fence would be", "is too weak to withstand a collision with a car",
     "A", "'It cannot physically hold a car back. It works only as a shared expectation.'"),
    ("C18", "Medium", "The writer believes that poster campaigns would be",
     "useless, since the problem is not impatience", "the quickest way to restore order at busy junctions", "useful only if they are displayed at night", "more effective than traffic wardens could ever be",
     "A", "'The cure, then, is not a campaign of posters asking drivers to be patient.'"),
    ("C18", "Hard", "'Order in traffic, like most order, is a habit before it is a law' suggests that",
     "rules work only when people expect others to keep them", "laws should be abolished in favour of unwritten habits", "traffic laws are too harsh to be obeyed by anyone", "habits matter more than order in a modern city",
     "A", "The passage argues that once drivers expect others to stop, the belief 'maintains itself' - the habit sustains the law."),

    ("C19", "Medium", "The boy attracted the writer's attention because he",
     "was reading rather than looking at a phone", "was wearing a uniform that was badly torn", "was shouting at the conductor about his fare", "was sitting directly beside the writer",
     "A", "'He was the only person on the bus who was not looking at a phone.'"),
    ("C19", "Medium", "The boy paid his fare",
     "without taking his eyes off his book", "only after the conductor had threatened him", "with a note the conductor could not change", "when the bus finally reached Ojota",
     "A", "'When the conductor shouted for fares he found his coins by touch.'"),
    ("C19", "Medium", "The writer's feeling towards the boy is mainly one of",
     "envy, because the writer can no longer read like that", "pity, because the boy could not afford a phone", "irritation, because the boy was blocking the light", "suspicion, because the book had no cover",
     "A", "'I have thought about him often since, mostly with envy. I was once that boy.'"),
    ("C19", "Medium", "The word 'lurched' as used in the passage means",
     "jerked suddenly", "stopped completely", "accelerated smoothly", "broke down entirely",
     "A", "A bus that lurches moves with a sudden unsteady jolt, as in traffic."),
    ("C19", "Hard", "In the last paragraph the writer suggests that",
     "the young still read, but amid far more distraction", "the boy was a rare exception who proves that the young do not read", "reading on buses should be encouraged by the government", "phones should be banned on public transport",
     "A", "'What has changed is not the young but the noise around them.'"),

    ("C20", "Easy", "The bride's father paid for the wedding by",
     "selling a piece of land", "borrowing from his bank", "spending his whole pension", "asking the guests to contribute",
     "A", "'Her father, a retired civil servant, sold a plot of land to pay for it.'"),
    ("C20", "Medium", "According to the writer, a large wedding in much of Nigeria is chiefly",
     "a display of the family's standing to the community", "a religious duty that the family cannot avoid", "a way of raising money for the newly married couple", "a private celebration for the couple's close relatives",
     "A", "'A wedding is not a private celebration but a public statement... addressed... to the community.'"),
    ("C20", "Medium", "A smaller wedding, the passage says, would have been interpreted as a sign of",
     "poverty or a quarrel", "the father's generosity", "the couple's good sense", "wise financial planning",
     "A", "'A smaller wedding would have been read as poverty, or quarrel, or worse.'"),
    ("C20", "Medium", "The word 'reckoning' as used in the passage means",
     "calculation", "complaint", "imagination", "punishment",
     "A", "'By her father's reckoning' - according to his calculation of the cost."),
    ("C20", "Hard", "The writer's main point in the final paragraph is that",
     "costly weddings survive on what people assume others expect", "his uncle was foolish and deserves to be criticised", "guests always prefer large weddings to small ones", "the couple should have bought a car instead of a flat",
     "A", "'Extravagance of this kind survives... because everyone believes that everyone else expects it.'"),

    ("C21", "Medium", "The comparison to a man who dies of thirst in a river is used to show that Calabar",
     "wastes in one season the water it lacks in the next", "is surrounded by rivers that are dangerous to cross", "has creeks that are drying up a little more every year", "buys river water from vendors at very high prices",
     "A", "Rain drains 'unused, into the creeks' for six months, then households pay for water for the other six."),
    ("C21", "Easy", "According to the passage, harvesting rainwater requires",
     "simple, well-known equipment", "expensive imported technology", "the services of government engineers", "a new borehole beside every house",
     "A", "'A roof, a gutter, a pipe and a tank are all that is required.'"),
    ("C21", "Medium", "One reason people do not install tanks is that",
     "a tank must be paid for when money is scarce", "rainwater cannot be made safe enough to drink", "tanks are forbidden by the current building code", "roofs in Calabar are too small to collect much",
     "A", "'Tanks cost money at the moment of building, when money is scarce.'"),
    ("C21", "Medium", "The word 'eaves' as used in the passage refers to",
     "the overhanging edges of a roof", "the gutters that run along the street", "the clay pots used for storing water", "the outside walls of a house",
     "A", "Pots were kept under the eaves - the overhanging edge of the roof - to catch water running off it."),
    ("C21", "Medium", "The writer's proposed solution is",
     "a building rule requiring a tank on every roof", "more boreholes in every street of the city", "lower prices for water sold by the vendors", "a campaign to teach people to boil their water",
     "A", "'A single clause in the building code - no roof without a tank.'"),

    ("C22", "Medium", "The writer did not open the folded paper because he",
     "was afraid of the invigilator", "was too honest to cheat", "already knew all the answers", "did not know what it contained",
     "A", "'Not because I was virtuous but because I was afraid; the invigilator... was Mr Ishola.'"),
    ("C22", "Medium", "Kelechi and the others were caught because",
     "they all wrote the same wrong answers in the same order", "Mr Ishola saw the paper being passed under the desk", "the writer reported them to the principal afterwards", "the printing press was raided by the police that week",
     "A", "The leaked answers were for a different paper, so 'all five wrote the same wrong answers in the same order'."),
    ("C22", "Medium", "Kelechi's father is described in order to show",
     "what the expulsion cost a poor family", "that he had encouraged his son to cheat", "how wealthy Kelechi's family really was", "that he was angry with the principal",
     "A", "He 'had sold a cow to pay the fees' and 'wept in the principal's office'."),
    ("C22", "Easy", "The word 'virtuous' as used in the passage means",
     "morally good", "very frightened", "clever", "popular",
     "A", "Virtuous means having high moral standards; the writer denies that this was his motive."),
    ("C22", "Hard", "The writer now believes that the best protection against cheating is",
     "students' confidence that they can pass unaided", "stricter invigilators of the kind Mr Ishola was", "harsher punishments such as immediate expulsion", "searching every student before every examination",
     "A", "'What I try to give them instead is... the certainty that I could pass on my own.'"),

    ("C23", "Medium", "The nurse at the health post",
     "comes once a week, and not always then", "lives permanently in the village of Kwakwa", "works only during the months of the rainy season", "is also the herbalist at the end of the street",
     "A", "'A nurse who visits on Tuesdays if her motorcycle is working.'"),
    ("C23", "Medium", "The writer's attitude to families who consult the herbalist is",
     "sympathetic, since they have little real choice", "scornful, because they are superstitious and ignorant", "indifferent to their situation and their children", "admiring, because herbal medicine works better",
     "A", "'It is harder [to condemn] when one has seen the road... What they lack is not belief in medicine but access to it.'"),
    ("C23", "Medium", "The drug shelf is described as 'full in January and empty by March' to show that",
     "supplies are not replaced during the year", "the villagers steal the drugs from the health post", "nobody in the village falls ill after March", "the nurse sells the drugs in the town",
     "A", "The writer later asks for 'a drug supply that is refilled when it runs out rather than once a year'."),
    ("C23", "Medium", "The word 'unglamorous' as used in the passage means",
     "unexciting", "very costly", "dangerous", "impossible",
     "A", "The remedies are plain and unexciting - 'none would make a headline'."),
    ("C23", "Hard", "The writer argues that a teaching hospital in the state capital would",
     "save fewer lives in Kwakwa than simple local measures", "solve the problems of the village completely", "be cheaper than employing a community health worker", "be built and equipped within a single year",
     "A", "'Together they would save more children in Kwakwa than a teaching hospital in the state capital ever will.'"),

    ("C24", "Medium", "The viewing centre is compared to a church in order to emphasise",
     "the intensity of feeling inside it", "the fact that it opens on Sunday evenings", "the quiet behaviour of the audience", "the great size of the building",
     "A", "'The shed holds more concentrated emotion than any church in the district.'"),
    ("C24", "Medium", "The writer once regarded the viewing centre as",
     "a symptom of idleness and neglected local football", "a good business investment for its owner", "a place of worship for football supporters", "a training school for young footballers",
     "A", "'A symptom: of unemployment, of a nation watching other people's leagues because it had neglected its own.'"),
    ("C24", "Medium", "The writer's opinion changed after he",
     "sat in the shed and watched the men there", "started supporting a Manchester club himself", "learnt that admission to the shed was free", "was employed to sell tickets at the viewing centre",
     "A", "'I have sat in the shed often enough now to see something else.'"),
    ("C24", "Hard", "What the men 'buy' with their two hundred naira, according to the writer, is",
     "ninety minutes in a world where fairness rules", "a chance to meet influential people from the district", "training for a professional career in football", "a cheap meal and a drink during the match",
     "A", "'Ninety minutes in which the rules are clear, the referee is (mostly) fair, effort is rewarded...'"),
    ("C24", "Hard", "The phrase 'a city that is none of these things' implies that the city is",
     "unfair, and run on whom you know", "too small to have a football league of its own", "quiet and orderly compared with the shed", "always dark at night because of power cuts",
     "A", "The city lacks what the match offers: clear rules, fairness, reward for effort, outcomes not decided by 'whom you know'."),

    ("C25", "Medium", "The yams were tied with the largest at the bottom so that",
     "the harvest could be judged at a glance", "the small ones at the top would not rot", "the family could eat the big ones first", "the bamboo frame would not fall over",
     "A", "'So that a visitor could read a man's harvest at a glance.'"),
    ("C25", "Medium", "The grandfather is compared to 'a general inspecting troops' to show",
     "his proud, careful examination of the rows", "that he had once been a soldier in the army", "that the yams were arranged in rows for battle", "that he punished any family member who was slow",
     "A", "The simile pictures him walking the rows with authority and attention, checking every tuber."),
    ("C25", "Medium", "The uncle prefers cassava mainly because it",
     "is less demanding and more profitable", "tastes much better than yam", "was his own father's favourite crop", "needs a larger barn than yam does",
     "A", "Cassava 'needs no barn, sells for more' and grows 'in tired ground', while yam 'wants... a year of the farmer's attention'."),
    ("C25", "Medium", "The word 'uncomplaining' as used in the passage suggests that cassava",
     "tolerates poor conditions", "is a very difficult crop to grow", "makes no sound when it is harvested", "is left in the ground and never harvested",
     "A", "Cassava 'will grow in tired ground and wait in it, uncomplaining' - it endures neglect."),
    ("C25", "Hard", "The writer's final point is that the barn had a value that was",
     "social and emotional, not merely financial", "recorded carefully in the family's account book", "greater than the value of the land it stood on", "purely financial, like the uncle's cassava",
     "A", "'Something went with the barn that was not measured in naira' - the family gathering, pride and visible security."),

    ("C26", "Easy", "According to the first paragraph, over short distances in city traffic a bicycle is",
     "faster than a car or a bus", "slower but cheaper than a bus", "exactly as fast as a car", "the most expensive of the three options",
     "A", "'Over any distance under five kilometres in city traffic, faster than either a car or a bus.'"),
    ("C26", "Medium", "The writer thinks the most important reason Nigerians avoid bicycles is",
     "the fear of appearing poor", "the danger from lorries on the roads", "the heat and the heavy rain", "the poor quality of the bicycles sold",
     "A", "'But the largest part, I suspect, is status... to be seen on one is to announce that one cannot afford anything better.'"),
    ("C26", "Medium", "The example of Amsterdam and Copenhagen is used to show that",
     "attitudes to cycling can change in a generation", "cycling has always been popular in European cities", "European cities enjoy far better weather than Lagos", "bankers in Europe are poorer than bankers in Nigeria",
     "A", "'Forty years ago the same was true... until a generation decided otherwise.'"),
    ("C26", "Medium", "The expression 'articulated lorries' as used in the passage refers to",
     "large lorries built in two jointed sections", "lorries that make a very loud noise", "lorries that carry spoken announcements", "small delivery vans used by traders",
     "A", "An articulated lorry has a cab and a trailer joined by a pivot; the point is their size and danger to cyclists."),
    ("C26", "Hard", "In the last two sentences the writer suggests that",
     "both government and citizens have a part to play", "only the government can change anything about it", "the weather must change before people will cycle", "the problem cannot be solved in Nigerian cities",
     "A", "Safe lanes are 'the government's job'; being seen to prefer the bicycle 'is ours'."),
]

# --------------------------------------------------------------------------------------------
# Cloze passages (gaps written as [n]; all keys written as "A" here and rotated by build())
# --------------------------------------------------------------------------------------------
CLOZE_P = [
    ("Z13", "Cloze passage: The village well",
     "The well at the centre of Umuaka is older than anyone in the village can [1]. It was dug, the elders say, by "
     "their great-grandfathers, and for a hundred years it [2] the whole community with water. Every morning before "
     "sunrise the women gathered around it, lowering their buckets on long ropes and [3] them up hand over hand. The "
     "well was more than a source of water; it was where news was [4], marriages were arranged and quarrels were "
     "settled. Three years ago a borehole was sunk beside the school, and the crowd at the well began to [5]. The "
     "young women preferred the tap, which was quicker and did not [6] their arms. Only a few old women still make "
     "the journey to the well each morning, [7] that borehole water 'has no taste'. Last month the council announced "
     "that the well would be [8] with concrete because a child had nearly fallen into it. The elders protested, but "
     "the decision had been [9]. Next week the men will arrive with their cement, and the place where the village "
     "once gathered will become a [10] slab that nobody visits."),
    ("Z14", "Cloze passage: The new bus terminal",
     "The new bus terminal at Oshodi was [1] with great ceremony by the governor, who cut a ribbon and [2] the crowd "
     "that the days of chaos were over. For the first month it seemed that he was right. Buses left from [3] bays, "
     "passengers queued under shelters, and the touts, [4] had ruled the old motor park, were nowhere to be seen. "
     "Then, one by one, the old habits [5]. A driver who was tired of waiting his turn began loading at the gate; a "
     "tout appeared to help him, [6] a small fee; passengers, seeing a bus that was leaving at once, [7] the queue "
     "and ran to it. Within six months the terminal was as [8] as the park it had replaced, and the shelters stood "
     "empty while the crowd fought at the gate. The lesson is not that the terminal was a bad idea. It is that a "
     "building cannot [9] behaviour by itself; the rules must be enforced every day until they become habit, and "
     "the day enforcement [10], the old disorder returns."),
    ("Z15", "Cloze passage: A visit to the dentist",
     "For two weeks Chidi had [1] the pain in his back tooth, chewing on the other side of his mouth and [2] cold "
     "drinks. When at last a night came in which he could not sleep, his mother marched him to the dental clinic on "
     "Aba Road. The waiting room smelt of [3] and was full of people holding their jaws. When his name was called, "
     "Chidi sat in the big chair and the dentist, a cheerful woman in a green gown, tilted it [4] until he was "
     "almost lying down. She [5] the tooth with a small mirror and a pointed instrument, tapping it gently and "
     "asking whether it hurt. It did. The tooth, she said, was badly [6]; the sugar from years of sweets and soft "
     "drinks had eaten a hole through the enamel and reached the nerve. She could [7] it, but Chidi would have to "
     "change his habits or the next tooth would go the same way. The injection stung, and the drilling was loud, "
     "but after twenty minutes the pain that had [8] him for a fortnight was gone. On the way home his mother bought "
     "him a toothbrush and a tube of [9], and Chidi, who had expected a lecture, was surprised when she said only "
     "that she was [10] of him for sitting still."),
    ("Z16", "Cloze passage: The school farm",
     "Every Wednesday afternoon the students of Government Secondary School, Bida, [1] their books for hoes and "
     "cutlasses and walk to the school farm behind the football field. The farm was the idea of the agricultural "
     "science teacher, Mr Ndagi, who [2] that a subject taught only from a textbook was a subject half learnt. He "
     "divided the two hectares into plots and [3] one to each class, with a prize at the end of the year for the "
     "plot with the best [4]. The first season was a disaster. The rains came late, the maize was planted too [5] "
     "together, and goats from the neighbouring village ate what the drought had spared. Mr Ndagi refused to be "
     "[6]. The following year the students built a fence, planted at the [7] spacing, and dug a shallow well for "
     "the dry weeks. The harvest was so good that the school kitchen bought the maize and the surplus was sold at "
     "the market, [8] the students to buy a second wheelbarrow. Today the farm produces vegetables, groundnuts and "
     "a small [9] of cassava, and students who once regarded farming as punishment now compete [10] to be chosen "
     "for the farm committee."),
    ("Z17", "Cloze passage: The night the lights went out",
     "The power [1] came at eight o'clock, just as the final of the competition was about to start. A groan went up "
     "from every house on the street, [2] by the coughing of generators being pulled into life. Ours refused to "
     "start. My father pulled the cord until he was [3] of breath, checked the fuel, cleaned the plug and pulled "
     "again, while my brother stood beside him offering advice that was not [4]. In the end my father gave up and "
     "lit a kerosene lamp, and the family sat in the parlour in a circle of yellow light, [5] the roar of the match "
     "from the neighbours' television. It was my grandmother who [6] the silence. She began to tell a story about a "
     "tortoise and a drum, one we had all heard before, and to our surprise we listened as [7] as if it were new. By "
     "the time she finished, the match had ended and the lights had come back, but nobody [8] to switch on the "
     "television. My brother asked for another story. It occurred to me later that the power cut had [9] us "
     "something we had lost without noticing: an evening in which the whole family faced one another [10] of a "
     "screen."),
    ("Z18", "Cloze passage: Learning to swim",
     "I was nineteen before I learnt to swim, and I learnt for the worst of reasons: [1]. My friends had planned a "
     "trip to the beach at Tarkwa Bay, and I could not [2] to be the one who sat on the sand guarding the bags. So "
     "for three weeks I went every evening to the public pool at the stadium, where a retired soldier called Baba "
     "Segun taught children for a small fee and adults, he said, for the [3] of it. The first lesson was "
     "humiliating. He made me stand in water that reached my chest and put my face in it, and I came up [4] and "
     "spitting after two seconds. 'The water is not your enemy,' he said. 'You are fighting it, so it fights you.' "
     "He taught me to float first, lying on my back and [5] my body to go loose until the water held me up. Then "
     "came the legs, then the arms, then, on the ninth evening, three metres of something that could [6] be called "
     "swimming. By the end of the third week I could cross the pool twice without [7]. At Tarkwa Bay I did not go "
     "far out; the waves were nothing like the [8] water of the pool. But I went in, and when my friends dared one "
     "another to swim to the rock, I went with them, [9] a little, and came back on my own. Baba Segun had been "
     "right: the sea did not want to drown me. It only wanted me to stop [10]."),
    ("Z19", "Cloze passage: The compound election",
     "Our compound has twelve flats and, for as long as I have lived there, one chairman: Mr Bankole, a retired "
     "customs officer who [1] the position in 2009 when nobody else wanted it. He collects the money for the "
     "security man and the [2] of the borehole, settles quarrels about parking, and posts notices in capital "
     "letters about the [3] of rubbish. Last month, for the first time, somebody stood against him. Mrs Adeyemi in "
     "Flat 7, a lawyer, argued that fifteen years was long enough for anybody and that the accounts had not been "
     "[4] since 2018. Mr Bankole was offended. He had, he said, given his time [5] and been paid in complaints. The "
     "campaign was short and surprisingly [6]. Mrs Adeyemi promised monthly statements and a WhatsApp group; Mr "
     "Bankole reminded everyone who had [7] the borehole when it broke down at Christmas. On the night of the vote "
     "all twelve flats were [8], which had never happened for any other meeting. Mrs Adeyemi won by seven votes to "
     "five. Mr Bankole shook her hand stiffly and went upstairs, and the next morning a notice appeared in capital "
     "letters, [9] the new chairman well and reminding residents that the security man's salary was [10] on "
     "Friday."),
    ("Z20", "Cloze passage: The bookshop on Broad Street",
     "Bello's Bookshop on Broad Street has [1] three recessions, two fires and the arrival of the internet, and its "
     "owner, now seventy-four, sees no reason why it should not survive him. The shop is narrow and deep, and books "
     "are [2] from floor to ceiling in an order that only Mr Bello understands. Ask for a title and he will [3] for "
     "a moment, climb a ladder and come down with it, usually with a second book you did not ask for but will "
     "probably [4]. He does not sell textbooks, which he regards as a [5] trade for people in a hurry, and he does "
     "not sell online, which he regards as no trade at all. What he sells, he says, is [6]: the chance to walk in "
     "wanting one thing and leave with another. His customers are fewer than they were, but they are [7]; some have "
     "been coming for forty years and now bring their grandchildren. When the landlord raised the rent last year, "
     "three of them [8] quietly to pay the difference. Mr Bello found out, refused, and then, after a night's [9], "
     "accepted on condition that the money be recorded as loans. 'A bookshop,' he told them, 'should owe its "
     "customers. It [10] them honest.'"),
]

CLOZE = {
    "Z13": [
        (1, "remember", "count", "believe", "forget", "A", "'Older than anyone can remember' is the natural expression for great age."),
        (2, "supplied", "denied", "sold", "charged", "A", "The well 'supplied the whole community with water' - supply somebody with something."),
        (3, "hauling", "throwing", "pushing", "filling", "A", "Buckets on long ropes are hauled (pulled) up 'hand over hand'."),
        (4, "exchanged", "concealed", "purchased", "invented", "A", "The well was a meeting place where news was exchanged."),
        (5, "thin", "grow", "gather", "shout", "A", "After the borehole arrived, the crowd began to thin (become smaller)."),
        (6, "tire", "wash", "cool", "fill", "A", "The tap was quicker and did not tire their arms, unlike hauling buckets."),
        (7, "insisting", "denying", "admitting", "forgetting", "A", "The old women keep going to the well, insisting that borehole water 'has no taste'."),
        (8, "sealed", "painted", "decorated", "widened", "A", "A dangerous well is sealed with concrete so that nobody can fall in."),
        (9, "taken", "refused", "forgotten", "postponed", "A", "'The decision had been taken' - the protest came too late."),
        (10, "bare", "busy", "wooden", "wet", "A", "A sealed well becomes a bare concrete slab 'that nobody visits'."),
    ],
    "Z14": [
        (1, "commissioned", "demolished", "condemned", "reconstructed", "A", "A new public building is commissioned (formally opened) by the governor."),
        (2, "assured", "warned", "begged", "asked", "A", "He 'assured the crowd that the days of chaos were over' - a confident promise."),
        (3, "numbered", "crowded", "deserted", "shuttered", "A", "In an orderly terminal buses leave from numbered bays."),
        (4, "who", "whom", "which", "whose", "A", "'The touts, who had ruled the old motor park' - 'who' is the subject of 'had ruled'."),
        (5, "returned", "disappeared", "improved", "ended", "A", "'One by one, the old habits returned' introduces the slide back into disorder."),
        (6, "for", "with", "from", "against", "A", "The tout helped 'for a small fee' - in return for payment."),
        (7, "abandoned", "lengthened", "defended", "respected", "A", "Passengers left the orderly queue for a bus that was leaving at once."),
        (8, "chaotic", "orderly", "clean", "quiet", "A", "The terminal became 'as chaotic as the park it had replaced'."),
        (9, "change", "build", "lose", "copy", "A", "'A building cannot change behaviour by itself' - the rules must be enforced."),
        (10, "stops", "starts", "continues", "succeeds", "A", "'The day enforcement stops, the old disorder returns.'"),
    ],
    "Z15": [
        (1, "endured", "enjoyed", "caused", "cured", "A", "He 'endured the pain' for two weeks - put up with it."),
        (2, "avoiding", "buying", "pouring", "demanding", "A", "A person with toothache avoids cold drinks, which make the pain worse."),
        (3, "antiseptic", "kerosene", "fried food", "wet paint", "A", "A dental clinic smells of antiseptic."),
        (4, "backwards", "forwards", "sideways", "upwards", "A", "The dentist's chair is tilted backwards 'until he was almost lying down'."),
        (5, "examined", "removed", "cleaned", "polished", "A", "She examined the tooth with a mirror and a probe before deciding what to do."),
        (6, "decayed", "chipped", "loose", "stained", "A", "Sugar had 'eaten a hole through the enamel' - the tooth was decayed."),
        (7, "save", "sell", "hide", "grow", "A", "The dentist could save the tooth by filling it."),
        (8, "tormented", "comforted", "protected", "surprised", "A", "Pain that keeps you awake torments you."),
        (9, "toothpaste", "ointment", "chocolate", "mouthwash", "A", "A toothbrush goes with a tube of toothpaste."),
        (10, "proud", "ashamed", "tired", "afraid", "A", "Instead of a lecture she said she was proud of him for sitting still."),
    ],
    "Z16": [
        (1, "exchange", "collect", "arrange", "abandon", "A", "They 'exchange their books for hoes and cutlasses' - swap one for the other."),
        (2, "believed", "doubted", "denied", "forgot", "A", "The farm was his idea because he believed textbook-only teaching was 'half learnt'."),
        (3, "assigned", "sold", "lent", "described", "A", "He divided the land into plots and assigned one to each class."),
        (4, "yield", "fence", "teacher", "uniform", "A", "The prize goes to the plot with the best yield (harvest)."),
        (5, "close", "far", "early", "late", "A", "Maize planted 'too close together' does not grow well; the sentence lists mistakes."),
        (6, "discouraged", "congratulated", "interrupted", "promoted", "A", "After a disastrous season he 'refused to be discouraged' and tried again."),
        (7, "correct", "wrong", "closest", "same", "A", "Having planted too close before, they now planted at the correct spacing."),
        (8, "enabling", "forcing", "forbidding", "warning", "A", "The sale of the surplus enabled the students to buy a wheelbarrow."),
        (9, "plot", "bag", "cup", "tower", "A", "The farm now produces 'a small plot of cassava'."),
        (10, "eagerly", "angrily", "lazily", "secretly", "A", "Students who once hated farming now compete eagerly for the committee."),
    ],
    "Z17": [
        (1, "cut", "plant", "bill", "cable", "A", "A 'power cut' is a failure of electricity supply; the story is about the lights going out."),
        (2, "followed", "caused", "stopped", "replaced", "A", "The groan was followed by the sound of generators being started."),
        (3, "short", "full", "fond", "proud", "A", "'Short of breath' - out of breath from pulling the cord."),
        (4, "welcome", "loud", "written", "free", "A", "Unhelpful advice from a bystander is 'not welcome'."),
        (5, "hearing", "seeing", "stopping", "forgetting", "A", "Sitting in the dark, they could hear the match from next door."),
        (6, "broke", "kept", "feared", "enjoyed", "A", "'Broke the silence' - was the first to speak."),
        (7, "closely", "loudly", "briefly", "rudely", "A", "They 'listened as closely as if it were new' - with full attention."),
        (8, "bothered", "refused", "failed", "learnt", "A", "'Nobody bothered to switch on the television' - they preferred the story."),
        (9, "given", "cost", "denied", "lent", "A", "The power cut had given them back an evening together."),
        (10, "instead", "ahead", "outside", "short", "A", "'Faced one another instead of a screen.'"),
    ],
    "Z18": [
        (1, "pride", "thirst", "illness", "money", "A", "He learnt out of pride - he could not stand being left to guard the bags."),
        (2, "bear", "wait", "agree", "ask", "A", "'Could not bear to be the one' - could not tolerate the idea."),
        (3, "fun", "end", "top", "rest", "A", "'For the fun of it' - for pleasure rather than payment."),
        (4, "gasping", "laughing", "singing", "smiling", "A", "After putting his face in the water he came up gasping and spitting."),
        (5, "allowing", "forcing", "telling", "ordering", "A", "To float one relaxes, 'allowing the body to go loose'."),
        (6, "just", "never", "later", "often", "A", "'Something that could just be called swimming' - barely qualifying."),
        (7, "stopping", "swimming", "breathing", "starting", "A", "Crossing the pool twice 'without stopping' shows his progress."),
        (8, "calm", "deep", "cold", "dirty", "A", "The waves of the sea are contrasted with the calm water of the pool."),
        (9, "frightened", "delighted", "bored", "asleep", "A", "He went with them, 'frightened a little', but came back on his own."),
        (10, "fighting", "swimming", "breathing", "floating", "A", "This echoes Baba Segun's lesson: 'You are fighting it, so it fights you.'"),
    ],
    "Z19": [
        (1, "accepted", "refused", "bought", "lost", "A", "He 'accepted the position in 2009 when nobody else wanted it'."),
        (2, "maintenance", "decoration", "advertising", "insurance", "A", "Residents pay for the maintenance (upkeep) of the borehole."),
        (3, "disposal", "purchase", "delivery", "storage", "A", "Notices about 'the disposal of rubbish' - how waste should be thrown away."),
        (4, "audited", "stolen", "closed", "copied", "A", "Accounts that have not been audited (checked) since 2018 are a fair complaint."),
        (5, "freely", "secretly", "late", "twice", "A", "He had 'given his time freely' - without payment."),
        (6, "bitter", "brief", "quick", "small", "A", "'Short and surprisingly bitter' - the campaign became unexpectedly hostile."),
        (7, "repaired", "condemned", "installed", "inspected", "A", "He reminded them who had repaired the borehole when it broke down."),
        (8, "represented", "renovated", "decorated", "inspected", "A", "All twelve flats were represented at the vote - unusually full attendance."),
        (9, "wishing", "warning", "ordering", "begging", "A", "'Wishing the new chairman well' - a gracious notice despite his defeat."),
        (10, "due", "paid", "lost", "free", "A", "The salary 'was due on Friday' - the payment date was approaching."),
    ],
    "Z20": [
        (1, "survived", "caused", "enjoyed", "predicted", "A", "The shop has survived recessions, fires and the internet."),
        (2, "stacked", "scattered", "sold", "hidden", "A", "Books 'stacked from floor to ceiling' in a narrow shop."),
        (3, "pause", "shout", "leave", "sleep", "A", "He pauses for a moment to think where the book is, then climbs the ladder."),
        (4, "buy", "return", "burn", "lose", "A", "A second book 'you did not ask for but will probably buy'."),
        (5, "dull", "noble", "rare", "fine", "A", "He dismisses textbooks as 'a dull trade for people in a hurry'."),
        (6, "surprise", "paper", "speed", "silence", "A", "What he sells is surprise - 'the chance to walk in wanting one thing and leave with another'."),
        (7, "loyal", "poor", "young", "noisy", "A", "Customers who have come for forty years are loyal."),
        (8, "offered", "refused", "forgot", "pretended", "A", "Three loyal customers 'offered quietly to pay the difference'."),
        (9, "reflection", "celebration", "rehearsal", "inspection", "A", "'After a night's reflection' - having thought it over."),
        (10, "keeps", "finds", "calls", "tells", "A", "'It keeps them honest' - owing money to customers keeps a shop honest."),
    ],
}

# --------------------------------------------------------------------------------------------
# Lexis: sentence interpretation
# --------------------------------------------------------------------------------------------
SI_STEM = "Choose the option that best explains the information conveyed in the sentence: "
SI = [
    ("The new stadium cost the state an arm and a leg.", "The stadium was extremely expensive", "The stadium was built by injured workers", "The stadium was finished very quickly", "The stadium was paid for by the athletes", "A", "To 'cost an arm and a leg' is to cost a great deal of money."),
    ("Ngozi visits her village once in a blue moon.", "Ngozi visits her village very rarely", "Ngozi visits her village every month", "Ngozi visits her village only at night", "Ngozi visits her village when the moon is full", "A", "'Once in a blue moon' means very rarely."),
    ("Stop beating about the bush and tell me what happened.", "Stop avoiding the point and speak plainly", "Stop cutting the hedge and come inside", "Stop shouting and lower your voice", "Stop lying and admit your mistake", "A", "'Beat about the bush' is to avoid coming to the point."),
    ("Since the factory closed, all the workers are in the same boat.", "The workers are all in the same difficult situation", "The workers have all gone fishing on the same boat", "The workers are all travelling home together by boat", "The workers have all found new jobs at the same place", "A", "'In the same boat' means facing the same unpleasant situation."),
    ("When Mr Ojo blamed poor planning, he hit the nail on the head.", "Mr Ojo identified the exact cause of the problem", "Mr Ojo injured himself while repairing the building", "Mr Ojo lost his temper with the planning committee", "Mr Ojo blamed the wrong people for the failure", "A", "To 'hit the nail on the head' is to describe a situation exactly."),
    ("Amaka has been feeling under the weather since Monday.", "Amaka has been slightly ill since Monday", "Amaka has been caught in the rain since Monday", "Amaka has been very cheerful since Monday", "Amaka has been working outdoors since Monday", "A", "'Under the weather' means unwell."),
    ("The team threw in the towel with ten minutes left.", "The team gave up before the match ended", "The team changed its kit before the match ended", "The team scored a late goal", "The team protested to the referee", "A", "'Throw in the towel' means to admit defeat."),
    ("To add insult to injury, the driver demanded extra fare after the breakdown.", "The driver made a bad situation even worse", "The driver apologised for the breakdown", "The driver was injured in the breakdown", "The driver abused the injured passengers", "A", "'Add insult to injury' is to make a bad situation worse by a further wrong."),
    ("The third late delivery was the last straw for the customer.", "The final problem that made the customer lose patience", "The customer ordered drinking straws for the third time", "The customer was pleased that the delivery finally came", "The delivery arrived without any of its packaging", "A", "'The last straw' is the final difficulty that makes a situation unbearable."),
    ("Their donation was a drop in the ocean compared to what the hospital needs.", "Their donation was very small beside what is needed", "Their donation was made to a hospital by the sea", "Their donation was lost in transit", "Their donation was larger than expected", "A", "'A drop in the ocean' is a very small amount compared with what is needed."),
    ("By studying on the bus, Tunde kills two birds with one stone.", "Tunde achieves two aims with a single action", "Tunde throws stones at birds on his way to school", "Tunde is careless with his time on the way to school", "Tunde disturbs the other passengers with his books", "A", "'Kill two birds with one stone' is to achieve two things with one effort."),
    ("With prices rising, many families struggle to make ends meet.", "Many families barely have enough money for necessities", "Many families are moving to the far ends of the town", "Many families cannot agree with one another about prices", "Many families are managing to save a great deal of money", "A", "'Make ends meet' is to have just enough money to live on."),
    ("Ade got cold feet on the morning of the wedding.", "Ade became nervous and unwilling to go ahead", "Ade had no shoes to wear to his own wedding", "Ade arrived at the wedding venue far too early", "Ade fell ill with a fever on the morning of the wedding", "A", "'Get cold feet' is to lose one's nerve about a planned action."),
    ("The fire service arrived in the nick of time.", "The fire service arrived just before it was too late", "The fire service arrived far too late to be of any help", "The fire service arrived with a badly damaged engine", "The fire service arrived at the wrong address entirely", "A", "'In the nick of time' means at the last possible moment."),
    ("Take the agent's promises with a pinch of salt.", "Do not believe the agent's promises entirely", "Reward the agent with a gift of salt", "Write the agent's promises down carefully", "Accept the agent's promises with gratitude", "A", "To take something 'with a pinch of salt' is to doubt that it is completely true."),
    ("The contractor took the lion's share of the profit.", "The contractor took the largest part of the profit", "The contractor spent the profit on a visit to the zoo", "The contractor shared the profit equally with the workers", "The contractor refused to take any part of the profit", "A", "'The lion's share' is the biggest portion."),
    ("Reading between the lines, the letter is a refusal.", "The hidden meaning of the letter is a refusal", "The letter is written on ruled paper in small print", "The letter has been read too quickly to be understood", "The letter openly and plainly refuses the request", "A", "'Read between the lines' is to find a meaning that is implied, not stated."),
    ("Little did Chike know that the letter had already been posted.", "Chike had no idea that the letter had been posted", "Chike knew only a little about the letter's contents", "Chike posted the letter himself without telling anyone", "Chike read only a small part of the letter", "A", "'Little did he know' means he was completely unaware."),
    ("Were it not for the goalkeeper, the team would have lost.", "The goalkeeper saved the team from defeat", "The goalkeeper caused the team to lose", "The team lost despite the goalkeeper", "The goalkeeper did not play in the match", "A", "'Were it not for X' means 'if X had not been there' - the goalkeeper prevented the loss."),
    ("Bisi is nothing if not punctual.", "Bisi is extremely punctual", "Bisi is never punctual", "Bisi is punctual only when it suits her", "Bisi is nothing more than punctual", "A", "'Nothing if not' emphasises a quality: she is above all punctual."),
    ("Uncle Sam is no fool when it comes to money.", "Uncle Sam is very shrewd about money", "Uncle Sam has no money at all", "Uncle Sam wastes his money foolishly", "Uncle Sam refuses to talk about money", "A", "'No fool' means very sensible or clever."),
]

# --------------------------------------------------------------------------------------------
# Synonyms / antonyms (word in capitals)
# --------------------------------------------------------------------------------------------
SYN_STEM = "Choose the option nearest in meaning to the word in capitals: "
SYN = [
    ("The typewriter has become OBSOLETE in modern offices.", "outdated", "popular", "expensive", "essential", "A", "Obsolete means no longer in use because something newer exists."),
    ("The auditor was METICULOUS in checking every receipt.", "careful", "careless", "quick", "dishonest", "A", "Meticulous means very careful and precise."),
    ("The school plans to AUGMENT its library with new books.", "enlarge", "replace", "close", "decorate", "A", "To augment is to increase or add to."),
    ("There is a DEARTH of qualified teachers in rural areas.", "shortage", "surplus", "training", "demand", "A", "A dearth is a scarcity or lack."),
    ("The charity provides food for INDIGENT families.", "poor", "large", "rural", "foreign", "A", "Indigent means very poor, needy."),
    ("The VOCIFEROUS protesters could be heard from the next street.", "noisy", "peaceful", "few", "armed", "A", "Vociferous means loud and forceful in expressing views."),
    ("The chief's OSTENTATIOUS display of wealth annoyed the villagers.", "showy", "modest", "sudden", "secret", "A", "Ostentatious means designed to impress or attract notice."),
    ("The hot afternoon made the students LETHARGIC.", "sluggish", "lively", "hungry", "talkative", "A", "Lethargic means lacking energy, drowsy."),
    ("The lawyer asked only PERTINENT questions.", "relevant", "difficult", "rude", "lengthy", "A", "Pertinent means directly related to the matter in hand."),
    ("Power supply in the area is SPORADIC.", "irregular", "constant", "expensive", "reliable", "A", "Sporadic means occurring at irregular intervals."),
    ("The dispute began over a TRIVIAL matter.", "unimportant", "serious", "financial", "legal", "A", "Trivial means of little value or importance."),
    ("She is a ZEALOUS supporter of the campaign.", "enthusiastic", "reluctant", "secret", "wealthy", "A", "Zealous means full of energy and eagerness for a cause."),
    ("The OBSTINATE boy refused to apologise.", "stubborn", "shy", "clever", "lazy", "A", "Obstinate means stubbornly refusing to change one's mind."),
    ("The AFFLUENT suburb has wide, tree-lined streets.", "wealthy", "crowded", "ancient", "remote", "A", "Affluent means having a great deal of money."),
    ("New evidence EXONERATED the accused man.", "cleared", "convicted", "frightened", "delayed", "A", "To exonerate is to free someone from blame."),
    ("The manager tried to PLACATE the angry customers.", "pacify", "avoid", "punish", "ignore", "A", "To placate is to make someone less angry."),
    ("He SQUANDERED his inheritance within two years.", "wasted", "invested", "doubled", "hid", "A", "To squander is to waste money recklessly."),
    ("The INCESSANT noise from the road kept us awake.", "continuous", "distant", "occasional", "faint", "A", "Incessant means continuing without pause."),
    ("Climbing the mountain proved an ARDUOUS task.", "difficult", "pleasant", "brief", "simple", "A", "Arduous means requiring great effort."),
    ("The report VINDICATED the doctor's decision.", "justified", "criticised", "questioned", "reversed", "A", "To vindicate is to show that something was right or justified."),
]

ANT_STEM = "Choose the option opposite in meaning to the word in capitals: "
ANT = [
    ("The bridge is only a TEMPORARY structure.", "permanent", "weak", "wooden", "modern", "A", "Temporary (lasting a short time) is the opposite of permanent."),
    ("The meaning of the poem is OBSCURE.", "clear", "hidden", "ancient", "sad", "A", "Obscure (unclear) is the opposite of clear."),
    ("The NEGLIGENT nurse forgot to record the dose.", "careful", "friendly", "junior", "tired", "A", "Negligent (careless) is the opposite of careful."),
    ("She has a PROFOUND knowledge of history.", "superficial", "wide", "detailed", "accurate", "A", "Profound (deep) is the opposite of superficial (shallow)."),
    ("His EXTRAVAGANT spending worried his parents.", "thrifty", "generous", "careless", "sudden", "A", "Extravagant (wasteful) is the opposite of thrifty (economical)."),
    ("The new engine will ACCELERATE the process.", "slow down", "speed up", "complete", "repeat", "A", "Accelerate is the opposite of slow down."),
    ("The ARROGANT official refused to listen to the farmers.", "humble", "angry", "busy", "proud", "A", "Arrogant (proud, overbearing) is the opposite of humble."),
    ("The court found the man INNOCENT.", "guilty", "free", "honest", "poor", "A", "Innocent is the opposite of guilty."),
    ("He remained cheerful in ADVERSITY.", "prosperity", "poverty", "sickness", "hardship", "A", "Adversity (misfortune) is the opposite of prosperity."),
    ("Bola is always PUNCTUAL for lectures.", "late", "early", "ready", "present", "A", "Punctual (on time) is the opposite of late."),
    ("The scene at the motor park was CHAOTIC.", "orderly", "noisy", "crowded", "dangerous", "A", "Chaotic (in complete disorder) is the opposite of orderly."),
    ("The speaker's VERBOSE address bored the audience.", "concise", "long", "loud", "learned", "A", "Verbose (using too many words) is the opposite of concise."),
    ("The doctor said the growth was BENIGN.", "malignant", "small", "painful", "harmless", "A", "Benign (not harmful) is the opposite of malignant."),
    ("The land around the mine is STERILE.", "fertile", "rocky", "dry", "flat", "A", "Sterile (unable to produce crops) is the opposite of fertile."),
    ("The MALICIOUS rumour ruined her reputation.", "benevolent", "spiteful", "false", "secret", "A", "Malicious (intending harm) is the opposite of benevolent (kindly)."),
    ("As a NOVICE, he made many mistakes.", "expert", "student", "child", "stranger", "A", "A novice (beginner) is the opposite of an expert."),
    ("The RIGID rules allowed no exceptions.", "flexible", "strict", "new", "written", "A", "Rigid (unbending) is the opposite of flexible."),
    ("The village was TRANQUIL at dawn.", "noisy", "calm", "dark", "cold", "A", "Tranquil (peaceful) is the opposite of noisy."),
    ("The shop sells ARTIFICIAL flowers.", "natural", "plastic", "bright", "large", "A", "Artificial (man-made) is the opposite of natural."),
    ("The road began to DETERIORATE after the floods.", "improve", "worsen", "change", "narrow", "A", "Deteriorate (get worse) is the opposite of improve."),
]

# --------------------------------------------------------------------------------------------
# Grammar / sentence completion
# --------------------------------------------------------------------------------------------
GR_STEM = "Choose the option that best completes the gap: "
GR = [
    ("Mathematics ____ my favourite subject.", "is", "are", "were", "have been", "A", "Names of subjects ending in -s (mathematics, physics, economics) take a singular verb."),
    ("Either the students or the teacher ____ responsible for the noise.", "is", "are", "were", "have been", "A", "With 'either... or' the verb agrees with the nearer subject, 'the teacher'."),
    ("She speaks English ____ than her brother.", "more fluently", "most fluently", "fluentlier", "more fluent", "A", "An adverb of manner ('fluently') forms its comparative with 'more'."),
    ("This is the ____ book I have ever read.", "most interesting", "more interesting", "interestingest", "interesting", "A", "'The... I have ever' requires the superlative: 'most interesting'."),
    ("He has very ____ friends, so he is often lonely.", "few", "little", "less", "a little", "A", "'Friends' is countable, so 'few' (not 'little') is used."),
    ("There is ____ milk left in the fridge, so buy some.", "little", "few", "a few", "many", "A", "'Milk' is uncountable, so 'little' is used; 'little' (not 'a little') stresses the shortage."),
    ("I have not seen Musa ____ last Christmas.", "since", "for", "from", "during", "A", "'Since' marks the starting point of a period that continues to now."),
    ("The meeting has been postponed ____ next Tuesday.", "until", "by", "on", "at", "A", "Something is postponed until (up to) a later time."),
    ("Funke is married ____ a doctor from Ilorin.", "to", "with", "by", "for", "A", "One is married to a person, not 'with'."),
    ("The clerk was accused ____ stealing the money.", "of", "for", "with", "on", "A", "'Accused of' is the correct collocation ('charged with', but 'accused of')."),
    ("The chairman objected ____ the new proposal.", "to", "at", "on", "against", "A", "'Object to' is the correct preposition."),
    ("The novel consists ____ twelve chapters.", "of", "in", "with", "from", "A", "'Consist of' means to be made up of."),
    ("We arrived ____ Lagos shortly after noon.", "in", "at", "to", "on", "A", "'Arrive in' is used for cities and countries; 'arrive at' for smaller places or buildings."),
    ("The teacher shared the sweets ____ the five children.", "among", "between", "across", "within", "A", "'Among' is used for more than two; 'between' for two."),
    ("If Ada had studied harder, she ____ the examination.", "would have passed", "would pass", "will pass", "had passed", "A", "Third conditional: 'if' + past perfect, 'would have' + past participle."),
    ("I wish it ____ raining so that we could go out.", "would stop", "stops", "will stop", "has stopped", "A", "'Wish' + 'would' expresses a desire for a change in the present situation."),
    ("By the time you arrive, we ____ dinner.", "will have finished", "finish", "have finished", "are finishing", "A", "The future perfect describes an action completed before a future time."),
    ("The letters ____ yesterday, so they should arrive tomorrow.", "were posted", "are posted", "have been posted", "posted", "A", "A finished past action with a time adverb ('yesterday') takes the simple past passive."),
    ("He asked me whether I ____ the film before.", "had seen", "have seen", "saw", "see", "A", "In reported speech after 'asked', the present perfect becomes the past perfect."),
    ("You ____ better see a doctor about that cough.", "had", "have", "would", "should", "A", "'Had better' + bare infinitive is the fixed expression for advice."),
    ("____ he is very rich, he is not happy.", "Although", "Despite", "However", "In spite of", "A", "'Although' introduces a clause; 'despite' and 'in spite of' take a noun or -ing form."),
    ("The reason he failed is ____ he did not read.", "that", "because", "why", "for", "A", "'The reason... is that' is the accepted construction; 'the reason is because' is faulty."),
    ("It was ____ hot day that we could not go out.", "such a", "so", "so a", "such", "A", "'Such a' + adjective + noun; 'so' is followed directly by an adjective."),
    ("Amina is ____ honest girl.", "an", "a", "the", "one", "A", "'Honest' begins with a vowel sound (the 'h' is silent), so 'an' is used."),
    ("One of the boys ____ broken the window.", "has", "have", "are", "were", "A", "The subject is 'one', which is singular."),
    ("The information you gave me ____ very useful.", "was", "were", "have been", "are", "A", "'Information' is an uncountable noun and takes a singular verb."),
    ("Ten thousand naira ____ not enough for the rent.", "is", "are", "were", "have been", "A", "A sum of money regarded as a single amount takes a singular verb."),
    ("Kemi ____ in Kano for ten years before she moved to Jos.", "had lived", "has lived", "lives", "is living", "A", "The past perfect shows the earlier of two past actions."),
    ("The teacher made us ____ the passage aloud.", "read", "to read", "reading", "reads", "A", "'Make' + object + bare infinitive (without 'to') in the active voice."),
    ("Ayo avoided ____ to his uncle after the quarrel.", "speaking", "to speak", "speak", "spoke", "A", "'Avoid' is followed by the -ing form."),
    ("Everyone except Tunde ____ arrived.", "has", "have", "are", "were", "A", "'Everyone' is singular; the phrase 'except Tunde' does not change the number."),
    ("Would you mind ____ the window?", "opening", "to open", "open", "opened", "A", "'Mind' is followed by the -ing form."),
]

# --------------------------------------------------------------------------------------------
# Oral English
# --------------------------------------------------------------------------------------------
STRESS_STEM = "In the following word, choose the option that has the correct stress pattern (the stressed syllable is written in capitals): "
STRESS = [
    ("university", "U-ni-ver-si-ty", "u-NI-ver-si-ty", "u-ni-VER-si-ty", "u-ni-ver-SI-ty", "C", "u-ni-VER-si-ty - words ending in '-ity' are stressed on the syllable before '-ity'."),
    ("important", "IM-por-tant", "im-POR-tant", "im-por-TANT", "IM-POR-tant", "B", "im-POR-tant - stress on the second syllable."),
    ("engineer", "EN-gi-neer", "en-GI-neer", "en-gi-NEER", "EN-GI-neer", "C", "Words ending in '-eer' are stressed on that ending: en-gi-NEER."),
    ("competition", "COM-pe-ti-tion", "com-PE-ti-tion", "com-pe-TI-tion", "com-pe-ti-TION", "C", "'-tion' words are stressed on the syllable before the ending: com-pe-TI-tion."),
    ("certificate", "CER-ti-fi-cate", "cer-TI-fi-cate", "cer-ti-FI-cate", "cer-ti-fi-CATE", "B", "cer-TI-fi-cate - stress on the second syllable."),
    ("information", "IN-for-ma-tion", "in-FOR-ma-tion", "in-for-MA-tion", "in-for-ma-TION", "C", "'-tion' words are stressed on the preceding syllable: in-for-MA-tion."),
    ("hospital", "HOS-pi-tal", "hos-PI-tal", "hos-pi-TAL", "hos-PI-TAL", "A", "HOS-pi-tal - stress on the first syllable."),
    ("independent", "IN-de-pen-dent", "in-DE-pen-dent", "in-de-PEN-dent", "in-de-pen-DENT", "C", "in-de-PEN-dent - stress on the third syllable."),
    ("calculator", "CAL-cu-la-tor", "cal-CU-la-tor", "cal-cu-LA-tor", "cal-cu-la-TOR", "A", "CAL-cu-la-tor - stress on the first syllable, as in 'calculate'."),
    ("apology", "A-po-lo-gy", "a-PO-lo-gy", "a-po-LO-gy", "a-po-lo-GY", "B", "a-PO-lo-gy - stress on the second syllable."),
]

RHYME_STEM = "Choose the word that rhymes with the word in capitals: "
RHYME = [
    ("BOUGH", "cow", "dough", "tough", "through", "A", "'Bough' is /baʊ/, rhyming with 'cow'; 'dough' is /dəʊ/, 'tough' /tʌf/, 'through' /θruː/."),
    ("SUITE", "sweet", "suit", "site", "shoot", "A", "'Suite' is pronounced /swiːt/, exactly like 'sweet'."),
    ("CHOIR", "fire", "chair", "core", "cheer", "A", "'Choir' is /kwaɪə/, rhyming with 'fire'."),
    ("BREAK", "cake", "beak", "brick", "bleak", "A", "'Break' is /breɪk/, rhyming with 'cake', not with 'beak' or 'bleak'."),
    ("HEIR", "air", "here", "hire", "her", "A", "'Heir' has a silent 'h' and is pronounced /eə/, like 'air'."),
]

SOUND = [
    ("Choose the word that has the same vowel sound as the one represented by the letters in capitals: sEAt", "field", "head", "bear", "heart", "A", "'Seat' has /iː/, as in 'field'."),
    ("Choose the word that has the same vowel sound as the one represented by the letter in capitals: fUll", "good", "fool", "cut", "fun", "A", "'Full' has the short /ʊ/, as in 'good'; 'fool' has the long /uː/."),
    ("Choose the word that has the same vowel sound as the one represented by the letters in capitals: fEAr", "here", "hair", "fur", "far", "A", "'Fear' has /ɪə/, as in 'here'."),
    ("Choose the word that has the same vowel sound as the one represented by the letters in capitals: hAIr", "there", "here", "her", "hire", "A", "'Hair' has /eə/, as in 'there'."),
    ("Choose the word that has the same vowel sound as the one represented by the letters in capitals: flOOd", "blood", "food", "foot", "floor", "A", "'Flood' is pronounced with /ʌ/, like 'blood', despite the spelling."),
    ("Choose the word that has the same vowel sound as the one represented by the letter in capitals: lIght", "buy", "bit", "beat", "bet", "A", "'Light' has /aɪ/, as in 'buy'."),
    ("Choose the word that has the same vowel sound as the one represented by the letter in capitals: hAnd", "cat", "car", "call", "cake", "A", "'Hand' has /æ/, as in 'cat'."),
    ("Choose the word that has the same vowel sound as the one represented by the letters in capitals: wOrk", "bird", "born", "bore", "bar", "A", "'Work' has /ɜː/, as in 'bird'."),
    ("Choose the word that has the same consonant sound as the one represented by the letter in capitals: viSion", "leisure", "sure", "session", "send", "A", "The 's' in 'vision' is /ʒ/, as in 'leisure'; 'sure' and 'session' have /ʃ/."),
    ("Choose the word that has the same consonant sound as the one represented by the letters in capitals: PHone", "laugh", "pin", "hope", "shop", "A", "'ph' in 'phone' is /f/, as is the 'gh' in 'laugh'."),
    ("Choose the word in which the letter 'k' is SILENT.", "knee", "kite", "king", "kettle", "A", "In 'knee' the 'k' before 'n' is not pronounced."),
    ("Choose the word in which the letter 't' is SILENT.", "castle", "table", "title", "tent", "A", "In 'castle' the 't' is silent: /kɑːsl/."),
    ("Choose the word in which the letter 's' is SILENT.", "island", "insist", "system", "sister", "A", "In 'island' the 's' is not pronounced: /aɪlənd/."),
    ("Choose the word in which the letter 'g' is SILENT.", "gnaw", "gate", "gift", "game", "A", "In 'gnaw' the 'g' before 'n' is silent."),
]

EMPH_STEM = "Choose the option to which the given sentence relates when the word in capitals is stressed: "
EMPH = [
    ("FATIMA baked the cake for the party.", "Did Zainab bake the cake for the party?", "Did Fatima buy the cake for the party?", "Did Fatima bake the bread for the party?", "Did Fatima bake the cake for the wedding?", "A", "Stress on FATIMA contrasts the person who baked it."),
    ("The mechanic repaired the CAR yesterday.", "Did the mechanic repair the bus yesterday?", "Did the mechanic repair the car today?", "Did the driver repair the car yesterday?", "Did the mechanic wash the car yesterday?", "A", "Stress on CAR contrasts what was repaired."),
    ("Emeka travelled to Enugu by TRAIN.", "Did Emeka travel to Enugu by bus?", "Did Emeka travel to Onitsha by train?", "Did Obi travel to Enugu by train?", "Did Emeka walk to Enugu yesterday?", "A", "Stress on TRAIN contrasts the means of transport."),
    ("The children PLANTED the trees last week.", "Did the children cut down the trees last week?", "Did the teachers plant the trees last week?", "Did the children plant the flowers last week?", "Did the children plant the trees yesterday?", "A", "Stress on PLANTED contrasts the action."),
    ("Mrs Bello bought TWO goats at the market.", "Did Mrs Bello buy three goats at the market?", "Did Mrs Bello buy two goats at the farm?", "Did Mr Bello buy two goats at the market?", "Did Mrs Bello sell two goats at the market?", "A", "Stress on TWO contrasts the number."),
]


def build():
    subject = "Use of English"
    questions = []
    passages = [{"key": k, "title": t, "text": x} for k, t, x in COMP_P] + [{"key": k, "title": t, "text": x} for k, t, x in CLOZE_P]
    for key, diff, q, a, b, c, d, ans, exp in COMP:
        questions.append({"subject": subject, "topic": "Comprehension", "passage": key, "difficulty": diff, "q": q,
                          "A": a, "B": b, "C": c, "D": d, "answer": ans, "explanation": exp})
    titles = {k: t for k, t, _ in CLOZE_P}
    ptext = {k: x for k, _, x in CLOZE_P}
    for key, rows in CLOZE.items():
        short = titles[key].split(": ", 1)[1]
        assert len(rows) == 10, key
        for n, a, b, c, d, ans, exp in rows:
            assert f"[{n}]" in ptext[key], (key, n)
            questions.append({"subject": subject, "topic": "Cloze Tests", "passage": key, "difficulty": "Medium",
                              "q": f"In the cloze passage above ('{short}'), choose the most appropriate option to fill gap [{n}].",
                              "A": a, "B": b, "C": c, "D": d, "answer": ans, "explanation": exp})
    for stem, topic, rows in ((SI_STEM, "Lexis and Structure", SI), (SYN_STEM, "Synonyms", SYN), (ANT_STEM, "Antonyms", ANT),
                              (GR_STEM, "Sentence Completion", GR), (STRESS_STEM, "Oral English", STRESS),
                              (RHYME_STEM, "Oral English", RHYME), (EMPH_STEM, "Oral English", EMPH)):
        for q, a, b, c, d, ans, exp in rows:
            questions.append({"subject": subject, "topic": topic, "difficulty": "Medium", "q": stem + q,
                              "A": a, "B": b, "C": c, "D": d, "answer": ans, "explanation": exp})
    for q, a, b, c, d, ans, exp in SOUND:
        questions.append({"subject": subject, "topic": "Oral English", "difficulty": "Medium", "q": q,
                          "A": a, "B": b, "C": c, "D": d, "answer": ans, "explanation": exp})

    # Cloze keys: deterministic rotation so the answers spread over A-D within each passage.
    cloze = [q for q in questions if q["topic"] == "Cloze Tests"]
    for i, q in enumerate(cloze):
        opts = [q[k] for k in "ABCD"]
        shift = (i * 3 + 2) % 4
        opts = opts[-shift:] + opts[:-shift] if shift else opts
        new_ans = "ABCD"[("ABCD".index(q["answer"]) + shift) % 4]
        for k, v in zip("ABCD", opts):
            q[k] = v
        q["answer"] = new_ans
    rest = [q for q in questions if q["topic"] != "Cloze Tests"]
    _balance(rest)
    questions = cloze + rest

    # Gates (same as batch_common): unique stems, four options, explanation length, length bias.
    texts = [(x["q"], x.get("passage")) for x in questions]
    assert len(texts) == len(set(texts)), "duplicate question text"
    problems = []
    for x in questions:
        if not (x["answer"] in "ABCD" and all(x[k] for k in "ABCD")):
            problems.append(("missing option", x["q"]))
        if len(x["explanation"]) < 25:
            problems.append(("short explanation", x["q"]))
        distinct = {x[k].strip() for k in "ABCD"} if "stress pattern" in x["q"] else {x[k].strip().lower() for k in "ABCD"}
        if len(distinct) != 4:
            problems.append(("repeated option", x["q"]))
        lens = {k: len(x[k]) for k in "ABCD"}
        longest_other = max(v for k, v in lens.items() if k != x["answer"])
        if lens[x["answer"]] > 30 and lens[x["answer"]] > 1.5 * longest_other:
            problems.append(("length bias", x["q"], lens))
    if problems:
        for p in problems:
            print("PROBLEM:", p)
        sys.exit(f"{len(problems)} problems - file not written.")

    batch = {
        "batch_id": "batch_034_english_round5",
        "exam_type": "JAMB",
        "note": "Use of English round 5: 12 new comprehension passages, 8 new cloze passages, sentence interpretation, synonyms/antonyms in sentences, grammar, oral forms.",
        "passages": passages,
        "questions": questions,
        "deactivate": [],
    }
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(batch, fh, ensure_ascii=False, indent=1)
    print(f"wrote {OUT}: {len(questions)} questions, {len(passages)} passages")
    print("answer letters:", dict(Counter(x["answer"] for x in questions)))
    print("cloze letters:", dict(Counter(x["answer"] for x in cloze)))
    print("per topic:", dict(sorted(Counter(x["topic"] for x in questions).items())))
    # Passage questions are unique by construction (stem + passage); scan the stand-alone items.
    n = _near_duplicates(subject, [q for q in questions if not q.get("passage")], OUT_NAME)
    print(f"near-duplicate warnings: {n}")


if __name__ == "__main__":
    build()
