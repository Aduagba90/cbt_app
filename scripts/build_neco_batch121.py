"""Batch 121 - WAEC Physics round 3 (WAEC top-up, Round 23).

Lifts WAEC Physics from 142 toward ~185 with angles not yet in any
bank: instruments and accuracy, motion graphs, momentum numerics, machines
and efficiency, heat calculations, gas laws, waves and echoes, lenses,
electric circuits and billing, magnetism, radioactivity numerics and
electronics basics. Scanned against WAEC rounds 1-2, NECO Physics and
the JAMB Physics pool.

    python3 scripts/build_neco_batch121.py -> content/batch_121_waec_phy3.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Physics"

T_MEAS = "Measurement and Instruments"
T_MOT = "Motion, Force and Momentum"
T_EN = "Energy, Work and Machines"
T_HEAT = "Heat and Gases"
T_WAV = "Waves, Sound and Light"
T_ELE = "Electricity and Magnetism"
T_MOD = "Modern Physics and Electronics"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- measurement
    (T_MEAS, "Medium", "The instrument best suited to measuring the diameter of a thin wire is the",
     "micrometer screw gauge", "metre rule", "vernier caliper only", "tape rule", "A",
     "It reads to a hundredth of a millimetre."),
    (T_MEAS, "Medium", "A vernier caliper reads lengths to an accuracy of about",
     "0.1 mm", "1 cm", "0.1 cm only", "1 mm only", "A",
     "Its slide sharpens the scale.", "0.1"),
    (T_MEAS, "Medium", "The volume of an irregular stone is best found with a",
     "measuring cylinder and water", "ruler and formula", "spring balance", "barometer", "A",
     "The displaced water tells it."),
    (T_MEAS, "Hard", "A stopwatch reading used in a physics experiment is an example of a quantity that is",
     "measured, not counted", "always exact", "dimensionless", "a base quantity", "A",
     "Time readings carry some uncertainty."),

    # ------------------------------------------------------------- motion and momentum
    (T_MOT, "Medium", "On a velocity-time graph, the slope represents",
     "acceleration", "distance", "speed", "displacement", "A",
     "Slope over time yields it."),
    (T_MOT, "Medium", "What quantity does the space beneath a velocity-time graph measure?",
     "distance travelled", "acceleration", "force", "power", "A",
     "Multiply the axes' product and sum."),
    (T_MOT, "Hard", "A car speeds up from 10 m/s to 30 m/s in 4 s; its acceleration is",
     "5 m/s squared", "10 m/s squared", "2.5 m/s squared", "20 m/s squared", "A",
     "Change of velocity over time.", "(30-10)/4"),
    (T_MOT, "Hard", "A body of mass 2 kg moving at 6 m/s has momentum of",
     "12 kg m/s", "3 kg m/s", "8 kg m/s", "36 kg m/s", "A",
     "It is mass times velocity.", "2*6"),
    (T_MOT, "Hard", "Two colliding bodies exchange momentum yet keep the total constant; this states the conservation of",
     "momentum", "energy only", "mass number", "charge", "A",
     "No outside force interferes."),
    (T_MOT, "Medium", "Newton's third law pairs of forces act on",
     "different bodies", "the same body", "one direction only", "no body at all", "A",
     "Action here, reaction there."),
    (T_MOT, "Medium", "A body in equilibrium under forces has their resultant equal to",
     "zero", "its weight", "unity", "infinity", "A",
     "All the pulls cancel out."),

    # ------------------------------------------------------------- energy, work, machines
    (T_EN, "Hard", "Pushing with 50 N through a distance of 4 m does work of",
     "200 joules", "12.5 joules", "54 joules", "400 joules", "A",
     "Work is force times distance.", "50*4"),
    (T_EN, "Hard", "A machine lifts 300 N through 2 m using an effort of 150 N over 6 m; its velocity ratio is",
     "3", "2", "4", "0.5", "A",
     "Effort distance over load distance.", "6/2"),
    (T_EN, "Hard", "A machine with MA 2 and VR 4 runs at an efficiency of",
     "50%", "25%", "75%", "100%", "A",
     "Divide MA by VR for percent.", "2/4*100"),
    (T_EN, "Medium", "Power is defined as the rate of doing",
     "work", "force", "torque", "stress", "A",
     "Joules per second measure it."),
    (T_EN, "Hard", "A 60 W lamp runs for 10 s; the energy used is",
     "600 joules", "6 joules", "70 joules", "6000 joules", "A",
     "Energy equals power times time.", "60*10"),
    (T_EN, "Medium", "Pull back a catapult and the rubber stores mainly",
     "elastic potential", "kinetic", "chemical", "nuclear", "A",
     "Release turns it to motion."),

    # ------------------------------------------------------------- heat and gases
    (T_HEAT, "Hard", "Heat gained by 2 kg of water warmed 3 K (c = 4200 J per kg K) is",
     "25,200 J", "8,400 J", "12,600 J", "50,400 J", "A",
     "Use mass times c times rise.", "2*4200*3"),
    (T_HEAT, "Hard", "Heat needed to melt 0.5 kg of ice at 0 degrees (L = 336,000 J/kg) is",
     "168,000 J", "336,000 J", "672,000 J", "84,000 J", "A",
     "Multiply mass by latent heat.", "0.5*336000"),
    (T_HEAT, "Medium", "The anomalous expansion of water is shown by water",
     "contracting till 4 degrees only", "boiling at all temperatures", "freezing from the bottom up", "expanding without limit", "A",
     "Below 4 degrees it reverses."),
    (T_HEAT, "Medium", "A bimetallic strip bends when heated because the two metals",
     "expand by different amounts", "melt at once", "conduct equally", "shrink alike", "A",
     "The brass curves out first."),
    (T_HEAT, "Hard", "At constant temperature, doubling the volume of a fixed gas mass",
     "halves its pressure", "doubles its pressure", "keeps pressure constant", "zeroes its pressure", "A",
     "Boyle's law governs this."),
    (T_HEAT, "Hard", "Heating a gas at constant volume raises its pressure because the molecules",
     "strike walls harder", "shrink in size", "escape the container", "lose all speed", "A",
     "Hotter molecules strike harder."),

    # ------------------------------------------------------------- waves, sound, light
    (T_WAV, "Hard", "An echo returns 2 s after the clap; the wall is 340 m away (sound = 340 m/s) because sound travels",
     "340 m each way in 2 s", "170 m in 2 s", "680 m each way", "340 m in 4 s", "A",
     "Half the time is one-way.", "2*340/2"),
    (T_WAV, "Medium", "Sound waves are longitudinal because their vibrations are",
     "along the travel path", "at right angles", "absent entirely", "circular only", "A",
     "Compressions follow rarefactions."),
    (T_WAV, "Medium", "Light waves differ from sound waves because light",
     "can travel through a vacuum", "needs a material medium", "is always longitudinal", "travels slower", "A",
     "Space's silence yet sunshine."),
    (T_WAV, "Hard", "A converging lens forms a real, inverted image when the object lies",
     "beyond the focal length", "inside the focal length", "on the lens surface", "at infinity only", "A",
     "Rays truly meet after the lens."),
    (T_WAV, "Medium", "White light splitting through a prism shows it is",
     "a mixture of colours", "a pure element", "always invisible", "monochromatic", "A",
     "Red bends least, violet most."),
    (T_WAV, "Medium", "The pitch of a note is decided chiefly by its",
     "frequency", "amplitude", "speed", "medium only", "A",
     "More vibrations each second, higher note."),

    # ------------------------------------------------------------- electricity
    (T_ELE, "Hard", "A 12 V battery drives 3 A through a resistor; its resistance is",
     "4 ohms", "36 ohms", "0.25 ohms", "15 ohms", "A",
     "Divide voltage by current.", "12/3"),
    (T_ELE, "Hard", "Two 6-ohm resistors in parallel give a total resistance of",
     "3 ohms", "12 ohms", "6 ohms", "0.5 ohms", "A",
     "Two equal resistors halve their value.", "6*6/(6+6)"),
    (T_ELE, "Medium", "In a series circuit, the current passing through each component is",
     "the same", "divided equally always", "zero after the first", "highest at the end", "A",
     "One path carries one flow."),
    (T_ELE, "Hard", "A 2 kW heater running 5 hours at N30 per kWh costs",
     "N300", "N150", "N600", "N60", "A",
     "kW times hours times rate.", "2*5*30"),
    (T_ELE, "Medium", "The device that measures electric current is the",
     "ammeter", "voltmeter", "ohmmeter only", "wattmeter", "A",
     "It connects in the series path."),
    (T_ELE, "Medium", "A suspended magnet comes to rest pointing",
     "north-south", "east-west", "up-down", "any random way", "A",
     "The earth's field aligns it."),
    (T_ELE, "Medium", "Soft iron is used in transformer cores because it",
     "magnetises and demagnetises easily", "keeps magnetism forever", "is a poor conductor", "is very heavy", "A",
     "Quick to gain, quick to lose."),

    # ------------------------------------------------------------- modern and electronics
    (T_MOD, "Hard", "A radioactive source's activity falls to one eighth after 3 half-lives because 2 cubed is 8; so after 3 half-lives the fraction remaining is",
     "1/8", "1/3", "1/6", "3/8", "A",
     "Halve it three times over.", "1/2**3"),
    (T_MOD, "Medium", "Which particle matches the alpha particle exactly?",
     "helium nucleus", "electron", "photon", "hydrogen atom", "A",
     "Two protons, two neutrons."),
    (T_MOD, "Medium", "Gamma radiation is best stopped by",
     "thick lead blocks", "thin paper", "a sheet of card", "human skin alone", "A",
     "Even steel struggles with it."),
    (T_MOD, "Hard", "The photoelectric effect shows light behaving as",
     "packets of energy", "a continuous wave only", "a magnetic field", "a sound-like ripple", "A",
     "Einstein's photons knock electrons."),
    (T_MOD, "Medium", "In a p-n junction diode, conventional current flows",
     "from p to n only", "from n to p only", "both ways equally", "never at all", "A",
     "Forward bias opens the gate."),
    (T_MOD, "Hard", "Splitting a heavy uranium nucleus releases energy by",
     "nuclear fission", "nuclear fusion", "chemical burning", "radio static", "A",
     "The pieces weigh less than the whole."),
    (T_MOD, "Medium", "The transistor in a radio mainly serves to",
     "amplify weak signals", "store songs", "replace the battery", "tune the dial only", "A",
     "Small inputs become loud outputs."),
]

build_batch(
    S,
    "batch_121_waec_phy3.json",
    "121",
    "WAEC Physics round 3 (Round 23 top-up): micrometer and vernier "
    "accuracy, displacement volume, velocity-time gradient and area, "
    "acceleration 5 m/s squared, momentum 12 kg m/s and its "
    "conservation, Newton's third law, equilibrium, work 200 J, velocity "
    "ratio 3, efficiency 50%, power, lamp energy 600 J, elastic energy, "
    "water heat 25,200 J, ice latent heat 168,000 J, anomalous "
    "expansion, bimetallic strip, Boyle's law, constant-volume heating, "
    "echo 340 m, longitudinal sound, light in vacuum, real images, "
    "dispersion, pitch, resistance 4 ohms, parallel 3 ohms, series "
    "current, heater bill N300, ammeter, compass rest direction, soft "
    "iron cores, one-eighth activity, alpha particle, gamma shielding, "
    "photoelectric effect, diode direction, fission and transistor "
    "amplification. Scanned against WAEC rounds 1-2, NECO Physics and "
    "the JAMB Physics pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
