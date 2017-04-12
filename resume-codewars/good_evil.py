# goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1') == 'Battle Result: Evil eradicates all trace of Good', 'Evil should win' );
# Return ""Battle Result: Good triumphs over Evil" if good wins,
# "Battle Result: Evil eradicates all trace of Good" if evil wins,
# or "Battle Result: No victor on this battle field" if it ends in a tie.
good_force = [1, 2, 3, 3, 4, 10]
evil_force = [1, 2, 2, 2, 3, 5, 10]


def goodVsEvil(good, evil):
    power_good, power_evil = 0, 0
    i = 0
    t = 0
    for g in good.split():
        power_good += int(g) * good_force[i]
        i += 1
    for e in evil.split():
        power_evil += int(e) * evil_force[t]
        t += 1
    if power_good > power_evil:
        return "Battle Result: Good triumphs over Evil"
    elif power_evil > power_good:
        return 'Battle Result: Evil eradicates all trace of Good'
    else:
        return "Battle Result: No victor on this battle field"


print(goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1'))