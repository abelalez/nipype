# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.freesurfer.utils import MRIMarchingCubes

def test_MRIMarchingCubes_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    connectivity_value=dict(argstr='%d',
    position=-1,
    usedefault=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='%s',
    mandatory=True,
    position=1,
    ),
    label_value=dict(argstr='%d',
    mandatory=True,
    position=2,
    ),
    out_file=dict(argstr='./%s',
    genfile=True,
    position=-2,
    ),
    subjects_dir=dict(),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = MRIMarchingCubes.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_MRIMarchingCubes_outputs():
    output_map = dict(surface=dict(),
    )
    outputs = MRIMarchingCubes.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

