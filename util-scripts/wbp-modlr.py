sco = "SubClassOf:"
thing = "owl:Thing"

nen = """
wb:Item(Agent) hasName xsd:string
hasName recordedAt Item(Event)
hasName nameStructure Item(NameStructure)
hasName	isDirectlyBasedOn	Reference
wb:Item(Agent) hasSex Item(SexType)
hasSex recordedAt Item(Event)
hasSex isDirectlyBasedOn Reference
wb:Item(Agent) hasOccupation Item(Occupation)
hasOccupation	recordedAt Item(Event)
hasOccupation	isDirectlyBasedOn	Reference
wb:Item(Agent) hasAgeCategory Item(AgeCategory)
hasAgeCategory hasAge xsd:int
hasAgeCategory isDirectlyBasedOn Reference
wb:Item(Agent) hasAge	xsd:int
hasAge hasAgeCategory wb:Item(AgeCategory)
hasAge isDirectlyBasedOn Reference
wb:Item(Agent) participatesIn	Item(Event)
participatesIn recordedAt	Item(Event)
participatesIn hasTemporalExtent Item(TemporalExtent)
participatesIn isDirectlyBasedOn Reference
participatesIn hasParticipationRoleType	Item(ParticipationRoleCV)
wb:Item(Agent)	hasInterAgentRelationship	Item(Agent)
hasInterAgentRelationship	recordedAt Item(Event)
hasInterAgentRelationship	isDirectlyBasedOn	Reference
hasInterAgentRelationship	hasInterAgentRelationshipType	Item(InterAgentRelationshipCV)
"""
nen = nen.replace("\t", " ")
# Data Properties
# Agent hasAge xsd:int
# Agent hasName xsd:string


def with_prefix(prefix, value):
    return f"{prefix}{value}" if ':' not in value else value


lines = [line.strip() for line in nen.split("\n") if line != ""]
for line in lines:
    sub, propName, obj = line.split()
    # print(f"p:{propName} some (ps:{propName} some wd:{obj}) {sco} wd:{sub}\n")
    print(f"{with_prefix('p:', propName)} some ({with_prefix('ps:', propName)} some {with_prefix('wd:', obj)}) {sco} {with_prefix('wd:', sub)}")
    # print(f"wdt:{propName} some wd:{obj} {sco} wd:{sub}\n")
    print(f"{with_prefix('wdt:', propName)} some {with_prefix('wd:', obj)} {sco} {with_prefix('wd:', sub)}")
    # print(f"wd:{sub} {sco} wdt:{propName} only wd:{obj}\n")
    print(f"{with_prefix('wd:', sub)} {sco} {with_prefix('wdt:', propName)} only {with_prefix('wd:', obj)}")
