"""Batch 176 - WAEC Physics round 6 (WAEC top-up, R33).

Grows WAEC Physics from 218 toward ~253 with angles not yet in the
bank: the principle of moments; terminal velocity of a raindrop;
the orbiting astronaut; the relative density bottle; the hydrometer;
upthrust as displaced weight; capillarity; viscosity; the jar lid
in hot water; resonance between forks; the magnifying glass image;
the umbra; internal resistance and terminal p.d.; the e.m.f. as
energy per coulomb; the filament bulb's wasted heat; beta raising
the atomic number; average speed 30 km/h; gravity holding the
atmosphere; the manometer; the longer spanner's greater moment;
the spring balance losing 2 N in water; free electrons and metal
conduction; the dull black radiator; the pot's convection current;
frequency unchanged between media; the eclipse between sun and
earth; the ray along the normal; two mirrors at right angles;
the 25 cm near point; why transformers refuse d.c.; the electric
bell; protons plus neutrons; the nuclear station's turbines;
repetition against random error; the speedometer's instantaneous
reading. Scanned against WAEC rounds 1-5, NECO Physics (all
rounds) and the JAMB pool.

    python3 scripts/build_neco_batch176.py -> content/batch_176_waec_physics6.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Physics"

T_MEAS = "Measurements and Units"
T_MOT = "Motion"
T_FOR = "Force, Momentum and Newton's Laws"
T_PRU = "Pressure and Upthrust"
T_HEA = "Heat Energy"
T_WAS = "Waves and Sound"
T_LIT = "Light and Optics"
T_ELE = "Electricity"
T_MAG = "Magnetism and Electromagnetism"
T_MOD = "Modern Physics"

PASSAGES = []
PQ = []

Q = [
    (T_FOR, "Hard", "A uniform beam rests balanced on a pivot. For the beam to remain level, the sum of the clockwise moments must equal",
     "the sum of the anticlockwise moments", "the total weight of the beam only",
     "the beam's mass times its length", "zero in every direction always", "A",
     "Turning effects on both sides cancel out exactly."),
    (T_FOR, "Medium", "A raindrop falling from a great height finally settles at a steady velocity because",
     "air resistance has grown to balance its weight", "its weight gradually falls to nothing",
     "the earth's pull stops acting on it", "the air beneath it turns solid", "A",
     "Equal and opposite forces leave no acceleration."),
    (T_FOR, "Hard", "An astronaut inside an orbiting spacecraft floats about because",
     "he and the craft fall freely around the earth together", "no gravity exists so far from the ground",
     "his mass has become zero in space", "the engines push him sideways always", "A",
     "Everything shares the same free fall around the planet."),
    (T_MEAS, "Medium", "A relative density bottle is used in the laboratory to",
     "find a liquid's density", "measure atmospheric pressure",
     "time a pendulum's swing", "read tiny current differences", "A",
     "Weighing full and empty gives the liquid's mass per volume."),
    (T_PRU, "Medium", "The instrument that floats in a liquid to read its relative density directly is the",
     "hydrometer", "barometer",
     "manometer", "hydraulic press gauge", "A",
     "It sinks deeper in lighter liquids."),
    (T_PRU, "Easy", "A stone hangs fully inside a bucket of water on a spring balance. The upthrust on the stone equals",
     "the weight of water it displaces", "its own full weight in air",
     "the weight of the bucket", "the volume of the stone only", "A",
     "Archimedes ties upthrust to displaced fluid."),
    (T_PRU, "Medium", "Water climbs a little way up a narrow glass tube dipped into it. This rise is called",
     "capillarity", "viscosity",
     "osmosis", "surface evaporation", "A",
     "The narrow tube wicks the water upward."),
    (T_PRU, "Hard", "The internal friction between the layers of a flowing liquid, which opposes the flow, is called",
     "viscosity", "capillarity",
     "upthrust", "surface tension", "A",
     "Thick palm oil has it more than water."),
    (T_HEA, "Easy", "A stubborn metal lid on a glass jar comes loose easily after hot water is poured over it because",
     "the metal expands more than the glass", "the glass melts a little at the rim",
     "the water washes the threads clean", "the lid gains weight and slips", "A",
     "Different expansions part the two materials."),
    (T_HEA, "Hard", "A struck tuning fork makes an identical fork nearby begin to sound. The effect is called",
     "resonance", "reverberation",
     "refraction", "interference of light", "A",
     "Matching frequencies transfer the vibration through air."),
    (T_HEA, "Medium", "Metals conduct heat far better than non-metals mainly because metals possess",
     "free electrons that carry energy quickly", "more atoms packed per gram",
     "heavier nuclei in their atoms", "hollow tubes inside the lattice", "A",
     "The electron cloud courier of energy races ahead."),
    (T_HEA, "Medium", "Dull black cooling fins at the back of a refrigerator work best because a blackened surface is a good",
     "radiator of heat", "reflector of heat",
     "conductor of electricity", "insulator of heat", "A",
     "What absorbs well also radiates well."),
    (T_HEA, "Easy", "A pot of water warming on a stove circulates its heat chiefly by",
     "convection", "conduction through the metal only",
     "radiation across the kitchen", "capillary rise", "A",
     "Hot water rises and cooler water sinks to take its place."),
    (T_WAS, "Medium", "When a water wave crosses from deep water into shallow water, the property that remains unchanged is its",
     "frequency", "wavelength",
     "speed", "depth of travel", "A",
     "The source's vibrations fix the frequency."),
    (T_LIT, "Easy", "During a solar eclipse, the body that comes between the sun and the earth is the",
     "moon", "earth itself",
     "Venus", "a passing comet", "A",
     "The moon's shadow sweeps across the earth."),
    (T_LIT, "Medium", "A ray of light entering a glass block exactly along the normal to the surface",
     "passes straight on without bending", "bends sharply towards the normal",
     "bends away from the normal", "is reflected back entirely", "A",
     "Zero angle of incidence means zero refraction."),
    (T_LIT, "Hard", "Two plane mirrors set at right angles to each other facing a coin produce a number of images equal to",
     "three", "two",
     "four", "one only", "A",
     "Ninety degrees folds the coin into three views."),
    (T_LIT, "Medium", "When a convex lens serves as a magnifying glass, the image it forms is",
     "virtual, erect and magnified", "real, inverted and small",
     "real, erect and equal", "virtual, inverted and tiny", "A",
     "The object sits inside the focal length."),
    (T_LIT, "Easy", "The completely dark centre region of a shadow cast by an opaque object is the",
     "umbra", "penumbra",
     "eclipse", "image", "A",
     "No ray of light enters that core."),
    (T_LIT, "Medium", "The least distance of distinct vision for a normal human eye is about",
     "25 cm", "2.5 cm",
     "250 cm", "5 mm", "A",
     "Closer than this the eye cannot focus.", "25"),
    (T_ELE, "Hard", "When a cell supplies current to a circuit, the potential difference across its terminals is",
     "less than its electromotive force", "greater than its electromotive force",
     "exactly equal always", "zero whenever current flows", "A",
     "Internal resistance swallows part of the e.m.f."),
    (T_ELE, "Medium", "The electromotive force of a cell is best described as the",
     "energy it gives to each coulomb of charge", "force pushing electrons through a wire",
     "current it forces round the circuit", "number of cells joined in series", "A",
     "Joules per coulomb measure its strength."),
    (T_ELE, "Easy", "In a filament lamp, most of the electrical energy supplied is finally wasted as",
     "heat", "sound",
     "chemical change", "mechanical motion", "A",
     "Only a small share leaves as light."),
    (T_ELE, "Medium", "A stone hangs from a spring balance reading 5 N in air. Lowered into water, the balance reads 3 N. The upthrust of the water is",
     "2 N", "3 N",
     "5 N", "8 N", "A",
     "The balance loses exactly what the water gives.", "2"),
    (T_MAG, "Medium", "A transformer cannot operate on steady direct current because direct current produces",
     "no changing magnetic flux in the core", "too much current at once",
     "a reversed voltage in the secondary", "magnetic poles that never form", "A",
     "Induction needs a continually changing flux."),
    (T_MAG, "Easy", "When the button of an electric bell is pressed, the hammer keeps striking the gong because the electromagnet",
     "repeatedly makes and breaks the circuit", "spins the hammer round a wheel",
     "stores charge in a capacitor", "heats a bimetallic strip", "A",
     "Each break releases the armature to strike again."),
    (T_MOD, "Medium", "When a radioactive nuclide emits a beta particle, the atomic number of the nuclide",
     "increases by one", "decreases by one",
     "remains unchanged", "increases by four", "A",
     "A neutron has changed into a proton."),
    (T_MOD, "Medium", "The sum of the protons and neutrons inside an atomic nucleus gives the",
     "mass number", "atomic number",
     " proton number", "neutron density", "A",
     "Together the nucleons are counted."),
    (T_MOD, "Medium", "In a nuclear power station, the heat released by fission is used chiefly to",
     "raise steam that drives turbines", "light the control room lamps",
     "charge car batteries directly", "melt the fuel rods for reuse", "A",
     "Spinning generators make the electricity."),
    (T_MOT, "Medium", "A motorist covers 40 km in the first hour and 20 km in the second hour. His average speed for the whole journey is",
     "30 km/h", "40 km/h",
     "20 km/h", "60 km/h", "A",
     "Total distance over total time.", "30"),
    (T_MOT, "Easy", "The reading on a car's speedometer at any instant gives the car's",
     "instantaneous speed", "average speed since departure",
     "acceleration in km/h", "distance covered that day", "A",
     "It samples the speed of the moment."),
    (T_MEAS, "Medium", "Repeating a measurement several times and taking the average chiefly reduces",
     "random errors", "all errors completely",
     "the instrument's zero error", "the unit of the quantity", "A",
     "Chance highs and lows cancel one another."),
    (T_MEAS, "Easy", "The earth's atmosphere stays bound to the earth because of the earth's",
     "gravity", "magnetic field",
     "rotation from west to east", "heat from the sun", "A",
     "Every air molecule is pulled earthward."),
    (T_ELE, "Medium", "The pressure of a gas supply in the laboratory is compared with the atmosphere using a",
     "manometer", "barometer",
     "ammeter", "voltmeter", "A",
     "The liquid columns show the difference."),
    (T_FOR, "Easy", "A stubborn nut turns more easily when the mechanic slips on a longer spanner because the longer spanner gives",
     "a greater turning moment", "a smaller force at the nut",
     "a firmer grip by its teeth", "less friction at the thread", "A",
     "The longer arm multiplies the turning effect."),
]

build_batch(
    S,
    "batch_176_waec_physics6.json",
    "176",
    "WAEC Physics round 6 (R33 top-up): principle of moments; "
    "terminal velocity of the raindrop; the orbiting astronaut in "
    "free fall; the relative density bottle; the hydrometer; "
    "upthrust as displaced weight; capillarity; viscosity; the jar "
    "lid over hot water; resonance of matching forks; free "
    "electrons carrying heat; the dull black radiator; the pot's "
    "convection; frequency unchanged between media; the eclipse "
    "geometry; the ray along the normal; two mirrors at ninety "
    "degrees giving three images; the magnifying glass; the "
    "umbra; the 25 cm near point; terminal p.d. below e.m.f.; "
    "e.m.f. as energy per coulomb; the filament's wasted heat; "
    "the balance losing 2 N to upthrust; why transformers refuse "
    "d.c.; the electric bell's make-and-break; beta raising the "
    "atomic number; nucleons giving the mass number; fission "
    "raising steam for turbines; 30 km/h average; the "
    "speedometer's instantaneous reading; repetition against "
    "random error; gravity holding the atmosphere; the manometer; "
    "the longer spanner's moment. Scanned against WAEC rounds "
    "1-5, NECO Physics (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
