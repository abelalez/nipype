# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.slicer.surface import ModelMaker

def test_ModelMaker_inputs():
    input_map = dict(InputVolume=dict(argstr='%s',
    position=-1,
    ),
    args=dict(argstr='%s',
    ),
    color=dict(argstr='--color %s',
    ),
    debug=dict(argstr='--debug ',
    ),
    decimate=dict(argstr='--decimate %f',
    ),
    end=dict(argstr='--end %d',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    filtertype=dict(argstr='--filtertype %s',
    ),
    generateAll=dict(argstr='--generateAll ',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    jointsmooth=dict(argstr='--jointsmooth ',
    ),
    labels=dict(argstr='--labels %s',
    sep=',',
    ),
    modelSceneFile=dict(argstr='--modelSceneFile %s...',
    hash_files=False,
    ),
    name=dict(argstr='--name %s',
    ),
    pad=dict(argstr='--pad ',
    ),
    pointnormals=dict(argstr='--pointnormals ',
    ),
    saveIntermediateModels=dict(argstr='--saveIntermediateModels ',
    ),
    skipUnNamed=dict(argstr='--skipUnNamed ',
    ),
    smooth=dict(argstr='--smooth %d',
    ),
    splitnormals=dict(argstr='--splitnormals ',
    ),
    start=dict(argstr='--start %d',
    ),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = ModelMaker.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_ModelMaker_outputs():
    output_map = dict(modelSceneFile=dict(exists=True,
    ),
    )
    outputs = ModelMaker.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

