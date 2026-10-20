"""Batch 108 - WAEC Literature-in-English round 3 (WAEC top-up, Round 21).

Lifts WAEC Literature from 110 toward ~155 with fresh angles: figures of
speech (hyperbole, litotes, irony, paradox, oxymoron, pun, euphemism),
poetry forms (sonnet types, ode, elegy, ballad, blank vs free verse,
dramatic monologue), prose elements (plot stages, character types, point
of view), drama terms (soliloquy, aside, foil, comic relief, tragic
flaw), and African writers and works. Scanned against WAEC rounds 1-2,
NECO Literature and the JAMB pool (incl. Use of English literary terms).

    python3 scripts/build_neco_batch108.py -> content/batch_108_waec_lit3.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Literature-in-English"

T_DEV = "Figures of Speech"
T_POET = "Poetry: Forms and Terms"
T_PROSE = "Prose: Plot, Character and Narration"
T_DRAMA = "Drama Terms"
T_AFR = "African Writers and Works"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- devices
    (T_DEV, "Easy", "I have a mountain of work is an example of",
     "hyperbole", "euphemism", "litotes", "pun", "A",
     "The mountain is deliberate overstatement."),
    (T_DEV, "Hard", "Not a bad result at all, meaning quite good, is",
     "litotes", "hyperbole", "paradox", "sarcasm", "A",
     "Praise hides in an understatement."),
    (T_DEV, "Medium", "A statement of the opposite of what is meant, to sting, is",
     "irony", "simile", "synecdoche", "metonymy", "A",
     "The words and meaning part ways."),
    (T_DEV, "Hard", "The child is the father of the man is an example of",
     "paradox", "hyperbole", "litotes", "alliteration", "A",
     "It sounds absurd yet rings true."),
    (T_DEV, "Hard", "Bittersweet parting combines two opposing words in an",
     "oxymoron", "irony", "pun", "metaphor", "A",
     "The pair clashes on purpose."),
    (T_DEV, "Medium", "A play on the double meaning of a word is a",
     "pun", "paradox", "personification", "pathos", "A",
     "The wit rides on two senses."),
    (T_DEV, "Medium", "Saying he passed on instead of he died is a",
     "euphemism", "hyperbole", "irony", "litotes", "A",
     "A soft word cushions a hard fact."),
    (T_DEV, "Medium", "Giving human qualities to a non-human thing is",
     "personification", "onomatopoeia", "assonance", "allusion", "A",
     "The wind whispered its secret."),
    (T_DEV, "Medium", "Words that imitate natural sounds produce",
     "onomatopoeia", "synecdoche", "metonymy", "hyperbole", "A",
     "Buzz, crash and hiss do it."),
    (T_DEV, "Hard", "Calling a businessman a suit is an example of",
     "metonymy", "simile", "paradox", "euphemism", "A",
     "A linked thing stands for the whole."),
    (T_DEV, "Hard", "Using one part to represent a whole, as in all hands on deck, is",
     "synecdoche", "metonymy", "litotes", "irony", "A",
     "The hands stand for the sailors."),
    (T_DEV, "Medium", "The emotional quality a writer's word-choice creates is the",
     "tone", "plot", "theme", "setting", "A",
     "Voice carries the feeling."),
    (T_DEV, "Medium", "A hint of what will happen later in a story is",
     "foreshadowing", "flashback", "digression", "denouement", "A",
     "The seed is planted early."),

    # ------------------------------------------------------------- poetry
    (T_POET, "Hard", "A Shakespearean sonnet is built from three quatrains and a",
     "closing couplet", "sestet", "octave", "tercet", "A",
     "Two lines seal the argument."),
    (T_POET, "Hard", "In a Petrarchan sonnet, the turn of thought occurs between the octave and the",
     "sestet", "couplet", "quatrain", "refrain", "A",
     "The volta pivots right there."),
    (T_POET, "Medium", "A long lyric poem in praise of something or somebody is an",
     "ode", "elegy", "ballad", "epigram", "A",
     "Praise pours out in stanzas."),
    (T_POET, "Medium", "A poem mourning the dead is an",
     "elegy", "ode", "sonnet", "limerick", "A",
     "Grief walks through its lines."),
    (T_POET, "Hard", "Story-songs handed down in simple quatrains describe the",
     "ballad", "sonnet", "ode", "epigram", "A",
     "Sung originally to a crowd."),
    (T_POET, "Medium", "One speaker pouring words at a mute listener throughout makes a",
     "dramatic monologue", "soliloquy on stage", "chorus", "refrain", "A",
     "One voice carries the drama."),
    (T_POET, "Medium", "Poetry with regular rhyme and metre but no rhyme at line ends",
     "describes blank verse", "describes free verse", "describes a sonnet", "describes doggerel", "A",
     "Iambic rhythm, unrhymed lines."),
    (T_POET, "Medium", "Verse that obeys no fixed metre or rhyme scheme is",
     "free verse", "blank verse", "heroic couplet", "lyric", "A",
     "It follows speech's own music."),
    (T_POET, "Hard", "A line running over into the next without pause shows",
     "enjambment", "caesura", "elision", "cadence", "A",
     "Sense spills past the line break."),
    (T_POET, "Medium", "The voice that speaks in a poem is the",
     "persona", "protagonist", "narratee", "impresario", "A",
     "Not always the poet at all."),
    (T_POET, "Medium", "What term names lines that keep returning at intervals in a poem?",
     "refrain", "motif", "chorus line", "cadence", "A",
     "It returns like a chorus."),
    (T_POET, "Hard", "A stanza of three lines is a",
     "tercet", "quatrain", "sestet", "octave", "A",
     "Three lines make up one unit."),

    # ------------------------------------------------------------- prose
    (T_PROSE, "Medium", "The peak of tension in a story is its",
     "climax", "exposition", "denouement", "prologue", "A",
     "The whole story turns on it."),
    (T_PROSE, "Medium", "The part of a story that ties up loose ends after the climax is the",
     "denouement", "rising action", "flashback", "epigraph", "A",
     "The knot gets untied here."),
    (T_PROSE, "Medium", "Background information given at a story's opening is the",
     "exposition", "climax", "interlude", "obiter dicta", "A",
     "It sets stage and players."),
    (T_PROSE, "Hard", "A character who contrasts with another to highlight qualities is a",
     "foil", "confidant", "chorus", "stock figure", "A",
     "Shining beside, differences show."),
    (T_PROSE, "Hard", "A character with only one or two traits and no inner growth is",
     "flat", "round", "dynamic", "tragic", "A",
     "We see a single side only."),
    (T_PROSE, "Hard", "A character who changes as the story unfolds is",
     "dynamic", "static", "flat", "typical", "A",
     "Growth marks the journey."),
    (T_PROSE, "Medium", "A story told by a character inside the action uses",
     "first-person narration", "omniscient narration", "third-person limited", "objective narration", "A",
     "The narrating I reports it."),
    (T_PROSE, "Medium", "A narrator who knows every character's mind is",
     "omniscient", "naive", "unreliable", "intrusive", "A",
     "All hearts lie open to him."),
    (T_PROSE, "Hard", "A break in chronology to show earlier events is a",
     "flashback", "foreshadow", "ellipsis", "epilogue", "A",
     "Time folds back on itself."),
    (T_PROSE, "Medium", "The central idea a story explores is its",
     "theme", "plot", "diction", "syntax", "A",
     "The message beneath the events."),
    (T_PROSE, "Medium", "A novella differs from a novel mainly by being",
     "shorter", "written in verse", "always comic", "devoid of plot", "A",
     "It is a slim cousin of the novel."),

    # ------------------------------------------------------------- drama
    (T_DRAMA, "Medium", "A character alone on stage speaking thoughts aloud delivers a",
     "soliloquy", "monologue to others", "aside", "prologue", "A",
     "The audience alone overhears."),
    (T_DRAMA, "Medium", "The short remark an actor throws to the house unheard by fellow actors is an",
     "aside", "soliloquy", "chorus", "epilogue", "A",
     "It slips under the scene."),
    (T_DRAMA, "Hard", "A humorous scene easing a tragedy's tension is",
     "comic relief", "dramatic irony", "pathetic fallacy", "deus ex machina", "A",
     "Laughter lets breath return."),
    (T_DRAMA, "Hard", "The hero's error or weakness that causes his ruin is the",
     "tragic flaw", "comic relief", "chorus", "catharsis", "A",
     "Hamartia dooms the great."),
    (T_DRAMA, "Medium", "The audience knows what characters do not; this is",
     "dramatic irony", "sarcasm", "litotes", "paradox", "A",
     "Knowledge sits with the house."),
    (T_DRAMA, "Hard", "An unexpected power that saves a hopeless situation is called",
     "deus ex machina", "hubris", "anagnorisis", "peripeteia", "A",
     "A god is lowered by crane."),
    (T_DRAMA, "Medium", "A play that ends happily after confusion is a",
     "comedy", "tragedy", "farce", "melodrama", "A",
     "Marriage often crowns it."),
    (T_DRAMA, "Medium", "Pity and fear purged in the audience by tragedy is",
     "catharsis", "hubris", "cliche", "burlesque", "A",
     "Aristotle named the cleansing."),

    # ------------------------------------------------------------- African writers
    (T_AFR, "Easy", "The author of Things Fall Apart is",
     "Chinua Achebe", "Wole Soyinka", "Chimamanda Adichie", "Ngugi wa Thiong'o", "A",
     "The novel made Okonkwo famous."),
    (T_AFR, "Medium", "In Things Fall Apart, Okonkwo's chi is said to say",
     "yes when he says yes", "no to all his plans", "nothing at all", "maybe to war", "A",
     "Yet his fate turns against him."),
    (T_AFR, "Medium", "Wole Soyinka, Nigeria's first Nobel laureate in Literature, won the prize in",
     "1986", "1966", "1996", "2006", "A",
     "The first African laureate.", "1986"),
    (T_AFR, "Hard", "Chimamanda Adichie's novel set during the Biafran war is",
     "Half of a Yellow Sun", "Purple Hibiscus", "Americanah", "The Concubine", "A",
     "The flag's half sun titles it."),
    (T_AFR, "Hard", "Okot p'Bitek's Song of Lawino was first composed in",
     "Acoli", "English", "Swahili", "Arabic", "A",
     "He later self-translated it."),
    (T_AFR, "Medium", "Who penned The Lion and the Jewel?",
     "Wole Soyinka", "John Kargon", "Ama Ata Aidoo", "Efua Sutherland", "A",
     "Lakunle and Sidi fill it."),
    (T_AFR, "Hard", "Elechi Amadi's The Concubine is set among which people?",
     "The Ikwerre of the Niger Delta", "The Yoruba of Ibadan", "The Hausa of Kano", "The Tiv of Benue", "A",
     "Ihuoma's story is delta-born."),
    (T_AFR, "Medium", "Fiction based on the writer's life story is called",
     "autobiographical novel", "allegory", "fable", "parody", "A",
     "Life thinly dressed as fiction."),
]

build_batch(
    S,
    "batch_108_waec_lit3.json",
    "108",
    "WAEC Literature round 3 (Round 21 top-up): hyperbole, litotes, "
    "irony, paradox, oxymoron, pun, euphemism, personification, "
    "onomatopoeia, metonymy vs synecdoche, tone, foreshadowing, "
    "Shakespearean and Petrarchan sonnets, ode, elegy, ballad, dramatic "
    "monologue, blank vs free verse, enjambment, persona, refrain, "
    "tercet, climax, denouement, exposition, foil, flat vs dynamic "
    "characters, first-person and omniscient narration, flashback, "
    "theme, novella, soliloquy, aside, comic relief, tragic flaw, "
    "dramatic irony, deus ex machina, comedy, catharsis, and African "
    "writers (Achebe, Okonkwo's chi, Soyinka 1986, Adichie's Biafra "
    "novel, p'Bitek's Acoli, The Lion and the Jewel, The Concubine's "
    "setting, autobiographical fiction). Scanned against WAEC rounds "
    "1-2, NECO Literature and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
