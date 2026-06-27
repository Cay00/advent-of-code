#   The notation X|Y means that if both page number X and page number Y are to be produced
#   as part of an update, page number X must be printed at some point before page number Y.

#   The Elf has for you both the page ordering rules and the pages to produce in each update (your puzzle input),
#   but can't figure out whether each update has the pages in the right order.

#   The first section specifies the page ordering rules, one per line.
#   The first rule, 47|53, means that if an update includes both page number 47 and page number 53,
#   then page number 47 must be printed at some point before page number 53.

#   The second section specifies the page numbers of each update.
#   Because most safety manuals are different, the pages needed in the updates are different too.
#   The first update, 75,47,61,53,29, means that the update consists of page numbers 75, 47, 61, 53, and 29.

#   To get the printers going as soon as possible, start by identifying which updates are already in the right order.
#   For some reason, the Elves also need to know the middle page number of each update being printed.

#   For example:

#   47|53
#   97|13
#   97|61
#   97|47
#   75|29
#   61|13
#   75|53
#   29|13
#   97|29
#   53|29
#   61|53
#   97|53
#   61|29
#   47|13
#   75|47
#   97|75
#   47|61
#   75|61
#   47|29
#   75|13
#   53|13

#   75,47,61,53,29
#   97,61,53,29,13
#   75,29,13
#   75,97,47,61,53
#   61,13,29
#   97,13,75,29,47

#   test answer 1: 143
#   test answer 2: 123
