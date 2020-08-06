from onshape_client.client import Client 
from onshape_client.oas import (
    BTMParameterString149,
    BTMSketch151,
    BTMSketchConstraint2,
    BTMSketchCurveSegment155,
    BTMIndividualQuery138,
    BTMParameterQueryList148,
    BTMSketchPoint158,
    BTCurveGeometryLine117,
    BTMSketchCurve4,
    BTCurveGeometryCircle115,
    BTMIndividualSketchRegionQuery140,
    BTMIndividualQueryBase139
)
import json
from onshape_client.oas.models.bt_feature_definition_call1406 import (
    BTFeatureDefinitionCall1406,
)
from onshape_client.onshape_url import OnshapeElement
from onshape_client.oas.models.bt_id_translation_params import BTIdTranslationParams
from onshape_client.oas.models.btm_feature134 import BTMFeature134
from onshape_client.oas.models.btm_parameter_enum145 import BTMParameterEnum145
from onshape_client.oas.models.btm_parameter_quantity147 import BTMParameterQuantity147
from onshape_client.client import Client 
from onshape_client.oas import BTCopyDocumentParams, BTDocumentSearchParams

element = OnshapeElement(
	'https://rogers.onshape.com/documents/b7c65d78bde731408815188e/w/09daa8ec5418b4d1e583d4b3/e/96d39b57bfcc8cca0d96c2b5'
)

key = ""
secret = ""

with open('../scripts/api-key', "r") as f: 
	key = f.readline().rstrip()
	secret = f.readline().rstrip()

base_url = 'https://rogers.onshape.com'

client = Client(configuration={"base_url": base_url, "access_key": key, "secret_key": secret})


Square0 = BTMSketch151(entities=[BTMSketchCurveSegment155(start_point_id="LINE1.start", end_point_id="LINE1.end", start_param=0.0, end_param=1.0, geometry=BTCurveGeometryLine117(pnt_x=0.0, pnt_y=0.0, dir_x=0.0, dir_y=0.0254, bt_type="BTCurveGeometryLine-117"), entity_id="LINE1", bt_type="BTMSketchCurveSegment-155"),BTMSketchCurveSegment155(start_point_id="LINE2.start", end_point_id="LINE2.end", start_param=0.0, end_param=1.0, geometry=BTCurveGeometryLine117(pnt_x=0.0, pnt_y=0.0254, dir_x=0.0254, dir_y=0.0, bt_type="BTCurveGeometryLine-117"), entity_id="LINE2", bt_type="BTMSketchCurveSegment-155"),BTMSketchCurveSegment155(start_point_id="LINE3.start", end_point_id="LINE3.end", start_param=0.0, end_param=1.0, geometry=BTCurveGeometryLine117(pnt_x=0.0254, pnt_y=0.0254, dir_x=0.0, dir_y=-0.0254, bt_type="BTCurveGeometryLine-117"), entity_id="LINE3", bt_type="BTMSketchCurveSegment-155"),BTMSketchCurveSegment155(start_point_id="LINE4.start", end_point_id="LINE4.end", start_param=0.0, end_param=1.0, geometry=BTCurveGeometryLine117(pnt_x=0.0254, pnt_y=0.0, dir_x=-0.0254, dir_y=0.0, bt_type="BTCurveGeometryLine-117"), entity_id="LINE4", bt_type="BTMSketchCurveSegment-155"),], name="Square", parameters=[BTMParameterQueryList148(parameter_id="sketchPlane", queries=[BTMIndividualQuery138(deterministic_ids=['JDC'])]),BTMParameterQuantity147(expression="1*in", parameter_id="length", bt_type="BTMParameterQuantity-147"),], constraints=[BTMSketchConstraint2(constraint_type="COINCIDENT",parameters=[BTMParameterString149(value="point1", parameter_id="localFirst", bt_type="BTMParameterString-149"),BTMParameterString149(value="'LINE1.start", parameter_id="localSecond", bt_type="BTMParameterString-149"),],entity_id="constrainId",bt_type="BTMSketchConstraint-2"),BTMSketchConstraint2(constraint_type="LENGTH",parameters=[BTMParameterString149(value="point1", parameter_id="localFirst", bt_type="BTMParameterString-149"),BTMParameterString149(value="'LINE1.start", parameter_id="localSecond", bt_type="BTMParameterString-149"),BTMParameterQuantity147(expression="1*in", parameter_id="length", bt_type="BTMParameterQuantity-147"),],entity_id="constrainId",bt_type="BTMSketchConstraint-2"),], bt_type="BTMSketch-151")

Square_Extrude1 = BTMFeature134(bt_type="BTMFeature-134", name="Square Extrude", feature_type="extrude", parameters=[BTMParameterEnum145(enum_name="ToolBodyType",value="SURFACE",parameter_id="bodyType"),BTMParameterEnum145(enum_name="OperationDomain",value="MODEL",parameter_id="domain"),BTMParameterEnum145(enum_name="SecondDirectionBoundingType",value="BLIND",parameter_id="secondDirectionBound"),BTMParameterEnum145(enum_name="BoundingType",value="BLIND",parameter_id="endBound"),BTMParameterQueryList148(parameter_id="endBoundEntityFace", queries=[]),BTMParameterQueryList148(parameter_id="endBoundEntityBody", queries=[]),BTMParameterQueryList148(parameter_id="endBoundEntityVertex", queries=[]),BTMParameterEnum145(enum_name="NewBodyOperationType",value="NEW",parameter_id="operationType"),BTMParameterEnum145(enum_name="NewSurfaceOperationType",value="NEW",parameter_id="surfaceOperationType"),BTMParameterEnum145(enum_name="FlatOperationType",value="REMOVE",parameter_id="flatOperationType"),BTMParameterQueryList148(parameter_id="surfaceEntities", queries=[BTMIndividualQuery138(deterministic_ids=['JGC'])]),BTMParameterQuantity147(expression="1*in",parameter_id="depth"),])

Circle_On_a_Face2 = BTMSketch151(entities=[BTMSketchCurve4(center_id="Circle.center", entity_id="Circle", geometry=BTCurveGeometryCircle115(radius=0.00635, xcenter=0.0127, ycenter=0.0127, xdir=0.0127, ydir=0.0, clockwise=False)),], name="Circle On a Face", parameters=[BTMParameterQueryList148(parameter_id="sketchPlane", queries=[BTMIndividualQuery138(deterministic_ids=['JGC'])]),], constraints=[], bt_type="BTMSketch-151")

Extrude_Remove_Circle3 = BTMFeature134(bt_type="BTMFeature-134", name="Extrude Remove Circle", feature_type="extrude", parameters=[BTMParameterEnum145(enum_name="OperationDomain",value="MODEL",parameter_id="domain"),BTMParameterEnum145(enum_name="ToolBodyType",value="SOLID",parameter_id="bodyType"),BTMParameterEnum145(enum_name="NewBodyOperationType",value="REMOVE",parameter_id="operationType"),BTMParameterEnum145(enum_name="BoundingType",value="BLIND",parameter_id="endBound"),BTMParameterQueryList148(parameter_id="booleanScope", queries=[BTMIndividualQuery138(deterministic_ids=['JHD'])]),BTMParameterQueryList148(parameter_id="booleanSurfaceScope", queries=[]),BTMParameterQuantity147(expression="1 in",parameter_id="offsetDistance"),BTMParameterQuantity147(expression="1 in",parameter_id="secondDirectionDepth"),BTMParameterQueryList148(parameter_id="surfaceEntities", queries=[]),BTMParameterEnum145(enum_name="NewSurfaceOperationType",value="NEW",parameter_id="surfaceOperationType"),BTMParameterEnum145(enum_name="FlatOperationType",value="REMOVE",parameter_id="flatOperationType"),BTMParameterQueryList148(parameter_id="entities", queries=[BTMIndividualQuery138(deterministic_ids=['JJC'])]),BTMParameterQuantity147(expression="1 in",parameter_id="depth"),])


def funcTester(func_string, part_studio, client):
	feature_definition = BTFeatureDefinitionCall1406(feature=func_string)
	client.part_studios_api.add_part_studio_feature(
	    did=part_studio.did,
	    wvm=part_studio.wvm,
	    wvmid=part_studio.wvmid,
	    eid=part_studio.eid,
	    bt_feature_definition_call_1406=feature_definition,
	    _preload_content=False,
	) 
funcTester(Square0, element, client)
funcTester(Square_Extrude1, element, client)
funcTester(Circle_On_a_Face2, element, client)
funcTester(Extrude_Remove_Circle3, element, client)
