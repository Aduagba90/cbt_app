"""Batch 153 - NECO Literature-in-English round 4 (NECO top-up, R28).

Grows NECO Literature from 177 toward ~213 with angles not yet in the
bank: drama technique further (aside, comic relief, foil, hamartia,
hubris, deus ex machina, climax, exposition, farce); poetry craft
(blank verse, free verse, enjambment, caesura, dramatic monologue,
antithesis, epigram, imagery, symbolism, tone, lyric, the epic and
its griot); prose further (antagonist, round character, satire,
verbal and situational irony, subplot, first-person narrator,
novella); and writer-work pairs (Tutuola, Okri, Adichie, Nwapa,
Ngugi, Soyinka, Rotimi, Saro-Wiwa). Scanned against NECO rounds 1-3,
WAEC Literature (all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch153.py -> content/batch_153_neco_lit4.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Literature-in-English"

T_DR = "Drama Technique Further"
T_PO = "Poetry Craft"
T_PR = "Prose Further"
T_WW = "Writers and Works Further"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- drama
    (T_DR, "Medium", "Turning briefly to the stalls while his fellows on stage carry on unaware, an actor delivers a quiet remark called an",
     "aside", "soliloquy", "dialogue", "epilogue", "A",
     "A whisper thrown to the house."),
    (T_DR, "Medium", "A funny scene slipped into a serious play to ease tension is",
     "comic relief", "tragic flaw", "dramatic irony", "interlude of fate", "A",
     "Laughter lets the wound breathe."),
    (T_DR, "Hard", "A character set beside the hero to make his qualities shine brighter is his",
     "foil", "confidant", "chorus", "understudy", "A",
     "Dull silver makes gold gleam."),
    (T_DR, "Hard", "The hero's own error or weakness that brings his downfall is his",
     "hamartia", "hubris", "catharsis", "anagnorisis", "A",
     "The crack within brings the fall."),
    (T_DR, "Hard", "Overweening pride that courts destruction, the mark of many a tragic hero, is called",
     "hubris", "hamartia", "pathos", "peripeteia", "A",
     "He climbed too high on self-love."),
    (T_DR, "Hard", "An unexpected power or event that suddenly rescues characters from an impossible corner is",
     "deus ex machina", "denouement", "dramatic irony", "deus vobiscum", "A",
     "A god lowered by a crane."),
    (T_DR, "Medium", "The point of highest tension in a play, after which the end hastens, is the",
     "climax", "exposition", "prologue", "intermission", "A",
     "The wave crests before it breaks."),
    (T_DR, "Medium", "The opening part of a play that introduces characters and setting is the",
     "exposition", "climax", "denouement", "catastrophe", "A",
     "The lay of the land comes first."),
    (T_DR, "Medium", "A play built on absurd exaggeration and ridiculous situations, all for laughter, is a",
     "farce", "tragedy", "melodrama", "masque", "A",
     "Doors slam, trousers fall."),

    # ------------------------------------------------------------- poetry
    (T_PO, "Hard", "Lines of ten syllables each, unrhymed, in the pattern of much English drama, make up",
     "blank verse", "free verse", "heroic couplet", "rhyme royal", "A",
     "Shakespeare's chosen stride."),
    (T_PO, "Hard", "Poetry that follows no fixed metre or rhyme scheme is written in",
     "free verse", "blank verse", "couplets", "sestets", "A",
     "It walks barefoot, its own law."),
    (T_PO, "Hard", "When a sentence runs on past the end of a line into the next, the device is",
     "enjambment", "caesura", "end-stopping", "elision", "A",
     "The line leaps its own border."),
    (T_PO, "Hard", "A firm pause placed within a single line of verse is a",
     "caesura", "couplet", "cadence", "canto", "A",
     "A breath held in mid-line of verse."),
    (T_PO, "Hard", "A poem in which one speaker talks throughout to a silent listener, revealing himself, is a",
     "dramatic monologue", "soliloquy", "serenade", "epistle", "A",
     "One mouth, one unwitting confession."),
    (T_PO, "Hard", "'To err is human, to forgive divine' balances two opposed ideas in one breath. The device is",
     "antithesis", "synecdoche", "litotes", "apostrophe", "A",
     "Two weights on one scale."),
    (T_PO, "Medium", "A short, witty saying, often in verse and ending in a pointed turn, is an",
     "epigram", "elegy", "epic", "eclogue", "A",
     "A little dagger in a sentence."),
    (T_PO, "Medium", "Words that summon pictures in the reader's mind collectively form a poem's",
     "imagery", "diction", "cadence", "scansion", "A",
     "The mind's eye does the seeing."),
    (T_PO, "Hard", "In many African poems, the tortoise stands for cunning and the eagle for pride. Such standing-for makes them",
     "symbols", "similes", "allusions", "analogues", "A",
     "The creature carries a meaning."),
    (T_PO, "Medium", "The writer's attitude towards his subject, heard through the words, is the",
     "tone", "theme", "plot", "mood only", "A",
     "Anger, pity or scorn shows."),
    (T_PO, "Medium", "A short poem expressing personal feeling, meant to be sung in ancient times, is a",
     "lyric", "ballad", "epic", "satire", "A",
     "The lyre once walked with it."),
    (T_PO, "Hard", "A long narrative poem on the deeds of a great hero, preserved by a griot, is an",
     "epic", "ode", "sonnet", "dirge", "A",
     "Sundiata rides its lines."),

    # ------------------------------------------------------------- prose
    (T_PR, "Medium", "The character set against the protagonist, working to frustrate him, is the",
     "antagonist", "foil", "narrator", "confidant", "A",
     "The wall he must break through."),
    (T_PR, "Hard", "A character drawn with many traits, capable of surprising the reader, is a",
     "round character", "flat character", "stock character", "caricature", "A",
     "Life's full mixture moves him."),
    (T_PR, "Medium", "A work that mocks vice and folly to correct them, often with sharp wit, is a",
     "satire", "eulogy", "elegy", "idyll", "A",
     "Laughter with a whip in it."),
    (T_PR, "Hard", "Saying one thing while meaning its opposite, as when a failed cook calls his burnt pot 'a masterpiece', is",
     "verbal irony", "dramatic irony", "situational irony", "sarcasm-free wit", "A",
     "The tongue winks at the truth."),
    (T_PR, "Hard", "A fire station burning down on inspection day is the classic instance of",
     "situational irony", "verbal irony", "dramatic irony", "litotes", "A",
     "The event mocks all expectation."),
    (T_PR, "Medium", "A secondary strand of story running beside the main one is the",
     "subplot", "prologue", "motif", "climax", "A",
     "A smaller river beside the main."),
    (T_PR, "Medium", "A novel told by a character who says 'I' throughout uses",
     "first-person narration", "omniscient narration", "third-person narration", "objective narration", "A",
     "One pair of eyes sees all."),
    (T_PR, "Medium", "Longer than a short story yet too brief for a full-length novel, such a work belongs to the genre called",
     "novella", "trilogy", "anthology", "almanac", "A",
     "The middle child of prose."),

    # ------------------------------------------------------------- writers & works
    (T_WW, "Hard", "The Palm-Wine Drinkard, a tale of a drinkard following his tapster into the bush of ghosts, was written by",
     "Amos Tutuola", "Chinua Achebe", "Cyprian Ekwensi", "Gabriel Okara", "A",
     "His English walked like a spirit."),
    (T_WW, "Hard", "The Famished Road, narrated by the abiku spirit-child Azaro, is the novel of",
     "Ben Okri", "Wole Soyinka", "Ayi Kwei Armah", "Buchi Emecheta", "A",
     "The spirit child refused to stay."),
    (T_WW, "Hard", "Half of a Yellow Sun, set in the Biafran war years, is by the author of",
     "Purple Hibiscus", "The Joys of Motherhood", "Efuru", "Sozaboy", "A",
     "Adichie revisited the war."),
    (T_WW, "Hard", "Efuru, the story of a beautiful independent trader of the riverine area, was written by",
     "Flora Nwapa", "Zaynab Alkali", "Adaora Lily Ulasi", "Mabel Segun", "A",
     "Nigeria's pioneer woman novelist."),
    (T_WW, "Hard", "Weep Not, Child, the story of Njoroge's schooling destroyed by conflict, came from the pen of",
     "Ngugi wa Thiong'o", "Okot p'Bitek", "Leonard Kibera", "Meja Mwangi", "A",
     "Kenya's emergency years form it."),
    (T_WW, "Hard", "Elesin Oba, bidden to follow his dead king through the final gate, hesitates and fails. The play telling this story is",
     "Death and the King's Horseman", "Song of a Goat", "The Raft", "The Prodigal", "A",
     "Soyinka wrote it from a true Oyo episode."),
    (T_WW, "Hard", "Kurunmi, the play of the Ijebu war hero's clash with Ibadan, was written by",
     "Ola Rotimi", "Wole Soyinka", "Hubert Ogunde", "Dapo Adelugba", "A",
     "Rotimi staged the fall of a warrior."),
    (T_WW, "Hard", "Sozaboy, a novel of an illiterate boy soldier told in 'rotten English', is the work of",
     "Ken Saro-Wiwa", "Chinua Achebe", "Elechi Amadi", "Kole Omotoso", "A",
     "Its broken tongue bore the war."),
]

build_batch(
    S,
    "batch_153_neco_lit4.json",
    "153",
    "NECO Literature round 4 (R28 top-up): aside, comic relief, foil, "
    "hamartia, hubris, deus ex machina, climax, exposition, farce; "
    "blank verse, free verse, enjambment, caesura, dramatic monologue, "
    "antithesis, epigram, imagery, symbolism, tone, lyric, epic and "
    "griot; antagonist, round character, satire, verbal and "
    "situational irony, subplot, first-person narration, novella; "
    "Tutuola's Palm-Wine Drinkard, Okri's Famished Road, Adichie's "
    "Half of a Yellow Sun, Nwapa's Efuru, Ngugi's Weep Not, Child, "
    "Soyinka's Death and the King's Horseman, Rotimi's Kurunmi, "
    "Saro-Wiwa's Sozaboy. Scanned against NECO rounds 1-3, WAEC "
    "Literature (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
