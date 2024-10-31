# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.1.0 for Linux x86 (64-bit) (June 16, 2022)
# Date: Wed 6 Dec 2023 15:45:49


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '2*dRdRss1x1*complex(0,1)',
                order = {'QCD':1})

GC_2 = Coupling(name = 'GC_2',
                value = '2*dRdRss2x2*complex(0,1)',
                order = {'QCD':1})

GC_3 = Coupling(name = 'GC_3',
                value = '2*dRdRss3x3*complex(0,1)',
                order = {'QCD':1})

GC_4 = Coupling(name = 'GC_4',
                value = '-((dRdRts1x1*complex(0,1))/cmath.sqrt(2)) - (dRdRts2x2*complex(0,1))/cmath.sqrt(2)',
                order = {'QCD':1})

GC_5 = Coupling(name = 'GC_5',
                value = '(dRdRts1x1*complex(0,1))/cmath.sqrt(2) + (dRdRts3x3*complex(0,1))/cmath.sqrt(2)',
                order = {'QCD':1})

GC_6 = Coupling(name = 'GC_6',
                value = '(dRdRts2x2*complex(0,1))/cmath.sqrt(2) + (dRdRts3x3*complex(0,1))/cmath.sqrt(2)',
                order = {'QCD':1})

GC_7 = Coupling(name = 'GC_7',
                value = '-0.3333333333333333*(ee*complex(0,1))',
                order = {'QED':1})

GC_8 = Coupling(name = 'GC_8',
                value = '(ee*complex(0,1))/3.',
                order = {'QED':1})

GC_9 = Coupling(name = 'GC_9',
                value = '(-2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_10 = Coupling(name = 'GC_10',
                 value = '(2*ee*complex(0,1))/3.',
                 order = {'QED':1})

GC_11 = Coupling(name = 'GC_11',
                 value = '-(ee*complex(0,1))',
                 order = {'QED':1})

GC_12 = Coupling(name = 'GC_12',
                 value = 'ee*complex(0,1)',
                 order = {'QED':1})

GC_13 = Coupling(name = 'GC_13',
                 value = '(-4*ee*complex(0,1))/3.',
                 order = {'QED':1})

GC_14 = Coupling(name = 'GC_14',
                 value = '(4*ee*complex(0,1))/3.',
                 order = {'QED':1})

GC_15 = Coupling(name = 'GC_15',
                 value = '(2*ee**2*complex(0,1))/9.',
                 order = {'QED':2})

GC_16 = Coupling(name = 'GC_16',
                 value = '(8*ee**2*complex(0,1))/9.',
                 order = {'QED':2})

GC_17 = Coupling(name = 'GC_17',
                 value = 'ee**2*complex(0,1)',
                 order = {'QED':2})

GC_18 = Coupling(name = 'GC_18',
                 value = '2*ee**2*complex(0,1)',
                 order = {'QED':2})

GC_19 = Coupling(name = 'GC_19',
                 value = '(32*ee**2*complex(0,1))/9.',
                 order = {'QED':2})

GC_20 = Coupling(name = 'GC_20',
                 value = '-0.5*ee**2/cw',
                 order = {'QED':2})

GC_21 = Coupling(name = 'GC_21',
                 value = '(ee**2*complex(0,1))/(2.*cw)',
                 order = {'QED':2})

GC_22 = Coupling(name = 'GC_22',
                 value = 'ee**2/(2.*cw)',
                 order = {'QED':2})

GC_23 = Coupling(name = 'GC_23',
                 value = '-((ee**2*complex(0,1))/(cw*cmath.sqrt(2)))',
                 order = {'QED':2})

GC_24 = Coupling(name = 'GC_24',
                 value = '-G',
                 order = {'QCD':1})

GC_25 = Coupling(name = 'GC_25',
                 value = '-(complex(0,1)*G)',
                 order = {'QCD':1})

GC_26 = Coupling(name = 'GC_26',
                 value = 'complex(0,1)*G',
                 order = {'QCD':1})

GC_27 = Coupling(name = 'GC_27',
                 value = 'G',
                 order = {'QCD':1})

GC_28 = Coupling(name = 'GC_28',
                 value = '-2*ee*G',
                 order = {'QCD':1,'QED':1})

GC_29 = Coupling(name = 'GC_29',
                 value = '(-2*ee*complex(0,1)*G)/3.',
                 order = {'QCD':1,'QED':1})

GC_30 = Coupling(name = 'GC_30',
                 value = '(2*ee*complex(0,1)*G)/3.',
                 order = {'QCD':1,'QED':1})

GC_31 = Coupling(name = 'GC_31',
                 value = '(-4*ee*complex(0,1)*G)/3.',
                 order = {'QCD':1,'QED':1})

GC_32 = Coupling(name = 'GC_32',
                 value = '(4*ee*complex(0,1)*G)/3.',
                 order = {'QCD':1,'QED':1})

GC_33 = Coupling(name = 'GC_33',
                 value = '(-8*ee*complex(0,1)*G)/3.',
                 order = {'QCD':1,'QED':1})

GC_34 = Coupling(name = 'GC_34',
                 value = '(8*ee*complex(0,1)*G)/3.',
                 order = {'QCD':1,'QED':1})

GC_35 = Coupling(name = 'GC_35',
                 value = 'complex(0,1)*G**2',
                 order = {'QCD':2})

GC_36 = Coupling(name = 'GC_36',
                 value = '-2*complex(0,1)*lam',
                 order = {'QED':2})

GC_37 = Coupling(name = 'GC_37',
                 value = '-4*complex(0,1)*lam',
                 order = {'QED':2})

GC_38 = Coupling(name = 'GC_38',
                 value = '-6*complex(0,1)*lam',
                 order = {'QED':2})

GC_39 = Coupling(name = 'GC_39',
                 value = 'complex(0,1)*QLdRod1x1',
                 order = {'QCD':1})

GC_40 = Coupling(name = 'GC_40',
                 value = 'complex(0,1)*QLdRod2x2',
                 order = {'QCD':1})

GC_41 = Coupling(name = 'GC_41',
                 value = 'complex(0,1)*QLdRod3x3',
                 order = {'QCD':1})

GC_42 = Coupling(name = 'GC_42',
                 value = '-(CKM1x1*complex(0,1)*QLQLss1x1) - CKM2x1*complex(0,1)*QLQLss2x2 - CKM1x1*complex(0,1)*QLQLss3x3 - CKM2x1*complex(0,1)*QLQLss3x3',
                 order = {'QCD':1})

GC_43 = Coupling(name = 'GC_43',
                 value = '-(CKM1x2*complex(0,1)*QLQLss1x1) - CKM2x2*complex(0,1)*QLQLss2x2 - CKM1x2*complex(0,1)*QLQLss3x3 - CKM2x2*complex(0,1)*QLQLss3x3',
                 order = {'QCD':1})

GC_44 = Coupling(name = 'GC_44',
                 value = '-(CKM1x3*complex(0,1)*QLQLss1x1) - CKM2x3*complex(0,1)*QLQLss2x2 - CKM1x3*complex(0,1)*QLQLss3x3 - CKM2x3*complex(0,1)*QLQLss3x3',
                 order = {'QCD':1})

GC_45 = Coupling(name = 'GC_45',
                 value = 'CKM2x1*complex(0,1)*QLQLss1x1 + CKM3x1*complex(0,1)*QLQLss1x1 + CKM2x1*complex(0,1)*QLQLss2x2 + CKM3x1*complex(0,1)*QLQLss3x3',
                 order = {'QCD':1})

GC_46 = Coupling(name = 'GC_46',
                 value = '-(CKM1x1*complex(0,1)*QLQLss1x1) - CKM1x1*complex(0,1)*QLQLss2x2 + CKM3x1*complex(0,1)*QLQLss2x2 + CKM3x1*complex(0,1)*QLQLss3x3',
                 order = {'QCD':1})

GC_47 = Coupling(name = 'GC_47',
                 value = 'CKM2x2*complex(0,1)*QLQLss1x1 + CKM3x2*complex(0,1)*QLQLss1x1 + CKM2x2*complex(0,1)*QLQLss2x2 + CKM3x2*complex(0,1)*QLQLss3x3',
                 order = {'QCD':1})

GC_48 = Coupling(name = 'GC_48',
                 value = '-(CKM1x2*complex(0,1)*QLQLss1x1) - CKM1x2*complex(0,1)*QLQLss2x2 + CKM3x2*complex(0,1)*QLQLss2x2 + CKM3x2*complex(0,1)*QLQLss3x3',
                 order = {'QCD':1})

GC_49 = Coupling(name = 'GC_49',
                 value = 'CKM2x3*complex(0,1)*QLQLss1x1 + CKM3x3*complex(0,1)*QLQLss1x1 + CKM2x3*complex(0,1)*QLQLss2x2 + CKM3x3*complex(0,1)*QLQLss3x3',
                 order = {'QCD':1})

GC_50 = Coupling(name = 'GC_50',
                 value = '-(CKM1x3*complex(0,1)*QLQLss1x1) - CKM1x3*complex(0,1)*QLQLss2x2 + CKM3x3*complex(0,1)*QLQLss2x2 + CKM3x3*complex(0,1)*QLQLss3x3',
                 order = {'QCD':1})

GC_51 = Coupling(name = 'GC_51',
                 value = 'complex(0,1)*QLQLst1x1*cmath.sqrt(2)',
                 order = {'QCD':1})

GC_52 = Coupling(name = 'GC_52',
                 value = '-(CKM1x1*complex(0,1)*QLQLst1x1)',
                 order = {'QCD':1})

GC_53 = Coupling(name = 'GC_53',
                 value = '-(CKM1x2*complex(0,1)*QLQLst1x1)',
                 order = {'QCD':1})

GC_54 = Coupling(name = 'GC_54',
                 value = '-(CKM1x3*complex(0,1)*QLQLst1x1)',
                 order = {'QCD':1})

GC_55 = Coupling(name = 'GC_55',
                 value = 'complex(0,1)*QLQLst2x2*cmath.sqrt(2)',
                 order = {'QCD':1})

GC_56 = Coupling(name = 'GC_56',
                 value = '-(CKM2x1*complex(0,1)*QLQLst2x2)',
                 order = {'QCD':1})

GC_57 = Coupling(name = 'GC_57',
                 value = '-(CKM2x2*complex(0,1)*QLQLst2x2)',
                 order = {'QCD':1})

GC_58 = Coupling(name = 'GC_58',
                 value = '-(CKM2x3*complex(0,1)*QLQLst2x2)',
                 order = {'QCD':1})

GC_59 = Coupling(name = 'GC_59',
                 value = 'complex(0,1)*QLQLst3x3*cmath.sqrt(2)',
                 order = {'QCD':1})

GC_60 = Coupling(name = 'GC_60',
                 value = '-(CKM3x1*complex(0,1)*QLQLst3x3)',
                 order = {'QCD':1})

GC_61 = Coupling(name = 'GC_61',
                 value = '-(CKM3x2*complex(0,1)*QLQLst3x3)',
                 order = {'QCD':1})

GC_62 = Coupling(name = 'GC_62',
                 value = '-(CKM3x3*complex(0,1)*QLQLst3x3)',
                 order = {'QCD':1})

GC_63 = Coupling(name = 'GC_63',
                 value = '-(CKM1x1**2*complex(0,1)*QLQLst1x1*cmath.sqrt(2)) - CKM2x1**2*complex(0,1)*QLQLst2x2*cmath.sqrt(2) - CKM3x1**2*complex(0,1)*QLQLst3x3*cmath.sqrt(2)',
                 order = {'QCD':1})

GC_64 = Coupling(name = 'GC_64',
                 value = '-(CKM1x1*CKM1x2*complex(0,1)*QLQLst1x1*cmath.sqrt(2)) - CKM2x1*CKM2x2*complex(0,1)*QLQLst2x2*cmath.sqrt(2) - CKM3x1*CKM3x2*complex(0,1)*QLQLst3x3*cmath.sqrt(2)',
                 order = {'QCD':1})

GC_65 = Coupling(name = 'GC_65',
                 value = '-(CKM1x2**2*complex(0,1)*QLQLst1x1*cmath.sqrt(2)) - CKM2x2**2*complex(0,1)*QLQLst2x2*cmath.sqrt(2) - CKM3x2**2*complex(0,1)*QLQLst3x3*cmath.sqrt(2)',
                 order = {'QCD':1})

GC_66 = Coupling(name = 'GC_66',
                 value = '-(CKM1x1*CKM1x3*complex(0,1)*QLQLst1x1*cmath.sqrt(2)) - CKM2x1*CKM2x3*complex(0,1)*QLQLst2x2*cmath.sqrt(2) - CKM3x1*CKM3x3*complex(0,1)*QLQLst3x3*cmath.sqrt(2)',
                 order = {'QCD':1})

GC_67 = Coupling(name = 'GC_67',
                 value = '-(CKM1x2*CKM1x3*complex(0,1)*QLQLst1x1*cmath.sqrt(2)) - CKM2x2*CKM2x3*complex(0,1)*QLQLst2x2*cmath.sqrt(2) - CKM3x2*CKM3x3*complex(0,1)*QLQLst3x3*cmath.sqrt(2)',
                 order = {'QCD':1})

GC_68 = Coupling(name = 'GC_68',
                 value = '-(CKM1x3**2*complex(0,1)*QLQLst1x1*cmath.sqrt(2)) - CKM2x3**2*complex(0,1)*QLQLst2x2*cmath.sqrt(2) - CKM3x3**2*complex(0,1)*QLQLst3x3*cmath.sqrt(2)',
                 order = {'QCD':1})

GC_69 = Coupling(name = 'GC_69',
                 value = 'CKM1x1*complex(0,1)*QLQLts1x1*cmath.sqrt(2)',
                 order = {'QCD':1})

GC_70 = Coupling(name = 'GC_70',
                 value = 'CKM1x2*complex(0,1)*QLQLts1x1*cmath.sqrt(2)',
                 order = {'QCD':1})

GC_71 = Coupling(name = 'GC_71',
                 value = 'CKM1x3*complex(0,1)*QLQLts1x1*cmath.sqrt(2)',
                 order = {'QCD':1})

GC_72 = Coupling(name = 'GC_72',
                 value = '-(CKM2x1*complex(0,1)*QLQLts2x2*cmath.sqrt(2))',
                 order = {'QCD':1})

GC_73 = Coupling(name = 'GC_73',
                 value = '-(CKM2x2*complex(0,1)*QLQLts2x2*cmath.sqrt(2))',
                 order = {'QCD':1})

GC_74 = Coupling(name = 'GC_74',
                 value = 'CKM2x3*complex(0,1)*QLQLts2x2*cmath.sqrt(2)',
                 order = {'QCD':1})

GC_75 = Coupling(name = 'GC_75',
                 value = 'CKM3x1*complex(0,1)*QLQLts3x3*cmath.sqrt(2)',
                 order = {'QCD':1})

GC_76 = Coupling(name = 'GC_76',
                 value = 'CKM3x2*complex(0,1)*QLQLts3x3*cmath.sqrt(2)',
                 order = {'QCD':1})

GC_77 = Coupling(name = 'GC_77',
                 value = 'CKM3x3*complex(0,1)*QLQLts3x3*cmath.sqrt(2)',
                 order = {'QCD':1})

GC_78 = Coupling(name = 'GC_78',
                 value = '(complex(0,1)*QLQLtt1x1)/2. + (complex(0,1)*QLQLtt2x2)/2.',
                 order = {'QCD':1})

GC_79 = Coupling(name = 'GC_79',
                 value = '-0.5*(complex(0,1)*QLQLtt2x2) - (complex(0,1)*QLQLtt3x3)/2.',
                 order = {'QCD':1})

GC_80 = Coupling(name = 'GC_80',
                 value = '(complex(0,1)*QLQLtt1x1)/2. + (complex(0,1)*QLQLtt3x3)/2.',
                 order = {'QCD':1})

GC_81 = Coupling(name = 'GC_81',
                 value = '(CKM1x1*complex(0,1)*QLQLtt1x1)/(2.*cmath.sqrt(2)) + (CKM2x1*complex(0,1)*QLQLtt2x2)/(2.*cmath.sqrt(2)) + (CKM1x1*complex(0,1)*QLQLtt3x3)/(2.*cmath.sqrt(2)) + (CKM2x1*complex(0,1)*QLQLtt3x3)/(2.*cmath.sqrt(2))',
                 order = {'QCD':1})

GC_82 = Coupling(name = 'GC_82',
                 value = '(CKM1x2*complex(0,1)*QLQLtt1x1)/(2.*cmath.sqrt(2)) + (CKM2x2*complex(0,1)*QLQLtt2x2)/(2.*cmath.sqrt(2)) + (CKM1x2*complex(0,1)*QLQLtt3x3)/(2.*cmath.sqrt(2)) + (CKM2x2*complex(0,1)*QLQLtt3x3)/(2.*cmath.sqrt(2))',
                 order = {'QCD':1})

GC_83 = Coupling(name = 'GC_83',
                 value = '(CKM1x3*complex(0,1)*QLQLtt1x1)/(2.*cmath.sqrt(2)) + (CKM2x3*complex(0,1)*QLQLtt2x2)/(2.*cmath.sqrt(2)) + (CKM1x3*complex(0,1)*QLQLtt3x3)/(2.*cmath.sqrt(2)) + (CKM2x3*complex(0,1)*QLQLtt3x3)/(2.*cmath.sqrt(2))',
                 order = {'QCD':1})

GC_84 = Coupling(name = 'GC_84',
                 value = '-0.5*(CKM2x1*complex(0,1)*QLQLtt1x1)/cmath.sqrt(2) - (CKM3x1*complex(0,1)*QLQLtt1x1)/(2.*cmath.sqrt(2)) - (CKM2x1*complex(0,1)*QLQLtt2x2)/(2.*cmath.sqrt(2)) - (CKM3x1*complex(0,1)*QLQLtt3x3)/(2.*cmath.sqrt(2))',
                 order = {'QCD':1})

GC_85 = Coupling(name = 'GC_85',
                 value = '-0.5*(CKM1x1*complex(0,1)*QLQLtt1x1)/cmath.sqrt(2) - (CKM1x1*complex(0,1)*QLQLtt2x2)/(2.*cmath.sqrt(2)) + (CKM3x1*complex(0,1)*QLQLtt2x2)/(2.*cmath.sqrt(2)) + (CKM3x1*complex(0,1)*QLQLtt3x3)/(2.*cmath.sqrt(2))',
                 order = {'QCD':1})

GC_86 = Coupling(name = 'GC_86',
                 value = '-0.5*(CKM2x2*complex(0,1)*QLQLtt1x1)/cmath.sqrt(2) - (CKM3x2*complex(0,1)*QLQLtt1x1)/(2.*cmath.sqrt(2)) - (CKM2x2*complex(0,1)*QLQLtt2x2)/(2.*cmath.sqrt(2)) - (CKM3x2*complex(0,1)*QLQLtt3x3)/(2.*cmath.sqrt(2))',
                 order = {'QCD':1})

GC_87 = Coupling(name = 'GC_87',
                 value = '-0.5*(CKM1x2*complex(0,1)*QLQLtt1x1)/cmath.sqrt(2) - (CKM1x2*complex(0,1)*QLQLtt2x2)/(2.*cmath.sqrt(2)) + (CKM3x2*complex(0,1)*QLQLtt2x2)/(2.*cmath.sqrt(2)) + (CKM3x2*complex(0,1)*QLQLtt3x3)/(2.*cmath.sqrt(2))',
                 order = {'QCD':1})

GC_88 = Coupling(name = 'GC_88',
                 value = '-0.5*(CKM1x2*CKM2x1*complex(0,1)*QLQLtt1x1) + (CKM1x1*CKM2x2*complex(0,1)*QLQLtt1x1)/2. - (CKM1x2*CKM3x1*complex(0,1)*QLQLtt1x1)/2. + (CKM1x1*CKM3x2*complex(0,1)*QLQLtt1x1)/2. - (CKM1x2*CKM2x1*complex(0,1)*QLQLtt2x2)/2. + (CKM1x1*CKM2x2*complex(0,1)*QLQLtt2x2)/2. - (CKM2x2*CKM3x1*complex(0,1)*QLQLtt2x2)/2. + (CKM2x1*CKM3x2*complex(0,1)*QLQLtt2x2)/2. - (CKM1x2*CKM3x1*complex(0,1)*QLQLtt3x3)/2. - (CKM2x2*CKM3x1*complex(0,1)*QLQLtt3x3)/2. + (CKM1x1*CKM3x2*complex(0,1)*QLQLtt3x3)/2. + (CKM2x1*CKM3x2*complex(0,1)*QLQLtt3x3)/2.',
                 order = {'QCD':1})

GC_89 = Coupling(name = 'GC_89',
                 value = '-0.5*(CKM2x3*complex(0,1)*QLQLtt1x1)/cmath.sqrt(2) - (CKM3x3*complex(0,1)*QLQLtt1x1)/(2.*cmath.sqrt(2)) - (CKM2x3*complex(0,1)*QLQLtt2x2)/(2.*cmath.sqrt(2)) - (CKM3x3*complex(0,1)*QLQLtt3x3)/(2.*cmath.sqrt(2))',
                 order = {'QCD':1})

GC_90 = Coupling(name = 'GC_90',
                 value = '(CKM1x3*complex(0,1)*QLQLtt1x1)/(2.*cmath.sqrt(2)) + (CKM1x3*complex(0,1)*QLQLtt2x2)/(2.*cmath.sqrt(2)) - (CKM3x3*complex(0,1)*QLQLtt2x2)/(2.*cmath.sqrt(2)) - (CKM3x3*complex(0,1)*QLQLtt3x3)/(2.*cmath.sqrt(2))',
                 order = {'QCD':1})

GC_91 = Coupling(name = 'GC_91',
                 value = '(CKM1x3*CKM2x1*complex(0,1)*QLQLtt1x1)/2. - (CKM1x1*CKM2x3*complex(0,1)*QLQLtt1x1)/2. + (CKM1x3*CKM3x1*complex(0,1)*QLQLtt1x1)/2. - (CKM1x1*CKM3x3*complex(0,1)*QLQLtt1x1)/2. + (CKM1x3*CKM2x1*complex(0,1)*QLQLtt2x2)/2. - (CKM1x1*CKM2x3*complex(0,1)*QLQLtt2x2)/2. + (CKM2x3*CKM3x1*complex(0,1)*QLQLtt2x2)/2. - (CKM2x1*CKM3x3*complex(0,1)*QLQLtt2x2)/2. + (CKM1x3*CKM3x1*complex(0,1)*QLQLtt3x3)/2. + (CKM2x3*CKM3x1*complex(0,1)*QLQLtt3x3)/2. - (CKM1x1*CKM3x3*complex(0,1)*QLQLtt3x3)/2. - (CKM2x1*CKM3x3*complex(0,1)*QLQLtt3x3)/2.',
                 order = {'QCD':1})

GC_92 = Coupling(name = 'GC_92',
                 value = '(CKM1x3*CKM2x2*complex(0,1)*QLQLtt1x1)/2. - (CKM1x2*CKM2x3*complex(0,1)*QLQLtt1x1)/2. + (CKM1x3*CKM3x2*complex(0,1)*QLQLtt1x1)/2. - (CKM1x2*CKM3x3*complex(0,1)*QLQLtt1x1)/2. + (CKM1x3*CKM2x2*complex(0,1)*QLQLtt2x2)/2. - (CKM1x2*CKM2x3*complex(0,1)*QLQLtt2x2)/2. + (CKM2x3*CKM3x2*complex(0,1)*QLQLtt2x2)/2. - (CKM2x2*CKM3x3*complex(0,1)*QLQLtt2x2)/2. + (CKM1x3*CKM3x2*complex(0,1)*QLQLtt3x3)/2. + (CKM2x3*CKM3x2*complex(0,1)*QLQLtt3x3)/2. - (CKM1x2*CKM3x3*complex(0,1)*QLQLtt3x3)/2. - (CKM2x2*CKM3x3*complex(0,1)*QLQLtt3x3)/2.',
                 order = {'QCD':1})

GC_93 = Coupling(name = 'GC_93',
                 value = 'complex(0,1)*QLuRod1x1',
                 order = {'QCD':1})

GC_94 = Coupling(name = 'GC_94',
                 value = 'complex(0,1)*QLuRod2x2',
                 order = {'QCD':1})

GC_95 = Coupling(name = 'GC_95',
                 value = 'complex(0,1)*QLuRod3x3',
                 order = {'QCD':1})

GC_96 = Coupling(name = 'GC_96',
                 value = '(-2*ee**2*complex(0,1))/(3.*cw) - (cw*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_97 = Coupling(name = 'GC_97',
                 value = '(2*ee**2*complex(0,1))/(3.*cw) - (cw*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_98 = Coupling(name = 'GC_98',
                 value = '(ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_99 = Coupling(name = 'GC_99',
                 value = '-((ee**2*complex(0,1))/sw**2)',
                 order = {'QED':2})

GC_100 = Coupling(name = 'GC_100',
                  value = '(ee**2*complex(0,1))/sw**2',
                  order = {'QED':2})

GC_101 = Coupling(name = 'GC_101',
                  value = '(-2*ee**2*complex(0,1))/sw**2',
                  order = {'QED':2})

GC_102 = Coupling(name = 'GC_102',
                  value = '(2*ee**2*complex(0,1))/sw**2',
                  order = {'QED':2})

GC_103 = Coupling(name = 'GC_103',
                  value = '(cw**2*ee**2*complex(0,1))/sw**2',
                  order = {'QED':2})

GC_104 = Coupling(name = 'GC_104',
                  value = '-0.5*ee/sw',
                  order = {'QED':1})

GC_105 = Coupling(name = 'GC_105',
                  value = '-0.5*(ee*complex(0,1))/sw',
                  order = {'QED':1})

GC_106 = Coupling(name = 'GC_106',
                  value = '(ee*complex(0,1))/(2.*sw)',
                  order = {'QED':1})

GC_107 = Coupling(name = 'GC_107',
                  value = '-((ee*complex(0,1))/sw)',
                  order = {'QED':1})

GC_108 = Coupling(name = 'GC_108',
                  value = '(ee*complex(0,1))/sw',
                  order = {'QED':1})

GC_109 = Coupling(name = 'GC_109',
                  value = '-((ee*complex(0,1))/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_110 = Coupling(name = 'GC_110',
                  value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_111 = Coupling(name = 'GC_111',
                  value = '(CKM1x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_112 = Coupling(name = 'GC_112',
                  value = '(CKM1x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_113 = Coupling(name = 'GC_113',
                  value = '(CKM1x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_114 = Coupling(name = 'GC_114',
                  value = '(CKM2x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_115 = Coupling(name = 'GC_115',
                  value = '(CKM2x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_116 = Coupling(name = 'GC_116',
                  value = '(CKM2x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_117 = Coupling(name = 'GC_117',
                  value = '(CKM3x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_118 = Coupling(name = 'GC_118',
                  value = '(CKM3x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_119 = Coupling(name = 'GC_119',
                  value = '(CKM3x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_120 = Coupling(name = 'GC_120',
                  value = '-((cw*ee*complex(0,1))/sw)',
                  order = {'QED':1})

GC_121 = Coupling(name = 'GC_121',
                  value = '(cw*ee*complex(0,1))/sw',
                  order = {'QED':1})

GC_122 = Coupling(name = 'GC_122',
                  value = '-0.5*ee**2/sw',
                  order = {'QED':2})

GC_123 = Coupling(name = 'GC_123',
                  value = '-0.3333333333333333*(ee**2*complex(0,1))/sw',
                  order = {'QED':2})

GC_124 = Coupling(name = 'GC_124',
                  value = '-0.5*(ee**2*complex(0,1))/sw',
                  order = {'QED':2})

GC_125 = Coupling(name = 'GC_125',
                  value = '(-5*ee**2*complex(0,1))/(3.*sw)',
                  order = {'QED':2})

GC_126 = Coupling(name = 'GC_126',
                  value = 'ee**2/(2.*sw)',
                  order = {'QED':2})

GC_127 = Coupling(name = 'GC_127',
                  value = '(ee**2*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_128 = Coupling(name = 'GC_128',
                  value = '(-2*cw*ee**2*complex(0,1))/sw',
                  order = {'QED':2})

GC_129 = Coupling(name = 'GC_129',
                  value = '(-2*ee*complex(0,1)*G)/sw',
                  order = {'QCD':1,'QED':1})

GC_130 = Coupling(name = 'GC_130',
                  value = '(2*ee*complex(0,1)*G)/sw',
                  order = {'QCD':1,'QED':1})

GC_131 = Coupling(name = 'GC_131',
                  value = '-((ee*G*cmath.sqrt(2))/sw)',
                  order = {'QCD':1,'QED':1})

GC_132 = Coupling(name = 'GC_132',
                  value = '(ee*G*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_133 = Coupling(name = 'GC_133',
                  value = '-0.3333333333333333*(ee*complex(0,1)*sw)/cw',
                  order = {'QED':1})

GC_134 = Coupling(name = 'GC_134',
                  value = '(ee*complex(0,1)*sw)/(3.*cw)',
                  order = {'QED':1})

GC_135 = Coupling(name = 'GC_135',
                  value = '(-2*ee*complex(0,1)*sw)/(3.*cw)',
                  order = {'QED':1})

GC_136 = Coupling(name = 'GC_136',
                  value = '(ee*complex(0,1)*sw)/cw',
                  order = {'QED':1})

GC_137 = Coupling(name = 'GC_137',
                  value = '(-2*ee**2*complex(0,1)*sw)/(9.*cw)',
                  order = {'QED':2})

GC_138 = Coupling(name = 'GC_138',
                  value = '(-2*ee*complex(0,1)*G*sw)/(3.*cw)',
                  order = {'QCD':1,'QED':1})

GC_139 = Coupling(name = 'GC_139',
                  value = '(2*ee*complex(0,1)*G*sw)/(3.*cw)',
                  order = {'QCD':1,'QED':1})

GC_140 = Coupling(name = 'GC_140',
                  value = '(2*ee**2*complex(0,1)*sw**2)/(9.*cw**2)',
                  order = {'QED':2})

GC_141 = Coupling(name = 'GC_141',
                  value = '-0.5*(cw*ee)/sw - (ee*sw)/(2.*cw)',
                  order = {'QED':1})

GC_142 = Coupling(name = 'GC_142',
                  value = '-0.5*(cw*ee*complex(0,1))/sw - (ee*complex(0,1)*sw)/(6.*cw)',
                  order = {'QED':1})

GC_143 = Coupling(name = 'GC_143',
                  value = '(cw*ee*complex(0,1))/(2.*sw) - (ee*complex(0,1)*sw)/(6.*cw)',
                  order = {'QED':1})

GC_144 = Coupling(name = 'GC_144',
                  value = '-((cw*ee*complex(0,1))/sw) - (ee*complex(0,1)*sw)/(3.*cw)',
                  order = {'QED':1})

GC_145 = Coupling(name = 'GC_145',
                  value = '(cw*ee*complex(0,1))/sw - (ee*complex(0,1)*sw)/(3.*cw)',
                  order = {'QED':1})

GC_146 = Coupling(name = 'GC_146',
                  value = '-((cw*ee*complex(0,1))/sw) + (ee*complex(0,1)*sw)/(3.*cw)',
                  order = {'QED':1})

GC_147 = Coupling(name = 'GC_147',
                  value = '(cw*ee*complex(0,1))/sw + (ee*complex(0,1)*sw)/(3.*cw)',
                  order = {'QED':1})

GC_148 = Coupling(name = 'GC_148',
                  value = '-0.5*(cw*ee*complex(0,1))/sw + (ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'QED':1})

GC_149 = Coupling(name = 'GC_149',
                  value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'QED':1})

GC_150 = Coupling(name = 'GC_150',
                  value = '(4*cw*ee**2*complex(0,1))/(3.*sw) + (4*ee**2*complex(0,1)*sw)/(9.*cw)',
                  order = {'QED':2})

GC_151 = Coupling(name = 'GC_151',
                  value = '(8*cw*ee**2*complex(0,1))/(3.*sw) - (8*ee**2*complex(0,1)*sw)/(9.*cw)',
                  order = {'QED':2})

GC_152 = Coupling(name = 'GC_152',
                  value = '(cw*ee**2*complex(0,1))/sw - (ee**2*complex(0,1)*sw)/cw',
                  order = {'QED':2})

GC_153 = Coupling(name = 'GC_153',
                  value = '(-2*cw*ee*complex(0,1)*G)/sw - (2*ee*complex(0,1)*G*sw)/(3.*cw)',
                  order = {'QCD':1,'QED':1})

GC_154 = Coupling(name = 'GC_154',
                  value = '(2*cw*ee*complex(0,1)*G)/sw - (2*ee*complex(0,1)*G*sw)/(3.*cw)',
                  order = {'QCD':1,'QED':1})

GC_155 = Coupling(name = 'GC_155',
                  value = '(-2*cw*ee*complex(0,1)*G)/sw + (2*ee*complex(0,1)*G*sw)/(3.*cw)',
                  order = {'QCD':1,'QED':1})

GC_156 = Coupling(name = 'GC_156',
                  value = '(2*cw*ee*complex(0,1)*G)/sw + (2*ee*complex(0,1)*G*sw)/(3.*cw)',
                  order = {'QCD':1,'QED':1})

GC_157 = Coupling(name = 'GC_157',
                  value = '-((cw*ee*G)/sw) + (ee*G*sw)/cw',
                  order = {'QCD':1,'QED':1})

GC_158 = Coupling(name = 'GC_158',
                  value = '(cw*ee*G)/sw + (ee*G*sw)/cw',
                  order = {'QCD':1,'QED':1})

GC_159 = Coupling(name = 'GC_159',
                  value = '(-4*ee**2*complex(0,1))/3. + (2*cw**2*ee**2*complex(0,1))/sw**2 + (2*ee**2*complex(0,1)*sw**2)/(9.*cw**2)',
                  order = {'QED':2})

GC_160 = Coupling(name = 'GC_160',
                  value = '(4*ee**2*complex(0,1))/3. + (2*cw**2*ee**2*complex(0,1))/sw**2 + (2*ee**2*complex(0,1)*sw**2)/(9.*cw**2)',
                  order = {'QED':2})

GC_161 = Coupling(name = 'GC_161',
                  value = '-(ee**2*complex(0,1)) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_162 = Coupling(name = 'GC_162',
                  value = 'ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_163 = Coupling(name = 'GC_163',
                  value = 'complex(0,1)*uRdRss1x1',
                  order = {'QCD':1})

GC_164 = Coupling(name = 'GC_164',
                  value = 'complex(0,1)*uRdRss2x2',
                  order = {'QCD':1})

GC_165 = Coupling(name = 'GC_165',
                  value = 'complex(0,1)*uRdRss3x3',
                  order = {'QCD':1})

GC_166 = Coupling(name = 'GC_166',
                  value = '(complex(0,1)*uRdRts1x1)/cmath.sqrt(2)',
                  order = {'QCD':1})

GC_167 = Coupling(name = 'GC_167',
                  value = '-((complex(0,1)*uRdRts2x2)/cmath.sqrt(2))',
                  order = {'QCD':1})

GC_168 = Coupling(name = 'GC_168',
                  value = '(complex(0,1)*uRdRts3x3)/cmath.sqrt(2)',
                  order = {'QCD':1})

GC_169 = Coupling(name = 'GC_169',
                  value = '2*complex(0,1)*uRuRss1x1',
                  order = {'QCD':1})

GC_170 = Coupling(name = 'GC_170',
                  value = '2*complex(0,1)*uRuRss2x2',
                  order = {'QCD':1})

GC_171 = Coupling(name = 'GC_171',
                  value = '2*complex(0,1)*uRuRss3x3',
                  order = {'QCD':1})

GC_172 = Coupling(name = 'GC_172',
                  value = '(complex(0,1)*uRuRts1x1)/cmath.sqrt(2) + (complex(0,1)*uRuRts2x2)/cmath.sqrt(2)',
                  order = {'QCD':1})

GC_173 = Coupling(name = 'GC_173',
                  value = '-((complex(0,1)*uRuRts2x2)/cmath.sqrt(2)) - (complex(0,1)*uRuRts3x3)/cmath.sqrt(2)',
                  order = {'QCD':1})

GC_174 = Coupling(name = 'GC_174',
                  value = '(complex(0,1)*uRuRts1x1)/cmath.sqrt(2) + (complex(0,1)*uRuRts3x3)/cmath.sqrt(2)',
                  order = {'QCD':1})

GC_175 = Coupling(name = 'GC_175',
                  value = '-0.5*(ee**2*vev)/cw',
                  order = {'QED':1})

GC_176 = Coupling(name = 'GC_176',
                  value = '(ee**2*vev)/(2.*cw)',
                  order = {'QED':1})

GC_177 = Coupling(name = 'GC_177',
                  value = '-2*complex(0,1)*lam*vev',
                  order = {'QED':1})

GC_178 = Coupling(name = 'GC_178',
                  value = '-6*complex(0,1)*lam*vev',
                  order = {'QED':1})

GC_179 = Coupling(name = 'GC_179',
                  value = '-0.25*(ee**2*vev)/sw**2',
                  order = {'QED':1})

GC_180 = Coupling(name = 'GC_180',
                  value = '-0.25*(ee**2*complex(0,1)*vev)/sw**2',
                  order = {'QED':1})

GC_181 = Coupling(name = 'GC_181',
                  value = '(ee**2*complex(0,1)*vev)/(2.*sw**2)',
                  order = {'QED':1})

GC_182 = Coupling(name = 'GC_182',
                  value = '(ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_183 = Coupling(name = 'GC_183',
                  value = '-0.5*(ee**2*vev)/sw',
                  order = {'QED':1})

GC_184 = Coupling(name = 'GC_184',
                  value = '(ee**2*vev)/(2.*sw)',
                  order = {'QED':1})

GC_185 = Coupling(name = 'GC_185',
                  value = '-0.25*(ee**2*vev)/cw - (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_186 = Coupling(name = 'GC_186',
                  value = '(ee**2*vev)/(4.*cw) - (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_187 = Coupling(name = 'GC_187',
                  value = '-0.25*(ee**2*vev)/cw + (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_188 = Coupling(name = 'GC_188',
                  value = '(ee**2*vev)/(4.*cw) + (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_189 = Coupling(name = 'GC_189',
                  value = '-0.5*(ee**2*complex(0,1)*vev) - (cw**2*ee**2*complex(0,1)*vev)/(4.*sw**2) - (ee**2*complex(0,1)*sw**2*vev)/(4.*cw**2)',
                  order = {'QED':1})

GC_190 = Coupling(name = 'GC_190',
                  value = 'ee**2*complex(0,1)*vev + (cw**2*ee**2*complex(0,1)*vev)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*vev)/(2.*cw**2)',
                  order = {'QED':1})

GC_191 = Coupling(name = 'GC_191',
                  value = '-(yb/cmath.sqrt(2))',
                  order = {'QED':1})

GC_192 = Coupling(name = 'GC_192',
                  value = '-((complex(0,1)*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_193 = Coupling(name = 'GC_193',
                  value = '-(CKM1x3*yb)',
                  order = {'QED':1})

GC_194 = Coupling(name = 'GC_194',
                  value = '-(CKM2x3*yb)',
                  order = {'QED':1})

GC_195 = Coupling(name = 'GC_195',
                  value = '-(CKM3x3*yb)',
                  order = {'QED':1})

GC_196 = Coupling(name = 'GC_196',
                  value = '-(yc/cmath.sqrt(2))',
                  order = {'QED':1})

GC_197 = Coupling(name = 'GC_197',
                  value = '-((complex(0,1)*yc)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_198 = Coupling(name = 'GC_198',
                  value = 'yc/cmath.sqrt(2)',
                  order = {'QED':1})

GC_199 = Coupling(name = 'GC_199',
                  value = 'CKM2x1*yc',
                  order = {'QED':1})

GC_200 = Coupling(name = 'GC_200',
                  value = 'CKM2x2*yc',
                  order = {'QED':1})

GC_201 = Coupling(name = 'GC_201',
                  value = 'CKM2x3*yc',
                  order = {'QED':1})

GC_202 = Coupling(name = 'GC_202',
                  value = '-(ydo/cmath.sqrt(2))',
                  order = {'QED':1})

GC_203 = Coupling(name = 'GC_203',
                  value = '-((complex(0,1)*ydo)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_204 = Coupling(name = 'GC_204',
                  value = '-(CKM1x1*ydo)',
                  order = {'QED':1})

GC_205 = Coupling(name = 'GC_205',
                  value = '-(CKM2x1*ydo)',
                  order = {'QED':1})

GC_206 = Coupling(name = 'GC_206',
                  value = '-(CKM3x1*ydo)',
                  order = {'QED':1})

GC_207 = Coupling(name = 'GC_207',
                  value = '-ye',
                  order = {'QED':1})

GC_208 = Coupling(name = 'GC_208',
                  value = 'ye',
                  order = {'QED':1})

GC_209 = Coupling(name = 'GC_209',
                  value = '-(ye/cmath.sqrt(2))',
                  order = {'QED':1})

GC_210 = Coupling(name = 'GC_210',
                  value = '-((complex(0,1)*ye)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_211 = Coupling(name = 'GC_211',
                  value = '-ym',
                  order = {'QED':1})

GC_212 = Coupling(name = 'GC_212',
                  value = 'ym',
                  order = {'QED':1})

GC_213 = Coupling(name = 'GC_213',
                  value = '-(ym/cmath.sqrt(2))',
                  order = {'QED':1})

GC_214 = Coupling(name = 'GC_214',
                  value = '-((complex(0,1)*ym)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_215 = Coupling(name = 'GC_215',
                  value = '-(ys/cmath.sqrt(2))',
                  order = {'QED':1})

GC_216 = Coupling(name = 'GC_216',
                  value = '-((complex(0,1)*ys)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_217 = Coupling(name = 'GC_217',
                  value = '-(CKM1x2*ys)',
                  order = {'QED':1})

GC_218 = Coupling(name = 'GC_218',
                  value = '-(CKM2x2*ys)',
                  order = {'QED':1})

GC_219 = Coupling(name = 'GC_219',
                  value = '-(CKM3x2*ys)',
                  order = {'QED':1})

GC_220 = Coupling(name = 'GC_220',
                  value = '-(yt/cmath.sqrt(2))',
                  order = {'QED':1})

GC_221 = Coupling(name = 'GC_221',
                  value = '-((complex(0,1)*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_222 = Coupling(name = 'GC_222',
                  value = 'yt/cmath.sqrt(2)',
                  order = {'QED':1})

GC_223 = Coupling(name = 'GC_223',
                  value = 'CKM3x1*yt',
                  order = {'QED':1})

GC_224 = Coupling(name = 'GC_224',
                  value = 'CKM3x2*yt',
                  order = {'QED':1})

GC_225 = Coupling(name = 'GC_225',
                  value = 'CKM3x3*yt',
                  order = {'QED':1})

GC_226 = Coupling(name = 'GC_226',
                  value = '-ytau',
                  order = {'QED':1})

GC_227 = Coupling(name = 'GC_227',
                  value = 'ytau',
                  order = {'QED':1})

GC_228 = Coupling(name = 'GC_228',
                  value = '-(ytau/cmath.sqrt(2))',
                  order = {'QED':1})

GC_229 = Coupling(name = 'GC_229',
                  value = '-((complex(0,1)*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_230 = Coupling(name = 'GC_230',
                  value = '-(yup/cmath.sqrt(2))',
                  order = {'QED':1})

GC_231 = Coupling(name = 'GC_231',
                  value = '-((complex(0,1)*yup)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_232 = Coupling(name = 'GC_232',
                  value = 'yup/cmath.sqrt(2)',
                  order = {'QED':1})

GC_233 = Coupling(name = 'GC_233',
                  value = 'CKM1x1*yup',
                  order = {'QED':1})

GC_234 = Coupling(name = 'GC_234',
                  value = 'CKM1x2*yup',
                  order = {'QED':1})

GC_235 = Coupling(name = 'GC_235',
                  value = 'CKM1x3*yup',
                  order = {'QED':1})

GC_236 = Coupling(name = 'GC_236',
                  value = 'complex(0,1)*QLdRod1x1*complexconjugate(CKM1x1)',
                  order = {'QCD':1})

GC_237 = Coupling(name = 'GC_237',
                  value = '-(complex(0,1)*QLuRod1x1*complexconjugate(CKM1x1))',
                  order = {'QCD':1})

GC_238 = Coupling(name = 'GC_238',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_239 = Coupling(name = 'GC_239',
                  value = 'ydo*complexconjugate(CKM1x1)',
                  order = {'QED':1})

GC_240 = Coupling(name = 'GC_240',
                  value = '-(yup*complexconjugate(CKM1x1))',
                  order = {'QED':1})

GC_241 = Coupling(name = 'GC_241',
                  value = 'complex(0,1)*QLdRod1x1*complexconjugate(CKM1x2)',
                  order = {'QCD':1})

GC_242 = Coupling(name = 'GC_242',
                  value = '-(complex(0,1)*QLuRod1x1*complexconjugate(CKM1x2))',
                  order = {'QCD':1})

GC_243 = Coupling(name = 'GC_243',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_244 = Coupling(name = 'GC_244',
                  value = 'ys*complexconjugate(CKM1x2)',
                  order = {'QED':1})

GC_245 = Coupling(name = 'GC_245',
                  value = '-(yup*complexconjugate(CKM1x2))',
                  order = {'QED':1})

GC_246 = Coupling(name = 'GC_246',
                  value = 'complex(0,1)*QLdRod1x1*complexconjugate(CKM1x3)',
                  order = {'QCD':1})

GC_247 = Coupling(name = 'GC_247',
                  value = '-(complex(0,1)*QLuRod1x1*complexconjugate(CKM1x3))',
                  order = {'QCD':1})

GC_248 = Coupling(name = 'GC_248',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x3))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_249 = Coupling(name = 'GC_249',
                  value = 'yb*complexconjugate(CKM1x3)',
                  order = {'QED':1})

GC_250 = Coupling(name = 'GC_250',
                  value = '-(yup*complexconjugate(CKM1x3))',
                  order = {'QED':1})

GC_251 = Coupling(name = 'GC_251',
                  value = 'complex(0,1)*QLdRod2x2*complexconjugate(CKM2x1)',
                  order = {'QCD':1})

GC_252 = Coupling(name = 'GC_252',
                  value = '-(complex(0,1)*QLuRod2x2*complexconjugate(CKM2x1))',
                  order = {'QCD':1})

GC_253 = Coupling(name = 'GC_253',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_254 = Coupling(name = 'GC_254',
                  value = '-(yc*complexconjugate(CKM2x1))',
                  order = {'QED':1})

GC_255 = Coupling(name = 'GC_255',
                  value = 'ydo*complexconjugate(CKM2x1)',
                  order = {'QED':1})

GC_256 = Coupling(name = 'GC_256',
                  value = 'complex(0,1)*QLdRod2x2*complexconjugate(CKM2x2)',
                  order = {'QCD':1})

GC_257 = Coupling(name = 'GC_257',
                  value = '-(complex(0,1)*QLuRod2x2*complexconjugate(CKM2x2))',
                  order = {'QCD':1})

GC_258 = Coupling(name = 'GC_258',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_259 = Coupling(name = 'GC_259',
                  value = '-(yc*complexconjugate(CKM2x2))',
                  order = {'QED':1})

GC_260 = Coupling(name = 'GC_260',
                  value = 'ys*complexconjugate(CKM2x2)',
                  order = {'QED':1})

GC_261 = Coupling(name = 'GC_261',
                  value = 'complex(0,1)*QLdRod2x2*complexconjugate(CKM2x3)',
                  order = {'QCD':1})

GC_262 = Coupling(name = 'GC_262',
                  value = '-(complex(0,1)*QLuRod2x2*complexconjugate(CKM2x3))',
                  order = {'QCD':1})

GC_263 = Coupling(name = 'GC_263',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x3))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_264 = Coupling(name = 'GC_264',
                  value = 'yb*complexconjugate(CKM2x3)',
                  order = {'QED':1})

GC_265 = Coupling(name = 'GC_265',
                  value = '-(yc*complexconjugate(CKM2x3))',
                  order = {'QED':1})

GC_266 = Coupling(name = 'GC_266',
                  value = 'complex(0,1)*QLdRod3x3*complexconjugate(CKM3x1)',
                  order = {'QCD':1})

GC_267 = Coupling(name = 'GC_267',
                  value = '-(complex(0,1)*QLuRod3x3*complexconjugate(CKM3x1))',
                  order = {'QCD':1})

GC_268 = Coupling(name = 'GC_268',
                  value = '(ee*complex(0,1)*complexconjugate(CKM3x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_269 = Coupling(name = 'GC_269',
                  value = 'ydo*complexconjugate(CKM3x1)',
                  order = {'QED':1})

GC_270 = Coupling(name = 'GC_270',
                  value = '-(yt*complexconjugate(CKM3x1))',
                  order = {'QED':1})

GC_271 = Coupling(name = 'GC_271',
                  value = 'complex(0,1)*QLdRod3x3*complexconjugate(CKM3x2)',
                  order = {'QCD':1})

GC_272 = Coupling(name = 'GC_272',
                  value = '-(complex(0,1)*QLuRod3x3*complexconjugate(CKM3x2))',
                  order = {'QCD':1})

GC_273 = Coupling(name = 'GC_273',
                  value = '(ee*complex(0,1)*complexconjugate(CKM3x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_274 = Coupling(name = 'GC_274',
                  value = 'ys*complexconjugate(CKM3x2)',
                  order = {'QED':1})

GC_275 = Coupling(name = 'GC_275',
                  value = '-(yt*complexconjugate(CKM3x2))',
                  order = {'QED':1})

GC_276 = Coupling(name = 'GC_276',
                  value = 'complex(0,1)*QLdRod3x3*complexconjugate(CKM3x3)',
                  order = {'QCD':1})

GC_277 = Coupling(name = 'GC_277',
                  value = '-(complex(0,1)*QLuRod3x3*complexconjugate(CKM3x3))',
                  order = {'QCD':1})

GC_278 = Coupling(name = 'GC_278',
                  value = '(ee*complex(0,1)*complexconjugate(CKM3x3))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_279 = Coupling(name = 'GC_279',
                  value = 'yb*complexconjugate(CKM3x3)',
                  order = {'QED':1})

GC_280 = Coupling(name = 'GC_280',
                  value = '-(yt*complexconjugate(CKM3x3))',
                  order = {'QED':1})

GC_281 = Coupling(name = 'GC_281',
                  value = '2*complex(0,1)*complexconjugate(dRdRss1x1)',
                  order = {'QCD':1})

GC_282 = Coupling(name = 'GC_282',
                  value = '2*complex(0,1)*complexconjugate(dRdRss2x2)',
                  order = {'QCD':1})

GC_283 = Coupling(name = 'GC_283',
                  value = '2*complex(0,1)*complexconjugate(dRdRss3x3)',
                  order = {'QCD':1})

GC_284 = Coupling(name = 'GC_284',
                  value = '(complex(0,1)*complexconjugate(dRdRts1x1))/cmath.sqrt(2) + (complex(0,1)*complexconjugate(dRdRts2x2))/cmath.sqrt(2)',
                  order = {'QCD':1})

GC_285 = Coupling(name = 'GC_285',
                  value = '-((complex(0,1)*complexconjugate(dRdRts1x1))/cmath.sqrt(2)) - (complex(0,1)*complexconjugate(dRdRts3x3))/cmath.sqrt(2)',
                  order = {'QCD':1})

GC_286 = Coupling(name = 'GC_286',
                  value = '-((complex(0,1)*complexconjugate(dRdRts2x2))/cmath.sqrt(2)) - (complex(0,1)*complexconjugate(dRdRts3x3))/cmath.sqrt(2)',
                  order = {'QCD':1})

GC_287 = Coupling(name = 'GC_287',
                  value = 'complex(0,1)*complexconjugate(QLdRod1x1)',
                  order = {'QCD':1})

GC_288 = Coupling(name = 'GC_288',
                  value = 'CKM1x1*complex(0,1)*complexconjugate(QLdRod1x1)',
                  order = {'QCD':1})

GC_289 = Coupling(name = 'GC_289',
                  value = 'CKM1x2*complex(0,1)*complexconjugate(QLdRod1x1)',
                  order = {'QCD':1})

GC_290 = Coupling(name = 'GC_290',
                  value = 'CKM1x3*complex(0,1)*complexconjugate(QLdRod1x1)',
                  order = {'QCD':1})

GC_291 = Coupling(name = 'GC_291',
                  value = 'complex(0,1)*complexconjugate(QLdRod2x2)',
                  order = {'QCD':1})

GC_292 = Coupling(name = 'GC_292',
                  value = 'CKM2x1*complex(0,1)*complexconjugate(QLdRod2x2)',
                  order = {'QCD':1})

GC_293 = Coupling(name = 'GC_293',
                  value = 'CKM2x2*complex(0,1)*complexconjugate(QLdRod2x2)',
                  order = {'QCD':1})

GC_294 = Coupling(name = 'GC_294',
                  value = 'CKM2x3*complex(0,1)*complexconjugate(QLdRod2x2)',
                  order = {'QCD':1})

GC_295 = Coupling(name = 'GC_295',
                  value = 'complex(0,1)*complexconjugate(QLdRod3x3)',
                  order = {'QCD':1})

GC_296 = Coupling(name = 'GC_296',
                  value = 'CKM3x1*complex(0,1)*complexconjugate(QLdRod3x3)',
                  order = {'QCD':1})

GC_297 = Coupling(name = 'GC_297',
                  value = 'CKM3x2*complex(0,1)*complexconjugate(QLdRod3x3)',
                  order = {'QCD':1})

GC_298 = Coupling(name = 'GC_298',
                  value = 'CKM3x3*complex(0,1)*complexconjugate(QLdRod3x3)',
                  order = {'QCD':1})

GC_299 = Coupling(name = 'GC_299',
                  value = '-(complex(0,1)*complexconjugate(CKM1x1)*complexconjugate(QLQLss1x1)) - complex(0,1)*complexconjugate(CKM2x1)*complexconjugate(QLQLss2x2) - complex(0,1)*complexconjugate(CKM1x1)*complexconjugate(QLQLss3x3) - complex(0,1)*complexconjugate(CKM2x1)*complexconjugate(QLQLss3x3)',
                  order = {'QCD':1})

GC_300 = Coupling(name = 'GC_300',
                  value = '-(complex(0,1)*complexconjugate(CKM1x2)*complexconjugate(QLQLss1x1)) - complex(0,1)*complexconjugate(CKM2x2)*complexconjugate(QLQLss2x2) - complex(0,1)*complexconjugate(CKM1x2)*complexconjugate(QLQLss3x3) - complex(0,1)*complexconjugate(CKM2x2)*complexconjugate(QLQLss3x3)',
                  order = {'QCD':1})

GC_301 = Coupling(name = 'GC_301',
                  value = '-(complex(0,1)*complexconjugate(CKM1x3)*complexconjugate(QLQLss1x1)) - complex(0,1)*complexconjugate(CKM2x3)*complexconjugate(QLQLss2x2) - complex(0,1)*complexconjugate(CKM1x3)*complexconjugate(QLQLss3x3) - complex(0,1)*complexconjugate(CKM2x3)*complexconjugate(QLQLss3x3)',
                  order = {'QCD':1})

GC_302 = Coupling(name = 'GC_302',
                  value = 'complex(0,1)*complexconjugate(CKM2x1)*complexconjugate(QLQLss1x1) + complex(0,1)*complexconjugate(CKM3x1)*complexconjugate(QLQLss1x1) + complex(0,1)*complexconjugate(CKM2x1)*complexconjugate(QLQLss2x2) + complex(0,1)*complexconjugate(CKM3x1)*complexconjugate(QLQLss3x3)',
                  order = {'QCD':1})

GC_303 = Coupling(name = 'GC_303',
                  value = '-(complex(0,1)*complexconjugate(CKM1x1)*complexconjugate(QLQLss1x1)) - complex(0,1)*complexconjugate(CKM1x1)*complexconjugate(QLQLss2x2) + complex(0,1)*complexconjugate(CKM3x1)*complexconjugate(QLQLss2x2) + complex(0,1)*complexconjugate(CKM3x1)*complexconjugate(QLQLss3x3)',
                  order = {'QCD':1})

GC_304 = Coupling(name = 'GC_304',
                  value = 'complex(0,1)*complexconjugate(CKM2x2)*complexconjugate(QLQLss1x1) + complex(0,1)*complexconjugate(CKM3x2)*complexconjugate(QLQLss1x1) + complex(0,1)*complexconjugate(CKM2x2)*complexconjugate(QLQLss2x2) + complex(0,1)*complexconjugate(CKM3x2)*complexconjugate(QLQLss3x3)',
                  order = {'QCD':1})

GC_305 = Coupling(name = 'GC_305',
                  value = '-(complex(0,1)*complexconjugate(CKM1x2)*complexconjugate(QLQLss1x1)) - complex(0,1)*complexconjugate(CKM1x2)*complexconjugate(QLQLss2x2) + complex(0,1)*complexconjugate(CKM3x2)*complexconjugate(QLQLss2x2) + complex(0,1)*complexconjugate(CKM3x2)*complexconjugate(QLQLss3x3)',
                  order = {'QCD':1})

GC_306 = Coupling(name = 'GC_306',
                  value = 'complex(0,1)*complexconjugate(CKM2x3)*complexconjugate(QLQLss1x1) + complex(0,1)*complexconjugate(CKM3x3)*complexconjugate(QLQLss1x1) + complex(0,1)*complexconjugate(CKM2x3)*complexconjugate(QLQLss2x2) + complex(0,1)*complexconjugate(CKM3x3)*complexconjugate(QLQLss3x3)',
                  order = {'QCD':1})

GC_307 = Coupling(name = 'GC_307',
                  value = '-(complex(0,1)*complexconjugate(CKM1x3)*complexconjugate(QLQLss1x1)) - complex(0,1)*complexconjugate(CKM1x3)*complexconjugate(QLQLss2x2) + complex(0,1)*complexconjugate(CKM3x3)*complexconjugate(QLQLss2x2) + complex(0,1)*complexconjugate(CKM3x3)*complexconjugate(QLQLss3x3)',
                  order = {'QCD':1})

GC_308 = Coupling(name = 'GC_308',
                  value = 'complex(0,1)*complexconjugate(QLQLst1x1)*cmath.sqrt(2)',
                  order = {'QCD':1})

GC_309 = Coupling(name = 'GC_309',
                  value = '-(complex(0,1)*complexconjugate(CKM1x1)*complexconjugate(QLQLst1x1))',
                  order = {'QCD':1})

GC_310 = Coupling(name = 'GC_310',
                  value = '-(complex(0,1)*complexconjugate(CKM1x2)*complexconjugate(QLQLst1x1))',
                  order = {'QCD':1})

GC_311 = Coupling(name = 'GC_311',
                  value = '-(complex(0,1)*complexconjugate(CKM1x3)*complexconjugate(QLQLst1x1))',
                  order = {'QCD':1})

GC_312 = Coupling(name = 'GC_312',
                  value = 'complex(0,1)*complexconjugate(QLQLst2x2)*cmath.sqrt(2)',
                  order = {'QCD':1})

GC_313 = Coupling(name = 'GC_313',
                  value = '-(complex(0,1)*complexconjugate(CKM2x1)*complexconjugate(QLQLst2x2))',
                  order = {'QCD':1})

GC_314 = Coupling(name = 'GC_314',
                  value = '-(complex(0,1)*complexconjugate(CKM2x2)*complexconjugate(QLQLst2x2))',
                  order = {'QCD':1})

GC_315 = Coupling(name = 'GC_315',
                  value = '-(complex(0,1)*complexconjugate(CKM2x3)*complexconjugate(QLQLst2x2))',
                  order = {'QCD':1})

GC_316 = Coupling(name = 'GC_316',
                  value = 'complex(0,1)*complexconjugate(QLQLst3x3)*cmath.sqrt(2)',
                  order = {'QCD':1})

GC_317 = Coupling(name = 'GC_317',
                  value = '-(complex(0,1)*complexconjugate(CKM3x1)*complexconjugate(QLQLst3x3))',
                  order = {'QCD':1})

GC_318 = Coupling(name = 'GC_318',
                  value = '-(complex(0,1)*complexconjugate(CKM3x2)*complexconjugate(QLQLst3x3))',
                  order = {'QCD':1})

GC_319 = Coupling(name = 'GC_319',
                  value = '-(complex(0,1)*complexconjugate(CKM3x3)*complexconjugate(QLQLst3x3))',
                  order = {'QCD':1})

GC_320 = Coupling(name = 'GC_320',
                  value = '-(complex(0,1)*complexconjugate(CKM1x1)**2*complexconjugate(QLQLst1x1)*cmath.sqrt(2)) - complex(0,1)*complexconjugate(CKM2x1)**2*complexconjugate(QLQLst2x2)*cmath.sqrt(2) - complex(0,1)*complexconjugate(CKM3x1)**2*complexconjugate(QLQLst3x3)*cmath.sqrt(2)',
                  order = {'QCD':1})

GC_321 = Coupling(name = 'GC_321',
                  value = '-(complex(0,1)*complexconjugate(CKM1x1)*complexconjugate(CKM1x2)*complexconjugate(QLQLst1x1)*cmath.sqrt(2)) - complex(0,1)*complexconjugate(CKM2x1)*complexconjugate(CKM2x2)*complexconjugate(QLQLst2x2)*cmath.sqrt(2) - complex(0,1)*complexconjugate(CKM3x1)*complexconjugate(CKM3x2)*complexconjugate(QLQLst3x3)*cmath.sqrt(2)',
                  order = {'QCD':1})

GC_322 = Coupling(name = 'GC_322',
                  value = '-(complex(0,1)*complexconjugate(CKM1x2)**2*complexconjugate(QLQLst1x1)*cmath.sqrt(2)) - complex(0,1)*complexconjugate(CKM2x2)**2*complexconjugate(QLQLst2x2)*cmath.sqrt(2) - complex(0,1)*complexconjugate(CKM3x2)**2*complexconjugate(QLQLst3x3)*cmath.sqrt(2)',
                  order = {'QCD':1})

GC_323 = Coupling(name = 'GC_323',
                  value = '-(complex(0,1)*complexconjugate(CKM1x1)*complexconjugate(CKM1x3)*complexconjugate(QLQLst1x1)*cmath.sqrt(2)) - complex(0,1)*complexconjugate(CKM2x1)*complexconjugate(CKM2x3)*complexconjugate(QLQLst2x2)*cmath.sqrt(2) - complex(0,1)*complexconjugate(CKM3x1)*complexconjugate(CKM3x3)*complexconjugate(QLQLst3x3)*cmath.sqrt(2)',
                  order = {'QCD':1})

GC_324 = Coupling(name = 'GC_324',
                  value = '-(complex(0,1)*complexconjugate(CKM1x2)*complexconjugate(CKM1x3)*complexconjugate(QLQLst1x1)*cmath.sqrt(2)) - complex(0,1)*complexconjugate(CKM2x2)*complexconjugate(CKM2x3)*complexconjugate(QLQLst2x2)*cmath.sqrt(2) - complex(0,1)*complexconjugate(CKM3x2)*complexconjugate(CKM3x3)*complexconjugate(QLQLst3x3)*cmath.sqrt(2)',
                  order = {'QCD':1})

GC_325 = Coupling(name = 'GC_325',
                  value = '-(complex(0,1)*complexconjugate(CKM1x3)**2*complexconjugate(QLQLst1x1)*cmath.sqrt(2)) - complex(0,1)*complexconjugate(CKM2x3)**2*complexconjugate(QLQLst2x2)*cmath.sqrt(2) - complex(0,1)*complexconjugate(CKM3x3)**2*complexconjugate(QLQLst3x3)*cmath.sqrt(2)',
                  order = {'QCD':1})

GC_326 = Coupling(name = 'GC_326',
                  value = '-(complex(0,1)*complexconjugate(CKM1x1)*complexconjugate(QLQLts1x1)*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_327 = Coupling(name = 'GC_327',
                  value = '-(complex(0,1)*complexconjugate(CKM1x2)*complexconjugate(QLQLts1x1)*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_328 = Coupling(name = 'GC_328',
                  value = '-(complex(0,1)*complexconjugate(CKM1x3)*complexconjugate(QLQLts1x1)*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_329 = Coupling(name = 'GC_329',
                  value = 'complex(0,1)*complexconjugate(CKM2x1)*complexconjugate(QLQLts2x2)*cmath.sqrt(2)',
                  order = {'QCD':1})

GC_330 = Coupling(name = 'GC_330',
                  value = 'complex(0,1)*complexconjugate(CKM2x2)*complexconjugate(QLQLts2x2)*cmath.sqrt(2)',
                  order = {'QCD':1})

GC_331 = Coupling(name = 'GC_331',
                  value = '-(complex(0,1)*complexconjugate(CKM2x3)*complexconjugate(QLQLts2x2)*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_332 = Coupling(name = 'GC_332',
                  value = '-(complex(0,1)*complexconjugate(CKM3x1)*complexconjugate(QLQLts3x3)*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_333 = Coupling(name = 'GC_333',
                  value = '-(complex(0,1)*complexconjugate(CKM3x2)*complexconjugate(QLQLts3x3)*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_334 = Coupling(name = 'GC_334',
                  value = '-(complex(0,1)*complexconjugate(CKM3x3)*complexconjugate(QLQLts3x3)*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_335 = Coupling(name = 'GC_335',
                  value = '-0.5*(complex(0,1)*complexconjugate(QLQLtt1x1)) - (complex(0,1)*complexconjugate(QLQLtt2x2))/2.',
                  order = {'QCD':1})

GC_336 = Coupling(name = 'GC_336',
                  value = '-0.5*(complex(0,1)*complexconjugate(QLQLtt1x1)) - (complex(0,1)*complexconjugate(QLQLtt3x3))/2.',
                  order = {'QCD':1})

GC_337 = Coupling(name = 'GC_337',
                  value = '(complex(0,1)*complexconjugate(QLQLtt2x2))/2. + (complex(0,1)*complexconjugate(QLQLtt3x3))/2.',
                  order = {'QCD':1})

GC_338 = Coupling(name = 'GC_338',
                  value = '-0.5*(complex(0,1)*complexconjugate(CKM1x1)*complexconjugate(QLQLtt1x1))/cmath.sqrt(2) - (complex(0,1)*complexconjugate(CKM2x1)*complexconjugate(QLQLtt2x2))/(2.*cmath.sqrt(2)) - (complex(0,1)*complexconjugate(CKM1x1)*complexconjugate(QLQLtt3x3))/(2.*cmath.sqrt(2)) - (complex(0,1)*complexconjugate(CKM2x1)*complexconjugate(QLQLtt3x3))/(2.*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_339 = Coupling(name = 'GC_339',
                  value = '-0.5*(complex(0,1)*complexconjugate(CKM1x2)*complexconjugate(QLQLtt1x1))/cmath.sqrt(2) - (complex(0,1)*complexconjugate(CKM2x2)*complexconjugate(QLQLtt2x2))/(2.*cmath.sqrt(2)) - (complex(0,1)*complexconjugate(CKM1x2)*complexconjugate(QLQLtt3x3))/(2.*cmath.sqrt(2)) - (complex(0,1)*complexconjugate(CKM2x2)*complexconjugate(QLQLtt3x3))/(2.*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_340 = Coupling(name = 'GC_340',
                  value = '-0.5*(complex(0,1)*complexconjugate(CKM1x3)*complexconjugate(QLQLtt1x1))/cmath.sqrt(2) - (complex(0,1)*complexconjugate(CKM2x3)*complexconjugate(QLQLtt2x2))/(2.*cmath.sqrt(2)) - (complex(0,1)*complexconjugate(CKM1x3)*complexconjugate(QLQLtt3x3))/(2.*cmath.sqrt(2)) - (complex(0,1)*complexconjugate(CKM2x3)*complexconjugate(QLQLtt3x3))/(2.*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_341 = Coupling(name = 'GC_341',
                  value = '(complex(0,1)*complexconjugate(CKM1x1)*complexconjugate(QLQLtt1x1))/(2.*cmath.sqrt(2)) + (complex(0,1)*complexconjugate(CKM1x1)*complexconjugate(QLQLtt2x2))/(2.*cmath.sqrt(2)) - (complex(0,1)*complexconjugate(CKM3x1)*complexconjugate(QLQLtt2x2))/(2.*cmath.sqrt(2)) - (complex(0,1)*complexconjugate(CKM3x1)*complexconjugate(QLQLtt3x3))/(2.*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_342 = Coupling(name = 'GC_342',
                  value = '(complex(0,1)*complexconjugate(CKM2x1)*complexconjugate(QLQLtt1x1))/(2.*cmath.sqrt(2)) + (complex(0,1)*complexconjugate(CKM3x1)*complexconjugate(QLQLtt1x1))/(2.*cmath.sqrt(2)) + (complex(0,1)*complexconjugate(CKM2x1)*complexconjugate(QLQLtt2x2))/(2.*cmath.sqrt(2)) + (complex(0,1)*complexconjugate(CKM3x1)*complexconjugate(QLQLtt3x3))/(2.*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_343 = Coupling(name = 'GC_343',
                  value = '(complex(0,1)*complexconjugate(CKM1x2)*complexconjugate(QLQLtt1x1))/(2.*cmath.sqrt(2)) + (complex(0,1)*complexconjugate(CKM1x2)*complexconjugate(QLQLtt2x2))/(2.*cmath.sqrt(2)) - (complex(0,1)*complexconjugate(CKM3x2)*complexconjugate(QLQLtt2x2))/(2.*cmath.sqrt(2)) - (complex(0,1)*complexconjugate(CKM3x2)*complexconjugate(QLQLtt3x3))/(2.*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_344 = Coupling(name = 'GC_344',
                  value = '(complex(0,1)*complexconjugate(CKM2x2)*complexconjugate(QLQLtt1x1))/(2.*cmath.sqrt(2)) + (complex(0,1)*complexconjugate(CKM3x2)*complexconjugate(QLQLtt1x1))/(2.*cmath.sqrt(2)) + (complex(0,1)*complexconjugate(CKM2x2)*complexconjugate(QLQLtt2x2))/(2.*cmath.sqrt(2)) + (complex(0,1)*complexconjugate(CKM3x2)*complexconjugate(QLQLtt3x3))/(2.*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_345 = Coupling(name = 'GC_345',
                  value = '(complex(0,1)*complexconjugate(CKM1x2)*complexconjugate(CKM2x1)*complexconjugate(QLQLtt1x1))/2. - (complex(0,1)*complexconjugate(CKM1x1)*complexconjugate(CKM2x2)*complexconjugate(QLQLtt1x1))/2. + (complex(0,1)*complexconjugate(CKM1x2)*complexconjugate(CKM3x1)*complexconjugate(QLQLtt1x1))/2. - (complex(0,1)*complexconjugate(CKM1x1)*complexconjugate(CKM3x2)*complexconjugate(QLQLtt1x1))/2. + (complex(0,1)*complexconjugate(CKM1x2)*complexconjugate(CKM2x1)*complexconjugate(QLQLtt2x2))/2. - (complex(0,1)*complexconjugate(CKM1x1)*complexconjugate(CKM2x2)*complexconjugate(QLQLtt2x2))/2. + (complex(0,1)*complexconjugate(CKM2x2)*complexconjugate(CKM3x1)*complexconjugate(QLQLtt2x2))/2. - (complex(0,1)*complexconjugate(CKM2x1)*complexconjugate(CKM3x2)*complexconjugate(QLQLtt2x2))/2. + (complex(0,1)*complexconjugate(CKM1x2)*complexconjugate(CKM3x1)*complexconjugate(QLQLtt3x3))/2. + (complex(0,1)*complexconjugate(CKM2x2)*complexconjugate(CKM3x1)*complexconjugate(QLQLtt3x3))/2. - (complex(0,1)*complexconjugate(CKM1x1)*complexconjugate(CKM3x2)*complexconjugate(QLQLtt3x3))/2. - (complex(0,1)*complexconjugate(CKM2x1)*complexconjugate(CKM3x2)*complexconjugate(QLQLtt3x3))/2.',
                  order = {'QCD':1})

GC_346 = Coupling(name = 'GC_346',
                  value = '(complex(0,1)*complexconjugate(CKM2x3)*complexconjugate(QLQLtt1x1))/(2.*cmath.sqrt(2)) + (complex(0,1)*complexconjugate(CKM3x3)*complexconjugate(QLQLtt1x1))/(2.*cmath.sqrt(2)) + (complex(0,1)*complexconjugate(CKM2x3)*complexconjugate(QLQLtt2x2))/(2.*cmath.sqrt(2)) + (complex(0,1)*complexconjugate(CKM3x3)*complexconjugate(QLQLtt3x3))/(2.*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_347 = Coupling(name = 'GC_347',
                  value = '-0.5*(complex(0,1)*complexconjugate(CKM1x3)*complexconjugate(QLQLtt1x1))/cmath.sqrt(2) - (complex(0,1)*complexconjugate(CKM1x3)*complexconjugate(QLQLtt2x2))/(2.*cmath.sqrt(2)) + (complex(0,1)*complexconjugate(CKM3x3)*complexconjugate(QLQLtt2x2))/(2.*cmath.sqrt(2)) + (complex(0,1)*complexconjugate(CKM3x3)*complexconjugate(QLQLtt3x3))/(2.*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_348 = Coupling(name = 'GC_348',
                  value = '-0.5*(complex(0,1)*complexconjugate(CKM1x3)*complexconjugate(CKM2x1)*complexconjugate(QLQLtt1x1)) + (complex(0,1)*complexconjugate(CKM1x1)*complexconjugate(CKM2x3)*complexconjugate(QLQLtt1x1))/2. - (complex(0,1)*complexconjugate(CKM1x3)*complexconjugate(CKM3x1)*complexconjugate(QLQLtt1x1))/2. + (complex(0,1)*complexconjugate(CKM1x1)*complexconjugate(CKM3x3)*complexconjugate(QLQLtt1x1))/2. - (complex(0,1)*complexconjugate(CKM1x3)*complexconjugate(CKM2x1)*complexconjugate(QLQLtt2x2))/2. + (complex(0,1)*complexconjugate(CKM1x1)*complexconjugate(CKM2x3)*complexconjugate(QLQLtt2x2))/2. - (complex(0,1)*complexconjugate(CKM2x3)*complexconjugate(CKM3x1)*complexconjugate(QLQLtt2x2))/2. + (complex(0,1)*complexconjugate(CKM2x1)*complexconjugate(CKM3x3)*complexconjugate(QLQLtt2x2))/2. - (complex(0,1)*complexconjugate(CKM1x3)*complexconjugate(CKM3x1)*complexconjugate(QLQLtt3x3))/2. - (complex(0,1)*complexconjugate(CKM2x3)*complexconjugate(CKM3x1)*complexconjugate(QLQLtt3x3))/2. + (complex(0,1)*complexconjugate(CKM1x1)*complexconjugate(CKM3x3)*complexconjugate(QLQLtt3x3))/2. + (complex(0,1)*complexconjugate(CKM2x1)*complexconjugate(CKM3x3)*complexconjugate(QLQLtt3x3))/2.',
                  order = {'QCD':1})

GC_349 = Coupling(name = 'GC_349',
                  value = '-0.5*(complex(0,1)*complexconjugate(CKM1x3)*complexconjugate(CKM2x2)*complexconjugate(QLQLtt1x1)) + (complex(0,1)*complexconjugate(CKM1x2)*complexconjugate(CKM2x3)*complexconjugate(QLQLtt1x1))/2. - (complex(0,1)*complexconjugate(CKM1x3)*complexconjugate(CKM3x2)*complexconjugate(QLQLtt1x1))/2. + (complex(0,1)*complexconjugate(CKM1x2)*complexconjugate(CKM3x3)*complexconjugate(QLQLtt1x1))/2. - (complex(0,1)*complexconjugate(CKM1x3)*complexconjugate(CKM2x2)*complexconjugate(QLQLtt2x2))/2. + (complex(0,1)*complexconjugate(CKM1x2)*complexconjugate(CKM2x3)*complexconjugate(QLQLtt2x2))/2. - (complex(0,1)*complexconjugate(CKM2x3)*complexconjugate(CKM3x2)*complexconjugate(QLQLtt2x2))/2. + (complex(0,1)*complexconjugate(CKM2x2)*complexconjugate(CKM3x3)*complexconjugate(QLQLtt2x2))/2. - (complex(0,1)*complexconjugate(CKM1x3)*complexconjugate(CKM3x2)*complexconjugate(QLQLtt3x3))/2. - (complex(0,1)*complexconjugate(CKM2x3)*complexconjugate(CKM3x2)*complexconjugate(QLQLtt3x3))/2. + (complex(0,1)*complexconjugate(CKM1x2)*complexconjugate(CKM3x3)*complexconjugate(QLQLtt3x3))/2. + (complex(0,1)*complexconjugate(CKM2x2)*complexconjugate(CKM3x3)*complexconjugate(QLQLtt3x3))/2.',
                  order = {'QCD':1})

GC_350 = Coupling(name = 'GC_350',
                  value = 'complex(0,1)*complexconjugate(QLuRod1x1)',
                  order = {'QCD':1})

GC_351 = Coupling(name = 'GC_351',
                  value = '-(CKM1x1*complex(0,1)*complexconjugate(QLuRod1x1))',
                  order = {'QCD':1})

GC_352 = Coupling(name = 'GC_352',
                  value = '-(CKM1x2*complex(0,1)*complexconjugate(QLuRod1x1))',
                  order = {'QCD':1})

GC_353 = Coupling(name = 'GC_353',
                  value = '-(CKM1x3*complex(0,1)*complexconjugate(QLuRod1x1))',
                  order = {'QCD':1})

GC_354 = Coupling(name = 'GC_354',
                  value = 'complex(0,1)*complexconjugate(QLuRod2x2)',
                  order = {'QCD':1})

GC_355 = Coupling(name = 'GC_355',
                  value = '-(CKM2x1*complex(0,1)*complexconjugate(QLuRod2x2))',
                  order = {'QCD':1})

GC_356 = Coupling(name = 'GC_356',
                  value = '-(CKM2x2*complex(0,1)*complexconjugate(QLuRod2x2))',
                  order = {'QCD':1})

GC_357 = Coupling(name = 'GC_357',
                  value = '-(CKM2x3*complex(0,1)*complexconjugate(QLuRod2x2))',
                  order = {'QCD':1})

GC_358 = Coupling(name = 'GC_358',
                  value = 'complex(0,1)*complexconjugate(QLuRod3x3)',
                  order = {'QCD':1})

GC_359 = Coupling(name = 'GC_359',
                  value = '-(CKM3x1*complex(0,1)*complexconjugate(QLuRod3x3))',
                  order = {'QCD':1})

GC_360 = Coupling(name = 'GC_360',
                  value = '-(CKM3x2*complex(0,1)*complexconjugate(QLuRod3x3))',
                  order = {'QCD':1})

GC_361 = Coupling(name = 'GC_361',
                  value = '-(CKM3x3*complex(0,1)*complexconjugate(QLuRod3x3))',
                  order = {'QCD':1})

GC_362 = Coupling(name = 'GC_362',
                  value = 'complex(0,1)*complexconjugate(uRdRss1x1)',
                  order = {'QCD':1})

GC_363 = Coupling(name = 'GC_363',
                  value = 'complex(0,1)*complexconjugate(uRdRss2x2)',
                  order = {'QCD':1})

GC_364 = Coupling(name = 'GC_364',
                  value = 'complex(0,1)*complexconjugate(uRdRss3x3)',
                  order = {'QCD':1})

GC_365 = Coupling(name = 'GC_365',
                  value = '-((complex(0,1)*complexconjugate(uRdRts1x1))/cmath.sqrt(2))',
                  order = {'QCD':1})

GC_366 = Coupling(name = 'GC_366',
                  value = '(complex(0,1)*complexconjugate(uRdRts2x2))/cmath.sqrt(2)',
                  order = {'QCD':1})

GC_367 = Coupling(name = 'GC_367',
                  value = '-((complex(0,1)*complexconjugate(uRdRts3x3))/cmath.sqrt(2))',
                  order = {'QCD':1})

GC_368 = Coupling(name = 'GC_368',
                  value = '2*complex(0,1)*complexconjugate(uRuRss1x1)',
                  order = {'QCD':1})

GC_369 = Coupling(name = 'GC_369',
                  value = '2*complex(0,1)*complexconjugate(uRuRss2x2)',
                  order = {'QCD':1})

GC_370 = Coupling(name = 'GC_370',
                  value = '2*complex(0,1)*complexconjugate(uRuRss3x3)',
                  order = {'QCD':1})

GC_371 = Coupling(name = 'GC_371',
                  value = '-((complex(0,1)*complexconjugate(uRuRts1x1))/cmath.sqrt(2)) - (complex(0,1)*complexconjugate(uRuRts2x2))/cmath.sqrt(2)',
                  order = {'QCD':1})

GC_372 = Coupling(name = 'GC_372',
                  value = '-((complex(0,1)*complexconjugate(uRuRts1x1))/cmath.sqrt(2)) - (complex(0,1)*complexconjugate(uRuRts3x3))/cmath.sqrt(2)',
                  order = {'QCD':1})

GC_373 = Coupling(name = 'GC_373',
                  value = '(complex(0,1)*complexconjugate(uRuRts2x2))/cmath.sqrt(2) + (complex(0,1)*complexconjugate(uRuRts3x3))/cmath.sqrt(2)',
                  order = {'QCD':1})

