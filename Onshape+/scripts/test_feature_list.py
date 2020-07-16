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
# self.drawings_api = api.DrawingsApi(api_client)
# self.documents_api = api.DocumentsApi(api_client)
# self.elements_api = api.ElementsApi(api_client)
# self.feature_studios_api = api.FeatureStudiosApi(api_client)
# self.metadata_api = api.MetadataApi(api_client)
# self.parts_api = api.PartsApi(api_client)
# self.part_studios_api = api.PartStudiosApi(api_client)


# element.assemblies                 element.drawings                   element.name                      
# element.base_url                   element.eid                        element.new_assembly(             
# element.configuration              element.element_type               element.optional_microversion     
# element.create(                    element.elements(                  element.original_url              
# element.create_drawing(            element.export_file(               element.part_studios              
# element.create_from_ids(           element.get_microversion_url(      element.poll(                     
# element.create_from_oas_models(    element.get_url(                   element.poll_translation_result(  
# element.default_workspace          element.import_file(               element.s_assembly_insert_message(
# element.delete(                    element.make_version(              element.wvm                       
# element.did                        element.mass_properties            element.wvmid                     
# element.DRAWING_DATA_TYPE          element.microversion       

with open("../scripts/api-key", "r") as f: 
    key = f.readline().rstrip()
    secret = f.readline().rstrip()

base_url = 'https://rogers.onshape.com'

headers = {'Accept': 'application/vnd.onshape.v1+json', 'Content-Type': 'application/json'}

client = Client(configuration={"base_url": base_url, "access_key": key, "secret_key": secret})

element = OnshapeElement(
        "https://rogers.onshape.com/documents/b7c65d78bde731408815188e/w/09daa8ec5418b4d1e583d4b3/e/d3ef40a634c6d4d599dd78e3"
    )

# doc = client.documents_api.create_document(
#         bt_document_params=BTCopyDocumentParams(
#             owner_type_index=1, new_name="Test Python Client", owner_id=""
#         )
#     )
# print(doc)
def test_insert_point_sketch(client, part_studio):
    PLANE_ID = "JDC"  # The plane deterministic ID for the sketch
    plane_query = BTMParameterQueryList148(
        parameter_id="sketchPlane",
        queries=[BTMIndividualQuery138(deterministic_ids=[PLANE_ID])],
    )
    point = BTMSketchPoint158(
        y=-0.071735, x=-0.0564367610245, is_user_point=True, is_construction=False
    )
    sketch = BTMSketch151(
        entities=[point], name="My New Point", parameters=[plane_query]
    )
    feature_definition = BTFeatureDefinitionCall1406(
        feature=sketch, bt_type="BTFeatureDefinitionCall-1406"
    )
    client.part_studios_api.add_part_studio_feature(
        did=part_studio.did,
        wvm=part_studio.wvm,
        wvmid=part_studio.wvmid,
        eid=part_studio.eid,
        bt_feature_definition_call_1406=feature_definition,
        _preload_content=False,
    )

def test_insert_line_sketch(client, part_studio):
    FEATURE_NAME = "My New Line"
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
        value=POINT_ID, parameter_id="localFirst", bt_type="BTMParameterString-149"
    )
    line_end_string_param = BTMParameterString149(
        value=f"{LINE_ID}.{START}",
        parameter_id="localSecond",
        bt_type="BTMParameterString-149",
    )
    coincident_constraint = BTMSketchConstraint2(
        constraint_type="COINCIDENT",
        parameters=[point_string_param, line_end_string_param],
        entity_id="constrainId",
        bt_type="BTMSketchConstraint-2",
    )
    point = BTMSketchPoint158(
        y=-0.071735,
        x=-0.0564367610245,
        entity_id=POINT_ID,
        bt_type="BTMSketchPoint-158",
    )
    line_geometry = BTCurveGeometryLine117(
        pnt_x=0.0, pnt_y=0.0, dir_x=0.5, dir_y=0.5, bt_type="BTCurveGeometryLine-117"
    )
    line = BTMSketchCurveSegment155(
        start_point_id=f"{LINE_ID}.{START}",
        end_point_id=f"{LINE_ID}.{END}",
        start_param=0.0,
        end_param=1.0,
        geometry=line_geometry,
        entity_id=LINE_ID,
        bt_type="BTMSketchCurveSegment-155",
    )
    sketch = BTMSketch151(
        entities=[line, point],
        name="My New Line",
        parameters=[plane_query],
        constraints=[coincident_constraint],
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
    features = client.part_studios_api.get_part_studio_features(
        did=part_studio.did,
        wvm=part_studio.wvm,
        wvmid=part_studio.wvmid,
        eid=part_studio.eid,
        _preload_content=False,
    )
    # assert json.loads(features.data)["features"][0]["name"] == FEATURE_NAME

def test_create_surface(client, part_studio):
    test_insert_line_sketch(client, part_studio)
    tool_body_type = BTMParameterEnum145(
        value="SURFACE", enum_name="ToolBodyType", parameter_id="bodyType"
    )
    operation_type = BTMParameterEnum145(
        value="NEW",
        enum_name="NewSurfaceOperationType",
        parameter_id="surfaceOperationType",
    )
    line_query = BTMParameterQueryList148(
        parameter_id="surfaceEntities",
        queries=[BTMIndividualQuery138(deterministic_ids=["JFB"])],
    )
    length = BTMParameterQuantity147(expression="3.03*in", parameter_id="depth")
    extrude_feature = BTMFeature134(
        bt_type="BTMFeature-134",
        name="My extrude",
        feature_type="extrude",
        parameters=[tool_body_type, operation_type, line_query, length],
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

result = client.part_studios_api.get_part_studio_features(
    element.did, element.wvm, element.wvmid, element.eid
)
print(result)
# result = test_create_surface(client, element)


def test_create_circle(client, part_studio):
    FEATURE_NAME = "My New Circle"
    PLANE_ID = "JDC"  # The plane deterministic ID for the sketch
    plane_query = BTMParameterQueryList148(
        parameter_id="sketchPlane",
        queries=[BTMIndividualQuery138(deterministic_ids=[PLANE_ID])],
    )
    CIRCLE_ID = "myCircle"

    circle_geometry = BTCurveGeometryCircle115(
        radius=0.5, xcenter=0.0, ycenter=0.0, xdir=1.0, ydir=0.0, clockwise=False
    )
    circle = BTMSketchCurve4(
        center_id=f"{CIRCLE_ID}.center", entity_id=CIRCLE_ID, geometry=circle_geometry
    )
    sketch = BTMSketch151(
        entities=[circle], name=FEATURE_NAME, parameters=[plane_query]
    )
    feature_definition = BTFeatureDefinitionCall1406(
        feature=sketch, bt_type="BTFeatureDefinitionCall-1406"
    )
    client.part_studios_api.add_part_studio_feature(
        did=part_studio.did,
        wvm=part_studio.wvm,
        wvmid=part_studio.wvmid,
        eid=part_studio.eid,
        bt_feature_definition_call_1406=feature_definition,
        _preload_content=False,
    )