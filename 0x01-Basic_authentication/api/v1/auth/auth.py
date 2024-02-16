#!/usr/bin/env python3
'''Task 3 module'''
import re
from flask import request
from typing import TypeVar, List


class Auth:
    ''' Authorization '''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        ''' Checks if a path requires authentication '''
        if path is not None or excluded_paths is not None:
            for exclusion_paths in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if exclusion_paths[-1] == '*':
                    pattern = '{}.*'.format(exclusion_paths[0: -1])
                elif exclusion_paths[-1] == '/':
                    pattern = '{}/*'.format(exclusion_paths[0: -1])
                else:
                    pattern = '{}/*'.format(exclusion_paths)
                if re.match(pattern, path):                    
                    return False
        return True

    
    def authorization_header(self, request=None) -> str:
        '''Gets the authorization header field from the request'''
        if request is not None:
            if request.header in request:
                return request.headers.get('Authorization')
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        ''''Validates user'''
        return None