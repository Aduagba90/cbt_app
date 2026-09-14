"""Builds content/batch_001_english_physics.json — the first "applied questions" batch.

Why a script and not hand-written JSON: every numerical Physics answer carries a `verify`
expression that this script evaluates and compares against the correct option before the
file is written. If a single answer disagrees, nothing is produced.

Run:  python3 scripts/build_content_batch1.py
"""
import json
import math
import os
import re
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "content", "batch_001_english_physics.json")

# ----------------------------------------------------------------------------- English
P1 = ("Mama Nkechi at Ogbete Market",
      "Every morning before dawn, Mama Nkechi arranges her tomatoes in neat pyramids at Ogbete Main Market in Enugu. "
      "She has sold vegetables there for twenty-two years, long enough to watch prices climb from a few kobo to hundreds "
      "of naira. Yet she does not complain about the cost of living the way younger traders do. 'The market teaches you "
      "patience,' she says, wiping her hands on her wrapper. 'Some days you sell everything; some days you carry your goods "
      "home. The trader who panics loses twice.' Her customers, many of whom she has known since they were children on "
      "their mothers' backs, rarely bargain hard with her. They know that her prices are fair and that she will slip an "
      "extra pepper into the bag of anyone who looks like they are struggling.")
P2 = ("A computer laboratory in Dala",
      "When Government Girls' Secondary School, Dala, received a solar-powered computer laboratory last year, many parents "
      "were sceptical. Computers, some argued, would distract the girls from their books. Twelve months later, the results "
      "have silenced most critics. The school recorded its best WAEC performance in a decade, and thirty students who had "
      "never touched a keyboard now type faster than their teachers. The principal attributes the change not to the machines "
      "themselves but to what they made possible: online past questions, video lessons in Hausa and English and, above all, "
      "a new confidence. 'The girls no longer see themselves as behind,' she explains. 'They see themselves as connected.' "
      "The challenge now is maintenance. Dust, heat and the occasional curious goat are constant threats, and the school's "
      "budget cannot stretch to a full-time technician.")
P3 = ("The floods in Lokoja",
      "The floods came to Lokoja in September, as they now do almost every year, but this time the town was ready. Months "
      "earlier, a group of secondary-school students had mapped the streets that always went under first and painted warning "
      "marks on walls to show how high the water had risen in previous years. When the Niger began to swell, volunteers moved "
      "elderly residents to higher ground before a single house was submerged. Not everyone was persuaded. Some traders "
      "refused to leave their shops, insisting that the river 'knew them' and would spare their goods. The river did not. Yet "
      "the overall picture was one of a community that had stopped waiting for help from Abuja and started helping itself. "
      "As one volunteer put it, 'We cannot stop the water, but we can stop the surprise.'")
P4 = ("Tunde's first day",
      "Tunde had rehearsed the sentence all the way from Abeokuta: 'Good morning, my name is Tunde Bakare and I am happy to "
      "be here.' But when the class teacher at his new school in Ibadan asked him to introduce himself, the words scattered "
      "like startled chickens. Forty pairs of eyes waited. A girl in the second row whispered something, and the whispers "
      "spread. Then a tall boy at the back stood up. 'Ma, he is the one who scored the highest in the entrance examination,' "
      "he announced, as though this settled the matter. The whispering stopped. Tunde never learnt why the boy, Chidi, had "
      "spoken for him, and Chidi never mentioned it again. But for the next six years, whenever Tunde faced a crowd, he "
      "remembered that the kindest thing a stranger can do is to give you a reason to be there.")

# (passage_index, difficulty, question, A, B, C, D, answer, explanation)
COMP = [
    (0, "Medium", "The main point of the passage is that Mama Nkechi",
     "sells the cheapest tomatoes in Enugu", "has learnt patience and fairness from years of trading",
     "is angry about rising prices", "wants younger traders to leave the market", "B",
     "The passage centres on the patience she has learnt ('The market teaches you patience') and the fairness her customers rely on."),
    (0, "Medium", "It can be inferred that her customers rarely bargain hard because",
     "they are afraid of her", "bargaining is forbidden in Ogbete market", "they trust her to be fair", "tomatoes are cheap", "C",
     "The passage says they 'know that her prices are fair' — trust, not fear or rules, explains their behaviour."),
    (0, "Hard", "The expression 'loses twice' most nearly means that the trader",
     "sells at a loss and also loses her peace of mind", "forgets to count her money", "is robbed two times", "loses two customers", "A",
     "Panic costs the trader money and also her calm; that is the double loss the proverb-like remark points to."),
    (0, "Easy", "The writer's attitude to Mama Nkechi is one of",
     "pity", "admiration", "suspicion", "indifference", "B",
     "The details chosen — her patience, fairness and quiet generosity — present her approvingly."),
    (0, "Easy", "Which of the following is TRUE according to the passage?",
     "She has traded for twelve years", "She sells at the market only at weekends",
     "She sometimes gives extra pepper to struggling customers", "She complains loudly about prices", "C",
     "The last sentence says she slips an extra pepper into the bag of anyone who looks like they are struggling."),

    (1, "Easy", "Parents were initially sceptical because they thought computers would",
     "be stolen", "distract the girls from studying", "be too expensive to run", "replace the teachers", "B",
     "The second sentence states the parents' fear directly: computers 'would distract the girls from their books'."),
    (1, "Medium", "According to the principal, the real cause of the improvement was",
     "the solar panels", "the speed of typing", "the opportunities and confidence the computers created", "the new WAEC syllabus", "C",
     "She attributes the change 'not to the machines themselves but to what they made possible' — resources and confidence."),
    (1, "Medium", "The word 'silenced', as used in the passage, means",
     "frightened", "proved wrong", "punished", "ignored", "B",
     "Good results answered the critics' objections, so they had nothing more to say — they were proved wrong."),
    (1, "Hard", "The last two sentences suggest that the laboratory's future depends mainly on",
     "the goats being kept out", "the students' typing speed", "money for upkeep and repair", "more video lessons", "C",
     "Maintenance is 'the challenge now', and the budget 'cannot stretch to a full-time technician' — funding for upkeep is the issue."),
    (1, "Medium", "'They see themselves as connected' implies that the girls now feel",
     "attached to their teachers", "part of the wider world", "tied to the school compound", "plugged into electricity", "B",
     "'Connected' contrasts with 'behind': through the internet the girls feel linked to the wider world of learning."),

    (2, "Easy", "The main idea of the passage is that",
     "floods in Lokoja are getting worse", "preparation by the community reduced the damage",
     "the government finally sent help", "traders lost all their goods", "B",
     "The passage repeatedly stresses readiness — mapping, marking, evacuating — and its result: a community 'helping itself'."),
    (2, "Hard", "'The river did not' means that the river",
     "did not rise", "did not reach the traders' shops", "did not spare the traders' goods", "did not know the traders", "C",
     "It answers the traders' claim that the river 'would spare their goods' — it did not spare them."),
    (2, "Easy", "The students' contribution was to",
     "build walls against the river", "identify the streets that flood first and mark previous water levels",
     "move elderly people", "write to Abuja for assistance", "B",
     "They 'mapped the streets that always went under first and painted warning marks' showing past water levels."),
    (2, "Medium", "The writer's tone towards the traders who stayed is",
     "admiring", "mildly critical", "furious", "fearful", "B",
     "The dry sentence 'The river did not' gently exposes the traders' error without anger."),
    (2, "Medium", "'We can stop the surprise' suggests that the community can",
     "prevent the flood", "control the river's flow", "be prepared for the flood", "surprise the government", "C",
     "They cannot stop the water, but preparation removes the shock — they can be ready."),

    (3, "Medium", "The expression 'the words scattered like startled chickens' means that Tunde",
     "spoke too loudly", "forgot what he wanted to say", "ran out of the classroom", "spoke in Yoruba instead of English", "B",
     "The rehearsed sentence fell apart from nerves — the image of scattering chickens describes his words deserting him."),
    (3, "Easy", "Chidi's announcement had the effect of",
     "making the class laugh at Tunde", "getting Tunde punished", "ending the whispering and giving Tunde respect", "angering the class teacher", "C",
     "'The whispering stopped' immediately after Chidi revealed Tunde's top score."),
    (3, "Medium", "It can be inferred that Tunde",
     "had come from another town", "had failed the entrance examination", "already knew Chidi", "disliked his new school", "A",
     "He rehearsed 'all the way from Abeokuta' to a school in Ibadan, so he had moved from another town."),
    (3, "Hard", "'as though this settled the matter' suggests that Chidi spoke",
     "hesitantly", "with confidence and finality", "angrily", "in a whisper", "B",
     "To speak as if something 'settles the matter' is to speak decisively, leaving no room for argument."),
    (3, "Easy", "The lesson Tunde drew from the experience is that",
     "one should always rehearse speeches", "strangers cannot be trusted",
     "a small act of kindness can give someone confidence", "examinations decide a person's worth", "C",
     "The final sentence: the kindest thing a stranger can do is 'give you a reason to be there'."),
]

SYN_STEM = "Choose the option nearest in meaning to the word in capitals: "
SYN = [
    ("The senator gave an EVASIVE answer when asked about the missing funds.", "honest", "indirect", "lengthy", "angry", "B", "Evasive means avoiding a direct answer — indirect."),
    ("The new bridge has ALLEVIATED the traffic problem in Apapa.", "worsened", "studied", "ignored", "reduced", "D", "To alleviate is to make a problem less severe — to reduce it."),
    ("Her explanation of the accident was LUCID.", "confusing", "long", "clear", "false", "C", "Lucid means clearly expressed and easy to understand."),
    ("The chief was RELUCTANT to sign the agreement.", "unwilling", "eager", "quick", "forced", "A", "Reluctant means unwilling or hesitant."),
    ("The company has decided to CURTAIL its spending on advertising.", "increase", "publicise", "cut down", "examine", "C", "To curtail is to reduce or cut short."),
    ("The lawyer's argument was so COGENT that the judge ruled in his favour.", "convincing", "lengthy", "emotional", "confusing", "A", "Cogent means clear, logical and convincing."),
    ("Despite the heavy rain, the farmers remained OPTIMISTIC about the harvest.", "worried", "hopeful", "careless", "confused", "B", "Optimistic means expecting a good outcome — hopeful."),
    ("The minister's remarks were widely regarded as PROVOCATIVE.", "soothing", "boring", "unclear", "inflammatory", "D", "Provocative remarks are intended to cause anger or strong reaction — inflammatory."),
    ("The village head is known for his BENEVOLENCE towards orphans.", "cruelty", "kindness", "strictness", "indifference", "B", "Benevolence is kindness and generosity."),
    ("The landlord issued an ULTIMATUM to the tenants.", "a final warning", "a receipt", "an apology", "a rent reduction", "A", "An ultimatum is a final demand or warning, with consequences if it is refused."),
    ("The students found the lecturer's explanation rather AMBIGUOUS.", "precise", "interesting", "brief", "unclear", "D", "Ambiguous means open to more than one meaning — unclear."),
    ("The referee's decision was IMPARTIAL.", "hasty", "biased", "fair", "harsh", "C", "Impartial means not favouring either side — fair."),
    ("The teacher COMMENDED the pupils for their neat handwriting.", "scolded", "praised", "questioned", "ignored", "B", "To commend is to praise formally."),
    ("The doctor advised him to ABSTAIN from alcohol.", "reduce", "enjoy", "buy", "keep away from", "D", "To abstain from something is to keep away from it completely."),
    ("There has been a PROLIFERATION of private universities in Nigeria.", "rapid increase", "closure", "inspection", "ranking", "A", "Proliferation means rapid growth in number."),
]

ANT_STEM = "Choose the option opposite in meaning to the word in capitals: "
ANT = [
    ("The witness gave a VAGUE description of the thief.", "precise", "long", "frightening", "false", "A", "Vague (unclear) is the opposite of precise."),
    ("The old man was FRUGAL with his money.", "careful", "extravagant", "wealthy", "greedy", "B", "Frugal means sparing with money; extravagant means spending freely and wastefully."),
    ("The road to the village is very NARROW.", "rough", "long", "straight", "wide", "D", "Narrow is the opposite of wide."),
    ("The manager's decision was HASTY.", "careless", "wrong", "well-considered", "sudden", "C", "Hasty means made too quickly; the opposite is carefully thought through."),
    ("The two brothers are always in HARMONY.", "conflict", "agreement", "business", "silence", "A", "Harmony (agreement) is the opposite of conflict."),
    ("The chemical is extremely VOLATILE.", "dangerous", "stable", "expensive", "colourless", "B", "Volatile means liable to change or evaporate rapidly; the opposite is stable."),
    ("He is a very HUMBLE man.", "poor", "quiet", "arrogant", "kind", "C", "Humble (modest) is the opposite of arrogant."),
    ("The teacher's instructions were EXPLICIT.", "loud", "written", "repeated", "vague", "D", "Explicit means stated clearly; the opposite is vague."),
    ("The government has decided to EXPAND the airport.", "build", "reduce", "sell", "close", "B", "Expand (make bigger) is the opposite of reduce."),
    ("The prices of foodstuffs have been FLUCTUATING since January.", "rising", "falling", "stable", "doubling", "C", "Fluctuating prices rise and fall; the opposite is stable."),
    ("The visitors were given a HOSTILE reception.", "friendly", "brief", "noisy", "formal", "A", "Hostile (unfriendly) is the opposite of friendly."),
    ("The council's response to the complaint was PROMPT.", "rude", "delayed", "written", "careful", "B", "Prompt means without delay; the opposite is delayed."),
    ("She spoke in a very FORMAL manner.", "loud", "polite", "rapid", "casual", "D", "Formal is the opposite of casual or informal."),
    ("The team's performance this season has been MEDIOCRE.", "average", "poor", "excellent", "consistent", "C", "Mediocre means of only average quality; the opposite is excellent."),
    ("The soldiers made a COWARDLY retreat.", "brave", "hasty", "quiet", "planned", "A", "Cowardly is the opposite of brave."),
]

SC_STEM = "Choose the option that best completes the gap: "
SC = [
    ("Hardly had the referee blown the final whistle ____ the fans rushed onto the pitch.", "than", "when", "that", "then", "B", "'Hardly … when' is the fixed pair; 'no sooner … than' is the other."),
    ("The principal, together with the teachers, ____ attending the conference in Abuja.", "are", "were", "is", "have been", "C", "A phrase beginning 'together with' does not change the number of the subject; 'the principal' is singular, so 'is'."),
    ("If I ____ you, I would accept the scholarship.", "am", "were", "was", "be", "B", "The unreal (hypothetical) condition takes 'were' for all persons: 'If I were you'."),
    ("Neither the driver nor the passengers ____ injured in the accident.", "was", "is", "has been", "were", "D", "With 'neither … nor', the verb agrees with the nearer subject — 'passengers', plural — so 'were'."),
    ("She is one of the few students who ____ passed the examination.", "has", "is", "was", "have", "D", "'Who' refers to 'students' (plural), not to 'she', so the verb is plural: 'have passed'."),
    ("The committee ____ its report to the governor last week.", "submit", "submitting", "submitted", "had submit", "C", "'Last week' fixes the action in the simple past: 'submitted'."),
    ("No sooner had we arrived at the station ____ the train left.", "when", "then", "than", "that", "C", "'No sooner' is always followed by 'than'."),
    ("He insisted ____ paying for the meal.", "on", "in", "for", "to", "A", "'Insist' takes the preposition 'on': insist on doing something."),
    ("By this time next year, my sister ____ from the university.", "will graduate", "will have graduated", "graduates", "has graduated", "B", "An action completed before a future point takes the future perfect: 'will have graduated'."),
    ("The more you practise past questions, ____ you become.", "the more confident", "more confident", "the most confident", "much confident", "A", "The parallel comparative pattern is 'the more …, the more …'."),
]

STRESS_STEM = "Choose the option to which the given sentence relates when the word in capitals is stressed: "
STRESS = [
    ("AMINA bought the red bag yesterday.", "Did Amina sell the red bag yesterday?", "Did Amina buy the blue bag yesterday?", "Did Aisha buy the red bag yesterday?", "Did Amina buy the red bag today?", "C", "Stressing AMINA answers a question about WHO bought the bag — the option that names a different person."),
    ("The teacher punished the BOY for coming late.", "Did the teacher praise the boy for coming late?", "Did the teacher punish the girl for coming late?", "Did the principal punish the boy for coming late?", "Did the teacher punish the boy for fighting?", "B", "Stress on BOY contrasts him with someone else who might have been punished — 'the girl'."),
    ("My uncle bought a NEW car in Lagos.", "Did your uncle buy a used car in Lagos?", "Did your aunt buy a new car in Lagos?", "Did your uncle buy a new car in Abuja?", "Did your uncle sell a new car in Lagos?", "A", "Stress on NEW contrasts with the car's condition — 'used'."),
    ("Kemi will travel to Kano TOMORROW.", "Will Kemi travel to Kaduna tomorrow?", "Will Kemi fly to Kano tomorrow?", "Will Tope travel to Kano tomorrow?", "Will Kemi travel to Kano next week?", "D", "Stress on TOMORROW contrasts the time of travel — 'next week'."),
    ("The students SANG the anthem loudly.", "Did the teachers sing the anthem loudly?", "Did the students sing the anthem softly?", "Did the students recite the anthem loudly?", "Did the students sing the chorus loudly?", "C", "Stress on SANG contrasts the action — 'recite'."),
]
SOUND = [
    ("Choose the word that has the same vowel sound as the one represented by the letters in capitals: pLAY", "weight", "said", "height", "sit", "A", "'Play' has the /eɪ/ sound, as in 'weight'; 'said' is /e/, 'height' is /aɪ/, 'sit' is /ɪ/."),
    ("Choose the word that has the same consonant sound as the one represented by the letters in capitals: CHurch", "machine", "chemist", "champagne", "nature", "D", "'Church' begins with /tʃ/, the sound in 'nature'; 'machine' and 'champagne' have /ʃ/, 'chemist' has /k/."),
    ("Choose the word that has the same vowel sound as the one represented by the letters in capitals: bOOk", "food", "pull", "boot", "blood", "B", "'Book' has the short /ʊ/ sound, as in 'pull'; 'food' and 'boot' have long /uː/, 'blood' has /ʌ/."),
    ("Choose the word that has the same consonant sound as the one represented by the letters in capitals: THin", "three", "this", "those", "father", "A", "'Thin' has the voiceless /θ/, as in 'three'; 'this', 'those' and 'father' have the voiced /ð/."),
    ("Choose the word that rhymes with the word in capitals: BEAR", "fear", "near", "pear", "dear", "C", "'Bear' is pronounced /beə/ and rhymes with 'pear'; 'fear', 'near' and 'dear' end in /ɪə/."),
]

# ----------------------------------------------------------------------------- Physics
# (topic, difficulty, question, A, B, C, D, answer, explanation, verify_expression_or_None)
PHYS = [
    ("Motion", "Medium", "A car starting from rest accelerates uniformly to 20 m/s in 5 s. The distance covered in this time is", "25 m", "50 m", "100 m", "200 m", "B", "a = 20/5 = 4 m/s²; s = ½at² = ½ × 4 × 5² = 50 m (or average velocity 10 m/s × 5 s).", "0.5*4*25"),
    ("Motion", "Easy", "A stone is thrown vertically upwards with a speed of 20 m/s. Taking g = 10 m/s², the maximum height reached is", "20 m", "10 m", "40 m", "80 m", "A", "At maximum height v = 0, so h = u²/2g = 20²/(2 × 10) = 20 m.", "20**2/20"),
    ("Motion", "Easy", "A ball is dropped from the top of a building 45 m high. Taking g = 10 m/s², the time it takes to reach the ground is", "2.0 s", "4.5 s", "3.0 s", "9.0 s", "C", "h = ½gt² ⇒ t = √(2h/g) = √(90/10) = √9 = 3 s.", "(2*45/10)**0.5"),
    ("Motion", "Hard", "A bus moves at a constant velocity of 10 m/s for 4 s and then decelerates uniformly to rest in a further 2 s. The total distance travelled is", "40 m", "50 m", "60 m", "80 m", "B", "Distance = area under the velocity–time graph: rectangle 10 × 4 = 40 m plus triangle ½ × 2 × 10 = 10 m; total 50 m.", "10*4+0.5*2*10"),
    ("Forces and Equilibrium", "Easy", "A net force of 20 N acts on a body of mass 5 kg. The acceleration produced is", "0.25 m/s²", "25 m/s²", "100 m/s²", "4 m/s²", "D", "F = ma ⇒ a = F/m = 20/5 = 4 m/s².", "20/5"),
    ("Forces and Equilibrium", "Medium", "A 2 kg block on a rough horizontal table is pulled by a horizontal force of 10 N. If the frictional force is 4 N, the acceleration of the block is", "2 m/s²", "3 m/s²", "5 m/s²", "7 m/s²", "B", "Net force = 10 − 4 = 6 N; a = F/m = 6/2 = 3 m/s².", "(10-4)/2"),
    ("Forces and Equilibrium", "Easy", "An astronaut has a mass of 60 kg on Earth. On the Moon, where g = 1.6 m/s², her weight is", "60 N", "37.5 N", "96 N", "600 N", "C", "Mass does not change; weight W = mg = 60 × 1.6 = 96 N.", "60*1.6"),
    ("Work Energy and Power", "Easy", "A boy pushes a crate 4 m across a floor with a steady horizontal force of 50 N. The work done is", "12.5 J", "54 J", "800 J", "200 J", "D", "Work = force × distance moved in the direction of the force = 50 × 4 = 200 J.", "50*4"),
    ("Work Energy and Power", "Medium", "A student of mass 60 kg climbs a flight of stairs 5 m high in 10 s. Taking g = 10 m/s², the average power developed is", "30 W", "300 W", "3000 W", "120 W", "B", "Power = work/time = mgh/t = (60 × 10 × 5)/10 = 300 W.", "60*10*5/10"),
    ("Work Energy and Power", "Easy", "The kinetic energy of a 1000 kg car moving at 20 m/s is", "10 kJ", "20 kJ", "400 kJ", "200 kJ", "D", "KE = ½mv² = ½ × 1000 × 20² = 200 000 J = 200 kJ.", "0.5*1000*400/1000"),
    ("Work Energy and Power", "Easy", "A machine receives 500 J of energy and does 400 J of useful work. Its efficiency is", "80%", "20%", "125%", "100%", "A", "Efficiency = (useful output/input) × 100 = (400/500) × 100 = 80%.", "400/500*100"),
    ("Momentum and Machines", "Medium", "A 0.5 kg ball moving at 8 m/s strikes a wall and rebounds along the same line at 6 m/s. The magnitude of the change in momentum is", "1 kg m/s", "4 kg m/s", "14 kg m/s", "7 kg m/s", "D", "Velocity reverses, so Δp = m(v + u) = 0.5 × (8 + 6) = 7 kg m/s.", "0.5*(8+6)"),
    ("Momentum and Machines", "Medium", "A 2 kg trolley moving at 3 m/s collides with a stationary 1 kg trolley and the two move off together. Their common velocity is", "1 m/s", "2 m/s", "3 m/s", "6 m/s", "B", "Momentum is conserved: 2 × 3 + 1 × 0 = (2 + 1)v ⇒ v = 6/3 = 2 m/s.", "6/3"),
    ("Momentum and Machines", "Easy", "A force of 50 N acts on a football for 0.2 s. The impulse given to the ball is", "10 N s", "250 N s", "0.004 N s", "50.2 N s", "A", "Impulse = force × time = 50 × 0.2 = 10 N s.", "50*0.2"),
    ("Momentum and Machines", "Hard", "A lever is used to lift a load of 100 N with an effort of 20 N. If the velocity ratio of the lever is 8, its efficiency is", "40%", "80%", "160%", "62.5%", "D", "MA = load/effort = 100/20 = 5; efficiency = (MA/VR) × 100 = (5/8) × 100 = 62.5%.", "(100/20)/8*100"),
    ("Properties of Matter", "Medium", "A block of mass 200 g has a volume of 250 cm³. When placed in water (density 1.0 g/cm³) it will", "sink because its density is 1.25 g/cm³", "float because its density is 0.8 g/cm³", "sink because it is heavier than 100 g", "float because its volume is greater than 200 cm³", "B", "Density = mass/volume = 200/250 = 0.8 g/cm³, which is less than that of water, so it floats.", None),
    ("Properties of Matter", "Easy", "A box of mass 20 kg rests on a floor with its base area 0.5 m². Taking g = 10 m/s², the pressure it exerts on the floor is", "10 Pa", "40 Pa", "100 Pa", "400 Pa", "D", "Pressure = force/area = (20 × 10)/0.5 = 400 Pa.", "20*10/0.5"),
    ("Properties of Matter", "Medium", "The pressure due to water at the bottom of a tank 3 m deep is (density of water = 1000 kg/m³, g = 10 m/s²)", "300 Pa", "3,000 Pa", "300,000 Pa", "30,000 Pa", "D", "Pressure in a liquid = hρg = 3 × 1000 × 10 = 30 000 Pa.", "3*1000*10"),
    ("Properties of Matter", "Medium", "A force of 5 N stretches a spring by 2 cm. Within the elastic limit, a force of 12.5 N will stretch it by", "3 cm", "4 cm", "5 cm", "6.25 cm", "C", "Hooke's law: extension ∝ force. k = 5/2 = 2.5 N/cm, so e = 12.5/2.5 = 5 cm.", "12.5/(5/2)"),
    ("Heat and Thermal Physics", "Medium", "The quantity of heat needed to raise the temperature of 2 kg of water from 20 °C to 70 °C is (specific heat capacity of water = 4200 J/kg K)", "420 kJ", "42 kJ", "168 kJ", "588 kJ", "A", "Q = mcΔθ = 2 × 4200 × (70 − 20) = 420 000 J = 420 kJ.", "2*4200*50/1000"),
    ("Heat and Thermal Physics", "Easy", "The heat required to melt 0.5 kg of ice at 0 °C is (specific latent heat of fusion of ice = 336,000 J/kg)", "168 kJ", "336 kJ", "672 kJ", "84 kJ", "A", "Q = mL = 0.5 × 336 000 = 168 000 J = 168 kJ. No temperature change occurs during melting.", "0.5*336000/1000"),
    ("Heat and Thermal Physics", "Easy", "A bimetallic strip made of brass and iron (brass expands more than iron) is heated. The strip will", "remain straight", "bend towards the brass side", "bend towards the iron side", "shrink in length", "C", "The brass side becomes longer than the iron side, so the strip curves with brass on the outside — it bends towards the iron.", None),
    ("Heat and Thermal Physics", "Medium", "A fixed mass of gas at 27 °C and 2 atm is heated at constant volume to 177 °C. The new pressure is", "1.5 atm", "3 atm", "4 atm", "13 atm", "B", "Pressure law: P₁/T₁ = P₂/T₂ with temperatures in kelvin: 2/300 = P₂/450 ⇒ P₂ = 3 atm.", "2*450/300"),
    ("Heat and Thermal Physics", "Easy", "400 cm³ of a gas at 100 kPa is compressed to 200 kPa at constant temperature. The new volume is", "200 cm³", "100 cm³", "800 cm³", "400 cm³", "A", "Boyle's law: P₁V₁ = P₂V₂ ⇒ 100 × 400 = 200 × V₂ ⇒ V₂ = 200 cm³.", "100*400/200"),
    ("Waves", "Easy", "A wave of frequency 500 Hz has a wavelength of 0.68 m. Its speed is", "735 m/s", "340 m/s", "500.68 m/s", "34 m/s", "B", "v = fλ = 500 × 0.68 = 340 m/s.", "500*0.68"),
    ("Waves", "Easy", "The period of a wave whose frequency is 50 Hz is", "0.02 s", "0.2 s", "2 s", "50 s", "A", "Period is the time for one complete cycle: T = 1/f = 1/50 = 0.02 s.", "1/50"),
    ("Sound", "Medium", "A boy standing in front of a cliff claps his hands and hears the echo 2 s later. If the speed of sound in air is 340 m/s, the distance of the cliff from the boy is", "170 m", "340 m", "680 m", "1360 m", "B", "The sound travels to the cliff and back: 2d = vt = 340 × 2 = 680 m ⇒ d = 340 m.", "340*2/2"),
    ("Sound", "Hard", "A pipe closed at one end is 17 cm long. Taking the speed of sound as 340 m/s, the frequency of its fundamental note is", "250 Hz", "1000 Hz", "500 Hz", "2000 Hz", "C", "For a closed pipe the fundamental has L = λ/4 ⇒ λ = 4 × 0.17 = 0.68 m; f = v/λ = 340/0.68 = 500 Hz.", "340/(4*0.17)"),
    ("Light and Optics", "Medium", "An object is placed 2 m in front of a plane mirror. If the object moves 0.5 m towards the mirror, the distance between the object and its image becomes", "1.5 m", "2.5 m", "4.0 m", "3.0 m", "D", "The image is as far behind the mirror as the object is in front: new object distance 1.5 m, so object–image separation = 2 × 1.5 = 3.0 m.", "2*(2-0.5)"),
    ("Light and Optics", "Medium", "A ray of light passes from air into glass at an angle of incidence of 60° and is refracted at 30°. The refractive index of the glass is", "0.58", "1.15", "1.73", "2.00", "C", "n = sin i / sin r = sin 60° / sin 30° = 0.866/0.5 = 1.73.", "math.sin(math.radians(60))/math.sin(math.radians(30))"),
    ("Light and Optics", "Hard", "The refractive index of a glass is 1.5. Its critical angle is approximately (sin 42° ≈ 0.67)", "30°", "42°", "48°", "60°", "B", "sin c = 1/n = 1/1.5 = 0.67 ⇒ c ≈ 42°.", "math.degrees(math.asin(1/1.5))"),
    ("Light and Optics", "Hard", "An object is placed 15 cm from a converging lens of focal length 10 cm. The image is formed", "6 cm from the lens, virtual and upright", "30 cm from the lens, real and inverted", "25 cm from the lens, real and upright", "30 cm from the lens, virtual and inverted", "B", "1/v = 1/f − 1/u = 1/10 − 1/15 = 1/30 ⇒ v = 30 cm; an object outside f gives a real, inverted image.", "1/(1/10-1/15)"),
    ("Electricity", "Easy", "A 12 V battery is connected across a 4 Ω resistor. The current that flows is", "0.33 A", "48 A", "8 A", "3 A", "D", "Ohm's law: I = V/R = 12/4 = 3 A.", "12/4"),
    ("Electricity", "Medium", "Resistors of 2 Ω and 4 Ω are connected in series to a 12 V battery of negligible internal resistance. The potential difference across the 4 Ω resistor is", "8 V", "6 V", "4 V", "12 V", "A", "Total resistance 6 Ω ⇒ I = 12/6 = 2 A; p.d. across 4 Ω = IR = 2 × 4 = 8 V.", "12/6*4"),
    ("Electricity", "Easy", "The combined resistance of a 6 Ω and a 3 Ω resistor connected in parallel is", "2 Ω", "4.5 Ω", "9 Ω", "18 Ω", "A", "1/R = 1/6 + 1/3 = 1/2 ⇒ R = 2 Ω (product over sum: 18/9 = 2).", "6*3/9"),
    ("Electricity", "Medium", "A 2 kW electric heater is used for 3 hours every day. If electricity costs ₦50 per kWh, the daily cost of running the heater is", "₦300", "₦150", "₦100", "₦600", "A", "Energy = 2 kW × 3 h = 6 kWh; cost = 6 × ₦50 = ₦300.", "2*3*50"),
    ("Electricity", "Easy", "A 60 W bulb operates on a 240 V supply. The current through the bulb is", "0.25 A", "4 A", "0.4 A", "14,400 A", "A", "P = IV ⇒ I = P/V = 60/240 = 0.25 A.", "60/240"),
    ("Electricity", "Easy", "A current of 2 A flows through a wire for 5 minutes. The quantity of charge that passes is", "10 C", "60 C", "2.5 C", "600 C", "D", "Q = It = 2 × (5 × 60) = 600 C. Time must be in seconds.", "2*300"),
    ("Atomic and Nuclear Physics", "Medium", "A radioactive sample of mass 80 g has a half-life of 2 days. The mass remaining after 6 days is", "40 g", "20 g", "10 g", "5 g", "C", "6 days = 3 half-lives: 80 → 40 → 20 → 10 g.", "80/2**3"),
    ("Atomic and Nuclear Physics", "Medium", "When a uranium-238 nucleus (atomic number 92) emits an alpha particle, the resulting nucleus has", "mass number 236 and atomic number 92", "mass number 238 and atomic number 90", "mass number 234 and atomic number 92", "mass number 234 and atomic number 90", "D", "An alpha particle is a helium nucleus (mass 4, charge 2): mass number falls by 4 to 234 and atomic number by 2 to 90.", None),
    ("Magnetism and Electromagnetic Induction", "Medium", "A transformer has 1200 turns in its primary coil and 60 turns in its secondary coil. If the primary is connected to a 240 V a.c. supply, the secondary voltage is", "4800 V", "120 V", "12 V", "1.2 V", "C", "Vs/Vp = Ns/Np ⇒ Vs = 240 × 60/1200 = 12 V (a step-down transformer).", "240*60/1200"),
]


def _num(text):
    m = re.search(r"-?\d[\d,]*\.?\d*", text.replace(" ", ""))
    return float(m.group(0).replace(",", "")) if m else None


def _balance(questions):
    """Spread correct answers evenly over A-D by swapping the correct option with the option in
    the least-used letter.  Explanations never mention letters, so this is safe."""
    from collections import Counter
    counts = Counter(q["answer"] for q in questions)
    target = math.ceil(len(questions) / 4)
    for q in questions:
        cur = q["answer"]
        if counts[cur] <= target:
            continue
        low = min("ABCD", key=lambda k: counts[k])
        if counts[low] >= target or low == cur:
            continue
        q[cur], q[low] = q[low], q[cur]
        q["answer"] = low
        counts[cur] -= 1
        counts[low] += 1
    return questions


def build():
    questions = []
    passages = [{"key": f"P{i+1}", "title": t, "text": x} for i, (t, x) in enumerate((P1, P2, P3, P4))]
    for pi, diff, q, a, b, c, d, ans, exp in COMP:
        questions.append({"subject": "Use of English", "topic": "Comprehension", "passage": f"P{pi+1}", "difficulty": diff,
                          "q": q, "A": a, "B": b, "C": c, "D": d, "answer": ans, "explanation": exp})
    for stem, topic, rows in ((SYN_STEM, "Synonyms", SYN), (ANT_STEM, "Antonyms", ANT), (SC_STEM, "Sentence Completion", SC), (STRESS_STEM, "Oral English", STRESS)):
        for q, a, b, c, d, ans, exp in rows:
            questions.append({"subject": "Use of English", "topic": topic, "difficulty": "Medium", "q": stem + q,
                              "A": a, "B": b, "C": c, "D": d, "answer": ans, "explanation": exp})
    for q, a, b, c, d, ans, exp in SOUND:
        questions.append({"subject": "Use of English", "topic": "Oral English", "difficulty": "Medium", "q": q,
                          "A": a, "B": b, "C": c, "D": d, "answer": ans, "explanation": exp})
    bad = []
    for topic, diff, q, a, b, c, d, ans, exp, verify in PHYS:
        item = {"subject": "Physics", "topic": topic, "difficulty": diff, "q": q, "A": a, "B": b, "C": c, "D": d, "answer": ans, "explanation": exp}
        if verify:
            expected = eval(verify, {"math": math})
            got = _num(item[ans])
            if got is None or abs(got - expected) > max(0.01 * abs(expected), 0.006):
                bad.append((q[:60], ans, item[ans], expected))
        questions.append(item)
    if bad:
        for b_ in bad:
            print("MISMATCH:", b_)
        sys.exit("Physics verification failed — file not written.")
    _balance(questions)
    # sanity: unique texts, four options, valid letters
    texts = [x["q"] for x in questions]
    assert len(texts) == len(set(texts)), "duplicate question text"
    assert all(x["answer"] in "ABCD" and all(x[k] for k in "ABCD") for x in questions)
    batch = {
        "batch_id": "batch_001_english_physics",
        "exam_type": "JAMB",
        "note": "First applied-questions batch: 4 comprehension passages (20 q), 15 synonyms, 15 antonyms, 10 sentence completion, 10 oral English; 41 Physics calculation/scenario questions (numerically verified).",
        "passages": passages,
        "questions": questions,
        "deactivate": [
            {"subject": "Use of English", "topic": "Word Classes", "reason": "grammar-definition questions JAMB does not set"},
            {"subject": "Use of English", "topic": "Comprehension", "only_without_passage": True, "reason": "pseudo-comprehension questions without a passage"},
        ],
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(batch, fh, ensure_ascii=False, indent=1)
    from collections import Counter
    print(f"wrote {OUT}: {len(questions)} questions, {len(passages)} passages")
    print("answer letters:", dict(Counter(x['answer'] for x in questions)))
    print("per subject/topic:", dict(Counter((x['subject'][:7], x['topic'][:14]) for x in questions)))


if __name__ == "__main__":
    build()
