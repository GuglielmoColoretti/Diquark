# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.1.0 for Linux x86 (64-bit) (June 16, 2022)
# Date: Wed 6 Dec 2023 15:45:49



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

QLQLts1x1 = Parameter(name = 'QLQLts1x1',
                      nature = 'external',
                      type = 'complex',
                      value = 0.1,
                      texname = '\\text{QLQLts1x1}',
                      lhablock = 'DIQ',
                      lhacode = [ 1, 1 ])

QLQLts2x2 = Parameter(name = 'QLQLts2x2',
                      nature = 'external',
                      type = 'complex',
                      value = 0.1,
                      texname = '\\text{QLQLts2x2}',
                      lhablock = 'DIQ',
                      lhacode = [ 2, 2 ])

QLQLts3x3 = Parameter(name = 'QLQLts3x3',
                      nature = 'external',
                      type = 'complex',
                      value = 0.1,
                      texname = '\\text{QLQLts3x3}',
                      lhablock = 'DIQ',
                      lhacode = [ 3, 3 ])

dRdRss1x1 = Parameter(name = 'dRdRss1x1',
                      nature = 'external',
                      type = 'complex',
                      value = 0.1,
                      texname = '\\text{dRdRss1x1}',
                      lhablock = 'DiqdRdRss',
                      lhacode = [ 1, 1 ])

dRdRss2x2 = Parameter(name = 'dRdRss2x2',
                      nature = 'external',
                      type = 'complex',
                      value = 0.1,
                      texname = '\\text{dRdRss2x2}',
                      lhablock = 'DiqdRdRss',
                      lhacode = [ 2, 2 ])

dRdRss3x3 = Parameter(name = 'dRdRss3x3',
                      nature = 'external',
                      type = 'complex',
                      value = 0.1,
                      texname = '\\text{dRdRss3x3}',
                      lhablock = 'DiqdRdRss',
                      lhacode = [ 3, 3 ])

dRdRts1x1 = Parameter(name = 'dRdRts1x1',
                      nature = 'external',
                      type = 'complex',
                      value = 0.1,
                      texname = '\\text{dRdRts1x1}',
                      lhablock = 'DiqdRdRts',
                      lhacode = [ 1, 1 ])

dRdRts2x2 = Parameter(name = 'dRdRts2x2',
                      nature = 'external',
                      type = 'complex',
                      value = 0.1,
                      texname = '\\text{dRdRts2x2}',
                      lhablock = 'DiqdRdRts',
                      lhacode = [ 2, 2 ])

dRdRts3x3 = Parameter(name = 'dRdRts3x3',
                      nature = 'external',
                      type = 'complex',
                      value = 0.1,
                      texname = '\\text{dRdRts3x3}',
                      lhablock = 'DiqdRdRts',
                      lhacode = [ 3, 3 ])

QLdRod1x1 = Parameter(name = 'QLdRod1x1',
                      nature = 'external',
                      type = 'complex',
                      value = 0.1,
                      texname = '\\text{QLdRod1x1}',
                      lhablock = 'DiqQLdRod',
                      lhacode = [ 1, 1 ])

QLdRod2x2 = Parameter(name = 'QLdRod2x2',
                      nature = 'external',
                      type = 'complex',
                      value = 0.1,
                      texname = '\\text{QLdRod2x2}',
                      lhablock = 'DiqQLdRod',
                      lhacode = [ 2, 2 ])

QLdRod3x3 = Parameter(name = 'QLdRod3x3',
                      nature = 'external',
                      type = 'complex',
                      value = 0.1,
                      texname = '\\text{QLdRod3x3}',
                      lhablock = 'DiqQLdRod',
                      lhacode = [ 3, 3 ])

QLQLss1x1 = Parameter(name = 'QLQLss1x1',
                      nature = 'external',
                      type = 'complex',
                      value = 0.1,
                      texname = '\\text{QLQLss1x1}',
                      lhablock = 'DiqQLQLss',
                      lhacode = [ 1, 1 ])

QLQLss2x2 = Parameter(name = 'QLQLss2x2',
                      nature = 'external',
                      type = 'complex',
                      value = 0.1,
                      texname = '\\text{QLQLss2x2}',
                      lhablock = 'DiqQLQLss',
                      lhacode = [ 2, 2 ])

QLQLss3x3 = Parameter(name = 'QLQLss3x3',
                      nature = 'external',
                      type = 'complex',
                      value = 0.1,
                      texname = '\\text{QLQLss3x3}',
                      lhablock = 'DiqQLQLss',
                      lhacode = [ 3, 3 ])

QLQLst1x1 = Parameter(name = 'QLQLst1x1',
                      nature = 'external',
                      type = 'complex',
                      value = 0.1,
                      texname = '\\text{QLQLst1x1}',
                      lhablock = 'DiqQLQLst',
                      lhacode = [ 1, 1 ])

QLQLst2x2 = Parameter(name = 'QLQLst2x2',
                      nature = 'external',
                      type = 'complex',
                      value = 0.1,
                      texname = '\\text{QLQLst2x2}',
                      lhablock = 'DiqQLQLst',
                      lhacode = [ 2, 2 ])

QLQLst3x3 = Parameter(name = 'QLQLst3x3',
                      nature = 'external',
                      type = 'complex',
                      value = 0.1,
                      texname = '\\text{QLQLst3x3}',
                      lhablock = 'DiqQLQLst',
                      lhacode = [ 3, 3 ])

QLQLtt1x1 = Parameter(name = 'QLQLtt1x1',
                      nature = 'external',
                      type = 'complex',
                      value = 0.1,
                      texname = '\\text{QLQLtt1x1}',
                      lhablock = 'DiqQLQLtt',
                      lhacode = [ 1, 1 ])

QLQLtt2x2 = Parameter(name = 'QLQLtt2x2',
                      nature = 'external',
                      type = 'complex',
                      value = 0.1,
                      texname = '\\text{QLQLtt2x2}',
                      lhablock = 'DiqQLQLtt',
                      lhacode = [ 2, 2 ])

QLQLtt3x3 = Parameter(name = 'QLQLtt3x3',
                      nature = 'external',
                      type = 'complex',
                      value = 0.1,
                      texname = '\\text{QLQLtt3x3}',
                      lhablock = 'DiqQLQLtt',
                      lhacode = [ 3, 3 ])

QLuRod1x1 = Parameter(name = 'QLuRod1x1',
                      nature = 'external',
                      type = 'complex',
                      value = 0.1,
                      texname = '\\text{QLuRod1x1}',
                      lhablock = 'DiqQLuRod',
                      lhacode = [ 1, 1 ])

QLuRod2x2 = Parameter(name = 'QLuRod2x2',
                      nature = 'external',
                      type = 'complex',
                      value = 0.1,
                      texname = '\\text{QLuRod2x2}',
                      lhablock = 'DiqQLuRod',
                      lhacode = [ 2, 2 ])

QLuRod3x3 = Parameter(name = 'QLuRod3x3',
                      nature = 'external',
                      type = 'complex',
                      value = 0.1,
                      texname = '\\text{QLuRod3x3}',
                      lhablock = 'DiqQLuRod',
                      lhacode = [ 3, 3 ])

uRdRss1x1 = Parameter(name = 'uRdRss1x1',
                      nature = 'external',
                      type = 'complex',
                      value = 0.1,
                      texname = '\\text{uRdRss1x1}',
                      lhablock = 'DiquRdRss',
                      lhacode = [ 1, 1 ])

uRdRss2x2 = Parameter(name = 'uRdRss2x2',
                      nature = 'external',
                      type = 'complex',
                      value = 0.1,
                      texname = '\\text{uRdRss2x2}',
                      lhablock = 'DiquRdRss',
                      lhacode = [ 2, 2 ])

uRdRss3x3 = Parameter(name = 'uRdRss3x3',
                      nature = 'external',
                      type = 'complex',
                      value = 0.1,
                      texname = '\\text{uRdRss3x3}',
                      lhablock = 'DiquRdRss',
                      lhacode = [ 3, 3 ])

uRdRts1x1 = Parameter(name = 'uRdRts1x1',
                      nature = 'external',
                      type = 'complex',
                      value = 0.1,
                      texname = '\\text{uRdRts1x1}',
                      lhablock = 'DiquRdRts',
                      lhacode = [ 1, 1 ])

uRdRts2x2 = Parameter(name = 'uRdRts2x2',
                      nature = 'external',
                      type = 'complex',
                      value = 0.1,
                      texname = '\\text{uRdRts2x2}',
                      lhablock = 'DiquRdRts',
                      lhacode = [ 2, 2 ])

uRdRts3x3 = Parameter(name = 'uRdRts3x3',
                      nature = 'external',
                      type = 'complex',
                      value = 0.1,
                      texname = '\\text{uRdRts3x3}',
                      lhablock = 'DiquRdRts',
                      lhacode = [ 3, 3 ])

uRuRss1x1 = Parameter(name = 'uRuRss1x1',
                      nature = 'external',
                      type = 'complex',
                      value = 0.1,
                      texname = '\\text{uRuRss1x1}',
                      lhablock = 'DiquRuRss',
                      lhacode = [ 1, 1 ])

uRuRss2x2 = Parameter(name = 'uRuRss2x2',
                      nature = 'external',
                      type = 'complex',
                      value = 0.1,
                      texname = '\\text{uRuRss2x2}',
                      lhablock = 'DiquRuRss',
                      lhacode = [ 2, 2 ])

uRuRss3x3 = Parameter(name = 'uRuRss3x3',
                      nature = 'external',
                      type = 'complex',
                      value = 0.1,
                      texname = '\\text{uRuRss3x3}',
                      lhablock = 'DiquRuRss',
                      lhacode = [ 3, 3 ])

uRuRts1x1 = Parameter(name = 'uRuRts1x1',
                      nature = 'external',
                      type = 'complex',
                      value = 0.1,
                      texname = '\\text{uRuRts1x1}',
                      lhablock = 'DiquRuRts',
                      lhacode = [ 1, 1 ])

uRuRts2x2 = Parameter(name = 'uRuRts2x2',
                      nature = 'external',
                      type = 'complex',
                      value = 0.1,
                      texname = '\\text{uRuRts2x2}',
                      lhablock = 'DiquRuRts',
                      lhacode = [ 2, 2 ])

uRuRts3x3 = Parameter(name = 'uRuRts3x3',
                      nature = 'external',
                      type = 'complex',
                      value = 0.1,
                      texname = '\\text{uRuRts3x3}',
                      lhablock = 'DiquRuRts',
                      lhacode = [ 3, 3 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymdo = Parameter(name = 'ymdo',
                 nature = 'external',
                 type = 'real',
                 value = 0.00504,
                 texname = '\\text{ymdo}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 1 ])

ymup = Parameter(name = 'ymup',
                 nature = 'external',
                 type = 'real',
                 value = 0.00255,
                 texname = '\\text{ymup}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 2 ])

yms = Parameter(name = 'yms',
                nature = 'external',
                type = 'real',
                value = 0.101,
                texname = '\\text{yms}',
                lhablock = 'YUKAWA',
                lhacode = [ 3 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 1.27,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

yme = Parameter(name = 'yme',
                nature = 'external',
                type = 'real',
                value = 0.000511,
                texname = '\\text{yme}',
                lhablock = 'YUKAWA',
                lhacode = [ 11 ])

ymm = Parameter(name = 'ymm',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{ymm}',
                lhablock = 'YUKAWA',
                lhacode = [ 13 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

MdqOD = Parameter(name = 'MdqOD',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{MdqOD}',
                  lhablock = 'MASS',
                  lhacode = [ 9990013 ])

MdqSS = Parameter(name = 'MdqSS',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{MdqSS}',
                  lhablock = 'MASS',
                  lhacode = [ 9990006 ])

MdqSSdR = Parameter(name = 'MdqSSdR',
                    nature = 'external',
                    type = 'real',
                    value = 1,
                    texname = '\\text{MdqSSdR}',
                    lhablock = 'MASS',
                    lhacode = [ 9990010 ])

MdqSSuR = Parameter(name = 'MdqSSuR',
                    nature = 'external',
                    type = 'real',
                    value = 1,
                    texname = '\\text{MdqSSuR}',
                    lhablock = 'MASS',
                    lhacode = [ 9990008 ])

MdqST = Parameter(name = 'MdqST',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{MdqST}',
                  lhablock = 'MASS',
                  lhacode = [ 9990002 ])

MdqTS = Parameter(name = 'MdqTS',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{MdqTS}',
                  lhablock = 'MASS',
                  lhacode = [ 9990007 ])

MdqTSdR = Parameter(name = 'MdqTSdR',
                    nature = 'external',
                    type = 'real',
                    value = 1,
                    texname = '\\text{MdqTSdR}',
                    lhablock = 'MASS',
                    lhacode = [ 9990011 ])

MdqTSuR = Parameter(name = 'MdqTSuR',
                    nature = 'external',
                    type = 'real',
                    value = 1,
                    texname = '\\text{MdqTSuR}',
                    lhablock = 'MASS',
                    lhacode = [ 9990009 ])

MdqTT = Parameter(name = 'MdqTT',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{MdqTT}',
                  lhablock = 'MASS',
                  lhacode = [ 9990005 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.000511,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MMU = Parameter(name = 'MMU',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{MMU}',
                lhablock = 'MASS',
                lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.00255,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.27,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.00504,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.101,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

WDiqODP = Parameter(name = 'WDiqODP',
                    nature = 'external',
                    type = 'real',
                    value = 1,
                    texname = '\\text{WDiqODP}',
                    lhablock = 'DECAY',
                    lhacode = [ 9990012 ])

WDiqODN = Parameter(name = 'WDiqODN',
                    nature = 'external',
                    type = 'real',
                    value = 1,
                    texname = '\\text{WDiqODN}',
                    lhablock = 'DECAY',
                    lhacode = [ 9990013 ])

WDiqSS = Parameter(name = 'WDiqSS',
                   nature = 'external',
                   type = 'real',
                   value = 1,
                   texname = '\\text{WDiqSS}',
                   lhablock = 'DECAY',
                   lhacode = [ 9990006 ])

WDiqSSdR = Parameter(name = 'WDiqSSdR',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{WDiqSSdR}',
                     lhablock = 'DECAY',
                     lhacode = [ 9990010 ])

WDiqSSuR = Parameter(name = 'WDiqSSuR',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{WDiqSSuR}',
                     lhablock = 'DECAY',
                     lhacode = [ 9990008 ])

WDiqSTP = Parameter(name = 'WDiqSTP',
                    nature = 'external',
                    type = 'real',
                    value = 1,
                    texname = '\\text{WDiqSTP}',
                    lhablock = 'DECAY',
                    lhacode = [ 9990000 ])

WDiqSTN = Parameter(name = 'WDiqSTN',
                    nature = 'external',
                    type = 'real',
                    value = 1,
                    texname = '\\text{WDiqSTN}',
                    lhablock = 'DECAY',
                    lhacode = [ 9990001 ])

WDiqSTM = Parameter(name = 'WDiqSTM',
                    nature = 'external',
                    type = 'real',
                    value = 1,
                    texname = '\\text{WDiqSTM}',
                    lhablock = 'DECAY',
                    lhacode = [ 9990002 ])

WDiqTS = Parameter(name = 'WDiqTS',
                   nature = 'external',
                   type = 'real',
                   value = 1,
                   texname = '\\text{WDiqTS}',
                   lhablock = 'DECAY',
                   lhacode = [ 9990007 ])

WDiqTSdR = Parameter(name = 'WDiqTSdR',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{WDiqTSdR}',
                     lhablock = 'DECAY',
                     lhacode = [ 9990011 ])

WDiqTSuR = Parameter(name = 'WDiqTSuR',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{WDiqTSuR}',
                     lhablock = 'DECAY',
                     lhacode = [ 9990009 ])

WDiqTTP = Parameter(name = 'WDiqTTP',
                    nature = 'external',
                    type = 'real',
                    value = 1,
                    texname = '\\text{WDiqTTP}',
                    lhablock = 'DECAY',
                    lhacode = [ 9990003 ])

WDiqTTN = Parameter(name = 'WDiqTTN',
                    nature = 'external',
                    type = 'real',
                    value = 1,
                    texname = '\\text{WDiqTTN}',
                    lhablock = 'DECAY',
                    lhacode = [ 9990004 ])

WDiqTTM = Parameter(name = 'WDiqTTM',
                    nature = 'external',
                    type = 'real',
                    value = 1,
                    texname = '\\text{WDiqTTM}',
                    lhablock = 'DECAY',
                    lhacode = [ 9990005 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.sin(cabi)',
                   texname = '\\text{CKM1x2}')

CKM1x3 = Parameter(name = 'CKM1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM1x3}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-cmath.sin(cabi)',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM2x2}')

CKM2x3 = Parameter(name = 'CKM2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM2x3}')

CKM3x1 = Parameter(name = 'CKM3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x1}')

CKM3x2 = Parameter(name = 'CKM3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x2}')

CKM3x3 = Parameter(name = 'CKM3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '1',
                   texname = '\\text{CKM3x3}')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/vev',
               texname = '\\text{yc}')

ydo = Parameter(name = 'ydo',
                nature = 'internal',
                type = 'real',
                value = '(ymdo*cmath.sqrt(2))/vev',
                texname = '\\text{ydo}')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/vev',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/vev',
               texname = '\\text{ym}')

ys = Parameter(name = 'ys',
               nature = 'internal',
               type = 'real',
               value = '(yms*cmath.sqrt(2))/vev',
               texname = '\\text{ys}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

yup = Parameter(name = 'yup',
                nature = 'internal',
                type = 'real',
                value = '(ymup*cmath.sqrt(2))/vev',
                texname = '\\text{yup}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

