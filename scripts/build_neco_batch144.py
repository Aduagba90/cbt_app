"""Batch 144 - WAEC Civic Education round 5 (WAEC top-up, R27).

Grows WAEC Civic from 171 toward ~208 with angles not yet in the
bank: duties of citizens (tax, obedience, voting, national service);
acquisition and loss of citizenship; the constitutional amendment
route; the legislative journey of a bill, veto override and recall;
election petition tribunals and INEC's boundaries; party registration
requirements; federal character, quota and national integration;
national symbols (flag, coat of arms, pledge, NYSC); FRSC; EFCC vs
ICPC; Code of Conduct; values (contentment, integrity, discipline);
representative vs direct democracy; features of free elections;
UDHR; human-rights limits. Scanned against WAEC rounds 1-4, NECO
Civic (all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch144.py -> content/batch_144_waec_civic5.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Civic Education"

T_DUT = "Duties and Obligations of Citizens"
T_CIT = "Citizenship"
T_LEGI = "The Legislature at Work"
T_ELEC = "Election Machinery"
T_INT = "Federal Character and Integration"
T_SYM = "National Symbols and Service"
T_ANTIG = "Anti-Corruption and Conduct"
T_VAL = "Civic Values"
T_DEM = "Democracy Deepened"
T_HR = "Human Rights Instruments"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- duties
    (T_DUT, "Medium", "Paying income tax honestly, when due, is primarily a citizen's",
     "legal duty", "optional kindness", "party obligation", "family tradition", "A",
     "The law demands it and services run on it."),
    (T_DUT, "Medium", "Respecting the national flag and anthem at public events expresses a citizen's",
     "duty of loyalty", "duty to a party", "right to protest", "freedom of worship", "A",
     "Small honours build one nation."),
    (T_DUT, "Hard", "Graduates serving under the NYSC scheme are performing a civic obligation of",
     "national service", "forced labour", "military conscription", "party mobilisation", "A",
     "The corps builds bridges across states."),

    # ------------------------------------------------------------- citizenship
    (T_CIT, "Hard", "Hadiza, a Nigerien wedded to a Kano trader for some years, now seeks Nigerian nationality. Her likely route is",
     "registration", "birth", "conquest", "plebiscite", "A",
     "Marriage opens the register's door."),
    (T_CIT, "Hard", "Naturalisation in Nigeria generally requires the applicant to be of full age, of good character and",
     "resident for a stated period", "born in Lagos", "a university graduate", "a civil servant", "A",
     "Years of lawful residence are asked."),
    (T_CIT, "Hard", "Chief Obi gladly collected American citizenship last year; Nigerian law says he",
     "forfeits Nigerian citizenship", "keeps two full passports", "votes in both lands", "loses his village land", "A",
     "The law frowns on split allegiance."),

    # ------------------------------------------------------------- legislature
    (T_LEGI, "Medium", "A bill becomes law when, after passage, it receives",
     "presidential assent", "a court seal", "the speaker's nod only", "newspaper publication", "A",
     "The pen of the president finishes it."),
    (T_LEGI, "Hard", "A president who withholds assent to a bill still sees it become law if",
     "two-thirds of both chambers", "half of the senators agree", "the courts order it", "the party chairman insists", "A",
     "The override is the Assembly's answer."),
    (T_LEGI, "Medium", "Before a bill's third and final reading, the stage that allows clause-by-clause amendment is the",
     "committee stage", "first reading", "gazette stage", "public rally", "A",
     "Members comb it line by line."),
    (T_LEGI, "Hard", "A legislator may be removed by his constituents through the process of",
     "recall", "impeachment", "referendum on the constitution", "judicial review", "A",
     "Signatures more than half can unseat him."),

    # ------------------------------------------------------------- elections
    (T_ELEC, "Medium", "Losing candidates who dispute an election result take their complaint to the",
     "election petition tribunal", "police command", "council of chiefs", "party secretariat", "A",
     "The courtroom follows the count."),
    (T_ELEC, "Medium", "Fixing constituency boundaries in Nigeria belongs to",
     "the Boundary Commission", "INEC itself", "the Senate alone", "surveyors' guild", "A",
     "INEC runs polls, not borders."),
    (T_ELEC, "Hard", "For INEC to register a new political party, the party must among other things show",
     "offices and national spread", "foreign sponsors", "a private army", "a television station", "A",
     "A national footing is the threshold."),

    # ------------------------------------------------------------- integration
    (T_INT, "Hard", "The federal character principle requires public appointments to reflect Nigeria's",
     "diversity of peoples", "seniority of age", "wealth of candidates", "order of application", "A",
     "No single group fills every chair."),
    (T_INT, "Medium", "Admitting students by quota from every state of the federation aims at",
     "national integration", "lowering fees", "longer courses", "private profit", "A",
     "One classroom gathers the nation."),
    (T_INT, "Hard", "A stubborn obstacle to national integration in Nigeria has been",
     "ethnic suspicion", "excess rainfall", "small families", "too many roads", "A",
     "Old fears divide new citizens."),

    # ------------------------------------------------------------- symbols & service
    (T_SYM, "Medium", "The green bands on Nigeria's flag stand for",
     "agriculture and natural wealth", "the army's uniform", "river forests", "foreign investors", "A",
     "Green fields feed the nation."),
    (T_SYM, "Hard", "On the coat of arms, the two horses and the eagle respectively stand for",
     "dignity and strength", "speed and famine", "trade and religion", "peace and war", "A",
     "Pride and power rear together."),
    (T_SYM, "Hard", "The great meeting of waters at Lokoja is recalled on Nigeria's coat of arms by",
     "two wavy silver bands", "a coiled river snake", "an anchor and a net", "a single blue circle", "A",
     "Two waters join at Lokoja."),
    (T_SYM, "Medium", "The National Youth Service Corps was created chiefly to",
     "rebuild unity after the war", "train soldiers", "replace the police", "staff embassies", "A",
     "Posting graduates across states mends fences."),
    (T_SYM, "Medium", "The Federal Road Safety Corps was established chiefly to",
     "make highways safe", "collect customs", "guard pipelines", "run railways", "A",
     "Its marshals patrol the corridors."),

    # ------------------------------------------------------------- anti-corruption
    (T_ANTIG, "Hard", "The body chiefly charged with prosecuting money-laundering and advance-fee fraud is the",
     "EFCC", "ICPC", "NAFDAC", "SON", "A",
     "Economic and financial crimes are its brief."),
    (T_ANTIG, "Hard", "While EFCC pursues economic crimes, the ICPC's core mandate covers",
     "bribery and graft generally", "road contracts only", "election petitions", "border smuggling", "A",
     "Bribery, gratification and abuse."),
    (T_ANTIG, "Hard", "Public officers declare their assets to the",
     "Code of Conduct Bureau", "Central Bank", "Stock Exchange", " Federal Ministry of Justice", "A",
     "The declaration precedes office."),

    # ------------------------------------------------------------- values
    (T_VAL, "Medium", "Contentment as a civic value means being satisfied with what one earns",
     "honestly", "secretly", "quickly", "abroad", "A",
     "Greed is contentment's opposite."),
    (T_VAL, "Medium", "A civil servant who refuses a bribe to speed a file demonstrates",
     "integrity", "cowardice", "laziness", "cleverness", "A",
     "The straight path beats the shortcut."),
    (T_VAL, "Hard", "Discipline as a national value shows itself in a citizen's",
     "self-control and orderliness", "wealth and titles", "loud complaints", "long travels", "A",
     "The ordered life orders the state."),

    # ------------------------------------------------------------- democracy deepened
    (T_DEM, "Hard", "In Nigeria's representative democracy, citizens chiefly govern through",
     "elected lawmakers", "street votes on every bill", "elders' councils", "the army's blessing", "A",
     "Representatives carry their voice."),
    (T_DEM, "Medium", "A credible election must be periodic, competitive and",
     "free and fair", "cheap and fast", "loud and colourful", "unopposed", "A",
     "Honest polls crown democracy."),
    (T_DEM, "Hard", "Unfettered majority rule that tramples minority rights degenerates into",
     "the tyranny of the majority", "absolute monarchy", "anarchy", "confederation", "A",
     "Numbers alone can also wound."),

    # ------------------------------------------------------------- human rights
    (T_HR, "Medium", "The Universal Declaration of Human Rights was proclaimed while the world still rebuilt after a war. That year was",
     "1948", "1960", "1979", "1999", "A",
     "December the tenth, after the war.", "1948"),
    (T_HR, "Hard", "Even lawful rights may be limited where their exercise would harm",
     "public safety and other rights", "no one ever", "only politicians", "foreign investors", "A",
     "My fist stops at your nose."),
    (T_HR, "Hard", "Chapter IV of the 1999 Constitution is devoted to",
     "fundamental human rights", "the legislative lists", "boundary rules", "political parties", "A",
     "The charter of the citizen stands there."),
]

build_batch(
    S,
    "batch_144_waec_civic5.json",
    "144",
    "WAEC Civic round 5 (R27 top-up): tax and anthem duties, NYSC as "
    "national service; citizenship by registration, naturalisation "
    "requirements, loss by foreign allegiance; assent, two-thirds veto "
    "override, committee stage, recall; election petition tribunals, "
    "Boundary Commission vs INEC, party registration spread; federal "
    "character, quota, ethnic suspicion; flag's green, horses and eagle "
    "of the coat of arms, Niger and Benue bands, NYSC's post-war "
    "purpose, FRSC; EFCC vs ICPC mandates, Code of Conduct Bureau "
    "assets; contentment, integrity, discipline; representative "
    "democracy, free and fair elections, tyranny of the majority; UDHR "
    "1948, rights limitation, Chapter IV. Scanned against WAEC rounds "
    "1-4, NECO Civic (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
