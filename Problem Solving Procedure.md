[] Find the next problem statement in "Cracking the Coding Interview 189 Programming Questions and Solutions.pdf", and compare it with what ChatGPT extracted in the file ctci_problem_statements_utf8_extracted_by_chatgpt.txt.

[] Copy the most recent directory from .../algorithms/doc/Cracking the Coding Interview/dpp/InterviewQuestions/Chapter1-ArraysAndStrings
e.g 

```cd .../algorithms/doc/Cracking the Coding Interview/dpp/InterviewQuestions/Chapter1-ArraysAndStrings
    cp -r 1.4 1.5
```
   This creates the base artifacts for the problem 1.5 such as problem.json, which we'll modify.

* We might improve this step by copying only the problem.json, RUNME, and SETMEUP files (and .idea if using Webstorm)

[] Clean out any extraneous content from the new directory.

[] Update the url in problem.json to navigate to the correct page in the pdf. For problem 1.6, this would be "http://localhost:63343/algorithms/doc/Cracking%20the%20Coding%20Interview/Cracking%20the%20Coding%20Interview%20189%20Programming%20Questions%20and%20Solutions.pdf#page=212".

[] Copy the problem title ("One Away") in the case of problem 1.5 to problem.json's "title" value:

[] Copy the problem statement into problem.json's "statement" value. Can copy this from ctci_problem_statements_utf8_extracted_by_chatgpt.txt, but confirm that file's statement matches the .pdf.

[] Read the problem statement so as to inform the following steps

[] Copy the hints, including the hint text from the file .../extract-hints-from-pdf/ctci_hints.json

[] Based on the problem statement, update the "constraints" value.

[] Based on the problem statement, estimate and update the best "timeComplexity" value.

[] Based on the problem statement, estimate and update the best "spaceComplexity" value.

[] Copy the examples from the .pdf to problem.json in the "examples" array.

[] Update the "explanation" value with explanatory text of your own concoction.

[] Copy the examples to the "tests" array in problem.json.

[] Generate problem.html
```../../../../../../practice/python/generate-problem-html-from-problem-json/RUNME ../../../../../../practice/python/generate-problem-html-from-problem-json/template.html problem.json```

[] Generate problem.py
```../../../../../../practice/python/generate-problem-py-from-problem-json/RUNME ./```

[] Construct the ontology.

    [] Identify the "Features"
        [] Objects
        [] Constraints
        [] Actions (Functions)

[] Can the problem be expressed symbolically (mathematically)?

[] State the ontology in the Analysis.

[] Define the constraints.

[] What kind of machine is needed to solve the problem. e.g. state machine, push down automata etc.?

[] Code the problem using the appropriate automata

[] Code the problem a different (organic) way.

have had an implicit mental task like "Look closely at the given example for any constraints or gotchas"

optimize our solution until it is the best it can be for space and time

[] Find Gayle's solution and compare with ours

[] Update our solution if necessary.

[] Based on the problem statement, estimate and update the timeComplexity value.

[] Based on the problem statement, estimate and update the spaceComplexity value.

[] Try to identify the "atomic algorithms" or at least "more fundamental algorithms" or "nearest ancestor algorithms" therein.

[] Label these algorithms

[] Research "more fundamental algorithms" in terms of most frequently used code patterns

[] Research the problem, and similar problems

[] Find sample problems in 

    [] LeetCode
    [] HackerRank has "Edit Distance" variants in its Algorithm section
    [] Codeforces has multiple string distance problems in its problem archive
    [] CodeSignal includes edit distance problems in its interview prep tracks
    [] NeetCode.io — has a dedicated "1D DP" and "2D DP" roadmap covering these string problems
    [] AlgoExpert — curated set that includes edit distance variants with video walkthroughs
    [] GeeksforGeeks — has extensive write-ups on edit distance and one-edit-distance specifically
    [] Create frequency map of use of related algorithms in this context

[] Execute such problems if found



[] Create some kind of spaced repetition system
[] Adapt maxrecall.net?