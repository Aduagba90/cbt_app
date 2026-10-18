"""Batch 092 - WAEC Literature-in-English round 2 (WAEC lift, Round 19).

WAEC Literature Paper 1 draws 50 items; the bank stood at 68. This lift adds
fresh items - catharsis, static character, symbolism, objective narration,
complication, external conflict; negritude and Senghor; more Achebe (No
Longer at Ease, Arrow of God, A Man of the People), The Concubine, Sozaboy,
Death and the King's Horseman, The Lion and the Jewel, Anthills; poets
Okigbo, Osundare, Abiku - scanned against WAEC r1, NECO rounds 1-2 and all
banks.

    python3 scripts/build_neco_batch92.py -> content/batch_092_waec_literature2.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Literature-in-English"

T_TER = "Literary Terms"
T_DRA = "Drama"
T_PRO = "Prose"
T_POE = "Poetry"
T_AFR = "African Literature"
T_TH = "Themes and Criticism"

PASSAGES = []
PQ = []

Q = [
    # ---------------------------------------------------------------- terms
    (T_TER, "Hard", "The purging of pity and fear that tragedy is expected to produce in the audience is",
     "catharsis", "pathos", "bathos", "hubris", "A",
     "Aristotle named the cleansing effect."),
    (T_TER, "Hard", "A character who remains exactly the same from the first page to the last is",
     "static", "round", "flat", "dynamic", "A",
     "No change marks the static figure."),
    (T_TER, "Medium", "An object that keeps standing for an idea all through a work is a",
     "symbol", "synonym", "synecdoche", "synopsis", "A",
     "The object carries the meaning."),
    (T_TER, "Hard", "A narrator who reports only what can be seen and heard, entering no mind, uses",
     "objective narration", "omniscient narration", "first-person narration", "second-person narration", "A",
     "The camera-eye tells all."),
    (T_TER, "Medium", "The events that entangle the conflict after the exposition are called the",
     "complication", "climax", "denouement", "flashback", "A",
     "Tangles thicken the plot."),
    (T_TER, "Medium", "A quarrel between the hero and his rival is an example of",
     "external conflict", "internal conflict", "internal", "psychological conflict", "A",
     "Two forces clash outside the mind."),
    (T_TER, "Easy", "The subject a work is about differs from its message, which is called the",
     "theme", "title", "topic", "plot", "A",
     "The theme is the central idea."),
    (T_TER, "Hard", "The pleasant, harmonious arrangement of sounds in a line is",
     "euphony", "cacophony", "onomatopoeia", "alliteration", "A",
     "Smooth sounds please the ear."),
    (T_TER, "Hard", "A sudden drop from the sublime to the ridiculous is",
     "bathos", "pathos", "ethos", "logos", "A",
     "The fall lands in laughter."),
    (T_TER, "Medium", "The arrangement of words in sentences, apart from their meaning, is",
     "syntax", "diction", "phonology", "semantics", "A",
     "Syntax is the word order."),
    # ---------------------------------------------------------------- drama
    (T_DRA, "Medium", "The central figure whose fate the audience follows most in a play is the",
     "protagonist", "antagonist", "narrator", "chorus", "A",
     "The story rides on his fortunes."),
    (T_DRA, "Hard", "The opening speech an actor delivers alone before the action begins is the",
     "prologue", "epilogue", "monologue", "dialogue", "A",
     "The prologue sets the stage."),
    (T_DRA, "Medium", "A speech delivered at the end of a play to round off the action is the",
     "epilogue", "prologue", "soliloquy", "aside", "A",
     "It bids the audience farewell."),
    (T_DRA, "Hard", "Sentimental drama with exaggerated suffering and impossible escapes is",
     "melodrama", "farce", "comedy", "tragedy", "A",
     "Tears flow over freely there."),
    (T_DRA, "Medium", "In drama, the term 'cast' refers to",
     "the actors and their roles", "the stage curtains", "the printed script", "the lighting crew", "A",
     "Casting assigns every role."),
    # ---------------------------------------------------------------- prose
    (T_PRO, "Hard", "A central character who lacks heroic virtues and may even be wicked is the",
     "anti-hero", "villain", "heroine", "foil", "A",
     "He leads without noble traits."),
    (T_PRO, "Hard", "A recurring image or idea that keeps appearing through a novel is a",
     "motif", "theme", "plot", "genre", "A",
     "The motif repeats with meaning."),
    (T_PRO, "Medium", "A story told inside the main story is",
     "an intercalary story", "an interlude", "an interval", "an interface", "A",
     "The inner tale enriches the frame."),
    (T_PRO, "Medium", "The physical setting of a novel refers to",
     "where the events happen", "when the events occur", "why the events occur", "who narrates the events", "A",
     "Place anchors the happenings."),
    (T_PRO, "Hard", "The unmistakable manner in which a writer handles language across all his works is his",
     "style", "genre", "plot", "audience", "A",
     "Style is the writer's fingerprint."),
    # ---------------------------------------------------------------- poetry
    (T_POE, "Hard", "The sonnet form that ends with a rhymed couplet is the",
     "Shakespearean", "Petrarchan", "Miltonic", "Spenserian", "A",
     "Three quatrains then a couplet."),
    (T_POE, "Hard", "A pause created within a line of verse, often by punctuation, is",
     "caesura", "enjambment", "cadence", "anapest", "A",
     "The pause cuts inside the line."),
    (T_POE, "Medium", "Two successive rhyming lines of verse form a",
     "couplet", "tercet", "quatrain", "sestet", "A",
     "A pair of lines closes the rhyme."),
    (T_POE, "Medium", "A long poem that tells a story in simple stanzas, often sung, is the",
     "ballad", "elegy", "ode", "epigram", "A",
     "Ballads sing the old stories."),
    (T_POE, "Hard", "In 'Abiku', the child that keeps dying and returning refers to an Ogbanje or spirit child. The poem was written by",
     "Wole Soyinka", "J.P. Clark", "Kofi Awoonor", "Lenrie Peters", "A",
     "Soyinka's Abiku is famous."),
    (T_POE, "Medium", "Christopher Okigbo, the poet of Labyrinths, died fighting for Biafra in",
     "the civil war", "a motor accident", "a plane crash abroad", "a flood disaster", "A",
     "He fell near the war's start."),
    (T_POE, "Hard", "The Nigerian poet Niyi Osundare is well known for",
     "songs of the people", "romances of the court", "nursery rhymes only", "Greek tragedies", "A",
     "His verse speaks for the common people."),
    # ---------------------------------------------------------------- african literature
    (T_AFR, "Hard", "The negritude movement, celebrating black culture, was led in poetry by",
     "Leopold Sedar Senghor", "Chinua Achebe", "Wole Soyinka", "Ngugi wa Thiong'o", "A",
     "The Senegalese poet-president led it."),
    (T_AFR, "Medium", "In No Longer at Ease, the grandson of Okonkwo who takes a bribe is",
     "Obi", "Uchendu", "Ikemefuna", "Unoka", "A",
     "Obi takes the bribe in Lagos."),
    (T_AFR, "Medium", "Arrow of God, the story of the priest Ezeulu, was written by",
     "Chinua Achebe", "Elechi Amadi", "Chukwuemeka Ike", "Isidore Okpewho", "A",
     "Achebe told Ezeulu's tragedy."),
    (T_AFR, "Medium", "A Man of the People, a satire on Nigerian politics, was written by",
     "Chinua Achebe", "Wole Soyinka", "Ola Rotimi", "Cyprian Ekwensi", "A",
     "Chief Nanga fills its pages."),
    (T_AFR, "Hard", "The Concubine, the story of the beautiful widow Ihuoma, was written by",
     "Elechi Amadi", "Chinua Achebe", "Flora Nwapa", "Buchi Emecheta", "A",
     "Amadi's Omokachi triangle."),
    (T_AFR, "Hard", "Sozaboy, the story of the young soldier Mene told in rotten English, is by",
     "Ken Saro-Wiwa", "Chinua Achebe", "Ben Okri", "Kole Omotoso", "A",
     "Saro-Wiwa invented the voice."),
    (T_AFR, "Medium", "In Death and the King's Horseman, the character bound to die with the king is",
     "Elesin", "Olunde", "Iyaloja", "Sidi", "A",
     "Elesin Oba owes the ritual death."),
    (T_AFR, "Easy", "In The Lion and the Jewel, the village belle who finally marries Baroka is",
     "Sidi", "Sadik", "Ailatou", "Aminata", "A",
     "Sidi chooses the lion at last."),
    (T_AFR, "Medium", "The young westernised schoolteacher of Ilujinle is",
     "Lakunle", "Baroka", "Sadiku", "Odun", "A",
     "Lakunle quotes books at Sidi."),
    (T_AFR, "Hard", "Anthills of the Savannah and The Famished Road are respectively by",
     "Achebe and Okri", "Okri and Achebe", "Soyinka and Achebe", "Ngugi and Okri", "A",
     "The pairing is Achebe first, Okri second."),
    (T_AFR, "Medium", "The setting of The Lion and the Jewel is a Yoruba village called",
     "Ilujinle", "Umuofia", "Yakoba", "Odani", "A",
     "The village opens the play."),
    # ---------------------------------------------------------------- themes and criticism
    (T_TH, "Medium", "Achebe's stated reason for writing was to teach Africans that their past was not",
     "one long night of savagery", "rich in heroes and arts", "full of wisdom and proverbs", "kind to their neighbours", "A",
     "He wrote against the slander."),
    (T_TH, "Medium", "Wole Soyinka's Nobel lecture and plays draw deeply on",
     "Yoruba myth and ritual", "Roman history", "Indian philosophy", "American legend", "A",
     "Ogun runs through his work."),
    (T_TH, "Medium", "The most reliable key to naming the theme of a poem is the poem's",
     "repeated images and final tone", "length of the lines", "date of publication", "name of the publisher", "A",
     "Patterns point to the message."),
    (T_TH, "Easy", "A story in which every element points to a second, hidden meaning throughout is an",
     "allegory", "analogy", "elegy", "epitaph", "A",
     "The whole tale carries a second tale."),
]

build_batch(
    S,
    "batch_092_waec_literature2.json",
    "092",
    "WAEC Literature round 2 (Round 19 lift): catharsis, static character, "
    "symbolism, objective narration, complication, external conflict, "
    "euphony, bathos, syntax; protagonist, prologue, epilogue, melodrama, "
    "cast; anti-hero, motif, intercalary story, physical setting; "
    "Shakespearean couplet, caesura, couplet, ballad, Soyinka's Abiku, "
    "Okigbo's Labyrinths, Osundare; negritude-Senghor, No Longer at Ease "
    "(Obi), Arrow of God (Ezeulu), A Man of the People, The Concubine "
    "(Ihuoma), Sozaboy (Mene), Death and the King's Horseman (Elesin), The "
    "Lion and the Jewel (Sidi, Lakunle, Ilujinle), Anthills pairing; "
    "Achebe's purpose, Soyinka's Yoruba roots, theme-spotting, allegory. "
    "Scanned against WAEC r1, NECO rounds 1-2 and all banks.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
