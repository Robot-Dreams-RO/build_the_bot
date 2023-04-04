########
3. TODO
########

Build a bot to help with triage in ER. This would be a bot that would get input from the patient about what symptoms they have and score their status. Then provide an order in which the patients will be seen by the doctor. This would be a great way to help the doctor and the patient. The doctor would be able to see the patients in order of severity and the patient would be able to see how long they would have to wait.

The patient will be triaged in one of these categories

========== ========================== ================================================
Definition Triage categories          General discriminators
========== ========================== ================================================
Red        Immediate - Immediate      Airway compromise

                                      Inadequate breathing

                                      Exsanguinate hemorrhage

                                      Currently seizing

                                      Abnormal age-related vital signs

                                      GCS ≤ 12

                                      Oxygen saturations ≤ 90%
Orange     Very urgent - ≤ 10 minutes Severe pain (pain score 7-10)

                                      Uncontrollable major hemorrhage

                                      GCS 13 or 14

                                      Abnormal age-related vital signs

                                      Signs of compensated shock

                                      Oxygen saturations ≤ 92%

                                      Central capillary refill time (CRT) > 2 seconds
Yellow     Urgent - ≤ 60 minutes      Moderate pain (pain score 4-6)

                                      Uncontrollable minor hemorrhage

                                      Abnormal age-related vital signs

                                      History of unconsciousness
Green      Standard - ≤ 120 minutes   Mild pain (Pain score 1-3)

                                      Problem <48 hours
Blue       Non-urgent - ≤ 240 minutes Problem > 48 hours

========== ========================== ================================================