"""Batch 168 - WAEC Civic Education round 6 (WAEC top-up, R31).

Grows WAEC Civic from 204 toward ~239 with angles not yet in the
bank: green traffic light, warning triangle, zebra-crossing
priority, the 50 km/h built-up limit, seat belts, the duty to stop
after a knock-down, the 112 emergency line; orderliness defined, a
stampede's lesson, national security defined, rule of law's
emergency limit; the civil wrong (tort); cybercrime and the
whistleblower; referendum, the voting age of 18, the constituency,
political tolerance; citizenship by birth never withdrawn, the
alien in law; SSS/DSS internal intelligence, NIA external
intelligence, the Navy's waters, Immigration passports, Customs
duties, the Correctional Service's reform aim; the African Charter;
inter-communal conflict's cause and its settlement; peer pressure
and drugs; poverty at the root of trafficking; justice as a value;
the anthem's author; hawking against the right to education.
Scanned against WAEC rounds 1-5, NECO Civic (all rounds) and the
JAMB pool.

    python3 scripts/build_neco_batch168.py -> content/batch_168_waec_civic6.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Civic Education"

T_TRF = "Traffic Regulations"
T_LO = "Law and Order"
T_RL = "Constitution, Rule of Law and Arms of Government"
T_CL = "Corruption and the Law"
T_EP = "Elections and Participation"
T_CIT = "Citizenship"
T_GS = "Government Structures"
T_RD = "Rights, Duties and Law"
T_HRI = "Human Rights Instruments"
T_SI = "Social Ills"
T_DR = "Drugs and Substance Abuse"
T_HT = "Human Trafficking"
T_VAL = "Values"
T_NS = "National Symbols"

PASSAGES = []
PQ = []

Q = [
    (T_TRF, "Easy", "A steady green traffic light instructs the driver to",
     "move on if the road is clear", "stop and wait behind the line",
     "slow down and prepare to halt", "reverse into a side street", "A",
     "Green gives the go-ahead, with care."),
    (T_TRF, "Easy", "A car that breaks down on the open highway should immediately be guarded with",
     "green leaves from a nearby tree", "a red reflecting warning triangle",
     "the spare tyre placed flat", "a white cloth tied to the bumper", "B",
     "The triangle warns oncoming traffic in good time."),
    (T_TRF, "Easy", "At a zebra crossing, the right of way belongs to",
     "the fastest vehicle", "pedestrians already on the crossing",
     "drivers approaching from the left", "motorcyclists only", "B",
     "The white stripes exist to protect the walker."),
    (T_TRF, "Medium", "In built-up areas, the highway code speed limit for private cars is",
     "50 km/h", "80 km/h", "100 km/h", "120 km/h", "A",
     "Fifty keeps the street safe for its busy life.", "50"),
    (T_TRF, "Easy", "Wearing a seat belt chiefly reduces the risk of",
     "being thrown out of the vehicle in a crash", "the risk of paying fines at checkpoints",
     "losing one's driving licence", "damage to the car seats", "A",
     "The belt holds the body inside the safety shell."),
    (T_TRF, "Medium", "A driver who knocks down a pedestrian must first of all",
     "stop immediately and help the victim", "drive off before the crowd gathers",
     "report to his mechanic first", "wait for the police to find him", "A",
     "Fleeing the scene turns an accident into a crime."),
    (T_TRF, "Easy", "The toll-free national number for summoning police, fire or medical help is",
     "112", "419", "199", "311", "A",
     "One short number reaches every rescue service.", "112"),
    (T_LO, "Easy", "Orderliness is best defined as",
     "doing things calmly and in proper sequence", "rushing to be served before others",
     "arguing with officials in public", "pushing weaker people aside", "A",
     "Each person waits and takes his proper turn."),
    (T_LO, "Medium", "Disorder at the gates of a crowded stadium can most easily end in",
     "a deadly stampede", "a profitable ticket racket",
     "an orderly double queue", "a better seating plan", "A",
     "Panic plus pressure crushes the people in front."),
    (T_LO, "Medium", "National security is best described as",
     "protecting the nation's people, territory and interests", "the recruitment of party thugs for elections",
     "the building of bigger prisons nationwide", "the printing of new currency notes", "A",
     "It covers life, land and the general welfare."),
    (T_RL, "Medium", "The rule of law may be partly limited in Nigeria during",
     "a properly declared state of emergency", "a change of the school calendar",
     "a national sports festival year", "a prolonged public holiday", "A",
     "Emergency powers suspend some normal safeguards."),
    (T_CL, "Medium", "Obtaining money through fake emails and false online identities, popularly called yahoo-yahoo, is a form of",
     "cybercrime", "civil wrong", "human trafficking", "treasonable felony", "A",
     "The fraudster's tools are the phone and the web."),
    (T_CL, "Medium", "A worker who risks his job to report stealing inside his ministry is popularly called a",
     "whistleblower", "ring leader", "contractor", "statistician", "A",
     "He blows the whistle and the thieves scatter."),
    (T_EP, "Medium", "A vote in which the whole electorate decides one question directly is a",
     "referendum", "by-election", "primary election", "plebiscite of judges", "A",
     "The people themselves answer yes or no."),
    (T_EP, "Easy", "A Nigerian becomes eligible to register and vote at the age of",
     "16", "18", "21", "25", "B",
     "Eighteen is the lawful age of the franchise.", "18"),
    (T_EP, "Easy", "The voters whom a member of the House of Representatives serves are together his",
     "constituency", "cabinet", "caucus", "corporation", "A",
     "He sits in the House to speak for them."),
    (T_EP, "Medium", "A party man who lets rivals campaign freely in his own ward displays",
     "political tolerance", "party indiscipline", "electoral fraud", "voter apathy", "A",
     "Democracy breathes where rivals meet freely."),
    (T_CIT, "Medium", "Of the ways of acquiring Nigerian citizenship, the one that can never be withdrawn is",
     "citizenship by birth", "citizenship by registration",
     "citizenship by naturalisation", "citizenship by honorary award", "A",
     "Birthright stands when every other falls."),
    (T_CIT, "Easy", "A foreigner resident in Nigeria who has not taken up citizenship is, in law, an",
     "alien", "indigene", "delegate", "elector", "A",
     "He lives among citizens but holds another passport."),
    (T_GS, "Medium", "Internal intelligence and state security reports are chiefly the work of the",
     "State Security Service (DSS)", "Nigeria Police Force",
     "Nigeria Immigration Service", "Federal Road Safety Corps", "A",
     "The DSS watches threats inside the country."),
    (T_GS, "Hard", "The gathering of intelligence beyond Nigeria's borders is assigned to the",
     "National Intelligence Agency (NIA)", "State Security Service (DSS)",
     "Nigeria Customs Service", "Nigeria Correctional Service", "A",
     "The NIA is Nigeria's eye abroad."),
    (T_GS, "Easy", "The service that defends Nigeria's territorial waters is the",
     "Nigerian Navy", "Nigerian Army", "Nigerian Air Force", "Nigeria Customs Service", "A",
     "Ships and gunboats guard the sea approaches."),
    (T_GS, "Easy", "Issuing Nigerian passports and controlling movement at the borders belong to the",
     "Nigeria Immigration Service", "Nigeria Customs Service",
     "Nigeria Correctional Service", "National Population Commission", "A",
     "The immigration desk is the traveller's first gate."),
    (T_GS, "Easy", "The service that collects duties on goods entering or leaving Nigeria is the",
     "Nigeria Customs Service", "Nigeria Immigration Service",
     "Nigerian National Petroleum Company", "National Drug Law Enforcement Agency", "A",
     "Every dutiable consignment answers at the port."),
    (T_GS, "Medium", "In 2019 the Nigerian Prisons Service was renamed the Correctional Service to emphasise",
     "the reformation and rehabilitation of offenders", "the feeding of inmates on private contracts",
     "the construction of more cell blocks", "longer jail terms for convicts", "A",
     "Correction, not mere confinement, is the aim."),
    (T_HRI, "Medium", "Besides the UDHR, Nigeria honours human rights under the African Charter on",
     "Human and Peoples' Rights", "Human and Peoples' Resources",
     "Human Rights and Free Trade", "the Rights of African Rulers", "A",
     "The Banjul Charter binds African states."),
    (T_SI, "Medium", "A common cause of inter-communal conflicts in Nigeria is",
     "struggles over land and grazing routes", "disagreements over football matches",
     "rivalry between neighbouring schools", "quarrels over market days", "A",
     "Farmland and pasture set neighbour against neighbour."),
    (T_SI, "Medium", "Inter-communal clashes are best settled through",
     "dialogue and mediation by neutral elders", "immediate reprisal attacks on the other town",
     "a fight to the finish", "waiting for the rainy season to pass", "A",
     "Talking across the table heals two towns."),
    (T_DR, "Easy", "The strongest pull that draws secondary school students into drug abuse is usually",
     "yielding to peer pressure", "reading chemistry textbooks",
     "watching agricultural programmes", "listening to their parents", "A",
     "The crowd of friends sets the habit."),
    (T_HT, "Medium", "The root condition that most exposes Nigerian youths to human traffickers is",
     "widespread poverty and desperation", "the abundance of rainfall in the south",
     "well-paved highways across the country", "the high rate of adult literacy", "A",
     "Empty pockets make false promises shine."),
    (T_VAL, "Easy", "Justice as a civic value means",
     "giving every person his due", "punishing only the poor",
     "obeying orders always", "keeping one's views private", "A",
     "Fairness measures each man his right portion."),
    (T_NS, "Medium", "The words of the national anthem, Nigeria, We Hail Thee, were written by",
     "Lillian Jean Williams", "Frances Berda", "Taiwo Akinkunmi", "Benjamin Odiase", "A",
     "An expatriate poetess penned the anthem's lines."),
    (T_RD, "Medium", "A private wrong for which the injured person may sue for damages is called",
     "a civil wrong", "a criminal offence", "a constitutional breach", "an electoral malpractice", "A",
     "The victim himself carries the case to court."),
    (T_RD, "Medium", "Sending a child of school age to hawk in traffic during school hours violates the child's",
     "right to education", "right to silence",
     "right to vote at eighteen", "freedom of trade unionism", "A",
     "School bells, not traffic, should claim the child."),
    (T_EP, "Easy", "Nigerians queue at polling units on election day mainly to",
     "cast their votes in an orderly way", "sell party memorabilia",
     "watch the counting from inside", "block others from voting", "A",
     "The queue makes every ballot equal."),
]

build_batch(
    S,
    "batch_168_waec_civic6.json",
    "168",
    "WAEC Civic round 6 (R31 top-up): green light go, warning "
    "triangle, zebra priority, 50 km/h built-up limit, seat belts, "
    "stop-and-help after a knock-down, the 112 line; orderliness "
    "defined, stampede risk, national security defined, rule-of-law "
    "emergency limit; the tort; yahoo-yahoo as cybercrime, the "
    "whistleblower; referendum, voting age 18, the constituency, "
    "political tolerance; citizenship by birth never withdrawn, the "
    "alien; DSS internal and NIA external intelligence, Navy's "
    "waters, Immigration passports, Customs duties, Correctional "
    "Service reform; African Charter; inter-communal causes and "
    "settlement; peer pressure into drugs; poverty behind "
    "trafficking; justice defined; anthem author Lillian Jean "
    "Williams; hawking against the right to education; queuing to "
    "vote. Scanned against WAEC rounds 1-5, NECO Civic (all rounds) "
    "and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
