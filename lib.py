# -*- coding= utf-8 -*-

named_obj = (
    'BRDG',
    'BUIL',
    'CCAR',
    'CRSS',
    'GOOD',
    'GOBJ',
    'PASS',
    'SIGN',
    'TUNL',
    'TREE',
    'VHCL',
    'WAY' ,
    'WYOB',
)

BRDGparam = (
#               attrname,   type,       hook,            version,    None
    lambda v:  ('waytype',  'uint16',   lambda x: x)     if v < 2    else None,
    lambda v:  ('_dummy',   'uint16',   lambda x: x)     if v== 0    else None,
    lambda v:  ('top_speed','uint16',   lambda x: x)     if v > 0    else None,
    lambda v:  ('cost',     'uint32',   lambda x: x/100) if v > -1   else None,
    lambda v:  ('maintain', 'uint32',   lambda x: x/100) if v > 1    else None,
    lambda v:  ('waytype',  'uint8',    lambda x: x)     if v > 0    else None,
    lambda v:  ('pillar_e', 'uint8',    lambda x: x)     if v > 2    else None,
    lambda v:  ('max_len',  'uint8',    lambda x: x)     if v > 3    else None,
    lambda v:  ('intro',    'uint16',   lambda x: x)     if v > 4    else None,
    lambda v:  ('retire',   'uint16',   lambda x: x)     if v > 4    else None,
    lambda v:  ('pillar_a', 'uint8',    lambda x: x)     if v > 6    else None,
    lambda v:  ('axle_load','uint16',   lambda x: x)     if v > 8    else None,
    lambda v:  ('max_hei',  'uint8',    lambda x: x)     if v > 6    else None,
    lambda v:  ('season',   'uint8',    lambda x: x)     if v > 5    else None,
)

BUILparam = (
#               attrname,   type,       hook,            version,    None
    lambda v:  ('g_type',   'uint16',   lambda x: x)     if v== 0    else None,
    lambda v:  ('g_type',   'uint8',    lambda x: x)     if v > 0    else None,
    lambda v:  ('_dummy',   'uint16',   lambda x: x)     if v== 0    else None,
    lambda v:  ('u_type',   'uint32',   lambda x: x)     if v== 0    else None,
    lambda v:  ('u_type',   'uint8',    lambda x: x)     if v > 0    else None,
    lambda v:  ('level',    'uint32',   lambda x: x)     if v== 0    else None,
    lambda v:  ('level',    'uint16',   lambda x: x)     if v > 0    else None,
    lambda v:  ('ex_data',  'uint32',   lambda x: x)     if v > -1   else None,
    lambda v:  ('size_x',   'uint16',   lambda x: x)     if v > -1   else None,
    lambda v:  ('size_y',   'uint16',   lambda x: x)     if v > -1   else None,
    lambda v:  ('layouts',  'uint32',   lambda x: x)     if v== 0    else None,
    lambda v:  ('layouts',  'uint8',    lambda x: x)     if v > 0    else None,
    lambda v:  ('climates', 'uint16',   lambda x: x)     if v > 3    else None,
    lambda v:  ('enables',  'uint8',    lambda x: x)     if v > 2    else None,
    lambda v:  ('flags',    'uint32',   lambda x: x)     if v== 0    else None,
    lambda v:  ('flags',    'uint8',    lambda x: x)     if v > 0    else None,
    lambda v:  ('chance',   'uint8',    lambda x: x)     if v > 0    else None,
    lambda v:  ('intro',    'uint16',   lambda x: x)     if v > 1    else None,
    lambda v:  ('retire',   'uint16',   lambda x: x)     if v > 1    else None,
    lambda v:  ('anim_time','uint16',   lambda x: x)     if v > 4    else None,
    lambda v:  ('capacity', 'uint16',   lambda x: x)     if v > 7    else None,
    lambda v:  ('maintain', 'sint32',   lambda x: x)     if v > 7    else None,
    lambda v:  ('price',    'sint32',   lambda x: x)     if v > 7    else None,
    lambda v:  ('undergnd', 'uint8',    lambda x: x)     if v > 6    else None,
)

CCARparam = (
#               attrname,   type,       hook,            version,    None
    lambda v:  ('weight',   'uint16',   lambda x: x)     if v > -1   else None,
    lambda v:  ('top_speed','uint16',   lambda x: x)     if v > 0    else None,
    lambda v:  ('intro',    'uint16',   lambda x: x)     if v > 0    else None,
    lambda v:  ('retire',   'uint16',   lambda x: x)     if v > 0    else None,

)

VHCLparam = (
#               attrname,   type,       hook,            version,    None
    lambda v:  ('waytype',  'uint16',   lambda x: x)     if v== 0    else None,
    lambda v:  ('payload',  'uint16',   lambda x: x)     if v== 0    else None,
    lambda v:  ('cost',     'uint32',   lambda x: x/100) if v > -1   else None,
    lambda v:  ('payload',  'uint16',   lambda x: x)     if v > 0    else None,
    lambda v:  ('load_time','uint16',   lambda x: x)     if v > 8    else None,
    lambda v:  ('top_speed','uint16',   lambda x: x)     if v > -1   else None,
    lambda v:  ('weight',   'uint32',   lambda x: x/1000)if v > 9    else None,
    lambda v:  ('weight',   'uint16',   lambda x: x)     if v < 10   else None,
    lambda v:  ('axle_load','uint16',   lambda x: x)     if v > 8    else None,
    lambda v:  ('power',    'uint32',   lambda x: x)     if v > 5    else None,
    lambda v:  ('power',    'uint16',   lambda x: x)     if v < 6    else None,
    lambda v:  ('run_cost', 'uint16',   lambda x: x/100) if v > -1   else None,
    lambda v:  ('fix_cost', 'uint32',   lambda x: x/100) if v > 10   else None,
    lambda v:  ('fix_cost', 'uint16',   lambda x: x/100) if 11> v >8 else None,
    lambda v:  ('intro',    'uint16',   lambda x: x)     if v > 0    else None,
    lambda v:  ('retire',   'uint16',   lambda x: x)     if v > 2    else None,
    lambda v:  ('gear',     'uint16',   lambda x: x)     if v > 5    else None,
    lambda v:  ('gear',     'uint8',    lambda x: x)     if v < 6    else None,
    lambda v:  ('waytype',  'uint8',    lambda x: x)     if v > 0    else None,
    lambda v:  ('sound',    'uint16',   lambda x: x)     if v== 0    else None,
    lambda v:  ('sound',    'sint8',    lambda x: x)     if v > 0    else None,
    lambda v:  ('engine',   'uint8',    lambda x: x)     if v > 0    else None,
    lambda v:  ('length',   'uint8',    lambda x: x)     if v > 6    else None,
    lambda v:  ('const_pr', 'uint16',   lambda x: x)     if v== 0    else None,
    lambda v:  ('const_pr', 'uint8',    lambda x: x)     if v > 0    else None,
    lambda v:  ('const_nx', 'uint16',   lambda x: x)     if v== 0    else None,
    lambda v:  ('const_nx', 'uint8',    lambda x: x)     if v > 0    else None,
    lambda v:  ('frei_imag','uint8',    lambda x: x)     if v > 7    else None,
)
