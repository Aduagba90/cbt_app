"""Batch 084 - NECO Literature-in-English round 2 (NECO lift, Round 18).

NECO Literature Paper III is a 60-item objective paper; the bank stood at
90, so one paper nearly exhausted it. This lift adds fresh items - new
devices (synecdoche, anaphora, pathetic fallacy, pun, paradox), poetry form
(enjambment, sonnet types, free verse), drama and prose terms, more African
works (Jagua Nana, Song of a Goat, Piano and Drums, Weep Not, Child, Beautyful
Ones) and oral performance detail - scanned against the NECO round-1 bank,
the WAEC twin bank and everything else.

    python3 scripts/build_neco_batch84.py -> content/batch_084_neco_literature2.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Literature-in-English"

T_FIG = "Figures of Speech"
T_POE = "Poetry"
T_DRA = "Drama"
T_PRO = "Prose"
T_GEN = "General Literary Knowledge"
T_AFR = "African Literature"
T_ORA = "Oral Literature"

PASSAGES = []
PQ = []

Q = [
    # ---------------------------------------------------------------- figures of speech
    (T_FIG, "Medium", "'All hands on deck for the harvest.' The figure of speech here is",
     "synecdoche", "metonymy", "personification", "hyperbole", "A",
     "A part, hands, stands for the whole workers."),
    (T_FIG, "Medium", "'Ask not what your country can do for you.' Such a question needing no answer is",
     "a rhetorical question", "an oxymoron", "a litotes", "an innuendo", "A",
     "It makes its point without awaiting an answer."),
    (T_FIG, "Medium", "'To err is human; to forgive, divine.' The balanced opposition in this line is",
     "antithesis", "synecdoche", "euphemism", "climax", "A",
     "Contrasting ideas balance in one sentence."),
    (T_FIG, "Hard", "In a novel, a storm breaks out just as the hero dies. The device where nature echoes human mood is",
     "pathetic fallacy", "comic relief", "bathos", "paradox", "A",
     "Nature mirrors the character's grief."),
    (T_FIG, "Medium", "A pun works by playing on",
     "the double meaning of words", "the sound of words alone", "the length of the lines", "the rhyme scheme", "A",
     "One word carries two senses at once."),
    (T_FIG, "Hard", "'The child is the father of the man.' This seemingly self-contradictory but true saying is",
     "a paradox", "a pun", "an epigram", "an irony", "A",
     "The surface contradiction hides a truth."),
    # ---------------------------------------------------------------- poetry
    (T_POE, "Medium", "When a line of poetry runs on into the next without pause, the technique is",
     "enjambment", "caesura", "refrain", "cadence", "A",
     "The sense spills over the line break."),
    (T_POE, "Hard", "A Petrarchan sonnet is divided into",
     "an octave and a sestet", "three quatrains and a couplet", "two stanzas of eight lines", "a stanza and an envoi", "A",
     "Eight lines then six complete it."),
    (T_POE, "Hard", "A Shakespearean sonnet is closed by",
     "a rhyming couplet", "a sestet", "an envoi", "a refrain", "A",
     "Two final lines rhyme to end it."),
    (T_POE, "Easy", "Poetry written without regular metre or rhyme is called",
     "free verse", "blank verse", "a sonnet", "an ode", "A",
     "Free verse follows no fixed pattern."),
    (T_POE, "Easy", "A short poem expressing the poet's personal feelings is a",
     "lyric", "ballad", "epic", "allegory", "A",
     "The lyric pours out private emotion."),
    (T_POE, "Hard", "The repetition of the same word or phrase at the beginning of successive lines is",
     "anaphora", "a refrain", "a couplet", "an epigram", "A",
     "Line openings repeat the same words."),
    # ---------------------------------------------------------------- drama
    (T_DRA, "Hard", "In classical Greek drama, the chorus mainly",
     "comments on the action", "plays the villain", "fights the hero", "designs the stage", "A",
     "The chorus sings the play's commentary."),
    (T_DRA, "Hard", "The downfall of a tragic hero is often traced to hubris, which means",
     "excessive pride", "sudden fear", "bad luck", "poor parentage", "A",
     "Pride goes before the tragic fall."),
    (T_DRA, "Medium", "A character built on a fixed, familiar pattern that audiences recognise instantly is a",
     "stock character", "round character", "dynamic character", "narrator", "A",
     "One repeated trait defines him."),
    (T_DRA, "Hard", "The classical unities in drama require unity of",
     "time, place and action", "plot, theme and moral", "song, dance and speech", "love, war and peace", "A",
     "One day, one place, one action."),
    (T_DRA, "Medium", "A farce differs from a serious comedy because it relies on",
     "absurd, exaggerated action", "deep moral lessons", "tragic endings", "quiet conversation", "A",
     "Loud absurdity drives farce."),
    # ---------------------------------------------------------------- prose
    (T_PRO, "Hard", "A novel written in the form of letters between characters is",
     "epistolary", "picaresque", "gothic", "pastoral", "A",
     "The letters carry the story."),
    (T_PRO, "Hard", "In third-person limited narration, the narrator",
     "follows the experience of one character", "enters every character's mind", "addresses the reader as 'you'", "speaks as 'I'", "A",
     "One character's view bounds the tale."),
    (T_PRO, "Medium", "A narrative that presents a character's unbroken flow of thoughts uses",
     "stream of consciousness", "flashback", "dialogue", "understatement", "A",
     "The mind's current runs unedited."),
    (T_PRO, "Hard", "A narrator whose account the reader cannot take at face value is called",
     "unreliable", "omniscient", "naive", "absent", "A",
     "Readers must judge beyond his words."),
    (T_PRO, "Hard", "A novel that traces its hero's growth from childhood to maturity is a",
     "bildungsroman", "romance", "detective novel", "novella", "A",
     "It is the novel of growing up."),
    # ---------------------------------------------------------------- general knowledge
    (T_GEN, "Easy", "One who writes plays for the stage is a",
     "playwright", "novelist", "poet", "critic", "A",
     "The playwright makes plays."),
    (T_GEN, "Easy", "The chain of events which the author carefully arranges in a story is the",
     "plot", "theme", "setting", "diction", "A",
     "The plot orders the happenings."),
    (T_GEN, "Medium", "A central character torn within himself over a decision faces",
     "an internal conflict", "an external conflict", "a social conflict", "a physical conflict", "A",
     "The battle rages inside him."),
    (T_GEN, "Medium", "The part of the plot that comes immediately after the climax is the",
     "falling action", "rising action", "exposition", "denouement", "A",
     "Tension eases towards the end."),
    (T_GEN, "Medium", "The anxious expectation created in the reader about what happens next is",
     "suspense", "surprise", "foreshadowing", "irony", "A",
     "The reader is kept on edge."),
    # ---------------------------------------------------------------- african literature
    (T_AFR, "Hard", "The title of Achebe's Things Fall Apart is taken from a poem by",
     "W.B. Yeats", "T.S. Eliot", "William Shakespeare", "John Milton", "A",
     "Yeats wrote 'The Second Coming'."),
    (T_AFR, "Medium", "The play Song of a Goat was written by",
     "J.P. Clark", "Wole Soyinka", "Ola Rotimi", "Chinua Achebe", "A",
     "Clark of the Niger Delta wrote it."),
    (T_AFR, "Medium", "The Lagos city novel Jagua Nana was written by",
     "Cyprian Ekwensi", "Chinua Achebe", "Amos Tutuola", "Flora Nwapa", "A",
     "Ekwensi painted Lagos street life."),
    (T_AFR, "Hard", "Gabriel Okara's poem contrasting African and Western music is",
     "Piano and Drums", "Night Rain", "The Piano", "Vanity", "A",
     "The poem sets piano against drums."),
    (T_AFR, "Medium", "Weep Not, Child, a story set during the Mau Mau rising, is by",
     "Ngugi wa Thiong'o", "Chinua Achebe", "Ayi Kwei Armah", "Wole Soyinka", "A",
     "Njoroge's story came from Kenya."),
    (T_AFR, "Hard", "The Beautyful Ones Are Not Yet Born, a Ghanaian novel, is by",
     "Ayi Kwei Armah", "Ngugi wa Thiong'o", "Okot p'Bitek", "Chinua Achebe", "A",
     "Armah wrote of post-independence rot."),
    (T_AFR, "Easy", "The hero of Things Fall Apart whose fame began with wrestling is",
     "Okonkwo", "Unoka", "Ikemefuna", "Obierika", "A",
     "He threw Amalinze the Cat."),
    # ---------------------------------------------------------------- oral literature
    (T_ORA, "Medium", "Traditional storytellers usually open folktales with",
     "a set opening formula", "a war song", "a list of ancestors", "a court oath", "A",
     "Fixed words invite the tale."),
    (T_ORA, "Medium", "In Igbo folktales, the tortoise appears chiefly as the",
     "trickster", "hero", "wise elder", "cowardly king", "A",
     "His cunning fills the tales."),
    (T_ORA, "Medium", "In riddle performance, the poser expects the audience to",
     "supply the answer", "sing the chorus", "clap in silence", "leave the circle", "A",
     "The answer completes the riddle."),
    (T_ORA, "Medium", "Call-and-response is a common feature of",
     "African oral performance", "written novels only", "modern drama only", "European opera", "A",
     "The leader calls, the crowd answers."),
    (T_ORA, "Hard", "Ijala, the chant of the Yoruba hunters, is performed to praise",
     "hunters and wild game", "brides and grooms", "newborn babies", "departed sailors", "A",
     "Hunters' deeds fill ijala."),
    (T_ORA, "Easy", "A folktale session in the village square is traditionally led by",
     "elders and master storytellers", "the youngest child", "the village blacksmith", "strangers passing by", "A",
     "Experience guards the telling."),
    (T_ORA, "Medium", "A storytelling performance commonly ends with",
     "a song from the whole audience", "a moment of total silence", "a sacrifice at the shrine", "a wrestling match", "A",
     "Song rounds off the telling."),
]

build_batch(
    S,
    "batch_084_neco_literature2.json",
    "084",
    "NECO Literature round 2 (Round 18 lift): fresh devices (synecdoche, "
    "anaphora, antithesis, pathetic fallacy, pun, paradox), poetry form "
    "(enjambment, Petrarchan vs Shakespearean sonnets, free verse, lyric, "
    "anaphora), drama and prose terms (hubris, stock character, unities, "
    "farce, epistolary, third-person limited, stream of consciousness, "
    "unreliable narrator, bildungsroman, falling action), African works new "
    "to the bank (Yeats title source, Song of a Goat, Jagua Nana, Piano and "
    "Drums, Weep Not Child, Beautyful Ones, Okonkwo) and oral performance "
    "detail (opening formula, tortoise trickster, ijala, call-and-response, "
    "closing song). Scanned against NECO round 1, the WAEC twin and all "
    "banks.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
