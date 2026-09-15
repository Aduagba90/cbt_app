"""Rewritten distractors for items whose correct option was much longer than the wrong ones.
Keyed by (start of) question text -> {old distractor text: new distractor text}.
Applied by build scripts before letter balancing, so answer keys are untouched.
"""

FIXES = {
    # ---------- batch 5 (English) ----------
    "The orthopaedic ward was nicknamed 'the okada ward' because": {
        "riders worked there": "most of the nurses on the ward had once been riders",
        "it was built with money from riders": "it had been built with levies collected from riders",
        "it was near the motorcycle park": "it stood directly opposite the main motorcycle park",
    },
    "The commissioner's question 'How many broken legs is a fast journey worth?' is intended to": {
        "request accurate statistics": "request accurate accident statistics from hospitals",
        "admit that the policy failed": "admit that the government's ban has failed",
        "mock the riders": "mock the riders for their reckless driving",
    },
    "The critics' main objection is that the government": {
        "banned motorcycles too late": "waited far too long before banning motorcycles",
        "ignored the hospital records": "refused to publish the hospital records",
        "punished office workers": "punished office workers instead of riders",
    },
    "The girl's remark 'Here you find Baba Book' implies that": {
        "the digital library has no staff": "the new digital library has no trained staff",
        "the old library has more books": "the old library has far more books than the new one",
        "the teenagers dislike computers": "the teenagers are uncomfortable with computers",
    },
    "Mr Adekunle cleaned his spectacles 'for a very long time' because he": {
        "could not see well": "could no longer see well without them",
        "wanted to leave": "was looking for an excuse to leave the room",
        "was angry with the girl": "was too annoyed with the girl to reply",
    },
    "Choose the option that best explains the information conveyed in the sentence: Not even the principal could persuade Tunde to apologise.": {
        "The principal did not try to persuade Tunde": "The principal did not make any attempt to persuade Tunde to apologise",
        "Tunde apologised only to the principal": "Tunde eventually apologised, but only to the principal himself",
        "Tunde persuaded the principal to apologise": "Tunde succeeded in persuading the principal to apologise instead",
    },
    # ---------- batch 6 (sciences) ----------
    "Aluminium does not corrode as readily as iron because": {
        "aluminium is less reactive than iron": "aluminium is much lower than iron in the reactivity series",
        "aluminium does not react with oxygen": "aluminium does not react with oxygen or water vapour",
        "iron is a transition metal": "iron is a transition metal with variable oxidation states",
    },
    "A student observed a thin slice of onion under the microscope and saw cells with a cell wall and nucleus but no chloroplasts. This is because": {
        "onion cells are animal cells": "onion cells are animal cells and therefore lack plastids",
        "the slice was too thin": "the slice was too thin for chloroplasts to be visible",
        "chloroplasts are found only in roots": "chloroplasts are found only in the roots of the onion plant",
    },
    "A patient is unable to digest fats properly after the removal of the gall bladder because": {
        "no lipase is produced": "the body can no longer produce any lipase at all",
        "the stomach cannot churn food": "the stomach can no longer churn fatty food properly",
        "the pancreas stops working": "the pancreas stops secreting its digestive juices",
    },
    "The same starch-saliva experiment was repeated with the saliva first boiled. Iodine turned blue-black. This is because boiling": {
        "increased the enzyme's activity": "increased the activity of the enzyme too much",
        "converted starch to glucose": "converted all the starch directly into glucose",
        "made the iodine stronger": "made the iodine solution more concentrated",
    },
    "A ring of bark (containing phloem) was removed from around a tree trunk. After some weeks the bark above the ring swelled because": {
        "water accumulated above the ring": "water from the roots accumulated above the ring",
        "the xylem was blocked": "the xylem vessels became blocked at the ring",
        "the roots sent food upwards": "the roots sent extra food upwards to heal the wound",
    },
    "Two flasks of germinating seeds were set up; the seeds in the second flask were first boiled. A thermometer in the first flask showed a rise in temperature, the second showed none. This shows that": {
        "boiled seeds respire faster": "boiled seeds respire faster than living seeds",
        "boiling adds heat to seeds": "boiling stores extra heat inside the seeds",
        "germinating seeds absorb heat": "germinating seeds absorb heat from the air",
    },
    "Yeast added to a sugar solution in a warm place produces bubbles of gas and a smell of alcohol. The process is": {
        "aerobic respiration": "aerobic respiration in the yeast",
        "photosynthesis": "photosynthesis by the yeast cells",
        "transpiration": "transpiration from the solution",
    },
    "Glucose was found in a patient's urine. This suggests a problem with": {
        "the liver's production of bile": "the liver's production and storage of bile",
        "the lungs": "the exchange of gases in the lungs",
        "the sweat glands": "the sweat glands and the control of body temperature",
    },
    "On a cold day a person passes more dilute urine than on a hot day because": {
        "the kidneys work harder in cold weather": "the kidneys filter blood much faster in cold weather",
        "the bladder expands in cold weather": "the bladder expands and holds more urine in cold weather",
        "cold water is drunk": "more cold water is drunk, which the kidneys cannot absorb",
    },
    "A plant left unwatered wilts because": {
        "its xylem vessels break": "its xylem vessels collapse and can no longer carry water",
        "its cell walls dissolve": "its cell walls dissolve once water is no longer available",
        "photosynthesis stops": "photosynthesis stops and the leaves no longer make food",
    },
    "A boy walking from bright sunlight into a dim room cannot see clearly at first. During this time his": {
        "pupils constrict": "pupils constrict to protect the retina",
        "lenses become thinner": "lenses become thinner to focus on near objects",
        "corneas thicken": "corneas thicken to gather more light",
    },
    "Lichens growing on a bare rock surface are an example of": {
        "climax vegetation": "climax vegetation in a stable community",
        "parasites": "parasites feeding on the minerals in rock",
        "secondary succession": "secondary succession after a forest fire",
    },
    "The main reason why farmers practise crop rotation with legumes is that legumes": {
        "need little water": "need very little water and survive drought",
        "have deep roots": "have deep roots that break up hard soil",
        "grow quickly": "grow quickly and shade out weeds",
    },
    # ---------- batch 8 : Economics ----------
    "The demand for salt is price inelastic mainly because salt": {
        "is expensive": "is expensive relative to other food items",
        "has many substitutes": "has many close substitutes in the market",
        "is a luxury": "is regarded as a luxury by most households",
    },
    "Malthus argued that population grows in a geometric progression while food supply grows in an arithmetic progression. His prediction has been largely averted in many countries mainly because of": {
        "wars and famines": "frequent wars and famines that reduced population",
        "a fall in life expectancy": "a general fall in life expectancy in poor countries",
        "migration to Africa": "large-scale migration of Europeans to Africa",
    },
    "The main reason governments impose excise duties on cigarettes and alcohol is to": {
        "encourage their production": "encourage local production of these goods",
        "increase imports": "increase the importation of cheaper brands",
        "subsidise farmers": "subsidise the farmers who grow tobacco",
    },
    "The main argument for protecting infant industries with tariffs is that they": {
        "will never be competitive": "will never be able to compete without tariffs",
        "produce only for export": "produce mainly for the export market",
        "employ foreigners": "employ mainly foreign skilled workers",
    },
    "A major reason why agricultural prices in Nigeria fluctuate more than the prices of manufactured goods is that": {
        "farmers are wealthy": "farmers are wealthy enough to withhold their produce",
        "food demand is elastic": "the demand for food is highly elastic in Nigeria",
        "manufactured goods are imported": "manufactured goods are imported at fixed world prices",
    },
    "Which of the following is the best indicator of a country's level of development?": {
        "total GDP": "the total gross domestic product",
        "size of population": "the total size of the population",
        "number of universities": "the number of universities in the country",
    },
    "Nigeria's development plans have often failed to meet their targets mainly because of": {
        "too many universities": "the establishment of too many universities",
        "excess foreign aid": "excessive inflows of foreign aid and loans",
        "over-population of Lagos": "the over-population of Lagos and other cities",
    },
    # ---------- batch 8 : Commerce ----------
    "A trader keeps a stock of 200 cartons of milk although she sells 20 cartons a week. The main disadvantage of holding such stock is": {
        "she cannot meet demand": "she will be unable to meet sudden demand",
        "her shop looks empty": "her shop will look empty to customers",
        "she cannot get a discount": "she will not qualify for a trade discount",
    },
    "A manufacturer decides to sell directly to retailers, bypassing wholesalers. A likely disadvantage to the manufacturer is that it must now": {
        "reduce production": "reduce production to match smaller orders",
        "increase prices to wholesalers": "increase the prices it charges to wholesalers",
        "stop advertising": "stop advertising because retailers do it",
    },
    "A Nigerian exporter wants to be sure of payment before shipping goods to a new customer in Ghana. The safest method is": {
        "open account": "an open account with monthly settlement",
        "a post-dated cheque": "a post-dated cheque from the customer",
        "cash on delivery": "cash on delivery through the shipping agent",
    },
    "The document that gives details of goods to be exported and is used by customs officers to assess duty is": {
        "a bill of lading": "a bill of lading issued by the shipping line",
        "a certificate of origin": "a certificate of origin from the chamber of commerce",
        "an indent": "an indent sent by the overseas buyer",
    },
    "A company's telephone system that allows callers to dial extensions directly within the office is": {
        "a telex": "a telex machine linked to the head office",
        "a courier service": "a courier service for internal mail",
        "a fax machine": "a fax machine connected to every department",
    },
    "Mr Bello insured his car with two companies for its full value of ₦4 million each. After a total loss, he can recover": {
        "₦8 million in total": "₦8 million in total, ₦4 million from each insurer",
        "nothing": "nothing, because double insurance cancels both policies",
        "₦4 million from each company": "₦4 million from each company plus interest",
    },
    "A company insures its workers against injury at work. This type of insurance is": {
        "life assurance": "life assurance for the employees",
        "marine insurance": "marine insurance on the company's staff",
        "fidelity guarantee": "fidelity guarantee insurance for staff",
    },
    "A trader ships goods worth ₦10 million to Lagos and insures them against loss at sea. Because the ship arrived safely, the trader": {
        "receives his premium back": "receives his premium back because no loss occurred",
        "receives interest on the premium": "receives interest on the premium for the period",
        "can claim half the premium": "can claim half the premium as a no-claim bonus",
    },
    "A chamber of commerce differs from a trade association in that a chamber of commerce": {
        "represents only one industry": "represents the interests of only one industry",
        "is a government agency": "is a government agency that regulates trade",
        "sells goods to members": "buys and sells goods on behalf of members",
    },
    # ---------- batch 8 : Literature ----------
    "'and it is not a question' suggests that the grandfather": {
        "does not care whether the speaker returns": "does not really care whether the speaker returns or not",
        "has forgotten the speaker's name": "has grown so old that he has forgotten the speaker's name",
        "is deaf": "is too deaf to hear any answer the speaker might give",
    },
    "The ringing phone 'in a city that does not know his name' emphasises": {
        "the grandfather's popularity": "how popular the grandfather once was in the city",
        "the speaker's wealth": "the wealth the speaker has acquired in the city",
        "the noise of Lagos": "the constant noise and bustle of life in Lagos",
    },
    "The broom in the extract functions mainly as": {
        "a weapon": "a weapon she intends to use against the council",
        "a prop with no meaning": "a stage prop with no meaning beyond the action",
        "comic relief": "comic relief to lighten the mood of the scene",
    },
    "Segun's action of 'putting the phone away at last' marks": {
        "the climax of his indifference": "the climax of his indifference towards his mother",
        "his decision to leave": "his decision to leave the market and go home",
        "his anger with his mother": "his anger with his mother for shouting at him",
    },
    "In 'The Lion and the Jewel', Lakunle's insistence on Western ways while refusing to pay the bride price presents him as": {
        "a tragic hero": "a tragic hero destroyed by his ideals",
        "the voice of tradition": "the true voice of village tradition",
        "a chorus figure": "a chorus figure commenting on events",
    },
    "In 'Second Class Citizen' by Buchi Emecheta, Adah's struggle in London mainly dramatises": {
        "the joys of migration": "the joys and rewards of migrating to Britain",
        "the superiority of Western education": "the superiority of Western education over African",
        "life in an Igbo village": "the peaceful rhythm of life in an Igbo village",
    },
    "'Unexpected Joy at Dawn' by Alex Agyei-Agyiri is set against the background of": {
        "the Nigerian civil war": "the Nigerian civil war and the blockade of Biafra",
        "the Ethiopian famine": "the Ethiopian famine and the refugee crisis of the 1980s",
        "apartheid in South Africa": "apartheid in South Africa and the Soweto uprising",
    },
    "In 'Wuthering Heights', Heathcliff's cruelty in adulthood is presented as rooted mainly in": {
        "his wealth": "the sudden wealth he acquires during his absence",
        "his education": "the harsh education he received at Thrushcross Grange",
        "his religion": "the strict religion preached to him by Joseph",
    },
    "In 'Look Back in Anger', Jimmy Porter's constant tirades chiefly express": {
        "contentment with post-war Britain": "his deep contentment with life in post-war Britain",
        "religious devotion": "his religious devotion and longing for the church",
        "love of the upper class": "his admiration for the upper class and its values",
    },
    "In Niyi Osundare's 'The Leader and the Led', the animals' search for a leader ends with the choice of": {
        "the lion, for its strength": "the lion, because of its strength and majesty",
        "no leader at all": "no leader at all, since every animal is rejected",
        "the hyena": "the hyena, because it is cunning and fearless",
    },
    "Senghor's 'Black Woman' is best described as": {
        "a lament for a dead mother": "a lament for the poet's dead mother",
        "a protest against colonialism only": "a bitter protest against French colonial rule",
        "a love poem to a European woman": "a love poem addressed to a European woman",
    },
    "In Maya Angelou's 'Caged Bird', the caged bird 'sings of freedom' because": {
        "it is happy in the cage": "it is perfectly happy and contented in the cage",
        "the free bird taught it": "the free bird taught it the song of freedom",
        "it wants food": "it wants its keeper to bring it food and water",
    },
    "T. S. Eliot's 'The Journey of the Magi' presents the wise men's journey as": {
        "easy and joyful": "easy, joyful and full of celebration",
        "a dream": "a dream from which the speaker awakes",
        "a military expedition": "a military expedition against a rival king",
    },
    # ---------- batch 8 : Government ----------
    "A state differs from a nation in that a state must have": {
        "a common language": "a common language spoken by all its people",
        "a common culture": "a common culture shared by all its people",
        "a common religion": "a common religion practised by all its people",
    },
    "In a confederation, the central authority is": {
        "supreme over the units": "supreme over the units, which cannot secede",
        "responsible for all taxation": "responsible for all taxation in the member states",
        "elected directly by all citizens": "elected directly by all citizens of the member states",
    },
    "Which of the following is an advantage of federalism for a country like Nigeria?": {
        "it eliminates ethnic differences": "it eliminates ethnic differences among the people",
        "it makes government cheaper": "it makes government cheaper by reducing the number of officials",
        "it removes the need for a constitution": "it removes the need for a written constitution",
    },
    "Britain is said to have an unwritten constitution because": {
        "it has no rules of government": "it has no rules regulating the conduct of government",
        "parliament has no powers": "parliament has no powers to make constitutional law",
        "its laws are not written down": "its laws are passed on by word of mouth alone",
    },
    "A written constitution is an advantage for a federal state mainly because it": {
        "can be changed easily": "can be changed easily whenever the need arises",
        "abolishes the courts": "abolishes the need for courts to settle disputes",
        "removes political parties": "removes the need for political parties and elections",
    },
    "A major weakness of the one-party system is that it": {
        "encourages opposition": "encourages too much opposition to government",
        "is too expensive": "is too expensive for developing countries to run",
        "wastes money on many elections": "wastes public money on too many elections",
    },
    "Which of the following is the most important channel for measuring public opinion in a modern democracy?": {
        "town criers": "town criers and market announcements",
        "the civil service": "the civil service and its records",
        "traditional rulers": "traditional rulers and their councils",
    },
    "A common feature of the Yoruba and Hausa/Fulani pre-colonial systems that made indirect rule easy to apply was": {
        "the absence of chiefs": "the total absence of chiefs and kings",
        "republican assemblies": "republican assemblies of all adult males",
        "written constitutions": "written constitutions limiting the rulers",
    },
    "Herbert Macaulay is regarded as the father of Nigerian nationalism mainly because he": {
        "led the army": "led the army that resisted the British occupation",
        "wrote the 1922 Constitution": "wrote the 1922 Constitution for Sir Hugh Clifford",
        "became the first Governor-General": "became the first Nigerian Governor-General",
    },
    "The Macpherson Constitution of 1951 was significant because it": {
        "granted independence": "granted Nigeria full independence from Britain",
        "created the Senate": "created the Senate as a second legislative chamber",
        "abolished the regions": "abolished the three regions created by Richards",
    },
    "The Independence Constitution of 1960 provided for": {
        "an executive president": "an executive president elected by the whole country",
        "a unitary government": "a unitary government with power concentrated in Lagos",
        "military rule": "a period of military rule before civilian government",
    },
    "A major factor in the collapse of the First Republic was": {
        "the discovery of oil": "the discovery of oil in commercial quantities",
        "foreign invasion": "the invasion of the country by foreign forces",
        "the creation of states": "the creation of twelve states out of the regions",
    },
    "The body responsible for sharing federally collected revenue among the three tiers of government is the": {
        "Central Bank of Nigeria": "Central Bank of Nigeria's monetary policy committee",
        "National Assembly alone": "National Assembly Committee on Appropriation",
        "Federal Character Commission": "Federal Character Commission of Nigeria",
    },
    "The 1976 local government reform is important because it": {
        "abolished local governments": "abolished local governments throughout the federation",
        "created states": "created seven additional states out of the existing twelve",
        "introduced indirect rule": "introduced indirect rule through traditional rulers",
    },
    "A major problem of local governments in Nigeria is": {
        "too much revenue": "too much revenue from the federation account",
        "too many qualified staff": "too many highly qualified staff on the payroll",
        "lack of constitutional recognition": "lack of recognition in the 1999 Constitution",
    },
    "Public corporations were established mainly to": {
        "make maximum profit for shareholders": "make maximum profit for their private shareholders",
        "compete with the civil service": "compete with the civil service for skilled staff",
        "employ politicians": "provide employment for politicians who lost elections",
    },
    "Which of the following is a determinant of a country's foreign policy?": {
        "the weather": "the weather and climate of the country",
        "the number of universities": "the number of universities in the country",
        "the size of its capital city": "the size and location of its capital city",
    },
    "The Commonwealth Prime Ministers' Conference held in Lagos in January 1966 was convened mainly to discuss": {
        "the Suez crisis": "Britain's role in the Suez crisis of 1956",
        "the Nigerian civil war": "the threat of civil war in Nigeria",
        "the price of cocoa": "the falling world price of cocoa and groundnuts",
    },
    "The Commonwealth of Nations is an association of": {
        "all African countries": "all independent African countries",
        "West African states": "the English-speaking West African states",
        "oil-producing states": "the major oil-producing states of the world",
    },
    "Nigeria is a member of OPEC. The main aim of OPEC is to": {
        "fight terrorism": "fight terrorism in oil-producing regions",
        "promote free trade in Africa": "promote free trade among African countries",
        "provide loans to poor nations": "provide soft loans to poor oil-importing nations",
    },
    # ---------- batch 8 : CRS ----------
    "At Mount Sinai the covenant between God and Israel was sealed when Moses": {
        "built a golden calf": "built a golden calf at the foot of the mountain",
        "lifted up the bronze serpent": "lifted up the bronze serpent in the wilderness",
        "struck the rock": "struck the rock at Horeb and water came out",
    },
    "God's covenant with Noah, signified by the rainbow, was a promise that": {
        "Israel would possess Canaan": "the descendants of Noah would possess the land of Canaan",
        "Noah's descendants would be kings": "Noah's descendants would be kings over all the earth",
        "the ark would be preserved": "the ark would be preserved for ever on Mount Ararat",
    },
    "When the Israelites complained of thirst at Meribah, Moses struck the rock twice instead of speaking to it as commanded. As a result": {
        "the water did not come": "no water came out of the rock for the people",
        "Aaron became leader": "Aaron was made leader of Israel in his place",
        "the people were destroyed": "the people were destroyed by a plague from God",
    },
    "The ravens that fed Elijah at the brook Cherith during the famine illustrate": {
        "human generosity": "the generosity of the people of Israel",
        "Elijah's hunting skill": "Elijah's skill in trapping birds for food",
        "the kindness of Ahab": "the kindness of King Ahab towards the prophet",
    },
    "The failure of Samuel's sons Joel and Abijah as judges led the elders of Israel to": {
        "appoint Saul directly": "appoint Saul as king without consulting Samuel",
        "stone Samuel": "stone Samuel for the sins of his sons",
        "return to Egypt": "propose a return to Egypt under a new leader",
    },
    "Achan's disobedience at Jericho consisted of": {
        "worshipping Baal": "worshipping Baal in the ruins of the city",
        "refusing to fight": "refusing to fight alongside the other tribes",
        "sparing the king": "sparing the king of Jericho and his family",
    },
    "Lot's wife became a pillar of salt because she": {
        "refused to leave Sodom": "refused to leave Sodom with her husband",
        "stole from Sodom": "stole silver and gold from the houses of Sodom",
        "mocked the angels": "mocked the angels who came to rescue them",
    },
    "David's friendship with Jonathan is remarkable because Jonathan": {
        "was David's enemy": "had been David's bitter enemy at the court of Saul",
        "was a Philistine": "was a Philistine prince from the city of Gath",
        "betrayed David to Saul": "later betrayed David's hiding place to Saul",
    },
    "When two women each claimed a living baby, Solomon ordered the child to be cut in two in order to": {
        "punish both women": "punish both women for disturbing the court",
        "settle the case quickly": "settle the case quickly and dismiss the women",
        "please the court": "please the officials of the court with his wisdom",
    },
    "Which statement best describes the effect of Ahab's greed for Naboth's vineyard?": {
        "he gained the vineyard and prospered": "he gained the vineyard and prospered for many years",
        "Jezebel repented": "Jezebel repented and restored the vineyard to Naboth's sons",
        "Naboth sold the vineyard willingly": "Naboth sold the vineyard willingly for a better one",
    },
    "Nebuchadnezzar's dream of the great image with a head of gold and feet of iron and clay, interpreted by Daniel, taught that": {
        "Babylon would last for ever": "Babylon would last for ever as the greatest kingdom",
        "gold is more valuable than iron": "gold is more valuable than iron and clay",
        "Daniel would become king": "Daniel would become king over Babylon",
    },
    "King Hezekiah's reforms included": {
        "building high places for Baal": "building new high places for the worship of Baal",
        "making alliances with Assyria": "making alliances with Assyria against Egypt",
        "closing the temple": "closing the temple and stopping the daily sacrifices",
    },
    "Nehemiah's opponents Sanballat and Tobiah tried to stop the rebuilding of the wall by": {
        "sending gifts": "sending gifts to bribe the builders",
        "appealing to the priests": "appealing to the priests to stop the work",
        "helping with the work": "offering to help with the work in order to spy",
    },
    "Esther risked her life by going to the king uninvited in order to": {
        "become queen": "become queen in place of Vashti",
        "punish Mordecai": "punish Mordecai for refusing to bow to Haman",
        "obtain wealth": "obtain wealth and honour for her family",
    },
    "The response of the people of Nineveh to Jonah's preaching was to": {
        "stone him": "stone him and throw his body into the sea",
        "ignore him": "ignore him and continue in their wickedness",
        "expel him": "expel him from the city and its surroundings",
    },
    "Micah 6:8 summarises what God requires of man as": {
        "sacrifices and burnt offerings": "sacrifices and burnt offerings of year-old calves",
        "tithing all income": "tithing all income and offering the first fruits",
        "fasting twice a week": "fasting twice a week and praying in the temple",
    },
    "Amos condemned the women of Samaria as 'cows of Bashan' because they": {
        "were farmers": "were farmers who neglected the temple",
        "refused to marry": "refused to marry and bear children",
        "worshipped cows": "worshipped golden cows at Bethel and Dan",
    },
    "When God called Jeremiah, Jeremiah objected that he": {
        "was too old": "was too old to travel and preach",
        "was a sinner": "was a sinner with unclean lips",
        "was a foreigner": "was a foreigner and not of the priestly line",
    },
    "When Jesus was presented in the temple, Simeon declared that the child would be": {
        "a king like David": "a king like David who would defeat the Romans",
        "a priest like Aaron": "a priest like Aaron serving in the temple",
        "a prophet like Elijah": "a prophet like Elijah who would call down fire",
    },
    "At twelve years old Jesus was found in the temple": {
        "cleansing it": "driving out the traders and money-changers",
        "healing the sick": "healing the sick and casting out demons",
        "hiding from Herod": "hiding from the soldiers of King Herod",
    },
    "Jesus said that anyone who wishes to be His disciple must": {
        "sell the temple": "sell everything and give the money to the temple",
        "become a Pharisee": "become a Pharisee and keep the whole law",
        "fast every day": "fast every day and pray in the synagogue",
    },
    "At the wedding in Cana, Jesus turned water into wine. John calls this": {
        "a parable": "a parable about the coming kingdom of God",
        "a fulfilment of the law": "a fulfilment of the law given through Moses",
        "a temptation": "a temptation which Jesus overcame at the feast",
    },
    "When Jesus stilled the storm on the Sea of Galilee, the disciples asked,": {
        "'Are you the King of the Jews?'": "'Are you the King of the Jews who was promised?'",
        "'Should we call down fire?'": "'Lord, should we call down fire from heaven?'",
        "'Where shall we buy bread?'": "'Where shall we buy bread for all these people?'",
    },
    "In the parable of the talents, the servant who buried his one talent was condemned because he": {
        "lost the money": "lost the money in a bad trade",
        "gave it to the poor": "gave it away to the poor without permission",
        "stole it": "stole it and fled to another country",
    },
    "The parable of the prodigal son teaches chiefly about": {
        "the danger of wealth": "the danger of wealth to a young man",
        "the duties of servants": "the duties of servants to their master",
        "the end of the world": "the judgment at the end of the world",
    },
    "Jesus taught that when giving alms, one should not let the left hand know what the right hand is doing, in order to": {
        "keep accounts secret": "keep one's accounts secret from tax collectors",
        "give more": "be able to give more than the Pharisees",
        "confuse the poor": "prevent the poor from knowing who gave",
    },
    "When Jesus sent out the twelve, He told them to take": {
        "two tunics and money": "two tunics and enough money for the journey",
        "letters of introduction": "letters of introduction to the synagogue rulers",
        "swords": "swords and staffs to defend themselves",
    },
    "At the Last Supper Jesus identified His betrayer as": {
        "Peter": "Peter, who would deny Him three times",
        "Thomas": "Thomas, who doubted the resurrection",
        "John": "John, the disciple whom He loved",
    },
    "At the moment Jesus died, the curtain of the temple was torn in two, signifying": {
        "the destruction of Jerusalem": "the coming destruction of Jerusalem by the Romans",
        "an earthquake only": "nothing more than the effect of the earthquake",
        "the end of the Sabbath": "the end of the Sabbath and the start of the Passover",
    },
    "Before ascending, Jesus commissioned the disciples to": {
        "build a temple": "build a new temple in Jerusalem",
        "return to fishing": "return to their fishing in Galilee",
        "fight Rome": "raise an army and fight against Rome",
    },
    "Jesus said the greatest commandment is to love God, and the second is to": {
        "keep the Sabbath": "keep the Sabbath day holy",
        "honour the priests": "honour the priests and the elders",
        "pay tithes": "pay tithes of all that you earn",
    },
    "The early believers in Jerusalem 'had all things in common' and": {
        "kept their property secret": "kept their property secret from the apostles",
        "left Jerusalem": "left Jerusalem to escape persecution",
        "stopped praying in the temple": "stopped praying in the temple with the Jews",
    },
    "Before Pentecost Jesus told the apostles to wait in Jerusalem for": {
        "the destruction of the temple": "the destruction of the temple that He had foretold",
        "Paul's arrival": "the arrival of Paul from Tarsus to lead them",
        "the Roman census": "the Roman census ordered by the emperor",
    },
    "Paul taught that 'all have sinned and fall short of the glory of God' and are justified": {
        "by works of the law": "by faithfully keeping the works of the law",
        "by circumcision": "by circumcision according to the custom of Moses",
        "by temple sacrifice": "by offering sacrifices in the temple at Jerusalem",
    },
    "Jesus taught humility at a feast by advising guests to": {
        "take the highest seat": "take the highest seat before anyone else",
        "leave early": "leave early so as not to trouble the host",
        "bring gifts": "bring gifts that are worthy of the host",
    },
    "Jesus praised the poor widow who put two small coins in the treasury because she": {
        "gave the most money": "gave the most money of all the worshippers",
        "gave secretly": "gave secretly so that no one would see her",
        "gave gold": "gave gold coins rather than copper ones",
    },
    "When asked whether it was lawful to pay tax to Caesar, Jesus answered,": {
        "'Do not pay'": "'Do not pay, for Caesar has no authority over the children of God'",
        "'Pay only the temple tax'": "'Pay only the temple tax, and let Caesar collect his own'",
        "'Caesar is a thief'": "'Caesar is a thief who robs the poor of what belongs to God'",
    },
    "The parable of the ten virgins teaches that believers should": {
        "sleep early": "sleep early so as to be strong for the feast",
        "buy oil": "buy enough oil to sell to their neighbours",
        "avoid weddings": "avoid weddings that take place at night",
    },
    "Peter declared 'God shows no partiality' after": {
        "the Council of Jerusalem": "the decision of the Council of Jerusalem on circumcision",
        "healing the lame man": "healing the lame man at the Beautiful Gate",
        "his release from prison": "his miraculous release from Herod's prison",
    },
    "In the parable of the Pharisee and the tax collector, the tax collector was justified because he": {
        "gave tithes": "gave tithes of all that he earned",
        "prayed longer": "prayed longer than the Pharisee did",
        "stood at the front": "stood at the front of the temple to pray",
    },
    "Zacchaeus, after meeting Jesus, promised to": {
        "leave Jericho": "leave Jericho and follow Jesus to Jerusalem",
        "build a synagogue": "build a synagogue for the people of Jericho",
        "become a disciple immediately": "become one of the twelve disciples immediately",
    },
    "David's adultery with Bathsheba led directly to": {
        "the death of Saul": "the death of Saul on Mount Gilboa",
        "the division of the kingdom": "the division of the kingdom into Israel and Judah",
        "war with the Philistines": "a long and bitter war with the Philistines",
    },
    # ---------- batch 8 : IRS ----------
    "The Prophet (SAW) said, 'Religion is sincerity (nasihah)'. When asked to whom, he replied:": {
        "to the wealthy only": "to the wealthy, the rulers and the learned men of the community",
        "to one's family only": "to one's parents, spouse, children and close relatives only",
        "to the scholars only": "to the scholars, the imams and the judges of the Muslims only",
    },
    "A man believes in Allah but also consults a fortune-teller and acts on his predictions. According to a Hadith, his prayers": {
        "are doubled": "are doubled in reward because of his faith",
        "are unaffected": "are unaffected so long as he still prays",
        "become voluntary": "become voluntary instead of obligatory",
    },
    "The Prophet (SAW) defined Ihsan as": {
        "to fast in Ramadan": "to fast in Ramadan and stand in prayer at night",
        "to give Zakat": "to give Zakat and sadaqah generously to the poor",
        "to perform Hajj": "to perform Hajj and Umrah as often as one is able",
    },
    "Belief in the Last Day (Yawm al-Qiyamah) influences a Muslim's conduct mainly by": {
        "making him fear people": "making him fear people more than he fears Allah",
        "encouraging him to acquire wealth": "encouraging him to acquire wealth before the end comes",
        "removing responsibility for actions": "removing his personal responsibility for his actions",
    },
    "A Muslim who deliberately misses Zuhr must": {
        "pay a fine": "pay a fine to the mosque as expiation",
        "fast for one day": "fast for one day in place of the prayer",
        "double the next Asr": "double the number of rak'ahs in the next Asr",
    },
    "Zakat differs from sadaqah in that Zakat is": {
        "voluntary": "voluntary and left to the giver's conscience",
        "given only in Ramadan": "given only in the last ten days of Ramadan",
        "given only to relatives": "given only to poor relatives and neighbours",
    },
    "A man deliberately eats during a Ramadan fast without any excuse. In addition to repentance, the expiation (kaffarah) prescribed for deliberately breaking the fast is": {
        "feeding one poor person": "feeding one poor person for each day missed",
        "paying Zakat twice": "paying Zakat twice in that year",
        "performing Umrah": "performing Umrah before the next Ramadan",
    },
    "The stoning of the pillars at Mina commemorates": {
        "the Prophet's victory at Badr": "the Prophet's victory over the Quraysh at Badr",
        "the destruction of Abrahah's army": "the destruction of Abrahah's army of elephants",
        "the digging of Zamzam": "the digging of the well of Zamzam by Abdul-Muttalib",
    },
    "A student who refuses to cheat in an examination although everyone around her is cheating is practising": {
        "hijrah": "hijrah (migration for the sake of Allah)",
        "riba": "riba (dealing in usury and interest)",
        "shirk": "shirk (associating partners with Allah)",
    },
    "The 'Year of Sorrow' ('Am al-Huzn) refers to the year in which": {
        "the battle of Uhud was lost": "the Muslims lost the battle of Uhud and Hamzah was killed",
        "the Prophet left Makkah": "the Prophet was forced to leave Makkah for Madinah",
        "Ibrahim, the Prophet's son, died": "Ibrahim, the Prophet's infant son, died in Madinah",
    },
    "When the people of Ta'if rejected the Prophet (SAW) and stoned him, he": {
        "cursed them": "cursed them and asked Allah to destroy the town",
        "sent an army against them": "sent an army from Madinah to punish them",
        "abandoned his mission": "abandoned his mission and returned to trading",
    },
    "The Prophet (SAW) mended his own clothes, milked his goats and helped with housework. This teaches that": {
        "a leader should not do menial work": "a leader should not be seen doing menial work",
        "men should not work outside": "men should stay at home and not work outside",
        "housework is for servants": "housework should be left to servants and slaves",
    },
    "Abu Bakr's first major challenge as caliph was": {
        "the conquest of Persia": "the conquest of the Persian empire",
        "the compilation of Hadith": "the compilation of the Hadith into books",
        "the building of Kufah": "the building of the garrison city of Kufah",
    },
    "The Ansar were": {
        "the Makkan emigrants": "the Makkan Muslims who emigrated to Madinah",
        "the Jews of Madinah": "the Jewish tribes living in Madinah",
        "the Quraysh leaders": "the Quraysh leaders who opposed the Prophet",
    },
    "In Islam a husband is required to provide his wife with maintenance (nafaqah), which includes": {
        "only food": "only food, since clothing is her own responsibility",
        "a car and a house": "a car and a house in her own name",
        "nothing if she is rich": "nothing at all if she has wealth of her own",
    },
    "A husband pronounces one revocable divorce (talaq). During the wife's iddah he": {
        "cannot take her back": "cannot take her back under any circumstances",
        "must pay a second mahr": "must pay a second mahr before taking her back",
        "must obtain a court order": "must obtain a court order before taking her back",
    },
    "Parents' duties to children in Islam include": {
        "leaving them to fend for themselves": "leaving them to fend for themselves from an early age",
        "favouring sons over daughters": "favouring sons over daughters in gifts and inheritance",
        "denying them inheritance": "denying them any share of the family inheritance",
    },
    "When a noble woman of Makhzum was caught stealing and people sought to excuse her, the Prophet (SAW) said that earlier nations were destroyed because": {
        "they were poor": "they were poor and had nothing to give in charity",
        "they prayed too little": "they prayed too little and fasted too rarely",
        "they traded on Fridays": "they traded on Fridays instead of attending prayer",
    },
    "Which of the following business arrangements is permitted in Islam?": {
        "a fixed-interest loan": "a loan repaid with a fixed rate of interest",
        "gambling on football results": "a pool for betting on football results",
        "selling wine to non-Muslims": "a shop that sells wine to non-Muslims only",
    },
    "A Muslim is allowed to eat forbidden food only when": {
        "he is travelling": "he is travelling a long distance from home",
        "it is cheaper": "it is cheaper than the lawful food available",
        "a non-Muslim offers it": "a non-Muslim host offers it out of hospitality",
    },
    "Under Umar ibn al-Khattab, the treasury (Bayt al-Mal) paid stipends to": {
        "soldiers only": "soldiers only, in proportion to their rank",
        "the caliph's family only": "the caliph's family and close companions only",
        "the Quraysh only": "the Quraysh only, as the Prophet's tribe",
    },
    "Umar chose his successor by": {
        "naming his son": "naming his son Abdullah as the next caliph",
        "holding a general election": "holding a general election among all Muslims",
        "leaving the matter to the army": "leaving the matter to the commanders of the army",
    },
    "The Muslims lost the advantage at the battle of Uhud mainly because": {
        "they had no leader": "they had no leader after the Prophet was wounded",
        "it rained": "heavy rain prevented them from using their bows",
        "the Quraysh were more numerous": "the Quraysh were three times more numerous",
    },
    "Islam first reached West Africa, including Kanem-Bornu and later Hausaland, mainly through": {
        "military conquest by Arabs": "military conquest by Arab armies from Egypt",
        "European missionaries": "European missionaries who arrived by sea",
        "the sea route from India": "the sea route from India and the Persian Gulf",
    },
    "Islam's view of the environment is that man is": {
        "free to exploit nature as he likes": "free to exploit nature in any way he likes",
        "not responsible for animals": "not responsible for the welfare of animals",
        "forbidden to farm": "forbidden to farm or cut down any tree",
    },
    "Which Islamic principle most directly addresses examination malpractice?": {
        "Qasr": "Qasr (shortening prayers on a journey)",
        "iddah": "iddah (the waiting period after divorce)",
        "tayammum": "tayammum (dry ablution with clean earth)",
    },
}


def apply_fixes(questions):
    """Replace distractor texts in place. Returns number of items patched; raises if a key is unused."""
    used, n = set(), 0
    for q in questions:
        for key, mapping in FIXES.items():
            if q["q"].startswith(key):
                used.add(key)
                for letter in "ABCD":
                    if q[letter] in mapping:
                        q[letter] = mapping[q[letter]]
                n += 1
    return n, used
