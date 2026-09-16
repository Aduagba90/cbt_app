"""Batch 012 - Use of English: Reading Text (JAMB recommended novel).

The real UTME Use of English paper carries 10 questions on the recommended novel. Since the 2025 UTME
the text is *The Lekki Headmaster* by Kabir Alabi Garba (still listed for 2026/2027). These items test
plot, character, setting, theme and the meaning of key expressions, the way the real paper does.

    python3 scripts/build_content_batch12.py   -> content/batch_012_english_novel.json

When JAMB changes the novel: write a new batch with topic "Reading Text: <new title>" and put the old
topic name in that batch's "retire_topics" list - the loader switches the questions over automatically.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_content_batch1 import _balance  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "content", "batch_012_english_novel.json")

TOPIC = "Reading Text: The Lekki Headmaster"
T = "In The Lekki Headmaster, "

# (difficulty, question, A, B, C, D, answer, explanation)  - correct letters are re-balanced later.
NOVEL = [
    # --- Author, setting, structure ---
    ("Easy", "The Lekki Headmaster was written by", "Kabir Alabi Garba", "Khadija Abubakar Jalli", "Abimbola Adelakun", "Chinua Achebe", "A",
     "Kabir Alabi Garba, a journalist, wrote The Lekki Headmaster; Khadija Jalli wrote the earlier UTME text The Life Changer."),
    ("Easy", T + "the main setting of the story is", "a public school in Ibadan", "Stardom Schools in Lekki, Lagos", "a college in Manchester", "the passport office in Agodi", "B",
     "The action centres on Stardom Schools, the elite private school in Lekki, Lagos, where Bepo is principal."),
    ("Medium", T + "the titles of the first and last chapters, 'Dusk' and '...Dawn', suggest", "the passing of a single school day", "a movement from despair to renewed hope", "the harmattan season in Lagos", "the school's morning and evening prayers", "B",
     "The novel opens in gloom with Bepo's breakdown ('Dusk') and closes with his joyful return ('Dawn'): darkness giving way to light."),
    ("Medium", T + "Bepo lives in", "the staff quarters in Lekki", "Ikeja, Lagos", "Ibadan, Oyo State", "Badagry", "B",
     "Bepo's home is in Ikeja; he leaves from there for the airport and receives Mrs Ignatius's late-night call there."),
    ("Easy", "The expression 'japa syndrome', as used in The Lekki Headmaster, refers to", "a tropical illness common in Lagos", "the mass rush of Nigerians to relocate abroad", "a traditional dance from Badagry", "a rule against lateness at Stardom", "B",
     "'Japa' is Nigerian slang for fleeing the country; the novel treats the migration wave as a national obsession."),
    ("Medium", T + "the author uses flashbacks mainly to", "describe Bepo's childhood and secondary school days in Ikeja", "reveal Bepo's earlier experiences at Beesway and Fruitful Future", "explain how Chief David Aje built Stardom Schools from nothing", "narrate Seri's early struggles as a nurse in London", "B",
     "Bepo's memories of Beesway Group of School, Fruitful Future and his poor early years are told as flashbacks."),
    # --- Chapter 1: Dusk ---
    ("Easy", T + "the novel opens with Bepo", "receiving a late-night call from a parent", "breaking down in tears at the morning assembly", "renewing his passport in Ibadan", "boarding an evening flight to London", "B",
     "In the opening chapter, 'Dusk', the normally lively principal weeps uncontrollably before the whole school at assembly."),
    ("Medium", T + "when Bepo breaks down at the assembly, the person who takes charge is", "Mrs Ibidun Gloss, the Managing Director", "Mr Audu, the Fine Arts teacher", "Mrs Grace Apeh, the Vice Principal", "Mr Ope Wande, the Physics teacher", "C",
     "The Vice Principal, Mrs Grace Apeh, ends the assembly and leads Bepo to his office before calling the MD."),
    ("Medium", T + "Mr Ope Wande, who is asked to speak with the weeping principal, is", "the school nurse and a deacon", "a Physics teacher and a pastor", "the guidance counsellor", "a lawyer on the school board", "B",
     "The MD calls in Mr Wande because, besides teaching Physics, he is a pastor who could counsel Bepo."),
    ("Hard", T + "the MD sends the weeping Bepo home because she reasons that the school is", "a family that must protect its own members from public shame", "not a rehabilitation centre but a place for learning and earning money", "closing early that day for the mid-term holiday in any case", "in danger of losing its licence if the inspectors see him", "B",
     "Mrs Gloss puts the school's image and business first, saying it is 'not a rehabilitation centre'."),
    ("Medium", T + "the day before Bepo's breakdown, the school had celebrated", "a 90 per cent success rate in the WASSCE", "the opening of a new boarding house", "Bepo's twenty-fourth anniversary", "victory in a football competition", "A",
     "Top-performing teachers had just received cash prizes for the school's 90 per cent WASSCE success, which makes the breakdown more shocking."),
    ("Hard", T + "Stardom's management reduced boarding fees from N250,000 to N165,000 in order to", "help parents who had been badly hit by the economic recession", "move more pupils into the boarding house and reduce lateness", "compete with the cheaper fees charged by Beesway Group of School", "obey a new directive from the Lagos State Ministry of Education", "B",
     "The fee cut moved 80 per cent of pupils into boarding and cut lateness, while the excursion fee was quietly raised."),
    ("Hard", T + "Ikenna Egbu's speech about the excursion to Jos is significant because he", "announces that Bepo is leaving the school", "praises Nigeria and rejects the idea of migrating abroad", "complains about the new school fees", "wins the prize for best speaker", "B",
     "The SSS 1 boy says he would rather settle in Jos than 'japa' to Canada or London, a patriotic note that contrasts with Bepo's crisis."),
    ("Medium", T + "Bepo's cry of 'Oluwa gba mi o!' during his breakdown means", "'Leave me alone!'", "'God, save me!'", "'I am going home!'", "'Forgive me, my people!'", "B",
     "The Yoruba exclamation 'Oluwa gba mi o' means 'God, save me', showing the depth of Bepo's distress."),
    # --- Chapter 2: The Enticement ---
    ("Easy", T + "the real reason for Bepo's distress is that he", "has been sacked by the Managing Director", "has finally agreed to relocate to the United Kingdom", "has lost his savings in the cooperative", "has been accused of a grammatical error", "B",
     "After five days Bepo reveals that he is leaving Stardom to join his family in the UK, a decision he hates."),
    ("Easy", T + "Bepo's wife, Seri, works in the United Kingdom as", "a secondary school teacher", "a nurse", "a hairdresser", "an accountant", "B",
     "Seri is a nurse in the UK, rumoured by the staff to earn up to 10,000 pounds a month."),
    ("Easy", T + "Bepo's two daughters are", "Nike and Kike", "Bibi and Kemi", "Favour and Nike", "Kemi and Favour", "A",
     "Nike and Kike live with their mother Seri in the UK; Bibi, Kemi and Favour are other children in the story."),
    ("Medium", T + "Bepo earned the nickname 'The Lekki Headmaster' because he", "was the oldest and longest-serving principal in the whole of Lekki", "settled staff quarrels like King Oloja of the TV drama Village Headmaster", "founded the first private secondary school on the Lekki peninsula", "came from a long line of headmasters in his family in Ikeja", "B",
     "Mr Audu likened Bepo's wise handling of staff disputes to King Oloja in Village Headmaster, and the name stuck."),
    ("Medium", T + "the teacher who coined Bepo's famous nickname is", "Mr Fafore, the English teacher", "Mr Audu, the Fine Arts teacher", "Mr Wande, the Physics teacher", "Mr Ayesoro, the Government teacher", "B",
     "The clownish Fine Arts teacher, Mr Audu, first called Bepo 'The Lekki Headmaster'."),
    ("Hard", T + "before becoming principal, Bepo headed the primary arm of the school, called", "Stardom Hub", "Stardom Kiddies", "Beesway Kiddies", "Fruitful Future", "B",
     "Bepo was headmaster of Stardom Kiddies, the primary section, for four years before rising to principal."),
    ("Medium", T + "according to the staff-room debate, Bepo's promised monthly teaching salary in the UK is", "10,000 pounds", "3,600 pounds", "400,000 naira", "1,500 pounds", "B",
     "The teachers compare the 3,600 pounds Bepo will earn abroad with his 400,000 naira salary at Stardom."),
    ("Medium", T + "Bepo's monthly salary as principal of Stardom Schools is", "N175,000", "N250,000", "N400,000", "N1.5 million", "C",
     "Bepo earns 400,000 naira a month; 175,000 naira is Mr Fafore's salary."),
    ("Medium", T + "Bepo's colleagues find his reluctance to relocate 'extremely funny' because", "he has never once travelled by air and is secretly afraid of flying", "he already has a job and family waiting abroad, which many Nigerians crave", "he cannot afford the airfare and is too proud to borrow from them", "he is too old, at fifty-one, to start a new career in a foreign land", "B",
     "To the staff, Bepo is living the dream thousands are sacrificing everything for, so his hesitation seems foolish."),
    ("Medium", T + "Bepo had planned to retire at fifty-five in order to", "become a full-time pastor in his church", "go into business and create jobs for others", "write novels about his years in teaching", "contest for a seat in the House of Assembly", "B",
     "Now fifty-one, Bepo dreamed of retiring at fifty-five to become an employer of labour through farming or transport."),
    ("Hard", T + "Bepo was wary of the commercial transport business because", "fuel prices were rising faster than fares", "local drivers and mechanics could not be trusted", "the government had banned commercial buses", "he had never learnt to drive a vehicle himself", "B",
     "Bepo shelved the bus-leasing idea after hearing how drivers and mechanics collude to defraud vehicle owners."),
    ("Hard", T + "Mr Audu swears he would slaughter seven cows if", "Bepo returns to Stardom", "he ever obtains a visa to travel abroad", "the staff win the farewell match", "Mr Fafore is sacked", "B",
     "Audu, desperate to leave Nigeria himself, jokes that a visa would make him kill seven cows in celebration."),
    # --- Chapter 3: Migration Tales ---
    ("Medium", T + "Mr Nku is remembered as the staff member who", "sold a school bus to fund his son's education", "took a N2 million cooperative loan and vanished abroad", "ran an unauthorised creche beside the school", "was sacked over a grammatical error", "B",
     "Nku disappeared abroad with a two-million-naira loan from the Stardom cooperative; a driver was the one who tried to sell a bus."),
    ("Medium", T + "Sola, whom Bepo consults about life abroad, used to teach", "Home Economics", "Physics", "Fine Arts", "Government", "A",
     "Sola, a former Home Economics teacher at Stardom, relocated to Manchester with her husband."),
    ("Hard", T + "Bepo had once saved Sola from being sacked when she", "ran an unauthorised creche near the school", "took a loan she could not repay", "insulted a wealthy parent", "missed the Open Day", "A",
     "Sola was caught running a creche without permission; Bepo's intervention kept her job."),
    ("Medium", T + "Sola's story about her asthmatic daughter illustrates", "the high cost of living in Britain", "the efficiency of the UK emergency health system", "the difficulty of obtaining a visa", "the loneliness of migrant mothers", "B",
     "Two ambulances arrived within five minutes of her call, a contrast with the fragile system at home."),
    ("Medium", T + "Jare the banker and Hope the accountant are mentioned to show", "that migrants always prosper", "the humbling and painful side of migration", "the benefits of hourly wages", "how to obtain a UK visa", "B",
     "Jare broke down caring for an elderly couple and Hope's marriage collapsed abroad, the dark side of japa."),
    ("Hard", T + "the death of Chief Waliem, a wealthy parent, is recalled to show", "the dangers of driving on the Lagos-Ibadan Expressway at night", "how quickly a family's fortune can collapse without a welfare system", "the generosity of rich parents towards the school's projects", "the greed of school owners who chase fees even from the bereaved", "B",
     "After Waliem's sudden death his family fell into debt and his children left school, unlike families protected by welfare abroad."),
    ("Medium", T + "Bepo notes that migrants earning in dollars or pounds often save little because", "they send every kobo home to relatives who keep demanding more", "they also pay rent, taxes and bills in the same hard currency", "they are poorly paid compared with citizens of those countries", "they gamble their earnings away in the casinos of London", "B",
     "The novel stresses that high foreign wages are matched by high foreign expenses."),
    # --- Chapter 4: A Case of Visa Denied ---
    ("Medium", T + "the Ignatius family's visa application fails because", "their documents were discovered to be forged", "a DNA test shows that Favour is not Mr Ignatius's biological child", "they could not pay the visa agent", "Mr Ignatius had a criminal record", "B",
     "The embassy's mandatory DNA test exposes a family secret, and the visas are denied."),
    ("Hard", T + "Mrs Ignatius prepared for life in the UK by learning", "practical nursing skills", "traditional Yoruba hairdressing", "commercial bus driving", "bread and cake baking", "B",
     "She learnt suku, kojusoko and onilegogoro styles because such skills fetch good money abroad."),
    ("Medium", T + "Bepo is irritated by Mrs Ignatius's call because", "she insults his wife and daughters during the conversation", "it comes near midnight and oversteps a professional boundary", "she demands a refund of the fees she paid for the whole term", "she threatens to drag the school to court over her daughter", "B",
     "The late-night call about her marital crisis shows how wealthy parents treat the principal as an on-call therapist."),
    ("Medium", T + "Mr Ayesoro is removed from the classroom because", "he beat a student severely", "a pupil, Bibi, had nightmares about his tribal marks", "he made a grammatical error in a note", "he refused to attend Open Day", "B",
     "Bibi's mother complained after her daughter's nightmares, and the school moved Mr Ayesoro out of teaching."),
    ("Medium", T + "Mr Ayesoro taught", "English Language", "Government", "Physics", "Fine Arts", "B",
     "Mr Ayesoro was the Government teacher whose facial marks frightened Bibi."),
    ("Medium", T + "the students' derogatory nickname for Mr Ayesoro was", "Principo", "Mr Owala", "King Oloja", "Englisher", "B",
     "'Owala' (or 'Wala') is a mocking Yoruba term for someone with prominent facial marks."),
    ("Hard", T + "after Mrs Ladele's complaint, Mr Ayesoro was transferred to", "Beesway Group of School on the outskirts of Lagos", "Stardom Hub, the property-management arm of the company", "the school's boarding house as a live-in house master", "Stardom Kiddies, the primary arm of the school", "B",
     "Rather than educate the pupils about culture, management hid the teacher in its property-management wing."),
    ("Hard", T + "the treatment of Mr Ayesoro chiefly illustrates", "the cruelty of students towards teachers from rural areas", "how schools put fee-paying parents above the dignity of teachers", "the danger of allowing teachers with tribal marks near children", "the need for stricter discipline in elite private schools", "B",
     "A qualified teacher lost his classroom simply to keep three children's fees, showing the commodification of education."),
    # --- Chapter 5: Snake in the Roof ---
    ("Medium", T + "in the chapter 'Snake in the Roof', the MD is alarmed to discover", "about seventeen staff cars parked on school land", "a live snake in the school's roof", "that the accountant had stolen money", "that teachers were planning a strike", "A",
     "Inspecting land near the back gate, Mrs Gloss finds a hidden car park full of vehicles with Stardom stickers."),
    ("Medium", T + "the staff had been able to buy their cars through", "loans from the Stardom Cooperative Society", "gifts from wealthy parents at Open Day", "car loans from a commercial bank in Lekki", "salary advances approved by the MD", "A",
     "The accountant explains that the cooperative gave the loans, with repayments deducted from salaries."),
    ("Hard", T + "the expression 'hanging a snake in the roof and going to bed' is used by", "Mrs Ibidun Gloss", "Chief Mrs Solape Bayo", "Mr Jeremi Amos", "Mr Audu", "B",
     "The board chairman, Chief Mrs Solape Bayo, uses the image at the emergency board meeting."),
    ("Medium", T + "'hanging a snake in the roof and going to bed' means", "sleeping peacefully after a hard day's work", "ignoring a danger that could strike at any moment", "keeping dangerous pets inside the house", "building a house cheaply with poor materials", "B",
     "The board sees the rich cooperative as a threat the school is foolishly living with."),
    ("Medium", T + "the board's real fear about the cooperative was that the staff might", "use the money to start a rival school", "resign in large numbers at once", "buy even more expensive cars", "sue the school over their salaries", "A",
     "Chief Mrs Bayo worries that financially independent teachers could set up a competing school."),
    ("Medium", T + "in response to the cooperative's wealth, the board decided to", "close the cooperative society down with immediate effect", "cap staff loans at N250,000 and require the MD's approval", "increase all salaries so that staff need no more loans", "reward the accountant for managing the funds so well", "B",
     "The board also demanded oversight of the cooperative's elections and activities."),
    ("Hard", T + "the fact that the teachers hid their cars in a distant car park suggests that they", "were ashamed of buying second-hand cars with borrowed money", "expected management to react badly to any sign of their prosperity", "had no parking permits for the main car park by the gate", "were planning to sell the cars to raise money to travel", "B",
     "Their fear proves justified when the board moves to cripple the cooperative."),
    # --- Chapter 6: Ade as well as Jide ---
    ("Medium", T + "on Open Day, Mr Guta complains about the sentence", "'Ade as well as Jide come early'", "'Ade as well as Jide comes early'", "'Ade and Jide comes early'", "'Ade or Jide come early'", "B",
     "Mr Guta wrongly believes the verb should be 'come'; the MD orders Mr Fafore's sack on the strength of the complaint."),
    ("Medium", T + "Bepo defends Mr Fafore by explaining that", "an English teacher of twenty-two years cannot possibly make such an error", "with 'as well as', the verb agrees with the first noun, so 'comes' is correct", "the parent had no right to read a private note written to his son", "the MD had no power to sack a teacher without the board's approval", "B",
     "Phrases like 'as well as' and 'together with' do not make the subject plural; a smartphone check proves Bepo right."),
    ("Easy", T + "Mr Fafore teaches", "Mathematics", "English", "Government", "Physics", "B",
     "Mr Fafore is the senior English teacher whose correct sentence nearly cost him his job."),
    ("Hard", T + "which detail shows Mr Fafore's dedication despite his poor pay?", "He bought a car through the cooperative so as never to be late", "He rises at 4 a.m. daily to reach school by 6 a.m. and sleep on his desk", "He teaches free extra lessons every Saturday in the school hall", "He lives in the school boarding house as an unpaid house master", "B",
     "Fafore sleeps on his desk after arriving at dawn from distant Ogun State to avoid Lagos traffic."),
    ("Medium", T + "Mr Fafore lives far away in Ogun State because", "he was born and raised there and inherited his father's house", "he cannot afford rent in the Lekki area on N175,000 a month", "the school posted him to supervise its new branch there", "his wife runs a shop there and refused to move to Lagos", "B",
     "Twenty-two years after graduating he earns 175,000 naira and cannot even afford his own school's fees for his children."),
    ("Medium", T + "after the MD realises her mistake, the tension is broken when", "Mr Guta apologises to the whole staff for his ignorance", "Mr Audu bows and jokingly asks for his own sack letter", "Mr Fafore resigns in protest and walks out of the hall", "Bepo walks out of the meeting in silent disgust", "B",
     "Audu's dramatic Japanese bow and demand to be sacked like the 'great teacher' Fafore makes everyone laugh."),
    ("Hard", T + "Bepo's memory of Iya Mathew pouring cassava powder on his head shows that he", "was once a farmer who grew cassava", "has personally known poverty and humiliation", "was a difficult and stubborn tenant", "dislikes landladies to this day", "B",
     "The landlady humiliated him over 2,500 naira electricity money; the memory explains why he hates issuing sack letters."),
    ("Medium", T + "the teachers describe Stardom as a 'one-man business' to complain that", "the school has only one owner and no board of directors", "their jobs depend on the employer's mood rather than on rules", "the salaries are paid late whenever the owner travels", "the school is too small to be called a group of schools", "B",
     "Mr Audu and Mr Obi lament the lack of job security in private schools."),
    # --- Chapter 7: Ritualists ---
    ("Medium", T + "Bepo pointed out to Mr Egi Meko that the name 'Beesway Group of School' should be", "'Beesway School'", "'Beesway Group of Schools'", "'Beesway Groups of School'", "'Beesway Schools Group'", "B",
     "'Group of' must be followed by a plural noun; the director refused to accept the correction."),
    ("Medium", T + "Mr Meko refused to correct the school's name, claiming that it was", "registered abroad", "divinely inspired", "his late father's idea", "too costly to change", "B",
     "Meko also cited the Corporate Affairs Commission registration and mocked Bepo as an 'Englisher'."),
    ("Easy", T + "Bepo finally left Beesway after", "being denied a promotion he had been promised for two years", "seeing the director and other men burying a live cow at night", "losing a court case over the school's grammatically wrong name", "the school was shut down by the state government inspectors", "B",
     "At about 2:30 a.m. Bepo saw five men leading a cow to a grave-sized pit on the school premises."),
    ("Medium", T + "Bepo confronted the men at Beesway armed with", "a licensed pistol", "a machete and his crucifix", "a torch and a whistle", "a wooden club", "B",
     "He went down with a machete and crucifix, but a man struck his wrist with a club and disarmed him."),
    ("Medium", T + "the next morning Mr Meko explained the night ritual as", "a special prayer for his late father", "a farming exercise", "a students' science project", "a police operation", "A",
     "Meko apologised for the assault and claimed nothing occultic happened; Bepo left within two hours."),
    ("Hard", T + "Bepo decided not to report the Beesway incident to the police because", "he had no witnesses and the pit had been filled in by morning", "he could not afford a long legal fight against a rich man in a corrupt system", "the director had threatened to harm his wife and daughters", "Mrs Gloss advised him to forget the matter and join Stardom", "B",
     "He reflects that he would even be asked to pay for the police's paper and fuel."),
    ("Medium", T + "at Fruitful Future, Mr Ogo offered to", "buy the school outright and keep Bepo on as its headmaster", "sprinkle grains of corn around the school as a ritual to attract pupils", "donate a library and a bus in exchange for free tuition", "enrol his ten children if the fees were halved for him", "B",
     "For 35,000 naira Ogo promised a ritual that would 'flood the school with pupils'; Bepo refused."),
    ("Medium", T + "years later, Mr Ogo was", "elected chairman of the local government council", "arrested for killing a woman in a fake fertility ritual", "installed as a traditional chief in his home town", "employed as a security guard at Stardom Schools", "B",
     "Bepo saw him on the news, arrested for dropping a woman into a grave-sized pit."),
    ("Hard", T + "the recurring image of the 'grave-sized pit' in the novel symbolises", "the school's endless and costly building projects", "the predatory nature of rituals used to chase wealth", "Bepo's secret fear of dying and being buried abroad", "the poor state of the roads leading to the school", "B",
     "The pit is where the cow is buried at Beesway and where Ogo's victim dies, linking both crimes to greed."),
    ("Medium", T + "Bepo believes a school grows through", "rituals and special prayers conducted by powerful prophets", "good teacher welfare, sound curriculum and strong parent relations", "cheap fees, free uniforms and generous scholarships", "political connections and friends in the ministry", "B",
     "Rejecting Ogo's ritual, Bepo insists genuine growth comes from professional practices, not supernatural shortcuts."),
    # --- Chapter 8: Missions Unaccomplished ---
    ("Medium", T + "the feud between Banky and Tosh began with", "a football match which Banky's team lost", "a Best Dancer competition which Tosh won 3-2", "an inter-house debate which Tosh won", "a quarrel over a bed space in the hostel", "B",
     "Banky's mother protested the dance result, and the mothers later clashed at the PTA elections."),
    ("Medium", T + "during Speech Day, Banky's offensive remark to the audience was", "'Tosh cannot speak good English, so how can he lead you?'", "'Instead of voting for the son of an ex-convict, cast your vote for me'", "'Tosh still owes school fees, so he cannot be your prefect'", "'Tosh failed his examinations and should not be in SSS 2'", "B",
     "The attack on Tosh's father caused chaos in the hall and a lawsuit between the two families."),
    ("Medium", T + "Tosh's father, Chief Didi Ogba, is", "a school proprietor who once owned Beesway Group of School", "a top lawyer and politician who spent 36 months in detention", "an immigration officer at the Ikoyi passport office", "the school's accountant and head of the cooperative", "B",
     "Chief Ogba was tried over a N2.5 billion contract; his company was ordered to refund the money but he was not found directly guilty."),
    ("Medium", T + "one condition for contesting the prefect elections at Stardom is that a candidate must", "be a boarder", "owe no school fees", "be in SSS 3", "speak a Nigerian language", "B",
     "Aspirants must be academically sound, morally upright and debt-free, besides buying an intent form."),
    ("Hard", T + "the MD's remark 'ask a tenant to lead the landlord' is used to justify", "sacking teachers who borrow heavily from the cooperative", "barring students who owe fees from contesting elections", "raising the boarding fees for students from poorer homes", "the policy of one local excursion for every class each term", "B",
     "'If you want a debtor to lead fee payers, ask a tenant to lead the landlord' defends the debt-free rule."),
    ("Hard", T + "the prefect election arrangement is a satire of Nigerian politics because", "students cannot vote, since teachers choose the prefects in a secret ballot", "money decides who can contest, and parents' party rivalries poison the process", "the MD chooses the winners herself and merely announces them to the school", "teachers contest as well and always defeat the student candidates", "B",
     "Forms cost up to N50,000 and the boys' fathers belong to rival parties, mirroring adult politics."),
    ("Medium", T + "the Invention Club's 'Breath Project' aims to", "plant a thousand trees round the school", "build a phone from recycled panels and chips", "produce cheap oxygen for village hospitals", "compose and record a new school anthem", "B",
     "The five-year project attracted media attention and funding from the NGO Life Grid."),
    ("Medium", T + "Bepo's involvement with the Invention Club shows that he", "was originally a science teacher", "believes invention is not limited by one's discipline", "wanted to leave teaching for technology", "disliked the arts", "B",
     "Though an English teacher, Bepo is the club's patron and vows to return for the phone's launch."),
    # --- Chapter 9: Laughing Waterfalls ---
    ("Medium", T + "Bepo's excursion policy at Stardom provided", "one international trip every term for the senior classes", "one local excursion each term and one international trip a year", "two visits to Badagry every year for every class in the school", "excursions for SSS 3 students only, in their final term", "B",
     "The policy exposed pupils to Nigeria's natural, historical and cultural sites before many left to study abroad."),
    ("Medium", T + "Bepo insisted on excursions because he wanted pupils who might later study abroad to", "learn how to travel alone without their parents", "know their fatherland well before leaving it", "avoid boredom during the long school terms", "pass their Geography and History examinations", "B",
     "He feared elite children would leave Nigeria without ever knowing it."),
    ("Medium", T + "the waterfall described as the highest in West Africa is", "Erin Ijesha Waterfalls", "Gurara Falls", "Owu Waterfalls", "Ikogosi Warm Springs", "C",
     "Owu Waterfalls in Kwara State is presented as the highest in West Africa."),
    ("Hard", T + "Ikogosi in Ekiti State is remembered in the novel as", "the site of the first storey building", "a warm spring discovered by Rev. John S. McGee in 1852", "the home of the Ooni", "the venue of the Osun festival", "B",
     "The novel recounts the folklore and history behind each site the pupils visited."),
    ("Medium", T + "Bepo took pupils to Ajegunle to teach them that", "slums are dangerous places that must be avoided at night", "being born in a slum does not condemn one to poverty", "footballers from poor homes always become rich and famous", "Lagos is overpopulated because of migration from villages", "B",
     "He cited Odion Ighalo and Victor Osimhen, who rose from the low ends of Lagos to stardom."),
    ("Medium", T + "Bepo's phrase 'life is a potpourri of opposites' is illustrated by", "the novelty football match between the staff and the students", "contrasting visits to Banana Island and to slums like Ajegunle", "the arts-versus-sciences debate at Bepo's farewell ceremony", "the reduction of boarding fees alongside the higher excursion fee", "B",
     "Pupils saw affluent estates and corporate offices alongside slums and charity homes."),
    ("Medium", T + "at the Black Heritage Museum in Badagry, Bepo compares the slave trade to", "the boarding-house system in elite schools", "the modern rush of Nigerians to migrate abroad", "the payment of school fees by poor parents", "the prefect elections at Stardom Schools", "B",
     "He sees japa as a voluntary 'new slavery' in which Africans again leave to build foreign economies."),
    ("Hard", T + "the First Storey Building in Badagry is significant in the novel as the place where", "Bepo was born and spent his childhood", "the Bible was translated into Yoruba", "the captured slaves were sold at auction", "the Akran of Badagry was first crowned", "B",
     "The pupils visit the Akran's palace, the First Storey Building and the Point of No Return."),
    # --- Chapter 10: Passport Pains ---
    ("Medium", T + "Bepo had allowed his passport to expire for two years because", "he had never been keen on relocating", "it had been stolen", "he could not afford the renewal fee", "he had been banned from travelling", "A",
     "Only his family's pressure turned the renewal into an emergency."),
    ("Medium", T + "Bepo chose to renew his passport in Ibadan in order to", "visit his home town and see his aged mother before travelling", "avoid the crowds and hassles at the Lagos passport offices", "meet Tai, an old school friend who worked at the passport office", "attend a conference of principals holding in the city", "B",
     "The japa wave had created maddening crowds at the Ikoyi and Ikeja offices."),
    ("Medium", T + "Tai, the agent, charged Bepo N100,000 although the official fee was", "N35,000", "N50,000", "N70,000", "N93,000", "C",
     "Bepo pays a 30,000-naira premium to the agent, who turns out to be a business-centre operator in a syndicate."),
    ("Medium", T + "the journey from Lagos to Ibadan took only about 50 minutes because", "Bepo travelled by the new train service", "the Lagos-Ibadan Expressway had been reconstructed", "he travelled at night when the road was free", "he rode on a motorcycle through the traffic", "B",
     "A decade earlier the same trip in a school bus had taken two hours."),
    ("Medium", T + "the many religious camps along the expressway make Bepo wonder whether Nigeria has", "'too many roads and too few cars'", "'many religionists but few godly people'", "'no honest pastors'", "'too few schools'", "B",
     "The thought fits his own situation: he is bribing an agent even as he passes the camps."),
    ("Medium", T + "Bepo's passport renewal is finally delayed by", "the sudden arrest of Tai by immigration officers", "a network glitch during the validation of his NIN", "a public holiday declared by the federal government", "a missing birth certificate and tax clearance", "B",
     "After paying the syndicate he is defeated by technology: the NIN office cannot validate him for three weeks."),
    ("Hard", T + "the brown roofs of Ibadan remind Bepo of", "Achebe's Things Fall Apart", "J. P. Clark's poem 'Ibadan'", "Soyinka's Ake", "the Third Mainland Bridge", "B",
     "He also recalls Adelakun's Under the Brown Rusted Roofs and Ibadan's first university and television station."),
    ("Hard", T + "Bepo's experience at the passport office shows that", "digitisation had finally ended corruption in the passport process", "officials sabotage the online system to keep an extortion racket alive", "the agents are in fact senior immigration officers in disguise", "the Ibadan office is far worse than those in Ikoyi and Ikeja", "B",
     "Government claims the process is fully digital, yet the erratic portal drives applicants to pay agents like Tai."),
    # --- Chapter 11: Point of No Return ---
    ("Medium", T + "Bepo changed his departure date and paid an airline penalty because", "his visa was delayed at the British High Commission", "the school wanted time for a befitting send-off", "his wife asked him to wait for the girls' school holidays", "the airline cancelled the flight at the last minute", "B",
     "The school gladly covered the 100-dollar penalty so that the farewell could hold."),
    ("Medium", T + "in the farewell debate, the winning side argued that", "the sciences have contributed more to Nigeria's development", "the arts have contributed more to Nigeria's development", "migration is good for Nigeria", "boarding schools are better than day schools", "B",
     "SSS 3, citing Nollywood and Soyinka's Nobel Prize, won the debate in Bepo's honour."),
    ("Easy", T + "the banner at Bepo's farewell read", "'Goodbye and God Bless, Principo'", "'For He Gave Stardom His Very Best'", "'Point of No Return: Farewell, Sir'", "'The Lekki Headmaster Goes to London'", "B",
     "The banner in the main hall summed up 24 years of service."),
    ("Medium", T + "the dance that sends Bepo into a hallucination of the slave trade is", "the Bata dance of the Yoruba", "the Atilogwu dance of the Igbo", "the Koroso dance of the Hausa", "the Canoe dance of the Badagry people", "D",
     "The canoe dance takes him back to the slavery museum; he recovers only when the performance ends."),
    ("Medium", T + "Bepo was employed at Stardom twenty-four years earlier by", "Mrs Ibidun Gloss", "Chief David Aje, the founder", "Chief Mrs Solape Bayo", "Mr Ope Wande", "B",
     "The MD's late father interviewed Bepo himself and called him an 'essential teacher'."),
    ("Medium", T + "the MD refuses to announce the amount of Bepo's farewell cheque because", "the sum was embarrassingly small", "it might tempt other staff to 'run away' too", "the board had forbidden it", "Bepo asked her not to", "B",
     "She reveals only that it is a domiciliary cheque in foreign currency."),
    ("Hard", T + "the Yoruba proverb about the master carver whose works live on expresses the theme of", "migration", "legacy", "corruption", "poverty", "B",
     "Bepo reflects that even after he leaves, the minds he has shaped will endure."),
    ("Medium", T + "at the end of the farewell, Bepo", "delivers a long and witty speech of thanks to the staff", "breaks down in tears at the podium, unable to speak", "announces to the shocked hall that he will not travel", "hands over the school keys to the new principal", "B",
     "His tears mirror the breakdown in the opening chapter; the whole hall weeps with him."),
    ("Medium", T + "the MD jokingly calls Britain", "'the land of no return'", "'the heaven and haven of good things'", "'a cold and hungry island'", "'the home of grammar'", "B",
     "Her tribute laments that Stardom and Nigeria are losing Bepo to Britain."),
    # --- Chapter 12: Dawn ---
    ("Medium", T + "Bepo leaves home at 3 p.m. for a 10 p.m. flight because", "he had once missed a flight because of Lagos traffic", "the airline demanded early check-in", "he wanted to shop at the airport", "the school bus was leaving early", "A",
     "He is determined not to repeat the day he missed a British Airways flight."),
    ("Medium", T + "before leaving, Bepo sold his SUV to", "Mr Audu", "the school accountant", "his landlord, Mr Ogunwale", "Tai, the agent", "B",
     "He sold the Pathfinder to the accountant and gave his freezer and electronics to his landlady."),
    ("Medium", T + "Jide, the landlord's grandson, was coached by Bepo at weekends in", "Mathematics and Physics", "elocution and African history", "football and athletics", "Yoruba and Hausa", "B",
     "Bepo feels guilty about abandoning the boy's weekend lessons."),
    ("Medium", T + "Bepo is disturbed when seven-year-old Kemi uses the word", "'Principo'", "'japa'", "'ritual'", "'visa'", "B",
     "That so young a child knows 'japa' shows how deeply the urge to flee has entered Nigerian life."),
    ("Medium", T + "in his nightmare at the airport, Bepo", "sees Stardom Schools burning to the ground in his absence", "is ordered by a white slave master to board a slave ship", "loses his passport and ticket minutes before boarding", "is arrested by immigration officers for using an agent", "B",
     "He wakes screaming 'no' just as an airline official taps him to announce boarding."),
    ("Medium", T + "Bepo's airport nightmare suggests that he sees migration as", "a well-earned holiday", "a new form of slavery", "a professional promotion", "a religious duty", "B",
     "The dream links his flight to London with the slave ships that left Badagry."),
    ("Medium", T + "on the Monday after his departure, the gloomy assembly is interrupted by", "the arrival of a new principal", "a shout of 'Principoo' as Bepo reappears", "a fire alarm", "the MD's resignation", "B",
     "The pupils sweep Bepo off his feet in a frenzied celebration."),
    ("Easy", T + "Bepo's final declaration on his return is", "'I will come back next year when my papers are ready'", "'I am back! My heart is here! I am here to complete my mission!'", "'London is now my home, but Stardom is in my heart'", "'Goodbye, Stardom, for ever; I have done my very best'", "B",
     "His return, celebrated with the school's victory song, ends the novel on a note of hope."),
    ("Hard", T + "Bepo's decision to return to Stardom is best described as", "cowardice in the face of the challenge of a new life abroad", "the triumph of personal conviction over family and social pressure", "blind obedience to the wishes of the Managing Director", "a calculated wish for an even bigger farewell cheque", "B",
     "Despite a UK job and his wife's ultimatum, he chooses his mission with Nigerian youth."),
    # --- Themes / character ---
    ("Medium", T + "which of the following is NOT a major theme of the novel?", "migration and identity", "leadership and sacrifice", "space exploration", "corruption in public institutions", "C",
     "The novel deals with japa, leadership, education, corruption and cultural heritage, not space exploration."),
    ("Medium", T + "Mrs Ibidun Gloss is best described as", "a careless and lazy administrator who leaves everything to Bepo", "a pragmatic businesswoman who guards the school's image and finances", "a timid woman who is ruled by her board and her senior staff", "a classroom teacher promoted beyond her ability and experience", "B",
     "She inherited the school from her father, holds a law degree and puts business first, yet respects Bepo."),
    ("Hard", T + "the secret physical pain that Mrs Gloss endures is used to show that", "she should hand over the school to a younger person", "wealth and power do not protect one from vulnerability", "the school clinic is too poorly equipped to treat her", "she is too old and too sick to lead a modern school", "B",
     "Her chronic pain mirrors her hidden fear that her staff might grow strong enough to challenge her."),
    ("Medium", T + "Mr Audu functions in the novel chiefly as", "the villain", "a source of comic relief", "Bepo's rival", "the voice of the parents", "B",
     "From coining the nickname to his Japanese bow, Audu's jokes lighten the tensest scenes."),
    ("Medium", T + "Bepo's attitude to migration throughout the novel is one of", "eager and open enthusiasm", "reluctance rooted in patriotism", "total indifference to it", "fear of flying long distances", "B",
     "He believes it makes no sense to abandon a developing nation to help build a developed one."),
    ("Medium", T + "the novel presents private education in Nigeria mainly as", "a charitable service run by dedicated and selfless people", "a heavily monetised business where fees outweigh principle", "a responsibility that government has wrongly abandoned", "a failing system in which no competent teacher remains", "B",
     "Fee manipulation, the Ayesoro and Fafore affairs and the costly prefect forms all show schooling as commerce."),
    ("Hard", T + "Bepo can be described as a round character because he", "appears in every single chapter of the novel from start to finish", "combines humour, empathy and firmness with private fear and doubt", "never once changes his mind about anything in the story", "is the narrator through whose eyes every event is seen", "B",
     "The novel shows both his public confidence and his private tears, and his views develop to a final decision."),
]


def build():
    questions = []
    for diff, q, a, b, c, d, ans, exp in NOVEL:
        questions.append({"subject": "Use of English", "topic": TOPIC, "difficulty": diff, "q": q,
                          "A": a, "B": b, "C": c, "D": d, "answer": ans, "explanation": exp})
    _balance(questions)
    texts = [x["q"] for x in questions]
    assert len(texts) == len(set(texts)), "duplicate question text"
    for x in questions:
        assert x["answer"] in "ABCD" and all(x[k] for k in "ABCD"), x["q"]
        assert len(x["explanation"]) >= 25, x["q"]
        assert len({x[k].strip().lower() for k in "ABCD"}) == 4, x["q"]
        lens = {k: len(x[k]) for k in "ABCD"}
        longest_other = max(v for k, v in lens.items() if k != x["answer"])
        assert not (lens[x["answer"]] > 30 and lens[x["answer"]] > 1.5 * longest_other), ("length bias", x["q"])
    batch = {
        "batch_id": "batch_012_english_novel",
        "exam_type": "JAMB",
        "note": "Use of English reading text: The Lekki Headmaster (Kabir Alabi Garba), the UTME recommended novel. 10 appear in every JAMB mock.",
        "passages": [],
        "questions": questions,
        "deactivate": [],
        "retire_topics": [],
    }
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(batch, fh, ensure_ascii=False, indent=1)
    from collections import Counter
    print(f"wrote {OUT}: {len(questions)} questions")
    print("answer letters:", dict(Counter(x["answer"] for x in questions)))
    print("difficulty:", dict(Counter(x["difficulty"] for x in questions)))


if __name__ == "__main__":
    build()
