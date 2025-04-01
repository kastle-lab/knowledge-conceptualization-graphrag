# -*- coding: utf-8 -*-
import re

def convert_subclass(axiom_string):

    axiom_string = axiom_string.replace('`', '').replace('`', '')
    a, b = axiom_string.split('SubClassOf')
    return f"All x where x is of type {a.strip()} implies that x is of type {b.strip()}"


def convert_disjoint(axiom_string):

    axiom_string = axiom_string.replace('`', '').replace('`', '')
    a, b = axiom_string.split('DisjointWith')

    disjoint = f"For all x where x is of type {a.strip()} implies x is not of " \
    f"type {b.strip()} and where x is of type {b.strip()} implies x is not of " \
    f"type {a.strip()}"

    return disjoint

def convert_global_domain(axiom_string):

    axiom_string = axiom_string.replace('`', '').replace('`', '')
    r, a = axiom_string.split('some owl:Thing SubClassOf')

    domain = f"For all x, if there exists a relationship {r.strip()} with x and "\
       f"x is of type {a.strip()}"

    return domain


def convert_scoped_domain(axiom_string):

    axiom_string = axiom_string.replace('`', '').replace('`', '')
    r, ba = axiom_string.split('some')
    b, a = ba.split('SubClassOf')

    domain = f"For all x, if there exists a relationship {r.strip()} with x and "\
        f"y and y is of type {b.strip()} implies x is of type {a.strip()}"

    return domain

def convert_global_range(axiom_string):

    axiom_string = axiom_string.replace('`', '').replace('`', '')
    axiom_string = axiom_string.replace('owl:Thing SubClassOf', '')
    r, b = axiom_string.split('only')

    range = f"For all x and y, if there exists a relationship {r.strip()} with x "\
        f"and y and implies y is of type {b.strip()}"

    return range

def convert_scoped_range(axiom_string):

    axiom_string = axiom_string.replace('`', '').replace('`', '')
    a, rb = axiom_string.split('SubClassOf')
    r, b = rb.split('only')

    range = f"For all x, if x is of type {a.strip()} and there exists a relationship "\
        f"{r.strip()} with x and y and implies y is of type {b.strip()}"

    return range

def convert_existential(axiom_string):

    axiom_string = axiom_string.replace('`', '').replace('`', '')
    a, rb = axiom_string.split('SubClassOf')
    r, b = rb.split('some')

    exist = f"For all x where x is of type {a.strip()} implies there exists a y and a "\
        f"relationship {r.strip()} with x and y and y is of type {b.strip()}"

    return exist

def convert_inverse_existential(axiom_string):

    axiom_string = axiom_string.replace('`', '').replace('`', '')
    b, ra = axiom_string.split('SubClassOf inverse')
    r, a = ra.split('some')

    exist = f"For every x that is of type {b.strip()} there has to be an inverse "\
        f"{r.strip()}-filler that connects y and x such that y is of type {a.strip()}"

    return exist


def convert_functionality(axiom_string):

    axiom_string = axiom_string.replace('`', '').replace('`', '')
    axiom_string = axiom_string.replace('owl:Thing SubClassOf', '')
    r = axiom_string.replace('max 1 owl:Thing', '')

    funct = f"For all x implies either there does not exist a y and a relationship "\
        f"{r.strip()} with x and y or there exists exactly 1 y and a relationship "\
        f"{r.strip()} with x and y."

    return funct


def convert_qualified_functionality(axiom_string):

    axiom_string = axiom_string.replace('`', '').replace('`', '')
    axiom_string = axiom_string.replace('owl:Thing SubClassOf', '')
    r, b = axiom_string.split('max 1')

    funct = f"For all x implies either there does not exist a y and a relationship "\
        f"{r.strip()} with x and y or there exists exactly 1 y and a relationship "\
        f"{r.strip()} with x and y and y is of type {b.strip()}."

    return funct


def convert_scoped_functionality(axiom_string):

    axiom_string = axiom_string.replace('`', '').replace('`', '')
    axiom_string = axiom_string.replace('max 1 owl:Thing', '')
    a, r = axiom_string.split('SubClassOf')

    funct = f"For all x where x is of type {a.strip()} implies either there does not "\
        f"exist a y and a relationship {r.strip()} with x and y or there exists exactly "\
        f"1 y and a relationship {r.strip()} with x and y."

    return funct

def convert_qualified_scoped_functionality(axiom_string):

    axiom_string = axiom_string.replace('`', '').replace('`', '')
    a, rb = axiom_string.split('SubClassOf')
    r, b = rb.split('max 1')

    funct = f"For all x where x is of type {a.strip()} implies either there does not "\
        f"exist a y and a relationship {r.strip()} with x and y or there exists exactly "\
        f"1 y and a relationship {r.strip()} with x and y and y is of type {b.strip()}."

    return funct


def convert_inverse_functionality(axiom_string):

    axiom_string = axiom_string.replace('`', '').replace('`', '')
    axiom_string = axiom_string.replace('owl:Thing SubClassOf inverse', '')
    r = axiom_string.replace('max 1', '')

    funct = f"For all y implies either there does not exist a x and an inverse "\
        f"relationship {r.strip()} with y and x or there exists exactly 1 x and "\
        f"an inverse relationship {r.strip()} with y and x."

    return funct

def convert_inverse_qualified_functionality(axiom_string):

    axiom_string = axiom_string.replace('`', '').replace('`', '')
    axiom_string = axiom_string.replace('owl:Thing SubClassOf inverse', '')
    r, a = axiom_string.split('max 1')

    funct = f"For all y implies either there does not exist a x and an inverse "\
        f"relationship {r.strip()} with x and y or there exists exactly 1 y and "\
        f"an inverse relationship {r.strip()} with y and x and x is of type {a.strip()}."

    return funct

def convert_inverse_scoped_functionality(axiom_string):

    axiom_string = axiom_string.replace('`', '').replace('`', '')
    axiom_string = axiom_string.replace('max 1 owl:Thing', '')
    b, r = axiom_string.split('SubClassOf inverse')

    funct = f"For all y where y is of type {b.strip()} implies either there does "\
        f"not exist a x and an inverse relationship {r.strip()} with y and x or "\
        f"there exists exactly 1 x and a relationship {r.strip()} with y and x."

    return funct


def convert_inverse_qualified_scoped_functionality(axiom_string):

    axiom_string = axiom_string.replace('`', '').replace('`', '')
    b, ra = axiom_string.split('SubClassOf inverse')
    r, a = ra.split('max 1')

    funct = f"For all y where y is of type {b.strip()} implies either there does "\
        f"not exist a y and an inverse relationship {r.strip()} with y and x or "\
        f"there exists exactly 1 x and a relationship {r.strip()} with y and x is "\
        f"of type {a.strip()}."

    return funct



def convert_structural_tautology(axiom_string):
    axiom_string = axiom_string.replace('`', '').replace('`', '')
    a, rb = axiom_string.split('SubClassOf')
    r, b = rb.split('min 0')

    ax17 = f"For all x where x is of type {a.strip()} implies there may exist a y "\
        f"and a relationship {r.strip()} with x and y and y is of type {b.strip()}."

    return ax17



def generate_subclass(axiom_string):

    a, r, b = axiom_string.split(' ')

    return f"`{a} SubClassOf {b}`"


def generate_disjoint(axiom_string):

    a, r, b = axiom_string.split(' ')

    return f"`{a} DisjointWith {b}`"

def generate_global_domain(axiom_string):

    a, r, b = axiom_string.split(' ')

    return f"`{r} some owl:Thing SubClassOf {a}`"

def generate_scoped_domain(axiom_string):

    a, r, b = axiom_string.split(' ')

    return f"`{r} some {b} SubClassOf {a}`"

def generate_global_range(axiom_string):

    a, r, b = axiom_string.split(' ')

    return f"`owl:Thing SubClassOf {r} only {b}`"


def generate_scoped_range(axiom_string):

    a, r, b = axiom_string.split(' ')

    return f"`{a} SubClassOf {r} only {b}`"

def generate_existential(axiom_string):

    a, r, b = axiom_string.split(' ')

    return f"`{a} SubClassOf {r} some {b}`"


def generate_inverse_existential(axiom_string):

    a, r, b = axiom_string.split(' ')

    return f"`{b} SubClassOf inverse {r} some {a}`"


def generate_functionality(axiom_string):

    a, r, b = axiom_string.split(' ')

    return f"`owl:Thing SubClassOf {r} max 1 owl:Thing`"


def generate_qualified_functionality(axiom_string):

    a, r, b = axiom_string.split(' ')

    return f"`owl:Thing SubClassOf {r} max 1 {b}`"

def generate_scoped_functionality(axiom_string):

    a, r, b = axiom_string.split(' ')

    return f"`{a} SubClassOf {r} max 1 owl:Thing`"



def generate_qualified_scoped_functionality(axiom_string):

    a, r, b = axiom_string.split(' ')

    return f"`{a} SubClassOf {r} max 1 {b}`"


def generate_inverse_functionality(axiom_string):

    a, r, b = axiom_string.split(' ')

    return f"`owl:Thing SubClassOf inverse {r} max 1 owl:Thing`"

def generate_inverse_qualified_functionality(axiom_string):

    a, r, b = axiom_string.split(' ')

    return f"`owl:Thing SubClassOf inverse {r} max 1 {a}`"

def generate_inverse_scoped_functionality(axiom_string):

    a, r, b = axiom_string.split(' ')

    return f"`{b} SubClassOf inverse {r} max 1 owl:Thing`"

def generate_inverse_qualified_scoped_functionality(axiom_string):

    a, r, b = axiom_string.split(' ')

    return f"`{b} SubClassOf inverse {r} max 1 {a}`"

def generate_structural_tautology(axiom_string):
    
    if re.search('SubClassOf ', axiom_string):
        axiom_string = axiom_string.replace('SubClassOf ', '')

        a, b = axiom_string.split(' ')
        r = 'SubClassOf'
        return f"`{b} SubClassOf min 0 {a}`"
    else:
        a, r, b = axiom_string.split(' ')

        return f"`{b} SubClassOf {r} min 0 {a}`"

def print_zipped(orig_list, created_statements):
    for x,y in zip(orig_list, created_statements):
        print("`" + x.strip() + "`")
        print(y)

def convert_run_all(relation_list, name_string, results_dict):
    rl_lst = []
    rl_nl = []

    for x in relation_list:
        if name_string == "subclass":
            rl_lst.append(generate_subclass(x))
            rl_nl.append(convert_subclass(generate_subclass(x)))

        elif name_string == "disjoint":
            rl_lst.append(generate_disjoint(x))
            rl_nl.append(convert_disjoint(generate_disjoint(x)))

        elif name_string == "global domain":
            rl_lst.append(generate_global_domain(x))
            rl_nl.append(convert_global_domain(generate_global_domain(x)))

        elif name_string == "scoped domain":
            rl_lst.append(generate_scoped_domain(x))
            rl_nl.append(convert_scoped_domain(generate_scoped_domain(x)))

        elif name_string == "global range":
            rl_lst.append(generate_global_range(x))
            rl_nl.append(convert_global_range(generate_global_range(x)))

        elif name_string == "scoped range":
            rl_lst.append(generate_existential(x))
            rl_nl.append(convert_existential(generate_existential(x)))

        elif name_string == "existential":
            rl_lst.append(generate_existential(x))
            rl_nl.append(convert_existential(generate_existential(x)))

        elif name_string == "inverse existential":
            rl_lst.append(generate_inverse_existential(x))
            rl_nl.append(convert_inverse_existential(generate_inverse_existential(x)))

        elif name_string == "functionality":
            rl_lst.append(generate_functionality(x))
            rl_nl.append(convert_functionality(generate_functionality(x)))

        elif name_string == "qualified functionality":
            rl_lst.append(generate_qualified_functionality(x))
            rl_nl.append(convert_qualified_functionality(generate_qualified_functionality(x)))

        elif name_string == "scoped functionality":
            rl_lst.append(generate_scoped_functionality(x))
            rl_nl.append(convert_scoped_functionality(generate_scoped_functionality(x)))

        elif name_string == "qualified scoped functionality":
            rl_lst.append(generate_qualified_scoped_functionality(x))
            rl_nl.append(convert_qualified_scoped_functionality(generate_qualified_scoped_functionality(x)))

        elif name_string == "inverse functionality":
            rl_lst.append(generate_inverse_functionality(x))
            rl_nl.append(convert_inverse_functionality(generate_inverse_functionality(x)))

        elif name_string == "inverse qualified functionality":
            rl_lst.append(generate_inverse_qualified_functionality(x))
            rl_nl.append(convert_inverse_qualified_functionality(generate_inverse_qualified_functionality(x)))

        elif name_string == "inverse scoped functionality":
            rl_lst.append(generate_inverse_scoped_functionality(x))
            rl_nl.append(convert_inverse_scoped_functionality(generate_inverse_scoped_functionality(x)))

        elif name_string == "inverse qualified scoped functionality":
            rl_lst.append(generate_inverse_qualified_scoped_functionality(x))
            rl_nl.append(convert_inverse_qualified_scoped_functionality(generate_inverse_qualified_scoped_functionality(x)))

        elif name_string == "structural tautology":
            rl_lst.append(generate_structural_tautology(x))
            rl_nl.append(convert_structural_tautology(generate_structural_tautology(x)))

        results_dict.setdefault(name_string, []).append((x, rl_lst[-1], rl_nl[-1]))

    # Sort results_dict by unique name_strings
    sorted_results_dict = dict(sorted(results_dict.items()))

    return sorted_results_dict
    print(sorted_results_dict['subclass'])

    # Add all items to final_list
    for name_string, items in sorted_results_dict.items():
        for item in items:
            final_list.append(item)

    return final_list


def reorganize_keys(final_dict):
    return_dict = {}

    for k, v in final_dict.items():
        axiom_names = [x[0] for x in v]
        axiom_manchester = [x[1] for x in v]
        axiom_natural_language = [x[2] for x in v]

        for index, n in enumerate(axiom_names):
            return_dict.setdefault(n, {}).setdefault('axiom', []).append(k)
            return_dict.setdefault(n, {}).setdefault('manchester', []).append(axiom_manchester[index])
            return_dict.setdefault(n, {}).setdefault('natural_language', []).append( axiom_natural_language[index])

    return return_dict

def write_file(class_name, class_values, print_list = ['manchester']):

    with open(f'{class_name}_axioms.md', 'w') as file:
        for k,dictvals in class_values.items():
            file.write(f"# {k}\n")

            for ax_index, ax_value in enumerate(dictvals['axiom']):
                file.write(f"{ax_value}: ")

                if 'manchester' in print_list:
                    file.write(f"{dictvals['manchester'][ax_index]}\n")
                    file.write("\n")

                if 'natural_language' in print_list:
                    file.write(f"{dictvals['natural_language'][ax_index]}\n")
                    file.write("\n")


if __name__ == "__main__":

    type_value = "graphrag"

    if type_value == "graphrag":

        sd = [
            "Place sfWithin Place",
            "Place sfContains Place",
            "Place sfTouches Place",
            "Place sfOverlaps Place",
            "Place sfIntersects Place",
            "Place hasPlaceType PlaceType",
            "Place impactedBy HazardEvent",
            "HazardEvent hasImpacted Place",
            "HazardEvent hasHazardType HazardType",
            "HazardEvent isOfFireType FireType"
        ]

        sr = [
            "Place sfWithin Place",
            "Place sfContains Place",
            "Place sfTouches Place",
            "Place sfOverlaps Place",
            "Place sfIntersects Place",
            "Place hasPlaceType PlaceType",
            "Place impactedBy HazardEvent",
            "HazardEvent hasImpacted Place",
            "HazardEvent hasHazardType HazardType",
            "HazardEvent isOfFireType FireType",
            "Place averageMonthlyTemperatureInCelsius integer",
            "Place maximumMonthlyTemperatureInCelsius integer",
            "Place minimumMonthlyTemperatureInCelsius integer",
            "Place averageCoolingDegreeDaysPerMonth integer",
            "Place averageHeatingDegreeDaysPerMonth integer",
            "Place percentObese nonNegativeInteger",
            "Place percentBelowPovertyLine nonNegativeInteger",
            "Place percentDiabetic nonNegativeInteger",
            "Place hasPopulation nonNegativeInteger",
            "Place hasNumberOfHouseHolds nonNegativeInteger",
            "Place numberOfFiresImpactingPlace nonNegativeInteger",
            "Place dollarDamageOfFiresImpactingPlace nonNegativeInteger",
            "Place numberOfHurricanesImpactingPlace nonNegativeInteger",
            "Place dollarDamageOfHurricanesImpactingPlace nonNegativeInteger",
            "Place numberOfEarthquakesImpactingPlace nonNegativeInteger",
            "Place numberOfTornadoesImpactingPlace nonNegativeInteger",
            "Place dollarDamageOfTornadoesImpactingPlace nonNegativeInteger",
            "Place numberOfStormSurgesImpactingPlace nonNegativeInteger",
            "Place dollarDamageOfStormSurgesImpactingPlace nonNegativeInteger",
            "Place numberOfFloodsImpactingPlace nonNegativeInteger",
            "Place dollarDamageOfFloodsImpactingPlace nonNegativeInteger",
            "Place numberOfLandslidesImpactingPlace nonNegativeInteger",
            "Place dollarDamageOfLandslidesImpactingPlace nonNegativeInteger",
            "Place hasName string",
            "Place hasKWGEntity anyURI",
            "HazardEvent hasName string",
            "HazardEvent hasKWGEntity anyURI",
            "HazardEvent hasStartDate date",
            "HazardEvent hasEndDate date",
            "HazardEvent affectedAreaInAcres nonNegativeInteger",
            "HazardEvent numberOfDeaths nonNegativeInteger",
            "HazardEvent damageToInfrastructureInDollars nonNegativeInteger",
            "HazardEvent damageToCropsInDollars nonNegativeInteger"
        ]

        gr = [
            "Place hasPlaceType PlaceType"
        ]

        # check these two: hasPlaceType is "scoped qualified existential" --> "qualified scoped functionality" and "existential"?
        qsf = [
            "Place hasPlaceType PlaceType"
        ]

        ex = [
            "Place hasPlaceType PlaceType"
        ]

        flist = {}
        # flist = convert_run_all(sc, "subclass", flist)
        # flist = convert_run_all(dis, "disjoint", flist)
        # flist = convert_run_all(gd, "global domain", flist)
        flist = convert_run_all(sd, "scoped domain", flist)
        flist = convert_run_all(gr, "global range", flist)
        flist = convert_run_all(sr, "scoped range", flist)
        flist = convert_run_all(ex, "existential", flist)
        # flist = convert_run_all(iex, "inverse existential", flist)
        # flist = convert_run_all(fun, "functionality", flist)
        # flist = convert_run_all(qfun, "qualified functionality", flist)
        # flist = convert_run_all(sf, "scoped functionality", flist)
        flist = convert_run_all(qsf, "qualified scoped functionality", flist)
        # flist = convert_run_all(ifun, "inverse functionality", flist)
        # flist = convert_run_all(iqf, "inverse qualified functionality", flist)
        # flist = convert_run_all(isf, "inverse scoped functionality", flist)
        # flist = convert_run_all(iqsf, "inverse qualified scoped functionality", flist)
        # flist = convert_run_all(st, "structural tautology", flist)

        flist = reorganize_keys(flist)

        write_file(type_value, class_values = flist, print_list = ['manchester'])
        

    elif type_value == "health":

        sc = [
            "MentalHealth SubClassOf Health",
            "MentalHealthStatus SubClassOf Status",
            "PhysicalHealth SubClassOf Health",
            "PhysicalHealthStatus SubClassOf Status",
            "Disease SubClassOf Health"]



        dis = [
            "Health hasHealthRecord HealthRecord",
            "Health hasHealthCondition HealthCondition",
            "Health hasSymptom Symptom",
            "Disease hasSymptom Symptom",
            "Symptom hasSeverity Severity",
            "Disease hasTreatment Treatment",
            "Treatment includesService Service",
            "Treatment affects Health",
            "Health hasStatus Status",
            "PhysicalHealth hasStatus PhysicalHealthStatus",
            "MentalHealth hasStatus MentalHealthStatus",
            "Patient hasHealth Health",
            "Health isAssociatedWith Visit",
            "Patient recieves Treatment"
        ]

        gd = [
            "Health hasHealthRecord HealthRecord",
            "Health hasHealthCondition HealthCondition",
            "Symptom hasSeverity Severity",
            "Disease hasTreatment Treatment",
            "Treatment includesService Service",
            "Patient hasHealth Health",
            "Patient recieves Treatment"
        ]


        sd = [
            "Health hasHealthRecord HealthRecord",
            "Health hasHealthCondition HealthCondition",
            "Health hasSymptom Symptom",
            "Disease hasSymptom Symptom",
            "Symptom hasSeverity Severity",
            "Disease hasTreatment Treatment",
            "Treatment includesService Service",
            "Treatment affects Health",
            "Health hasStatus Status",
            "PhysicalHealth hasStatus PhysicalHealthStatus",
            "MentalHealth hasStatus MentalHealthStatus",
            "Patient hasHealth Health",
            "Patient recieves Treatment"
        ]

        gr = [
            "Health hasHealthRecord HealthRecord",
            "Health hasHealthCondition HealthCondition",
            "Symptom hasSeverity Severity",
            "Disease hasTreatment Treatment",
            "Treatment includesService Service",
            "Patient hasHealth Health",
            "Health isAssociatedWith Visit",
            "Patient recieves Treatment"
        ]

        sr = [
            "Health hasHealthRecord HealthRecord",
            "Health hasHealthCondition HealthCondition",
            "Health hasSymptom Symptom",
            "Disease hasSymptom Symptom",
            "Symptom hasSeverity Severity",
            "Disease hasTreatment Treatment",
            "Treatment includesService Service",
            "Treatment affects Health",
            "Health hasStatus Status",
            "PhysicalHealth hasStatus PhysicalHealthStatus",
            "MentalHealth hasStatus MentalHealthStatus",
            "Patient hasHealth Health",
            "Patient recieves Treatment"
        ]


        ex = [
            "Health hasHealthRecord HealthRecord",
            "Health hasHealthCondition HealthCondition",
            "Health hasSymptom Symptom",
            "Disease hasSymptom Symptom",
            "Symptom hasSeverity Severity",
            "Disease hasTreatment Treatment",
            "Treatment includesService Service",
            "Treatment affects Health",
            "Health hasStatus Status",
            "PhysicalHealth hasStatus PhysicalHealthStatus",
            "MentalHealth hasStatus MentalHealthStatus",
            "Patient hasHealth Health",
            "Health isAssociatedWith Visit",
            "Patient recieves Treatment"
        ]


        iex = [
            "Health hasHealthRecord HealthRecord",
            "Health hasHealthCondition HealthCondition",
            "Symptom hasSeverity Severity",
            "Disease hasTreatment Treatment",
            "Treatment includesService Service",
            "Health hasStatus Status",
            "PhysicalHealth hasStatus PhysicalHealthStatus",
            "MentalHealth hasStatus MentalHealthStatus",
            "Patient hasHealth Health",
            "Health isAssociatedWith Visit",
        ]


        fun = [
            "Symptom hasSeverity Severity",
            "Treatment affects Health",
            "Patient hasHealth Health",
        ]

        qfun = [
            "Symptom hasSeverity Severity",
            "Treatment affects Health",
            "Patient hasHealth Health",
        ]


        sf = [
            "Symptom hasSeverity Severity",
            "Treatment affects Health",
            "Patient hasHealth Health",
        ]


        qsf = [
            "Symptom hasSeverity Severity",
            "Treatment affects Health",
            "PhysicalHealth hasStatus PhysicalHealthStatus",
            "MentalHealth hasStatus MentalHealthStatus",
        ]

        ifun = [
            "Symptom hasSeverity Severity",
            "Treatment affects Health",
        ]

        iqf = [
            "Symptom hasSeverity Severity",
            "Treatment affects Health",
        ]


        isf = [
            "Symptom hasSeverity Severity",
            "Health hasStatus Status",
            "PhysicalHealth hasStatus PhysicalHealthStatus",
            "MentalHealth hasStatus MentalHealthStatus",
            "Patient hasHealth Health",
            "Health isAssociatedWith Visit"
        ]

        iqsf = [
            "Symptom hasSeverity Severity",
            "PhysicalHealth hasStatus PhysicalHealthStatus",
            "MentalHealth hasStatus MentalHealthStatus",
            "Patient hasHealth Health",
            "Health isAssociatedWith Visit",
        ]

        st = [
            "Health hasHealthCondition HealthCondition",
            "Health hasSymptom Symptom",
            "Disease hasSymptom Symptom",
            "Disease hasTreatment Treatment",
            "Treatment includesService Service",
            "Treatment affects Health",
            "Health hasStatus Status",
            "MentalHealth hasStatus MentalHealthStatus",
            "Patient recieves Treatment"]

        flist = {}

        flist = convert_run_all(sc, "subclass", flist)
        flist = convert_run_all(dis, "disjoint", flist)
        flist = convert_run_all(gd, "global domain", flist)
        flist = convert_run_all(sd, "scoped domain", flist)
        flist = convert_run_all(gr, "global range", flist)
        flist = convert_run_all(sr, "scoped range", flist)
        flist = convert_run_all(ex, "existential", flist)
        flist = convert_run_all(iex, "inverse existential", flist)
        flist = convert_run_all(fun, "functionality", flist)
        flist = convert_run_all(qfun, "qualified functionality", flist)
        flist = convert_run_all(sf, "scoped functionality", flist)
        flist = convert_run_all(qsf, "qualified scoped functionality", flist)
        flist = convert_run_all(ifun, "inverse functionality", flist)
        flist = convert_run_all(iqf, "inverse qualified functionality", flist)
        flist = convert_run_all(isf, "inverse scoped functionality", flist)
        flist = convert_run_all(iqsf, "inverse qualified scoped functionality", flist)
        flist = convert_run_all(st, "structural tautology", flist)



        flist = reorganize_keys(flist)

        write_file('health', class_values = flist, print_list = ['manchester'])






    elif type_value == "drug":
        dis = [
            "patient isAdministered Dosage",
            "Dosage hasDosageStrength DosageStrength",
            "Dosage hasDosageForm DosageForm",
            "Dosage hasQuantity Quantity",
            "Drug hasDosage Dosage",
            "Drug hasRouteOfAdministration RouteOfAdministration",
            "Drug affects Body",
            "Drug affects Health",
            "Drug hasSideEffect SideEffect",
            "SideEffect affects Health",
            "Drug hasName DrugName",
            "Drug hasDrugClass DrugClass"
        ]


        gd = [
            "Drug hasDosage Dosage",
            "Drug hasRouteOfAdministration RouteOfAdministration",
            "patient isAdministered Dosage",
            "Dosage hasDosageStrength DosageStrength",
            "Drug hasSideEffect SideEffect",
            "Dosage hasDosageForm DosageForm",
            "Drug hasName DrugName",
            "Drug hasDrugClass DrugClass"
        ]



        sd = [
            "patient isAdministered Dosage",
            "Dosage hasDosageStrength DosageStrength",
            "Dosage hasDosageForm DosageForm",
            "Drug hasDosage Dosage",
            "Drug hasRouteOfAdministration RouteOfAdministration",
            "Drug hasName DrugName",
            "Drug hasDrugClass DrugClass"
        ]


        gr = [
            "Dosage hasDosageStrength DosageStrength",
            "Dosage hasDosageForm DosageForm",
            "Drug hasDosage Dosage",
            "Drug hasRouteOfAdministration RouteOfAdministration",
            "Drug hasDrugName DrugName",
            "Drug hasDrugClass DrugClass"
        ]


        sr = [
            "Dosage hasDosageStrength DosageStrength",
            "Dosage hasDosageForm DosageForm",
            "Drug hasDosage Dosage",
            "Drug hasRouteOfAdministration RouteOfAdministration",
            "Drug affects Body_or_Health",
            "Drug hasSideEffect SideEffect",
            "Drug hasDrugName DrugName",
            "Drug hasDrugClass DrugClass",
            "SideEffect affects Health",
            "Dosage hasQuantity Quantity"
        ]

        ex = [
            "Dosage hasQuantity Quantity",
            "Dosage hasDosageStrength DosageStrength",
            "Dosage hasDosageForm DosageForm",
            "Drug hasDosage Dosage",
            "Drug hasRouteOfAdministration RouteOfAdministration",
            "Drug hasDrugName DrugName",
            "Drug hasDrugClass DrugClass",
            "Drug affects Body",
            "Drug affects Health",
            "Drug hasSideEffect SideEffect",
            "SideEffect affects Health"
        ]

        iex = [
            "patient isAdministered Dosage",
            "Dosage hasDosageStrength DosageStrength",
            "Dosage hasDosageForm DosageForm",
            "Drug hasDosage Dosage",
            "Drug hasDrugName DrugName",
            "Drug hasDrugClass DrugClass",
            "Drug hasRouteOfAdministration RouteOfAdministration"
        ]

        st = [
            "patient isAdministered Dosage",
            "Dosage hasDosageStrength DosageStrength",
            "Dosage hasDosageForm DosageForm",
            "Dosage hasQuantity Quantity",
            "Drug hasDosage Dosage",
            "Drug hasRouteOfAdministration RouteOfAdministration",
            "Drug affects Body_or_Health",
            "Drug hasSideEffect SideEffect",
            "SideEffect affects Health",
            "Drug hasDrugName DrugName",
            "Drug hasDrugClass DrugClass"]


        flist = {}

        flist = convert_run_all(dis, "disjoint", flist)
        flist = convert_run_all(gd, "global domain", flist)
        flist = convert_run_all(sd, "scoped domain", flist)
        flist = convert_run_all(gr, "global range", flist)
        flist = convert_run_all(sr, "scoped range", flist)
        flist = convert_run_all(ex, "existential", flist)
        flist = convert_run_all(iex, "inverse existential", flist)
        flist = convert_run_all(st, "structural tautology", flist)

        flist = reorganize_keys(flist)

        write_file('drug', class_values = flist, print_list = ['manchester'])
    
    
    elif type_value == "imaging":

        sc = []

        dis = [
            "Labs-Imaging assesses Body",
            "Labs-Imaging hasContrast Contrast",
            "Labs-Imaging hasLabsImagingResult Labs-ImagingResult",
            "Labs-Imaging hasLabsImagingType Labs-ImagingType",
            "Labs-ImagingType createdByEquipment Equipment",
            "Visit leadsTo Labs-Imaging"]


        gd = [
            "Labs-Imaging hasContrast Contrast",
            "Labs-Imaging hasLabsImagingResult Labs-ImagingResult",
            "Labs-Imaging hasLabsImagingType Labs-ImagingType",
            "Labs-ImagingType createdByEquipment Equipment"]

        sd = [
            "Labs-Imaging assesses Body",
            "Labs-Imaging hasContrast Contrast",
            "Labs-Imaging hasLabsImagingResult Labs-ImagingResult",
            "Labs-Imaging hasLabsImagingType Labs-ImagingType",
            "Labs-ImagingType createdByEquipment Equipment"]



        gr = [
            "Labs-Imaging hasContrast Contrast",
            "Labs-Imaging hasLabsImagingResult Labs-ImagingResult",
            "Labs-Imaging hasLabsImagingType Labs-ImagingType",
            "Labs-ImagingType createdByEquipment Equipment",
            ]

        sr = [
            "Labs-Imaging hasContrast Contrast",
            "Labs-Imaging hasLabsImagingResult Labs-ImagingResult",
            "Labs-Imaging hasLabsImagingType Labs-ImagingType",
            "Labs-ImagingType createdByEquipment Equipment"]


        ex = [
            "Labs-Imaging assesses Body",
            "Labs-Imaging hasLabsImagingResult Labs-ImagingResult",
            "Labs-Imaging hasLabsImagingType Labs-ImagingType",]


        iex = [
            "Labs-Imaging hasContrast Contrast",
            "Labs-Imaging hasLabsImagingResult Labs-ImagingResult",
            "Labs-Imaging hasLabsImagingType Labs-ImagingType",
            "Labs-ImagingType createdByEquipment Equipment",
            "Visit leadsTo Labs-Imaging"
        ]

        fun = [
            "Labs-Imaging assesses Body",
            "Labs-Imaging hasContrast Contrast",
            "Labs-Imaging hasLabsImagingResult Labs-ImagingResult",
            "Labs-Imaging hasLabsImagingType Labs-ImagingType",
            "Labs-ImagingType createdByEquipment Equipment",
            ]

        qfun = [
            "Labs-Imaging assesses Body",
            "Labs-Imaging hasContrast Contrast",
            "Labs-Imaging hasLabsImagingResult Labs-ImagingResult",
            "Labs-Imaging hasLabsImagingType Labs-ImagingType",
        ]

        sf = [
            "Labs-Imaging hasContrast Contrast",
            "Labs-ImagingType createdByEquipment Equipment",
        ]

        qsf = [
            "Labs-Imaging hasContrast Contrast",
            "Labs-Imaging hasLabsImagingResult Labs-ImagingResult",
            "Labs-Imaging hasLabsImagingType Labs-ImagingType",
        ]

        ifun = [
            "Labs-Imaging assesses Body",
            "Labs-Imaging hasContrast Contrast",
            "Labs-Imaging hasLabsImagingResult Labs-ImagingResult",
            "Labs-Imaging hasLabsImagingType Labs-ImagingType",
            "Labs-ImagingType createdByEquipment Equipment",
        ]

        iqf = [
            "Labs-Imaging hasContrast Contrast",
            "Labs-Imaging hasLabsImagingResult Labs-ImagingResult",
            "Labs-Imaging hasLabsImagingType Labs-ImagingType"]

        isf = [

            "Labs-ImagingType createdByEquipment Equipment",
            "Labs-Imaging hasLabsImagingType Labs-ImagingType",
            "Labs-Imaging hasResult Labs-ImagingResult",
            "Labs-Imaging hasContrast Contrast",
            "Labs-Imaging assesses Body",
            "Visit leadsTo Labs-Imaging"
        ]

        iqsf = [
            "Labs-ImagingType createdByEquipment Equipment",
            "Labs-Imaging hasLabsImagingType Labs-ImagingType",
            "Labs-Imaging hasResult Result",
            "Labs-Imaging hasContrast Contrast",
            "Labs-Imaging assesses Body",
            "Visit leadsTo Labs-Imaging"]

        st = [
            "Labs-Imaging hasContrast Contrast",
            "Labs-Imaging hasResult Result",
            "Labs-Imaging hasType Type",
            "Type hasEquipment Equipment",
            "Labs-Imaging assesses Body"]


        flist = {}

        flist = convert_run_all(sc, "subclass", flist)
        flist = convert_run_all(dis, "disjoint", flist)
        flist = convert_run_all(gd, "global domain", flist)
        flist = convert_run_all(sd, "scoped domain", flist)
        flist = convert_run_all(gr, "global range", flist)
        flist = convert_run_all(sr, "scoped range", flist)
        flist = convert_run_all(ex, "existential", flist)
        flist = convert_run_all(iex, "inverse existential", flist)
        flist = convert_run_all(fun, "functionality", flist)
        flist = convert_run_all(qfun, "qualified functionality", flist)
        flist = convert_run_all(sf, "scoped functionality", flist)
        flist = convert_run_all(qsf, "qualified scoped functionality", flist)
        flist = convert_run_all(ifun, "inverse functionality", flist)
        flist = convert_run_all(iqf, "inverse qualified functionality", flist)
        flist = convert_run_all(isf, "inverse scoped functionality", flist)
        flist = convert_run_all(iqsf, "inverse qualified scoped functionality", flist)
        flist = convert_run_all(st, "structural tautology", flist)

        flist = reorganize_keys(flist)

        write_file('labs-imaging', class_values = flist, print_list = ['manchester'])


    elif type_value == "visit":

        sc = [
            'Visit SubClassOf Event',
            'DischargeID SubClassOf Identifier']
            
        dis = [
            "Visit hasDischargeID DischargeID",
            "Visit hasOutcome Outcome",
            "Visit hasTemporalExtent TemporalExtent",
            "Visit leadsTo Labs/Imaging",
            "Patient hasVisit Visit",
            "Health isAssociatedWith Visit",
            "Gender isAssociatedWith Visit",
            "Ethnicity isAssociatedWith Visit",
            "Race isAssociatedWith Visit",
            "Age isAssociatedWith Visit",
            "PatientType isAssociatedWith Visit",
            "PriorityOfAdmission isAssociatedWith Visit",
            "Diagnosis isAssociatedWith Visit"
        ]

        gd = [
            "Patient hasVisit Visit"]

        sd = [
            "Visit leadsTo Labs-Imaging",
            "Patient hasVisit Visit"
           ]

        gr = [
            "Visit hasDischargeID DischargeID",
            "Visit hasOutcome Outcome",
            "Visit hasTemporalExtent TemporalExtent",
            "Patient hasVisit Visit"
            ]

        sr = [
            "Visit hasDischargeID DischargeID",
            "Visit hasOutcome Outcome",
            "Visit hasTemporalExtent TemporalExtent",
            "Patient hasVisit Visit",
            "Health isAssociatedWith Visit",
            "Gender isAssociatedWith Visit",
            "Ethnicity isAssociatedWith Visit",
            "Race isAssociatedWith Visit",
            "Age isAssociatedWith Visit",
            "PatientType isAssociatedWith Visit",
            "PriorityOfAdmission isAssociatedWith Visit",
            "Diagnosis isAssociatedWith Visit"
            ]


        ex = [       
            "Visit hasDischargeID DischargeID",
            "Visit hasOutcome Outcome",
            "Visit hasTemporalExtent TemporalExtent",
            "Patient hasVisit Visit",
            "Health isAssociatedWith Visit",
            "Gender isAssociatedWith Visit",
            "Ethnicity isAssociatedWith Visit",
            "Race isAssociatedWith Visit",
            "Age isAssociatedWith Visit",
            "PatientType isAssociatedWith Visit",
            "PriorityOfAdmission isAssociatedWith Visit",
            "Diagnosis isAssociatedWith Visit"
        ]


        iex = [
            "Visit hasDischargeID DischargeID",
            "Visit hasOutcome Outcome",
            "Patient hasVisit Visit"
        ]

        fun = [ 
            "Visit hasDischargeID DischargeID",
            "Visit hasOutcome Outcome",
            "Visit hasTemporalExtent TemporalExtent",
            ]


        qfun = [
            "Visit hasDischargeID DischargeID",    
            "Visit hasOutcome Outcome",
            "Visit hasTemporalExtent TemporalExtent"]

        sf = [
            "Visit hasDischargeID DischargeID",
            "Visit hasOutcome Outcome",
            "Visit hasTemporalExtent TemporalExtent"]


        qsf = [
            "Visit hasDischargeID DischargeID",
            "Visit hasOutcome Outcome",
            "Visit hasTemporalExtent TemporalExtent",]

        ifun = [
            "Visit hasDischargeID DischargeID",
            "Visit hasOutcome Outcome",
            "Visit hasTemporalExtent TemporalExtent",
            "Visit leadsTo Labs/Imaging",
            "Patient hasVisit Visit",]


        iqf = [
            "Visit hasDischargeID DischargeID",
            "Visit hasOutcome Outcome",
            "Visit hasTemporalExtent TemporalExtent",
            "Visit leadsTo Labs/Imaging",
            "Patient hasVisit Visit"]


        isf = [
            "Visit hasDischargeID DischargeID",
            "Visit hasOutcome Outcome",
            "Visit hasTemporalExtent TemporalExtent",
            "Visit leadsTo Labs/Imaging",
            "Patient hasVisit Visit"]

        iqsf = [
            "Visit hasDischargeID DischargeID",
            "Visit hasOutcome Outcome",
            "Visit hasTemporalExtent TemporalExtent",
            "Visit leadsTo Labs/Imaging",
            "Patient hasVisit Visit"]


        st = [
            "Visit SubClassOf Event",
            "DischargeID SubClassOf Identifier",
            "Visit hasDischargeID DischargeID",
            "Visit hasOutcome Outcome",
            "Visit hasTemporalExtent TemporalExtent",
            "Visit leadsTo Labs/Imaging",
            "Patient hasVisit Visit",
            "Health isAssociatedWith Visit",
            "Gender isAssociatedWith Visit",
            "Ethnicity isAssociatedWith Visit",
            "Race isAssociatedWith Visit",
            "Age isAssociatedWith Visit",
            "PatientType isAssociatedWith Visit",
            "PriorityOfAdmission isAssociatedWith Visit",
            "Diagnosis isAssociatedWith Visit",
        ]

        flist = {}

        flist = convert_run_all(sc, "subclass", flist)
        flist = convert_run_all(dis, "disjoint", flist)
        flist = convert_run_all(gd, "global domain", flist)
        flist = convert_run_all(sd, "scoped domain", flist)
        flist = convert_run_all(gr, "global range", flist)
        flist = convert_run_all(sr, "scoped range", flist)
        flist = convert_run_all(ex, "existential", flist)
        flist = convert_run_all(iex, "inverse existential", flist)
        flist = convert_run_all(fun, "functionality", flist)
        flist = convert_run_all(qfun, "qualified functionality", flist)
        flist = convert_run_all(sf, "scoped functionality", flist)
        flist = convert_run_all(qsf, "qualified scoped functionality", flist)
        flist = convert_run_all(ifun, "inverse functionality", flist)
        flist = convert_run_all(iqf, "inverse qualified functionality", flist)
        flist = convert_run_all(isf, "inverse scoped functionality", flist)
        flist = convert_run_all(iqsf, "inverse qualified scoped functionality", flist)
        flist = convert_run_all(st, "structural tautology", flist)

        flist = reorganize_keys(flist)

        write_file('visit', class_values = flist, print_list = ['manchester'])

    elif type_value == "diagnosis":

        sc = []

        dis = [
            "Diagnosis hasPrincipalDiagnosis PrincipalDiagnosis",
            "Diagnosis hasDiagnosisTypes DiagnosisTypes",
            "Diagnosis identifies Disease",
            "Diagnosis affects Body",
            "Diagnosis isAssociatedWith Visit",
            "Patient hasDiagnosis Diagnosis",
            "Treatment treatmentFor Diagnosis"
        ]

        gd = [
            "Diagnosis hasPrincipalDiagnosis PrincipalDiagnosis",
            "Diagnosis hasDiagnosisTypes DiagnosisTypes",
            "Diagnosis identifies Disease",
            "Patient hasDiagnosis Diagnosis",
            "Treatment treatmentFor Diagnosis"
        ]

        sd = [
            "Diagnosis hasPrincipalDiagnosis PrincipalDiagnosis",
            "Diagnosis hasDiagnosisTypes DiagnosisTypes",
            "Diagnosis identifies Disease",
            "Patient hasDiagnosis Diagnosis",
            "Treatment treatmentFor Diagnosis"
        ]
        
        gr = [
            "Diagnosis hasPrincipalDiagnosis PrincipalDiagnosis",
            "Diagnosis hasDiagnosisTypes DiagnosisTypes",
            "Patient hasDiagnosis Diagnosis"
        ]

        sr = [
            "Diagnosis hasPrincipalDiagnosis PrincipalDiagnosis",
            "Diagnosis hasDiagnosisTypes DiagnosisTypes",
            "Diagnosis identifies Disease",
            "Diagnosis affects Body",
            "Diagnosis isAssociatedWith Visit",
            "Patient hasDiagnosis Diagnosis",
        ]

        ex = [
            "Diagnosis hasPrincipalDiagnosis PrincipalDiagnosis",
            "Diagnosis hasDiagnosisTypes DiagnosisTypes",
            "Diagnosis identifies Disease",
            "Diagnosis affects Body",
            "Diagnosis isAssociatedWith Visit",
            "Patient hasDiagnosis Diagnosis",
            "Treatment treatmentFor Diagnosis"
        ]

        iex = [
            "Diagnosis hasPrincipalDiagnosis PrincipalDiagnosis",
            "Diagnosis hasDiagnosisTypes DiagnosisTypes",
            "Patient hasDiagnosis Diagnosis",
        ]

        fun = [
            "Diagnosis hasPrincipalDiagnosis PrincipalDiagnosis",
        ]

        qfun = [
            "Diagnosis hasPrincipalDiagnosis PrincipalDiagnosis",
        ]

        sf = [
            "Diagnosis hasPrincipalDiagnosis PrincipalDiagnosis",
        ]

        qsf = [
            "Diagnosis hasPrincipalDiagnosis PrincipalDiagnosis",
        ]

        ifun = [
            "Diagnosis hasPrincipalDiagnosis PrincipalDiagnosis",
        ]

        iqf = [
            "Diagnosis hasPrincipalDiagnosis PrincipalDiagnosis",
        ]

        isf = [
            "Diagnosis hasPrincipalDiagnosis PrincipalDiagnosis",
        ]


        iqsf = [
            "Diagnosis hasPrincipalDiagnosis PrincipalDiagnosis",
        ]

        st = [
            "Diagnosis hasPrincipalDiagnosis PrincipalDiagnosis",
            "Diagnosis hasDiagnosisTypes DiagnosisTypes",
            "Diagnosis identifies Disease",
            "Diagnosis affects Body",
            "Diagnosis isAssociatedWith Visit",
            "Patient hasDiagnosis Diagnosis",
            "Treatment treatmentFor Diagnosis"
        ]

        flist = {}

        flist = convert_run_all(sc, "subclass", flist)
        flist = convert_run_all(dis, "disjoint", flist)
        flist = convert_run_all(gd, "global domain", flist)
        flist = convert_run_all(sd, "scoped domain", flist)
        flist = convert_run_all(gr, "global range", flist)
        flist = convert_run_all(sr, "scoped range", flist)
        flist = convert_run_all(ex, "existential", flist)
        flist = convert_run_all(iex, "inverse existential", flist)
        flist = convert_run_all(fun, "functionality", flist)
        flist = convert_run_all(qfun, "qualified functionality", flist)
        flist = convert_run_all(sf, "scoped functionality", flist)
        flist = convert_run_all(qsf, "qualified scoped functionality", flist)
        flist = convert_run_all(ifun, "inverse functionality", flist)
        flist = convert_run_all(iqf, "inverse qualified functionality", flist)
        flist = convert_run_all(isf, "inverse scoped functionality", flist)
        flist = convert_run_all(iqsf, "inverse qualified scoped functionality", flist)
        flist = convert_run_all(st, "structural tautology", flist)

        flist = reorganize_keys(flist)

        write_file('diagnosis', class_values = flist, print_list = ['manchester'])

    elif type_value == "temporal_extent":

        sc = [
            "TimeInterval SubClassOf ComplexTemporalExtent",
            "PointInTime SubClassOf ComplexTemporalExtent",
            "DischargeDate SubClassOf PointInTime",
            "DateOfStay SubClassOf PointInTime"
        ]

        dis = [
            "Visit hasTemporalExtent TemporalExtent",
            "TemporalExtent contains ComplexTemporalExtent",
            "TimeInterval startsFrom PointInTime",
            "TimeInterval endsAt PointInTime"
        ]

        gd = [
            "TimeInterval startsFrom PointInTime",
            "TimeInterval endsAt PointInTime"
        ]

        sd = [
            "TemporalExtent contains ComplexTemporalExtent",
            "TimeInterval startsFrom PointInTime",
            "TimeInterval endsAt PointInTime"
        ]
        gr = [
            "Visit hasTemporalExtent TemporalExtent",
            "TimeInterval startsFrom PointInTime",
            "TimeInterval endsAt PointInTime"
        ]

        sr = [
            "Visit hasTemporalExtent TemporalExtent",
            "TemporalExtent contains ComplexTemporalExtent",
            "TimeInterval startsFrom PointInTime",
            "TimeInterval endsAt PointInTime"
        ]

        ex = [
            "Visit hasTemporalExtent TemporalExtent",
            "TemporalExtent contains ComplexTemporalExtent",
            "TimeInterval startsFrom PointInTime",
            "TimeInterval endsAt PointInTime"
        ]

        iex = [
            "TemporalExtent contains ComplexTemporalExtent"
        ]

        fun = [
            "Visit hasTemporalExtent TemporalExtent",
            "TimeInterval startsFrom PointInTime",
            "TimeInterval endsAt PointInTime"
        ]

        qfun = [
            "Visit hasTemporalExtent TemporalExtent",
            "TemporalExtent contains ComplexTemporalExtent",
            "TimeInterval startsFrom PointInTime",
            "TimeInterval endsAt PointInTime"
        ]

        sf = [
            "Visit hasTemporalExtent TemporalExtent",
            "TemporalExtent contains ComplexTemporalExtent",
            "TimeInterval startsFrom PointInTime",
            "TimeInterval endsAt PointInTime"
        ]

        qsf = [
            "Visit hasTemporalExtent TemporalExtent",
            "TemporalExtent contains ComplexTemporalExtent",
            "TimeInterval startsFrom PointInTime",
            "TimeInterval endsAt PointInTime"
        ]

        ifun = [
            "Visit hasTemporalExtent TemporalExtent",
        ]

        iqf = [
            "Visit hasTemporalExtent TemporalExtent",
        ]

        isf = [
            "Visit hasTemporalExtent TemporalExtent",
            "TemporalExtent contains ComplexTemporalExtent",
        ]

        iqsf = [
            "Visit hasTemporalExtent TemporalExtent",
            "TemporalExtent contains ComplexTemporalExtent",
        ]

        st = [
            "TimeInterval SubClassOf ComplexTemporalExtent",
            "PointInTime SubClassOf ComplexTemporalExtent",
            "DischargeDate SubClassOf PointInTime",
            "DateOfStay SubClassOf PointInTime",
            "Visit hasTemporalExtent TemporalExtent",
            "TemporalExtent contains ComplexTemporalExtent",
            "TimeInterval startsFrom PointInTime",
            "TimeInterval endsAt PointInTime"
        ]

        flist = {}
        flist = convert_run_all(sc, "subclass", flist)
        flist = convert_run_all(dis, "disjoint", flist)
        flist = convert_run_all(gd, "global domain", flist)
        flist = convert_run_all(sd, "scoped domain", flist)
        flist = convert_run_all(gr, "global range", flist)
        flist = convert_run_all(sr, "scoped range", flist)
        flist = convert_run_all(ex, "existential", flist)
        flist = convert_run_all(iex, "inverse existential", flist)
        flist = convert_run_all(fun, "functionality", flist)
        flist = convert_run_all(qfun, "qualified functionality", flist)
        flist = convert_run_all(sf, "scoped functionality", flist)
        flist = convert_run_all(qsf, "qualified scoped functionality", flist)
        flist = convert_run_all(ifun, "inverse functionality", flist)
        flist = convert_run_all(iqf, "inverse qualified functionality", flist)
        flist = convert_run_all(isf, "inverse scoped functionality", flist)
        flist = convert_run_all(iqsf, "inverse qualified scoped functionality", flist)
        flist = convert_run_all(st, "structural tautology", flist)

        flist = reorganize_keys(flist)

        write_file(type_value, class_values = flist, print_list = ['manchester'])


