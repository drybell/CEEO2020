{
    "BTMSketch151": {
        "entities": [
            {
                "type": 155,
                "typeName": "BTMSketchCurveSegment",
                "message": {
                    "startPointId": "KwbsVwMqEIvo.start",
                    "endPointId": "KwbsVwMqEIvo.end",
                    "startParam": -0.025400000000000002,
                    "endParam": 0.025400000000000002,
                    "geometry": {
                        "type": 117,
                        "typeName": "BTCurveGeometryLine",
                        "message": {
                            "pntX": 0.0,
                            "pntY": 0.025400000000000002,
                            "dirX": 0.0,
                            "dirY": -1.0
                        }
                    },
                    "centerId": "",
                    "internalIds": [],
                    "isConstruction": false,
                    "parameters": [],
                    "entityId": "KwbsVwMqEIvo",
                    "namespace": "",
                    "hasUserCode": false,
                    "nodeId": "MVR+inW8o0w/wUhYp"
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
                                "value": "KwbsVwMqEIvo.start",
                                "parameterId": "localFirst",
                                "hasUserCode": false,
                                "nodeId": "MOdnCqq6xgcJfB53+"
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
                                            "geometryIds": [],
                                            "hasUserCode": false,
                                            "nodeId": "Mg9y7akifFYRuPIIm"
                                        }
                                    }
                                ],
                                "parameterId": "externalSecond",
                                "hasUserCode": false,
                                "nodeId": "MeYTqMiKyFCcpgb9a"
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
                    "entityId": "KwbsVwMqEIvo.startSnap0",
                    "namespace": "",
                    "hasUserCode": false,
                    "nodeId": "MDe21TkBTXulUrZpJ"
                }
            },
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
                                "value": "KwbsVwMqEIvo.end",
                                "parameterId": "localFirst",
                                "hasUserCode": false,
                                "nodeId": "MzBWGpRvesayj1O9P"
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
                                            "geometryIds": [],
                                            "hasUserCode": false,
                                            "nodeId": "MgoichqN8hjMMAqwa"
                                        }
                                    }
                                ],
                                "parameterId": "externalSecond",
                                "hasUserCode": false,
                                "nodeId": "Mqcs9j8i1Vr6vFXSB"
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
                    "entityId": "KwbsVwMqEIvo.endSnap0",
                    "namespace": "",
                    "hasUserCode": false,
                    "nodeId": "M2VQrgUJrZ2s3ux/u"
                }
            }
        ],
        "featureType": "newSketch",
        "featureId": "F6vWEnLTG1syOX7_1",
        "name": "Sketch 3",
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
                                    "JCC"
                                ],
                                "hasUserCode": false,
                                "nodeId": "FjtO9dtE70scpKI"
                            }
                        }
                    ],
                    "parameterId": "sketchPlane",
                    "hasUserCode": false,
                    "nodeId": "ocgO9J2knpngn2Qs"
                }
            },
            {
                "type": 145,
                "typeName": "BTMParameterEnum",
                "message": {
                    "enumName": "FeatureScriptVersionNumber",
                    "value": "V1311_FIX_CONFIGURE_FACE_COLOR_SOURCE",
                    "namespace": "",
                    "parameterId": "asVersion",
                    "hasUserCode": false,
                    "nodeId": "MU7Tn+CmqtmqkP1FC"
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
        "nodeId": "M/lY9my1ybGsTJsT0"
    },
    "BTMFeature134": {
        "featureType": "sweep",
        "featureId": "F6lQ6o4a91Xek0X_1",
        "name": "Sweep 1",
        "parameters": [
            {
                "type": 145,
                "typeName": "BTMParameterEnum",
                "message": {
                    "enumName": "ToolBodyType",
                    "value": "SOLID",
                    "namespace": "",
                    "parameterId": "bodyType",
                    "hasUserCode": false,
                    "nodeId": "2RmrSgN2EDEjgxDN"
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
                    "nodeId": "NB9bFTV0vlJS6qOd"
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
                                "nodeId": "FmPUbH3aObItsMc"
                            }
                        }
                    ],
                    "parameterId": "profiles",
                    "hasUserCode": false,
                    "nodeId": "1RXwI/CA22aR29LB"
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
                    "nodeId": "8o2lRPz1H74gE6kU"
                }
            },
            {
                "type": 148,
                "typeName": "BTMParameterQueryList",
                "message": {
                    "queries": [],
                    "parameterId": "surfaceProfiles",
                    "hasUserCode": false,
                    "nodeId": "hlZMVsm5lJZQ94fc"
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
                                    "JKB"
                                ],
                                "hasUserCode": false,
                                "nodeId": "FdiFbe2heRVrrTM"
                            }
                        }
                    ],
                    "parameterId": "path",
                    "hasUserCode": false,
                    "nodeId": "PlnNmlIp8ahpb06v"
                }
            },
            {
                "type": 144,
                "typeName": "BTMParameterBoolean",
                "message": {
                    "value": false,
                    "parameterId": "keepProfileOrientation",
                    "hasUserCode": false,
                    "nodeId": "mYRqFicNrUVe9CMY"
                }
            },
            {
                "type": 144,
                "typeName": "BTMParameterBoolean",
                "message": {
                    "value": false,
                    "parameterId": "defaultScope",
                    "hasUserCode": false,
                    "nodeId": "n+rdcmKuYqLFtndl"
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
                                "nodeId": "M3Uui0fQBoxjHnPol"
                            }
                        }
                    ],
                    "parameterId": "booleanScope",
                    "hasUserCode": false,
                    "nodeId": "6o8B6XrVhJ7kBOiu"
                }
            },
            {
                "type": 144,
                "typeName": "BTMParameterBoolean",
                "message": {
                    "value": true,
                    "parameterId": "defaultSurfaceScope",
                    "hasUserCode": false,
                    "nodeId": "fcMzV8ho1GNpumFT"
                }
            },
            {
                "type": 148,
                "typeName": "BTMParameterQueryList",
                "message": {
                    "queries": [],
                    "parameterId": "booleanSurfaceScope",
                    "hasUserCode": false,
                    "nodeId": "ER7zE15sNYp3gAFy"
                }
            },
            {
                "type": 145,
                "typeName": "BTMParameterEnum",
                "message": {
                    "enumName": "FeatureScriptVersionNumber",
                    "value": "V1311_FIX_CONFIGURE_FACE_COLOR_SOURCE",
                    "namespace": "",
                    "parameterId": "asVersion",
                    "hasUserCode": false,
                    "nodeId": "MQeAeNtCNY6J6Iqpi"
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
        "nodeId": "MHv8E6V6bpJKTonTX"
    }
}