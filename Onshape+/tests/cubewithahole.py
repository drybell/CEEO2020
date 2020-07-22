
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
key = ""
secret = ""

with open('../scripts/api-key', "r") as f: 
	key = f.readline().rstrip()
	secret = f.readline().rstrip()

base_url = 'https://rogers.onshape.com'

client = Client(configuration={"base_url": base_url, "access_key": key, "secret_key": secret})

element = OnshapeElement(
        "https://rogers.onshape.com/documents/b7c65d78bde731408815188e/w/09daa8ec5418b4d1e583d4b3/e/fbca3f5c681a7618c9d7d895"
    )
# https://rogers.onshape.com/documents/b7c65d78bde731408815188e/w/09daa8ec5418b4d1e583d4b3/e/fbca3f5c681a7618c9d7d895

# result = client.part_studios_api.get_part_studio_features(
#         element.did, element.wvm, element.wvmid, element.eid
#     )
# print(result)

def create_square(client, part_studio):
    FEATURE_NAME = "Square"
    PLANE_ID = "JDC"  # The plane deterministic ID for the sketch
    plane_query = BTMParameterQueryList148(
        parameter_id="sketchPlane",
        queries=[BTMIndividualQuery138(deterministic_ids=[PLANE_ID])],
    )
    LINE_ID = "myLine"
    START = "start"
    END = "end"
    POINT_ID = "myPoint"

    point_string_param = BTMParameterString149(
        value='point1', parameter_id="localFirst", bt_type="BTMParameterString-149"
    )
    point_string_param2 = BTMParameterString149(
        value='point2', parameter_id="localFirst", bt_type="BTMParameterString-149"
    )
    point_string_param3 = BTMParameterString149(
        value='point3', parameter_id="localFirst", bt_type="BTMParameterString-149"
    )
    point_string_param4 = BTMParameterString149(
        value='point4', parameter_id="localFirst", bt_type="BTMParameterString-149"
    )
    line_end_string_param = BTMParameterString149(
        value=f"'LINE1.start",
        parameter_id="localSecond",
        bt_type="BTMParameterString-149",
    )
    line_end_string_param2 = BTMParameterString149(
        value=f"LINE2.start",
        parameter_id="localSecond",
        bt_type="BTMParameterString-149",
    )
    line_end_string_param3 = BTMParameterString149(
        value=f"LINE3.start",
        parameter_id="localSecond",
        bt_type="BTMParameterString-149",
    )
    line_end_string_param4 = BTMParameterString149(
        value=f"LINE4.start",
        parameter_id="localSecond",
        bt_type="BTMParameterString-149",
    )
    length = BTMParameterQuantity147(expression="1*in", parameter_id="length")
    coincident_constraint1 = BTMSketchConstraint2(
        constraint_type="COINCIDENT",
        parameters=[point_string_param, line_end_string_param],
        entity_id="constrainId",
        bt_type="BTMSketchConstraint-2",
    )
    coincident_constraint2 = BTMSketchConstraint2(
        constraint_type="LENGTH",
        parameters=[point_string_param, line_end_string_param, length],
        entity_id="constrainId",
        bt_type="BTMSketchConstraint-2",
    )
    point = BTMSketchPoint158(
        y=0.0, x=0.0, is_user_point=True, is_construction=False
    )
    point2 = BTMSketchPoint158(
        y=.0254, x=0.0, is_user_point=True, is_construction=False
    )
    point3 = BTMSketchPoint158(
        y=.0254, x=.0254, is_user_point=True, is_construction=False
    )
    point4 = BTMSketchPoint158(
        y=0.0, x=.0254, is_user_point=True, is_construction=False
    )
    line_geometry1 = BTCurveGeometryLine117(
        pnt_x=0.0, pnt_y=0.0, dir_x=0.0, dir_y=.0254, bt_type="BTCurveGeometryLine-117"
    )
    line_geometry2 = BTCurveGeometryLine117(
        pnt_x=0.0, pnt_y=.0254, dir_x=.0254, dir_y=0.0, bt_type="BTCurveGeometryLine-117"
    )
    line_geometry3 = BTCurveGeometryLine117(
        pnt_x=.0254, pnt_y=.0254, dir_x=0.0, dir_y=-.0254, bt_type="BTCurveGeometryLine-117"
    )
    line_geometry4 = BTCurveGeometryLine117(
        pnt_x=.0254, pnt_y=0.0, dir_x=-.0254, dir_y=0.0, bt_type="BTCurveGeometryLine-117"
    )
    line = BTMSketchCurveSegment155(
        start_point_id=f"LINE1.start",
        end_point_id=f"LINE1.end",
        start_param=0.0,
        end_param=1.0,
        geometry=line_geometry1,
        entity_id='LINE1',
        bt_type="BTMSketchCurveSegment-155",
    )
    line2 = BTMSketchCurveSegment155(
        start_point_id=f"LINE2.start",
        end_point_id=f"LINE2.end",
        start_param=0.0,
        end_param=1.0,
        geometry=line_geometry2,
        entity_id='LINE2',
        bt_type="BTMSketchCurveSegment-155",
    )
    line3 = BTMSketchCurveSegment155(
        start_point_id=f"LINE3.start",
        end_point_id=f"LINE3.end",
        start_param=0.0,
        end_param=1.0,
        geometry=line_geometry3,
        entity_id='LINE3',
        bt_type="BTMSketchCurveSegment-155",
    )
    line4 = BTMSketchCurveSegment155(
        start_point_id=f"LINE4.start",
        end_point_id=f"LINE4.end",
        start_param=0.0,
        end_param=1.0,
        geometry=line_geometry4,
        entity_id='LINE4',
        bt_type="BTMSketchCurveSegment-155",
    )
  
    sketch = BTMSketch151(
        entities=[line, line2, line3, line4],
        name="Square",
        parameters=[plane_query, length],
        constraints=[coincident_constraint1, coincident_constraint2],
        bt_type="BTMSketch-151",
    )
    feature_definition = BTFeatureDefinitionCall1406(feature=sketch)
    client.part_studios_api.add_part_studio_feature(
        did=part_studio.did,
        wvm=part_studio.wvm,
        wvmid=part_studio.wvmid,
        eid=part_studio.eid,
        bt_feature_definition_call_1406=feature_definition,
        _preload_content=False,
    )
    # features = client.part_studios_api.get_part_studio_features(
    #     did=part_studio.did,
    #     wvm=part_studio.wvm,
    #     wvmid=part_studio.wvmid,
    #     eid=part_studio.eid,
    #     _preload_content=False,
    # )
    # assert json.loads(features.data)["features"][0]["name"] == FEATURE_NAME


# 


def test_create_surface(client, part_studio):
    # square(client,part_studio)
    tool_body_type = BTMParameterEnum145(
        value="SURFACE", enum_name="ToolBodyType", parameter_id="bodyType"
    )
    operation_domain = BTMParameterEnum145(
        value="MODEL",
        enum_name="OperationDomain",
        parameter_id="domain",
    ) 
    toolbodytype = BTMParameterEnum145(
        value="NEW",
        enum_name="NewBodyOperationType",
        parameter_id="operationType",
    )
    operationtype = BTMParameterEnum145(
        value="NEW",
        enum_name="NewSurfaceOperationType",
        parameter_id="surfaceOperationType",
    )
    boundingtype = BTMParameterEnum145(
        value="BLIND",
        enum_name="BoundingType",
        parameter_id="endBound",
    )
    flat = BTMParameterEnum145(
        value="REMOVE",
        enum_name="FlatOperationType",
        parameter_id="flatOperationType",
    )
    blind = BTMParameterEnum145(
        value="BLIND",
        enum_name="SecondDirectionBoundingType",
        parameter_id="secondDirectionBound",
    )

    line_query = BTMParameterQueryList148(
        parameter_id="surfaceEntities",
        queries=[BTMIndividualQuery138(deterministic_ids=["JGC"])],
    )
    query2 = BTMParameterQueryList148(
        parameter_id="endBoundEntityFace",
        queries=[],
    )
    query3 = BTMParameterQueryList148(
        parameter_id="endBoundEntityBody",
        queries=[],
    )
    query4 = BTMParameterQueryList148(
        parameter_id="endBoundEntityVertex",
        queries=[],
    )
    
    length = BTMParameterQuantity147(expression="1*in", parameter_id="depth")
    extrude_feature = BTMFeature134(
        bt_type="BTMFeature-134",
        name="Square Extrude",
        feature_type="extrude",
        parameters=[tool_body_type, operation_domain, 
        			blind, boundingtype, query2, query3, query4,
        			toolbodytype, operationtype, flat, line_query, length],
    )
    feature_definition = BTFeatureDefinitionCall1406(feature=extrude_feature)
    client.part_studios_api.add_part_studio_feature(
        did=part_studio.did,
        wvm=part_studio.wvm,
        wvmid=part_studio.wvmid,
        eid=part_studio.eid,
        bt_feature_definition_call_1406=feature_definition,
        _preload_content=False,
    )

def extrude_remove_circle(client, part_studio):
    # square(client,part_studio)
    tool_body_type = BTMParameterEnum145(
        value="SURFACE", enum_name="ToolBodyType", parameter_id="bodyType"
    )
    operation_domain = BTMParameterEnum145(
        value="MODEL",
        enum_name="OperationDomain",
        parameter_id="domain",
    ) 
    toolbodytype = BTMParameterEnum145(
        value="REMOVE",
        enum_name="NewBodyOperationType",
        parameter_id="operationType",
    )
    operationtype = BTMParameterEnum145(
        value="NEW",
        enum_name="NewSurfaceOperationType",
        parameter_id="surfaceOperationType",
    )
    boundingtype = BTMParameterEnum145(
        value="BLIND",
        enum_name="BoundingType",
        parameter_id="endBound",
    )
    flat = BTMParameterEnum145(
        value="REMOVE",
        enum_name="FlatOperationType",
        parameter_id="flatOperationType",
    )
    blind = BTMParameterEnum145(
        value="BLIND",
        enum_name="SecondDirectionBoundingType",
        parameter_id="secondDirectionBound",
    )

    line_query = BTMParameterQueryList148(
        parameter_id="surfaceEntities",
        queries=[BTMIndividualQuery138(deterministic_ids=["JJC"])],
    )
    query2 = BTMParameterQueryList148(
        parameter_id="endBoundEntityFace",
        queries=[],
    )
    query3 = BTMParameterQueryList148(
        parameter_id="endBoundEntityBody",
        queries=[],
    )
    query4 = BTMParameterQueryList148(
        parameter_id="endBoundEntityVertex",
        queries=[],
    )
    
    length = BTMParameterQuantity147(expression="1*in", parameter_id="depth")
    offset = BTMParameterQuantity147(expression="1 in", parameter_id="offsetDistance")
    ffset = BTMParameterQuantity147(expression="1 in", parameter_id="secondDirectionDepth")
    extrude_feature = BTMFeature134(
        bt_type="BTMFeature-134",
        name="Extrude Remove Circle",
        feature_type="extrude",
        parameters=[tool_body_type, operation_domain, 
        			blind, boundingtype, query2, query3, query4,
        			toolbodytype, operationtype, flat, line_query, length, offset],
    )
    feature_definition = BTFeatureDefinitionCall1406(feature=extrude_feature)
    client.part_studios_api.add_part_studio_feature(
        did=part_studio.did,
        wvm=part_studio.wvm,
        wvmid=part_studio.wvmid,
        eid=part_studio.eid,
        bt_feature_definition_call_1406=feature_definition,
        _preload_content=False,
    )

def test_create_circle(client, part_studio):
    FEATURE_NAME = "Circle On a Face"
    PLANE_ID = "JGC" # The plane deterministic ID for the sketch
    plane_query = BTMParameterQueryList148(parameter_id="sketchPlane", queries=[BTMIndividualQuery138(deterministic_ids=[PLANE_ID])])
    CIRCLE_ID = "Circle"

    circle_geometry = BTCurveGeometryCircle115(radius=0.00635, xcenter=0.0127, ycenter=0.0127, xdir=.0127, ydir=0.0, clockwise=False)
    circle = BTMSketchCurve4(center_id=f"{CIRCLE_ID}.center", entity_id=CIRCLE_ID, geometry=circle_geometry)
    sketch = BTMSketch151(entities=[circle], name=FEATURE_NAME, parameters=[plane_query])
    feature_definition = BTFeatureDefinitionCall1406(feature=sketch)
    client.part_studios_api.add_part_studio_feature(
        did=part_studio.did,
        wvm=part_studio.wvm,
        wvmid=part_studio.wvmid,
        eid=part_studio.eid,
        bt_feature_definition_call_1406=feature_definition,
        _preload_content=False,
    )


# create_square(client, element)
# test_create_surface(client, element)
# test_create_circle(client, element)
extrude_remove_circle(client, element)


print('Done')