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

Tcomb = cea_obj.get_Tcomb(Pc=1000,
                          MR=5.0
                          ) #Tcomb = temperatura de combustão
print(f'Tcomb: {Tcomb/1.8:.2f}°C') #.2f sempre vai deixar em duas casas decimais

Densities = cea_obj.get_Densities(Pc=1000,
                                   MR =5.0,
                                   eps=8.0)
print(f'Densities: {Densities}')

ch_molwt_g, ch_gamma = cea_obj.get_Chamber_MolWt_gamma(
            Pc=1000, MR=5.0, eps=8.0
        )
print (f'Massa Molar: {ch_molwt_g:.3f}\n'
       f'Gamma:{ch_gamma:.3f}')

ex_molwt_g, ex_gamma = cea_obj.get_exit_MolWt_gamma(
            Pc=1000, MR=5.0, eps=8.0
        )
print (f'Massa Molar de saída: {ex_molwt_g:.3f}\n'
       f'Gamma de saída:{ex_gamma:.3f}')
                            
