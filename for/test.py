from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """


def alphabet_set(old_list):
    a_list = []
    b_list = []
    c_list = []
    d_list = []
    e_list = []
    f_list = []
    g_list = []
    h_list = []
    i_list = []
    j_list = []
    k_list = []
    l_list = []
    m_list = []
    n_list = []
    o_list = []
    p_list = []
    q_list = []
    r_list = []
    s_list = []
    t_list = []
    u_list = []
    v_list = []
    w_list = []
    x_list = []
    y_list = []
    z_list = []
    new_list = []
    for item in old_list:
        if item[0] == "A":
            a_list.append(item)
        elif item[0] == "B":
            b_list.append(item)
        elif item[0] == "C":
            c_list.append(item)
        elif item[0] == "D":
            d_list.append(item)
        elif item[0] == "E":
            e_list.append(item)
        elif item[0] == "F":
            f_list.append(item)
        elif item[0] == "G":
            g_list.append(item)
        elif item[0] == "H":
            h_list.append(item)
        elif item[0] == "I":
            i_list.append(item)
        elif item[0] == "J":
            j_list.append(item)
        elif item[0] == "K":
            k_list.append(item)
        elif item[0] == "L":
            l_list.append(item)
        elif item[0] == "M":
            m_list.append(item)
        elif item[0] == "N":
            n_list.append(item)
        elif item[0] == "O":
            o_list.append(item)
        elif item[0] == "P":
            p_list.append(item)
        elif item[0] == "Q":
            q_list.append(item)
        elif item[0] == "R":
            r_list.append(item)
        elif item[0] == "S":
            s_list.append(item)
        elif item[0] == "T":
            t_list.append(item)
        elif item[0] == "U":
            u_list.append(item)
        elif item[0] == "V":
            v_list.append(item)
        elif item[0] == "W":
            w_list.append(item)
        elif item[0] == "X":
            x_list.append(item)
        elif item[0] == "Y":
            y_list.append(item)
        elif item[0] == "Z":
            z_list.append(item)
        else:
            continue

    # if a_list != []:
    #     new_list.append(a_list)
    # else:
    #     new_list.append("Aland")

    new_list.append(a_list)
    new_list.append(b_list)
    new_list.append(c_list)
    new_list.append(d_list)
    new_list.append(e_list)
    new_list.append(f_list)
    new_list.append(g_list)
    new_list.append(h_list)
    new_list.append(i_list)
    new_list.append(j_list)
    new_list.append(k_list)
    new_list.append(l_list)
    new_list.append(m_list)
    new_list.append(n_list)
    new_list.append(o_list)
    new_list.append(p_list)
    new_list.append(q_list)
    new_list.append(r_list)
    new_list.append(s_list)
    new_list.append(t_list)
    new_list.append(u_list)
    new_list.append(v_list)

    if x_list != []:
        new_list.append(x_list)
    else:
        new_list.append(["Xland"])

    new_list.append(w_list)
    new_list.append(x_list)
    new_list.append(y_list)
    new_list.append(z_list)

    # print(new_list)
    final_list = []
    for item in new_list:
        if item != []:
            final_list.append(item[0][0])

        else:
            continue
    print(len(final_list))
    print(final_list)
    return final_list


def alphabet_set_better(old_list):
    new_list = []
    for item in old_list:
        if "x" in item:
            new_list.append(item[item.index("x")].upper())
        else:
            new_list.append(item[0])

    print(sorted(set(new_list)))


def count_vowels(item):
    number_of_a = item.lower().count("a")
    number_of_e = item.lower().count("e")
    number_of_i = item.lower().count("i")
    number_of_o = item.lower().count("o")
    number_of_u = item.lower().count("u")
    total = number_of_a + number_of_e + number_of_i + number_of_o + number_of_u
    return total


def most_vowels(old_list):
    for i in range(0, len(old_list)):
        for j in range(i + 1, len(old_list)):
            if count_vowels(old_list[i]) < count_vowels(old_list[j]):
                old_list[i], old_list[j] = old_list[j], old_list[i]
        # print(l)

    print("sorted list")
    # print(l)
    print(
        [
            old_list[0],
            old_list[1],
            old_list[2],
        ]
    )
    new_list = [old_list[0], old_list[1], old_list[2]]
    return new_list


def make_most_vowel_list(old_list):
    old_list.sort(reverse=True, key=count_vowels)

    new_list = []
    for item in old_list:
        new_item = item, count_vowels(item)
        new_list.append(new_item)

    print(new_list)


# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()
    # alphabet_set(countries)
    # alphabet_set_better(countries)
    make_most_vowel_list(countries)

    """ Write the calls to your functions here. """
