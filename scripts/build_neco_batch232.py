"""Batch 232 - WAEC Literature round 7 (WAEC top-up, R47).

Grows WAEC Literature from 267 toward ~292 with angles verified
absent from the whole Literature pool (1,293 items across JAMB, WAEC
and NECO). The devices shelf is saturated, so this batch leans on
fresh author-work pairs and a few fresh terms. Pairs: Cry, the
Beloved Country (Paton); A Tale of Two Cities (Dickens); The Great
Gatsby (Fitzgerald); The Scarlet Letter (Hawthorne); Moby Dick
(Melville); The Adventures of Huckleberry Finn (Twain); The Crucible
(Miller); Doctor Faustus (Marlowe); The Importance of Being Earnest
(Wilde); Pygmalion (Shaw); Murder in the Cathedral (Eliot); Twelfth
Night (Shakespeare); A Grain of Wheat (Ngugi); The Last Duty
(Okpewho); Idu (Nwapa); Ekwefi and Ezinma (Things Fall Apart);
Obierika (Things Fall Apart); Season of Migration to the North
(Salih); Devil on the Cross (Ngugi). Terms: synaesthesia;
verisimilitude; willing suspension of disbelief; proscenium/thrust
stage; prompter; understudy. Checked and avoided (already banked):
haiku, morality/mystery plays, confidant, unreliable narrator,
static character, nemesis/anagnorisis/peripeteia (options), epigram,
eulogy, heroic couplet, volta, sonnet types, concrete poem,
rising/falling action, inciting incident, third person limited,
point of view, Xala/Petals/Ozidi/Great Ponds/Toads/Hopes/Raft/Sister
Killjoy/Thing Around Your Neck (option-only mentions), Waiting for
Godot theatre-of-absurd item, Tempest (option), Jane Eyre/Wuthering
Heights families, Hamlet/Othello/King Lear items, Anthills paired
item, To Kill a Mockingbird (7), Great Expectations (option), Bride
Price (5), Voice/persona items.

    python3 scripts/build_neco_batch232.py -> content/batch_232_waec_lit7.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Literature-in-English"

T_WW = "Writers and Works"
T_AWW = "African Writers and Works"
T_TFA = "African Prose — Things Fall Apart"
T_SH = "Shakespearean Drama"
T_FIG = "Figures of Speech"
T_LT = "Literary Terms"
T_DT = "Drama Terms"

PASSAGES = []
PQ = []

Q = [
    (T_WW, "Medium", "Cry, the Beloved Country, the novel of the Reverend Kumalo's journey through a broken South Africa in search of his son, was written by",
     "Alan Paton", "Nadine Gordimer",
     "Joseph Conrad", "Doris Lessing", "A",
     "The parson's road to Johannesburg broke his heart."),
    (T_WW, "Medium", "A Tale of Two Cities, the novel of Sydney Carton's sacrifice set in London and Paris during the French Revolution, was written by",
     "Charles Dickens", "William Makepeace Thackeray",
     "George Eliot", "Thomas Hardy", "A",
     "'It is a far, far better thing that I do...'"),
    (T_WW, "Medium", "The Great Gatsby, the tragedy of the mysterious millionaire Jay Gatsby and the green light across the bay, was written by",
     "F. Scott Fitzgerald", "Ernest Hemingway",
     "John Steinbeck", "Theodore Dreiser", "A",
     "The parties were loud; the dream was doomed."),
    (T_WW, "Medium", "The Scarlet Letter, in which Hester Prynne is made to wear a letter of shame in Puritan New England, was written by",
     "Nathaniel Hawthorne", "Herman Melville",
     "Edgar Allan Poe", "Henry James", "A",
     "One embroidered letter branded a whole town's conscience."),
    (T_WW, "Medium", "Moby Dick, the epic pursuit of the great white whale by the obsessed Captain Ahab, was written by",
     "Herman Melville", "Nathaniel Hawthorne",
     "Joseph Conrad", "Robert Louis Stevenson", "A",
     "Call him the captain; the whale was his fate."),
    (T_WW, "Easy", "The Adventures of Huckleberry Finn, the story of the boy who sails a raft down the Mississippi with the runaway slave Jim, was written by",
     "Mark Twain", "Henry David Thoreau",
     "Jack London", "Washington Irving", "A",
     "The river carried the boy and the story of America."),
    (T_WW, "Medium", "The Crucible, the play that uses the Salem witch trials to attack the witch-hunts of its own day, was written by",
     "Arthur Miller", "Tennessee Williams",
     "Eugene O'Neill", "Edward Albee", "A",
     "He wrote of 1692 and meant the 1950s."),
    (T_WW, "Hard", "Doctor Faustus, the tragedy of the scholar who sells his soul to the devil for twenty-four years of power, was written by",
     "Christopher Marlowe", "Ben Jonson",
     "John Webster", "Thomas Kyd", "A",
     "'Was this the face that launched a thousand ships?'"),
    (T_WW, "Medium", "The Importance of Being Earnest, the comedy of mistaken identities in which both Jack and Algernon invent convenient alter egos, was written by",
     "Oscar Wilde", "George Bernard Shaw",
     "Noel Coward", "Richard Brinsley Sheridan", "A",
     "A handbag at Victoria Station began it all."),
    (T_WW, "Medium", "Pygmalion, the play in which Professor Higgins trains the flower girl Eliza Doolittle to speak like a duchess, was written by",
     "George Bernard Shaw", "Oscar Wilde",
     "John Galsworthy", "J. M. Synge", "A",
     "The rain in Spain stays mainly in the plain."),
    (T_WW, "Hard", "Murder in the Cathedral, the verse tragedy of Archbishop Thomas Becket's killing in his own cathedral, was written by",
     "T. S. Eliot", "W. B. Yeats",
     "Christopher Fry", "Dylan Thomas", "A",
     "'This is one moment, but know that another shall follow.'"),
    (T_SH, "Medium", "The Shakespeare comedy in which the twins Viola and Sebastian, shipwrecked separately in Illyria, cause a merry tangle of mistaken love before all is resolved, is",
     "Twelfth Night", "As You Like It",
     "The Tempest", "The Winter's Tale", "A",
     "Malvolio's yellow stockings still make audiences laugh."),
    (T_AWW, "Medium", "Ngugi wa Thiong'o's novel of Kenya's struggle for independence, centred on the fighter Gikonyo and his wife Mumbi, is",
     "A Grain of Wheat", "Weep Not, Child",
     "The River Between", "Petals of Blood", "A",
     "The wheel of Kenya's story turns on Uhuru day."),
    (T_AWW, "Hard", "Isidore Okpewho's novel of the civil war, told through the diaries and voices of those around a border town, is",
     "The Last Duty", "The Concubine",
     "The Potter's Wheel", "Sozaboy", "A",
     "Each narrator carries one piece of the war."),
    (T_AWW, "Hard", "Flora Nwapa's sequel to Efuru, the story of the dutiful wife Idu and her husband Adiewere, is titled",
     "Idu", "Never Again",
     "Women are Different", "One is Enough", "A",
     "Idu's devotion to Adiewere fills the tale."),
    (T_TFA, "Medium", "In Things Fall Apart, Okonkwo's second wife, the mother of his daughter Ezinma, is",
     "Ekwefi", "Ojiugo",
     "Ojugo's sister", "Chielo", "A",
     "She lost nine children and loved the tenth fiercely."),
    (T_TFA, "Easy", "In Things Fall Apart, Okonkwo's close friend who questions the new order and refuses to join the killing of the messenger is",
     "Obierika", "Unoka",
     "Ikemefuna", "Nwakibie", "A",
     "He saw both worlds and mourned the clash."),
    (T_AWW, "Hard", "Season of Migration to the North, the novel of the Sudanese scholar who returns from Europe to his village on the Nile, was written by",
     "Tayeb Salih", "Naguib Mahfouz",
     "Chinua Achebe", "Ayub Kwei Armah", "A",
     "The journey north and back unmade him."),
    (T_AWW, "Medium", "Devil on the Cross, which Ngugi wa Thiong'o wrote in Gikuyu on prison toilet paper, is a satire on",
     "the worshippers of money in Kenya", "the building of the railway line",
     "the Mau Mau war only", "colonial schools and missions", "A",
     "The devil's feast crowns the thief of the age."),
    (T_FIG, "Hard", "The figure of speech in which one sense is described in the terms of another, as in 'a loud colour' or 'a sweet voice', is",
     "synaesthesia", "synecdoche",
     "assonance", "hyperbole", "A",
     "The ear tastes and the eye listens."),
    (T_LT, "Hard", "The quality that makes a work of fiction feel true to life, so that readers accept its world as believable while they read it, is called",
     "verisimilitude", "versatility",
     "veracity of record", "verbosity", "A",
     "The made-up world must ring true to hold us."),
    (T_LT, "Medium", "Coleridge said readers grant the poet a temporary willingness to believe even the improbable for the sake of enjoyment. He called this the",
     "willing suspension of disbelief", "willing surrender of knowledge",
     "wilful blindness of the reader", "wise suspension of judgment", "A",
     "We agree to believe while the poem lasts."),
    (T_DT, "Hard", "The arch that frames the stage in a traditional theatre, separating the actors' world from the audience's, is called the",
     "proscenium arch", "prompt arch",
     "pergola of stage", "proscenium of sound", "A",
     "The audience peeps through it into another room."),
    (T_DT, "Medium", "The person who sits hidden beside the stage during a play, ready to whisper a forgotten line to an actor, is the",
     "prompter", "producer",
     "director", "stage manager", "A",
     "The unseen voice saves the scene."),
    (T_DT, "Medium", "An actor who learns another actor's part so that he can step in if the lead falls ill is called the",
     "understudy", "understudy of stage only",
     "under-agent", "understudy in the pit", "A",
     "He waits each night, ready to become the hero."),
]

build_batch(
    S,
    "batch_232_waec_lit7.json",
    "232",
    "WAEC Literature round 7 (R47 top-up): fresh pairs - Cry, the "
    "Beloved Country; A Tale of Two Cities; The Great Gatsby; The "
    "Scarlet Letter; Moby Dick; Huckleberry Finn; The Crucible; "
    "Doctor Faustus; The Importance of Being Earnest; Pygmalion; "
    "Murder in the Cathedral; Twelfth Night; A Grain of Wheat; The "
    "Last Duty; Idu; Ekwefi and Ezinma; Obierika; Season of "
    "Migration to the North; Devil on the Cross. Terms - "
    "synaesthesia; verisimilitude; willing suspension of disbelief; "
    "proscenium arch; prompter; understudy. Scanned against the "
    "whole Literature pool (JAMB, WAEC and NECO stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
