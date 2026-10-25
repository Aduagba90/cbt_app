"""Batch 142 - WAEC Literature-in-English round 5 (WAEC top-up, R27).

Grows WAEC Literature from 162 toward ~200 with angles not yet in the
bank: further figures of speech (personification, hyperbole,
euphemism, metonymy, synecdoche, oxymoron, paradox, pun, litotes,
apostrophe); drama technique (soliloquy, dramatic irony, denouement,
catharsis, chorus, comedy, protagonist); poetry forms (elegy, ode,
sonnet, ballad, dirge, panegyric, refrain, couplet); prose craft
(omniscient narrator, setting, flat character, motif, flashback,
theme); oral literature (riddle, folktale, myth, oriki praise poetry,
call-and-response); and writer-work pairs (Amadi, Adichie, p'Bitek,
Soyinka, Laye). Scanned against WAEC rounds 1-4, NECO Literature (all
rounds) and the JAMB pool.

    python3 scripts/build_neco_batch142.py -> content/batch_142_waec_lit5.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Literature-in-English"

T_FIG = "Further Figures of Speech"
T_DR = "Drama Technique"
T_PO = "Poetry Forms"
T_PR = "Prose Craft"
T_OR = "Oral Literature"
T_WW = "Writers and Works"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- figures
    (T_FIG, "Medium", "'The garden smiled at the morning sun.' The figure of speech here is",
     "personification", "simile", "metaphor", "irony", "A",
     "A garden has no face to smile with."),
    (T_FIG, "Medium", "'I have told you a thousand times to shut the gate.' The expression 'a thousand times' is",
     "hyperbole", "litotes", "euphemism", "paradox", "A",
     "Deliberate overstatement for effect."),
    (T_FIG, "Medium", "A condolence notice says the patriarch 'has gone to be with the Lord'. Softening the word death in this way is",
     "euphemism", "hyperbole", "pun", "metonymy", "A",
     "A soft cloth wraps a hard fact."),
    (T_FIG, "Hard", "When newsreaders report that 'the presidency has reacted', 'presidency' stands for the president and his aides. The device at work is",
     "metonymy", "synecdoche", "personification", "oxymoron", "A",
     "Near things stand for greater things."),
    (T_FIG, "Hard", "'All hands on deck' uses 'hands' to mean the whole workers. The device is",
     "synecdoche", "metonymy", "hyperbole", "litotes", "A",
     "The part carries the whole."),
    (T_FIG, "Medium", "The phrase 'deafening silence' joins contradictory words. It is an",
     "oxymoron", "paradox", "antithesis", "pun", "A",
     "Two opposites share one breath."),
    (T_FIG, "Hard", "'The child is father of the man' sounds contradictory yet rings true. Such a statement is a",
     "paradox", "oxymoron", "hyperbole", "euphemism", "A",
     "Truth wears contradiction's coat."),
    (T_FIG, "Hard", "When a dying Mercutio says, 'Ask for me tomorrow and you shall find me a grave man', he employs a",
     "pun", "simile", "innuendo", "paradox", "A",
     "One word carries two coffins."),
    (T_FIG, "Hard", "Describing a fine meal as 'not bad at all' understates it on purpose. The device is",
     "litotes", "hyperbole", "apostrophe", "metaphor", "A",
     "Praise arrives by denial."),
    (T_FIG, "Medium", "A poet who turns to address an absent friend, 'O Milton, you should be living now', uses",
     "apostrophe", "aside", "allusion", "ellipsis", "A",
     "The absent one is summoned by name."),

    # ------------------------------------------------------------- drama
    (T_DR, "Medium", "Hamlet, quite alone, weighs life and death in 'To be or not to be'. A speech of such private thinking is a",
     "soliloquy", "dialogue", "chorus", "prologue", "A",
     "The audience eavesdrops on his heart."),
    (T_DR, "Hard", "The audience watches Othello trust Iago while knowing Iago deceives him. The effect created is",
     "dramatic irony", "pathetic fallacy", "comic relief", "aside", "A",
     "We know what he does not."),
    (T_DR, "Hard", "The final unravelling in which all plot knots are loosened is the",
     "denouement", "exposition", "climax", "interlude", "A",
     "The tangles come loose at last."),
    (T_DR, "Hard", "A good tragedy leaves the audience purged of pity and fear, an effect Aristotle called",
     "catharsis", "cathaxon", "hubris", "hamartia", "A",
     "The emotions drain away cleansed."),
    (T_DR, "Medium", "In classical Greek drama, the group that sings and comments on the action is the",
     "chorus", "cast", "crew", "claque", "A",
     "Many voices judge the stage."),
    (T_DR, "Medium", "The hero climbs high only to fall to his death, and the house leaves sobered. Such a play is a",
     "tragedy", "comedy", "farce", "masque", "A",
     "Greatness falls and the house is hushed."),
    (T_DR, "Medium", "The chief character around whom a play's action turns is the",
     "protagonist", "antagonist", "foil", "extra", "A",
     "The story rides on his shoulders."),

    # ------------------------------------------------------------- poetry
    (T_PO, "Medium", "Tennyson grieved his dead friend Hallam through the stanzas of In Memoriam. A poem of such grieving is an",
     "elegy", "ode", "epigram", "epithalamium", "A",
     "Grief walks its measured lines."),
    (T_PO, "Medium", "A long, serious poem in praise of a person or thing is an",
     "ode", "dirge", "ballad", "limerick", "A",
     "Praise rises in stately stanzas."),
    (T_PO, "Medium", "A sonnet, in its classic form, contains",
     "fourteen lines", "twelve lines", "sixteen lines", "eight lines", "A",
     "Fourteen lines, no more, no less."),
    (T_PO, "Medium", "A simple narrative poem, often of folk origin and meant for singing, is the",
     "ballad", "sonnet", "ode", "epigram", "A",
     "It carries a story in its tune."),
    (T_PO, "Hard", "A song of lamentation performed at a funeral is a",
     "dirge", "hymn", "anthem", "aubade", "A",
     "Mourning is set to melody there."),
    (T_PO, "Hard", "In Yoruba oral tradition, a poem composed in praise of a person or lineage is called",
     "oriki", "ijala", "esa", "rara", "A",
     "Praise names the family's glory."),
    (T_PO, "Medium", "In many songs the same chorus returns after every verse. That recurring passage in poetry is the",
     "refrain", "rhyme", "rhythm", "run-on", "A",
     "It returns like a familiar face."),
    (T_PO, "Medium", "Two successive lines of verse that rhyme with each other form a",
     "couplet", "quatrain", "tercet", "sestet", "A",
     "A pair that answers itself."),

    # ------------------------------------------------------------- prose
    (T_PR, "Hard", "The narrator who knows every character's secret thought and moves freely everywhere is",
     "omniscient", "first-person", "naive", "unreliable", "A",
     "No heart is closed to him."),
    (T_PR, "Medium", "The time and place in which a story unfolds constitute its",
     "setting", "theme", "plot", "diction", "A",
     "When and where it all happens."),
    (T_PR, "Hard", "A character built on a single trait, changing little from start to finish, is a",
     "flat character", "round character", "stock hero", "confidant", "A",
     "One note sounds through him."),
    (T_PR, "Hard", "An image or idea that keeps returning throughout a novel, threading it together, is a",
     "motif", "theme", "plot", "climax", "A",
     "It haunts the book by design."),
    (T_PR, "Medium", "A scene that takes the reader back to events before the story's present is a",
     "flashback", "foreshadow", "flash-forward", "interlude", "A",
     "The clock turns against its rule."),
    (T_PR, "Medium", "The central idea that a whole novel is built to explore is its",
     "theme", "plot", "setting", "point of view", "A",
     "The seed-thought beneath the story."),

    # ------------------------------------------------------------- oral literature
    (T_OR, "Medium", "'What has one eye yet cannot see? A needle.' This question-puzzle form is a",
     "riddle", "proverb", "chant", "myth", "A",
     "Wit hides inside a question."),
    (T_OR, "Medium", "A traditional story, often beginning 'once upon a time', in which animals speak and a moral ends all, is a",
     "folktale", "legend", "myth", "epic", "A",
     "The fireside owns this story."),
    (T_OR, "Hard", "A sacred story explaining why the sky stands far from the earth belongs to the genre of",
     "myth", "legend", "fable", "memoir", "A",
     "It answers the world's first questions."),
    (T_OR, "Medium", "The singer leads a line and the crowd answers with the next. This pattern is",
     "call-and-response", "monody", "recitative", "gregorian", "A",
     "One voice asks, many reply."),

    # ------------------------------------------------------------- writers & works
    (T_WW, "Hard", "The novel The Concubine, set among the Igbo of Umolu, was written by",
     "Elechi Amadi", "Chinua Achebe", "Onuora Nzekwu", "T. M. Aluko", "A",
     "Amadi told Ihuoma's tragic story."),
    (T_WW, "Hard", "Purple Hibiscus, the coming-of-age novel of Kambili Achike, is the work of",
     "Chimamanda Ngozi Adichie", "Buchi Emecheta", "Flora Nwapa", "Zaynab Alkali", "A",
     "Adichie's first novel won prizes."),
    (T_WW, "Hard", "Okot p'Bitek's famous long poem, in which a village wife mourns her husband's new western ways, is titled",
     "Song of Lawino", "The Palm-Wine Drinkard", "The Voice", "Purple Hibiscus", "A",
     "Lawino's lament gives the poem its name."),
    (T_WW, "Medium", "In the Ilujinle village comedy where the schoolteacher Lakunle loses Sidi to the old Baroka, the playwright is",
     "Wole Soyinka", "J. P. Clark", "Ola Rotimi", "Femi Osofisan", "A",
     "Sidi, Lakunle and Baroka people it."),
    (T_WW, "Hard", "The autobiographical The African Child, recalling a boyhood in Guinea, came from the pen of",
     "Camara Laye", "Sembene Ousmane", "Leopold Senghor", "Amadou Hampate Ba", "A",
     "Laye wrote his village memories."),
]

build_batch(
    S,
    "batch_142_waec_lit5.json",
    "142",
    "WAEC Literature round 5 (R27 top-up): personification (garden "
    "smiled), hyperbole (thousand times), euphemism (passed on), "
    "metonymy (pen and sword), synecdoche (all hands), oxymoron "
    "(deafening silence), paradox (child father of man), pun (grave "
    "man), litotes (not bad), apostrophe (O Milton); soliloquy, "
    "dramatic irony (Othello-Iago), denouement, catharsis, chorus, "
    "tragedy, protagonist; elegy, ode, sonnet 14 lines, ballad, dirge, "
    "oriki, refrain, couplet; omniscient narrator, setting, flat "
    "character, motif, flashback, theme; riddle, folktale, myth, "
    "call-and-response; The Concubine (Amadi), Purple Hibiscus "
    "(Adichie), Song of Lawino (p'Bitek), The Lion and the Jewel "
    "(Soyinka), The African Child (Laye). Scanned against WAEC rounds "
    "1-4, NECO Literature (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
