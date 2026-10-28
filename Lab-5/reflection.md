# Lab 5 - Reflection

**Name:** Guru R Bharadwaj | **SRN:** PES1UG24CS177 | **Section:** 5 C

## 1. Which issues were the easiest to fix, and which were the hardest? Why?

The Flake8 findings were the easiest. Long lines, `== None`, an unused import and a missing newline each took one small edit, and none of them changed what the program does. Swapping MD5 for SHA-256 and `random` for `secrets` was also quick, since they were one-line replacements.

`eval` took the most work. I couldn't just delete it, because `main()` passed the discount as a string expression (`"base_fee * 0.85"`). I had to change the function to take a number, add a range check, change the call site and confirm the renewal fee was still 510.0. The mutable default argument was also hard in a different way: the fix is short, but the bug only appears when you call the function twice, so you have to understand why `[]` is shared before the fix makes sense.

## 2. Did the static analysis tools report any false positives? If so, describe one example.

Not exactly, though some findings matter less here than the tool suggests. B311 (`random` is not cryptographically secure) fires on any use of `random`. For a shuffle or a game that would be a false positive. Here it is generating a locker PIN, so the warning is fair, but a tool can't tell those cases apart. B105 (hardcoded password) is a guess based on the variable name. It happened to be right this time, and it would also fire on a harmless string assigned to a variable named `password_hint`.

There were also gaps. Bandit flagged the hardcoded secret but not the `print` that showed it on screen, and no tool noticed that the output came out in the wrong order. I found those by running the program and reading what it printed.

## 3. How would you integrate static analysis tools into your actual software development workflow?

On my own machine I would run Flake8 and Pylint inside the editor so problems show up while I type, and add a pre-commit hook that runs all three tools before each commit.

For a team, I would add a GitHub Actions job that runs on every pull request. It would fail the build on any Bandit High or Medium finding, on any Flake8 error, or if the Pylint score drops below a set value such as 9.5. The rules would live in a shared `.pylintrc` or `setup.cfg` in the repo so everyone checks against the same settings. Anyone who silences a finding with `# nosec` or `# pylint: disable` should add a comment saying why.

## 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

The shell injection, the `eval`, the weak hash and the leaked secret are gone, and Bandit went from 6 issues (2 High) to none.

The code also behaves better. `register_member` no longer shares one log list between calls, the roster file is always closed, and `cancel_membership` tells the caller whether it worked. Importing the module no longer runs the demo.

It is easier to read too. Function names are all snake_case, each function has a docstring, and the dead variables are gone. `check_membership_status` went from six lines to three.

Pylint went from 4.81 to 10.00 and Flake8 from 9 findings to 0. The program prints the same results as before, except the hash (now SHA-256) and the secret, which it no longer prints.
