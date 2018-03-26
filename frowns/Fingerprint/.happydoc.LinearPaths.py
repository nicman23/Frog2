(S'a6daa8de39f9307bb858f3b3e0a78023'
p1
(ihappydoclib.parseinfo.moduleinfo
ModuleInfo
p2
(dp3
S'_namespaces'
p4
((dp5
S'SplitFingerprintGenerator'
p6
(ihappydoclib.parseinfo.classinfo
ClassInfo
p7
(dp8
g4
((dp9
(dp10
S'createFP'
p11
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p12
(dp13
g4
((dp14
(dp15
tp16
sS'_exception_info'
p17
(dp18
sS'_parameter_names'
p19
(S'self'
p20
S'molecule'
p21
tp22
sS'_parameter_info'
p23
(dp24
g20
(NNNtp25
sg21
(NNNtp26
ssS'_filename'
p27
S'../python/frowns/Fingerprint/LinearPaths.py'
p28
sS'_docstring'
p29
S''
sS'_name'
p30
g11
sS'_parent'
p31
g7
sS'_comment_info'
p32
(dp33
(S'name_atom'
tp34
S' XXX FIX ME\n A simple optimization is to cache all the names before\n the dfs walk.\n There are more optimizations for later...\n'
p35
ssS'_configuration_values'
p36
(dp37
sS'_class_info'
p38
g14
sS'_function_info'
p39
g15
sS'_comments'
p40
S''
sbsS'__init__'
p41
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p42
(dp43
g4
((dp44
(dp45
tp46
sg17
(dp47
sg19
(S'self'
p48
S'maxdepth'
p49
S'integersPerAtoms'
p50
tp51
sg23
(dp52
g48
(NNNtp53
sg50
(I1
S'[ 4 ] * 6'
Ntp54
sg49
(I1
S'7'
Ntp55
ssg27
g28
sg29
S''
sg30
g41
sg31
g7
sg32
g33
sg36
(dp56
sg38
g44
sg39
g45
sg40
S''
sbstp57
sg27
g28
sg29
S''
sS'_class_member_info'
p58
(lp59
sg30
g6
sg31
g2
sg32
g33
sS'_base_class_info'
p60
(lp61
sg36
(dp62
sg38
g9
sg39
g10
sg40
S''
sbs(dp63
S'generatePaths'
p64
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p65
(dp66
g4
((dp67
(dp68
tp69
sg17
(dp70
sg19
(S'molecule'
p71
S'maxdepth'
p72
S'name_atom'
p73
S'name_bond'
p74
tp75
sg23
(dp76
g74
(I1
S'name_bond'
Ntp77
sg71
(NNNtp78
sg72
(I1
S'5'
Ntp79
sg73
(I1
S'name_atom'
Ntp80
ssg27
g28
sg29
S'(molecule, maxdepth, *name_atom, *name_bond) -> linear paths\n    Generate all linear paths through a molecule up to maxdepth\n    change name_atom and name_bond to name the atoms and bonds\n    in the molecule\n\n    name_atom and name_bond must return a stringable value'
p81
sg30
g64
sg31
g2
sg32
g33
sg36
(dp82
sg38
g67
sg39
g68
sg40
S''
sbsS'name_bond'
p83
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p84
(dp85
g4
((dp86
(dp87
tp88
sg17
(dp89
sg19
(S'bond'
p90
S'lookup'
p91
tp92
sg23
(dp93
g91
(I1
S"{ 1 : '-', 2 : '=', 3 : '#', 4 : '~' }"
Ntp94
sg90
(NNNtp95
ssg27
g28
sg29
S''
sg30
g83
sg31
g2
sg32
g33
sg36
(dp96
sg38
g86
sg39
g87
sg40
S''
sbsS'name_atom'
p97
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p98
(dp99
g4
((dp100
(dp101
tp102
sg17
(dp103
sg19
(S'atom'
p104
tp105
sg23
(dp106
g104
(NNNtp107
ssg27
g28
sg29
S''
sg30
g97
sg31
g2
sg32
g33
sg36
(dp108
sg38
g100
sg39
g101
sg40
g35
sbsS'_dfswalk'
p109
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p110
(dp111
g4
((dp112
(dp113
tp114
sg17
(dp115
sg19
(S'atom'
p116
S'visitedAtoms'
p117
S'path'
p118
S'paths'
p119
S'depth'
p120
S'maxdepth'
p121
S'name_atom'
p122
S'name_bond'
p123
tp124
sg23
(dp125
g119
(NNNtp126
sg122
(NNNtp127
sg120
(NNNtp128
sg121
(NNNtp129
sg123
(NNNtp130
sg116
(NNNtp131
sg117
(NNNtp132
sg118
(NNNtp133
ssg27
g28
sg29
S''
sg30
g109
sg31
g2
sg32
g33
sg36
(dp134
sg38
g112
sg39
g113
sg40
S''
sbstp135
sS'_import_info'
p136
(ihappydoclib.parseinfo.imports
ImportInfo
p137
(dp138
S'_named_imports'
p139
(dp140
S'Fingerprint'
p141
(lp142
S'*'
assS'_straight_imports'
p143
(lp144
sbsg27
g28
sg29
S'"""Linear Paths\n\nGenerate linear paths for a molecule.\n\nFor example, generate all linear paths up to depth 5\npaths = generatePaths(molecule, maxdepth=5)\n\nThese paths can be used for a variety of cases, but we are using\nthem for the purposes of fingerprinting molecules.\nSee Fingerprint.py\n"""'
p145
sg30
S'LinearPaths'
p146
sg31
Nsg32
g33
sg36
(dp147
S'include_comments'
p148
I1
sS'cacheFilePrefix'
p149
S'.happydoc.'
p150
sS'useCache'
p151
I1
sS'docStringFormat'
p152
S'StructuredText'
p153
ssg38
g5
sg39
g63
sg40
S''
sbt.