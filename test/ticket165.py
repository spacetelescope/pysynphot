import pysynphot as S


def test_aper():
    olist=['wfc3,uvis1,f218w,aper#0.60', #discovery case
           'wfc3,uvis1,f218w,aper#1.38',
           'wfc3,uvis1,f218w,aper#2.0',
           'wfc3,uvis2,f218w'] #should pass even before code is fixed

    for mode in olist:
        def makebp(mode):
            try:
                bp=S.ObsBandpass(mode)
            except KeyError,e:
                raise AssertionError(e.message)
        yield makebp,mode
        
        
def test_extrap():
    #Make sure we didn't break the extrapolation exception
    try:
        bp=S.ObsBandpass('wfc3,uvis1,f218w,aper#5')
        raise AssertionError('Extrapolation not caught')
    except NotImplementedError:
        pass
