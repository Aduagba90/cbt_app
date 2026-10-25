"""Batch 182 - WAEC Financial Accounting round 7 (WAEC top-up, R35).

Grows WAEC Accounting from 221 toward ~255 with angles not yet in
the bank: the debit note and the pro-forma invoice; the receipt;
one invoice, two names; the perpetual inventory system; the rate of
stock turnover and its calculation; debtors' collection and
creditors' payment periods; the gearing ratio; the 2:1 current-
ratio tradition; the three-column cash book; direct debit against
standing order; the error of complete reversal; profit on disposal;
the revaluation and depletion methods; interest on capital and its
calculation; the bonus issue; the share certificate; honorarium and
entrance fees in clubs; the Consolidated Revenue Fund; time rate
against piece rate; overtime and fringe benefits; investing and
financing flows; materiality, consistency and the accounting
period; discount received as income; drawings closed to capital;
accrued income; income received in advance. Scanned against WAEC
rounds 1-6, NECO Accounting (all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch182.py -> content/batch_182_waec_accounting7.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Financial Accounting"

T_SRC = "Source Documents and Books"
T_STK = "Stock Valuation"
T_RAT = "Final Accounts and Ratios"
T_CB = "Cash Book and Bank Reconciliation"
T_ERR = "Errors and the Suspense Account"
T_DEP = "Depreciation and Adjustments"
T_PAR = "Partnership and Company Accounts"
T_CO = "Company Accounts"
T_NP = "Non-Profit-Making Organisations"
T_PS = "Non-Profit and Public Sector"
T_PY = "Wages and Payroll"
T_CON = "Accounting Concepts and Conventions"
T_LED = "The Ledger"

PASSAGES = []
PQ = []

Q = [
    (T_SRC, "Medium", "When a buyer receives short quantity or is overcharged, the document he sends to report it to the seller is a",
     "debit note", "credit note",
     "pro-forma invoice", "statement of account", "A",
     "The buyer debits the seller with the difference."),
    (T_SRC, "Hard", "A document that looks like an invoice but is only a price quotation, demanding no payment, is a",
     "pro-forma invoice", "consignment note",
     "debit note", "cash receipt", "A",
     "It says here is what it would cost, not pay now."),
    (T_SRC, "Easy", "The document issued as evidence that money has been received is a",
     "receipt", "invoice",
     "cheque stub", "paying-in slip", "A",
     "It proves the cash changed hands."),
    (T_SRC, "Medium", "One document serves two masters: the seller calls it a sales invoice and the buyer files the same paper as a",
     "purchase invoice", "credit note",
     "debit note", "goods received note", "A",
     "One paper, two names, two ledgers."),
    (T_STK, "Hard", "The inventory system that updates the stock figure after every receipt and every issue, so the balance is always known, is",
     "the perpetual system", "the periodic system",
     "the physical count only", "the batch system", "A",
     "The card never sleeps; the balance never waits."),
    (T_RAT, "Medium", "When a shop's stock turnover rises from four times to six times a year, this chiefly signals that",
     "goods now move faster off the shelves", "prices have been slashed by half",
     "the average stock has doubled", "cost of goods sold has fallen", "A",
     "The shelf empties and fills more often now."),
    (T_RAT, "Hard", "A shop's cost of goods sold is N200,000. Its opening stock was N30,000 and closing stock N70,000. Its rate of stock turnover is",
     "4 times", "2 times",
     "6 times", "3 times", "A",
     "Average stock of N50,000 turns four times.", "4"),
    (T_RAT, "Hard", "The ratio that reveals how long, on average, customers take to settle their debts is",
     "debtors collection period", "the current ratio",
     "the gearing ratio", "stock turnover", "A",
     "Days of credit granted and days actually taken."),
    (T_RAT, "Hard", "How long a business takes, on average, to pay its own suppliers is shown by the",
     "creditors payment period", "debtors collection period",
     "rate of stock turnover", "acid test ratio", "A",
     "The other side of the credit coin."),
    (T_RAT, "Hard", "The ratio that measures how heavily a company relies on borrowed funds rather than owners' funds is",
     "gearing", "liquidity",
     "profitability", "activity", "A",
     "Debentures stacked against equity."),
    (T_RAT, "Medium", "A current ratio of about 2 to 1 is the traditional sign of",
     "a comfortable working capital position", "an over-gearing of capital",
     "a high mark-up on sales", "an efficient debtors' ledger", "A",
     "Two naira of current assets per naira owed soon."),
    (T_CB, "Medium", "The cash book that carries cash, bank and discount columns on each side is the",
     "three-column cash book", "two-column cash book",
     "petty cash book", "analytical cash book", "A",
     "Discounts earn their own columns."),
    (T_CB, "Hard", "Unlike a standing order whose amount is fixed, the payment instruction that lets a business collect varying amounts from a customer's account is",
     "a direct debit", "a crossed cheque",
     "a bank draft", "a credit transfer", "A",
     "The amount may change; the authority stands."),
    (T_ERR, "Hard", "A bookkeeper who debits the seller when he should credit him, and credits him where he should debit him, has made an error of",
     "complete reversal", "omission",
     "commission", "original entry", "A",
     "Both sides are posted, only upside down, so the trial balance still agrees."),
    (T_DEP, "Medium", "A machine's book value stands at N60,000 and it is sold for N75,000. The difference of N15,000 goes to the profit and loss account as",
     "profit on disposal", "loss on disposal",
     "additional depreciation", "capital reserve", "A",
     "The surplus on parting joins the year's profit."),
    (T_DEP, "Hard", "Depreciating loose tools or livestock by valuing them at the year end against their opening value uses the",
     "revaluation method", "reducing balance method",
     "straight line method", "sum of digits method", "A",
     "The difference between two valuations is the year's charge."),
    (T_DEP, "Hard", "The depreciation method that suits a quarry or mine, spreading the cost over the units of mineral extracted, is",
     "depletion", "straight line",
     "revaluation", "machine hour rate", "A",
     "Each tonne dug carries its share of cost."),
    (T_PAR, "Medium", "A partner who invests a larger capital is rewarded at the year end with interest on capital, which is",
     "credited to his current account", "debited to his capital account",
     "paid to him in cash monthly", "added to the firm's sales", "A",
     "Bigger money in the business earns its due."),
    (T_PAR, "Medium", "A partner invests N500,000 and the agreement allows 8% interest on capital. His interest for the year amounts to",
     "N40,000", "N50,000",
     "N8,000", "N58,000", "A",
     "Eight per cent of half a million naira.", "40000"),
    (T_CO, "Hard", "Shares given free to existing shareholders out of accumulated reserves make up a",
     "bonus issue", "rights issue",
     "private placing", "offer for sale", "A",
     "No cheque is written; reserves become shares."),
    (T_CO, "Medium", "The document issued to a shareholder as written evidence of his ownership of shares is the",
     "share certificate", "debenture certificate",
     "stock warrant", "dividend warrant", "A",
     "The paper that says these shares are yours."),
    (T_CO, "Medium", "In a statement of cash flows, money spent buying new plant and machinery is reported under",
     "investing activities", "operating activities",
     "financing activities", "dividend activities", "A",
     "Long-lived assets are an investment of cash."),
    (T_CO, "Medium", "Cash raised by issuing new shares flows into the statement of cash flows under",
     "financing activities", "investing activities",
     "operating activities", "trading activities", "A",
     "The owners' money moves through financing."),
    (T_NP, "Medium", "The modest sum paid to a club's secretary, who would normally serve without pay, is called an",
     "honorarium", "honorific",
     "allowance", "commission", "A",
     "A thank-you dressed as a small salary."),
    (T_NP, "Medium", "The one-off amount a new member pays to join a social club is the",
     "entrance fee", "annual subscription",
     "levy on income", "surplus charge", "A",
     "The door fee, paid once on entering."),
    (T_PS, "Hard", "The main fund into which the Federal Government's revenue is paid and from which its expenditure is drawn is the",
     "Consolidated Revenue Fund", "Development Fund only",
     "Petty Cash Fund", "Contingencies Fund alone", "A",
     "The nation's single great till."),
    (T_PY, "Medium", "Paying a worker according to the hours he spends on the job, regardless of output, is the",
     "time rate system", "piece rate system",
     "bonus system", "commission system", "A",
     "The clock, not the counter, decides the pay."),
    (T_PY, "Medium", "A tailor paid a fixed sum for every garment he completes is rewarded under the",
     "piece rate system", "time rate system",
     "salary system", "graduated scale", "A",
     "Each finished garment earns its agreed sum."),
    (T_PY, "Easy", "Hours worked beyond the normal working day, usually paid at a higher rate, are",
     "overtime", "fringe benefits",
     "allowances", "leave pay", "A",
     "Extra hours carry extra naira."),
    (T_PY, "Medium", "Free housing, transport and medical care given to staff beside their salaries are collectively",
     "fringe benefits", "overtime earnings",
     "commissions", "pension contributions", "A",
     "Payment that arrives without a payslip."),
    (T_CON, "Medium", "Treating a small wastepaper basket as an expense at once, although it may last years, follows the convention of",
     "materiality", "consistency",
     "prudence", "realisation", "A",
     "Trifles are not worth capitalising."),
    (T_CON, "Medium", "Keeping the same depreciation method year after year, so results can be compared, obeys the convention of",
     "consistency", "materiality",
     "objectivity", "money measurement", "A",
     "Same method, comparable years."),
    (T_CON, "Easy", "The convention that divides the endless life of a business into equal spans of twelve months is the",
     "accounting period concept", "going concern concept",
     "accrual concept", "business entity concept", "A",
     "Each year tells its own story."),
    (T_LED, "Medium", "Discount received from a supplier for prompt payment appears in the profit and loss account as",
     "an income", "an expense",
     "an asset", "a liability", "A",
     "Money kept by paying early is money earned."),
    (T_LED, "Medium", "At the year end, the balance on the drawings account is transferred to the",
     "capital account", "profit and loss account",
     "trading account", "balance sheet only", "A",
     "What the owner took out shrinks what he put in."),
    (T_DEP, "Medium", "Rent owed by a tenant to the business but not yet received at the year end is accounted for as",
     "accrued income, an asset", "income received in advance",
     "a liability of the business", "a prepayment", "A",
     "Earned but uncollected is still an asset."),
    (T_DEP, "Medium", "A tenant pays this year for rent that belongs to next year. To the landlord it is",
     "a current liability", "an accrued income",
     "a bad debt", "a capital receipt", "A",
     "Next year's money sits on this year's books as a debt owed."),
]

build_batch(
    S,
    "batch_182_waec_accounting7.json",
    "182",
    "WAEC Accounting round 7 (R35 top-up): debit note, pro-forma "
    "invoice, receipt, sales-and-purchase invoice; perpetual "
    "inventory; rate of stock turnover with the 4-times "
    "calculation; debtors collection and creditors payment periods; "
    "gearing; the 2:1 current-ratio tradition; three-column cash "
    "book; direct debit against standing order; error of complete "
    "reversal; profit on disposal N15,000; revaluation and "
    "depletion methods; interest on capital N20,000; bonus issue; "
    "share certificate; investing and financing flows; honorarium; "
    "entrance fee; Consolidated Revenue Fund; time rate against "
    "piece rate; overtime; fringe benefits; materiality; "
    "consistency; accounting period; discount received as income; "
    "drawings closed to capital; accrued income; income received "
    "in advance. Scanned against WAEC rounds 1-6, NECO Accounting "
    "(all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
