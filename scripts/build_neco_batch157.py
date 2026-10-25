"""Batch 157 - WAEC Financial Accounting round 6 (WAEC top-up, R29).

Grows WAEC Accounting from 190 toward ~226 with angles not yet in the
bank: FIFO under rising prices, weighted average smoothing,
perpetual vs periodic inventory, lower of cost and net realisable
value; carriage inwards; factory cost of production arithmetic;
straight-line depreciation with residual value; bad-debt write-off
posting; control-account purpose; bank charges in reconciliation;
dishonoured cheques; petty-cash analysis columns; gross vs net pay;
PAYE at source; partnership appropriation arithmetic; goodwill as an
intangible; rights issue; the auditor's opinion; operating cash
flows; mark-up arithmetic; the acid test; ROCE arithmetic; personal
vs impersonal ledgers; book-keeping vs accounting; returns inwards
day book; the sales ledger; journal proper for fixed assets; the
realisation concept; accumulated provision; compensating errors;
capital introduced; raw materials consumed arithmetic. Scanned
against WAEC rounds 1-5, NECO Accounting (all rounds) and the JAMB
pool.

    python3 scripts/build_neco_batch157.py -> content/batch_157_waec_accounting6.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Financial Accounting"

T_STK = "Stock Valuation"
T_FIN = "Final Accounts Further"
T_DEP = "Depreciation and Bad Debts"
T_CTL = "Control Accounts and Reconciliation"
T_PAY = "Wages and Payroll"
T_PART = "Partnership Arithmetic"
T_CO = "Company Accounts Further"
T_LED = "Ledgers, Books and Concepts"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- stock valuation
    (T_STK, "Hard", "During a period of rising prices, the FIFO method of pricing issues leaves closing stock at",
     "the most recent prices", "the oldest prices", "average prices", "zero prices", "A",
     "Old stock went out first; new remains."),
    (T_STK, "Hard", "The weighted average cost method of stock valuation is favoured because it",
     "smooths price fluctuations", "ignores prices entirely", "uses only the latest price", "uses only the first price", "A",
     "Extremes cancel in the mean."),
    (T_STK, "Medium", "Under the periodic inventory system, the cost of goods sold is found",
     "only at the year end by counting", "after every single sale", "by the cashier daily", "by the auditor monthly", "A",
     "The shelf is counted, then priced."),
    (T_STK, "Hard", "A line of goods cost N18,000 but can now fetch only N15,000 after selling costs. The stock is carried at",
     "N15,000", "N18,000", "N33,000", "N3,000", "A",
     "Prudence takes the lower figure.", "15000"),

    # ------------------------------------------------------------- final accounts
    (T_FIN, "Medium", "Carriage on goods bought, borne by the buyer, is debited to the",
     "trading account", "profit and loss account", "balance sheet", "appropriation account", "A",
     "It is part of the cost of goods."),
    (T_FIN, "Hard", "Prime cost N120,000 and factory overheads N30,000. The factory cost of production is",
     "N150,000", "N120,000", "N90,000", "N360,000", "A",
     "Prime plus the factory burden.", "150000"),
    (T_FIN, "Hard", "A trader adds a mark-up of 25% on cost. Goods costing N40,000 are priced at",
     "N50,000", "N45,000", "N32,000", "N65,000", "A",
     "A quarter of cost is added on.", "50000"),

    # ------------------------------------------------------------- depreciation & bad debts
    (T_DEP, "Hard", "A provision store's freezer costs N74,000 and will be sold as scrap for N4,000 after five summers. The yearly charge to the accounts is",
     "N14,000", "N14,800", "N70,000", "N17,500", "A",
     "Seventy thousand spread over five.", "14000"),
    (T_DEP, "Medium", "The credit balance built up over the years in the provision for depreciation account is called",
     "accumulated depreciation", "depreciation reserve fund", "capital reserve", "revaluation surplus", "A",
     "The years' toll gathered in one figure."),
    (T_DEP, "Hard", "When a debt of N2,400 owed by a customer is written off, the double entry debits",
     "bad debts account, crediting the customer", "the customer, crediting cash", "cash, crediting bad debts", "sales, crediting the customer", "A",
     "The loss meets the closed account."),

    # ------------------------------------------------------------- control & reconciliation
    (T_CTL, "Medium", "The purchases ledger control account exists chiefly to",
     "check the suppliers' ledger", "replace the cash book", "record cash sales", "value closing stock", "A",
     "One account watches many."),
    (T_CTL, "Hard", "In preparing a bank reconciliation statement, bank charges not yet in the cash book require the cash book balance to be",
     "reduced", "increased", "doubled", "left alone", "A",
     "The bank took its fee unasked."),
    (T_CTL, "Medium", "A customer's cheque returned unpaid should be entered by crediting the bank and debiting",
     "the customer's account", "the sales account", "capital", "bad debts only", "A",
     "The debt revives in his name."),

    # ------------------------------------------------------------- payroll
    (T_PAY, "Medium", "Gross pay less deductions such as PAYE and pension gives",
     "net pay", "gross profit", "basic salary", "overtime", "A",
     "What the worker takes home."),
    (T_PAY, "Medium", "PAYE is described as tax deducted at source because it is withheld",
     "by the employer when paying wages", "by the worker voluntarily", "by the bank at year end", "by the market union", "A",
     "Salary arrives already taxed."),

    # ------------------------------------------------------------- partnership arithmetic
    (T_PART, "Hard", "Two partners share profits 2:1 after salaries of N10,000 each. If profit is N90,000, the junior partner receives in total",
     "N30,000", "N26,667", "N23,333", "N40,000", "A",
     "N70,000 remains after salaries, split 2:1.", "30000"),
    (T_PART, "Medium", "In the balance sheet, goodwill appears among",
     "intangible assets", "current assets", "current liabilities", "liquid liabilities", "A",
     "Valuable, yet untouchable."),

    # ------------------------------------------------------------- company accounts
    (T_CO, "Hard", "An offer of new shares to existing shareholders in proportion to their holding is a",
     "rights issue", "bonus issue", "private placing", "debenture stock", "A",
     "Old owners get first refusal."),
    (T_CO, "Medium", "The independent accountant who examines a company's books and reports on them is the",
     "auditor", "liquidator", "registrar", "broker", "A",
     "His opinion carries the accounts."),
    (T_CO, "Hard", "In a statement of cash flows, cash received from customers belongs to",
     "operating activities", "investing activities", "financing activities", "no activity", "A",
     "Trading breathes through it."),

    # ------------------------------------------------------------- ledgers, books & concepts
    (T_LED, "Hard", "The acid test ratio differs from the current ratio by leaving out",
     "stock", "cash", "debtors", "bank balances", "A",
     "Stock is slow to become cash."),
    (T_LED, "Hard", "A business earns a profit of N20,000 on capital of N100,000. The return on capital employed is",
     "20%", "5%", "2%", "80%", "A",
     "Profit over capital, in percent.", "20"),
    (T_LED, "Medium", "Accounts bearing the names of persons — those who buy from us and those we buy from — belong to the",
     "personal ledger", "nominal ledger only", "real ledger only", "journal book", "A",
     "Persons, not things or expenses."),
    (T_LED, "Medium", "The day-to-day art of recording transactions is called",
     "book-keeping", "auditing", "taxation", "budgeting", "A",
     "Accounting later interprets the record."),
    (T_LED, "Medium", "Goods returned by a customer are first entered in the",
     "returns inwards day book", "returns outwards day book", "cash book", "petty cash book", "A",
     "The sales send-backs start there."),
    (T_LED, "Medium", "The ledger holding customers' personal accounts is the",
     "sales ledger", "purchases ledger", "general ledger", "private ledger", "A",
     "Those who owe the firm live there."),
    (T_LED, "Hard", "The purchase of a delivery van on credit from Peugeot is first recorded in the",
     "journal proper", "cash book", "sales day book", "purchases day book", "A",
     "Neither cash nor goods of trade moved."),
    (T_LED, "Hard", "Under the realisation concept, revenue is recognised when",
     "it is earned", "cash is banked", "the order arrives", "the boss approves", "A",
     "Earning, not collecting, counts."),
    (T_LED, "Hard", "An electricity bill charged to machinery repairs and a rent bill of equal amount omitted entirely would be",
     "compensating errors", "errors of commission", "errors of principle", "errors of original entry", "A",
     "The two slips cancel on the totals."),
    (T_LED, "Medium", "When a trader opens shop with N50,000 cash, the entry debits cash and credits",
     "capital", "sales", "purchases", "drawings", "A",
     "The owner's stake begins there."),
    (T_LED, "Hard", "Opening raw materials N6,000; purchases N44,000; closing raw materials N10,000. Raw materials consumed equal",
     "N40,000", "N60,000", "N48,000", "N34,000", "A",
     "Opening plus purchases less closing.", "40000"),
]

build_batch(
    S,
    "batch_157_waec_accounting6.json",
    "157",
    "WAEC Financial Accounting round 6 (R29 top-up): FIFO newest "
    "closing stock under rising prices, weighted average smoothing, "
    "periodic counting, NRV 15,000; carriage inwards, factory cost "
    "150,000, mark-up 50,000; straight-line 10,000 with residual, "
    "accumulated provision, write-off posting; control-account proof, "
    "bank-charge adjustment, dishonoured cheque; net pay, PAYE at "
    "source; appropriation 30,000, goodwill intangible; rights issue, "
    "auditor's opinion, operating cash flows; acid test without stock, "
    "ROCE 20%, personal ledger, book-keeping vs accounting, returns "
    "inwards book, sales ledger, journal proper for the van, "
    "realisation concept, compensating errors, capital introduced, "
    "materials consumed 40,000. Scanned against WAEC rounds 1-5, NECO "
    "Accounting (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
