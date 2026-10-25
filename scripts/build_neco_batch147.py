"""Batch 147 - WAEC Physics round 5 (WAEC top-up, R27).

Grows WAEC Physics from 185 toward ~221 with angles not yet in the
bank: vernier precision and density arithmetic; scalars vs vectors;
distance-time graph reading; equations of motion; Newton's third-law
pairs; momentum conservation; efficiency arithmetic; anomalous
expansion of water; absolute zero; latent heat arithmetic; prism
deviation; lens power in dioptres; magnification arithmetic; lens for
short sight; the wave equation; sound as longitudinal wave;
electromagnetic spectrum order; Ohm's law and mixed-resistor
arithmetic; the kilowatt-hour bill; magnetic circles around a current;
Lenz's law; X-ray and photoelectric ideas; isotopes; alpha decay's
mass change; surface tension. Numeric items carry verify strings where
the correct option's first number equals the value. Scanned against
WAEC rounds 1-3, NECO Physics (all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch147.py -> content/batch_147_waec_physics5.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Physics"

T_ME = "Measurement and Density"
T_MO = "Motion and Forces"
T_EN = "Energy and Power"
T_HE = "Heat Further"
T_LI = "Light and Lenses"
T_WA = "Waves Further"
T_EL = "Electricity Further"
T_MG = "Magnetism and Induction Further"
T_MD = "Modern Physics Further"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- measurement
    (T_ME, "Medium", "A vernier caliper can read lengths to a precision of",
     "0.01 cm", "1 cm", "0.5 cm", "10 cm", "A",
     "Its sliding scale splits each millimetre.", "0.01"),
    (T_ME, "Medium", "A metal cube of side 2 cm balances the scale at 24 grams. Its density works out to",
     "3 g per cubic cm", "12 g per cubic cm", "0.75 g per cubic cm", "48 g per cubic cm", "A",
     "Mass over the eight cubic cm.", "3"),
    (T_ME, "Medium", "Which quantity needs BOTH magnitude and direction for its full description?",
     "displacement", "speed", "mass", "time", "A",
     "It points as well as sizes."),

    # ------------------------------------------------------------- motion & forces
    (T_MO, "Medium", "A straight, sloping distance-time graph tells us the object moved with",
     "uniform speed", "increasing acceleration", "no motion at all", "uneven jerks", "A",
     "Equal distance in equal time."),
    (T_MO, "Hard", "Starting from rest with uniform acceleration 2 m per second squared, a body's velocity after 5 seconds is",
     "10 m per second", "7 m per second", "2.5 m per second", "20 m per second", "A",
     "V equals u plus a t, all in order.", "10"),
    (T_MO, "Hard", "At the highest point of a projectile's flight, its velocity is",
     "entirely horizontal", "entirely vertical", "zero in all directions", "doubled", "A",
     "Only the sideways part survives."),
    (T_MO, "Medium", "A rifle recoils as the bullet leaves, illustrating Newton's",
     "third law", "first law", "second law", "law of cooling", "A",
     "Action and reaction pair the kick."),
    (T_MO, "Hard", "A 2 kg trolley moving at 3 m per second catches up and couples with a stationary 1 kg trolley. Their common speed is",
     "2 m per second", "3 m per second", "1 m per second", "6 m per second", "A",
     "Momentum before equals after.", "2"),

    # ------------------------------------------------------------- energy
    (T_EN, "Hard", "A motor draws 600 W but delivers only 450 W of useful work. Its efficiency is",
     "75%", "60%", "45%", "133%", "A",
     "Useful output over total input.", "75"),
    (T_EN, "Medium", "In a hydroelectric dam the chain of energy conversion is",
     "potential to kinetic to electrical", "electrical to light to heat", "chemical to sound to light", "nuclear to chemical to heat", "A",
     "Falling water spins the turbines."),

    # ------------------------------------------------------------- heat
    (T_HE, "Hard", "Water shows anomalous expansion because its greatest density occurs at",
     "4 degrees Celsius", "0 degrees Celsius", "100 degrees Celsius", "-4 degrees Celsius", "A",
     "Ice floats on the denser layer.", "4"),
    (T_HE, "Medium", "The temperature at which molecular motion theoretically stops is",
     "-273 degrees Celsius", "0 degrees Celsius", "-100 degrees Celsius", "100 degrees Celsius", "A",
     "Absolute zero stands there.", "-273"),
    (T_HE, "Hard", "Melting 2 kg of ice at 0 degrees, with latent heat 330,000 J per kg, requires",
     "660,000 joules", "330,000 joules", "165,000 joules", "1,650,000 joules", "A",
     "Mass times latent heat, simply.", "660000"),
    (T_HE, "Medium", "Since the vacuum between sun and earth blocks conduction and convection, solar heat arrives by",
     "radiation", "convection currents", "conducted waves", "steam jets", "A",
     "Empty space carries no particles."),

    # ------------------------------------------------------------- light & lenses
    (T_LI, "Hard", "A triangular glass prism bends a ray of white light so that the emergent ray deviates towards the",
     "base of the prism", "apex of the prism", "left face always", "source of light", "A",
     "Two refractions lean it inward."),
    (T_LI, "Hard", "The dioptre, unit of a lens's power, is defined as one divided by the focal length measured in",
     "metres", "centimetres", "seconds", "grams", "A",
     "Power is one over focal length."),
    (T_LI, "Hard", "An object stands 5 cm from a lens and its image forms 10 cm away. The magnification is",
     "2", "0.5", "5", "50", "A",
     "Image distance over object distance.", "2"),
    (T_LI, "Medium", "A short-sighted student's distant images form before the retina; the correcting lens is",
     "concave", "convex", "cylindrical", "plane", "A",
     "It spreads the focus backward."),

    # ------------------------------------------------------------- waves
    (T_WA, "Hard", "A tuning fork of frequency 170 hertz produces sound travelling at 340 m per second. The wavelength is",
     "2 m", "1.7 m", "340 m", "0.5 m", "A",
     "Velocity divided by the frequency.", "2"),
    (T_WA, "Medium", "Sound waves, whose particles vibrate along the direction of travel, are",
     "longitudinal", "transverse", "stationary", "electromagnetic", "A",
     "Compression follows rarefaction."),
    (T_WA, "Hard", "Of the electromagnetic family, the member with the longest wavelength is",
     "radio waves", "gamma rays", "ultraviolet", "X-rays", "A",
     "Broadcast masts ride the longest."),

    # ------------------------------------------------------------- electricity
    (T_EL, "Hard", "When a 12-volt battery drives current through a 4-ohm resistor, the current that flows is",
     "3 amperes", "48 amperes", "0.33 amperes", "8 amperes", "A",
     "Ohm's law: voltage over resistance.", "3"),
    (T_EL, "Hard", "A 2-ohm resistor in series with two parallel resistors of 6 and 3 ohms presents a circuit resistance of",
     "4 ohms", "11 ohms", "2 ohms", "5 ohms", "A",
     "The parallel pair collapses to 2.", "4"),
    (T_EL, "Medium", "Electric energy is sold by the kilowatt-hour, which is the energy of a 1 kW appliance running for",
     "one hour", "one second", "one day", "one minute", "A",
     "The familiar 'unit' on bills."),
    (T_EL, "Hard", "A 1.5 kW electric kettle boiling for 4 hours (in a power cut of numbers) consumes 6 units; at 50 naira per unit the cost is",
     "N300", "N150", "N600", "N75", "A",
     "Six units at fifty naira each.", "300"),

    # ------------------------------------------------------------- magnetism
    (T_MG, "Medium", "Iron filings sprinkled on a card around a vertical current-carrying wire arrange themselves into",
     "concentric circles", "straight parallel lines", "a single bar magnet", "random loops", "A",
     "Iron filings circle the wire."),
    (T_MG, "Hard", "Lenz's law states that an induced current flows in the direction that",
     "opposes the change causing it", "supports the change fully", "heats the coil most", "flips twice per cycle", "A",
     "Nature resists the shove."),

    # ------------------------------------------------------------- modern
    (T_MD, "Hard", "X-rays are produced when fast electrons are suddenly stopped by striking a",
     "metal target", "glass wall", "rubber seal", "water jacket", "A",
     "The sudden stop frees rays."),
    (T_MD, "Hard", "The photoelectric effect shows light behaving as streams of energy packets called",
     "photons", "protons", "phonons", "neutrons", "A",
     "Each packet knocks an electron."),
    (T_MD, "Medium", "Atoms of the same element with equal protons but different neutrons are",
     "isotopes", "isomers", "ions", "allotropes", "A",
     "Hydrogen's three faces, for one."),
    (T_MD, "Hard", "In alpha decay, the mass number of the parent nucleus drops by",
     "4", "1", "2", "0", "A",
     "The alpha particle carries four.", "4"),
    (T_MD, "Medium", "Gamma rays are best described as",
     "electromagnetic waves", "charged particles", "slow neutrons", "sound in vacuum", "A",
     "No mass, no charge, pure energy."),

    # ------------------------------------------------------------- surface tension
    (T_MD, "Medium", "A pond skater walks on water because of the water's",
     "surface tension", "high density", "low viscosity", "electrical charge", "A",
     "The surface film bears its legs."),
]

build_batch(
    S,
    "batch_147_waec_physics5.json",
    "147",
    "WAEC Physics round 5 (R27 top-up): vernier 0.01 cm, density 2 g "
    "per cubic cm, velocity as vector; sloping distance-time graph, "
    "v = u + at giving 10 m/s, projectile's horizontal top velocity, "
    "third-law recoil, coupled trolleys 2 m/s; 75% efficiency, "
    "hydroelectric chain; water's 4-degree density peak, absolute "
    "zero -273, latent heat 660,000 J, solar radiation; prism deviation "
    "to base, 2-dioptre lens, magnification 2, concave for short "
    "sight; wavelength 2 m, longitudinal sound, longest-wave radio; "
    "Ohm 3 A, mixed resistance 4 ohms, the kilowatt-hour, N300 bill; "
    "concentric field circles, Lenz opposition; X-ray target, photons, "
    "isotopes, alpha mass drop 4, gamma as EM, surface tension. "
    "Scanned against WAEC rounds 1-3, NECO Physics (all rounds) and "
    "the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
