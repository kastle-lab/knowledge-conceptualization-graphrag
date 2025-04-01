# Place hasPlaceType PlaceType
existential: `Place SubClassOf hasPlaceType some PlaceType`

global range: `owl:Thing SubClassOf hasPlaceType only PlaceType`

qualified scoped functionality: `Place SubClassOf hasPlaceType max 1 PlaceType`

scoped domain: `hasPlaceType some PlaceType SubClassOf Place`

scoped range: `Place SubClassOf hasPlaceType some PlaceType`

# Place sfWithin Place
scoped domain: `sfWithin some Place SubClassOf Place`

scoped range: `Place SubClassOf sfWithin some Place`

# Place sfContains Place
scoped domain: `sfContains some Place SubClassOf Place`

scoped range: `Place SubClassOf sfContains some Place`

# Place sfTouches Place
scoped domain: `sfTouches some Place SubClassOf Place`

scoped range: `Place SubClassOf sfTouches some Place`

# Place sfOverlaps Place
scoped domain: `sfOverlaps some Place SubClassOf Place`

scoped range: `Place SubClassOf sfOverlaps some Place`

# Place sfIntersects Place
scoped domain: `sfIntersects some Place SubClassOf Place`

scoped range: `Place SubClassOf sfIntersects some Place`

# Place impactedBy HazardEvent
scoped domain: `impactedBy some HazardEvent SubClassOf Place`

scoped range: `Place SubClassOf impactedBy some HazardEvent`

# HazardEvent hasImpacted Place
scoped domain: `hasImpacted some Place SubClassOf HazardEvent`

scoped range: `HazardEvent SubClassOf hasImpacted some Place`

# HazardEvent hasHazardType HazardType
scoped domain: `hasHazardType some HazardType SubClassOf HazardEvent`

scoped range: `HazardEvent SubClassOf hasHazardType some HazardType`

# HazardEvent isOfFireType FireType
scoped domain: `isOfFireType some FireType SubClassOf HazardEvent`

scoped range: `HazardEvent SubClassOf isOfFireType some FireType`

# Place averageMonthlyTemperatureInCelsius integer
scoped range: `Place SubClassOf averageMonthlyTemperatureInCelsius some integer`

# Place maximumMonthlyTemperatureInCelsius integer
scoped range: `Place SubClassOf maximumMonthlyTemperatureInCelsius some integer`

# Place minimumMonthlyTemperatureInCelsius integer
scoped range: `Place SubClassOf minimumMonthlyTemperatureInCelsius some integer`

# Place averageCoolingDegreeDaysPerMonth integer
scoped range: `Place SubClassOf averageCoolingDegreeDaysPerMonth some integer`

# Place averageHeatingDegreeDaysPerMonth integer
scoped range: `Place SubClassOf averageHeatingDegreeDaysPerMonth some integer`

# Place percentObese nonNegativeInteger
scoped range: `Place SubClassOf percentObese some nonNegativeInteger`

# Place percentBelowPovertyLine nonNegativeInteger
scoped range: `Place SubClassOf percentBelowPovertyLine some nonNegativeInteger`

# Place percentDiabetic nonNegativeInteger
scoped range: `Place SubClassOf percentDiabetic some nonNegativeInteger`

# Place hasPopulation nonNegativeInteger
scoped range: `Place SubClassOf hasPopulation some nonNegativeInteger`

# Place hasNumberOfHouseHolds nonNegativeInteger
scoped range: `Place SubClassOf hasNumberOfHouseHolds some nonNegativeInteger`

# Place numberOfFiresImpactingPlace nonNegativeInteger
scoped range: `Place SubClassOf numberOfFiresImpactingPlace some nonNegativeInteger`

# Place dollarDamageOfFiresImpactingPlace nonNegativeInteger
scoped range: `Place SubClassOf dollarDamageOfFiresImpactingPlace some nonNegativeInteger`

# Place numberOfHurricanesImpactingPlace nonNegativeInteger
scoped range: `Place SubClassOf numberOfHurricanesImpactingPlace some nonNegativeInteger`

# Place dollarDamageOfHurricanesImpactingPlace nonNegativeInteger
scoped range: `Place SubClassOf dollarDamageOfHurricanesImpactingPlace some nonNegativeInteger`

# Place numberOfEarthquakesImpactingPlace nonNegativeInteger
scoped range: `Place SubClassOf numberOfEarthquakesImpactingPlace some nonNegativeInteger`

# Place numberOfTornadoesImpactingPlace nonNegativeInteger
scoped range: `Place SubClassOf numberOfTornadoesImpactingPlace some nonNegativeInteger`

# Place dollarDamageOfTornadoesImpactingPlace nonNegativeInteger
scoped range: `Place SubClassOf dollarDamageOfTornadoesImpactingPlace some nonNegativeInteger`

# Place numberOfStormSurgesImpactingPlace nonNegativeInteger
scoped range: `Place SubClassOf numberOfStormSurgesImpactingPlace some nonNegativeInteger`

# Place dollarDamageOfStormSurgesImpactingPlace nonNegativeInteger
scoped range: `Place SubClassOf dollarDamageOfStormSurgesImpactingPlace some nonNegativeInteger`

# Place numberOfFloodsImpactingPlace nonNegativeInteger
scoped range: `Place SubClassOf numberOfFloodsImpactingPlace some nonNegativeInteger`

# Place dollarDamageOfFloodsImpactingPlace nonNegativeInteger
scoped range: `Place SubClassOf dollarDamageOfFloodsImpactingPlace some nonNegativeInteger`

# Place numberOfLandslidesImpactingPlace nonNegativeInteger
scoped range: `Place SubClassOf numberOfLandslidesImpactingPlace some nonNegativeInteger`

# Place dollarDamageOfLandslidesImpactingPlace nonNegativeInteger
scoped range: `Place SubClassOf dollarDamageOfLandslidesImpactingPlace some nonNegativeInteger`

# Place hasName string
scoped range: `Place SubClassOf hasName some string`

# Place hasKWGEntity anyURI
scoped range: `Place SubClassOf hasKWGEntity some anyURI`

# HazardEvent hasName string
scoped range: `HazardEvent SubClassOf hasName some string`

# HazardEvent hasKWGEntity anyURI
scoped range: `HazardEvent SubClassOf hasKWGEntity some anyURI`

# HazardEvent hasStartDate date
scoped range: `HazardEvent SubClassOf hasStartDate some date`

# HazardEvent hasEndDate date
scoped range: `HazardEvent SubClassOf hasEndDate some date`

# HazardEvent affectedAreaInAcres nonNegativeInteger
scoped range: `HazardEvent SubClassOf affectedAreaInAcres some nonNegativeInteger`

# HazardEvent numberOfDeaths nonNegativeInteger
scoped range: `HazardEvent SubClassOf numberOfDeaths some nonNegativeInteger`

# HazardEvent damageToInfrastructureInDollars nonNegativeInteger
scoped range: `HazardEvent SubClassOf damageToInfrastructureInDollars some nonNegativeInteger`

# HazardEvent damageToCropsInDollars nonNegativeInteger
scoped range: `HazardEvent SubClassOf damageToCropsInDollars some nonNegativeInteger`

