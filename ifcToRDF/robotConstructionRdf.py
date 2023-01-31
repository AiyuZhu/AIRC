import pandas as pd
import ifcopenshell
import ifcopenshell.util.element

from rdflib import Graph, Literal, URIRef, Namespace
# rdflib knows about quite a few popular namespaces, like W3C ontologies, schema.org etc.
from rdflib.namespace import XSD, RDF

# show all column
pd.set_option('display.max_columns', None)


models = ifcopenshell.open('test/test_model.ifc')
df = pd.read_csv('test/ConstructionPlan.csv')

# Create a Graph
g = Graph()

BOT = Namespace("https://w3id.org/bot#")
DICE = Namespace("https://w3id.org/digitalconstruction/Entities#")


INST = Namespace("http://www.w3.org/2002/07/owl#Ontology")

g.bind('bot', BOT)
g.bind('dice', DICE)
g.bind('inst', INST)


# match ifc and csv by guid
for element in models.by_type('IfcFooting'):
    info = element.get_info()
    # print(info)
    # Create an RDF URI node to use as the subject for multiple triples
    c_inst = URIRef("http://www.w3.org/2002/07/owl#Ontology/" + info['type'] + '_' + str(info['id']))
    # generate instance for component
    g.add((c_inst, BOT.hasGuid, Literal(info['GlobalId'])))
    g.add((c_inst, RDF.type, BOT.Element))
    # print(df.loc[df['Guid'] == info['GlobalId']])
    activities = df.loc[df['Guid'] == info['GlobalId']]
    # add component construction order
    g.add((c_inst, DICE.hasLabel, Literal(str(activities['Conmponent_sequence_id'][0]))))
    # print(activities['Activity_instance'])
    for row in activities.iterrows():
        # print(row[1])
        # print(row[1]['Activity_instance'])
        # print(row[1]['Date'])
        # print(row[1]['Start_time'])
        # print(row[1]['End_time'])
        activity_inst = URIRef("http://www.w3.org/2002/07/owl#Ontology/"+row[1]['Activity_instance'])
        g.add((c_inst, DICE.hasActivity, activity_inst))
        g.add((activity_inst, DICE.isActivityOf, c_inst))
        g.add((activity_inst, DICE.hasLabel, Literal(str(row[1]['Construction_sequence_id']))))
        g.add((activity_inst, RDF.type, DICE.Activity))
        g.add((activity_inst, DICE.hasStart, Literal(row[1]['Start_time'])))
        g.add((activity_inst, DICE.hasEnd, Literal(row[1]['End_time'])))
        g.add((activity_inst, DICE.hasSpatialPosition, Literal(row[1]['Target_point'])))


print(g.serialize(format='ttl'))