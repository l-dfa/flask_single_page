# :filename: single_page/ajacs/models.py               data source

class Nations(object):
    _nations = {'en': 'England',
                'it': 'Italy',
                'de': 'Germany',
    }
    
    @classmethod
    def get(cls, key=None, default=None):
        '''given nation id returns its name'''
        return cls._nations.get(key, default)
        
    @classmethod
    def keys(cls):
        '''return all nation keys '''
        return cls._nations.keys()

    @classmethod
    def values(cls):
        '''return all nation names '''
        return cls._nations.values()

    @classmethod
    def set(cls, key, val):
        '''set a name
           
           WARN this is valid only in the current session
        '''
        cls._nations[key] = val

class NationData(object):
    _data = { 'en': [100, 200, 300],
              'it': [10, 20, 30],
              'de': [150, 250, 350],
    }
    
    @classmethod
    def get(cls, key=None, default=None):
        '''given nation id returns its data'''
        return cls._data.get(key, default)
