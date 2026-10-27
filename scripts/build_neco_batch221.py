"""Batch 221 - NECO Literature round 6 (NECO top-up, R44).

Grows NECO Literature from 250 toward ~275. The Literature pool
(1,268 items across JAMB, WAEC and NECO) is nearly saturated for
literary devices, so this batch leans on fresh author-work pairs and
verified-absent general terms. Pairs: People of the City (Ekwensi);
The Old Man and the Sea (Hemingway); Paradise Lost (Milton); Anowa
and The Dilemma of a Ghost (Aidoo); The Potter's Wheel (Ike);
Second-Class Citizen (Emecheta); The Stillborn (Alkali); Once Upon
Four Robbers (Osofisan); Americanah (Adichie); So Long a Letter
(Mariama Ba); Kongi's Harvest (Soyinka); Our Husband Has Gone Mad
Again (Rotimi). Terms: poetic licence; eponymous; dumb show;
improvisation; props; doggerel; poetic diction; lullaby; work song;
magic realism; utopia; slapstick. Checked and avoided (already
banked): dramatis personae, dystopia, Ozidi epic item, Okigbo,
River Between, Ovonramwen, Jagua Nana, No Longer at Ease, Arrow of
God, Man of the People, Romeo and Juliet star-crossed, Ozidi, all
major figures of speech, unities, negritude, juxtaposition,
closet drama, end-stopped/enjambment, blank verse, conceit, bathos,
deus ex machina, comedy of manners, mime, idyll, caricature,
anti-hero, palm-oil proverb, moonlight tales.

    python3 scripts/build_neco_batch221.py -> content/batch_221_neco_lit6.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Literature-in-English"

T_WW = "Writers and Works"
T_WWF = "Writers and Works Further"
T_AL = "African Literature"
T_PROSE = "Prose"
T_DRAMA = "Drama"
T_DV = "Drama Vocabulary"
T_POET = "Poetry"
T_PC = "Poetry Craft"
T_ORAL = "Oral Literature"
T_GENRE = "Forms and Genres"

PASSAGES = []
PQ = []

Q = [
    (T_WW, "Easy", "The Old Man and the Sea, the story of the fisherman Santiago's long struggle with a giant marlin, was written by",
     "Ernest Hemingway", "William Golding",
     "John Steinbeck", "Mark Twain", "A",
     "Santiago's epic duel with the fish fills the slim book."),
    (T_WW, "Medium", "Paradise Lost, the epic poem of Satan's rebellion and the fall of Adam and Eve from Eden, was written by",
     "John Milton", "Geoffrey Chaucer",
     "Alexander Pope", "John Keats", "A",
     "The blind English poet dictated its blank verse."),
    (T_AL, "Medium", "Cyprian Ekwensi's early novel of Lagos life, whose hero is the crime reporter Amusa Sango, is",
     "People of the City", "Jagua Nana",
     "The Burning Grass", "Beautiful Feathers", "A",
     "Amusa Sango chases crime through the young city."),
    (T_AL, "Medium", "Ama Ata Aidoo's play about the proud village girl who scorns custom to marry the trader Kofi Ako and ends in ruin is",
     "Anowa", "The Dilemma of a Ghost",
     "Our Sister Killjoy", "Changes", "A",
     "Anowa's headstrong path leads her to a bitter end."),
    (T_AL, "Medium", "Ama Ata Aidoo's first play, in which the student Ato Yawson returns from America with a Black American wife, is",
     "The Dilemma of a Ghost", "Anowa",
     "The Marriage of Anansewa", "The Lion and the Jewel", "A",
     "The ghost of tradition haunts the young couple's home."),
    (T_AL, "Medium", "Chukwuemeka Ike's humorous novel in which the stubborn boy Obu is sent from home to serve the strict Teacher Zaccheus is",
     "The Potter's Wheel", "The Naked Gods",
     "Toads for Supper", "The Concubine", "A",
     "The potter's wheel shapes clay as school shapes the boy."),
    (T_AL, "Medium", "Buchi Emecheta's novel in which Adah struggles to survive, study and write in London with her young children is",
     "Second-Class Citizen", "The Joys of Motherhood",
     "The Bride Price", "Gwendolen", "A",
     "Adah refuses the label that London pins on her."),
    (T_AL, "Hard", "Zaynab Alkali's novel about three village girls, Li, Awa and Faku, and the dreams they carry, is",
     "The Stillborn", "The Virtuous Woman",
     "Cobwebs and Other Stories", "The Descendants", "A",
     "A dream that dies before it is born titles the book."),
    (T_AL, "Hard", "Femi Osofisan's play in which four condemned armed robbers tell their stories before a firing squad, questioning justice under a military regime, is",
     "Once Upon Four Robbers", "Morountodun",
     "Midnight Hotel", "The Chattering and the Song", "A",
     "The executioner's drums open and close the play."),
    (T_WW, "Easy", "Chimamanda Ngozi Adichie's novel in which Ifemelu returns to Nigeria after years in America, famous for her blog on race, is",
     "Americanah", "Half of a Yellow Sun",
     "Purple Hibiscus", "The Thing Around Your Neck", "A",
     "Ifemelu's sharp blog posts give the book its name."),
    (T_AL, "Medium", "Mariama Ba's novel written as one long letter from the newly widowed Ramatoulaye to her friend Aissatou is",
     "So Long a Letter", "Scarlet Song",
     "The Joys of Motherhood", "Efuru", "A",
     "Her notebooks carry her thoughts to her friend."),
    (T_AL, "Hard", "In Wole Soyinka's play, the military ruler President Kongi awaits the new-yam festival that will crown his power over the kingdom of Isma. The play is",
     "Kongi's Harvest", "A Dance of the Forests",
     "Madmen and Specialists", "Death and the King's Horseman", "A",
     "The dictator wants the harvest to crown his rule."),
    (T_WWF, "Medium", "Ola Rotimi's comedy in which the retired Major Lejoka-Brown throws himself into election politics with disastrous results is",
     "Our Husband Has Gone Mad Again", "Kurunmi",
     "If: A Tragedy of the Ruled", "Hopes of the Living Dead", "A",
     "The Major's politics turns his household upside down."),
    (T_PC, "Medium", "The freedom a poet or novelist allows himself to bend facts and break ordinary rules for the sake of artistic effect is called",
     "poetic licence", "poetic justice",
     "poetic diction", "plagiarism", "A",
     "Art may stretch truth where plain record may not."),
    (T_PROSE, "Easy", "A work named after its main character, as Oliver Twist is named after the orphan boy, is said to be",
     "eponymous", "anonymous",
     "pseudonymous", "synonymous", "A",
     "The hero's own name stands on the title page."),
    (T_DRAMA, "Medium", "A short dramatic scene performed entirely in silence, without any spoken words, is called a",
     "dumb show", "soliloquy",
     "aside", "chorus", "A",
     "Hands and faces speak where no voice is heard."),
    (T_DRAMA, "Easy", "Actors who invent their words and movements on the spot, without any prepared script, are said to be performing",
     "improvisation", "recitation",
     "interpretation", "repetition", "A",
     "The scene is born fresh at every performance."),
    (T_DV, "Easy", "Movable objects handled by actors during a performance, such as fans, letters and walking sticks, are called",
     "props", "scenery",
     "costumes", "make-up", "A",
     "The actor picks them up and uses them on stage."),
    (T_POET, "Medium", "Light verse of rough, careless rhythm, written for laughter rather than for serious art, is called",
     "doggerel", "an elegy",
     "a dirge", "blank verse", "A",
     "Its clumsy lines are loved for their fun."),
    (T_PC, "Hard", "The special, often elevated choice of words and phrasing that belongs to poetry rather than to everyday speech is called",
     "poetic diction", "poetic licence",
     "poetic justice", "rhetoric", "A",
     "Poets dress ideas in words beyond daily talk."),
    (T_ORAL, "Easy", "A soft, rocking song sung by a mother to soothe her baby to sleep is a",
     "lullaby", "limerick",
     "lyric", "dirge", "A",
     "Its gentle rhythm nods the child off to sleep."),
    (T_ORAL, "Easy", "A song sung in rhythm by workers at a shared task, such as paddling a canoe or pounding cassava, to make the labour lighter is a",
     "work song", "war song",
     "praise song", "lullaby", "A",
     "The beat of the song sets the pace of the work."),
    (T_GENRE, "Hard", "A style of fiction in which spirits and the living mix as a matter of course, as in Ben Okri's The Famished Road, is called",
     "magic realism", "science fiction",
     "naturalism", "romanticism", "A",
     "The spirit world walks in without any surprise."),
    (T_GENRE, "Easy", "An imagined perfect society, in which everything is arranged for the good of all, is called a",
     "utopia", "dystopia",
     "pastoral", "gothic", "A",
     "The word paints a nowhere land free of all ills."),
    (T_DRAMA, "Medium", "Broad physical comedy built on falls, chases, collisions and harmless beatings is called",
     "slapstick", "black comedy",
     "satire", "tragicomedy", "A",
     "The humour lands in bumps and pratfalls."),
]

build_batch(
    S,
    "batch_221_neco_lit6.json",
    "221",
    "NECO Literature round 6 (R44 top-up): 13 fresh author-work "
    "pairs (People of the City; Old Man and the Sea; Paradise Lost; "
    "Anowa; Dilemma of a Ghost; Potter's Wheel; Second-Class "
    "Citizen; The Stillborn; Once Upon Four Robbers; Americanah; So "
    "Long a Letter; Kongi's Harvest; Our Husband Has Gone Mad "
    "Again) plus poetic licence; eponymous; dumb show; "
    "improvisation; props; doggerel; poetic diction; lullaby; work "
    "song; magic realism; utopia; slapstick. Scanned against the "
    "whole Literature pool (JAMB, WAEC and NECO stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
