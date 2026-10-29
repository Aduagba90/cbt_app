"""Batch 242 - NECO Civic Education round 5 (NECO top-up, R49).

Grows NECO Civic Education from 270 toward ~295 with angles verified
absent from the whole Civic pool (560 items across JAMB, WAEC and
NECO) and cleared of cross-subject twins via db sweep against Gov,
Econ, CA, CRS, IRS, Agric and English pools. Fresh angles:
creativity; cooperation; perseverance; critical thinking;
communication skills; leadership qualities; limitations of rights;
inalienable rights; the PVC as voting requirement; one man, one
vote; eligibility to vote (18 years); sex education; school as an
agent of socialization; the press as watchdog; national ethics
(section 23 list); social justice (civic sense); the quota system;
English as Nigeria's official language; the diaspora; oath of
office; conflict of interest; democratic values; vigilante groups;
widows' inheritance rights; birth registration. Avoided as banked
or cross-twins: orderliness/queue family, contentment, integrity,
discipline, self-reliance (values banked), patience/self-esteem/
dignity of labour/selfless items, national symbols families incl.
coat of arms/national flower/motto/unity-in-diversity, citizenship
acquisition family, dual citizenship (Gov), duties/obligations
family, rights-of-citizen family, rule of law, equality before the
law, constitutionalism, constitutional democracy, political culture
(Gov), duties of government (Gov Chapter II item), fundamental
objectives/directive principles (Gov x2), political apathy, popular
participation, voter registration-importance (Gov), secret ballot
family, thuggery/fake news (Gov R47), ethnic politics (Gov R47),
religious intolerance, cultism/drugs/trafficking families, HIV
family, youth empowerment family, responsible parenthood family,
socialization agents partially (peer group banked; family items
banked), mass media shaping opinion (Gov), NYSC, traffic rules incl.
112, vandalism, corruption/EFCC family, whistleblower (banked),
cybercrime (banked), examination malpractice, good governance (as
option), quota-adjacent import quota (Econ — different fact), oath
witness gap (Use of English — different fact), PCC/ombudsman (CA +
Gov), NIN (CA), adult suffrage, hate speech, diaspora-adjacent
remittances (Econ — different fact), inheritance-bio (Biology —
different fact), widow items (CRS — different facts), forgiveness
family (CRS — dropped for safety), truthfulness (~honesty banked —
dropped), Maslow (syllabus fit — dropped), school-as-agent kept
with distinctive stem.

    python3 scripts/build_neco_batch242.py -> content/batch_242_neco_civic5.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Civic Education"

T_VAL = "Values"
T_LEAD = "Leadership and Followership"
T_HR = "Human Rights"
T_ELEC = "Elections"
T_ELECD = "Elections and Democracy"
T_ELECF = "Elections Further"
T_PAR = "Responsible Parenthood"
T_FAM = "Family and Society"
T_MEDIA = "Civil Society, Media and Order"
T_CONST = "The Constitution and Its Works"
T_QUOTA = "Federal Character and Integration"
T_NAT = "National Unity and Integration"
T_CIT = "Citizenship and Nationalism"
T_DEM = "Democracy and Its Pillars"
T_ORDER = "Law and Order"
T_PROT = "Rights Protection and Tolerance"

PASSAGES = []
PQ = []

Q = [
    (T_VAL, "Medium", "The value shown by a student who finds a new, better way of solving an old classroom problem is",
     "creativity", "contentment",
     "obedience", "silence", "A",
     "He refuses to walk the old road when a new one can be cut."),
    (T_VAL, "Easy", "When members of a community come together to dig their well, each person working beside the others, the value they display is",
     "cooperation", "competition",
     "concealment", "confusion", "A",
     "Many hands, one well, one joy."),
    (T_VAL, "Medium", "A trader who keeps retrying her business after three failed attempts, refusing to give up, displays the value of",
     "perseverance", "pride",
     "prejudice", "pleasure", "A",
     "She falls seven times and rises eight."),
    (T_VAL, "Hard", "Before accepting a rumour forwarded on WhatsApp, a good citizen first examines the evidence and asks whether it is true. This habit of examining before believing is called",
     "critical thinking", "wishful thinking",
     "double thinking", "magical thinking", "A",
     "The mind that asks questions is harder to deceive."),
    (T_LEAD, "Medium", "The ability to pass information clearly and to listen carefully to others, which every class prefect needs, is called",
     "communication skill", "calculation skill",
     "navigation skill", "negotiation only", "A",
     "A leader who cannot be understood cannot lead."),
    (T_LEAD, "Easy", "A good leader, besides being honest and hardworking, must be able to",
     "inspire and guide those he leads", "avoid all the followers",
     "do everyone's work alone", "rule by fear only", "A",
     "Leadership is lifting others, not standing on them."),
    (T_HR, "Hard", "During a declared emergency, the law may place certain limits on a citizen's freedom of movement. This shows that citizens' rights are",
     "limited by law in the public interest", "absolute and untouchable",
     "granted by the police at will", "suspended forever once limited", "A",
     "Even the freest river has banks."),
    (T_HR, "Medium", "Fundamental human rights are described as inalienable because they",
     "cannot be taken away from a person", "belong only to citizens",
     "are sold to the highest bidder", "expire after ten years", "A",
     "No government can lawfully peel them from a human being."),
    (T_ELECF, "Easy", "The document that a registered Nigerian voter must present at the polling unit before being allowed to vote is the",
     "permanent voter card", "national identity card only",
     "international passport", "driver's licence only", "A",
     "No card, no vote — the rule is simple."),
    (T_ELECD, "Medium", "The principle that every citizen's vote carries the same weight, so that no voter counts more than another, is expressed as",
     "one man, one vote", "one leader, one vote",
     "one party, one vote", "one state, one vote", "A",
     "The professor's vote and the labourer's weigh the same."),
    (T_ELEC, "Medium", "For a person to be qualified to vote in a Nigerian election, the person must, among other things, have attained the age of",
     "eighteen years", "sixteen years",
     "twenty-one years", "twenty-five years", "A",
     "The law hands the ballot to adulthood."),
    (T_PAR, "Medium", "Schools include sex education in the curriculum chiefly to help young people",
     "make informed choices about their bodies", "avoid every other subject in school",
     "leave school before graduation", "become parents while still children", "A",
     "Knowledge guards the young better than silence."),
    (T_FAM, "Medium", "Besides the family and the peer group, the institution where children are formally taught the knowledge, skills and values of their society is the",
     "school", "market",
     "motor park", "law court", "A",
     "The teacher stands beside the parent in shaping the child."),
    (T_MEDIA, "Medium", "The press is often called the watchdog of society because it",
     "exposes wrongdoing in high places", "guards the bank vaults at night",
     "barks at strangers on the street", "entertains children with cartoons", "A",
     "A barking press scares away the thieves of public trust."),
    (T_CONST, "Medium", "The 1999 Constitution names the national ethics of Nigeria as discipline, integrity, dignity of labour, social justice, religious tolerance and",
     "self-reliance", "selfishness",
     "speed", "silence", "A",
     "Six simple words carry the nation's conscience."),
    (T_VAL, "Medium", "The principle of social justice demands that the wealth, opportunities and burdens of society be",
     "fairly shared among all citizens", "given to the strongest alone",
     "kept by the government alone", "shared only with strangers", "A",
     "Justice means nobody's share is stolen by another's power."),
    (T_QUOTA, "Hard", "The quota system, used in admissions and employment, allots places to people from different states or regions mainly to",
     "ensure that every group gets a fair share", "punish the best candidates",
     "keep some regions out entirely", "avoid all forms of merit", "A",
     "The national cake is cut so every table receives a slice."),
    (T_NAT, "Easy", "Because Nigeria has over five hundred languages, the language adopted for official business, schools and the civil service is",
     "English", "Hausa only",
     "Yoruba only", "Igbo only", "A",
     "One borrowed tongue speaks for many native ones."),
    (T_CIT, "Easy", "Nigerians living abroad — the doctors, engineers and traders in America, Europe and elsewhere — are collectively referred to as the Nigerian",
     "diaspora", "delegation",
     "directorate", "dividend", "A",
     "Scattered like salt, yet still of the same shaker."),
    (T_LEAD, "Medium", "Public officers take the oath of office at the start of their tenure mainly to",
     "pledge faithful service to the nation", "announce their salaries in public",
     "declare their holidays and allowances", "register their political parties", "A",
     "The tongue promises what the term must perform."),
    (T_LEAD, "Hard", "A commissioner who awards a road contract to a construction company owned by his own brother, without disclosing it, is guilty of",
     "conflict of interest", "conflict of tribes",
     "confusion of duties", "contest of ideas", "A",
     "Public power was used to fill a private pocket."),
    (T_DEM, "Medium", "Values such as tolerance of opposition, respect for the rule of law and willingness to compromise, which keep democracy alive, are collectively called",
     "democratic values", "demographic values",
     "domestic values", "diplomatic values", "A",
     "Democracy stands on the habits of its people."),
    (T_ORDER, "Medium", "In many Nigerian communities, young men organise themselves into ____ groups to guard the neighbourhood at night. Unchecked, such groups can turn to lawlessness, which is why the police do not encourage them.",
     "vigilante", "vegetarian",
     "volunteer teaching", "visitors'", "A",
     "A double-edged guard: protection today, menace tomorrow."),
    (T_PROT, "Hard", "In some communities a widow is denied her late husband's property, which is seized by his relatives. This practice violates her",
     "right to own property", "right to vote",
     "right to education", "right to drive", "A",
     "Her marriage did not cancel her ownership."),
    (T_CIT, "Medium", "The registration of a child's birth at the national population office soon after the child is born is important because the record",
     "proves the child's identity and nationality", "guarantees the child a government job",
     "replaces the need for schooling", "earns the parents a monthly grant", "A",
     "A certificate no bigger than a hand carries a whole life's beginning."),
]

build_batch(
    S,
    "batch_242_neco_civic5.json",
    "242",
    "NECO Civic Education round 5 (R49 top-up): creativity; "
    "cooperation; perseverance; critical thinking; communication "
    "skills; leadership qualities; limitations of rights; inalienable "
    "rights; PVC; one man one vote; voting age 18; sex education; "
    "school as agent of socialization; press as watchdog; national "
    "ethics; social justice; quota system; English as official "
    "language; the diaspora; oath of office; conflict of interest; "
    "democratic values; vigilante groups; widows' inheritance "
    "rights; birth registration. Scanned against the whole Civic "
    "pool (JAMB, WAEC and NECO stems) and cleared of cross-subject "
    "twins (Gov, Econ, CA, CRS, IRS, Agric, Use of English).",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
