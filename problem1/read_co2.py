from numpy import genfromtxt

def read_co2(file_name = "co2_mm_mlo.txt", verbose=False):
    '''
    # from https://www.esrl.noaa.gov/gmd/ccgg/trends/
    # CO2 expressed as a mole fraction in dry air, micromol/mol, abbreviated as ppm
    #
    #  (-99.99 missing data;  -1 no data for #daily means in month)
    #
    #            decimal       monthly    de-season  #days  st.dev  unc. of
    #             date         average     alized          of days  mon mean
    '''

    data = genfromtxt(file_name, comments='#')

    dates = data[:,2]
    averages = data[:,3]
    uncertainties = data[:,7]
    if verbose:
        print (dates)
        print(averages)
        print(uncertainties)
    return [dates, averages, uncertainties]
