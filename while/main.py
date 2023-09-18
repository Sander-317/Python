from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"


def unique_koala_facts(number):
    loops, max_loops = 0, 1000
    facts = []
    while len(facts) < number:
        fact = random_koala_fact()
        if fact not in facts:
            facts.append(fact)
        if loops > max_loops:
            break
        loops += 1
    return facts


def num_joey_facts():
    loops, max_loops = 0, 1000
    check_fact = random_koala_fact()
    check_fact_count = 0
    facts = []
    while loops < max_loops:
        # print(check_fact_count)
        fact = random_koala_fact()
        facts.append(fact)
        if fact == check_fact:
            check_fact_count += 1
        if check_fact_count == 10:
            break
        if loops > max_loops:
            break
        loops += 1

    print("facts length", len(facts))
    print(set(facts))
    print("facts set length", len(set(facts)))
    joey_count = 0
    for item in set(facts):
        if "joey" in item:
            joey_count += 1
        else:
            continue
    print("joey count", joey_count)

    return joey_count


# 'The koala weighs 15 to 30 pounds.
# koalas measure about 60cm to 85cm long, and weigh about 14kg.


def koala_weight():
    loops, max_loops = 0, 1000
    facts = []
    while loops < max_loops:
        fact = random_koala_fact()
        if "kg" in fact:
            facts.append(fact)
            break
        if loops > max_loops:
            break
        loops += 1

    index = facts[0].index("kg")
    result = int(facts[0][index - 2] + facts[0][index - 1])
    return result


# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    print(random_koala_fact())
    print(unique_koala_facts(10))
    print(koala_weight())
    print(num_joey_facts())
