from rocketcea.cea_obj import CEA_Obj

cea_obj = CEA_Obj(oxName='N2O', fuelName='Ethanol')
full_cea_output = cea_obj.get_full_cea_output(Pc=[1000], # number or list of chamber pressures
                                MR=[6.0],   # number or list of mixture ratios
                                PcOvPe=[100,200],# number or list of Pc/Pexit
                                eps=[40.0,60],   # number or list of supersonic area ratios
                                subar=[3,2],     # number or list of subsonic area ratios
                                short_output=0,  # 0 or 1 to control output length
                                pc_units='psia', # pc_units = 'psia', 'bar', 'atm', 'mmh'
                                output='siunits',# output = 'calories' or 'siunits'
                                fac_CR=None)     # finite area combustor, contraction ratio,)
print(full_cea_output)