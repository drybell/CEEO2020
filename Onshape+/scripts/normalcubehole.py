{
    "BTMSketch151": {
        "entities": [
            {
                "type": 4,
                "typeName": "BTMSketchCurve",
                "message": {
                    "geometry": {
                        "type": 115,
                        "typeName": "BTCurveGeometryCircle",
                        "message": {
                            "radius": 0.00635,
                            "xCenter": 0.0127,
                            "yCenter": 0.0127,
                            "xDir": 0.0127,
                            "yDir": 0.0,
                            "clockwise": false
                        }
                    },
                    "centerId": "Circle.center",
                    "internalIds": [],
                    "isConstruction": false,
                    "parameters": [],
                    "entityId": "Circle",
                    "namespace": "",
                    "hasUserCode": false,
                    "nodeId": "M5v3K4x5rrIGQZ7eg"
                }
            }
        ],
        "constraints": [],
        "featureType": "newSketch",
        "featureId": "FmK8jL2YyjMMALm_1",
        "name": "Circle On a Face",
        "parameters": [
            {
                "type": 148,
                "typeName": "BTMParameterQueryList",
                "message": {
                    "queries": [
                        {
                            "type": 138,
                            "typeName": "BTMIndividualQuery",
                            "message": {
                                "geometryIds": [
                                    "JGC"
                                ],
                                "hasUserCode": false,
                                "nodeId": "MKb33rxXVuD8fDi9I"
                            }
                        }
                    ],
                    "parameterId": "sketchPlane",
                    "hasUserCode": false,
                    "nodeId": "MIsVlOP92mAJDCd7J"
                }
            }
        ],
        "suppressed": false,
        "namespace": "",
        "subFeatures": [],
        "returnAfterSubfeatures": false,
        "suppressionState": {
            "type": 0
        },
        "hasUserCode": false,
        "nodeId": "MJMFl5KzlVqdU+Axm"
    },
    "BTMFeature134": {
        "featureType": "extrude",
        "featureId": "F8FHjQhi9DkW6eQ_1",
        "name": "Extrude Remove Circle",
        "parameters": [
            {
                "type": 145,
                "typeName": "BTMParameterEnum",
                "message": {
                    "enumName": "OperationDomain",
                    "value": "MODEL",
                    "namespace": "",
                    "parameterId": "domain",
                    "hasUserCode": false,
                    "nodeId": "MjFSLHQj/tzRYhLfB"
                }
            },
            {
                "type": 145,
                "typeName": "BTMParameterEnum",
                "message": {
                    "enumName": "ToolBodyType",
                    "value": "SOLID",
                    "namespace": "",
                    "parameterId": "bodyType",
                    "hasUserCode": false,
                    "nodeId": "M6q/FaEdhJxZFt5ff"
                }
            },
            {
                "type": 145,
                "typeName": "BTMParameterEnum",
                "message": {
                    "enumName": "NewBodyOperationType",
                    "value": "REMOVE",
                    "namespace": "",
                    "parameterId": "operationType",
                    "hasUserCode": false,
                    "nodeId": "MlOk7SFiMYe0D3uNh"
                }
            },
            {
                "type": 145,
                "typeName": "BTMParameterEnum",
                "message": {
                    "enumName": "BoundingType",
                    "value": "BLIND",
                    "namespace": "",
                    "parameterId": "endBound",
                    "hasUserCode": false,
                    "nodeId": "MXSvphmVYxGftAkZe"
                }
            },
            {
                "type": 148,
                "typeName": "BTMParameterQueryList",
                "message": {
                    "queries": [
                        {
                            "type": 138,
                            "typeName": "BTMIndividualQuery",
                            "message": {
                                "geometryIds": [
                                    "JHD"
                                ],
                                "hasUserCode": false,
                                "nodeId": "MV7skUXpviD6D+QIq"
                            }
                        }
                    ],
                    "parameterId": "booleanScope",
                    "hasUserCode": false,
                    "nodeId": "MWqQwHQXlWO7hft4A"
                }
            },
            {
                "type": 148,
                "typeName": "BTMParameterQueryList",
                "message": {
                    "queries": [],
                    "parameterId": "booleanSurfaceScope",
                    "hasUserCode": false,
                    "nodeId": "Mrr2Uik6nHpFGmkYL"
                }
            },
            {
                "type": 147,
                "typeName": "BTMParameterQuantity",
                "message": {
                    "units": "",
                    "value": 0.0,
                    "expression": "1 in",
                    "isInteger": false,
                    "parameterId": "offsetDistance",
                    "hasUserCode": false,
                    "nodeId": "M0Ot1kSD9r1HtTBKi"
                }
            },
            {
                "type": 147,
                "typeName": "BTMParameterQuantity",
                "message": {
                    "units": "",
                    "value": 0.0,
                    "expression": "1 in",
                    "isInteger": false,
                    "parameterId": "secondDirectionDepth",
                    "hasUserCode": false,
                    "nodeId": "MWOB9tafFxtY4IqA9"
                }
            },
            {
                "type": 148,
                "typeName": "BTMParameterQueryList",
                "message": {
                    "queries": [],
                    "parameterId": "surfaceEntities",
                    "hasUserCode": false,
                    "nodeId": "Mr7oNwFvdJSa+v3ic"
                }
            },
            {
                "type": 145,
                "typeName": "BTMParameterEnum",
                "message": {
                    "enumName": "NewSurfaceOperationType",
                    "value": "NEW",
                    "namespace": "",
                    "parameterId": "surfaceOperationType",
                    "hasUserCode": false,
                    "nodeId": "McQ8l0XmuEeXml4aD"
                }
            },
            {
                "type": 145,
                "typeName": "BTMParameterEnum",
                "message": {
                    "enumName": "FlatOperationType",
                    "value": "REMOVE",
                    "namespace": "",
                    "parameterId": "flatOperationType",
                    "hasUserCode": false,
                    "nodeId": "M/aruz23rOgTlBSfG"
                }
            },
            {
                "type": 148,
                "typeName": "BTMParameterQueryList",
                "message": {
                    "queries": [
                        {
                            "type": 138,
                            "typeName": "BTMIndividualQuery",
                            "message": {
                                "geometryIds": [
                                    "JJC"
                                ],
                                "hasUserCode": false,
                                "nodeId": "MknULp2iS7E0VpTsb"
                            }
                        }
                    ],
                    "parameterId": "entities",
                    "hasUserCode": false,
                    "nodeId": "M1lWWIwQzKxW1HnwL"
                }
            },
            {
                "type": 147,
                "typeName": "BTMParameterQuantity",
                "message": {
                    "units": "",
                    "value": 0.0,
                    "expression": "1 in",
                    "isInteger": false,
                    "parameterId": "depth",
                    "hasUserCode": false,
                    "nodeId": "M3gIwL5Dl5kmOT+17"
                }
            }
        ],
        "suppressed": false,
        "namespace": "",
        "subFeatures": [],
        "returnAfterSubfeatures": false,
        "suppressionState": {
            "type": 0
        },
        "hasUserCode": false,
        "nodeId": "MS3TZqA3xr2L89sLt"
    }
}