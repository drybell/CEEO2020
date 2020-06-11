FeatureScript 1301;
import(path : "onshape/std/geometry.fs", version : "1301.0");

annotation { "Feature Type Name" : "My Feature" }
export const myFeature = defineFeature(function(context is Context, id is Id, definition is map)
    precondition
    {
        // Define the parameters of the feature type
    }
    {
        // Define the function's action
        fCuboid(context, id + "cuboid1", {
                "corner1" : vector(0, 0, 0) * inch,
                "corner2" : vector(1, 1, 1) * inch
        });
    });
