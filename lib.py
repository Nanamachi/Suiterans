# -*- coding= utf-8 -*-
from colordef import *

VERSION = 'v1.0.0'

translate = lambda x,y: y

named_obj = (
    'BRDG',
    'BUIL',
    'CCAR',
    'CRSS',
    'CURS',
    'FIEL',
    'GOOD',
    'GRND',
    'GOBJ',
    'MENU',
    'MISC',
    'PASS',
    'SIGN',
    'SMOK',
    'SYMB',
    'TUNL',
    'TREE',
    'VHCL',
    'WAY' ,
    'WYOB',
)

imaged_obj = (
    'BRDG',
    'BUIL',
    'CCAR',
    'CRSS',
    'FACT',
    'GOBJ',
    'PASS',
    'SIGN',
    'TUNL',
    'TREE',
    'VHCL',
    'WAY' ,
    'WYOB',
)

displayable_node = (
    'name',
    'type',
    'author',
    'cost',
    'intro_year',
    'intro_month',
    'retire_year',
    'retire_month',
    'anim_time',
    'axle_load',
    'brd_ptls',
    'capacity',
    'category',
    'chance',
    'climate',
    'climates',
    'color',
    'const_nx',
    'const_pr',
    'consume',
    'cost_rmv',
    'dist_wt',
    'draw_a_ob',
    'elec_amt',
    'elec_bst',
    'enables',
    'engine',
    'ex_data',
    'exp_min',
    'exp_prob',
    'exp_range',
    'exp_time',
    'factor',
    'fields',
    'fix_cost',
    'flags',
    'flc_cls',
    'frei_imag',
    'g_type',
    'gear',
    'has_way',
    'index',
    'layouts',
    'length',
    'level',
    'load_time',
    'location',
    'mail_bst',
    'mail_dmd',
    'maintain',
    'max_fld',
    'max_hei',
    'max_len',
    'max_wt',
    'min_fld',
    'min_speed',
    'off_left',
    'off_x',
    'off_y',
    'op_anm_t',
    'own_wtyp',
    'pax_bst',
    'pax_dmd',
    'pax_lvl',
    'payload',
    'pdctivity',
    'phasen',
    'pillar_a',
    'pillar_e',
    'pos_x',
    'pos_y',
    'power',
    'price',
    'probablty',
    'prod_p_f',
    'product',
    'range',
    'run_cost',
    'season',
    'size_x',
    'size_y',
    'snow_img',
    'sound',
    'spawn_wt',
    'spd_bonus',
    'speed',
    'start_fld',
    'styp',
    'sup_cnt',
    'supply',
    'top_speed',
    'tree_on',
    'u_type',
    'undergnd',
    'value',
    'waytype',
    'weight',
    'wt_p_unit',
    'xz_anm_t',
    'version',
)

BRDGparam = (
#               attrname,   type,       hook,            version,    None
    lambda v:  ('waytype',  'uint16',   lambda x: x)     if v < 2    else None,
    lambda v:  ('_dummy',   'uint16',   lambda x: x)     if v== 0    else None,
    lambda v:  ('top_speed','uint16',   lambda x: x)     if v > 0    else None,
    lambda v:  ('cost',     'uint32',   lambda x: x/100) if v > -1   else None,
    lambda v:  ('maintain', 'uint32',   lambda x: x/100) if v > 1    else None,
    lambda v:  ('waytype',  'uint8',    lambda x: x)     if v > 1    else None,
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
    lambda v:  ('elec_bst', 'ufix0816', lambda x: x)     if v > 2    else None,
    lambda v:  ('pax_bst',  'ufix0816', lambda x: x)     if v > 2    else None,
    lambda v:  ('mail_bst', 'ufix0816', lambda x: x)     if v > 2    else None,
    lambda v:  ('elec_amt', 'sint16',   lambda x: x)     if v > 2    else None,
    lambda v:  ('pax_dmd',  'sint16',   lambda x: x)     if v > 2    else None,
    lambda v:  ('mail_dmd', 'sint16',   lambda x: x)     if v > 2    else None,
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

IMGparam = (
#               attrname,   type,       hook,            version,    None
    lambda v:  ('x',        'uint8',    lambda x: x)     if v== 0    else None,
    lambda v:  ('x',        'sint16',   lambda x: x)     if v > 0    else None,
    lambda v:  ('y',        'sint16',   lambda x: x)     if v > 0    else None,
    lambda v:  ('width',    'uint8',    lambda x: x)     if v < 3    else None,
    lambda v:  ('width',    'sint16',   lambda x: x)     if v > 2    else None,
    lambda v:  ('y',        'uint8',    lambda x: x)     if v== 0    else None,
    lambda v:  ('_dummy',   'uint8',    lambda x: x)     if v > 2    else None,
    lambda v:  ('height',   'uint8',    lambda x: x)     if v < 3    else None,
    lambda v:  ('height',   'sint16',   lambda x: x)     if v > 2    else None,
    lambda v:  ('_dummy',   'uint8',    lambda x: x)     if 3> v >0  else None,
    lambda v:  ('length',   'uint32',   lambda x: x)     if v== 0    else None,
    lambda v:  ('length',   'uint16',   lambda x: x)     if 3> v >0  else None,
    lambda v:  ('_dummy',   'uint16',   lambda x: x)     if v== 0    else None,
    lambda v:  ('zoomable', 'uint8',    lambda x: x)     if v > -1   else None,
    lambda v:  ('_dummy',   'uint8',    lambda x: x)     if v== 0    else None,
)

IMG1param = (
#               attrname,   type,       hook,            version,    None
    lambda v:  ('count',    'uint16',   lambda x: x)     if v > -1   else None,
    lambda v:  ('_dummy',   'uint16',   lambda x: x)     if v > -1   else None,
)

IMG2param = (
#               attrname,   type,       hook,            version,    None
    lambda v:  ('count',    'uint16',   lambda x: x)     if v > -1   else None,
    lambda v:  ('_dummy',   'uint16',   lambda x: x)     if v > -1   else None,
)

PASSparam = (
#               attrname,   type,       hook,            version,    None
    lambda v:  ('weight',   'uint16',   lambda x: x)     if v > -1   else None,
    lambda v:  ('_dummy',   'uint16',   lambda x: x)     if v > -1   else None,
)

SIGNparam = (
#               attrname,   type,       hook,            version,    None
    lambda v:  ('min_speed','uint16',   lambda x: x)     if v > 0    else None,
    lambda v:  ('cost',     'uint32',   lambda x: x/100) if v > 1    else None,
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
    lambda v:  ('season',   'uint8',    lambda x: x)     if v > 1    else None,
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
    lambda v:  ('gear',     'ufix0616', lambda x: x/100) if v > 5    else None,
    lambda v:  ('gear',     'ufix0608', lambda x: x/100) if 0< v <6  else None,
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
    lambda v:  ('cost',     'uint32',   lambda x: x/100) if v > 0    else None,
    lambda v:  ('maintain', 'uint32',   lambda x: x)     if v > 0    else None,
    lambda v:  ('top_speed','uint32',   lambda x: x)     if v > 0    else None,
    lambda v:  ('intro',    'uint16',   lambda x: x)     if v > 0    else None,
    lambda v:  ('retire',   'uint16',   lambda x: x)     if v > 0    else None,
    lambda v:  ('waytype',  'uint8',    lambda x: x)     if v > 0    else None,
    lambda v:  ('own_wtyp', 'uint8',    lambda x: x)     if v > 0    else None,
)

_trans_word = {
    'name':         translate('parameter','name'),
    'type':         translate('parameter','type'),
    'author':       translate('parameter','author'),
    'cost':         translate('parameter','cost'),
    'intro_year':   translate('parameter','intro_year'),
    'intro_month':  translate('parameter','intro_month'),
    'retire_year':  translate('parameter','retire_year'),
    'retire_month': translate('parameter','retire_month'),
    'anim_time':    translate('parameter','anim_time'),
    'axle_load':    translate('parameter','axle_load'),
    'brd_ptls':     translate('parameter','brd_ptls'),
    'capacity':     translate('parameter','capacity'),
    'category':     translate('parameter','category'),
    'chance':       translate('parameter','chance'),
    'climate':      translate('parameter','climate'),
    'climates':     translate('parameter','climates'),
    'color':        translate('parameter','color'),
    'const_nx':     translate('parameter','const_nx'),
    'const_pr':     translate('parameter','const_pr'),
    'consume':      translate('parameter','consume'),
    'cost_rmv':     translate('parameter','cost_rmv'),
    'dist_wt':      translate('parameter','dist_wt'),
    'draw_a_ob':    translate('parameter','draw_a_ob'),
    'elec_amt':     translate('parameter','elec_amt'),
    'elec_bst':     translate('parameter','elec_bst'),
    'enables':      translate('parameter','enables'),
    'engine':       translate('parameter','engine'),
    'ex_data':      translate('parameter','ex_data'),
    'exp_min':      translate('parameter','exp_min'),
    'exp_prob':     translate('parameter','exp_prob'),
    'exp_range':    translate('parameter','exp_range'),
    'exp_time':     translate('parameter','exp_time'),
    'factor':       translate('parameter','factor'),
    'fields':       translate('parameter','fields'),
    'fix_cost':     translate('parameter','fix_cost'),
    'flags':        translate('parameter','flags'),
    'flc_cls':      translate('parameter','flc_cls'),
    'frei_imag':    translate('parameter','frei_imag'),
    'g_type':       translate('parameter','g_type'),
    'gear':         translate('parameter','gear'),
    'has_way':      translate('parameter','has_way'),
    'index':        translate('parameter','index'),
    'layouts':      translate('parameter','layouts'),
    'length':       translate('parameter','length'),
    'level':        translate('parameter','level'),
    'load_time':    translate('parameter','load_time'),
    'location':     translate('parameter','location'),
    'mail_bst':     translate('parameter','mail_bst'),
    'mail_dmd':     translate('parameter','mail_dmd'),
    'maintain':     translate('parameter','maintain'),
    'max_fld':      translate('parameter','max_fld'),
    'max_hei':      translate('parameter','max_hei'),
    'max_len':      translate('parameter','max_len'),
    'max_wt':       translate('parameter','max_wt'),
    'min_fld':      translate('parameter','min_fld'),
    'min_speed':    translate('parameter','min_speed'),
    'off_left':     translate('parameter','off_left'),
    'off_x':        translate('parameter','off_x'),
    'off_y':        translate('parameter','off_y'),
    'op_anm_t':     translate('parameter','op_anm_t'),
    'own_wtyp':     translate('parameter','own_wtyp'),
    'pax_bst':      translate('parameter','pax_bst'),
    'pax_dmd':      translate('parameter','pax_dmd'),
    'pax_lvl':      translate('parameter','pax_lvl'),
    'payload':      translate('parameter','payload'),
    'pdctivity':    translate('parameter','pdctivity'),
    'phasen':       translate('parameter','phasen'),
    'pillar_a':     translate('parameter','pillar_a'),
    'pillar_e':     translate('parameter','pillar_e'),
    'pos_x':        translate('parameter','pos_x'),
    'pos_y':        translate('parameter','pos_y'),
    'power':        translate('parameter','power'),
    'price':        translate('parameter','price'),
    'probablty':    translate('parameter','probablty'),
    'prod_p_f':     translate('parameter','prod_p_f'),
    'product':      translate('parameter','product'),
    'range':        translate('parameter','range'),
    'run_cost':     translate('parameter','run_cost'),
    'season':       translate('parameter','season'),
    'size_x':       translate('parameter','size_x'),
    'size_y':       translate('parameter','size_y'),
    'snow_img':     translate('parameter','snow_img'),
    'sound':        translate('parameter','sound'),
    'spawn_wt':     translate('parameter','spawn_wt'),
    'spd_bonus':    translate('parameter','spd_bonus'),
    'speed':        translate('parameter','speed'),
    'start_fld':    translate('parameter','start_fld'),
    'styp':         translate('parameter','styp'),
    'sup_cnt':      translate('parameter','sup_cnt'),
    'supply':       translate('parameter','supply'),
    'top_speed':    translate('parameter','top_speed'),
    'tree_on':      translate('parameter','tree_on'),
    'u_type':       translate('parameter','u_type'),
    'undergnd':     translate('parameter','undergnd'),
    'value':        translate('parameter','value'),
    'waytype':      translate('parameter','waytype'),
    'weight':       translate('parameter','weight'),
    'wt_p_unit':    translate('parameter','wt_p_unit'),
    'xz_anm_t':     translate('parameter','xz_anm_t'),
    'version':      translate('parameter','version'),
    '__UnDefined__':translate('parameter','__UnDefined__'),
}
