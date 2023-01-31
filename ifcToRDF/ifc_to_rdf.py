from rdflib import Graph, Literal, URIRef, Namespace
# rdflib knows about quite a few popular namespaces, like W3C ontologies, schema.org etc.
from rdflib.namespace import XSD, RDF

# Create a Graph
g = Graph()

BOT = Namespace("https://w3id.org/bot#")
DICE = Namespace("https://w3id.org/digitalconstruction/Entities#")

# Create an RDF URI node to use as the subject for multiple triples
INST = Namespace("http://www.w3.org/2002/07/owl#Ontology")

g.bind('bot', BOT)
g.bind('dice', DICE)
g.bind('inst', INST)


g.add((INST.comp_1, BOT.hasGuid, Literal("267VPU8AB9991QBA3MI1_A", datatype=XSD['string'])))
g.add((INST.comp_1, DICE.hasLabel, Literal("1", datatype=XSD['string'])))
g.add((INST.comp_1, RDF.type, BOT.Element))
g.add((INST.comp_1, RDF.type, DICE.ifc_element))
g.add((INST.comp_1, DICE.hasINST, INST.INST_1))


# g.add((INST.INST_1, BOT.hasGuid, Literal("267VPU8AB9991QBA3MI1_A", datatype=XSD['string'])))
g.add((INST.INST_1, RDF.type, DICE.INST))
g.add((INST.INST_1, DICE.isSubINSTOf, INST.comp_1))
g.add((INST.INST_1, DICE.hasStart, Literal('2022-11-10T08:00:00', datatype=XSD['dateTime'])))
g.add((INST.INST_1, DICE.hasEnd, Literal("2022-11-10T09:00:00", datatype=XSD['dateTime'])))
g.add((INST.INST_1, DICE.hasState, Literal("need construction", datatype=XSD['string'])))
g.add((INST.INST_1, DICE.hasState, Literal("need positioning for picking up", datatype=XSD['string'])))
g.add((INST.INST_1, DICE.hasState, Literal("need pick up", datatype=XSD['string'])))
g.add((INST.INST_1, DICE.hasState, Literal("need transfer to target", datatype=XSD['string'])))
g.add((INST.INST_1, DICE.hasState, Literal("need positioning for assembling", datatype=XSD['string'])))
g.add((INST.INST_1, DICE.hasState, Literal("need assembly", datatype=XSD['string'])))
g.add((INST.INST_1, DICE.hasState, Literal("constructed", datatype=XSD['string'])))
g.add((INST.INST_1, DICE.hasSubINST, INST.move_to_compoent))
g.add((INST.INST_1, DICE.hasSubINST, INST.position_for_picking))
g.add((INST.INST_1, DICE.hasSubINST, INST.pick))
g.add((INST.INST_1, DICE.hasSubINST, INST.transfer))
g.add((INST.INST_1, DICE.hasSubINST, INST.position_for_installing))
g.add((INST.INST_1, DICE.hasSubINST, INST.install))


# g.add((INST.move_to_compoent, BOT.hasGuid, Literal("90b511b9-b7c0-465c-8e11-4a4033666r78", datatype=XSD['string'])))
g.add((INST.move_to_compoent, DICE.hasLabel, Literal("1", datatype=XSD['string'])))
g.add((INST.move_to_compoent, RDF.type, DICE.INST))
g.add((INST.move_to_compoent, DICE.isSubINSTOf, INST.INST_1))
g.add((INST.move_to_compoent, DICE.hasStart, Literal('2022-11-10T08:00:00', datatype=XSD['dateTime'])))
g.add((INST.move_to_compoent, DICE.hasEnd, Literal("2022-11-10T09:00:00", datatype=XSD['dateTime'])))


# g.add((INST.position_for_picking, BOT.hasGuid, Literal("90b511b9-b7c0-465c-8e11-455133666r78", datatype=XSD['string'])))
g.add((INST.position_for_picking, DICE.hasLabel, Literal("2", datatype=XSD['string'])))
g.add((INST.position_for_picking, RDF.type, DICE.INST))
g.add((INST.position_for_picking, DICE.isSubINSTOf, INST.INST_1))
g.add((INST.position_for_picking, DICE.hasStart, Literal('2022-11-10T08:00:00', datatype=XSD['dateTime'])))
g.add((INST.position_for_picking, DICE.hasEnd, Literal("2022-11-10T09:00:00", datatype=XSD['dateTime'])))


# g.add((INST.pick, BOT.hasGuid, Literal("90b511b9-b7c0-465c-8e11-4a4037896r78", datatype=XSD['string'])))
g.add((INST.pick, DICE.hasLabel, Literal("3", datatype=XSD['string'])))
g.add((INST.pick, RDF.type, DICE.INST))
g.add((INST.pick, DICE.isSubINSTOf, INST.INST_1))
g.add((INST.pick, DICE.hasStart, Literal('2022-11-10T08:00:00', datatype=XSD['dateTime'])))
g.add((INST.pick, DICE.hasEnd, Literal("2022-11-10T09:00:00", datatype=XSD['dateTime'])))


# g.add((INST.transfer, BOT.hasGuid, Literal("90b511b9-b7c0-465c-8e11-4a40336653218", datatype=XSD['string'])))
g.add((INST.transfer, DICE.hasLabel, Literal("4", datatype=XSD['string'])))
g.add((INST.transfer, RDF.type, DICE.INST))
g.add((INST.transfer, DICE.isSubINSTOf, INST.INST_1))
g.add((INST.transfer, DICE.hasStart, Literal('2022-11-10T08:00:00', datatype=XSD['dateTime'])))
g.add((INST.transfer, DICE.hasEnd, Literal("2022-11-10T09:00:00", datatype=XSD['dateTime'])))


# g.add((INST.position_for_installing, BOT.hasGuid, Literal("90b511b9-b7c0-465c-8e11-10243666r78", datatype=XSD['string'])))
g.add((INST.position_for_installing, DICE.hasLabel, Literal("5", datatype=XSD['string'])))
g.add((INST.position_for_installing, RDF.type, DICE.INST))
g.add((INST.position_for_installing, DICE.isSubINSTOf, INST.INST_1))
g.add((INST.position_for_installing, DICE.hasStart, Literal('2022-11-10T08:00:00', datatype=XSD['dateTime'])))
g.add((INST.position_for_installing, DICE.hasEnd, Literal("2022-11-10T09:00:00", datatype=XSD['dateTime'])))


# g.add((INST.install, BOT.hasGuid, Literal("90b511b9-b7c0-465c-8e11-7781666r78", datatype=XSD['string'])))
g.add((INST.install, DICE.hasLabel, Literal("6", datatype=XSD['string'])))
g.add((INST.install, RDF.type, DICE.INST))
g.add((INST.install, DICE.isSubINSTOf, INST.INST_1))
g.add((INST.install, DICE.hasStart, Literal('2022-11-10T08:00:00', datatype=XSD['dateTime'])))
g.add((INST.install, DICE.hasEnd, Literal("2022-11-10T09:00:00", datatype=XSD['dateTime'])))


print(g.serialize(format='ttl'))



