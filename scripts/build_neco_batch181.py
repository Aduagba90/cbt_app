"""Batch 181 - NECO Literature round 5 (NECO top-up, R34).

Grows NECO Literature from 214 toward ~250 with angles not yet in
the bank: assonance; apostrophe to death; the rhetorical question;
litotes of no small feat; zeugma breaking car and heart;
caricature; the epitaph; the limerick; the oriki as panegyric;
scansion; internal and eye rhyme; the mystery plays; the theatre
of the absurd; black comedy; tragicomedy; parody; the gothic,
historical, science-fiction and detective novel; story against
plot; peripeteia; poetic justice; the proverb as palm-oil; Hubert
Ogunde's folk opera; The Trials of Brother Jero; A Raisin in the
Sun; The Merchant of Venice; the Iliad; Antigone; Lenrie Peters;
Birago Diop; Wordsworth; Dickens; Austen. Scanned against NECO
rounds 1-4, WAEC Literature (all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch181.py -> content/batch_181_neco_lit5.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Literature-in-English"

T_FIG = "Figures of Speech"
T_FIG2 = "Further Figures of Speech"
T_GEN = "General Literary Knowledge"
T_POE = "Poetry"
T_POC = "Poetry Craft"
T_DRA = "Drama"
T_DRV = "Drama Vocabulary"
T_PRO = "Prose"
T_ORA = "Oral Literature"
T_WAW = "Writers and Works"
T_WAW2 = "Writers and Works Further"

PASSAGES = []
PQ = []

Q = [
    (T_FIG, "Medium", "The echoing vowel sounds of 'deep green sleep' illustrate",
     "assonance", "alliteration",
     "consonance", "euphony of bells", "A",
     "The same vowel rings through the nearby words."),
    (T_FIG, "Medium", "In 'Death, be not proud', the poet speaks straight at death as though death were a person. The device is",
     "apostrophe", "aside",
     "allusion", "antithesis", "A",
     "The absent and the abstract are addressed aloud."),
    (T_FIG, "Easy", "A question asked for effect, which expects no answer, is called",
     "a rhetorical question", "an aside",
     "a soliloquy", "an epigram", "A",
     "The answer already lives in the asking."),
    (T_FIG2, "Hard", "Calling a great victory 'no small feat' is the figure of",
     "litotes", "hyperbole",
     "irony", "paradox", "A",
     "Praise sneaks in through a negative."),
    (T_FIG2, "Hard", "'She broke his car and his heart' yokes two objects to one verb. The device is",
     "zeugma", "metonymy",
     "synecdoche", "chiasmus", "A",
     "One verb drives two very different loads."),
    (T_GEN, "Medium", "A portrait in writing that wildly exaggerates a person's features for comic effect is a",
     "caricature", "character foil",
     "cameo role", "cartouche", "A",
     "The nose grows; the man shrinks."),
    (T_GEN, "Hard", "When the villain's own trap springs shut on him in the final scene, poetic",
     "justice has been served", "licence has been taken",
     "justice is delayed", "fallacy is exposed", "A",
     "Each recompense fits its deed exactly."),
    (T_POE, "Medium", "A short poem carved or written in memory of a dead person, often on a grave, is an",
     "epitaph", "epigram",
     "epilogue", "epithet", "A",
     "A few lines stand where the sleeper lies."),
    (T_POE, "Easy", "A five-line humorous verse, usually nonsense, with a bouncy rhyme scheme, is a",
     "limerick", "lyric",
     "ballad", "villanelle", "A",
     "There once was a form quite absurd..."),
    (T_POE, "Hard", "The Yoruba oriki chant, pouring lavish praise on its subject, belongs to the class of poems called",
     "panegyrics", "elegies",
     "satires", "aubades", "A",
     "Praise poetry crowns the honoured head."),
    (T_POC, "Hard", "Marking out a poem's metre, foot by foot and stress by stress, is the work of",
     "scansion", "prosody only",
     "versification licence", "prosody", "A",
     "The scanner counts the beats as they fall."),
    (T_POC, "Medium", "In 'Once upon a midnight dreary, while I pondered, weak and weary', the rhymes inside single lines are",
     "internal rhymes", "eye rhymes",
     "end rhymes", "half rhymes", "A",
     "Dreary and weary rhyme within the line itself."),
    (T_POC, "Hard", "'Love' and 'prove' look as if they rhyme on paper yet sound different when spoken. Such a pairing is an",
     "eye rhyme", "internal rhyme",
     "slant rhyme", "double rhyme", "A",
     "The eye is pleased; the ear is cheated."),
    (T_DRA, "Hard", "In medieval England, cycles of plays that retold Bible stories from creation to doomsday were the",
     "mystery plays", "morality plays",
     "masques", "interludes", "A",
     "Whole towns staged the sacred pageant."),
    (T_DRA, "Hard", "Drama in the manner of Waiting for Godot, where nothing resolves and characters talk in circles, belongs to the theatre of the",
     "absurd", "cruelty",
     "temperance", "revolt", "A",
     "Beckett's trunks never leave the road."),
    (T_DRA, "Medium", "A play that makes the audience laugh at death and disaster, subjects normally wept over, is",
     "black comedy", "sentimental drama",
     "melodrama", "farce", "A",
     "Laughter in the graveyard."),
    (T_DRA, "Medium", "A play that opens in tears and darkness yet closes in laughter and union is best described as a",
     "tragicomedy", "tragedy",
     "farce", "problem play", "A",
     "The storm spends itself in a wedding."),
    (T_DRA, "Medium", "A comic imitation that mocks a serious work by copying its style absurdly is a",
     "parody", "paraphrase",
     "pastoral", "parable", "A",
     "The copy laughs at its original."),
    (T_DRV, "Hard", "The sudden stroke of reversal in which the tragic hero's fortune turns in a moment is called",
     "peripeteia", "anagnorisis only",
     "catastrophe", "catharsis", "A",
     "At one turn the wheel flips the king."),
    (T_PRO, "Medium", "A novel of haunted castles, secret passages and nameless terrors, like Frankenstein, belongs to the",
     "gothic tradition", "picaresque tradition",
     "realist school", "stream school", "A",
     "Thunder always rolls over its towers."),
    (T_PRO, "Medium", "A novel whose story is set among documented events of a past age, real kings and real wars included, is",
     "a historical novel", "an autobiographical novel",
     "a detective novel", "an epistolary novel", "A",
     "The past is its stage and its proof."),
    (T_PRO, "Easy", "Stories of space travel, robots and imagined future worlds belong to",
     "science fiction", "detective fiction",
     "faction", "pastoral romance", "A",
     "Tomorrow furnishes its scenery."),
    (T_PRO, "Medium", "A novel that unravels a crime through clues and a sleuth's reasoning is",
     "detective fiction", "gothic fiction",
     "historical fiction", "metafiction", "A",
     "The reader races the detective to the answer."),
    (T_PRO, "Hard", "The raw events of a tale arranged in their simple time order form its story; when the author rearranges them for effect, the result is the",
     "plot", "theme",
     "setting", "subtext", "A",
     "Story is the wood; plot is the joinery."),
    (T_ORA, "Medium", "Among the Igbo of Achebe's world, the proverb is described as the palm-oil",
     "with which words are eaten", "that lights the shrine at dusk",
     "pressed for the king's table", "that anoints the newborn", "A",
     "Speech greased with proverb goes down well."),
    (T_ORA, "Hard", "The man regarded as the father of Nigerian folk opera, who staged Strike and Hunger in 1945, is",
     "Hubert Ogunde", "Ola Rotimi",
     "Wale Ogunyemi", "Duro Ladipo", "A",
     "His travelling troupe sang Nigeria awake."),
    (T_WAW, "Medium", "Wole Soyinka's comedy about the charlatan prophet Brother Jero is titled",
     "The Trials of Brother Jero", "The Lion and the Jewel",
     "A Dance of the Forests", "Kongi's Harvest", "A",
     "The beach prophet meets his match."),
    (T_WAW, "Medium", "The American play A Raisin in the Sun, about the Younger family's dream, was written by",
     "Lorraine Hansberry", "Arthur Miller",
     "Tennessee Williams", "August Wilson", "A",
     "A black family's dream defers no longer."),
    (T_WAW, "Medium", "In which Shakespeare play does the moneylender Shylock demand his pound of flesh?",
     "The Merchant of Venice", "The Tempest",
     "King Lear", "Julius Caesar", "A",
     "The bond names a pound of flesh."),
    (T_WAW, "Medium", "Homer's epic poem recounting the wrath of Achilles at the siege of Troy is the",
     "Iliad", "Odyssey",
     "Aeneid", "Divine Comedy", "A",
     "Ten years of war sing in its lines."),
    (T_WAW, "Hard", "The Sophocles tragedy in which a girl defies the king to bury her fallen brother is",
     "Antigone", "Medea",
     "Electra", "Oedipus at Colonus", "A",
     "She scattered dust on duty's side."),
    (T_WAW2, "Medium", "'The Panic of Growing Older', an anthology poem on ageing, was written by the Gambian poet",
     "Lenrie Peters", "David Diop",
     "Birago Diop", "Leopold Senghor", "A",
     "Its stanzas count the years' alarm."),
    (T_WAW2, "Hard", "'Vanity' and other poems mourning the loss of ancestral values were written by the Senegalese poet",
     "Birago Diop", "Lenrie Peters",
     "David Diop", "Wole Soyinka", "A",
     "His 'Vanished' voices echo through the poem."),
    (T_WAW2, "Easy", "The English Romantic poet who wandered 'lonely as a cloud' is",
     "William Wordsworth", "John Milton",
     "Alexander Pope", "Geoffrey Chaucer", "A",
     "His daffodils still flutter and dance."),
    (T_WAW2, "Easy", "Oliver Twist, the novel of the workhouse orphan, was written by",
     "Charles Dickens", "Jane Austen",
     "George Eliot", "Thomas Hardy", "A",
     "The boy who dared ask for more."),
    (T_WAW2, "Easy", "Pride and Prejudice, the novel of Elizabeth Bennet and Mr Darcy, is by",
     "Jane Austen", "Charlotte Bronte",
     "Emily Bronte", "Mary Shelley", "A",
     "A first impression slowly revised."),
]

build_batch(
    S,
    "batch_181_neco_lit5.json",
    "181",
    "NECO Literature round 5 (R34 top-up): assonance of deep green "
    "sleep; apostrophe to death; the rhetorical question; litotes "
    "of no small feat; zeugma of car and heart; caricature; poetic "
    "justice; the epitaph; the limerick; oriki as panegyric; "
    "scansion; internal and eye rhyme; the mystery plays; theatre "
    "of the absurd; black comedy; tragicomedy; parody; gothic, "
    "historical, science-fiction and detective novels; story "
    "against plot; peripeteia; the proverb as palm-oil; Ogunde's "
    "folk opera; The Trials of Brother Jero; A Raisin in the Sun; "
    "The Merchant of Venice; the Iliad; Antigone; Lenrie Peters; "
    "Birago Diop; Wordsworth's daffodils; Dickens's Oliver Twist; "
    "Austen's Pride and Prejudice. Scanned against NECO rounds "
    "1-4, WAEC Literature (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
