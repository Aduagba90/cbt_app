"""Batch 167 - WAEC Literature round 6 (WAEC top-up, R31).

Grows WAEC Literature from 202 toward ~237 with angles not yet in the
bank: anaphora, chiasmus, conceit, malapropism, innuendo, cliche,
cacophony; epistolary, picaresque and bildungsroman novels; stream of
consciousness, in medias res, suspense, internal conflict,
third-person limited; comedy of manners, morality play, stage
directions, closet drama; pastoral, anthology, the iamb,
colloquialism; The Gods Are Not to Blame, Song of a Goat, Death of a
Salesman, Animal Farm's allegory, Antony's oration, Macbeth, Lord of
the Flies, Piano and Drums, Diop's Africa, God's Bits of Wood, The
Beautyful Ones, The Road Not Taken. Scanned against WAEC rounds 1-5,
NECO Literature (all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch167.py -> content/batch_167_waec_lit6.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Literature-in-English"

T_FIG = "Figures of Speech"
T_LT = "Literary Terms"
T_PC = "Prose Craft"
T_PCN = "Prose: Plot, Character and Narration"
T_DT = "Drama Terms"
T_PFT = "Poetry: Forms and Terms"
T_AWW = "African Writers and Works"
T_WW = "Writers and Works"

PASSAGES = []
PQ = []

Q = [
    (T_FIG, "Hard", "Repeating the same words at the opening of successive lines, as in 'We shall fight... we shall fight...', is called",
     "anaphora", "a refrain of end-words", "an antithesis", "a caesura", "A",
     "The same opening words drum the point home."),
    (T_FIG, "Hard", "In 'Ask not what your country can do for you; ask what you can do for your country', the second half mirrors and reverses the first. The device is",
     "anaphora", "chiasmus", "an epigram", "zeugma", "B",
     "The wording crosses over like a mirrored fold."),
    (T_FIG, "Hard", "A startling, far-fetched comparison sustained at length, as when Donne likens two lovers to the legs of a compass, is a",
     "conceit", "plain simile", "an oxymoron", "an understatement", "A",
     "A bold comparison carried to great length."),
    (T_FIG, "Medium", "A comic character who declares himself 'the very pineapple of politeness' when he means pinnacle is guilty of",
     "a pun", "a spoonerism", "a malapropism", "an oxymoron", "C",
     "Mrs Malaprop of the stage gave the slip its name."),
    (T_FIG, "Medium", "A remark that hints at something improper without ever stating it outright is an",
     "epitaph", "apostrophe", "overstatement", "innuendo", "D",
     "The sting hides inside the suggestion."),
    (T_FIG, "Easy", "An expression worn smooth and lifeless by overuse, such as 'as busy as a bee', is a",
     "coinage", "cliche", "neologism", "idiom of two words", "B",
     "Familiarity has worn the words flat."),
    (T_FIG, "Medium", "Harsh, jarring combinations of sound, as in 'the rusty engine's clank and croak', are called",
     "euphony", "melody", "cacophony", "cadence", "C",
     "Clashing sounds grate upon the ear by design."),
    (T_LT, "Easy", "A published book that gathers poems or stories by many different writers is an",
     "almanac", "gazetteer", "thesaurus of verse", "anthology", "D",
     "Many voices are bound together in one volume."),
    (T_LT, "Medium", "Expressions proper to casual conversation, such as 'I am beat' for 'I am tired', are",
     "technical jargon", "colloquialisms", "archaisms", "neologisms", "B",
     "Home-bred talk rather than bookish English."),
    (T_LT, "Easy", "The gripping uncertainty a reader feels about how events will finally turn out is",
     "surprise", "suspense", "irony of fate", "mere coincidence", "B",
     "The outcome hangs and the reader waits."),
    (T_PC, "Medium", "A novel whose whole story unfolds through the letters its characters write is",
     "a picaresque novel", "an epistolary novel", "an autobiographical novel", "a detective novel", "B",
     "Letters carry the entire story along."),
    (T_PC, "Hard", "An episodic novel that follows a sly, wandering rogue through his street adventures is",
     "a gothic novel", "a historical novel", "a picaresque novel", "a romance of chivalry", "C",
     "The lovable rogue roams episode by episode."),
    (T_PC, "Medium", "Jane Eyre follows its orphan heroine from a cruel childhood to full womanhood; such a growth novel is a",
     "novel of manners", "adventure novel", "tragic novel", "bildungsroman", "D",
     "The novel grows up beside its hero."),
    (T_PC, "Hard", "An epic that plunges straight into the middle of the action and fills in the past later is said to begin",
     "ab ovo", "in medias res", "with a formal prologue", "at the denouement", "B",
     "The tale starts hot and the backstory follows."),
    (T_PCN, "Medium", "Narration that reproduces a character's raw, jumbled thoughts exactly as they occur is known as",
     "omniscient narration", "a framed narrative", "stream of consciousness", "documentary realism", "C",
     "Thought pours out unedited, as in life."),
    (T_PCN, "Medium", "A heroine torn between her love for a poor teacher and her duty to the suitor her family has chosen faces a conflict that is",
     "internal, within her own mind", "external, against nature",
     "communal, between two towns", "accidental and comic", "A",
     "The battle rages inside one breast."),
    (T_PCN, "Medium", "A narrator who stands outside the story yet enters the mind of only one character uses",
     "the first-person point of view", "the omniscient point of view",
     "the second-person point of view", "the third-person limited point of view", "D",
     "One mind only is opened to the reader."),
    (T_DT, "Medium", "A polished comedy that satirises the affectations of fashionable high society is the",
     "comedy of humours", "comedy of manners", "slapstick farce", "black comedy", "B",
     "Drawing-room follies are held up to laughter."),
    (T_DT, "Hard", "A medieval play in which Virtues and Vices appear as living characters, as in Everyman, is a",
     "morality play", "miracle play", "mystery play", "court interlude", "A",
     "Personified virtues teach salvation's road."),
    (T_DT, "Easy", "The bracketed instructions in a printed play, telling actors where to move and how to speak, are the",
     "prompt notes", "prologue", "marginal glosses", "stage directions", "D",
     "The printed hand guides the living stage."),
    (T_DT, "Hard", "A play composed to be read quietly in the study rather than acted upon a stage is a",
     "radio play", "closet drama", "masque for court", "farce in one act", "B",
     "Some plays are born only for the page."),
    (T_PFT, "Medium", "Poetry that idealises the simple pleasures of shepherds and the countryside is",
     "an urban satire", "a war poem", "pastoral", "an epic of conquest", "C",
     "Shepherds pipe in an imagined golden countryside."),
    (T_PFT, "Hard", "The metrical foot formed by one unstressed syllable followed by one stressed syllable is the",
     "trochee", "spondee", "iamb", "anapaest", "C",
     "Da-DUM: the English line's commonest foot."),
    (T_AWW, "Medium", "Ola Rotimi's play that relocates the Greek story of Oedipus into Yorubaland is",
     "Kurunmi", "The Gods Are Not to Blame", "Ovonramwen Nogbaisi", "Our Husband Has Gone Mad Again", "B",
     "Odewale's story replays Oedipus in Yoruba dress."),
    (T_AWW, "Medium", "The play Song of a Goat, in which a goat is sacrificed over a childless marriage, was written by",
     "Wole Soyinka", "Ola Rotimi", "J. P. Clark", "Hubert Ogunde", "C",
     "Clark's Niger Delta tragedy of Zifa's house."),
    (T_AWW, "Medium", "In Okara's Piano and Drums, the piano with its complex harmonies chiefly stands for",
     "the village drumming culture", "the modern Western world",
     "the poet's late father", "the long flowing river", "B",
     "The drum speaks Africa; the piano, the West."),
    (T_AWW, "Medium", "David Diop's poem Africa mourns the continent's suffering under conquest yet ends in",
     "bitter despair", "quiet acceptance of fate", "proud hope of rebirth", "a prayer for exile", "C",
     "Africa's bitter past yields to proud rebirth."),
    (T_AWW, "Hard", "God's Bits of Wood, the novel of the 1947 railway strike in French West Africa, was written by",
     "Chinua Achebe", "Ngugi wa Thiong'o", "Ayi Kwei Armah", "Sembene Ousmane", "D",
     "The Dakar-Niger strike becomes an epic."),
    (T_AWW, "Hard", "The Beautyful Ones Are Not Yet Born, with its unnamed clerk who refuses a bribe, is by the Ghanaian novelist",
     "Kofi Awoonor", "Ayi Kwei Armah", "Chinua Achebe", "Buchi Emecheta", "B",
     "The man refuses the bribe and keeps his soul."),
    (T_WW, "Medium", "The ageing American salesman Willy Loman was created by the playwright",
     "Tennessee Williams", "Eugene O'Neill", "Arthur Miller", "Clifford Odets", "C",
     "Loman chases the American dream to his fall."),
    (T_WW, "Medium", "In Orwell's Animal Farm, the animals' rebellion and its aftermath stand for",
     "the French Revolution", "the Industrial Revolution",
     "the American War of Independence", "the Russian Revolution and its betrayal", "D",
     "The farmyard mirrors the Soviet story."),
    (T_WW, "Medium", "In Julius Caesar, the cunning funeral oration that begins 'Friends, Romans, countrymen' is delivered by",
     "Brutus", "Mark Antony", "Cassius", "Octavius", "B",
     "Antony turns the crowd with ironised praise."),
    (T_WW, "Easy", "The Shakespeare tragedy in which a Scottish general, spurred by his ambitious wife, murders his king is",
     "Hamlet", "Othello", "Macbeth", "King Lear", "C",
     "Vaulting ambition murders a sleeping king."),
    (T_WW, "Easy", "In Golding's Lord of the Flies, the schoolboys stranded on a coral island gradually",
     "build a model democracy", "descend into savagery",
     "discover friendly natives", "turn the island into a farm", "B",
     "Without grown-ups the boys' order collapses."),
    (T_WW, "Easy", "The Road Not Taken, which ponders two roads diverging in a yellow wood, is by the American poet",
     "Walt Whitman", "Emily Dickinson", "Langston Hughes", "Robert Frost", "D",
     "Two roads stand for life's forked choices."),
]

build_batch(
    S,
    "batch_167_waec_lit6.json",
    "167",
    "WAEC Literature round 6 (R31 top-up): anaphora, chiasmus, conceit, "
    "malapropism, innuendo, cliche, cacophony; anthology, colloquialism, "
    "suspense; epistolary, picaresque, bildungsroman, in medias res; "
    "stream of consciousness, internal conflict, third-person limited; "
    "comedy of manners, morality play, stage directions, closet drama; "
    "pastoral, the iamb; The Gods Are Not to Blame, Song of a Goat, "
    "Piano and Drums, Diop's Africa, God's Bits of Wood, The Beautyful "
    "Ones, Willy Loman, Animal Farm allegory, Antony's oration, "
    "Macbeth, Lord of the Flies, The Road Not Taken. Scanned against "
    "WAEC rounds 1-5, NECO Literature (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
