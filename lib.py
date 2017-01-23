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

imaged_obj = (
    'VHCL'
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

special_color = (
	0x244B67, # Player color 1
	0x395E7C,
	0x4C7191,
	0x6084A7,
	0x7497BD,
	0x88ABD3,
	0x9CBEE9,
	0xB0D2FF,

	0x7B5803, # Player color 2
	0x8E6F04,
	0xA18605,
	0xB49D07,
	0xC6B408,
	0xD9CB0A,
	0xECE20B,
	0xFFF90D,

	0x57656F, # Dark windows, lit yellowish at night
	0x7F9BF1, # Lighter windows, lit blueish at night
	0xFFFF53, # Yellow light
	0xFF211D, # Red light
	0x01DD01, # Green light
	0x6B6B6B, # Non-darkening grey 1 (menus)
	0x9B9B9B, # Non-darkening grey 2 (menus)
	0xB3B3B3, # non-darkening grey 3 (menus)
	0xC9C9C9, # Non-darkening grey 4 (menus)
	0xDFDFDF, # Non-darkening grey 5 (menus)
	0xE3E3FF, # Nearly white light at day, yellowish light at night
	0xC1B1D1, # Windows, lit yellow
	0x4D4D4D, # Windows, lit yellow
	0xFF017F, # purple light
	0x0101FF, # blue light
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

IMGparam = (
#               attrname,   type,       hook,            version,    None
    lambda v:  ('x',        'uint8',    lambda x: x)     if v== 0    else None,
    lambda v:  ('x',        'sint16',   lambda x: x)     if v > 0    else None,
    lambda v:  ('y',        'sint16',   lambda x: x)     if v > 0    else None,
    lambda v:  ('width',    'uint8',    lambda x: x)     if v < 3    else None,
    lambda v:  ('width',    'sint16',   lambda x: x)     if v > 2    else None,
    lambda v:  ('y',        'uint8',    lambda x: x)     if v== 0    else None,
    lambda v:  ('height',   'uint8',    lambda x: x)     if v < 3    else None,
    lambda v:  ('height',   'sint16',   lambda x: x)     if v > 2    else None,
    lambda v:  ('_dummy',   'uint8',    lambda x: x)     if v > 0    else None,
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
