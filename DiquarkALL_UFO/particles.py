# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.1.0 for Linux x86 (64-bit) (June 16, 2022)
# Date: Wed 6 Dec 2023 15:45:49


from __future__ import division
from object_library import all_particles, Particle
import parameters as Param

import propagators as Prop

DiqODP = Particle(pdg_code = 9990012,
                  name = 'DiqODP',
                  antiname = 'DiqODP~',
                  spin = 1,
                  color = 8,
                  mass = Param.MdqOD,
                  width = Param.WDiqODP,
                  texname = 'DiqODP',
                  antitexname = 'DiqODP~',
                  charge = 1,
                  GhostNumber = 0,
                  LeptonNumber = 0,
                  Y = 0)

DiqODP__tilde__ = DiqODP.anti()

DiqODN = Particle(pdg_code = 9990013,
                  name = 'DiqODN',
                  antiname = 'DiqODN~',
                  spin = 1,
                  color = 8,
                  mass = Param.MdqOD,
                  width = Param.WDiqODN,
                  texname = 'DiqODN',
                  antitexname = 'DiqODN~',
                  charge = 0,
                  GhostNumber = 0,
                  LeptonNumber = 0,
                  Y = 0)

DiqODN__tilde__ = DiqODN.anti()

DiqSS = Particle(pdg_code = 9990006,
                 name = 'DiqSS',
                 antiname = 'DiqSS~',
                 spin = 1,
                 color = 6,
                 mass = Param.MdqSS,
                 width = Param.WDiqSS,
                 texname = 'DiqSS',
                 antitexname = 'DiqSS~',
                 charge = 1/3,
                 GhostNumber = 0,
                 LeptonNumber = 0,
                 Y = 0)

DiqSS__tilde__ = DiqSS.anti()

DiqSSdR = Particle(pdg_code = 9990010,
                   name = 'DiqSSdR',
                   antiname = 'DiqSSdR~',
                   spin = 1,
                   color = 6,
                   mass = Param.MdqSSdR,
                   width = Param.WDiqSSdR,
                   texname = 'DiqSSdR',
                   antitexname = 'DiqSSdR~',
                   charge = -2/3,
                   GhostNumber = 0,
                   LeptonNumber = 0,
                   Y = 0)

DiqSSdR__tilde__ = DiqSSdR.anti()

DiqSSuR = Particle(pdg_code = 9990008,
                   name = 'DiqSSuR',
                   antiname = 'DiqSSuR~',
                   spin = 1,
                   color = 6,
                   mass = Param.MdqSSuR,
                   width = Param.WDiqSSuR,
                   texname = 'DiqSSuR',
                   antitexname = 'DiqSSuR~',
                   charge = 4/3,
                   GhostNumber = 0,
                   LeptonNumber = 0,
                   Y = 0)

DiqSSuR__tilde__ = DiqSSuR.anti()

DiqSTP = Particle(pdg_code = 9990000,
                  name = 'DiqSTP',
                  antiname = 'DiqSTP~',
                  spin = 1,
                  color = 6,
                  mass = Param.MdqST,
                  width = Param.WDiqSTP,
                  texname = 'DiqSTP',
                  antitexname = 'DiqSTP~',
                  charge = -2/3,
                  GhostNumber = 0,
                  LeptonNumber = 0,
                  Y = 0)

DiqSTP__tilde__ = DiqSTP.anti()

DiqSTN = Particle(pdg_code = 9990001,
                  name = 'DiqSTN',
                  antiname = 'DiqSTN~',
                  spin = 1,
                  color = 6,
                  mass = Param.MdqST,
                  width = Param.WDiqSTN,
                  texname = 'DiqSTN',
                  antitexname = 'DiqSTN~',
                  charge = 1/3,
                  GhostNumber = 0,
                  LeptonNumber = 0,
                  Y = 0)

DiqSTN__tilde__ = DiqSTN.anti()

DiqSTM = Particle(pdg_code = 9990002,
                  name = 'DiqSTM',
                  antiname = 'DiqSTM~',
                  spin = 1,
                  color = 6,
                  mass = Param.MdqST,
                  width = Param.WDiqSTM,
                  texname = 'DiqSTM',
                  antitexname = 'DiqSTM~',
                  charge = 4/3,
                  GhostNumber = 0,
                  LeptonNumber = 0,
                  Y = 0)

DiqSTM__tilde__ = DiqSTM.anti()

DiqTS = Particle(pdg_code = 9990007,
                 name = 'DiqTS',
                 antiname = 'DiqTS~',
                 spin = 1,
                 color = 3,
                 mass = Param.MdqTS,
                 width = Param.WDiqTS,
                 texname = 'DiqTS',
                 antitexname = 'DiqTS~',
                 charge = -1/3,
                 GhostNumber = 0,
                 LeptonNumber = 0,
                 Y = 0)

DiqTS__tilde__ = DiqTS.anti()

DiqTSdR = Particle(pdg_code = 9990011,
                   name = 'DiqTSdR',
                   antiname = 'DiqTSdR~',
                   spin = 1,
                   color = 3,
                   mass = Param.MdqTSdR,
                   width = Param.WDiqTSdR,
                   texname = 'DiqTSdR',
                   antitexname = 'DiqTSdR~',
                   charge = 2/3,
                   GhostNumber = 0,
                   LeptonNumber = 0,
                   Y = 0)

DiqTSdR__tilde__ = DiqTSdR.anti()

DiqTSuR = Particle(pdg_code = 9990009,
                   name = 'DiqTSuR',
                   antiname = 'DiqTSuR~',
                   spin = 1,
                   color = 3,
                   mass = Param.MdqTSuR,
                   width = Param.WDiqTSuR,
                   texname = 'DiqTSuR',
                   antitexname = 'DiqTSuR~',
                   charge = -4/3,
                   GhostNumber = 0,
                   LeptonNumber = 0,
                   Y = 0)

DiqTSuR__tilde__ = DiqTSuR.anti()

DiqTTP = Particle(pdg_code = 9990003,
                  name = 'DiqTTP',
                  antiname = 'DiqTTP~',
                  spin = 1,
                  color = 3,
                  mass = Param.MdqTT,
                  width = Param.WDiqTTP,
                  texname = 'DiqTTP',
                  antitexname = 'DiqTTP~',
                  charge = 2/3,
                  GhostNumber = 0,
                  LeptonNumber = 0,
                  Y = 0)

DiqTTP__tilde__ = DiqTTP.anti()

DiqTTN = Particle(pdg_code = 9990004,
                  name = 'DiqTTN',
                  antiname = 'DiqTTN~',
                  spin = 1,
                  color = 3,
                  mass = Param.MdqTT,
                  width = Param.WDiqTTN,
                  texname = 'DiqTTN',
                  antitexname = 'DiqTTN~',
                  charge = -1/3,
                  GhostNumber = 0,
                  LeptonNumber = 0,
                  Y = 0)

DiqTTN__tilde__ = DiqTTN.anti()

DiqTTM = Particle(pdg_code = 9990005,
                  name = 'DiqTTM',
                  antiname = 'DiqTTM~',
                  spin = 1,
                  color = 3,
                  mass = Param.MdqTT,
                  width = Param.WDiqTTM,
                  texname = 'DiqTTM',
                  antitexname = 'DiqTTM~',
                  charge = -4/3,
                  GhostNumber = 0,
                  LeptonNumber = 0,
                  Y = 0)

DiqTTM__tilde__ = DiqTTM.anti()

a = Particle(pdg_code = 22,
             name = 'a',
             antiname = 'a',
             spin = 3,
             color = 1,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'a',
             antitexname = 'a',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

Z = Particle(pdg_code = 23,
             name = 'Z',
             antiname = 'Z',
             spin = 3,
             color = 1,
             mass = Param.MZ,
             width = Param.WZ,
             texname = 'Z',
             antitexname = 'Z',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

W__plus__ = Particle(pdg_code = 24,
                     name = 'W+',
                     antiname = 'W-',
                     spin = 3,
                     color = 1,
                     mass = Param.MW,
                     width = Param.WW,
                     texname = 'W+',
                     antitexname = 'W-',
                     charge = 1,
                     GhostNumber = 0,
                     LeptonNumber = 0,
                     Y = 0)

W__minus__ = W__plus__.anti()

g = Particle(pdg_code = 21,
             name = 'g',
             antiname = 'g',
             spin = 3,
             color = 8,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'g',
             antitexname = 'g',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

ghA = Particle(pdg_code = 9000001,
               name = 'ghA',
               antiname = 'ghA~',
               spin = -1,
               color = 1,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'ghA',
               antitexname = 'ghA~',
               charge = 0,
               GhostNumber = 1,
               LeptonNumber = 0,
               Y = 0)

ghA__tilde__ = ghA.anti()

ghZ = Particle(pdg_code = 9000002,
               name = 'ghZ',
               antiname = 'ghZ~',
               spin = -1,
               color = 1,
               mass = Param.MZ,
               width = Param.WZ,
               texname = 'ghZ',
               antitexname = 'ghZ~',
               charge = 0,
               GhostNumber = 1,
               LeptonNumber = 0,
               Y = 0)

ghZ__tilde__ = ghZ.anti()

ghWp = Particle(pdg_code = 9000003,
                name = 'ghWp',
                antiname = 'ghWp~',
                spin = -1,
                color = 1,
                mass = Param.MW,
                width = Param.WW,
                texname = 'ghWp',
                antitexname = 'ghWp~',
                charge = 1,
                GhostNumber = 1,
                LeptonNumber = 0,
                Y = 0)

ghWp__tilde__ = ghWp.anti()

ghWm = Particle(pdg_code = 9000004,
                name = 'ghWm',
                antiname = 'ghWm~',
                spin = -1,
                color = 1,
                mass = Param.MW,
                width = Param.WW,
                texname = 'ghWm',
                antitexname = 'ghWm~',
                charge = -1,
                GhostNumber = 1,
                LeptonNumber = 0,
                Y = 0)

ghWm__tilde__ = ghWm.anti()

ghG = Particle(pdg_code = 82,
               name = 'ghG',
               antiname = 'ghG~',
               spin = -1,
               color = 8,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'ghG',
               antitexname = 'ghG~',
               charge = 0,
               GhostNumber = 1,
               LeptonNumber = 0,
               Y = 0)

ghG__tilde__ = ghG.anti()

ve = Particle(pdg_code = 12,
              name = 've',
              antiname = 've~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 've',
              antitexname = 've~',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0)

ve__tilde__ = ve.anti()

vm = Particle(pdg_code = 14,
              name = 'vm',
              antiname = 'vm~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'vm',
              antitexname = 'vm~',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0)

vm__tilde__ = vm.anti()

vt = Particle(pdg_code = 16,
              name = 'vt',
              antiname = 'vt~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'vt',
              antitexname = 'vt~',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0)

vt__tilde__ = vt.anti()

e__minus__ = Particle(pdg_code = 11,
                      name = 'e-',
                      antiname = 'e+',
                      spin = 2,
                      color = 1,
                      mass = Param.Me,
                      width = Param.ZERO,
                      texname = 'e-',
                      antitexname = 'e+',
                      charge = -1,
                      GhostNumber = 0,
                      LeptonNumber = 1,
                      Y = 0)

e__plus__ = e__minus__.anti()

mu__minus__ = Particle(pdg_code = 13,
                       name = 'mu-',
                       antiname = 'mu+',
                       spin = 2,
                       color = 1,
                       mass = Param.MMU,
                       width = Param.ZERO,
                       texname = 'mu-',
                       antitexname = 'mu+',
                       charge = -1,
                       GhostNumber = 0,
                       LeptonNumber = 1,
                       Y = 0)

mu__plus__ = mu__minus__.anti()

ta__minus__ = Particle(pdg_code = 15,
                       name = 'ta-',
                       antiname = 'ta+',
                       spin = 2,
                       color = 1,
                       mass = Param.MTA,
                       width = Param.ZERO,
                       texname = 'ta-',
                       antitexname = 'ta+',
                       charge = -1,
                       GhostNumber = 0,
                       LeptonNumber = 1,
                       Y = 0)

ta__plus__ = ta__minus__.anti()

u = Particle(pdg_code = 2,
             name = 'u',
             antiname = 'u~',
             spin = 2,
             color = 3,
             mass = Param.MU,
             width = Param.ZERO,
             texname = 'u',
             antitexname = 'u~',
             charge = 2/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

u__tilde__ = u.anti()

c = Particle(pdg_code = 4,
             name = 'c',
             antiname = 'c~',
             spin = 2,
             color = 3,
             mass = Param.MC,
             width = Param.ZERO,
             texname = 'c',
             antitexname = 'c~',
             charge = 2/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

c__tilde__ = c.anti()

t = Particle(pdg_code = 6,
             name = 't',
             antiname = 't~',
             spin = 2,
             color = 3,
             mass = Param.MT,
             width = Param.WT,
             texname = 't',
             antitexname = 't~',
             charge = 2/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

t__tilde__ = t.anti()

d = Particle(pdg_code = 1,
             name = 'd',
             antiname = 'd~',
             spin = 2,
             color = 3,
             mass = Param.MD,
             width = Param.ZERO,
             texname = 'd',
             antitexname = 'd~',
             charge = -1/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

d__tilde__ = d.anti()

s = Particle(pdg_code = 3,
             name = 's',
             antiname = 's~',
             spin = 2,
             color = 3,
             mass = Param.MS,
             width = Param.ZERO,
             texname = 's',
             antitexname = 's~',
             charge = -1/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

s__tilde__ = s.anti()

b = Particle(pdg_code = 5,
             name = 'b',
             antiname = 'b~',
             spin = 2,
             color = 3,
             mass = Param.MB,
             width = Param.ZERO,
             texname = 'b',
             antitexname = 'b~',
             charge = -1/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

b__tilde__ = b.anti()

H = Particle(pdg_code = 25,
             name = 'H',
             antiname = 'H',
             spin = 1,
             color = 1,
             mass = Param.MH,
             width = Param.WH,
             texname = 'H',
             antitexname = 'H',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

G0 = Particle(pdg_code = 250,
              name = 'G0',
              antiname = 'G0',
              spin = 1,
              color = 1,
              mass = Param.MZ,
              width = Param.WZ,
              texname = 'G0',
              antitexname = 'G0',
              goldstone = True,
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 0,
              Y = 0)

G__plus__ = Particle(pdg_code = 251,
                     name = 'G+',
                     antiname = 'G-',
                     spin = 1,
                     color = 1,
                     mass = Param.MW,
                     width = Param.WW,
                     texname = 'G+',
                     antitexname = 'G-',
                     goldstone = True,
                     charge = 1,
                     GhostNumber = 0,
                     LeptonNumber = 0,
                     Y = 0)

G__minus__ = G__plus__.anti()

