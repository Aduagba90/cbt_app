"""Batch 164 - NECO Government round 5 (NECO top-up, R30).

Grows NECO Government from 193 toward ~230 with angles not yet in the
bank: constitutions by origin (granted, enacted, evolved);
constitutionalism; parliamentary privileges, the Speaker's office and
quorum; devolution vs federalism; confederation features; the civil
service commission; privatisation and commercialisation; local
government revenue; Chapter II fundamental objectives; political
culture; qualities of an electoral body; merits of delegated
legislation; the executive's defence and treaty functions; emergency
proclamation; the immunity clause; coalition and multi-party
government. Scanned against NECO rounds 1-4, WAEC Government (all
rounds) and the JAMB pool.

    python3 scripts/build_neco_batch164.py -> content/batch_164_neco_gov5.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Government"

T_CONST = "Constitutions Further"
T_PARL = "Parliamentary Machinery"
T_STR = "Structures of Power"
T_CIV = "Institutions Further"
T_FED = "Federal Principles Further"
T_POL = "Political Life"
T_EXEC = "The Executive Further"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- constitutions
    (T_CONST, "Hard", "A constitution handed down by a ruler or colonial power, like the Clifford Constitution, is said to be",
     "granted", "enacted", "evolved", "rigid", "A",
     "The people received it, not wrote it."),
    (T_CONST, "Medium", "A constitution made by the people's own representatives in an assembly is",
     "enacted", "granted", "evolved", "unitary", "A",
     "The constituent assembly wrote it."),
    (T_CONST, "Hard", "A constitution built up gradually through customs, conventions and statutes over time is",
     "evolved", "granted", "enacted", "written", "A",
     "Britain's is its classic case."),
    (T_CONST, "Medium", "Constitutionalism means government according to the",
     "constitution and the rule of law", "army's command", "ruler's moods", "party's manifesto alone", "A",
     "Even the powerful bow to it."),

    # ------------------------------------------------------------- parliamentary machinery
    (T_PARL, "Hard", "The legal protections members enjoy to speak freely in the house are called parliamentary",
     "privileges", "licenses", "immunities of crime", "patents", "A",
     "Sue-free words on the floor."),
    (T_PARL, "Medium", "During plenary in the green chamber of the National Assembly, the mace and the gavel belong to the",
     "Speaker", "Senate President", "Clerk", "Majority Leader", "A",
     "He keeps the green chamber in order."),
    (T_PARL, "Hard", "The minimum number of members required to be present before business can lawfully proceed is the",
     "quorum", "caucus", "conclave", "plenum", "A",
     "Without it, the house cannot act."),
    (T_PARL, "Medium", "A long vacation address in which the governor opens a new legislative year is delivered at",
     "a state opening", "a caucus meeting", "a court sitting", "a party rally", "A",
     "Speeches from the throne's cousin."),

    # ------------------------------------------------------------- structures
    (T_STR, "Hard", "Unlike federalism, devolution keeps ultimate power at the centre while",
     "letting regions make some laws", "abolishing all regions", "electing a monarch", "fusing the courts", "A",
     "The centre lends, never gives."),
    (T_STR, "Hard", "In a confederation, the component states retain their",
     "sovereignty and can secede", "armies under one command", "currency by law", "judges from the centre", "A",
     "The centre serves at their pleasure."),
    (T_STR, "Medium", "The lowest tier of government closest to the people is the",
     "local government", "federal executive", "senate committee", "state assembly", "A",
     "Ward matters are its beat."),

    # ------------------------------------------------------------- institutions
    (T_CIV, "Hard", "The body that recruits, promotes and disciplines civil servants is the",
     "civil service commission", "electoral commission", "judicial council", "party secretariat", "A",
     "Merit passes through its hands."),
    (T_CIV, "Hard", "Selling government shares in NITEL and power firms to private investors is",
     "privatisation", "commercialisation", "nationalisation", "indigenisation", "A",
     "Ownership changes hands for cash."),
    (T_CIV, "Medium", "Reorganising a public corporation to run on profit lines without selling it is",
     "commercialisation", "privatisation", "liquidation", "deregulation of staff", "A",
     "The state keeps the shop; business rules the till."),
    (T_CIV, "Hard", "Besides federal grants, a council in Lagos state collects yearly from landlords and kiosk owners its own",
     "rates and licences", "import duties", "pay-as-you-earn of civil servants", "oil royalties", "A",
     "Houses and shops in the ward pay."),
    (T_CIV, "Hard", "Chapter II of the 1999 Constitution, on the nation's goals and duties of government, is titled",
     "fundamental objectives", "fundamental rights", "legislative lists", "transitional provisions", "A",
     "Directive principles live there."),

    # ------------------------------------------------------------- federal principles
    (T_FED, "Medium", "In a federation, constitutional disputes between the centre and a state are settled by the",
     "courts", "army", "ruling party", "council of state alone", "A",
     "The judiciary referees the tiers."),
    (T_FED, "Hard", "The power to conduct census and form the police in Nigeria's federal practice lies with",
     "the federal government", "the states", "local councils", "the courts", "A",
     "Exclusive items sit on the central list."),
    (T_FED, "Medium", "Each state in a federation, whatever its size or wealth, normally returns an equal voice in the",
     "upper house", "lower house", "cabinet", "civil service", "A",
     "Three senators apiece, big or small."),

    # ------------------------------------------------------------- political life
    (T_POL, "Medium", "The sum of a people's beliefs, feelings and attitudes towards politics is their political",
     "culture", "economy", "geography", "architecture", "A",
     "It colours how they vote and obey."),
    (T_POL, "Hard", "For an electoral body to command trust, it must above all be",
     "independent and impartial", "richly funded by parties", "staffed by candidates", "elected every year", "A",
     "Even hands count even votes."),
    (T_POL, "Hard", "A major merit of delegated legislation is that it",
     "saves the house much time", "removes all courts oversight", "ends the need for experts", "abolishes public hearings", "A",
     "Ministers fine-tune what the house frames."),
    (T_POL, "Medium", "A government formed by two or more parties agreeing to share power is a",
     "coalition government", "caretaker committee", "shadow cabinet", "one-party state", "A",
     "Partners hold the reins together."),
    (T_POL, "Medium", "A system with many parties competing freely, as Nigeria practises, is a",
     "multi-party system", "two-party system", "one-party system", "no-party system", "A",
     "Many flags on one ballot."),
    (T_POL, "Hard", "Nigeria's return to many parties after years of two-party decree came with the",
     "1999 Constitution era", "1960 independence pact", "1979 decree only", "1966 coup", "A",
     "The fourth republic opened the field."),

    # ------------------------------------------------------------- executive further
    (T_EXEC, "Medium", "Command of the armed forces and declaration of war belong to the executive as its",
     "defence function", "judicial function", "legislative function", "ceremonial duty", "A",
     "The commander-in-chief's charge."),
    (T_EXEC, "Medium", "Negotiating and signing agreements with foreign nations is the executive's function in",
     "foreign relations", "lawmaking", "adjudication", "auditing", "A",
     "Treaties bear the head of state's hand."),
    (T_EXEC, "Hard", "A state of emergency may be proclaimed by the president only when the affairs of a state or the federation are",
     "seriously threatened", "running smoothly", "in surplus budget", "praised abroad", "A",
     "Two-thirds of the National Assembly must then ratify."),
    (T_EXEC, "Hard", "The immunity clause shields a sitting president or governor from",
     "civil and criminal prosecution", "all criticism forever", "impeachment votes", "election defeat", "A",
     "It ends the day the office ends."),
    (T_EXEC, "Medium", "The body of ministers and head of state that directs policy day by day is the",
     "executive council", "judicial panel", "electoral college", "civil service bench", "A",
     "The cabinet meets weekly on it."),

    # ------------------------------------------------------------- mixed further
    (T_POL, "Hard", "One durable argument for a unicameral legislature is that it",
     "avoids costly duplication of chambers", "gives small states a veto", "lengthens every bill", "abolishes parties", "A",
     "One house, one bill's road."),
    (T_CIV, "Medium", "When the Public Accounts Committee demands a ministry's books, the officer who must produce them is the",
     "permanent secretary", "senior driver", "minister's aide", "auditor-general", "A",
     "Files and funds answer to him."),
    (T_STR, "Medium", "The principle of checks and balances exists chiefly to prevent",
     "tyranny by one organ", "elections altogether", "the work of parliament", "all taxation", "A",
     "Each organ watches its neighbour."),
    (T_PARL, "Medium", "A lawmaker who abandons the party on whose platform he was elected for another, without leaving the seat, tests the law on",
     "party defection", "judicial review", "recall", "referendum", "A",
     "The floor-crossing question."),
    (T_CONST, "Hard", "Under the constitution Nigeria received at independence, the head of state was the British monarch, making the country a",
     "constitutional monarchy", "republic", "military diarchy", "confederation", "A",
     "The Queen kept the crown's role."),
]

build_batch(
    S,
    "batch_164_neco_gov5.json",
    "164",
    "NECO Government round 5 (R30 top-up): granted, enacted and evolved "
    "constitutions; constitutionalism; parliamentary privileges, the "
    "Speaker, quorum, state opening; devolution vs federalism, "
    "confederation's retained sovereignty, local tier; civil service "
    "commission, privatisation vs commercialisation, tenement rates, "
    "Chapter II fundamental objectives; courts settling federal "
    "disputes, exclusive items, equal state voices in the upper house; "
    "political culture, impartial electoral body, delegated "
    "legislation's merits, coalition and multi-party systems, 1999 "
    "party opening; defence and treaty functions, emergency "
    "proclamation, immunity clause, executive council; unicameral "
    "argument, permanent secretary, checks against tyranny, defection "
    "law, 1960 constitutional monarchy. Scanned against NECO rounds "
    "1-4, WAEC Government (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
