FeatureScript 937;
import(path : "onshape/std/geometry.fs", version : "937.0");
import(path : "5d235ff0a55e76d384b9e1a4/6dd946c641f93c53b40cd0e6/94e6e6652b3ad0ea52a5b2b1", version : "f7f0a1d5ae224806aea11e5d");

annotation { "Feature Type Name" : "3d Sketch", "Manipulator Change Function" : "new3dSketchManipulatorChange", "Editing Logic Function" : "new3dSketchEditLogic" }
export const new3dSketch = defineFeature(function(context is Context, id is Id, definition is map)
    precondition
    {
        annotation { "Name" : "Lines", "Item name" : "Line", "Item label template" : "Line #startX, #startY, #startZ", "UIHint" : [UIHint.COLLAPSE_ARRAY_ITEMS, UIHint.MATCH_LAST_ARRAY_ITEM] }
        definition.edges is array;
        for (var edge in definition.edges)
        {
            annotation { "Name" : "Starts on previous edge's end", "Default" : true }
            edge.startsFromPrevious is boolean;

            annotation { "Name" : "Start vertex for measure", "Filter" : EntityType.VERTEX, "MaxNumberOfPicks" : 1 }
            edge.startVertex is Query;

            annotation { "Name" : "Start X" }
            isLength(edge.startX, LENGTH_BOUNDS);

            annotation { "Name" : "Start Y" }
            isLength(edge.startY, LENGTH_BOUNDS);

            annotation { "Name" : "Start Z" }
            isLength(edge.startZ, LENGTH_BOUNDS);

            annotation { "Name" : "End vertex for measure", "Filter" : EntityType.VERTEX, "MaxNumberOfPicks" : 1 }
            edge.endVertex is Query;

            annotation { "Name" : "End X" }
            isLength(edge.endX, LENGTH_BOUNDS);

            annotation { "Name" : "End Y" }
            isLength(edge.endY, LENGTH_BOUNDS);

            annotation { "Name" : "End Z" }
            isLength(edge.endZ, LENGTH_BOUNDS);
        }

        annotation { "Name" : "New line" }
        definition.addLine is boolean;

        annotation { "Name" : "Fillet" }
        definition.hasFillet is boolean;

        if (definition.hasFillet)
            annotation { "Name" : "Radius" }
            isLength(definition.arcRadius, LENGTH_BOUNDS);

        annotation { "Name" : "Snap manipulators" }
        definition.snap is boolean;
        if (definition.snap)
        {
            annotation { "Name" : "Snap to everything", "Default" : true }
            definition.defaultSnap is boolean;

            if (!definition.defaultSnap)
                annotation { "Name" : "Snap entities", "Filter" : EntityType.VERTEX }
                definition.snapElements is Query;

            annotation { "Name" : "Snap radius" }
            isLength(definition.snapRadius, BLEND_BOUNDS);
        }
    }
    {
        var previousEnd = vector(0, 0, 0) * millimeter;
        for (var i = 0; i < size(definition.edges); i += 1)
        {
            var edge = definition.edges[i];
            if (i == 0 && edge.startsFromPrevious)
            {
                throw regenError("Cannot start from previous. No previous edge found");
            }
            var edgeStart = vector(edge.startX, edge.startY, edge.startZ);
            if (edge.startsFromPrevious)
                edgeStart = previousEnd;
            var edgeEnd = vector(edge.endX, edge.endY, edge.endZ);
            if (edge.endVertex != qUnion([]))
            {
                edgeEnd += evVertexPoint(context, {
                            "vertex" : edge.endVertex
                        });
            }
            if (edge.startVertex != qUnion([]) && !edge.startsFromPrevious)
            {
                edgeStart += evVertexPoint(context, {
                            "vertex" : edge.startVertex
                        });
            }
            previousEnd = edgeEnd;
            addManipulators(context, id, {
                        "start_" ~ i : edge.startsFromPrevious ? undefined : triadManipulator(vector(0, 0, 0) * millimeter, edgeStart, undefined),
                        "end___" ~ i : triadManipulator(vector(0, 0, 0) * millimeter, edgeEnd, undefined)
                    });
            opFitSpline(context, id + "spline" + unstableIdComponent(i) + "edge", {
                        "points" : [edgeStart, edgeEnd]
                    });
        }
        if (definition.hasFillet)
        {
            ThreeDfillet(context, id + "fillet", {
                        "deleteOriginal" : true,
                        "bPlane" : false,
                        "arcRadius" : definition.arcRadius,
                        "edges" : qCreatedBy(id + "spline", EntityType.EDGE)
                    });
        }
        try silent
        {
            opExtractWires(context, id + "wire", {
                        "edges" : qCreatedBy(id, EntityType.EDGE)
                    });
            opDeleteBodies(context, id + "deleteBodies1", {
                        "entities" : qSubtraction(qCreatedBy(id), qCreatedBy(id + "wire"))
                    });
        }
    });

export function new3dSketchEditLogic(context is Context, id is Id, oldDefinition is map, definition is map, isCreating is boolean) returns map
{
    if (definition.addLine)
    {
        definition.addLine = false;
        definition.edges = append(definition.edges, {
                    startX : 25 * millimeter,
                    startY : 25 * millimeter,
                    startZ : 25 * millimeter,
                    endX : 25 * millimeter,
                    endY : 25 * millimeter,
                    endZ : 25 * millimeter,
                });
    }
    return definition;
}

export function new3dSketchManipulatorChange(context is Context, definition is map, newManipulators is map) returns map
{
    for (var manip in newManipulators)
    {
        var key = manip.key;
        var value = manip.value;
        var i = stringToNumber(subString(key, 6, length(key)));
        var vertex;
        if (size(evaluateQuery(context, qWithinRadius(definition.defaultSnap ? qConstructionFilter(qEverything(EntityType.VERTEX), ConstructionObject.NO) : definition.snapElements, value.offset, definition.snapRadius))) > 0 && definition.snap)
        {
            vertex = qNthElement(qClosestTo(definition.defaultSnap ? qConstructionFilter(qEverything(EntityType.VERTEX), ConstructionObject.NO) : definition.snapElements, value.offset), 0);
            value.offset = vector(0, 0, 0) * millimeter;
        }
        definition.edges[i][subString(key, 0, 6) ~ "Vertex"] = vertex;
        definition.edges[i][subString(key, 0, 6) ~ "X"] = value.offset[0];
        definition.edges[i][subString(key, 0, 6) ~ "Y"] = value.offset[1];
        definition.edges[i][subString(key, 0, 6) ~ "Z"] = value.offset[2];
    }
    return definition;
}

export function subString(input is string, startIndex is number, endIndex is number) returns string
{
    var chars = subArray(splitIntoCharacters(input), startIndex, endIndex);
    var out = "";
    for (var char in chars)
    {
        if (char != "_")
            out ~= char;
    }
    return out;
}
