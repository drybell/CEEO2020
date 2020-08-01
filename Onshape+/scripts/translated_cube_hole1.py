{
    "0": {
        "parameters": [
            {
                "BTMParameterQueryList-148": [
                    {
                        "deterministic_ids": [
                            "JDC"
                        ],
                        "parameter_id": "sketchPlane",
                        "bt_type": "BTMIndividualQuery138"
                    }
                ]
            },
            {
                "BTMParameterQuantity-147": {
                    "expression": "1*in",
                    "parameter_id": "length"
                }
            }
        ],
        "name": "Square",
        "bt_type": "BTMSketch151",
        "entities": [
            {
                "start_point_id": "LINE1.start",
                "end_point_id": "LINE1.end",
                "start_param": 0.0,
                "end_param": 1.0,
                "geometry": {
                    "pnt_x": 0.0,
                    "pnt_y": 0.0,
                    "dir_x": 0.0,
                    "dir_y": 0.0254,
                    "bt_type": "BTCurveGeometryLine-117"
                },
                "entity_id": "LINE1",
                "bt_type": "BTMSketchCurveSegment-155"
            },
            {
                "start_point_id": "LINE2.start",
                "end_point_id": "LINE2.end",
                "start_param": 0.0,
                "end_param": 1.0,
                "geometry": {
                    "pnt_x": 0.0,
                    "pnt_y": 0.0254,
                    "dir_x": 0.0254,
                    "dir_y": 0.0,
                    "bt_type": "BTCurveGeometryLine-117"
                },
                "entity_id": "LINE2",
                "bt_type": "BTMSketchCurveSegment-155"
            },
            {
                "start_point_id": "LINE3.start",
                "end_point_id": "LINE3.end",
                "start_param": 0.0,
                "end_param": 1.0,
                "geometry": {
                    "pnt_x": 0.0254,
                    "pnt_y": 0.0254,
                    "dir_x": 0.0,
                    "dir_y": -0.0254,
                    "bt_type": "BTCurveGeometryLine-117"
                },
                "entity_id": "LINE3",
                "bt_type": "BTMSketchCurveSegment-155"
            },
            {
                "start_point_id": "LINE4.start",
                "end_point_id": "LINE4.end",
                "start_param": 0.0,
                "end_param": 1.0,
                "geometry": {
                    "pnt_x": 0.0254,
                    "pnt_y": 0.0,
                    "dir_x": -0.0254,
                    "dir_y": 0.0,
                    "bt_type": "BTCurveGeometryLine-117"
                },
                "entity_id": "LINE4",
                "bt_type": "BTMSketchCurveSegment-155"
            }
        ],
        "constraints": [
            {
                "constraint_type": "COINCIDENT",
                "constraints": [
                    {
                        "value": "point1",
                        "parameter_id": "localFirst",
                        "bt_type": "BTMParameterString-149"
                    },
                    {
                        "value": "'LINE1.start",
                        "parameter_id": "localSecond",
                        "bt_type": "BTMParameterString-149"
                    }
                ],
                "entity_id": "constrainId",
                "bt_type": "BTMSketchConstraint-2"
            },
            {
                "constraint_type": "LENGTH",
                "constraints": [
                    {
                        "value": "point1",
                        "parameter_id": "localFirst",
                        "bt_type": "BTMParameterString-149"
                    },
                    {
                        "value": "'LINE1.start",
                        "parameter_id": "localSecond",
                        "bt_type": "BTMParameterString-149"
                    },
                    {
                        "expression": "1*in",
                        "parameter_id": "length",
                        "bt_type": "BTMParameterQuantity-147"
                    }
                ],
                "entity_id": "constrainId",
                "bt_type": "BTMSketchConstraint-2"
            }
        ]
    },
    "1": {
        "feature_type": "extrude",
        "name": "Square Extrude",
        "parameters": [
            {
                "BTMParameterEnum-145": {
                    "enum_name": "ToolBodyType",
                    "value": "SURFACE",
                    "parameter_id": "bodyType"
                }
            },
            {
                "BTMParameterEnum-145": {
                    "enum_name": "OperationDomain",
                    "value": "MODEL",
                    "parameter_id": "domain"
                }
            },
            {
                "BTMParameterEnum-145": {
                    "enum_name": "SecondDirectionBoundingType",
                    "value": "BLIND",
                    "parameter_id": "secondDirectionBound"
                }
            },
            {
                "BTMParameterEnum-145": {
                    "enum_name": "BoundingType",
                    "value": "BLIND",
                    "parameter_id": "endBound"
                }
            },
            {
                "BTMParameterQueryList-148": [
                    {
                        "parameter_id": "endBoundEntityFace"
                    }
                ]
            },
            {
                "BTMParameterQueryList-148": [
                    {
                        "parameter_id": "endBoundEntityBody"
                    }
                ]
            },
            {
                "BTMParameterQueryList-148": [
                    {
                        "parameter_id": "endBoundEntityVertex"
                    }
                ]
            },
            {
                "BTMParameterEnum-145": {
                    "enum_name": "NewBodyOperationType",
                    "value": "NEW",
                    "parameter_id": "operationType"
                }
            },
            {
                "BTMParameterEnum-145": {
                    "enum_name": "NewSurfaceOperationType",
                    "value": "NEW",
                    "parameter_id": "surfaceOperationType"
                }
            },
            {
                "BTMParameterEnum-145": {
                    "enum_name": "FlatOperationType",
                    "value": "REMOVE",
                    "parameter_id": "flatOperationType"
                }
            },
            {
                "BTMParameterQueryList-148": [
                    {
                        "deterministic_ids": [
                            "JGC"
                        ],
                        "parameter_id": "surfaceEntities",
                        "bt_type": "BTMIndividualQuery138"
                    }
                ]
            },
            {
                "BTMParameterQuantity-147": {
                    "expression": "1*in",
                    "parameter_id": "depth"
                }
            }
        ],
        "bt_type": "BTMFeature-134"
    },
    "2": {
        "parameters": [
            {
                "BTMParameterQueryList-148": [
                    {
                        "deterministic_ids": [
                            "JGC"
                        ],
                        "parameter_id": "sketchPlane",
                        "bt_type": "BTMIndividualQuery138"
                    }
                ]
            }
        ],
        "name": "Circle On a Face",
        "bt_type": "BTMSketch151",
        "entities": [
            {
                "geometry": {
                    "radius": 0.00635,
                    "x_center": 0.0127,
                    "y_center": 0.0127,
                    "x_dir": 0.0127,
                    "y_dir": 0.0,
                    "clockwise": false
                },
                "ids": {
                    "center_id": "Circle.center",
                    "entity_id": "Circle"
                },
                "bt_type": "BTCurveGeometryCircle115"
            }
        ],
        "constraints": []
    },
    "3": {
        "feature_type": "extrude",
        "name": "Extrude Remove Circle",
        "parameters": [
            {
                "BTMParameterEnum-145": {
                    "enum_name": "OperationDomain",
                    "value": "MODEL",
                    "parameter_id": "domain"
                }
            },
            {
                "BTMParameterEnum-145": {
                    "enum_name": "ToolBodyType",
                    "value": "SOLID",
                    "parameter_id": "bodyType"
                }
            },
            {
                "BTMParameterEnum-145": {
                    "enum_name": "NewBodyOperationType",
                    "value": "REMOVE",
                    "parameter_id": "operationType"
                }
            },
            {
                "BTMParameterEnum-145": {
                    "enum_name": "BoundingType",
                    "value": "BLIND",
                    "parameter_id": "endBound"
                }
            },
            {
                "BTMParameterQueryList-148": [
                    {
                        "deterministic_ids": [
                            "JHD"
                        ],
                        "parameter_id": "booleanScope",
                        "bt_type": "BTMIndividualQuery138"
                    }
                ]
            },
            {
                "BTMParameterQueryList-148": [
                    {
                        "parameter_id": "booleanSurfaceScope"
                    }
                ]
            },
            {
                "BTMParameterQuantity-147": {
                    "expression": "1 in",
                    "parameter_id": "offsetDistance"
                }
            },
            {
                "BTMParameterQuantity-147": {
                    "expression": "1 in",
                    "parameter_id": "secondDirectionDepth"
                }
            },
            {
                "BTMParameterQueryList-148": [
                    {
                        "parameter_id": "surfaceEntities"
                    }
                ]
            },
            {
                "BTMParameterEnum-145": {
                    "enum_name": "NewSurfaceOperationType",
                    "value": "NEW",
                    "parameter_id": "surfaceOperationType"
                }
            },
            {
                "BTMParameterEnum-145": {
                    "enum_name": "FlatOperationType",
                    "value": "REMOVE",
                    "parameter_id": "flatOperationType"
                }
            },
            {
                "BTMParameterQueryList-148": [
                    {
                        "deterministic_ids": [
                            "JJC"
                        ],
                        "parameter_id": "entities",
                        "bt_type": "BTMIndividualQuery138"
                    }
                ]
            },
            {
                "BTMParameterQuantity-147": {
                    "expression": "1 in",
                    "parameter_id": "depth"
                }
            }
        ],
        "bt_type": "BTMFeature-134"
    }
}

