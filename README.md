# Text-Summarizer
Comparing state of the art models for text summary generation

[![Google Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/singhsidhukuldeep/Text-Summarizer/blob/master/Text_Summary_%5BGoogle_Colab%5D.ipynb)

## Usage

### Setup

```shell
pip3 install -r requirements.txt
python -m spacy download en_core_web_md
```

```Python
from NLTK_summarizer import SummarizerNLTK
print(SummarizerNLTK().summary(text = ""))

from BERT_summarizer import SummarizerBERT
print(SummarizerBERT().summary(text = ""))

from T5_BART_summarizer import SummarizerT5BART
print(SummarizerT5BART().summary(text = ""))
```

*Look at the documentation in the files for better understanding*

## Text used

Taken from Kaggle dataset: https://www.kaggle.com/snapcrack/all-the-news

```
WASHINGTON  —   Congressional Republicans have a new fear when it comes to their    health care lawsuit against the Obama administration: They might win. The incoming Trump administration could choose to no longer defend the executive branch against the suit, which challenges the administration’s authority to spend billions of dollars on health insurance subsidies for   and   Americans, handing House Republicans a big victory on    issues. But a sudden loss of the disputed subsidies could conceivably cause the health care program to implode, leaving millions of people without access to health insurance before Republicans have prepared a replacement. That could lead to chaos in the insurance market and spur a political backlash just as Republicans gain full control of the government. To stave off that outcome, Republicans could find themselves in the awkward position of appropriating huge sums to temporarily prop up the Obama health care law, angering conservative voters who have been demanding an end to the law for years. In another twist, Donald J. Trump’s administration, worried about preserving executive branch prerogatives, could choose to fight its Republican allies in the House on some central questions in the dispute. Eager to avoid an ugly political pileup, Republicans on Capitol Hill and the Trump transition team are gaming out how to handle the lawsuit, which, after the election, has been put in limbo until at least late February by the United States Court of Appeals for the District of Columbia Circuit. They are not yet ready to divulge their strategy. “Given that this pending litigation involves the Obama administration and Congress, it would be inappropriate to comment,” said Phillip J. Blando, a spokesman for the Trump transition effort. “Upon taking office, the Trump administration will evaluate this case and all related aspects of the Affordable Care Act. ” In a potentially   decision in 2015, Judge Rosemary M. Collyer ruled that House Republicans had the standing to sue the executive branch over a spending dispute and that the Obama administration had been distributing the health insurance subsidies, in violation of the Constitution, without approval from Congress. The Justice Department, confident that Judge Collyer’s decision would be reversed, quickly appealed, and the subsidies have remained in place during the appeal. In successfully seeking a temporary halt in the proceedings after Mr. Trump won, House Republicans last month told the court that they “and the  ’s transition team currently are discussing potential options for resolution of this matter, to take effect after the  ’s inauguration on Jan. 20, 2017. ” The suspension of the case, House lawyers said, will “provide the   and his future administration time to consider whether to continue prosecuting or to otherwise resolve this appeal. ” Republican leadership officials in the House acknowledge the possibility of “cascading effects” if the   payments, which have totaled an estimated $13 billion, are suddenly stopped. Insurers that receive the subsidies in exchange for paying    costs such as deductibles and   for eligible consumers could race to drop coverage since they would be losing money. Over all, the loss of the subsidies could destabilize the entire program and cause a lack of confidence that leads other insurers to seek a quick exit as well. Anticipating that the Trump administration might not be inclined to mount a vigorous fight against the House Republicans given the  ’s dim view of the health care law, a team of lawyers this month sought to intervene in the case on behalf of two participants in the health care program. In their request, the lawyers predicted that a deal between House Republicans and the new administration to dismiss or settle the case “will produce devastating consequences for the individuals who receive these reductions, as well as for the nation’s health insurance and health care systems generally. ” No matter what happens, House Republicans say, they want to prevail on two overarching concepts: the congressional power of the purse, and the right of Congress to sue the executive branch if it violates the Constitution regarding that spending power. House Republicans contend that Congress never appropriated the money for the subsidies, as required by the Constitution. In the suit, which was initially championed by John A. Boehner, the House speaker at the time, and later in House committee reports, Republicans asserted that the administration, desperate for the funding, had required the Treasury Department to provide it despite widespread internal skepticism that the spending was proper. The White House said that the spending was a permanent part of the law passed in 2010, and that no annual appropriation was required  —   even though the administration initially sought one. Just as important to House Republicans, Judge Collyer found that Congress had the standing to sue the White House on this issue  —   a ruling that many legal experts said was flawed  —   and they want that precedent to be set to restore congressional leverage over the executive branch. But on spending power and standing, the Trump administration may come under pressure from advocates of presidential authority to fight the House no matter their shared views on health care, since those precedents could have broad repercussions. It is a complicated set of dynamics illustrating how a quick legal victory for the House in the Trump era might come with costs that Republicans never anticipated when they took on the Obama White House.
```

## Results

| # | Model | Time Taken(with Downloads) | Completed | Summary | Time Taken (without downloads) |
| --- | --- | --- | --- | --- | --- |
| 1 | NLTK Corpus | 0 | True | The incoming Trump administration could choose... | 0 |
| 2 | bert-base-uncased kmeans | 27 | True | The incoming Trump administration could choose... | 15 |
| 3 | bert-base-uncased gmm | 3 | True | The incoming Trump administration could choose... | 4 |
| 4 | bert-large-uncased kmeans | 29 | True | The incoming Trump administration could choose... | 8 |
| 5 | bert-large-uncased gmm | 9 | True | The Justice Department, confident that Judge C... | 9 |
| 6 | xlnet-base-cased kmeans | 11 | True | But a sudden loss of the disputed subsidies co... | 3 |
| 7 | xlnet-base-cased gmm | 3 | True | But a sudden loss of the disputed subsidies co... | 3 |
| 8 | xlm-mlm-enfr-1024 kmeans | 20 | True | WASHINGTON --- Congressional Republicans have... | 4 |
| 9 | xlm-mlm-enfr-1024 gmm | 25 | True | But a sudden loss of the disputed subsidies co... | 5 |
| 10 | distilbert-base-uncased kmeans | 6 | True | But a sudden loss of the disputed subsidies co... | 2 |
| 11 | distilbert-base-uncased gmm | 2 | True | But a sudden loss of the disputed subsidies co... | 2 |
| 12 | albert-base-v1 kmeans | 3 | True | To stave off that outcome, Republicans could f... | 2 |
| 13 | albert-base-v1 gmm | 2 | True | But a sudden loss of the disputed subsidies co... | 2 |
| 14 | albert-large-v1 kmeans | 4 | True | The incoming Trump administration could choose... | 2 |
| 15 | albert-large-v1 gmm | 3 | True | But a sudden loss of the disputed subsidies co... | 3 |
| 16 | facebook/bart-large-cnn | 36 | False | ERROR | 56 |
| 17 | t5-11b | 4 | False | ERROR | 2 |
| 18 | t5-3b | SKIPPED | False | ERROR | SKIPPED |
| 19 | t5-base | 30 | True | a sudden loss | 38 |
| 20 | t5-large | SKIPPED | False | ERROR | SKIPPED |
| 21 | t5-small | 9 | True | incoming administration could | 11 |

*If you want to compare the outputs, go to `results` folder*

> All time is in seconds

> Skipped means it failed even after multiple attempts

> ERROR means the process didn't complete

**This code was run on Google Colab (GPU Runtime) which has fairly good hardware.**

**Also it might take some time downloading the large pre-trained models**

## Conclusion

NLTK works faster and better most of the time.

The next best is BERT but the way tokenization happens in BERT, sometimes it leaves the sentence in between loosing all meaning. It works well with very large texts.

T5 tries to figure out new sentences but is almost impossible to run even using decent hardware. For T5 you can chose the size of the model. Everything above t5-base is very slow, even on GPU or TPU.

facebook BART does too many computatons and exhausts memory really quickly.

## To-do

☐ Run on full datasets 

☑ Compare effciency on GPUs

☑ Add facebook's BART

☑ Add Google T5

☑ Add BERT large

## CREDITS

>Kuldeep Singh Sidhu

Github: [github/singhsidhukuldeep](https://github.com/singhsidhukuldeep)
`https://github.com/singhsidhukuldeep`

Website: [Kuldeep Singh Sidhu (Website)](http://kuldeepsinghsidhu.com)
`http://kuldeepsinghsidhu.com`

LinkedIn: [Kuldeep Singh Sidhu (LinkedIn)](https://www.linkedin.com/in/singhsidhukuldeep/)
`https://www.linkedin.com/in/singhsidhukuldeep/`