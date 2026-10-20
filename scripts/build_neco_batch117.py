"""Batch 117 - NECO Literature-in-English round 3 (NECO top-up, Round 22).

Lifts NECO Literature from 131 toward ~175 with angles not yet in any
bank: further figures of speech (apostrophe, pathos, satire, sarcasm,
allegory, juxtaposition, symbolism, imagery), genre and form terms
(pastoral, conceit, quatrain, octave, epigram, dirge), prose and drama
vocabulary (antihero, archetype, setting types, in medias res, chorus,
prologue, farce, comedy of manners), and African writers and landmark
works (Rotimi, Tutuola, Armah, Ngugi, Okara, Awoonor, Soyinka's plays,
Osundare, Angelou, Kofi Awoonor). Scanned against NECO rounds 1-2, WAEC
Literature (all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch117.py -> content/batch_117_neco_lit3.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Literature-in-English"

T_DEV = "Further Figures of Speech"
T_FORM = "Forms and Genres"
T_PROSE = "Prose Vocabulary"
T_DRAMA = "Drama Vocabulary"
T_AFR = "Writers and Works"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- devices
    (T_DEV, "Medium", "Twinkle, twinkle, little star, how I wonder what you are directly addresses a thing; the device is",
     "apostrophe", "ellipsis", "euphony", "cliché", "A",
     "Speech is thrown at the speechless."),
    (T_DEV, "Medium", "Writing that mocks vice with wit to correct society is",
     "satire", "elegy", "idyll", "panegyric", "A",
     "Laughter carries the rebuke."),
    (T_DEV, "Medium", "Bitter words meaning the opposite, spoken to wound, are",
     "sarcasm", "pathos", "bathos", "parody", "A",
     "The wounding sting is intended."),
    (T_DEV, "Hard", "A story whose characters and events stand for deeper meanings is an",
     "allegory", "anecdote", "abstract", "almanac", "A",
     "Every layer points beyond."),
    (T_DEV, "Hard", "Placing two contrasting ideas side by side for effect is",
     "juxtaposition", "jargon", "hyperbole", "hendiadys", "A",
     "Neighbours sharpen the contrast."),
    (T_DEV, "Medium", "An object that stands for a larger idea, like a dove for peace, is a",
     "symbol", "synonym", "cliché", "collocation", "A",
     "The thing carries the meaning."),
    (T_DEV, "Medium", "Words that appeal to the senses create",
     "imagery", "irony", "ambiguity", "analogy only", "A",
     "The mind sees, hears and smells."),
    (T_DEV, "Hard", "The quality in writing that arouses pity and sadness is",
     "pathos", "bathos", "ethos", "logos", "A",
     "Tears gather at its pity."),
    (T_DEV, "Hard", "An abrupt fall from the sublime to the ridiculous is",
     "bathos", "pathos", "ethos", "mythos", "A",
     "Grandeur trips over a stone."),
    (T_DEV, "Medium", "A worn-out expression that has lost its force is a",
     "cliché", "coinage", "colloquialism", "conceit", "A",
     "Time has dulled its shine."),
    (T_DEV, "Medium", "Pleasant, harmonious sound patterns in verse are called",
     "euphony", "cacophony", "dissonance", "monotony", "A",
     "The reading ear finds it sweet."),
    (T_DEV, "Hard", "Harsh, clashing sounds deliberately used produce",
     "cacophony", "euphony", "cadence", "caesura", "A",
     "The reading ear flinches at it."),

    # ------------------------------------------------------------- forms and genres
    (T_FORM, "Hard", "A four-line stanza is a",
     "quatrain", "tercet", "sestet", "couplet", "A",
     "Four lines, one rhyme plan."),
    (T_FORM, "Hard", "An eight-line stanza or the first eight lines of a sonnet is the",
     "octave", "quatrain", "sestet", "volta", "A",
     "The Petrarchan sonnet turns after it."),
    (T_FORM, "Medium", "A brief witty verse that ends with a sting is the",
     "epigram", "epic", "epilogue", "epitaph only", "A",
     "Its brevity lands the sting."),
    (T_FORM, "Hard", "A poem written in grief for the dead, often sung at burial, is a",
     "dirge", "ode", "sonnet", "pastoral", "A",
     "The graveside hears it sung."),
    (T_FORM, "Medium", "Poetry celebrating the simple life of shepherds is",
     "pastoral", "satirical", "didactic", "gothic", "A",
     "Green fields fill its world."),
    (T_FORM, "Hard", "A far-fetched, ingenious comparison running through a whole poem is a",
     "conceit", "concession", "concrete poem", "confessional", "A",
     "Metaphysical poets loved it."),
    (T_FORM, "Medium", "Heroic deeds told at length in verse make the",
     "epic", "epigram", "aubade", "auberge", "A",
     "Beowulf and Sundiata belong here."),
    (T_FORM, "Medium", "A poem of morning song greeting the dawn is the",
     "aubade", "elegy", "eclogue", "epithalamium", "A",
     "Daybreak itself is its subject."),

    # ------------------------------------------------------------- prose
    (T_PROSE, "Medium", "A central character lacking heroic virtues is an",
     "antihero", "archetype", "antagonist", "agitator", "A",
     "Flaws define him, not glory."),
    (T_PROSE, "Medium", "The character who opposes the protagonist is the",
     "antagonist", "archetype", "confidant", "chorus", "A",
     "Standing in the hero's way."),
    (T_PROSE, "Hard", "A first instance or model pattern recurring across literature is an",
     "archetype", "anachronism", "apologue", "abstract", "A",
     "The mother figure, for example."),
    (T_PROSE, "Medium", "The where and when of a story covers its",
     "setting", "theme", "plot", "tone", "A",
     "Place, time and society make it."),
    (T_PROSE, "Hard", "A story that begins in the middle of the action opens",
     "in medias res", "in vino veritas", "in tota silentia", "in situ", "A",
     "Virgil and Homer used the plunge."),
    (T_PROSE, "Hard", "The background against which a story's events shine by contrast is the",
     "foil setting", "theme", "dénouement", "fable", "A",
     "The contrast throws extra light."),
    (T_PROSE, "Medium", "The main storyline following cause and effect is the",
     "plot", "theme", "diction", "mood", "A",
     "Events chain together into it."),

    # ------------------------------------------------------------- drama
    (T_DRAMA, "Medium", "The group speaking as one voice to comment on the action is the",
     "chorus", "clown", "coryphaeus only", "critic", "A",
     "Greek tragedy made it famous."),
    (T_DRAMA, "Medium", "A speech delivered by one actor alone on stage is a",
     "monologue", "dialogue", "prologue", "epilogue", "A",
     "Other actors stay silent."),
    (T_DRAMA, "Hard", "The opening speech introducing a play is the",
     "prologue", "epilogue", "interlude", "aside", "A",
     "It steps before the story."),
    (T_DRAMA, "Hard", "A crude, boisterous comedy of absurd situations is",
     "farce", "tragicomedy", "melodrama", "masque", "A",
     "Doors slam and trousers fall."),
    (T_DRAMA, "Hard", "Comedy that pokes fun at the manners of high society is the comedy of",
     "manners", "humours", "errors", "menace", "A",
     "Wit skewers drawing-room airs."),
    (T_DRAMA, "Medium", "A play of gloomy atmosphere, exaggerated emotion and clear villain is a",
     "melodrama", "farce", "burlesque", "satire play", "A",
     "The organ announces the villain."),
    (T_DRAMA, "Medium", "The instructions in a script about movement and staging are the",
     "stage directions", "soliloquy", "scenario", "scriptorium", "A",
     "They tell actors where to go."),

    # ------------------------------------------------------------- writers and works
    (T_AFR, "Medium", "Ola Rotimi retold the Oedipus story in a Yoruba setting in",
     "The Gods Are Not to Blame", "Kurunmi", "Ovonramwen Nogbaisi", "Our Husband Has Gone Mad Again", "A",
     "Odewale's fate drives its plot."),
    (T_AFR, "Hard", "Amos Tutuola's famous tale built on Yoruba folk imagination is",
     "The Palm-Wine Drinkard", "The Concubine", "Sozaboy", "The Famished Road", "A",
     "Its hero searches the dead's town."),
    (T_AFR, "Hard", "Ayi Kwei Armah's novel on corruption after independence is",
     "The Beautiful Ones Are Not Yet Born", "Weep Not, Child", "Season of Migration to the North", "Xala", "A",
     "The man in the bus keeps his soul."),
    (T_AFR, "Hard", "Ngugi wa Thiong'o's novel of the Mau Mau schoolboy is",
     "Weep Not, Child", "Grain of Wheat", "Petals of Blood", "Devil on the Cross", "A",
     "Njoroge's schooling ends in tears."),
    (T_AFR, "Medium", "Gabriel Okara's poem contrasting piano and drums symbolises",
     "African and Western cultures", "war and peace", "town and harbour", "rich and poor", "A",
     "The two musics tug the poet."),
    (T_AFR, "Hard", "Kofi Awoonor's The Anvil and the Hammer speaks to the poet's experience of",
     "two worlds forging his art", "sea travel alone", "prison only", "farm labour", "A",
     "Caught between anvil and hammer."),
    (T_AFR, "Medium", "Wole Soyinka's play on a Yoruba king's ritual death is",
     "Death and the King's Horseman", "The Trials of Brother Jero", "A Dance of the Forests", "The Lion and the Jewel", "A",
     "Elesin's failed duty anchors it."),
    (T_AFR, "Medium", "Niyi Osundare, a leading Nigerian poet, is also remembered as a",
     "professor of English", "military governor", "bank chief", "high court judge", "A",
     "The classroom shaped his verse."),
    (T_AFR, "Hard", "Maya Angelou's famous autobiography is",
     "I Know Why the Caged Bird Sings", "Roots", "Go Tell It on the Mountain", "Invisible Man", "A",
     "The caged bird still sings."),
    (T_AFR, "Medium", "Elechi Amadi wrote The Concubine and also the war memoir set in the civil war:",
     "Sunset in Biafra", "The Great Ponds", "The Slave Girl", "Efuru", "A",
     "Biafra's evening fills it."),
    (T_AFR, "Hard", "Flora Nwapa, Nigeria's first published female novelist, wrote",
     "Efuru", "The Joys of Motherhood", "So Long a Letter", "The Bride Price", "A",
     "Efuru's story led the way."),
    (T_AFR, "Medium", "Buchi Emecheta's novel on motherhood in Lagos is",
     "The Joys of Motherhood", "Efuru", "The Concubine", "Purple Hibiscus", "A",
     "Nnu Ego's burdens fill it."),
]

build_batch(
    S,
    "batch_117_neco_lit3.json",
    "117",
    "NECO Literature round 3 (Round 22 top-up): apostrophe, satire, "
    "sarcasm, allegory, juxtaposition, symbolism, imagery, pathos vs "
    "bathos, cliché, euphony vs cacophony, quatrain, octave, epigram, "
    "dirge, pastoral, conceit, epic, aubade, antihero, antagonist, "
    "archetype, setting, in medias res, plot, chorus, monologue, "
    "prologue, farce, comedy of manners, melodrama, stage directions, "
    "and African writers: Rotimi's Odewale play, Tutuola's "
    "Palm-Wine Drinkard, Armah's independence novel, Ngugi's Weep Not, "
    "Child, Okara's two musics, Awoonor's forge, Soyinka's Horseman, "
    "Osundare the teacher, Angelou's caged bird, Amadi's Sunset in "
    "Biafra, Nwapa's Efuru and Emecheta's motherhood novel. Scanned "
    "against NECO rounds 1-2, WAEC Literature (all rounds) and the JAMB "
    "pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
