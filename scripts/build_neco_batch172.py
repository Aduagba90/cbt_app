"""Batch 172 - NECO Physics round 5 (NECO top-up, R32).

Grows NECO Physics from 198 toward ~233 with angles not yet in the
bank: the micrometer's 0.01 mm; mass as constant quantity of
matter; impulse as force times time; the conservation of energy;
Boyle's law; the barometer falling on a mountain; relative density;
ice floating; latent heat of fusion; evaporation versus boiling;
metal pots with plastic handles; Brownian motion; the timbre of a
note; ultrasound; amplitude; the tightened guitar string; thunder
after lightning; magnification as a ratio; the virtual image; the
convex driving mirror; the glass rod losing electrons; the voltmeter
in parallel; wire length doubling resistance; the electric iron's
heating effect; trivalent doping giving p-type; the transistor as
amplifier; the beta particle as an electron; gamma leaving A and Z
untouched; the Geiger-Muller counter; a half-life calculation; film
badges and distance; electromagnetic induction; Hooke's law; the
wheelbarrow as a second-class lever; the door's greatest moment;
staircase power. Scanned against NECO rounds 1-4, WAEC Physics
(all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch172.py -> content/batch_172_neco_physics5.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Physics"

T_MEAS = "Measurements and Units"
T_MOT = "Motion"
T_FOR = "Force, Momentum and Newton's Laws"
T_WEP = "Work, Energy and Power"
T_MAC = "Machines"
T_PRU = "Pressure and Upthrust"
T_HEA = "Heat Energy"
T_WAS = "Waves and Sound"
T_LIT = "Light and Optics"
T_CEL = "Current Electricity"
T_ELE = "Electronics and the Nucleus"
T_MOD = "Modern Physics"
T_MAG = "Magnetism and Electromagnetism"

PASSAGES = []
PQ = []

Q = [
    (T_MEAS, "Medium", "The micrometer screw gauge is used in the laboratory to measure diameters to the nearest",
     "0.01 mm", "0.1 mm", "1.0 mm", "0.001 cm only", "A",
     "Its fine screw reads a hundredth of a millimetre.", "0.01"),
    (T_FOR, "Easy", "The mass of a body differs from its weight because the mass is",
     "the same everywhere", "zero on the moon",
     "a force measured in newtons", "greater at the equator", "A",
     "Mass counts matter; weight pulls it downward."),
    (T_FOR, "Hard", "The product of the force acting on a body and the time for which it acts is called the",
     "impulse", "momentum of rest", "power of the force", "work done by the force", "A",
     "A large impulse changes momentum greatly."),
    (T_WEP, "Easy", "Energy can change from form to form but can never be created or destroyed. This is the law of",
     "conservation of energy", "conservation of momentum",
     "diminishing returns", "transformation of matter", "A",
     "The total stock of energy never grows or shrinks."),
    (T_WEP, "Medium", "A boy of mass 50 kg runs up a staircase 6 m high in 12 s. Taking g as 10 m/s2, his power is",
     "250 W", "25 W", "300 W", "3,000 W", "A",
     "Three thousand joules shared over twelve seconds.", "250"),
    (T_MAC, "Medium", "In a wheelbarrow, the load sits between the effort and the fulcrum. The wheelbarrow is therefore a",
     "second-class lever", "first-class lever",
     "third-class lever", "simple pulley", "A",
     "Load in the middle multiplies the effort."),
    (T_PRU, "Hard", "At constant temperature, the volume of a fixed mass of gas is inversely proportional to its pressure. This is",
     "Boyle's law", "Charles' law",
     "the pressure law", "Avogadro's law", "A",
     "Squeeze the gas and it shrinks in proportion."),
    (T_PRU, "Medium", "Carried to the top of a high mountain, a mercury barometer reads",
     "lower than at sea level", "higher than at sea level",
     "exactly the same as before", "zero at once", "A",
     "Less air presses down from above at the summit."),
    (T_PRU, "Easy", "The ratio of the density of a substance to the density of water is called its",
     "relative density", "specific heat capacity",
     "weight density", "buoyant force", "A",
     "Water is the standard against which all are weighed."),
    (T_PRU, "Easy", "An ice cube floats with most of it below the water surface because ice is",
     "less dense than water", "heavier than water",
     "colder than water always", "full of trapped fish", "A",
     "Its lighter molecules keep a ninth above the line."),
    (T_HEA, "Medium", "The heat absorbed by melting ice at zero degrees Celsius without any rise in temperature is the",
     "latent heat of fusion", "specific heat capacity",
     "heat of combustion", "sensible heat", "A",
     "The hidden heat that loosens the solid bonds."),
    (T_HEA, "Medium", "Evaporation differs from boiling because evaporation takes place",
     "at any temperature and only at the surface", "only at one fixed temperature throughout",
     "only inside the liquid bulk", "only in a closed vessel", "A",
     "Quiet surface escapes; boiling is a whole-body affair."),
    (T_HEA, "Easy", "Cooking pots are made of metal but their handles are of plastic or wood because metals",
     "conduct heat but plastics do not", "are cheaper than plastics",
     "reflect all the heat back", "melt in warm soup", "A",
     "The conductor carries the heat; the handle refuses it."),
    (T_HEA, "Hard", "Under the microscope, smoke particles in air dance about endlessly and irregularly. This is evidence that air molecules",
     "are in constant random motion", "are too heavy to move",
     "attract the smoke strongly", "move only when heated hard", "A",
     "Unseen molecules jostle the visible specks."),
    (T_WAS, "Hard", "A flute and a trumpet play the same note at the same loudness, yet the ear tells them apart. The difference is the notes'",
     "quality (timbre)", "pitch", "intensity alone", "wavelength", "A",
     "Each instrument dresses the note in its own overtones."),
    (T_WAS, "Easy", "Sound whose frequency lies above the range the human ear can hear is called",
     "ultrasound", "infrasound", "supersonic noise", "echo sound", "A",
     "Above twenty thousand hertz the ear gives up."),
    (T_WAS, "Medium", "The height of a wave's crest above the rest position of its particles is the wave's",
     "amplitude", "frequency", "wavelength", "period", "A",
     "Amplitude measures the size of the swing."),
    (T_WAS, "Medium", "Tightening the string of a guitar raises the note because the tightening",
     "raises the frequency of vibration", "shortens the guitar",
     "increases the wood's echoes", "lowers the amplitude", "A",
     "A tauter string trembles more times a second."),
    (T_WAS, "Easy", "During a thunderstorm, the lightning is seen before the thunder is heard because",
     "light travels much faster than sound", "sound travels much faster than light",
     "the eye works better at night", "thunder waits for rain", "A",
     "Light races ahead while sound walks behind."),
    (T_LIT, "Medium", "The magnification produced by a lens is the ratio of",
     "image height to object height", "object height to image height",
     "focal length to object distance", "power to voltage", "A",
     "How many times taller the image stands."),
    (T_LIT, "Easy", "An image that cannot be caught on a screen because the light only seems to come from it is",
     "virtual", "real", "inverted", "laterally reversed only", "A",
     "The bathroom mirror serves every morning."),
    (T_LIT, "Medium", "A car's driving mirror is made convex because a convex mirror",
     "shows a wide field of view behind", "makes a very large image",
     "focuses light on the driver", "removes glare completely", "A",
     "The bulging glass squeezes the whole road behind."),
    (T_CEL, "Medium", "A glass rod rubbed with dry silk becomes positively charged because the glass",
     "loses electrons to the silk", "gains protons from the silk",
     "gains electrons from the silk", "creates new charges", "A",
     "Negative electrons depart, leaving a positive rod."),
    (T_CEL, "Easy", "To read the potential difference across a lamp, a voltmeter is connected",
     "in parallel with the lamp", "in series with the lamp",
     "across the battery's cell only", "inside the lamp holder", "A",
     "It sits astride the two terminals it compares."),
    (T_CEL, "Medium", "Doubling the length of a wire, keeping everything else about it the same, does what to its resistance?",
     "It doubles the resistance", "It halves the resistance",
     "It leaves it unchanged", "It removes it entirely", "A",
     "Twice the wire means twice the path to push through."),
    (T_CEL, "Easy", "An electric iron becomes hot when switched on because the current in its element produces",
     "heat", "magnetism only", "chemical changes", "sound waves", "A",
     "The glowing element is the heating effect at work."),
    (T_ELE, "Hard", "Doping pure silicon with a small amount of a trivalent impurity such as boron produces",
     "p-type material", "n-type material",
     "a pure insulator", "a superconductor", "A",
     "Holes outnumber the electrons left behind."),
    (T_ELE, "Medium", "In a radio receiver, the transistor chiefly serves to",
     "amplify weak signals", "store electric charge",
     "step up the voltage", "measure the current", "A",
     "A whisper fed in comes out a shout."),
    (T_MOD, "Easy", "A beta particle is identical to",
     "an electron", "a helium nucleus", "a neutron", "a photon of light", "A",
     "It is a fast electron thrown out of the nucleus."),
    (T_MOD, "Hard", "When a radioactive nuclide emits a gamma ray, its mass number and atomic number both",
     "remain unchanged", "each fall by one",
     "each rise by one", "fall to zero together", "A",
     "The gamma ray carries only energy away."),
    (T_MOD, "Medium", "The instrument commonly used in the laboratory to detect and count nuclear radiations is the",
     "Geiger-Muller counter", "galvanometer",
     "voltmeter", "ammeter", "A",
     "Its tube clicks at each passing ray."),
    (T_MOD, "Hard", "A laboratory source of 800 g has a half-life of 2 days. The mass left after 6 days is",
     "100 g", "200 g", "400 g", "50 g", "A",
     "Three halvings: 800, 400, 200, then 100.", "100"),
    (T_MOD, "Medium", "Workers handling radioactive sources keep them with tongs and wear film badges chiefly to",
     "limit their exposure to radiation", "increase the source's half-life",
     "make the source stronger", "keep the source clean", "A",
     "Distance and monitoring guard the body."),
    (T_MAG, "Medium", "The production of an electric current in a coil by moving a magnet into it is called",
     "electromagnetic induction", "electrolysis",
     "electroplating", "magnetic screening", "A",
     "The moving magnet stirs up current in its wake."),
    (T_FOR, "Hard", "A spring stretches by 2 cm for every 50 g hung on it, until the load grows too heavy. Within that limit, the behaviour follows",
     "Hooke's law", "Boyle's law",
     "Ohm's law", "Newton's third law", "A",
     "Extension grows in step with the load."),
    (T_FOR, "Medium", "A door opens most easily when pushed at the edge farthest from its hinges because there",
     "the moment of the force is greatest", "the door weighs least",
     "friction disappears entirely", "the handle is coldest", "A",
     "A long arm turns the same push into more turning effect."),
]

build_batch(
    S,
    "batch_172_neco_physics5.json",
    "172",
    "NECO Physics round 5 (R32 top-up): micrometer 0.01 mm; mass "
    "constant everywhere; impulse as force times time; conservation "
    "of energy; staircase power 250 W; the wheelbarrow as a "
    "second-class lever; Boyle's law; barometer lower on the "
    "mountain; relative density; floating ice; latent heat of "
    "fusion; evaporation versus boiling; metal pot, plastic handle; "
    "Brownian motion; timbre; ultrasound; amplitude; the tightened "
    "guitar string; thunder after lightning; magnification ratio; "
    "virtual image; convex driving mirror; glass rod losing "
    "electrons; voltmeter in parallel; wire length doubles "
    "resistance; the iron's heating effect; trivalent p-type; the "
    "transistor amplifying; beta as electron; gamma leaving A and Z "
    "untouched; the Geiger counter; 800 g halved thrice to 100 g; "
    "film badges and tongs; induction by a moving magnet; Hooke's "
    "law; the door's far edge. Scanned against NECO rounds 1-4, "
    "WAEC Physics (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
