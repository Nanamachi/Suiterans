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

CRSSparam = (
#               attrname,   type,       hook,            version,    None
    lambda v:  ('waytype0', 'uint16',   lambda x: x)     if v== 0    else None,
    lambda v:  ('waytype0', 'uint8',    lambda x: x)     if v > 0    else None,
    lambda v:  ('waytype1', 'uint16',   lambda x: x)     if v== 0    else None,
    lambda v:  ('waytype1', 'uint8',    lambda x: x)     if v > 0    else None,
    lambda v:  ('top_spd0', 'uint16',   lambda x: x)     if v > 0    else None,
    lambda v:  ('top_spd1', 'uint16',   lambda x: x)     if v > 0    else None,
    lambda v:  ('op_anm_t', 'uint32',   lambda x: x)     if v > 0    else None,
    lambda v:  ('xz_anm_t', 'uint32',   lambda x: x)     if v > 0    else None,
    lambda v:  ('sound',    'sint8',    lambda x: x)     if v > 0    else None,
    lambda v:  ('intro',    'uint16',   lambda x: x)     if v > 1    else None,
    lambda v:  ('retire',   'uint16',   lambda x: x)     if v > 1    else None,
)

FACTparam = (
#               attrname,   type,       hook,            version,    None
    lambda v:  ('location', 'uint16',   lambda x: x)     if v > -1   else None,
    lambda v:  ('_dummy',   'uint16',   lambda x: x)     if v== 0    else None,
    lambda v:  ('pdctivity','uint16',   lambda x: x)     if v > -1   else None,
    lambda v:  ('range',    'uint16',   lambda x: x)     if v > -1   else None,
    lambda v:  ('dist_wt',  'uint16',   lambda x: x)     if v > -1   else None,
    lambda v:  ('color',    'uint16',   lambda x: x)     if v < 2    else None,
    lambda v:  ('color',    'uint8',    lambda x: x)     if v > 1    else None,
    lambda v:  ('fields',   'uint8',    lambda x: x)     if v > 1    else None,
    lambda v:  ('supply',   'uint16',   lambda x: x)     if v > -1   else None,
    lambda v:  ('product',  'uint16',   lambda x: x)     if v > -1   else None,
    lambda v:  ('pax_lvl',  'uint16',   lambda x: x)     if v > 0    else None,
    lambda v:  ('exp_prob', 'uint16',   lambda x: x)     if v > 2    else None,
    lambda v:  ('exp_min',  'uint16',   lambda x: x)     if v > 2    else None,
    lambda v:  ('exp_range','uint16',   lambda x: x)     if v > 2    else None,
    lambda v:  ('exp_time', 'uint16',   lambda x: x)     if v > 2    else None,
    lambda v:  ('elec_bst', 'uint16',   lambda x: x)     if v > 2    else None,
    lambda v:  ('pax_bst',  'uint16',   lambda x: x)     if v > 2    else None,
    lambda v:  ('mail_bst', 'uint16',   lambda x: x)     if v > 2    else None,
    lambda v:  ('elec_amt', 'uint16',   lambda x: x)     if v > 2    else None,
    lambda v:  ('pax_dmd',  'uint16',   lambda x: x)     if v > 2    else None,
    lambda v:  ('mail_dmd', 'uint16',   lambda x: x)     if v > 2    else None,
)

FFCLparam = (
#               attrname,   type,       hook,            version,    None
    lambda v:  ('snow_img', 'uint8',    lambda x: x)     if v > 0    else None,
    lambda v:  ('prod_p_f', 'uint16',   lambda x: x)     if v > 0    else None,
    lambda v:  ('capacity', 'uint16',   lambda x: x)     if v > 0    else None,
    lambda v:  ('spawn_wt', 'uint16',   lambda x: x)     if v > 0    else None,
)


FFIEparam = (
#               attrname,   type,       hook,            version,    None
    lambda v:  ('snow_img', 'uint8',    lambda x: x)     if v== 1    else None,
    lambda v:  ('probablty','uint16',   lambda x: x)     if v > 0    else None,
    lambda v:  ('prod_p_f', 'uint16',   lambda x: x)     if v== 1    else None,
    lambda v:  ('max_fld',  'uint16',   lambda x: x)     if v > 0    else None,
    lambda v:  ('min_fld',  'uint16',   lambda x: x)     if v > 0    else None,
    lambda v:  ('start_fld','uint16',   lambda x: x)     if v > 2    else None,
    lambda v:  ('flc_cls',  'uint16',   lambda x: x)     if v > 1    else None,
)

FPROparam = (
#               attrname,   type,       hook,            version,    None
    lambda v:  ('capacity', 'uint16',   lambda x: x)     if v > -1   else None,
    lambda v:  ('_dummy',   'uint16',   lambda x: x)     if v== 0    else None,
    lambda v:  ('factor',   'uint16',   lambda x: x)     if v > 0    else None,
)

FSMOparam = (
#               attrname,   type,       hook,            version,    None
    lambda v:  ('pos_x',    'sint16',   lambda x: x)     if v > -1   else None,
    lambda v:  ('pos_y',    'sint16',   lambda x: x)     if v > -1   else None,
    lambda v:  ('off_x',    'sint16',   lambda x: x)     if v > -1   else None,
    lambda v:  ('off_y',    'sint16',   lambda x: x)     if v > -1   else None,
    lambda v:  ('speed',    'sint16',   lambda x: x)     if v > -1   else None,
)

FSUPparam = (
#               attrname,   type,       hook,            version,    None
    lambda v:  ('capacity', 'uint16',   lambda x: x)     if v > -1   else None,
    lambda v:  ('sup_cnt',  'uint16',   lambda x: x)     if v > -1   else None,
    lambda v:  ('consume',  'uint16',   lambda x: x)     if v > -1   else None,
    lambda v:  ('_dummy',   'uint16',   lambda x: x)     if v > -1   else None,
)

GOBJparam = (
#               attrname,   type,       hook,            version,    None
    lambda v:  ('climates', 'uint16',   lambda x: x)     if v > 0    else None,
    lambda v:  ('dist_wt',  'uint16',   lambda x: x)     if v > 0    else None,
    lambda v:  ('season',   'uint8',    lambda x: x)     if v > 0    else None,
    lambda v:  ('tree_on',  'uint8',    lambda x: x)     if v > 0    else None,
    lambda v:  ('speed',    'uint16',   lambda x: x)     if v > 0    else None,
    lambda v:  ('waytype',  'uint16',   lambda x: x)     if v > 0    else None,
    lambda v:  ('cost_rmv', 'uint32',   lambda x: x)     if v > 0    else None,
)

GOODparam = (
#               attrname,   type,       hook,            version,    None
    lambda v:  ('value',    'uint16',   lambda x: x)     if v > -1   else None,
    lambda v:  ('category', 'uint16',   lambda x: x)     if v < 3    else None,
    lambda v:  ('category', 'uint8',    lambda x: x)     if v > 2    else None,
    lambda v:  ('spd_bonus','uint16',   lambda x: x)     if v > 0    else None,
    lambda v:  ('wt_p_unit','uint16',   lambda x: x)     if v > 1    else None,
    lambda v:  ('color',    'uint8',    lambda x: x)     if v > 2    else None,
)

PASSparam = (
#               attrname,   type,       hook,            version,    None
    lambda v:  ('weight',   'uint16',   lambda x: x)     if v== 0    else None,
    lambda v:  ('_dummy',   'uint16',   lambda x: x)     if v== 0    else None,
)

SIGNparam = (
#               attrname,   type,       hook,            version,    None
    lambda v:  ('min_speed','uint16',   lambda x: x)     if v > 0    else None,
    lambda v:  ('cost',     'uint32',   lambda x: x)     if v > 1    else None,
    lambda v:  ('flags',    'uint8',    lambda x: x)     if v > 0    else None,
    lambda v:  ('off_left', 'sint8',    lambda x: x)     if v > 3    else None,
    lambda v:  ('waytype',  'uint8',    lambda x: x)     if v > 2    else None,
    lambda v:  ('intro',    'uint16',   lambda x: x)     if v > 2    else None,
    lambda v:  ('retire',   'uint16',   lambda x: x)     if v > 2    else None,
)

TILEparam = (
#               attrname,   type,       hook,            version,    None
    lambda v:  ('_dummy',   'uint32',   lambda x: x)     if v== 0    else None,
    lambda v:  ('phasen',   'uint16',   lambda x: x)     if v > -1   else None,
    lambda v:  ('index',    'uint16',   lambda x: x)     if v > -1   else None,
    lambda v:  ('seasons',  'uint8',    lambda x: x)     if v > 1    else None,
)

TREEparam = (
#               attrname,   type,       hook,            version,    None
    lambda v:  ('climate',  'uint16',   lambda x: x)     if v > 1    else None,
    lambda v:  ('dist_wt',  'uint8',    lambda x: x)     if v > 1    else None,
    lambda v:  ('_dummy',   'uint8',    lambda x: x)     if v== 1    else None,
    lambda v:  ('season',   'uint8',    lambda x: x)     if v > 0    else None,
)

TUNLparam = (
#               attrname,   type,       hook,            version,    None
    lambda v:  ('top_speed','uint32',   lambda x: x)     if v > 0    else None,
    lambda v:  ('cost',     'uint32',   lambda x: x/100) if v > 0    else None,
    lambda v:  ('maintain', 'uint32',   lambda x: x/100) if v > 0    else None,
    lambda v:  ('waytype',  'uint8',    lambda x: x)     if v > 0    else None,
    lambda v:  ('intro',    'uint16',   lambda x: x)     if v > 0    else None,
    lambda v:  ('retire',   'uint16',   lambda x: x)     if v > 0    else None,
    lambda v:  ('axle_load','uint16',   lambda x: x)     if v > 4    else None,
    lambda v:  ('season',   'uint8',    lambda x: x)     if v > 1    else None,
    lambda v:  ('has_way',  'uint8',    lambda x: x)     if v > 2    else None,
    lambda v:  ('brd_ptls', 'uint8',    lambda x: x)     if v > 3    else None,
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
    lambda v:  ('gear',     'uint8',    lambda x: x)     if 0< v <6  else None,
    lambda v:  ('waytype',  'uint8',    lambda x: x)     if v > 0    else None,
    lambda v:  ('sound',    'sint16',   lambda x: x)     if v== 0    else None,
    lambda v:  ('sound',    'sint8',    lambda x: x)     if v > 0    else None,
    lambda v:  ('engine',   'uint8',    lambda x: x)     if v > 0    else None,
    lambda v:  ('length',   'uint8',    lambda x: x)     if v > 6    else None,
    lambda v:  ('const_pr', 'uint16',   lambda x: x)     if v== 0    else None,
    lambda v:  ('const_pr', 'uint8',    lambda x: x)     if v > 0    else None,
    lambda v:  ('const_nx', 'uint16',   lambda x: x)     if v== 0    else None,
    lambda v:  ('const_nx', 'uint8',    lambda x: x)     if v > 0    else None,
    lambda v:  ('frei_imag','uint8',    lambda x: x)     if v > 7    else None,
    lambda v:  ('_dummy',   'uint16',   lambda x: x)     if v== 0    else None,
)

WAYparam = (
#               attrname,   type,       hook,            version,    None
    lambda v:  ('cost',     'uint32',   lambda x: x/100) if v > 0    else None,
    lambda v:  ('maintain', 'uint32',   lambda x: x/100) if v > 0    else None,
    lambda v:  ('top_speed','uint32',   lambda x: x)     if v > 0    else None,
    lambda v:  ('max_wt',   'uint32',   lambda x: x)     if v > 0    else None,
    lambda v:  ('intro',    'uint32',   lambda x: x)     if v== 1    else None,
    lambda v:  ('intro',    'uint16',   lambda x: x)     if v > 1    else None,
    lambda v:  ('retire',   'uint16',   lambda x: x)     if v > 0    else None,
    lambda v:  ('axle_load','uint16',   lambda x: x)     if v > 5    else None,
    lambda v:  ('waytype',  'uint8',    lambda x: x)     if v > 0    else None,
    lambda v:  ('styp',     'uint8',    lambda x: x)     if v > 2    else None,
    lambda v:  ('draw_a_ob','uint8',    lambda x: x)     if v > 3    else None,
    lambda v:  ('season',   'uint8',    lambda x: x)     if v > 1    else None,
)

WYOBparam = (
#               attrname,   type,       hook,            version,    None
    lambda v:  ('cost',     'uint32',   lambda x: x)     if v > 0    else None,
    lambda v:  ('maintain', 'uint32',   lambda x: x)     if v > 0    else None,
    lambda v:  ('top_speed','uint32',   lambda x: x)     if v > 0    else None,
    lambda v:  ('intro',    'uint16',   lambda x: x)     if v > 0    else None,
    lambda v:  ('retire',   'uint16',   lambda x: x)     if v > 0    else None,
    lambda v:  ('waytype',  'uint8',    lambda x: x)     if v > 0    else None,
    lambda v:  ('own_wtyp', 'uint8',    lambda x: x)     if v > 0    else None,
)
