# kwgl-ont:Place kwgl-ont:hasPlaceType kwgl-ont:PlaceType
existential: `kwgl-ont:Place SubClassOf kwgl-ont:hasPlaceType some kwgl-ont:PlaceType`

global range: `owl:Thing SubClassOf kwgl-ont:hasPlaceType only kwgl-ont:PlaceType`

qualified scoped functionality: `kwgl-ont:Place SubClassOf kwgl-ont:hasPlaceType max 1 kwgl-ont:PlaceType`

scoped domain: `kwgl-ont:hasPlaceType some kwgl-ont:PlaceType SubClassOf kwgl-ont:Place`

scoped range: `kwgl-ont:Place SubClassOf kwgl-ont:hasPlaceType some kwgl-ont:PlaceType`

# kwgl-ont:Place kwgl-ont:sfWithin kwgl-ont:Place
scoped domain: `kwgl-ont:sfWithin some kwgl-ont:Place SubClassOf kwgl-ont:Place`

scoped range: `kwgl-ont:Place SubClassOf kwgl-ont:sfWithin some kwgl-ont:Place`

# kwgl-ont:Place kwgl-ont:sfContains kwgl-ont:Place
scoped domain: `kwgl-ont:sfContains some kwgl-ont:Place SubClassOf kwgl-ont:Place`

scoped range: `kwgl-ont:Place SubClassOf kwgl-ont:sfContains some kwgl-ont:Place`

# kwgl-ont:Place kwgl-ont:sfTouches kwgl-ont:Place
scoped domain: `kwgl-ont:sfTouches some kwgl-ont:Place SubClassOf kwgl-ont:Place`

scoped range: `kwgl-ont:Place SubClassOf kwgl-ont:sfTouches some kwgl-ont:Place`

# kwgl-ont:Place kwgl-ont:sfOverlaps kwgl-ont:Place
scoped domain: `kwgl-ont:sfOverlaps some kwgl-ont:Place SubClassOf kwgl-ont:Place`

scoped range: `kwgl-ont:Place SubClassOf kwgl-ont:sfOverlaps some kwgl-ont:Place`

# kwgl-ont:Place kwgl-ont:sfIntersects kwgl-ont:Place
scoped domain: `kwgl-ont:sfIntersects some kwgl-ont:Place SubClassOf kwgl-ont:Place`

scoped range: `kwgl-ont:Place SubClassOf kwgl-ont:sfIntersects some kwgl-ont:Place`

# kwgl-ont:Place kwgl-ont:impactedBy kwgl-ont:HazardEvent
scoped domain: `kwgl-ont:impactedBy some kwgl-ont:HazardEvent SubClassOf kwgl-ont:Place`

scoped range: `kwgl-ont:Place SubClassOf kwgl-ont:impactedBy some kwgl-ont:HazardEvent`

# kwgl-ont:HazardEvent kwgl-ont:hasImpacted kwgl-ont:Place
scoped domain: `kwgl-ont:hasImpacted some kwgl-ont:Place SubClassOf kwgl-ont:HazardEvent`

scoped range: `kwgl-ont:HazardEvent SubClassOf kwgl-ont:hasImpacted some kwgl-ont:Place`

# kwgl-ont:HazardEvent kwgl-ont:hasHazardType kwgl-ont:HazardType
scoped domain: `kwgl-ont:hasHazardType some kwgl-ont:HazardType SubClassOf kwgl-ont:HazardEvent`

scoped range: `kwgl-ont:HazardEvent SubClassOf kwgl-ont:hasHazardType some kwgl-ont:HazardType`

# kwgl-ont:HazardEvent kwgl-ont:isOfFireType kwgl-ont:FireType
scoped domain: `kwgl-ont:isOfFireType some kwgl-ont:FireType SubClassOf kwgl-ont:HazardEvent`

scoped range: `kwgl-ont:HazardEvent SubClassOf kwgl-ont:isOfFireType some kwgl-ont:FireType`

# kwgl-ont:Place kwgl-ont:averageMonthlyTemperatureInCelsius xsd:integer
scoped range: `kwgl-ont:Place SubClassOf kwgl-ont:averageMonthlyTemperatureInCelsius some xsd:integer`

# kwgl-ont:Place kwgl-ont:maximumMonthlyTemperatureInCelsius xsd:integer
scoped range: `kwgl-ont:Place SubClassOf kwgl-ont:maximumMonthlyTemperatureInCelsius some xsd:integer`

# kwgl-ont:Place kwgl-ont:minimumMonthlyTemperatureInCelsius xsd:integer
scoped range: `kwgl-ont:Place SubClassOf kwgl-ont:minimumMonthlyTemperatureInCelsius some xsd:integer`

# kwgl-ont:Place kwgl-ont:averageCoolingDegreeDaysPerMonth xsd:integer
scoped range: `kwgl-ont:Place SubClassOf kwgl-ont:averageCoolingDegreeDaysPerMonth some xsd:integer`

# kwgl-ont:Place kwgl-ont:averageHeatingDegreeDaysPerMonth xsd:integer
scoped range: `kwgl-ont:Place SubClassOf kwgl-ont:averageHeatingDegreeDaysPerMonth some xsd:integer`

# kwgl-ont:Place kwgl-ont:percentObese xsd:nonNegativeInteger
scoped range: `kwgl-ont:Place SubClassOf kwgl-ont:percentObese some xsd:nonNegativeInteger`

# kwgl-ont:Place kwgl-ont:percentBelowPovertyLine xsd:nonNegativeInteger
scoped range: `kwgl-ont:Place SubClassOf kwgl-ont:percentBelowPovertyLine some xsd:nonNegativeInteger`

# kwgl-ont:Place kwgl-ont:percentDiabetic xsd:nonNegativeInteger
scoped range: `kwgl-ont:Place SubClassOf kwgl-ont:percentDiabetic some xsd:nonNegativeInteger`

# kwgl-ont:Place kwgl-ont:hasPopulation xsd:nonNegativeInteger
scoped range: `kwgl-ont:Place SubClassOf kwgl-ont:hasPopulation some xsd:nonNegativeInteger`

# kwgl-ont:Place kwgl-ont:hasNumberOfHouseHolds xsd:nonNegativeInteger
scoped range: `kwgl-ont:Place SubClassOf kwgl-ont:hasNumberOfHouseHolds some xsd:nonNegativeInteger`

# kwgl-ont:Place kwgl-ont:numberOfFiresImpactingPlace xsd:nonNegativeInteger
scoped range: `kwgl-ont:Place SubClassOf kwgl-ont:numberOfFiresImpactingPlace some xsd:nonNegativeInteger`

# kwgl-ont:Place kwgl-ont:dollarDamageOfFiresImpactingPlace xsd:nonNegativeInteger
scoped range: `kwgl-ont:Place SubClassOf kwgl-ont:dollarDamageOfFiresImpactingPlace some xsd:nonNegativeInteger`

# kwgl-ont:Place kwgl-ont:numberOfHurricanesImpactingPlace xsd:nonNegativeInteger
scoped range: `kwgl-ont:Place SubClassOf kwgl-ont:numberOfHurricanesImpactingPlace some xsd:nonNegativeInteger`

# kwgl-ont:Place kwgl-ont:dollarDamageOfHurricanesImpactingPlace xsd:nonNegativeInteger
scoped range: `kwgl-ont:Place SubClassOf kwgl-ont:dollarDamageOfHurricanesImpactingPlace some xsd:nonNegativeInteger`

# kwgl-ont:Place kwgl-ont:numberOfEarthquakesImpactingPlace xsd:nonNegativeInteger
scoped range: `kwgl-ont:Place SubClassOf kwgl-ont:numberOfEarthquakesImpactingPlace some xsd:nonNegativeInteger`

# kwgl-ont:Place kwgl-ont:numberOfTornadoesImpactingPlace xsd:nonNegativeInteger
scoped range: `kwgl-ont:Place SubClassOf kwgl-ont:numberOfTornadoesImpactingPlace some xsd:nonNegativeInteger`

# kwgl-ont:Place kwgl-ont:dollarDamageOfTornadoesImpactingPlace xsd:nonNegativeInteger
scoped range: `kwgl-ont:Place SubClassOf kwgl-ont:dollarDamageOfTornadoesImpactingPlace some xsd:nonNegativeInteger`

# kwgl-ont:Place kwgl-ont:numberOfStormSurgesImpactingPlace xsd:nonNegativeInteger
scoped range: `kwgl-ont:Place SubClassOf kwgl-ont:numberOfStormSurgesImpactingPlace some xsd:nonNegativeInteger`

# kwgl-ont:Place kwgl-ont:dollarDamageOfStormSurgesImpactingPlace xsd:nonNegativeInteger
scoped range: `kwgl-ont:Place SubClassOf kwgl-ont:dollarDamageOfStormSurgesImpactingPlace some xsd:nonNegativeInteger`

# kwgl-ont:Place kwgl-ont:numberOfFloodsImpactingPlace xsd:nonNegativeInteger
scoped range: `kwgl-ont:Place SubClassOf kwgl-ont:numberOfFloodsImpactingPlace some xsd:nonNegativeInteger`

# kwgl-ont:Place kwgl-ont:dollarDamageOfFloodsImpactingPlace xsd:nonNegativeInteger
scoped range: `kwgl-ont:Place SubClassOf kwgl-ont:dollarDamageOfFloodsImpactingPlace some xsd:nonNegativeInteger`

# kwgl-ont:Place kwgl-ont:numberOfLandslidesImpactingPlace xsd:nonNegativeInteger
scoped range: `kwgl-ont:Place SubClassOf kwgl-ont:numberOfLandslidesImpactingPlace some xsd:nonNegativeInteger`

# kwgl-ont:Place kwgl-ont:dollarDamageOfLandslidesImpactingPlace xsd:nonNegativeInteger
scoped range: `kwgl-ont:Place SubClassOf kwgl-ont:dollarDamageOfLandslidesImpactingPlace some xsd:nonNegativeInteger`

# kwgl-ont:Place kwgl-ont:hasName xsd:string
scoped range: `kwgl-ont:Place SubClassOf kwgl-ont:hasName some xsd:string`

# kwgl-ont:Place kwgl-ont:hasKWGEntity xsd:anyURI
scoped range: `kwgl-ont:Place SubClassOf kwgl-ont:hasKWGEntity some xsd:anyURI`

# kwgl-ont:HazardEvent kwgl-ont:hasName xsd:string
scoped range: `kwgl-ont:HazardEvent SubClassOf kwgl-ont:hasName some xsd:string`

# kwgl-ont:HazardEvent kwgl-ont:hasKWGEntity xsd:anyURI
scoped range: `kwgl-ont:HazardEvent SubClassOf kwgl-ont:hasKWGEntity some xsd:anyURI`

# kwgl-ont:HazardEvent kwgl-ont:hasStartDate xsd:date
scoped range: `kwgl-ont:HazardEvent SubClassOf kwgl-ont:hasStartDate some xsd:date`

# kwgl-ont:HazardEvent kwgl-ont:hasEndDate xsd:date
scoped range: `kwgl-ont:HazardEvent SubClassOf kwgl-ont:hasEndDate some xsd:date`

# kwgl-ont:HazardEvent kwgl-ont:affectedAreaInAcres xsd:nonNegativeInteger
scoped range: `kwgl-ont:HazardEvent SubClassOf kwgl-ont:affectedAreaInAcres some xsd:nonNegativeInteger`

# kwgl-ont:HazardEvent kwgl-ont:numberOfDeaths xsd:nonNegativeInteger
scoped range: `kwgl-ont:HazardEvent SubClassOf kwgl-ont:numberOfDeaths some xsd:nonNegativeInteger`

# kwgl-ont:HazardEvent kwgl-ont:damageToInfrastructureInDollars xsd:nonNegativeInteger
scoped range: `kwgl-ont:HazardEvent SubClassOf kwgl-ont:damageToInfrastructureInDollars some xsd:nonNegativeInteger`

# kwgl-ont:HazardEvent kwgl-ont:damageToCropsInDollars xsd:nonNegativeInteger
scoped range: `kwgl-ont:HazardEvent SubClassOf kwgl-ont:damageToCropsInDollars some xsd:nonNegativeInteger`

