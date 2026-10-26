"""Batch 204 - NECO Physics round 7 (NECO top-up, R40).

Grows NECO Physics from 234 toward ~258 with angles not yet in
the bank: Newton's second law; inertia; the ampere; the newton;
the kilogram; speed, velocity and acceleration defined; weight
defined; heat vs temperature; the echo defined; magnetic
materials; magnetic poles; the step-down transformer; work and
energy defined; pressure defined; the beam balance; the ammeter;
conductors and insulators; heat flow direction; body temperature;
sound from vibration. Scanned against the whole Physics pool
(WAEC, NECO and JAMB stems, 1,300 items).

    python3 scripts/build_neco_batch204.py -> content/batch_204_neco_physics7.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Physics"

T_MECH = "Mechanics"
T_HEAT = "Heat Energy"
T_WAV = "Waves and Sound"
T_ELE = "Electricity and Magnetism"

PASSAGES = []
PQ = []

Q = [
    (T_MECH, "Medium", "Newton's second law of motion states that the rate of change of momentum of a body is directly proportional to the",
     "force applied to it", "mass of the body",
     "distance it travels", "time it spends", "A",
     "Force is the push that changes motion."),
    (T_MECH, "Easy", "The reluctance of a body to change its state of rest or of uniform motion is called",
     "inertia", "momentum",
     "impulse", "friction", "A",
     "Heavy loads resist being started or stopped."),
    (T_MECH, "Easy", "The SI unit of force is the",
     "newton", "joule",
     "watt", "pascal", "A",
     "One newton accelerates a kilogram by one metre per second squared."),
    (T_MECH, "Easy", "The SI base unit used to measure the mass of a body is the",
     "kilogram", "newton",
     "gram weight", "joule", "A",
     "The platinum cylinder in Paris sets the standard."),
    (T_MECH, "Easy", "The distance travelled by a body per unit time is its",
     "speed", "acceleration",
     "velocity's direction", "displacement", "A",
     "The odometer counts it as you go."),
    (T_MECH, "Medium", "The speed of a body in a stated direction is its",
     "velocity", "acceleration",
     "momentum", "power", "A",
     "Speed with a signpost attached."),
    (T_MECH, "Medium", "The rate of change of velocity of a body with time is its",
     "acceleration", "speed",
     "distance", "retardation only", "A",
     "Velocity's own rate of change."),
    (T_MECH, "Medium", "The force with which the earth pulls a body towards itself is the body's",
     "weight", "mass",
     "inertia", "density", "A",
     "It grows weaker the farther you go."),
    (T_MECH, "Medium", "The product of a force and the distance it moves its point of application along the line of action is",
     "work done", "power developed",
     "moment of force", "pressure applied", "A",
     "Push without movement earns no work."),
    (T_MECH, "Medium", "The capacity of a body to do work is its",
     "energy", "force",
     "power", "momentum", "A",
     "Stored work, ready to be spent."),
    (T_MECH, "Medium", "The force acting normally per unit area of a surface is",
     "pressure", "thrust alone",
     "stress of motion", "weight", "A",
     "The same push spread thinner hurts less."),
    (T_MECH, "Easy", "The mass of an object is measured in the laboratory with a",
     "beam balance", "spring balance",
     "hydrometer", "barometer", "A",
     "It compares mass with standard masses."),
    (T_ELE, "Easy", "The instrument used to measure the electric current flowing in a circuit is the",
     "ammeter", "voltmeter",
     "ohmmeter", "galvanometer scale", "A",
     "It is connected in series in the circuit."),
    (T_ELE, "Medium", "Materials that allow electric current to pass through them easily are called",
     "conductors", "insulators",
     "semiconductors", "diodes", "A",
     "Copper wire carries the current gladly."),
    (T_ELE, "Medium", "The transformer used at substations near homes to bring the high transmission voltage down to a safe level for household use is a",
     "step-down transformer", "step-up transformer",
     "generator coil", "rectifier unit", "A",
     "It hands the grid's power gently to the house."),
    (T_ELE, "Medium", "The parts of a magnet where its attractive power is strongest are its",
     "poles", "middle regions",
     "edges only", "coatings", "A",
     "Iron filings cluster thickly at the ends."),
    (T_ELE, "Medium", "Which of the following groups contains only magnetic materials?",
     "Iron, nickel and cobalt", "Copper, zinc and tin",
     "Aluminium, silver and gold", "Lead, sulphur and carbon", "A",
     "The three metals a magnet eagerly grabs."),
    (T_HEAT, "Medium", "The quantity of heat possessed by a body differs from its temperature in that heat depends on the body's",
     "mass as well as its temperature", "colour as well as its shape",
     "weight alone in vacuum", "melting point only", "A",
     "A cup and a drum of boiling water share one temperature."),
    (T_HEAT, "Easy", "When a hot metal block is dropped into cold water, heat flows from the block to the water until both reach the same",
     "temperature", "mass",
     "volume", "density", "A",
     "Heat always slides down the temperature hill."),
    (T_HEAT, "Easy", "The normal temperature of the human body is about",
     "37 °C", "45 °C",
     "27 °C", "98 °F only", "A",
     "The clinical thermometer reads around it.", "37"),
    (T_WAV, "Medium", "The sound heard after the original sound has been reflected from a distant surface is an",
     "echo", "undertone",
     "harmonic", "pitch", "A",
     "The cliff throws the shout back."),
    (T_WAV, "Easy", "Sound is produced whenever a body",
     "vibrates", "heats up",
     "cools down", "stands still", "A",
     "The drum skin trembles and the air carries it."),
    (T_WAV, "Medium", "Doubling the speed of a moving car multiplies its kinetic energy by",
     "4", "2",
     "8", "1", "A",
     "Double the speed and the energy quadruples.", "4"),
]

build_batch(
    S,
    "batch_204_neco_physics7.json",
    "204",
    "NECO Physics round 7 (R40 top-up): Newton's second law; "
    "inertia; the newton and ampere; the kilogram; speed, velocity "
    "and acceleration defined; weight; work and energy defined; "
    "pressure; the beam balance; the ammeter; conductors; the "
    "step-down transformer; magnetic poles; iron, nickel and "
    "cobalt; heat vs temperature; heat flow to equal temperature; "
    "body temperature 37 °C; the echo; sound by vibration; KE "
    "depends on velocity squared. Scanned against the whole "
    "Physics pool (WAEC, NECO and JAMB stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
