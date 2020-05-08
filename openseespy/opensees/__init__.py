import sys

# only work for 64 bit system
if sys.maxsize < 2**31:
    raise RuntimeError('64 bit system is required')

# platform dependent
if sys.platform.startswith('linux'):

    try:
        from openseespy.opensees.linux.opensees import *
    except:
        raise RuntimeError('Failed to import openseespy.')

elif sys.platform.startswith('win'):

    # python 3.7 is required
    if sys.version_info[0] == 3 and sys.version_info[1] == 7:

        try:
            from openseespy.opensees.win.opensees import *

        except:

            raise RuntimeError(
                'Failed to import openseespy. Anaconda is recommended https://www.anaconda.com/distribution/')

    else:
        raise RuntimeError(
            'Python version 3.7 is needed for Windows (Anaconda is recommended https://www.anaconda.com/distribution/)')

    # if sys.version_info[1] == 6:

    #    from openseespy.opensees.winpy36.opensees import *

    # elif sys.version_info[1] == 7:

    #    from openseespy.opensees.winpy37.opensees import *

    # elif sys.version_info[1] == 8:

    #    from openseespy.opensees.winpy38.opensees import *

elif sys.platform.startswith('darwin'):

    # from openseespy.opensees.mac.opensees import *
    raise RuntimeError(
        'Please install Mac version from openseespymac package (pip install openseespymac)')


else:

    raise RuntimeError(sys.platform+' is not supported yet')

