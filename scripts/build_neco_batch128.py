"""Batch 128 - NECO Civic Education round 4 (NECO top-up, Round 24).

Lifts NECO Civic from 151 toward ~195 with angles not yet in any bank:
constitutional functions, citizens' duties, rights enforcement bodies
(NHRC, Legal Aid), delegated legislation, democratic principles,
constitutionalism, civil society and the press, orderliness, drug abuse
effects and prevention, HIV/AIDS as a civic issue, human-rights
violations, women's and children's rights, religious tolerance and
conflict resolution. Scanned against NECO rounds 1-3, WAEC Civic (all
rounds) and the JAMB Government pool.

    python3 scripts/build_neco_batch128.py -> content/batch_128_neco_civic4.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Civic Education"

T_CONST = "The Constitution and Its Works"
T_RIGHT = "Rights, Duties and Enforcement"
T_DEM = "Democracy and Its Pillars"
T_SOC = "Civil Society, Media and Order"
T_DRUG = "Drug Abuse and Health"
T_VIOL = "Rights Protection and Tolerance"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- constitution
    (T_CONST, "Medium", "A constitution chiefly serves to",
     "limit government power", "record folk tales", "fix market prices", "name football clubs", "A",
     "It is the ground rule of state."),
    (T_CONST, "Hard", "Power given to a minister to make rules under an Act of parliament is",
     "delegated legislation", "judicial review", "popular sovereignty", "plebiscite", "A",
     "Parliament lends its pen."),
    (T_CONST, "Medium", "Constitutionalism means government according to the",
     "constitution's limits", "ruler's wishes", "army's orders", "richest man's mood", "A",
     "The book binds the powerful."),
    (T_CONST, "Medium", "The supremacy of the constitution means any law that contradicts it is",
     "void", "doubly binding", "printed again", "left to chance", "A",
     "The courts strike it down."),
    (T_CONST, "Hard", "An unwritten constitution is one drawn from",
     "statutes and conventions", "a single pamphlet", "royal proclamations only", "military decrees alone", "A",
     "Britain gathers it from many springs."),

    # ------------------------------------------------------------- rights and duties
    (T_RIGHT, "Medium", "Voting at elections, paying taxes and defending the nation are citizens'",
     "duties", "privileges", "punishments", "hobbies", "A",
     "Democracy asks for service."),
    (T_RIGHT, "Medium", "Respect for the national flag and anthem shows",
     "patriotism", "partisanship", "apathy", "fanaticism", "A",
     "Symbols carry the nation's soul."),
    (T_RIGHT, "Hard", "The National Human Rights Commission mainly",
     "investigates rights complaints", "judges election petitions", "collects taxes", "prints currency", "A",
     "It hears the ordinary citizen."),
    (T_RIGHT, "Hard", "Legal aid schemes exist so that poor citizens can",
     "defend themselves in court", "avoid all laws", "study abroad", "skip bail", "A",
     "Justice must not price out the poor."),
    (T_RIGHT, "Medium", "A right enjoyed without regard for others' rights leads to",
     "lawlessness", "greater unity", "faster courts", "cheaper goods", "A",
     "My freedom ends at your nose."),

    # ------------------------------------------------------------- democracy
    (T_DEM, "Medium", "Periodic free elections ensure that leaders remain",
     "accountable to the people", "in office for life", "above the law", "unelected", "A",
     "The ballot renews the mandate."),
    (T_DEM, "Hard", "Majority rule in a democracy must be tempered by",
     "respect for minority rights", "silencing opposition", "abolishing courts", "state propaganda", "A",
     "The minority keeps its voice."),
    (T_DEM, "Medium", "The principle of checks and examples of it include the legislature's power to",
     "screen and confirm appointments", "command the army directly", "print money secretly", "fix school fees", "A",
     "Each arm polices the others."),
    (T_DEM, "Medium", "Popular participation in governance can grow through",
     "town hall meetings", "night curfews", "secret police files", "closing newspapers", "A",
     "Voices join the decisions."),
    (T_DEM, "Hard", "A referendum decides an issue by",
     "direct vote of the people", "cabinet decree", "court order", "party primary", "A",
     "The people answer directly."),
    (T_DEM, "Medium", "One danger to democracy is election rigging, which",
     "steals the people's mandate", "speeds results", "improves turnout", "calms tempers", "A",
     "Fake figures break trust."),

    # ------------------------------------------------------------- civil society, media, order
    (T_SOC, "Medium", "Civil society organisations include",
     "labour unions", "the navy", "customs service", "the cabinet", "A",
     "Citizens organise themselves."),
    (T_SOC, "Medium", "A free press strengthens democracy by",
     "holding power to account", "praising leaders daily", "hiding public debts", "banning open debates", "A",
     "Press sunlight checks the mighty."),
    (T_SOC, "Hard", "The worst danger of fake news is that it",
     "poisons public trust", "educates children", "funds hospitals", "cleans elections", "A",
     "Poisoned trust stirs violence too."),
    (T_SOC, "Medium", "Orderliness in public life includes",
     "queuing patiently", "jumping school fences", "shouting down speakers", "burning tyres", "A",
     "Small disciplines hold the peace."),
    (T_SOC, "Medium", "Obedience to lawful authority should be balanced with",
     "courage to resist injustice", "total silence", "fear of questions", "worship of leaders", "A",
     "Citizens think as they obey."),
    (T_SOC, "Medium", "Political apathy, staying away from public affairs, weakens",
     "self-government", "the police only", "import duties", "the currency", "A",
     "Absent citizens lose their voice."),

    # ------------------------------------------------------------- drugs and health
    (T_DRUG, "Medium", "Taking medicine wrongly, without a doctor's order, is what defines",
     "without medical need", "as doctors prescribe", "at mealtimes only", "bought in hospitals", "A",
     "The misuse wrecks the body."),
    (T_DRUG, "Medium", "A common effect of hard drugs on youth is",
     "damaged health", "sharper memory", "stronger muscles", "a longer life", "A",
     "The high costs everything."),
    (T_DRUG, "Hard", "Withdrawal symptoms occur when a dependent user",
     "stops taking the drug", "eats well", "sleeps early", "exercises", "A",
     "The body screams for its chain."),
    (T_DRUG, "Medium", "The best school-based prevention against drug abuse is",
     "awareness and counselling", "longer holidays", "higher fees", "banning sports", "A",
     "Informed pupils refuse politely."),
    (T_DRUG, "Medium", "HIV spreads through all of these EXCEPT",
     "sharing mosquito bites", "unprotected sex", "infected blood", "mother to child", "A",
     "The mosquito carries no HIV."),
    (T_DRUG, "Hard", "Stigmatising people living with HIV/AIDS chiefly",
     "discourages testing", "cures the illness", "spreads awareness", "lengthens life", "A",
     "Kindness heals as much as drugs."),

    # ------------------------------------------------------------- rights protection and tolerance
    (T_VIOL, "Medium", "Child labour that keeps children out of school violates their right to",
     "education", "movement", "worship", "silence", "A",
     "The classroom calls them back."),
    (T_VIOL, "Medium", "The rights of the disabled are best protected by",
     "inclusive laws and access", "hiding them away", "mocking their needs", "ignoring ramps", "A",
     "Society climbs or falls together."),
    (T_VIOL, "Hard", "Human trafficking victims are often lured by false promises of",
     "jobs and education", "sports trials only", "free medical care", "farm tools", "A",
     "The mirage leads to servitude."),
    (T_VIOL, "Medium", "Domestic violence thrives where victims stay silent; reporting it to the police or social welfare shows",
     "courage and civic duty", "family shame", "disloyalty", "weakness", "A",
     "Speaking breaks the cycle."),
    (T_VIOL, "Medium", "Religious tolerance in a multi-faith nation like Nigeria means",
     "respecting other faiths", "forcing one religion", "bending all worship", "mocking beliefs", "A",
     "Many bells ring in one town."),
    (T_VIOL, "Hard", "Community conflicts are best settled through",
     "dialogue and mediation", "reprisal attacks", "endless lawsuits only", "silence and rumour", "A",
     "The talking table outlives the barricade."),
    (T_VIOL, "Medium", "Equal opportunity for women in work and school advances the whole society because it",
     "unlocks half the talent", "doubles market prices", "slows national growth", "shrinks families", "A",
     "No nation thrives on one wing."),
]

build_batch(
    S,
    "batch_128_neco_civic4.json",
    "128",
    "NECO Civic Education round 4 (Round 24 top-up): constitutional "
    "functions and supremacy, delegated legislation, constitutionalism, "
    "unwritten sources, citizens' duties, patriotism, the NHRC, legal "
    "aid, rights with responsibilities, accountable elections, minority "
    "rights, checks examples, popular participation, referenda, rigging "
    "dangers, civil society, the free press, fake news, orderliness, "
    "balanced obedience, political apathy, drug abuse effects, "
    "withdrawal, prevention, HIV routes and stigma, child labour, "
    "disability rights, trafficking lures, domestic violence reporting, "
    "religious tolerance, mediation and women's opportunity. Scanned "
    "against NECO rounds 1-3, WAEC Civic (all rounds) and the JAMB "
    "Government pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
