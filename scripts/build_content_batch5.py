"""Builds content/batch_005_english_round2.json — Use of English to the real UTME structure:
comprehension passages, CLOZE passages (10 gaps each, shown as a passage with numbered gaps),
sentence interpretation, synonyms/antonyms in sentences, basic grammar, word stress, rhymes,
vowel/consonant sounds and emphatic stress.

Run:  python3 scripts/build_content_batch5.py
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_content_batch1 import _balance  # noqa: E402
from distractor_fixes import apply_fixes  # noqa: E402

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "content", "batch_005_english_round2.json")

# ----------------------------------------------------------------------------- comprehension
C1 = ("Okada ban in the city",
      "When the state government banned commercial motorcycles from the city centre, the reaction was immediate and "
      "divided. Office workers who had relied on the machines to weave through traffic suddenly found themselves "
      "spending two hours on journeys that used to take twenty minutes. Riders, most of them young men who had "
      "borrowed money to buy their motorcycles, gathered outside the secretariat in protest. Yet hospital records "
      "told a different story. Within a month, the number of accident victims arriving at the emergency unit of the "
      "teaching hospital had fallen by almost half, and the orthopaedic ward, once nicknamed 'the okada ward', had "
      "empty beds for the first time in years. The commissioner for transport insisted that the policy was never "
      "about punishing anyone. 'We are asking a simple question,' she said. 'How many broken legs is a fast journey "
      "worth?' Critics reply that the question is unfair: the government banned the motorcycles without first "
      "providing the buses it had promised. Both sides, it seems, agree on one thing – that the city cannot go on "
      "as it was.")
C2 = ("The old librarian",
      "Mr Adekunle had run the town library for thirty-one years, and in all that time he had never once raised "
      "his voice. He did not need to. A single glance over the rim of his spectacles was enough to silence the "
      "rowdiest schoolboy. The children called him 'Baba Book' behind his back, and, although he pretended not to "
      "know, the name pleased him more than the certificate of merit the local government had given him. When "
      "the new digital library opened across the road, with its air-conditioning and its rows of glowing screens, "
      "everybody expected the old building to close. Instead, something curious happened. The teenagers went "
      "to the new place for their assignments and came back to the old one to read. 'Over there you find "
      "information,' one girl explained. 'Here you find Baba Book.' Mr Adekunle, who was listening from behind "
      "the shelves, took off his spectacles and cleaned them for a very long time.")

COMP = [
    ("C1", "Easy", "The immediate reaction to the ban was", "unanimous support", "divided", "total indifference", "violent", "B",
     "The first sentence says the reaction was 'immediate and divided'."),
    ("C1", "Medium", "The expression 'told a different story' means that the hospital records", "were badly kept", "contradicted the protesters' view of the ban", "were written by a different person", "described a fictional event", "B",
     "While workers and riders complained, the records showed the ban was saving lives — a different picture."),
    ("C1", "Medium", "The orthopaedic ward was nicknamed 'the okada ward' because", "riders worked there", "it was built with money from riders", "most of its patients were victims of motorcycle accidents", "it was near the motorcycle park", "C",
     "The ward treats bone injuries; its nickname came from the many motorcycle-accident patients it held."),
    ("C1", "Hard", "The commissioner's question 'How many broken legs is a fast journey worth?' is intended to", "request accurate statistics", "suggest that speed should not be bought with injuries", "mock the riders", "admit that the policy failed", "B",
     "It is a rhetorical question implying that no number of injuries justifies a quicker journey."),
    ("C1", "Medium", "The critics' main objection is that the government", "banned motorcycles too late", "did not provide alternative transport before the ban", "punished office workers", "ignored the hospital records", "B",
     "They say the buses that were promised were not provided first."),
    ("C2", "Easy", "Mr Adekunle controlled noisy children mainly by", "shouting at them", "reporting them to their parents", "a look over his spectacles", "locking the doors", "C",
     "'A single glance over the rim of his spectacles was enough to silence the rowdiest schoolboy.'"),
    ("C2", "Medium", "The nickname 'Baba Book'", "annoyed Mr Adekunle", "was unknown to Mr Adekunle", "secretly pleased Mr Adekunle", "was given by the local government", "C",
     "He 'pretended not to know', but the name 'pleased him more than the certificate of merit'."),
    ("C2", "Medium", "The word 'curious', as used in the passage, means", "inquisitive", "strange and unexpected", "amusing", "dangerous", "B",
     "Here 'curious' describes the surprising turn of events, not a person's desire to know."),
    ("C2", "Hard", "The girl's remark 'Here you find Baba Book' implies that", "the old library has more books", "the digital library has no staff", "the human warmth of the librarian matters as much as information", "the teenagers dislike computers", "C",
     "She contrasts 'information' (available across the road) with the person — what draws them back is Mr Adekunle himself."),
    ("C2", "Medium", "Mr Adekunle cleaned his spectacles 'for a very long time' because he", "could not see well", "was deeply moved and hiding his emotion", "was angry with the girl", "wanted to leave", "B",
     "Cleaning his glasses at length is a way of concealing tears or emotion after hearing the compliment."),
]

# ----------------------------------------------------------------------------- cloze passages
# Each gap is shown as [1] ... [10] in the passage; each question asks for one numbered gap.
Z1 = ("Cloze passage: A new school year",
      "The new school year began on a wet Monday morning. Parents [1] outside the gate with umbrellas, "
      "while the pupils, in uniforms still stiff from the tailor, filed into the [2] hall. The principal, a "
      "tall woman with a voice that needed no microphone, reminded them that success in the coming examinations "
      "would [3] on steady work rather than last-minute [4]. She then introduced three new teachers, one of "
      "[5] had come all the way from Sokoto. After the assembly, the students [6] to their classrooms, where "
      "timetables were [7] and textbooks shared out. By noon the rain had stopped, and the compound rang with "
      "the [8] of voices as friends who had not seen one another for two months exchanged holiday stories. "
      "It was, everyone agreed, a promising [9] to the term, even if the [10] of homework that evening came "
      "as an unwelcome reminder that the holidays were truly over.")
Z1Q = [
    (1, "hovered", "queued", "waited", "stayed", "C", "Parents 'waited outside the gate' — the natural, neutral verb; 'queued' implies a line, 'hovered' implies anxiety."),
    (2, "assembly", "dining", "sports", "staff", "A", "Pupils file into the ASSEMBLY hall for the principal's address."),
    (3, "rely", "depend", "base", "count", "B", "'Success would DEPEND on steady work' — depend on; 'rely' would need 'they would rely on'."),
    (4, "cramming", "sleeping", "reading", "playing", "A", "Last-minute CRAMMING is contrasted with steady work."),
    (5, "them", "which", "whom", "who", "C", "After a preposition ('one of'), the relative pronoun for people is WHOM."),
    (6, "dispersed", "departed", "crawled", "escaped", "A", "Students DISPERSED to their classrooms — spread out in different directions."),
    (7, "distributed", "contributed", "attributed", "constituted", "A", "Timetables were DISTRIBUTED (handed out)."),
    (8, "silence", "chatter", "echo", "noise", "B", "The compound 'rang with the CHATTER of voices' — friendly talk; 'noise' is possible but 'chatter' matches 'exchanged holiday stories'."),
    (9, "start", "finish", "end", "close", "A", "A promising START to the term."),
    (10, "absence", "arrival", "lack", "removal", "B", "The ARRIVAL of homework that evening reminded them the holidays were over."),
]
Z2 = ("Cloze passage: Saving for the future",
      "Many young Nigerians find it difficult to save money, not because they earn too little but because they "
      "have never [1] the habit. Financial experts advise that the moment a salary is paid, a fixed [2] – say ten "
      "per cent – should be moved into a separate account before any bill is [3]. This method, often called "
      "'paying yourself first', works because it removes the [4] to spend. Over time the small amounts [5] into a "
      "sum large enough to meet an emergency or to [6] a business. Experts also warn against borrowing to buy "
      "things that lose value, such as phones and clothes, since the [7] on such loans can swallow a third of "
      "one's income. [8], they recommend keeping a simple record of daily expenses; people are usually [9] to "
      "discover how much they spend on snacks and airtime. Saving, in the end, is less about mathematics than "
      "about [10].")
Z2Q = [
    (1, "formed", "made", "built", "created", "A", "One FORMS a habit (collocation)."),
    (2, "portion", "piece", "part", "percentage", "A", "A fixed PORTION of the salary; 'percentage' is possible but the dash then gives the percentage as an example, so 'portion' fits best."),
    (3, "settled", "sent", "posted", "signed", "A", "Bills are SETTLED (paid)."),
    (4, "temptation", "ability", "need", "power", "A", "It removes the TEMPTATION to spend."),
    (5, "grow", "accumulate", "increase", "rise", "B", "Small amounts ACCUMULATE into a large sum — gather together over time."),
    (6, "begin", "open", "start", "make", "C", "To START a business (collocation; 'open' is possible for a shop, but 'start' is the general verb)."),
    (7, "interest", "profit", "charge", "tax", "A", "INTEREST on loans can swallow a third of one's income."),
    (8, "Finally", "Therefore", "However", "Otherwise", "A", "The sentence adds a last piece of advice: FINALLY."),
    (9, "surprised", "delighted", "afraid", "annoyed", "A", "People are usually SURPRISED to discover how much they spend."),
    (10, "discipline", "luck", "wealth", "intelligence", "A", "Saving is about DISCIPLINE, the theme of the whole passage."),
]

# ----------------------------------------------------------------------------- sentence interpretation
SI_STEM = "Choose the option that best explains the information conveyed in the sentence: "
SI = [
    ("Bola would have won the election but for the last-minute defection of her supporters.", "Bola won the election in spite of the defection", "Bola lost because her supporters left her at the last minute", "Bola's supporters helped her win at the last minute", "Bola did not contest the election", "B", "'Would have won ... but for X' means she did NOT win, and X was the reason."),
    ("Not even the principal could persuade Tunde to apologise.", "The principal did not try to persuade Tunde", "Tunde apologised only to the principal", "Tunde refused to apologise despite pressure from everyone, including the principal", "Tunde persuaded the principal to apologise", "C", "'Not even X could' stresses that X, the most likely to succeed, also failed — Tunde stayed stubborn."),
    ("The manager's remarks were as unnecessary as they were unkind.", "The remarks were necessary but unkind", "The remarks were kind but unnecessary", "The remarks were both unnecessary and unkind", "The manager did not make any remarks", "C", "'As X as Y' states that both qualities apply equally."),
    ("Much as I admire Chinedu, I cannot support his decision.", "I admire Chinedu, so I support his decision", "Although I admire Chinedu, I do not support his decision", "I neither admire Chinedu nor support him", "I support Chinedu because I admire him", "B", "'Much as' means 'although' — a concession followed by a contrast."),
    ("The new road is anything but smooth.", "The road is very smooth", "The road is fairly smooth", "The road is not smooth at all", "The road has not been built", "C", "'Anything but X' means definitely not X."),
    ("Ngozi is too proud to ask for help.", "Ngozi is proud of asking for help", "Ngozi asks for help proudly", "Ngozi's pride prevents her from asking for help", "Ngozi is proud because she was helped", "C", "'Too X to Y' means so X that Y does not happen."),
    ("Had the goalkeeper not slipped, the match would have ended in a draw.", "The match ended in a draw", "The goalkeeper slipped and his team lost", "The goalkeeper did not slip", "The match was cancelled", "B", "An unreal past condition: the slip happened, and because of it the match did not end in a draw — the goalkeeper's side conceded and lost."),
    ("It was with a heavy heart that the chief announced the cancellation of the festival.", "The chief was ill", "The chief was unhappy to cancel the festival", "The chief was happy to cancel the festival", "The chief's heart was weak", "B", "'With a heavy heart' means sadly or reluctantly."),
    ("Emeka's business is barely keeping its head above water.", "The business is doing very well", "The business is only just surviving", "The business is located near water", "The business has closed down", "B", "'Keep one's head above water' means to survive with difficulty, usually financially."),
    ("No sooner had the teacher left than the class erupted in noise.", "The class was noisy before the teacher left", "The class became noisy immediately after the teacher left", "The teacher left because the class was noisy", "The class remained quiet after the teacher left", "B", "'No sooner ... than' means as soon as / immediately after."),
]

# ----------------------------------------------------------------------------- synonyms & antonyms
SYN_STEM = "Choose the option nearest in meaning to the word in capitals: "
SYN = [
    ("The governor's speech was full of PLATITUDES about unity and progress.", "insults", "dull, overused remarks", "promises", "statistics", "B", "A platitude is a remark that has been used so often it has become meaningless."),
    ("The committee's findings CORROBORATED the witness's account.", "contradicted", "confirmed", "questioned", "ignored", "B", "To corroborate is to support with additional evidence — to confirm."),
    ("The old bridge is in a PRECARIOUS condition.", "excellent", "unsafe", "modern", "expensive", "B", "Precarious means dangerously insecure or unstable."),
    ("He made a FUTILE attempt to stop the fire with a bucket of water.", "brave", "successful", "useless", "final", "C", "Futile means producing no result — pointless."),
    ("The two countries have a CORDIAL relationship.", "hostile", "friendly", "secret", "formal", "B", "Cordial means warm and friendly."),
    ("The lecturer gave a SUCCINCT summary of the chapter.", "lengthy", "brief and clear", "confusing", "humorous", "B", "Succinct means expressed briefly and clearly."),
    ("The chairman's decision was final and IRREVOCABLE.", "unfair", "temporary", "unchangeable", "popular", "C", "Irrevocable means impossible to reverse or cancel."),
    ("She was RETICENT about her plans for the future.", "excited", "reserved", "confused", "boastful", "B", "A reticent person does not reveal thoughts or feelings readily."),
    ("The soldiers showed remarkable FORTITUDE during the siege.", "cowardice", "courage in adversity", "cruelty", "carelessness", "B", "Fortitude is courage and strength in the face of pain or difficulty."),
    ("The auditor found several DISCREPANCIES in the accounts.", "profits", "inconsistencies", "signatures", "receipts", "B", "A discrepancy is a difference between things that should agree."),
]
ANT_STEM = "Choose the option opposite in meaning to the word in capitals: "
ANT = [
    ("The witness gave a CANDID account of what happened.", "honest", "detailed", "evasive", "brief", "C", "Candid means frank and honest; the opposite is evasive."),
    ("The rebels were finally SUBDUED by the army.", "defeated", "roused", "punished", "imprisoned", "B", "Subdued means brought under control or quietened; the opposite is roused (stirred up)."),
    ("The new policy has been widely CONDEMNED.", "criticised", "praised", "discussed", "ignored", "B", "To condemn is to express strong disapproval; the opposite is to praise."),
    ("The soil in this region is remarkably FERTILE.", "rich", "barren", "wet", "rocky", "B", "Fertile land produces abundant crops; barren land produces little or nothing."),
    ("The patient's condition is now STABLE.", "steady", "critical", "improving", "known", "B", "Stable means not likely to change or get worse; critical means dangerously unstable."),
    ("The minister's answer was DELIBERATELY vague.", "intentionally", "accidentally", "carefully", "cleverly", "B", "Deliberately (on purpose) is the opposite of accidentally."),
    ("He is known for his LAVISH spending on parties.", "generous", "frugal", "regular", "public", "B", "Lavish means extravagant; frugal means sparing and economical."),
    ("Her handwriting is LEGIBLE.", "beautiful", "clear", "illegible", "small", "C", "Legible means clear enough to read; the opposite is illegible."),
    ("The judge was praised for his LENIENT sentence.", "harsh", "mild", "fair", "quick", "A", "Lenient means merciful or mild; the opposite is harsh."),
    ("The organisation operates in a TRANSPARENT manner.", "open", "secretive", "efficient", "modern", "B", "Transparent here means open and honest; the opposite is secretive."),
]

# ----------------------------------------------------------------------------- basic grammar
GR_STEM = "Choose the option that best completes the gap: "
GR = [
    ("The news ____ so shocking that nobody spoke for a minute.", "were", "was", "are", "have been", "B", "'News' is an uncountable noun and takes a singular verb."),
    ("Each of the candidates ____ given a form to fill.", "were", "have been", "was", "are", "C", "'Each' is singular: each ... was."),
    ("This is the woman ____ son won the scholarship.", "who", "whom", "whose", "which", "C", "Possession ('her son') requires 'whose'."),
    ("Between you and ____, the principal is not happy with the result.", "I", "me", "myself", "mine", "B", "After a preposition ('between') the object form 'me' is required."),
    ("She has been working here ____ 2019.", "for", "since", "from", "during", "B", "'Since' + a point in time; 'for' + a length of time."),
    ("The children enjoyed ____ at the beach.", "themselves", "themself", "theirselves", "them", "A", "The reflexive plural is 'themselves'; 'theirselves' and 'themself' are not standard."),
    ("Neither of the two answers ____ correct.", "are", "were", "is", "have been", "C", "'Neither' (of two) takes a singular verb."),
    ("The teacher, as well as the students, ____ excited about the trip.", "are", "were", "is", "have been", "C", "'As well as' does not make the subject plural; 'the teacher' is singular."),
    ("I would rather you ____ me the truth now.", "tell", "told", "will tell", "have told", "B", "'Would rather + subject' takes the past form to refer to the present or future."),
    ("The suspect denied ____ the money.", "to steal", "steal", "stealing", "to have stole", "C", "'Deny' is followed by a gerund (-ing form)."),
    ("Twenty kilometres ____ a long way to walk.", "are", "is", "were", "have been", "B", "A distance treated as a single amount takes a singular verb."),
    ("It is high time we ____ for the examination.", "prepare", "prepared", "are preparing", "will prepare", "B", "'It is high time' is followed by the past simple with present meaning."),
    ("The police ____ arrested the suspects.", "has", "have", "is", "was", "B", "'Police' is a plural noun in English: the police have."),
    ("Kunle is senior ____ me by two years.", "than", "to", "over", "from", "B", "'Senior', 'junior', 'superior' and 'inferior' take 'to', not 'than'."),
    ("She insisted that he ____ the report before Friday.", "submits", "submitted", "submit", "will submit", "C", "After 'insist that', the subjunctive (base form) is used: that he submit."),
]

# ----------------------------------------------------------------------------- oral forms
STRESS_STEM = "In the following word, choose the option that has the correct stress pattern (the stressed syllable is written in capitals): "
STRESS = [
    ("photographer", "PHO-to-gra-pher", "pho-TO-gra-pher", "pho-to-GRA-pher", "pho-to-gra-PHER", "B", "Photographer is stressed on the second syllable: pho-TO-gra-pher."),
    ("democracy", "DE-mo-cra-cy", "de-MO-cra-cy", "de-mo-CRA-cy", "de-mo-cra-CY", "B", "Democracy: de-MO-cra-cy (second syllable), unlike demoCRAtic."),
    ("examination", "e-XA-mi-na-tion", "e-xa-MI-na-tion", "e-xa-mi-NA-tion", "e-xa-mi-na-TION", "C", "Words ending in -tion are stressed on the syllable before it: e-xa-mi-NA-tion."),
    ("comfortable", "COM-for-ta-ble", "com-FOR-ta-ble", "com-for-TA-ble", "com-for-ta-BLE", "A", "Comfortable is stressed on the first syllable: COM-for-ta-ble."),
    ("economics", "E-co-no-mics", "e-CO-no-mics", "e-co-NO-mics", "e-co-no-MICS", "C", "Words ending in -ics are stressed on the syllable before: e-co-NO-mics."),
    ("advantage", "AD-van-tage", "ad-VAN-tage", "ad-van-TAGE", "none of the above", "B", "Advantage: ad-VAN-tage (second syllable)."),
    ("The word 'record' in 'The band will record a new song' is stressed on the", "first syllable", "second syllable", "both syllables equally", "neither syllable", "B", "As a verb, re-CORD is stressed on the second syllable; the noun REC-ord on the first."),
    ("The word 'present' in 'She gave me a present' is stressed on the", "first syllable", "second syllable", "both syllables equally", "last letter", "A", "The noun PRE-sent is stressed on the first syllable; the verb pre-SENT on the second."),
]
RHYME_STEM = "Choose the word that rhymes with the word in capitals: "
RHYME = [
    ("COUGH", "though", "off", "through", "bough", "B", "Cough is pronounced /kɒf/ and rhymes with 'off'; the -ough spellings in the other words sound different."),
    ("HEIGHT", "weight", "eight", "kite", "freight", "C", "Height is /haɪt/ and rhymes with 'kite'; weight, eight and freight end in /eɪt/."),
    ("BREAD", "bead", "said", "plead", "need", "B", "Bread is /bred/ and rhymes with 'said' /sed/; the others have /iː/."),
    ("SEW", "few", "new", "go", "dew", "C", "Sew is pronounced /səʊ/ like 'go', not like 'few'."),
]
SOUND = [
    ("Choose the word that has the same vowel sound as the one represented by the letters in capitals: hEArt", "earth", "heard", "part", "beard", "C", "'Heart' has /ɑː/ as in 'part'; 'earth' and 'heard' have /ɜː/; 'beard' has /ɪə/."),
    ("Choose the word that has the same vowel sound as the one represented by the letters in capitals: cUt", "put", "mother", "pull", "full", "B", "'Cut' has /ʌ/, as in 'mother'; 'put', 'pull' and 'full' have /ʊ/."),
    ("Choose the word that has the same consonant sound as the one represented by the letters in capitals: meaSure", "sure", "vision", "sugar", "session", "B", "'Measure' has /ʒ/, as in 'vision'; 'sure', 'sugar' and 'session' have /ʃ/."),
    ("Choose the word that has the same consonant sound as the one represented by the letters in capitals: Gentle", "get", "give", "judge", "girl", "C", "'Gentle' begins with /dʒ/, the sound in 'judge'; 'get', 'give' and 'girl' have /g/."),
    ("Choose the word that has the same vowel sound as the one represented by the letters in capitals: sAId", "paid", "bed", "maid", "laid", "B", "'Said' is pronounced /sed/ with /e/, as in 'bed'; the others have /eɪ/."),
    ("Choose the word whose initial consonant is SILENT.", "knife", "kite", "king", "kettle", "A", "In 'knife' the 'k' is not pronounced (/naɪf/)."),
    ("Choose the word in which the letter 'h' is NOT pronounced.", "house", "honest", "horse", "hill", "B", "'Honest' is /ˈɒnɪst/ — the 'h' is silent, as in 'hour' and 'honour'."),
    ("Choose the word that has a different vowel sound from the others.", "meat", "seat", "great", "feet", "C", "'Great' has /eɪ/; 'meat', 'seat' and 'feet' have /iː/."),
]
EMPH_STEM = "Choose the option to which the given sentence relates when the word in capitals is stressed: "
EMPH = [
    ("Ngozi LENT her brother the money.", "Did Ngozi give her brother the money?", "Did Ngozi lend her sister the money?", "Did Chika lend her brother the money?", "Did Ngozi lend her brother the book?", "A", "Stress on LENT contrasts the action (lent, not gave)."),
    ("The farmer sold his GOATS at the market.", "Did the farmer buy his goats at the market?", "Did the farmer sell his goats at the farm?", "Did the farmer sell his cows at the market?", "Did the trader sell his goats at the market?", "C", "Stress on GOATS contrasts what was sold (goats, not cows)."),
    ("Our teacher travelled to ABUJA last week.", "Did your teacher travel to Abuja last month?", "Did your teacher travel to Lagos last week?", "Did your principal travel to Abuja last week?", "Did your teacher fly to Abuja last week?", "B", "Stress on ABUJA contrasts the destination."),
    ("Ibrahim BROKE the window yesterday.", "Did Musa break the window yesterday?", "Did Ibrahim break the door yesterday?", "Did Ibrahim repair the window yesterday?", "Did Ibrahim break the window today?", "C", "Stress on BROKE contrasts the action (broke, not repaired)."),
]


def build():
    questions = []
    passages = [{"key": "C1", "title": C1[0], "text": C1[1]}, {"key": "C2", "title": C2[0], "text": C2[1]},
                {"key": "Z1", "title": Z1[0], "text": Z1[1]}, {"key": "Z2", "title": Z2[0], "text": Z2[1]}]
    for key, diff, q, a, b, c, d, ans, exp in COMP:
        questions.append({"subject": "Use of English", "topic": "Comprehension", "passage": key, "difficulty": diff, "q": q, "A": a, "B": b, "C": c, "D": d, "answer": ans, "explanation": exp})
    for key, title, rows in (("Z1", Z1[0], Z1Q), ("Z2", Z2[0], Z2Q)):
        short = title.split(": ", 1)[1]
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
    apply_fixes(questions)
    # cloze options are rotated deterministically so the key is spread over A-D
    cloze = [q for q in questions if q["topic"] == "Cloze Tests"]
    for i, q in enumerate(cloze):
        opts = [q[k] for k in "ABCD"]
        shift = i % 4
        opts = opts[-shift:] + opts[:-shift] if shift else opts
        new_ans = "ABCD"[( "ABCD".index(q["answer"]) + shift) % 4]
        for k, v in zip("ABCD", opts):
            q[k] = v
        q["answer"] = new_ans
    rest = [q for q in questions if q["topic"] != "Cloze Tests"]
    _balance(rest)
    questions = cloze + rest
    texts = [(x["q"], x.get("passage")) for x in questions]
    assert len(texts) == len(set(texts)), "duplicate question text"
    assert all(x["answer"] in "ABCD" and all(x[k] for k in "ABCD") for x in questions)
    batch = {
        "batch_id": "batch_005_english_round2",
        "exam_type": "JAMB",
        "note": "Use of English round 2: 2 comprehension passages, 2 cloze passages (10 gaps each), sentence interpretation, synonyms/antonyms in context, basic grammar, word stress, rhymes, sounds, emphatic stress. Retires bare-word synonym/antonym items and one-line recall.",
        "passages": passages,
        "questions": questions,
        "deactivate": [
            {"subject": "Use of English", "like": ["Choose the word nearest in meaning to '%", "Choose the option nearest in meaning to '%", "Choose the word opposite in meaning to '%", "Choose the option opposite in meaning to '%", "The closest meaning to '%", "The opposite of '%"], "reason": "bare-word synonym/antonym items — JAMB sets the word inside a sentence"},
            {"subject": "Use of English", "topic": "Cloze Tests", "only_without_passage": True, "reason": "single-sentence 'cloze' items are not cloze tests"},
            {"subject": "Use of English", "topic": "Oral English", "max_length": 60, "reason": "'which word has a different sound' items with no given sound"},
        ],
    }
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(batch, fh, ensure_ascii=False, indent=1)
    from collections import Counter
    print(f"wrote {OUT}: {len(questions)} questions, {len(passages)} passages")
    print("answer letters:", dict(Counter(x['answer'] for x in questions)))
    print("per topic:", dict(Counter(x['topic'] for x in questions)))


if __name__ == "__main__":
    build()
