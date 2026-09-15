"""Builds content/batch_011_english_round4.json — Use of English, round 4 (more passages + lexis).

Run:  python3 scripts/build_content_batch11.py
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_content_batch1 import _balance  # noqa: E402
from distractor_fixes import apply_fixes  # noqa: E402

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "content", "batch_011_english_round4.json")

COMP_P = [
    ("C9", "The night market",
     "The night market on Akpakpava Road opens when the shops close. By eight o'clock the pavement has become a "
     "kitchen: charcoal glows under grills of suya and roasted plantain, pots of pepper soup steam beside pyramids of "
     "boiled groundnuts, and the air smells of smoke, onions and diesel from the generators that light the stalls. "
     "Office workers who left home at five in the morning stop here on their way back, not only because the food is "
     "cheap but because the market is the one place where a clerk and a director will stand shoulder to shoulder, "
     "waiting for the same woman to turn the same skewers.\n\n"
     "The council has tried twice to close it, citing hygiene and traffic. Both attempts failed within a fortnight. "
     "The traders simply returned, and the customers with them; the inspectors, who ate there themselves, found it "
     "hard to be zealous. A more sensible approach has since emerged: the council now collects a small nightly levy, "
     "provides two waste skips and a water tanker, and looks the other way.\n\n"
     "It is an untidy arrangement, and purists on both sides dislike it. But it feeds thousands, employs hundreds, "
     "and has produced, without anyone planning it, the most democratic dining room in the city."),
    ("C10", "The lost art of letter-writing",
     "My grandfather kept every letter he ever received in a tin trunk under his bed. When he died we found more than "
     "six hundred of them, tied in bundles by year: letters from his brother in the army, from a friend who had gone "
     "to study in London, from my grandmother during the two years they were engaged and living in different towns. "
     "Reading them, I was struck less by the news they contained than by the care with which it was told. Each letter "
     "began with enquiries about health and harvest, moved through its business in orderly paragraphs, and closed "
     "with greetings to a dozen named people.\n\n"
     "Nobody writes like that now. We send messages of a line or two, dozens a day, and keep none of them. The "
     "speed is a blessing; a grandmother in Kaduna can hear of a birth in Lagos within the hour. But something has "
     "been lost with the slowness. A letter that would take a week to arrive was written by someone who had thought "
     "about what was worth saying. A message that arrives in a second is often written by someone who has not.\n\n"
     "I do not suggest that we abandon our phones. I suggest only that once in a while we write something long "
     "enough to be worth keeping in a tin trunk."),
    ("C11", "Counterfeit drugs",
     "The tablets looked exactly right. The packaging carried the manufacturer's logo, a batch number and an expiry "
     "date two years away. Only the price gave them away: half what the pharmacy across the road was charging. The "
     "woman who bought them for her feverish child did not know that they contained chalk and a little paracetamol, "
     "and that the malaria they were supposed to cure would continue, unchecked, for another five days.\n\n"
     "Fake medicines kill more people in Africa each year than road accidents, yet they attract a fraction of the "
     "attention. Part of the reason is that their victims rarely know what killed them; a child who dies of malaria "
     "after taking 'medicine' is recorded as a malaria death. Part is that the trade is enormously profitable and "
     "its punishments, where they exist, are light. A drug counterfeiter in some states faces a smaller fine than a "
     "driver who ignores a traffic light.\n\n"
     "Technology now offers some defence. Scratch panels on genuine packs reveal a code which, sent by text message, "
     "confirms the product is authentic. But the system depends on buyers who know it exists and can afford the "
     "text. The deeper cure is cheaper: a market in which the real drug is not twice the price of the fake, and a "
     "law that treats the sale of chalk to a sick child as the crime it is."),
    ("C12", "Aunty Rose's scholarship",
     "Aunty Rose was not really my aunt. She was the woman who sold bread at the junction near our school, and she "
     "had adopted, in the loose way of Nigerian streets, every child who passed her table. She knew our names, our "
     "classes and, somehow, our results. A child who had done well would find an extra roll slipped into his bag; one "
     "who had failed would receive a long look and the words, 'Next term, eh?'\n\n"
     "The year I sat the entrance examination for the federal school, my father lost his job. The fees for the first "
     "term were beyond us, and I had resigned myself to the local secondary school when Aunty Rose appeared at our "
     "door with an envelope. It contained the exact sum, in old notes that smelt of flour. She would not say where "
     "it had come from and refused every suggestion of repayment. 'When you are big,' she said, 'you will do it for "
     "somebody else.'\n\n"
     "She died the year I graduated. At her funeral I counted eleven people who had received envelopes, though I "
     "suspect there were more. None of us had known about the others. Between us we now pay the school fees of "
     "twenty-three children in that town, and not one of them knows our names."),
    ("C13", "On lateness",
     "There is a joke in this country that Nigerians operate on 'African time', a private clock that runs an hour or "
     "two behind the one on the wall. Like many jokes, it conceals a cost. A meeting called for ten that begins at "
     "eleven-thirty has wasted ninety minutes of every person in the room, and the person who arrives last has, in "
     "effect, stolen that time from all the others.\n\n"
     "Lateness is rarely about traffic, whatever the latecomer says. It is about power. The important man arrives "
     "last because he can; the junior arrives first because he must. In many offices the meeting does not start "
     "until the most senior person walks in, which means that the more senior one becomes, the less reason one has "
     "to be punctual. Habits formed this way flow downwards, until the office messenger, too, has learnt that ten "
     "o'clock means whenever he arrives.\n\n"
     "Countries that have broken this habit did not do it through appeals to culture but through consequence. "
     "Meetings begin on time whether or not the chairman is present; latecomers find the door closed or the "
     "decision taken. When lateness stops being a display of importance and becomes merely an embarrassment, the "
     "private clock quietly resets itself."),
    ("C14", "The last blacksmith",
     "Baba Ogundipe is the last blacksmith in a town that once had forty. His forge, a low shed of blackened zinc "
     "behind the motor park, produces hoes, cutlasses and the curved knives that palm-wine tappers use, and he makes "
     "them exactly as his father did, with a hand-pumped bellows and a hammer whose handle has been replaced so "
     "many times that he cannot say how old it is.\n\n"
     "The imported tools that put his rivals out of business are cheaper, and he does not pretend otherwise. His "
     "customers are the farmers who have learnt that a Chinese cutlass, bright and light, loses its edge in a "
     "season, while one of his, dull and heavy, will outlast its owner. They pay twice as much and come back once a "
     "decade, which, as he observes with a dry smile, is a poor business model but an honest one.\n\n"
     "He has trained three apprentices. Two left for Lagos; the third, his grandson, works beside him and has begun "
     "to sell the knives online, photographed against a white sheet, to buyers in Europe who pay ten times the local "
     "price for what they call 'artisanal' blades. Baba Ogundipe finds the word amusing. 'They are farm tools,' he "
     "says. 'But if the white man wants to hang his hoe on the wall, let him pay for it.'"),
]

COMP = [
    ("C9", "Medium", "The pavement is described as having 'become a kitchen' because", "the council built a kitchen there", "food is cooked and sold openly on it every night", "the traders sleep there", "it is cleaned every evening", "B", "The paragraph describes grills, pots and stalls cooking on the pavement."),
    ("C9", "Medium", "Office workers stop at the market mainly because", "it lies on the only road that leads home", "the food is cheap and all classes mix there freely", "the shops have all closed by that time", "the council has ordered them to eat there", "B", "'Not only because the food is cheap but because ... a clerk and a director will stand shoulder to shoulder.'"),
    ("C9", "Medium", "The council's attempts to close the market failed partly because", "the traders bribed the inspectors", "the inspectors themselves ate at the market", "the governor intervened", "the customers protested violently", "B", "'The inspectors, who ate there themselves, found it hard to be zealous.'"),
    ("C9", "Hard", "'looks the other way' as used in the passage means that the council", "faces the opposite direction from the market", "deliberately ignores the market's irregularities", "has moved its offices to another street", "supervises the market closely every night", "B", "To look the other way is to pretend not to notice something wrong."),
    ("C9", "Medium", "The writer calls the market 'the most democratic dining room in the city' because", "people of the town vote there", "people of all ranks eat there together as equals", "the council runs it for the people", "the food is served free of charge", "B", "This echoes the earlier image of the clerk and the director standing shoulder to shoulder."),

    ("C10", "Medium", "The grandfather's letters were arranged", "alphabetically", "in bundles according to year", "by the name of the sender", "randomly in a trunk", "B", "'Tied in bundles by year.'"),
    ("C10", "Medium", "What impressed the writer most about the letters was", "the news that they contained", "the care with which they were written", "their remarkable length", "the fine quality of the paper", "B", "'Struck less by the news ... than by the care with which it was told.'"),
    ("C10", "Medium", "According to the writer, the main advantage of modern messages is their", "cheapness", "speed", "length", "privacy", "B", "'The speed is a blessing' — the Kaduna/Lagos example illustrates it."),
    ("C10", "Hard", "The writer believes that a letter written slowly was usually", "full of errors", "more thoughtful about what was worth saying", "written by an educated person", "delivered late", "B", "'Written by someone who had thought about what was worth saying.'"),
    ("C10", "Medium", "The writer's final recommendation is that we should", "stop using our phones altogether", "occasionally write something long and worth keeping", "buy tin trunks for our letters", "keep every text message we receive", "B", "'Once in a while we write something long enough to be worth keeping in a tin trunk.'"),

    ("C11", "Medium", "The only sign that the tablets were fake was", "the missing logo", "the unusually low price", "the wrong batch number", "the colour of the tablets", "B", "'Only the price gave them away: half what the pharmacy across the road was charging.'"),
    ("C11", "Medium", "Deaths from fake drugs receive little attention partly because", "they are recorded as deaths from the disease itself", "they occur only in remote villages", "the government deliberately hides the figures", "the drugs are legal in most states", "A", "'A child who dies of malaria after taking \"medicine\" is recorded as a malaria death.'"),
    ("C11", "Medium", "The writer compares the punishment for drug counterfeiting with that for", "murder", "ignoring a traffic light", "smuggling", "tax evasion", "B", "The comparison shows how light the penalties are."),
    ("C11", "Hard", "The weakness of the scratch-panel system is that it", "does not work on most phones", "relies on buyers knowing about it and affording the text", "is easily copied by the counterfeiters", "takes too long to send a reply", "B", "'The system depends on buyers who know it exists and can afford the text.'"),
    ("C11", "Medium", "By 'the deeper cure' the writer means", "a stronger drug against malaria fever", "fair prices for real drugs, plus real punishment", "more scratch panels on every packet", "better-equipped hospitals in the villages", "B", "The final sentence spells out these two remedies."),

    ("C12", "Medium", "The writer says Aunty Rose 'was not really my aunt' in order to", "criticise her", "explain that she was a family friend, not a relation", "show that she was a stranger to everyone", "suggest she lied about her identity", "B", "The passage explains the loose street sense in which children called her aunty."),
    ("C12", "Medium", "The words 'Next term, eh?' show that Aunty Rose", "was angry with children who failed", "encouraged children to do better without scolding them", "did not care about examination results", "expected failing children to leave school", "B", "A 'long look' followed by gentle encouragement."),
    ("C12", "Medium", "The notes in the envelope 'smelt of flour' because", "they had been hidden in a bakery", "they came from Aunty Rose's bread earnings", "they were counterfeit", "the envelope was dirty", "B", "The detail links the money to her trade as a bread seller."),
    ("C12", "Hard", "The final paragraph shows that Aunty Rose's kindness", "was wasted", "has multiplied through the people she helped", "was limited to eleven children", "was eventually repaid to her", "B", "Eleven beneficiaries now sponsor twenty-three children anonymously, as she did."),
    ("C12", "Medium", "The sponsored children do not know their sponsors' names because the sponsors", "are ashamed of their own poverty", "are following Aunty Rose's example of anonymous giving", "live abroad and rarely visit", "are afraid of being asked for more money", "B", "Aunty Rose refused to say where the money came from; her beneficiaries copy that."),

    ("C13", "Medium", "According to the writer, the latecomer to a meeting has in effect", "saved everyone's time", "stolen time from everyone else present", "shown respect to the chairman", "avoided a long and boring meeting", "B", "The passage says the last arrival has 'in effect, stolen that time from all the others'."),
    ("C13", "Medium", "The writer claims that lateness is really about", "traffic", "power", "laziness", "culture", "B", "The second paragraph states plainly: 'Lateness is rarely about traffic ... It is about power.'"),
    ("C13", "Hard", "The expression 'flow downwards' suggests that bad habits", "are washed away by rain", "spread from senior people to junior ones", "are caused by heavy rain", "disappear with the passage of time", "B", "Habits formed by senior staff are copied down the hierarchy to the messenger."),
    ("C13", "Medium", "Countries that solved the problem did so by", "appealing to culture", "imposing consequences for lateness", "employing more messengers", "starting meetings later", "B", "'Not through appeals to culture but through consequence.'"),
    ("C13", "Medium", "'The private clock quietly resets itself' means that", "people buy new watches", "people become punctual without being forced", "meetings are cancelled", "clocks are adjusted by the government", "B", "Once lateness is an embarrassment rather than a display of status, punctuality follows naturally."),

    ("C14", "Medium", "The hammer's age cannot be stated because", "it was bought abroad", "its handle has been replaced many times", "Baba Ogundipe has forgotten", "it belonged to his grandfather", "B", "'A hammer whose handle has been replaced so many times that he cannot say how old it is.'"),
    ("C14", "Medium", "Farmers prefer Baba Ogundipe's cutlasses because they", "are cheaper", "keep their edge far longer", "are lighter", "are brighter", "B", "The imported cutlass 'loses its edge in a season'; his 'will outlast its owner'."),
    ("C14", "Hard", "Baba Ogundipe calls his trade 'a poor business model but an honest one' because", "he cheats his customers quite openly", "his tools last so long that buyers rarely return", "he sells every single tool at a loss", "he pays no tax at all to the council", "B", "Customers 'come back once a decade' — good for them, bad for sales."),
    ("C14", "Medium", "The grandson has found new customers by", "opening a shop in Lagos", "selling the knives online to buyers abroad", "lowering the prices of the knives", "importing cheaper Chinese blades", "B", "He photographs the knives and sells them to buyers in Europe."),
    ("C14", "Medium", "Baba Ogundipe's final remark shows that he is", "angry with foreign buyers", "amused, but glad to profit from the foreign interest", "ashamed of his simple tools", "planning to stop making hoes altogether", "B", "'If the white man wants to hang his hoe on the wall, let him pay for it' is said with humour."),
]

CLOZE_P = [
    ("Z9", "Cloze passage: The interview",
     "Yemi arrived at the company's office forty minutes early, [1] that the traffic on Third Mainland Bridge might "
     "delay her. She had spent the previous evening [2] the firm's website and could name its directors, its "
     "products and the award it had won the year before. The receptionist showed her to a chair and asked her to "
     "[3]. Three other candidates were already waiting, each [4] a folder of certificates. When her name was "
     "called, Yemi stood, [5] her jacket and walked in with a confidence she did not entirely feel. The panel "
     "consisted of two men and a woman, who [6] her with a series of questions about why she wanted the job. She "
     "answered each one honestly, admitting when she did not know something rather than [7] to guess. Towards the "
     "end the woman asked what Yemi expected to be [8] and, when Yemi named a figure, raised an eyebrow but wrote "
     "it down. The letter of [9] arrived a week later. It offered slightly less than she had asked for, which, as "
     "her father pointed out, meant that she had asked for exactly the [10] amount."),
    ("Z10", "Cloze passage: The harmattan",
     "Every December the harmattan arrives from the Sahara, a dry wind [1] with fine dust that turns the noon sky the "
     "colour of weak tea. Visibility falls so sharply that flights are [2] and drivers switch on their headlamps at "
     "midday. Lips crack, skin turns grey and the water in the pot is cold enough at dawn to make bathing an act of "
     "[3]. Yet the season has its pleasures. The nights are cool and free of mosquitoes; the dust [4] the sun so that "
     "one can look directly at it as it sets; and the dryness means that clothes washed in the morning are stiff and "
     "ready by noon. Farmers, [5], watch the wind with anxiety. A single spark in the [6] grass can start a fire "
     "that races across a farm faster than a man can run, and every year the newspapers report villages [7] to "
     "ash. The elders say the harmattan was once milder and shorter, and the scientists, for once, [8] with them: "
     "as the desert advances southward, the wind that carries its dust reaches [9] each year and stays longer. "
     "Whether anything can be done about it is a question [10] which nobody in the village has an answer."),
    ("Z11", "Cloze passage: The school debate",
     "The motion before the house was that 'boarding schools produce better citizens than day schools', and the "
     "hall was [1] with students who had strong views on the matter. The first speaker for the motion argued that "
     "boarding schools teach independence, since a child who must wash his own clothes and manage his own pocket "
     "money [2] responsibility early. His opponent replied that the same child also learns bullying, hunger and "
     "the art of [3] rules, and that many of the country's most notorious criminals were products of famous "
     "boarding houses. The audience [4] loudly at this. The second speaker for the motion, [5] by the noise, "
     "produced statistics showing that boarders scored higher in national examinations, only to be told that "
     "boarding schools [6] the best students in the first place and could hardly claim credit for their success. "
     "By the time the chairman called for a vote, both sides had [7] the topic thoroughly and neither had "
     "convinced the other. The motion was [8] by a narrow margin, which the losing side [9] to the fact that "
     "most of the audience were themselves boarders. The chairman, wisely, [10] to comment."),
    ("Z12", "Cloze passage: The pharmacist's advice",
     "Mrs Adebayo has run the pharmacy on Ring Road for twenty-two years and has [1] a rule that irritates some of "
     "her customers: she will not sell antibiotics [2] a prescription. Many people, she explains, treat antibiotics "
     "as a cure for everything from headaches to malaria, [3] the fact that these drugs act only on bacteria and do "
     "nothing against viruses or parasites. Worse, patients who feel better after two days often [4] the course, "
     "leaving the strongest bacteria alive to multiply and pass on their [5]. The result is that infections which "
     "were once cured by a cheap tablet now [6] expensive drugs that many families cannot afford. Mrs Adebayo "
     "keeps a chart on her wall showing how quickly a common bacterium has become resistant to three [7] "
     "antibiotics in the past decade, and she points to it whenever a customer [8]. Some walk out and buy the drugs "
     "at the roadside instead. Others, [9], listen, and she counts every one of them as a small victory in a war "
     "that, she says, humanity is presently [10]."),
]

CLOZE = {
    "Z9": [
        (1, "fearing", "hoping", "knowing", "forgetting", "A", "She arrived early 'fearing' (worried) that traffic might delay her."),
        (2, "studying", "designing", "building", "reading", "A", "'Studying the firm's website' — she learnt its details thoroughly."),
        (3, "wait", "leave", "sit", "sign", "A", "The receptionist asked her to wait; the other candidates were 'already waiting'."),
        (4, "clutching", "reading", "hiding", "opening", "A", "'Each clutching a folder' — holding tightly, a sign of nervousness."),
        (5, "straightened", "removed", "buttoned", "folded", "A", "One straightens one's jacket before walking into an interview."),
        (6, "bombarded", "attacked", "greeted", "confused", "A", "'Bombarded her with a series of questions' — asked many in quick succession."),
        (7, "pretending", "refusing", "trying", "hoping", "A", "'Rather than pretending to guess' contrasts honesty with bluffing."),
        (8, "paid", "asked", "given", "offered", "A", "'What Yemi expected to be paid' — her salary expectation."),
        (9, "appointment", "invitation", "apology", "complaint", "A", "A 'letter of appointment' is the standard term for a job offer letter."),
        (10, "right", "wrong", "same", "lowest", "A", "Her father's point: an offer slightly below the request means the request was pitched correctly."),
    ],
    "Z10": [
        (1, "laden", "filled", "loaded", "packed", "A", "'A dry wind laden with fine dust' — the literary collocation."),
        (2, "cancelled", "delayed", "diverted", "grounded", "A", "Poor visibility leads to flights being cancelled."),
        (3, "courage", "faith", "madness", "duty", "A", "Cold water at dawn makes bathing 'an act of courage' — humorous exaggeration."),
        (4, "softens", "hides", "blocks", "reflects", "A", "The dust softens the sun so that one can look at it directly."),
        (5, "however", "therefore", "moreover", "meanwhile", "A", "'However' marks the contrast between the pleasures and the farmers' anxiety."),
        (6, "dry", "green", "tall", "wet", "A", "A spark in dry grass starts a fire."),
        (7, "reduced", "burnt", "turned", "set", "A", "'Villages reduced to ash' is the standard expression."),
        (8, "agree", "argue", "differ", "compete", "A", "'The scientists, for once, agree with them' — 'for once' implies they usually disagree."),
        (9, "further", "farther", "faster", "earlier", "A", "The wind reaches further (south) each year as the desert advances."),
        (10, "to", "for", "of", "at", "A", "'A question to which nobody has an answer' — 'an answer to a question'."),
    ],
    "Z11": [
        (1, "packed", "empty", "filled", "decorated", "A", "'The hall was packed with students' — very crowded."),
        (2, "learns", "avoids", "forgets", "teaches", "A", "The child 'learns responsibility early'."),
        (3, "breaking", "making", "obeying", "reading", "A", "The opponent lists negative lessons: 'the art of breaking rules'."),
        (4, "cheered", "wept", "yawned", "sang", "A", "The audience cheered loudly at the clever point."),
        (5, "undeterred", "frightened", "encouraged", "silenced", "A", "'Undeterred by the noise' — not put off; he continued with statistics."),
        (6, "admitted", "rejected", "trained", "failed", "A", "Boarding schools 'admitted the best students in the first place' — selection bias."),
        (7, "exhausted", "avoided", "ignored", "introduced", "A", "'Both sides had exhausted the topic' — discussed it fully."),
        (8, "carried", "defeated", "cancelled", "withdrawn", "A", "A motion that wins the vote is 'carried'."),
        (9, "attributed", "blamed", "objected", "admitted", "A", "'Attributed to the fact that' — explained the result by."),
        (10, "declined", "agreed", "began", "demanded", "A", "The chairman 'declined to comment' — the standard phrase."),
    ],
    "Z12": [
        (1, "enforced", "broken", "forgotten", "changed", "A", "She has 'enforced a rule' that irritates customers."),
        (2, "without", "with", "before", "after", "A", "She will not sell antibiotics without a prescription."),
        (3, "despite", "because of", "owing to", "considering", "A", "'Despite the fact that these drugs act only on bacteria' — contrast."),
        (4, "abandon", "complete", "repeat", "extend", "A", "Patients who feel better 'abandon the course' before it is finished."),
        (5, "resistance", "weakness", "disease", "cure", "A", "Surviving bacteria multiply and pass on their resistance."),
        (6, "require", "cure", "prevent", "produce", "A", "Such infections now 'require expensive drugs'."),
        (7, "common", "rare", "new", "cheap", "A", "Resistant to three common antibiotics — the ordinary ones."),
        (8, "objects", "pays", "leaves", "agrees", "A", "She points to the chart 'whenever a customer objects'."),
        (9, "fortunately", "surprisingly", "however", "sadly", "A", "'Others, fortunately, listen' — the positive contrast with those who walk out."),
        (10, "losing", "winning", "avoiding", "planning", "A", "A 'war that humanity is presently losing' — the theme of the passage is rising resistance."),
    ],
}

SI_STEM = "Choose the option that best explains the information conveyed in the sentence: "
SI = [
    ("The new bridge is a white elephant.", "The bridge is painted white", "The bridge cost a lot but is of little use", "The bridge is very large", "The bridge is admired by everyone", "B", "A 'white elephant' is an expensive possession that is useless or troublesome."),
    ("Kemi let the cat out of the bag about the surprise party.", "Kemi brought a cat to the party", "Kemi revealed the secret by mistake", "Kemi refused to attend the party", "Kemi organised the party", "B", "'Let the cat out of the bag' = reveal a secret."),
    ("The contractor is sitting on the fence about the project.", "The contractor has not decided which side to support", "The contractor has abandoned the project", "The contractor is resting at the site", "The contractor is guarding the project", "A", "'Sit on the fence' = avoid taking sides."),
    ("Uncle Dayo's business went to the dogs after his illness.", "Uncle Dayo started selling dogs", "Uncle Dayo's business declined badly", "Uncle Dayo's business was stolen", "Uncle Dayo moved his business", "B", "'Go to the dogs' = deteriorate badly."),
    ("The teacher turned a blind eye to the noise.", "The teacher could not see the noisy students", "The teacher deliberately ignored the noise", "The teacher punished the noisy students", "The teacher lost her sight", "B", "'Turn a blind eye' = pretend not to notice."),
    ("Obi is in hot water with the bank.", "Obi has a hot drink at the bank", "Obi is in trouble with the bank", "Obi works in the bank's kitchen", "Obi has a large deposit at the bank", "B", "'In hot water' = in trouble."),
    ("The two companies buried the hatchet last month.", "The companies hid their weapons", "The companies ended their quarrel", "The companies went bankrupt", "The companies merged", "B", "'Bury the hatchet' = make peace."),
    ("The examination was a piece of cake for Funmi.", "Funmi ate cake during the examination", "Funmi found the examination very easy", "Funmi was rewarded with cake", "Funmi failed the examination", "B", "'A piece of cake' = something very easy."),
    ("It is high time the council fixed the road.", "The road is on high ground", "The council should have fixed the road long ago", "The council fixed the road at noon", "The road will soon be fixed", "B", "'It is high time' + past tense expresses that something is overdue."),
    ("Mrs Eze wears the trousers in that house.", "Mrs Eze prefers to dress like a man", "Mrs Eze is the one who makes the decisions at home", "Mrs Eze sells trousers for a living", "Mrs Eze does the family laundry every week", "B", "To 'wear the trousers' is to be the dominant partner, the one who takes the decisions in a household."),
    ("The senator's resignation came out of the blue.", "The senator resigned because of the weather", "The senator's resignation was completely unexpected", "The senator resigned in a blue suit", "The senator resigned from the Blue Party", "B", "'Out of the blue' = suddenly and unexpectedly."),
    ("Dapo has been burning the candle at both ends since the semester began.", "Dapo has been wasting candles at both ends", "Dapo has been exhausting himself by working late and rising early", "Dapo has been studying by candlelight at night", "Dapo has been setting fires in the hostel", "B", "'Burn the candle at both ends' = overwork oneself day and night."),
    ("The witness spilled the beans under cross-examination.", "The witness dropped food in court", "The witness revealed secret information", "The witness refused to speak", "The witness lied to the court", "B", "'Spill the beans' = reveal a secret."),
    ("The manager gave the new clerk a dressing-down.", "The manager gave the clerk a set of new clothes", "The manager scolded the clerk severely", "The manager promoted the clerk to a new post", "The manager sent the clerk home early that day", "B", "A 'dressing-down' is a severe reprimand."),
    ("Chika passed with flying colours.", "Chika passed while waving flags", "Chika passed with great distinction", "Chika barely passed", "Chika passed the art examination", "B", "'With flying colours' = with great success."),
]

SYN_STEM = "Choose the option nearest in meaning to the word in capitals: "
SYN = [
    ("The manager was ADAMANT that the deadline would not be extended.", "uncertain", "unyielding", "hopeful", "apologetic", "B", "Adamant means refusing to change one's mind."),
    ("The road was IMPASSABLE after the storm.", "dangerous", "blocked", "narrow", "flooded", "B", "Impassable means impossible to travel along."),
    ("His CANDID remarks embarrassed the chairman.", "rude", "frank", "clever", "brief", "B", "Candid means truthful and straightforward."),
    ("The two accounts of the accident were CONTRADICTORY.", "similar", "conflicting", "detailed", "false", "B", "Contradictory accounts oppose each other."),
    ("The soldiers were ordered to RETREAT.", "advance", "withdraw", "attack", "rest", "B", "To retreat is to move back."),
    ("The auditors found several DISCREPANCIES in the accounts.", "profits", "inconsistencies", "signatures", "receipts", "B", "A discrepancy is a difference between things that should match."),
    ("She spoke with such ELOQUENCE that the crowd fell silent.", "anger", "fluent persuasiveness", "difficulty", "softness", "B", "Eloquence is fluent, persuasive speaking."),
    ("The government has pledged to ERADICATE polio.", "reduce", "wipe out", "study", "treat", "B", "To eradicate is to destroy completely."),
    ("The villagers were HOSTILE to the surveyors.", "friendly", "unfriendly", "indifferent", "generous", "B", "Hostile means unfriendly or antagonistic."),
    ("The old bridge is in a PRECARIOUS state.", "excellent", "dangerously unstable", "historic", "repaired", "B", "Precarious means not securely held; likely to fall."),
    ("The minister's statement was deliberately EVASIVE.", "direct", "avoiding a clear answer", "lengthy", "false", "B", "Evasive means avoiding commitment or a direct answer."),
    ("The rumour spread with astonishing RAPIDITY.", "accuracy", "speed", "cruelty", "difficulty", "B", "Rapidity means great speed; the rumour spread very quickly."),
    ("The old woman remained STOICAL throughout the ordeal.", "tearful", "uncomplaining", "confused", "hopeful", "B", "Stoical means enduring pain or hardship without complaint."),
    ("The judge described the crime as HEINOUS.", "minor", "utterly wicked", "unusual", "unproven", "B", "Heinous means shockingly evil."),
    ("The two leaders reached an AMICABLE settlement.", "hasty", "friendly", "secret", "expensive", "B", "Amicable means friendly and without hostility."),
]

ANT_STEM = "Choose the option opposite in meaning to the word in capitals: "
ANT = [
    ("The chief was known for his GENEROSITY to strangers.", "kindness", "meanness", "hospitality", "wealth", "B", "Generosity is the opposite of meanness/stinginess."),
    ("The road to the village is very ROUGH.", "long", "smooth", "narrow", "dusty", "B", "Rough is the opposite of smooth."),
    ("The evidence against him was FLIMSY.", "weak", "solid", "hidden", "false", "B", "Flimsy (weak, insubstantial) is opposed by solid/strong."),
    ("The teacher's explanation was very SUPERFICIAL.", "shallow", "thorough", "brief", "loud", "B", "Superficial (shallow) is the opposite of thorough/profound."),
    ("The prices in that shop are EXORBITANT.", "excessive", "reasonable", "fixed", "rising", "B", "Exorbitant (unreasonably high) is opposed by reasonable/moderate."),
    ("The bridge has been declared STRUCTURALLY SOUND.", "strong", "unsafe", "old", "narrow", "B", "'Sound' here means in good condition; the opposite is unsafe/defective."),
    ("The contract was signed VOLUNTARILY.", "freely", "under compulsion", "quickly", "secretly", "B", "Voluntarily (of one's own free will) is opposed by under compulsion."),
    ("The town's water supply is ABUNDANT during the rains.", "plentiful", "scarce", "clean", "free", "B", "Abundant is the opposite of scarce."),
    ("Her handwriting is remarkably LEGIBLE.", "clear", "unreadable", "neat", "large", "B", "Legible is the opposite of illegible/unreadable."),
    ("The witness gave a COHERENT account of events.", "logical", "confused", "brief", "honest", "B", "Coherent (logically connected) is opposed by confused/incoherent."),
    ("The new manager is very APPROACHABLE.", "friendly", "aloof", "young", "experienced", "B", "Approachable is the opposite of aloof/unapproachable."),
    ("The soil in this region is ARID.", "dry", "moist", "sandy", "rocky", "B", "Arid (very dry) is opposed by moist/wet."),
    ("The company's profits have been DWINDLING.", "shrinking", "growing", "steady", "hidden", "B", "Dwindling (gradually decreasing) is the opposite of growing."),
    ("The boy's behaviour was DELIBERATE.", "intentional", "accidental", "rude", "careless", "B", "Deliberate (intentional) is the opposite of accidental."),
    ("The old man was FRAIL after his illness.", "weak", "robust", "thin", "quiet", "B", "Frail is the opposite of robust/strong."),
]

GR_STEM = "Choose the option that best completes the gap: "
GR = [
    ("The principal, ____ I have great respect, retires next month.", "who", "whom", "for whom", "which", "C", "'For whom I have great respect' — the preposition governs the object pronoun 'whom'."),
    ("Not only ____ late, but he also forgot his books.", "he came", "did he come", "he did come", "came he", "B", "After 'Not only' at the start of a sentence, subject and auxiliary are inverted."),
    ("The police ____ investigating the matter.", "is", "are", "was", "has been", "B", "'Police' is a plural noun in English."),
    ("Many a student ____ failed for lack of preparation.", "have", "has", "were", "are", "B", "'Many a' + singular noun takes a singular verb."),
    ("____ of the two brothers is taller?", "Who", "Which", "Whom", "What", "B", "'Which' is used when choosing from a limited, known set."),
    ("She is the ____ of the two sisters.", "cleverer", "cleverest", "more cleverer", "most clever", "A", "The comparative is used for two."),
    ("I wish I ____ harder last term.", "worked", "had worked", "have worked", "work", "B", "A wish about the past takes the past perfect."),
    ("He asked me where ____.", "did I live", "I lived", "do I live", "was I living", "B", "Reported questions use statement word order and back-shift."),
    ("The bag was too heavy for her ____.", "to carry it", "to carry", "carrying", "that she carries", "B", "'Too + adjective + to + infinitive'; no object pronoun is repeated."),
    ("By this time next year, I ____ my degree.", "will complete", "will have completed", "complete", "am completing", "B", "The future perfect describes an action completed before a future time."),
    ("Ade, no less than his brothers, ____ to blame.", "are", "is", "were", "have been", "B", "'No less than' does not change the number of the subject 'Ade'."),
    ("The number of accidents on that road ____ alarming.", "are", "is", "were", "have been", "B", "'The number of' takes a singular verb (contrast 'a number of')."),
    ("A number of students ____ absent today.", "is", "are", "was", "has been", "B", "'A number of' takes a plural verb."),
    ("If it ____ tomorrow, the match will be postponed.", "will rain", "rains", "rained", "would rain", "B", "First conditional: present simple in the if-clause."),
    ("The man denied ____ the money.", "to steal", "stealing", "steal", "to have stole", "B", "'Deny' is followed by a gerund."),
    ("He is used to ____ early.", "wake", "waking", "woke", "have woken", "B", "'Be used to' + gerund (contrast 'used to wake')."),
    ("____ you study, ____ you will pass.", "The harder / the more likely", "Harder / more likely", "The hardest / the most likely", "More hard / more likely", "A", "'The + comparative ..., the + comparative ...' pattern."),
    ("Neither of the answers ____ correct.", "are", "is", "were", "have been", "B", "'Neither' as a pronoun is singular."),
    ("The doctor insisted ____ seeing the patient immediately.", "in", "on", "for", "at", "B", "The verb 'insist' takes the preposition 'on' followed by a gerund: insisted on seeing."),
    ("She congratulated him ____ his promotion.", "for", "on", "at", "about", "B", "'Congratulate someone on something'."),
    ("The children were prevented ____ entering the hall.", "to", "from", "of", "against", "B", "'Prevent someone from doing something'."),
    ("Kunle is indifferent ____ criticism.", "of", "to", "at", "with", "B", "'Indifferent' takes the preposition 'to': indifferent to criticism."),
    ("The suspect was acquitted ____ all the charges.", "from", "of", "for", "with", "B", "A person is 'acquitted of' a charge (found not guilty); 'convicted of' follows the same pattern."),
    ("The meeting was put ____ because of the strike.", "off", "up", "out", "away", "A", "The phrasal verb 'put off' means to postpone; the strike caused the meeting to be postponed."),
    ("The soldiers ____ the rebellion within a week.", "put down", "put up", "put off", "put out", "A", "'Put down' a rebellion = suppress it."),
    ("The child takes ____ his father in looks.", "up", "after", "on", "over", "B", "'Take after' = resemble a parent."),
    ("I cannot ____ with his rudeness any longer.", "put off", "put up", "put on", "put in", "B", "'Put up with' = tolerate."),
    ("The firemen managed to put ____ the fire.", "out", "off", "down", "away", "A", "'Put out' a fire = extinguish it."),
    ("He ____ a good impression at the interview.", "did", "made", "gave", "took", "B", "'Make an impression' is the collocation."),
    ("The witness ____ an oath before giving evidence.", "made", "did", "took", "gave", "C", "The fixed collocation is 'take an oath' (also 'swear an oath'), never 'make' or 'do' an oath."),
]

STRESS_STEM = "In the following word, choose the option that has the correct stress pattern (the stressed syllable is written in capitals): "
STRESS = [
    ("education", "E-du-ca-tion", "e-DU-ca-tion", "e-du-CA-tion", "e-du-ca-TION", "C", "'-tion' words are stressed on the preceding syllable: e-du-CA-tion."),
    ("biology", "BI-o-lo-gy", "bi-O-lo-gy", "bi-o-LO-gy", "bi-o-lo-GY", "B", "'-logy' words are stressed two syllables before the ending: bi-O-lo-gy."),
    ("develop", "DE-ve-lop", "de-VE-lop", "de-ve-LOP", "DE-VE-lop", "B", "de-VE-lop — second-syllable stress."),
    ("secretary", "SE-cre-ta-ry", "se-CRE-ta-ry", "se-cre-TA-ry", "se-cre-ta-RY", "A", "SE-cre-ta-ry — first-syllable stress in British English."),
    ("mathematics", "MA-the-ma-tics", "ma-THE-ma-tics", "ma-the-MA-tics", "ma-the-ma-TICS", "C", "'-ics' words are stressed on the preceding syllable: ma-the-MA-tics."),
    ("responsibility", "res-PON-si-bi-li-ty", "res-pon-SI-bi-li-ty", "res-pon-si-BI-li-ty", "res-pon-si-bi-LI-ty", "C", "'-ity' words are stressed on the syllable before: res-pon-si-BI-li-ty."),
    ("The word 'object' as a VERB is stressed", "on the first syllable", "on the second syllable", "on both syllables equally", "on neither syllable", "B", "Noun OB-ject; verb ob-JECT."),
    ("The word 'import' as a NOUN is stressed", "on the second syllable", "on the first syllable", "on both syllables equally", "on the final letter", "B", "Noun IM-port; verb im-PORT."),
    ("The word 'conduct' as a VERB is stressed", "on the first syllable", "on the second syllable", "on both syllables equally", "on neither syllable", "B", "Noun CON-duct; verb con-DUCT."),
    ("agriculture", "A-gri-cul-ture", "a-GRI-cul-ture", "a-gri-CUL-ture", "a-gri-cul-TURE", "A", "A-gri-cul-ture — first-syllable stress."),
    ("opportunity", "OP-por-tu-ni-ty", "op-POR-tu-ni-ty", "op-por-TU-ni-ty", "op-por-tu-NI-ty", "C", "'-ity' words are stressed on the syllable before: op-por-TU-ni-ty."),
    ("necessary", "NE-ces-sa-ry", "ne-CES-sa-ry", "ne-ces-SA-ry", "ne-ces-sa-RY", "A", "NE-ces-sa-ry — first-syllable stress."),
]

RHYME_STEM = "Choose the word that rhymes with the word in capitals: "
RHYME = [
    ("HEAD", "bead", "said", "heed", "hard", "B", "'Head' is /hed/, rhyming with 'said' /sed/."),
    ("GREAT", "meat", "gate", "greet", "sweat", "B", "'Great' is /greɪt/, rhyming with 'gate'."),
    ("SWORD", "word", "bird", "board", "sward", "C", "'Sword' is /sɔːd/ (silent 'w'), rhyming with 'board'."),
    ("WOMB", "comb", "bomb", "boom", "home", "C", "'Womb' is /wuːm/, rhyming with 'boom'."),
    ("AISLE", "mile", "easel", "ail", "hassle", "A", "'Aisle' is /aɪl/ (silent 's'), rhyming with 'mile'."),
    ("BURY", "fury", "very", "jury", "curry", "B", "'Bury' is pronounced /ˈberi/, rhyming with 'very'."),
]

SOUND = [
    ("Choose the word that has the same vowel sound as the one represented by the letters in capitals: bUS", "put", "but", "bush", "bull", "B", "'Bus' has /ʌ/, as in 'but'; the others have /ʊ/."),
    ("Choose the word that has the same vowel sound as the one represented by the letters in capitals: fAce", "fat", "far", "fame", "fall", "C", "'Face' has /eɪ/, as in 'fame'."),
    ("Choose the word that has the same vowel sound as the one represented by the letters in capitals: pEArl", "pear", "peer", "purse", "pair", "C", "'Pearl' has /ɜː/, as in 'purse'."),
    ("Choose the word that has the same vowel sound as the one represented by the letters in capitals: bOY", "buy", "bow", "boil", "bay", "C", "'Boy' has /ɔɪ/, as in 'boil'."),
    ("Choose the word that has the same vowel sound as the one represented by the letters in capitals: hOUse", "horse", "how", "hose", "who", "B", "'House' has /aʊ/, as in 'how'."),
    ("Choose the word that has the same consonant sound as the one represented by the letters in capitals: Sugar", "sun", "shoe", "zoo", "seat", "B", "'Sugar' begins with /ʃ/, as in 'shoe'."),
    ("Choose the word that has the same consonant sound as the one represented by the letters in capitals: THat", "thick", "there", "thumb", "thought", "B", "'That' begins with voiced /ð/, as in 'there'; the others have /θ/."),
    ("Choose the word that has the same consonant sound as the one represented by the letters in capitals: pleaSure", "sure", "garage", "sugar", "sand", "B", "'Pleasure' has /ʒ/, as in 'garage' (/ˈɡærɑːʒ/)."),
    ("Choose the word that has the same consonant sound as the one represented by the letters in capitals: Xylophone", "box", "zebra", "extra", "excel", "B", "Initial 'x' in 'xylophone' is /z/, as in 'zebra'."),
    ("Choose the word that has the same consonant sound as the one represented by the letters in capitals: siNG", "sin", "finger", "singer", "signal", "C", "'Sing' ends in /ŋ/ alone, as in 'singer'; 'finger' has /ŋg/."),
    ("Choose the word in which the letter 'b' is SILENT.", "climb", "cabin", "table", "ribbon", "A", "In 'climb' the final 'b' is not pronounced."),
    ("Choose the word in which the letter 'w' is SILENT.", "window", "wrist", "wander", "winter", "B", "'Wrist' is pronounced /rɪst/."),
    ("Choose the word in which the letter 'l' is SILENT.", "salt", "calm", "hold", "milk", "B", "'Calm' is pronounced /kɑːm/."),
    ("Choose the word in which the letters 'gh' are pronounced /f/.", "though", "enough", "night", "weigh", "B", "'Enough' ends in /f/; the others have silent 'gh'."),
]

EMPH_STEM = "Choose the option to which the given sentence relates when the word in capitals is stressed: "
EMPH = [
    ("Ibrahim REPAIRED the generator yesterday.", "Did Ibrahim sell the generator yesterday?", "Did Musa repair the generator yesterday?", "Did Ibrahim repair the pump yesterday?", "Did Ibrahim repair the generator today?", "A", "Stress on REPAIRED contrasts the action."),
    ("The children ate rice at the PARTY.", "Did the children eat beans at the party?", "Did the adults eat rice at the party?", "Did the children eat rice at home?", "Did the children cook rice at the party?", "C", "Stress on PARTY contrasts the place."),
    ("My BROTHER won the scholarship.", "Did your brother win the lottery?", "Did your sister win the scholarship?", "Did your brother lose the scholarship?", "Did his brother win the scholarship?", "B", "Stress on BROTHER contrasts the person."),
    ("Mrs Okoro teaches CHEMISTRY at the college.", "Does Mrs Okoro teach at the university?", "Does Mrs Okoro teach physics at the college?", "Does Mr Okoro teach chemistry at the college?", "Does Mrs Okoro study chemistry at the college?", "B", "Stress on CHEMISTRY contrasts the subject."),
    ("The bus leaves at SIX every morning.", "Does the bus leave at seven every morning?", "Does the train leave at six every morning?", "Does the bus arrive at six every morning?", "Does the bus leave at six every evening?", "A", "Stress on SIX contrasts the time."),
    ("Halima wrote the letter in HAUSA.", "Did Halima write the essay in Hausa?", "Did Halima write the letter in English?", "Did Fatima write the letter in Hausa?", "Did Halima read the letter in Hausa?", "B", "Stress on HAUSA contrasts the language."),
    ("The governor visited the school LAST week.", "Did the governor visit the school this week?", "Did the governor visit the hospital last week?", "Did the commissioner visit the school last week?", "Did the governor close the school last week?", "A", "Stress on LAST contrasts the time."),
    ("Ekaette BORROWED the book from the library.", "Did Ekaette borrow the book from a friend?", "Did Ekaette steal the book from the library?", "Did Ekaette borrow the magazine from the library?", "Did Ime borrow the book from the library?", "B", "Stress on BORROWED contrasts the action (borrowed, not stole)."),
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

    ptext = {k: x for k, _, x in CLOZE_P}
    for key, rows in CLOZE.items():
        for n, *_ in rows:
            assert f"[{n}]" in ptext[key], (key, n)
    apply_fixes(questions)
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
    texts = [(x["q"], x.get("passage")) for x in questions]
    assert len(texts) == len(set(texts)), "duplicate question text"
    assert all(x["answer"] in "ABCD" and all(x[k] for k in "ABCD") for x in questions)
    for x in questions:
        assert len(x["explanation"]) >= 25, x["q"]
        if "stress pattern" not in x["q"]:
            assert len({x[k].strip().lower() for k in "ABCD"}) == 4, x["q"]
    batch = {
        "batch_id": "batch_011_english_round4",
        "exam_type": "JAMB",
        "note": "Use of English round 4: 6 comprehension passages, 4 cloze passages, idioms, synonyms/antonyms in sentences, 30 grammar items, oral forms.",
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
