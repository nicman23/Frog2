(S'7a19bd6fb7bb5b402e60abd7b5dcd053'
p1
(ihappydoclib.parseinfo.moduleinfo
ModuleInfo
p2
(dp3
S'_namespaces'
p4
((dp5
S'MolReaderError'
p6
(ihappydoclib.parseinfo.classinfo
ClassInfo
p7
(dp8
g4
((dp9
(dp10
tp11
sS'_filename'
p12
S'../python/frowns/mdl_parsers/sdfile.py'
p13
sS'_docstring'
p14
S''
sS'_class_member_info'
p15
(lp16
sS'_name'
p17
g6
sS'_parent'
p18
g2
sS'_comment_info'
p19
(dp20
sS'_base_class_info'
p21
(lp22
S'Exception'
p23
asS'_configuration_values'
p24
(dp25
sS'_class_info'
p26
g9
sS'_function_info'
p27
g10
sS'_comments'
p28
S''
sbsS'MolReader'
p29
(ihappydoclib.parseinfo.classinfo
ClassInfo
p30
(dp31
g4
((dp32
(dp33
S'get_text'
p34
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p35
(dp36
g4
((dp37
(dp38
tp39
sS'_exception_info'
p40
(dp41
sS'_parameter_names'
p42
(S'self'
p43
tp44
sS'_parameter_info'
p45
(dp46
g43
(NNNtp47
ssg12
g13
sg14
S'->text that formed the last molecule read'
p48
sg17
g34
sg18
g30
sg19
g20
sg24
(dp49
sg26
g37
sg27
g38
sg28
S''
sbsS'_readFields'
p50
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p51
(dp52
g4
((dp53
(dp54
tp55
sg40
(dp56
sg42
(S'self'
p57
S'pattern'
p58
tp59
sg45
(dp60
g58
(I1
S're.compile( ">\\s+<([^>]+)>\\s+\\(*([^)]*)" )'
Ntp61
sg57
(NNNtp62
ssg12
g13
sg14
S'Read the database field component at the end of a molecule\n        record.  Sets a dictionary of key->values'
p63
sg17
g50
sg18
g30
sg19
g20
sg24
(dp64
sg26
g53
sg27
g54
sg28
S''
sbsS'_clear'
p65
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p66
(dp67
g4
((dp68
(dp69
tp70
sg40
(dp71
sg42
(S'self'
p72
tp73
sg45
(dp74
g72
(NNNtp75
ssg12
g13
sg14
S'Clear the _lastlines buffer'
p76
sg17
g65
sg18
g30
sg19
g20
sg24
(dp77
sg26
g68
sg27
g69
sg28
S''
sbsS'_read_to_next'
p78
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p79
(dp80
g4
((dp81
(dp82
tp83
sg40
(dp84
sg42
(S'self'
p85
tp86
sg45
(dp87
g85
(NNNtp88
ssg12
g13
sg14
S''
sg17
g78
sg18
g30
sg19
g20
sg24
(dp89
sg26
g81
sg27
g82
sg28
S''
sbsS'_pushback'
p90
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p91
(dp92
g4
((dp93
(dp94
tp95
sg40
(dp96
sg42
(S'self'
p97
S'line'
p98
tp99
sg45
(dp100
g97
(NNNtp101
sg98
(NNNtp102
ssg12
g13
sg14
S''
sg17
g90
sg18
g30
sg19
g20
sg24
(dp103
sg26
g93
sg27
g94
sg28
S''
sbsS'read_one'
p104
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p105
(dp106
g4
((dp107
(dp108
tp109
sg40
(dp110
sg42
(S'self'
p111
tp112
sg45
(dp113
g111
(NNNtp114
ssg12
g13
sg14
S'Read one molecule from the sd file'
p115
sg17
g104
sg18
g30
sg19
g20
sg24
(dp116
sg26
g107
sg27
g108
sg28
S''
sbsS'get_lines'
p117
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p118
(dp119
g4
((dp120
(dp121
tp122
sg40
(dp123
sg42
(S'self'
p124
tp125
sg45
(dp126
g124
(NNNtp127
ssg12
g13
sg14
S'->the lines of text that formed the last molecule read'
p128
sg17
g117
sg18
g30
sg19
g20
sg24
(dp129
sg26
g120
sg27
g121
sg28
S''
sbsS'readMProps'
p130
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p131
(dp132
g4
((dp133
(dp134
tp135
sg40
(dp136
sg42
(S'self'
p137
tp138
sg45
(dp139
g137
(NNNtp140
ssg12
g13
sg14
S''
sg17
g130
sg18
g30
sg19
g20
sg24
(dp141
sg26
g133
sg27
g134
sg28
S''
sbsS'_readline'
p142
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p143
(dp144
g4
((dp145
(dp146
tp147
sg40
(dp148
S'MolReaderError, "Unexpected end of file"'
p149
Nssg42
(S'self'
p150
S'endOk'
p151
tp152
sg45
(dp153
g151
(I1
S'0'
Ntp154
sg150
(NNNtp155
ssg12
g13
sg14
S'internal readline function, if endOk is 0 then upon an end of\n        line a MolReaderError is generated'
p156
sg17
g142
sg18
g30
sg19
g20
sg24
(dp157
sg26
g145
sg27
g146
sg28
S''
sbsS'_endOfMol'
p158
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p159
(dp160
g4
((dp161
(dp162
tp163
sg40
(dp164
sg42
(S'self'
p165
S'line'
p166
tp167
sg45
(dp168
g165
(NNNtp169
sg166
(NNNtp170
ssg12
g13
sg14
S'(line)-> return 1 if the line signifies the end of molecule\n        0 otherwise'
p171
sg17
g158
sg18
g30
sg19
g20
sg24
(dp172
sg26
g161
sg27
g162
sg28
S''
sbsS'__init__'
p173
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p174
(dp175
g4
((dp176
(dp177
tp178
sg40
(dp179
sg42
(S'self'
p180
S'file'
p181
S'stripHydrogens'
p182
tp183
sg45
(dp184
g180
(NNNtp185
sg181
(NNNtp186
sg182
(I1
S'1'
Ntp187
ssg12
g13
sg14
S''
sg17
g173
sg18
g30
sg19
g20
sg24
(dp188
sg26
g176
sg27
g177
sg28
S''
sbstp189
sg12
g13
sg14
S''
sg15
(lp190
sg17
g29
sg18
g2
sg19
g20
sg21
(lp191
sg24
(dp192
sg26
g32
sg27
g33
sg28
S''
sbs(dp193
S'test'
p194
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p195
(dp196
g4
((dp197
(dp198
tp199
sg40
(dp200
sg42
(tsg45
(dp201
sg12
g13
sg14
S''
sg17
g194
sg18
g2
sg19
g20
sg24
(dp202
sg26
g197
sg27
g198
sg28
S''
sbsS'parse_atom'
p203
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p204
(dp205
g4
((dp206
(dp207
tp208
sg40
(dp209
sg42
(S'line'
p210
tp211
sg45
(dp212
g210
(NNNtp213
ssg12
g13
sg14
S''
sg17
g203
sg18
g2
sg19
g20
sg24
(dp214
sg26
g206
sg27
g207
sg28
S''
sbsS'parse_bond'
p215
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p216
(dp217
g4
((dp218
(dp219
tp220
sg40
(dp221
sg42
(S'line'
p222
tp223
sg45
(dp224
g222
(NNNtp225
ssg12
g13
sg14
S''
sg17
g215
sg18
g2
sg19
g20
sg24
(dp226
sg26
g218
sg27
g219
sg28
S''
sbstp227
sS'_import_info'
p228
(ihappydoclib.parseinfo.imports
ImportInfo
p229
(dp230
S'_named_imports'
p231
(dp232
S'frowns.Molecule'
p233
(lp234
S'Molecule'
p235
asS'frowns.Atom'
p236
(lp237
S'Atom'
p238
asS'frowns.perception'
p239
(lp240
S'TrustedSmiles'
p241
aS'RingDetection'
p242
aS'BasicAromaticity'
p243
asS'frowns.Bond'
p244
(lp245
S'Bond'
p246
assS'_straight_imports'
p247
(lp248
S're'
p249
aS'os'
p250
asbsg12
g13
sg14
S'"""file reader for\nreading sdf (MDL) files\n"""'
p251
sg17
S'sdfile'
p252
sg18
Nsg19
g20
sg24
(dp253
S'include_comments'
p254
I1
sS'cacheFilePrefix'
p255
S'.happydoc.'
p256
sS'useCache'
p257
I1
sS'docStringFormat'
p258
S'StructuredText'
p259
ssg26
g5
sg27
g193
sg28
S''
sbt.