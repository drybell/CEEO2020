{
    "0": {
        "entities": [
            {
                "type": 155,
                "typeName": "BTMSketchCurveSegment",
                "message": {
                    "startPointId": "LINE1.start",
                    "endPointId": "LINE1.end",
                    "startParam": 0.0,
                    "endParam": 1.0,
                    "geometry": {
                        "type": 117,
                        "typeName": "BTCurveGeometryLine",
                        "message": {
                            "pntX": 0.0,
                            "pntY": 0.0,
                            "dirX": 0.0,
                            "dirY": 0.0254
                        }
                    },
                    "centerId": "",
                    "internalIds": [],
                    "isConstruction": false,
                    "parameters": [],
                    "entityId": "LINE1",
                    "namespace": "",
                    "hasUserCode": false,
                    "nodeId": "MemNMhOBOXTiIxMfP"
                }
            },
            {
                "type": 155,
                "typeName": "BTMSketchCurveSegment",
                "message": {
                    "startPointId": "LINE2.start",
                    "endPointId": "LINE2.end",
                    "startParam": 0.0,
                    "endParam": 1.0,
                    "geometry": {
                        "type": 117,
                        "typeName": "BTCurveGeometryLine",
                        "message": {
                            "pntX": 0.0,
                            "pntY": 0.0254,
                            "dirX": 0.0254,
                            "dirY": 0.0
                        }
                    },
                    "centerId": "",
                    "internalIds": [],
                    "isConstruction": false,
                    "parameters": [],
                    "entityId": "LINE2",
                    "namespace": "",
                    "hasUserCode": false,
                    "nodeId": "MfmXSf4lBRzh57RYC"
                }
            },
            {
                "type": 155,
                "typeName": "BTMSketchCurveSegment",
                "message": {
                    "startPointId": "LINE3.start",
                    "endPointId": "LINE3.end",
                    "startParam": 0.0,
                    "endParam": 1.0,
                    "geometry": {
                        "type": 117,
                        "typeName": "BTCurveGeometryLine",
                        "message": {
                            "pntX": 0.0254,
                            "pntY": 0.0254,
                            "dirX": 0.0,
                            "dirY": -0.0254
                        }
                    },
                    "centerId": "",
                    "internalIds": [],
                    "isConstruction": false,
                    "parameters": [],
                    "entityId": "LINE3",
                    "namespace": "",
                    "hasUserCode": false,
                    "nodeId": "M93ZqY2rR+3IxQhLh"
                }
            },
            {
                "type": 155,
                "typeName": "BTMSketchCurveSegment",
                "message": {
                    "startPointId": "LINE4.start",
                    "endPointId": "LINE4.end",
                    "startParam": 0.0,
                    "endParam": 1.0,
                    "geometry": {
                        "type": 117,
                        "typeName": "BTCurveGeometryLine",
                        "message": {
                            "pntX": 0.0254,
                            "pntY": 0.0,
                            "dirX": -0.0254,
                            "dirY": 0.0
                        }
                    },
                    "centerId": "",
                    "internalIds": [],
                    "isConstruction": false,
                    "parameters": [],
                    "entityId": "LINE4",
                    "namespace": "",
                    "hasUserCode": false,
                    "nodeId": "MrsdfU1BDqUzEJ9mm"
                }
            }
        ],
        "constraints": [
            {
                "type": 2,
                "typeName": "BTMSketchConstraint",
                "message": {
                    "constraintType": "COINCIDENT",
                    "parameters": [
                        {
                            "type": 149,
                            "typeName": "BTMParameterString",
                            "message": {
                                "value": "point1",
                                "parameterId": "localFirst",
                                "hasUserCode": false,
                                "nodeId": "M6SLo/+1weFY6C3hr"
                            }
                        },
                        {
                            "type": 149,
                            "typeName": "BTMParameterString",
                            "message": {
                                "value": "'LINE1.start",
                                "parameterId": "localSecond",
                                "hasUserCode": false,
                                "nodeId": "Ms5xjGBr685e3xIjO"
                            }
                        }
                    ],
                    "helpParameters": [],
                    "hasOffsetData1": false,
                    "offsetOrientation1": false,
                    "offsetDistance1": 0.0,
                    "hasOffsetData2": false,
                    "offsetOrientation2": false,
                    "offsetDistance2": 0.0,
                    "hasPierceParameter": false,
                    "pierceParameter": 0.0,
                    "entityId": "constrainId",
                    "namespace": "",
                    "hasUserCode": false,
                    "nodeId": "M/9LrNslxsUI1FYGU"
                }
            },
            {
                "type": 2,
                "typeName": "BTMSketchConstraint",
                "message": {
                    "constraintType": "LENGTH",
                    "parameters": [
                        {
                            "type": 149,
                            "typeName": "BTMParameterString",
                            "message": {
                                "value": "point1",
                                "parameterId": "localFirst",
                                "hasUserCode": false,
                                "nodeId": "MQ8/WRZlCgyIhbD5y"
                            }
                        },
                        {
                            "type": 149,
                            "typeName": "BTMParameterString",
                            "message": {
                                "value": "'LINE1.start",
                                "parameterId": "localSecond",
                                "hasUserCode": false,
                                "nodeId": "MUSBYANXpunYh8jtu"
                            }
                        },
                        {
                            "type": 147,
                            "typeName": "BTMParameterQuantity",
                            "message": {
                                "units": "",
                                "value": 0.0,
                                "expression": "1*in",
                                "isInteger": false,
                                "parameterId": "length",
                                "hasUserCode": false,
                                "nodeId": "MghsZJS2xfSAtUH6a"
                            }
                        }
                    ],
                    "helpParameters": [],
                    "hasOffsetData1": false,
                    "offsetOrientation1": false,
                    "offsetDistance1": 0.0,
                    "hasOffsetData2": false,
                    "offsetOrientation2": false,
                    "offsetDistance2": 0.0,
                    "hasPierceParameter": false,
                    "pierceParameter": 0.0,
                    "entityId": "constrainId",
                    "namespace": "",
                    "hasUserCode": false,
                    "nodeId": "MgVopaF/mWW7O0TEU"
                }
            }
        ],
        "featureType": "newSketch",
        "featureId": "FznrDqFtVtLAdpL_0",
        "name": "Square",
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
                                    "JDC"
                                ],
                                "hasUserCode": false,
                                "nodeId": "MJSaGpnoYwCdcb+Ng"
                            }
                        }
                    ],
                    "parameterId": "sketchPlane",
                    "hasUserCode": false,
                    "nodeId": "MuuK6KrQg33njQvIa"
                }
            },
            {
                "type": 147,
                "typeName": "BTMParameterQuantity",
                "message": {
                    "units": "",
                    "value": 0.0,
                    "expression": "1*in",
                    "isInteger": false,
                    "parameterId": "length",
                    "hasUserCode": false,
                    "nodeId": "MRw3vOxoKnbri/SVW"
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
        "nodeId": "MUsIVoprk0+SsKrm2",
        "bt__type": "BTMSketch151"
    },
    "1": {
        "featureType": "extrude",
        "featureId": "FbYwYHH48p3QnrH_0",
        "name": "Square Extrude",
        "parameters": [
            {
                "type": 145,
                "typeName": "BTMParameterEnum",
                "message": {
                    "enumName": "ToolBodyType",
                    "value": "SURFACE",
                    "namespace": "",
                    "parameterId": "bodyType",
                    "hasUserCode": false,
                    "nodeId": "Mp2EOKUMXJOtZycNj"
                }
            },
            {
                "type": 145,
                "typeName": "BTMParameterEnum",
                "message": {
                    "enumName": "OperationDomain",
                    "value": "MODEL",
                    "namespace": "",
                    "parameterId": "domain",
                    "hasUserCode": false,
                    "nodeId": "MPEBC1oaPAfv8y9Q8"
                }
            },
            {
                "type": 145,
                "typeName": "BTMParameterEnum",
                "message": {
                    "enumName": "SecondDirectionBoundingType",
                    "value": "BLIND",
                    "namespace": "",
                    "parameterId": "secondDirectionBound",
                    "hasUserCode": false,
                    "nodeId": "M/MqFEy123wp661Yk"
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
                    "nodeId": "MZ7N7p2hLIzys5Wgs"
                }
            },
            {
                "type": 148,
                "typeName": "BTMParameterQueryList",
                "message": {
                    "queries": [],
                    "parameterId": "endBoundEntityFace",
                    "hasUserCode": false,
                    "nodeId": "MUtXXoWdZf04afN/o"
                }
            },
            {
                "type": 148,
                "typeName": "BTMParameterQueryList",
                "message": {
                    "queries": [],
                    "parameterId": "endBoundEntityBody",
                    "hasUserCode": false,
                    "nodeId": "MVZ3nMh9ope8v/fqp"
                }
            },
            {
                "type": 148,
                "typeName": "BTMParameterQueryList",
                "message": {
                    "queries": [],
                    "parameterId": "endBoundEntityVertex",
                    "hasUserCode": false,
                    "nodeId": "Mcs/vD7BadSrgXU8k"
                }
            },
            {
                "type": 145,
                "typeName": "BTMParameterEnum",
                "message": {
                    "enumName": "NewBodyOperationType",
                    "value": "NEW",
                    "namespace": "",
                    "parameterId": "operationType",
                    "hasUserCode": false,
                    "nodeId": "M3FxSZunNjwSkHva5"
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
                    "nodeId": "Mh4yTJYfR5rTtGi9L"
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
                    "nodeId": "MFNo+PrfP7/nen0Gb"
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
                                    "JGC"
                                ],
                                "hasUserCode": false,
                                "nodeId": "MJkqUlla4fSxN/9LH"
                            }
                        }
                    ],
                    "parameterId": "surfaceEntities",
                    "hasUserCode": false,
                    "nodeId": "MRYYpagYXAXTqa2dk"
                }
            },
            {
                "type": 147,
                "typeName": "BTMParameterQuantity",
                "message": {
                    "units": "",
                    "value": 0.0,
                    "expression": "1*in",
                    "isInteger": false,
                    "parameterId": "depth",
                    "hasUserCode": false,
                    "nodeId": "MSHGG1p9DsII7c1qD"
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
        "nodeId": "Mta6kehDxJ7Qpy3Lc",
        "bt__type": "BTMFeature134"
    },
    "2": {
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
        "nodeId": "MJMFl5KzlVqdU+Axm",
        "bt__type": "BTMSketch151"
    },
    "3": {
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
        "nodeId": "MS3TZqA3xr2L89sLt",
        "bt__type": "BTMFeature134"
    }
}
