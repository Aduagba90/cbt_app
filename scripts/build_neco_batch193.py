"""Batch 193 - WAEC Literature round 7 (WAEC top-up, R37).

Grows WAEC Literature-in-English from 237 toward ~267 with
angles not yet in the bank: metaphor; personification;
hyperbole; euphemism; metonymy; synecdoche; oxymoron;
onomatopoeia; alliteration; dramatic irony; allegory; dramatis
personae; deus ex machina; catharsis; hamartia; comedy of
manners; ode; elegy; ballad; dramatic monologue; enjambment;
free verse; Iago in Othello; the star-crossed lovers; Macbeth's
witches; Caesar's dying words; Unoka's flute; the egwugwu; yams
in Things Fall Apart; the District Commissioner's book. Scanned
against the whole Literature-in-English pool (WAEC and NECO
stems, 487 items).

    python3 scripts/build_neco_batch193.py -> content/batch_193_waec_lit7.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Literature-in-English"

T_FIG = "Figures of Speech"
T_DRA = "Drama Terms"
T_POE = "Poetry Terms"
T_AFR = "African Prose — Things Fall Apart"
T_SHK = "Shakespearean Drama"

PASSAGES = []
PQ = []

Q = [
    (T_FIG, "Easy", "A direct comparison in which one thing is simply called another, as 'Okonkwo was a flaming fire', is a",
     "metaphor", "simile",
     "hyperbole", "irony", "A",
     "The word 'like' never appears in it."),
    (T_FIG, "Easy", "'The wind whispered through the dark leaves' gives nature a human voice. The figure used is",
     "personification", "onomatopoeia",
     "metonymy", "litotes", "A",
     "The leaves are made to speak like a person."),
    (T_FIG, "Easy", "Saying 'I have told you a thousand times' when it was only twice is a figure of speech called",
     "hyperbole", "euphemism",
     "paradox", "pun", "A",
     "Deliberate overstatement for effect."),
    (T_FIG, "Medium", "Putting a mild word in place of a harsh one, as 'passed away' for 'died', is called",
     "euphemism", "hyperbole",
     "irony", "innuendo", "A",
     "A gentle veil drawn over a hard truth."),
    (T_FIG, "Hard", "Using 'the crown' to stand for the king and all royalty is a figure of speech known as",
     "metonymy", "synecdoche",
     "symbolism", "allegory", "A",
     "A closely linked thing stands for the whole."),
    (T_FIG, "Hard", "'All hands on deck', where a part stands for the whole crew, illustrates",
     "synecdoche", "metonymy",
     "oxymoron", "zeugma", "A",
     "The sailors are named by their hands."),
    (T_FIG, "Medium", "In 'parting is such sweet sorrow', two opposites are squeezed into one phrase. This is",
     "an oxymoron", "a paradox",
     "an antithesis", "a pun", "A",
     "Bitter and sweet sit side by side."),
    (T_FIG, "Easy", "Words chosen for their sound, like 'buzz', 'hiss' and 'crackle', are used for a device called",
     "onomatopoeia", "alliteration",
     "assonance", "refrain", "A",
     "The word performs its own meaning."),
    (T_FIG, "Easy", "The repetition of the same consonant sound at the start of neighbouring words, as 'the soft singing of the sea', is",
     "alliteration", "rhyme",
     "rhythm", "cadence", "A",
     "The first sound rings again and again."),
    (T_FIG, "Medium", "The audience knows the stranger is a thief while the hero warmly welcomes him in. The device at work is",
     "dramatic irony", "situational irony",
     "sarcasm", "suspense", "A",
     "The audience sees what the character cannot."),
    (T_FIG, "Hard", "A story in which every character and event stands for something beyond itself, like Pilgrim's Progress, is an",
     "allegory", "fable",
     "parable", "epic", "A",
     "The whole tale walks on two levels at once."),
    (T_DRA, "Medium", "The list of a play's characters printed before the dialogue begins is called the",
     "dramatis personae", "cast of prologue",
     "scenario", "prompt copy", "A",
     "The cast is named before the curtain rises."),
    (T_DRA, "Hard", "An unreal, sudden event that rescues a play from an impossible tangle is called",
     "deus ex machina", "comic relief",
     "denouement", "coup de theatre", "A",
     "A god lowered by crane to untie the knot."),
    (T_DRA, "Hard", "The purging of pity and fear that a good tragedy works in its audience is called",
     "catharsis", "pathos",
     "hubris", "mime", "A",
     "The heart is washed clean by sorrow."),
    (T_DRA, "Medium", "The error or flaw within the tragic hero that brings about his ruin is called",
     "hamartia", "hubris",
     "peripeteia", "anagnorisis", "A",
     "The hero carries his own seed of downfall."),
    (T_DRA, "Hard", "A polished play that mocks the manners, wit and fashion of a fashionable social class is a",
     "comedy of manners", "black comedy",
     "farce", "burlesque", "A",
     "Rapiers of wit flash over the teacups."),
    (T_POE, "Medium", "A poem or play that pictures shepherds and country life in a golden, idealised light is called",
     "a pastoral", "an ode",
     "an epithalamion", "a georgic satire", "A",
     "The shepherd's pipe never hits a sour note."),
    (T_POE, "Medium", "A poem written in mourning for someone who has died, often in quiet reflective tones, is an",
     "elegy", "ode",
     "ballad", "epitaph", "A",
     "Grief set to measured music."),
    (T_POE, "Medium", "A simple narrative poem that tells a folk story in song-like quatrains is a",
     "ballad", "lyric",
     "pastoral", "aubade", "A",
     "The old minstrels' tale carried in verse."),
    (T_POE, "Hard", "A poem in which a single speaker, unknowingly, reveals his own character while talking to a silent listener is a",
     "dramatic monologue", "soliloquy",
     "confessional lyric", "serenade", "A",
     "The speaker hangs himself with his own words."),
    (T_POE, "Medium", "When the sense of a line of verse runs straight on into the next line without pause, the device is",
     "enjambment", "caesura",
     "end-stopped line", "elision", "A",
     "The meaning strides past the line's end."),
    (T_POE, "Medium", "Poetry that flows freely without any regular metre or rhyme scheme is called",
     "free verse", "blank verse",
     "sprung verse", "doggerel", "A",
     "It rides on no fixed rail of rhyme."),
    (T_SHK, "Medium", "In Othello, the ensign who poisons the Moor's mind against the innocent Desdemona is",
     "Iago", "Cassio",
     "Roderigo", "Brabantio", "A",
     "'Honest Iago' is anything but honest."),
    (T_SHK, "Easy", "The prologue of Romeo and Juliet describes the young lovers as a pair who are",
     "star-crossed", "moon-struck",
     "sea-tossed", "night-bound", "A",
     "The stars, not the lovers, take the blame."),
    (T_SHK, "Medium", "In Macbeth, the glowing promises that set the hero on his bloody path come from",
     "the three witches", "the ghost of Duncan",
     "Lady Macbeth's doctor", "the prince of Norway", "A",
     "Fair is foul, and foul is fair."),
    (T_SHK, "Medium", "Julius Caesar cries 'Et tu, Brute!' when he spots Brutus among his",
     "assassins", "senators",
     "generals", "judges", "A",
     "Even his friend has joined the plot."),
    (T_AFR, "Medium", "In Things Fall Apart, Okonkwo's father Unoka was a man who loved",
     "wine and the flute", "yam barns and titles",
     "war and wrestling", "the church and books", "A",
     "He died owing every neighbour a debt."),
    (T_AFR, "Hard", "In Things Fall Apart, the masked spirits before whom the nine villages settle their disputes are the",
     "egwugwu", "chi",
     "ndichie", "obyra", "A",
     "Women and children flee when they come."),
    (T_AFR, "Easy", "In Things Fall Apart, the crop that above all others measures a man's wealth and manhood is",
     "yam", "cocoa",
     "palm produce", "cassava", "A",
     "Yam is the king of a man's crops."),
    (T_AFR, "Hard", "At the close of Things Fall Apart, the District Commissioner plans to give Okonkwo's story",
     "one paragraph in his book", "a whole chapter of praise",
     "a report to the missionaries", "a monument in the square", "A",
     "A whole life reduced to a paragraph."),
]

build_batch(
    S,
    "batch_193_waec_lit7.json",
    "193",
    "WAEC Literature round 7 (R37 top-up): metaphor; "
    "personification; hyperbole; euphemism; metonymy; synecdoche; "
    "oxymoron; onomatopoeia; alliteration; dramatic irony; "
    "allegory; dramatis personae; deus ex machina; catharsis; "
    "hamartia; comedy of manners; ode; elegy; ballad; dramatic "
    "monologue; enjambment; free verse; Iago; star-crossed "
    "lovers; Macbeth's witches; 'Et tu, Brute'; Unoka's flute; "
    "the egwugwu; yams; the District Commissioner's paragraph. "
    "Scanned against the whole Literature-in-English pool (WAEC "
    "and NECO stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
