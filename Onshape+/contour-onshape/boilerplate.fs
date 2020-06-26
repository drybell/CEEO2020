FeatureScript 1247;
import(path : "onshape/std/geometry.fs", version : "1247.0");
annotation { "Feature Type Name" : "LabVIEW Feature" }
export const myFeature = defineFeature(function(context is Context, id is Id, definition is map)
    precondition
    {
        // Define the parameters of the feature type
    }
    {
        var sketch1 = newSketch(context, id + "sketch1", {
                "sketchPlane" : qCreatedBy(makeId("Top"), EntityType.FACE)
        });
        // Create sketch entities here
        skPolyline(sketch1, "polyline1", {
                "points" : []
        });
        skSolve(sketch1);
// Define the function's action
    });