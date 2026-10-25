"""Batch 139 - NECO Physics round 4 (NECO top-up, Round 26).

Lifts NECO Physics from 159 toward ~196 with angles not yet in any
bank: precision of a metre rule; pressure at depth arithmetic; moment
of a force arithmetic; velocity ratio of an inclined plane; work
arithmetic; solar-energy conversion; linear expansivity; specific heat
capacity arithmetic; land-and-sea breeze mechanism; echo arithmetic;
plane-mirror image properties; critical angle and total internal
reflection; ammeter placement; series resistors arithmetic; electrical
power arithmetic; fuse rating logic; magnet soft-iron keepers;
step-down transformer turns arithmetic; semiconductor doping; diode
rectification; beta decay mass number; half-life arithmetic; fission
vs fusion. Numeric items carry verify strings where the correct
option's first number equals the value. Scanned against NECO rounds
1-3, WAEC Physics (all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch139.py -> content/batch_139_neco_physics4.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Physics"

T_MEAS = "Measurement and Mechanics"
T_PRE = "Pressure and Moments"
T_MAC = "Machines, Work and Energy"
T_HEAT = "Thermal Physics"
T_WAV = "Waves and Sound"
T_LIG = "Light"
T_ELE = "Current Electricity"
T_MAG = "Magnetism and Induction"
T_ELE2 = "Electronics and the Nucleus"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- measurement & mechanics
    (T_MEAS, "Medium", "The precision of a metre rule graduated in millimetres is",
     "1 mm", "1 cm", "0.1 mm", "1 m", "A",
     "The smallest graduation is its precision.", "1"),
    (T_MEAS, "Medium", "A jogger runs a 300-metre lap in 60 seconds without slowing. His uniform speed is",
     "5 m per second", "60 m per second", "5 m per minute", "0.2 m per second", "A",
     "Distance divided by time taken.", "5"),
    (T_MEAS, "Hard", "A car speeds up from rest to 20 m per second in 4 seconds. Its acceleration is",
     "5 m per second squared", "4 m per second squared", "80 m per second squared", "0.2 m per second squared", "A",
     "Velocity change over time.", "5"),

    # ------------------------------------------------------------- pressure & moments
    (T_PRE, "Hard", "Taking water at 1,000 kg per cubic metre and g as 10, the pressure on a diver 5 metres down is",
     "50,000 pascals", "5,000 pascals", "500 pascals", "10,000 pascals", "A",
     "Rho, g and h multiply in order.", "50000"),
    (T_PRE, "Medium", "A hydraulic press multiplies force because pressure is transmitted",
     "equally throughout the liquid", "only downwards", "faster than light", "only to the walls", "A",
     "Pascal's principle at work."),
    (T_PRE, "Hard", "A force of 20 newtons acts at 3 metres from a pivot. The moment of the force is",
     "60 newton-metres", "23 newton-metres", "6.7 newton-metres", "17 newton-metres", "A",
     "Force times perpendicular distance.", "60"),
    (T_PRE, "Medium", "A boy of weight 400 N sits 1.5 m from a see-saw's pivot. His kid sister of 300 N must sit",
     "2 m from the pivot", "1.5 m from the pivot", "1 m from the pivot", "3 m from the pivot", "A",
     "Smaller weight needs longer arm.", "2"),

    # ------------------------------------------------------------- machines & energy
    (T_MAC, "Hard", "A loading ramp 6 m long lifts crates 2 m onto a lorry. Ignoring friction, its velocity ratio is",
     "3", "6", "2", "0.33", "A",
     "Effort distance over load distance.", "3"),
    (T_MAC, "Medium", "Work done when a force of 50 newtons moves its point of application 4 metres in the force's line is",
     "200 joules", "12.5 joules", "54 joules", "46 joules", "A",
     "Force times distance moved.", "200"),
    (T_MAC, "Medium", "A pump lifting 60 kg of water through 10 m in one minute, with g as 10, develops a power of",
     "100 watts", "600 watts", "10 watts", "6,000 watts", "A",
     "Work of 6,000 J per 60 seconds.", "100"),
    (T_MAC, "Medium", "In a solar water heater, the sun's energy is converted mainly into",
     "heat energy", "sound energy", "nuclear energy", "chemical energy only", "A",
     "Black pipes drink the sunlight."),
    (T_MAC, "Medium", "Petrol stored in a tank holds energy that is",
     "chemical", "kinetic", "sound", "nuclear", "A",
     "Burning releases it as heat."),

    # ------------------------------------------------------------- heat
    (T_HEAT, "Hard", "A metal rod exactly 1 m long expands by 0.0012 m when heated through 60 degrees Celsius. Its linear expansivity is",
     "0.00002 per kelvin", "0.0002 per kelvin", "0.0012 per kelvin", "0.0005 per kelvin", "A",
     "Extension over length times rise.", "0.00002"),
    (T_HEAT, "Hard", "The heat needed to raise 2 kg of water by 5 degrees Celsius, with specific heat capacity 4,200 J per kg per K, is",
     "42,000 joules", "4,200 joules", "21,000 joules", "84,000 joules", "A",
     "Mass times capacity times rise.", "42000"),
    (T_HEAT, "Medium", "Sea breezes blow from ocean to land on hot afternoons because the land",
     "heats faster and rises", "cools faster and sinks", "is always wetter", "absorbs no sunshine", "A",
     "Warm land air climbs seaward air."),
    (T_HEAT, "Medium", "Heat travelling through a solid metal spoon from hot soup to the fingers is mainly",
     "conduction", "convection", "radiation", "evaporation", "A",
     "Particle to particle it walks."),

    # ------------------------------------------------------------- waves & sound
    (T_WAV, "Medium", "In a transverse wave, the vibrations of the medium are",
     "perpendicular to travel", "along the travel", "in circles", "absent entirely", "A",
     "The wave marches past the wiggle."),
    (T_WAV, "Hard", "A hunter fires beside a rock face and hears the shot return 3 seconds later, sound travelling 340 m per second. The rock face stands",
     "510 metres away", "340 metres away", "1,020 metres away", "255 metres away", "A",
     "There and back in three seconds.", "510"),
    (T_WAV, "Medium", "The loudness of a sound wave is decided chiefly by its",
     "amplitude", "frequency", "speed in air", "wavelength in vacuum", "A",
     "Bigger swing, louder voice."),

    # ------------------------------------------------------------- light
    (T_LIG, "Medium", "Standing before a dressing mirror, you raise your right hand. The image raises its",
     "left hand", "right hand", "both hands", "no hand at all", "A",
     "The mirror swaps left for right."),
    (T_LIG, "Hard", "The critical angle of a medium is the angle of incidence in the denser medium for which the angle of refraction is",
     "90 degrees", "0 degrees", "45 degrees", "180 degrees", "A",
     "The refracted ray skims the surface.", "90"),
    (T_LIG, "Medium", "Total internal reflection occurs only when light travels from",
     "denser to less dense medium", "less dense to denser medium", "air into air", "vacuum into wood", "A",
     "The crowd must thin as it leaves."),
    (T_LIG, "Medium", "A ray passing from air into glass bends towards the normal because glass is",
     "optically denser", "optically rarer", "perfectly black", "magnetic", "A",
     "Slower speed pulls it inward."),

    # ------------------------------------------------------------- electricity
    (T_ELE, "Medium", "An ammeter measuring the current in a resistor must be connected",
     "in series with it", "in parallel with it", "across the battery only", "inside the cell", "A",
     "The full current flows through it."),
    (T_ELE, "Medium", "Wired one after another in a single loop, resistors of 4 ohms and 5 ohms add up to",
     "9 ohms", "20 ohms", "4.5 ohms", "1 ohm", "A",
     "Series resistances simply add.", "9"),
    (T_ELE, "Hard", "Strapped across the same two terminals, resistors of 4 ohms and 12 ohms together behave as",
     "3 ohms", "16 ohms", "48 ohms", "6 ohms", "A",
     "Product over sum of the pair.", "3"),
    (T_ELE, "Hard", "An electric lamp marked 60 W working on a 240-volt mains draws a current of about",
     "0.25 ampere", "4 amperes", "25 amperes", "144 amperes", "A",
     "Power over voltage gives it.", "0.25"),
    (T_ELE, "Medium", "A fuse rated 13 A is fitted in a circuit drawing 30 A. The fuse will",
     "blow and break the circuit", "melt the wiring first", "raise the voltage", "boost the current", "A",
     "It dies to save the house."),
    (T_ELE, "Medium", "Earthing household appliances protects the user by providing",
     "a path for fault current", "extra voltage for motors", "cheaper electricity bills", "brighter lamp light", "A",
     "Leakage runs to the ground."),

    # ------------------------------------------------------------- magnetism & induction
    (T_MAG, "Medium", "A soft iron keeper is placed across the poles of a stored magnet to",
     "preserve its magnetism", "increase its pole gap", "make it heavier", "turn its poles around", "A",
     "The closed ring holds the field."),
    (T_MAG, "Hard", "A transformer with 1,000 primary turns stepping 220 volts down to 22 volts must have secondary turns numbering",
     "100", "1,000", "10,000", "10", "A",
     "Turns follow the voltage ratio.", "100"),
    (T_MAG, "Medium", "In a dynamo, mechanical energy fed in leaves as",
     "electrical energy", "heat energy only", "sound energy", "chemical energy", "A",
     "Coil and magnet make current."),

    # ------------------------------------------------------------- electronics & nucleus
    (T_ELE2, "Medium", "Doping pure silicon with a pentavalent impurity yields",
     "an n-type semiconductor", "a p-type semiconductor", "an insulator", "a superconductor", "A",
     "Free electrons outnumber holes."),
    (T_ELE2, "Medium", "A diode allows current to pass only when it is",
     "forward biased", "reverse biased", "unconnected", "heated red hot", "A",
     "One way is a wall, one a gate."),
    (T_ELE2, "Hard", "A single diode in a power supply converts alternating current to direct current by",
     "rectification", "amplification", "modulation", "resonance", "A",
     "Half the wave passes through."),
    (T_ELE2, "Hard", "In beta decay, the mass number of the nuclide",
     "stays unchanged", "falls by one", "falls by four", "doubles", "A",
     "A neutron swaps its charge only."),
    (T_ELE2, "Hard", "A source of half-life 5 days sits untouched on a shelf for 15 days. The fraction still radioactive is",
     "one-eighth", "one-quarter", "one-half", "one-sixteenth", "A",
     "Three halvings in fifteen days."),
    (T_ELE2, "Medium", "The splitting of a heavy nucleus into lighter ones, releasing energy, is",
     "nuclear fission", "nuclear fusion", "photoelectric emission", "thermionic emission", "A",
     "The bar of the nucleus snaps."),
    (T_ELE2, "Medium", "The joining of light nuclei to form a heavier one, powering the sun, is",
     "nuclear fusion", "nuclear fission", "radioactive decay", "gamma emission", "A",
     "Hydrogen marries into helium."),
]

build_batch(
    S,
    "batch_139_neco_physics4.json",
    "139",
    "NECO Physics round 4 (Round 26 top-up): metre-rule precision 1 mm, "
    "uniform speed 5 m/s, acceleration 5 m/s2; depth pressure 100,000 "
    "Pa, hydraulic press principle, moment 60 Nm, see-saw 2 m; plank "
    "velocity ratio 5, work 200 J, pump power 100 W, solar and petrol "
    "energy forms; expansivity 0.00002/K, heat capacity 42,000 J, sea "
    "breeze, conduction; transverse vibration, cliff echo 340 m, "
    "loudness by amplitude; plane mirror image, critical angle 90 "
    "degrees refraction, TIR direction, air-to-glass bending; ammeter "
    "series, series 9 ohms, parallel 2 ohms, 60 W lamp 0.25 A, 13 A "
    "fuse on 30 A, earthing purpose; soft-iron keeper, step-down "
    "turns 100, dynamo output; n-type doping, forward-biased diode, "
    "rectification, beta mass number constant, 24-day half-life "
    "one-eighth, fission vs fusion. Scanned against NECO rounds 1-3, "
    "WAEC Physics (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
