#!/usr/bin/env python3
'''Task 3 module'''
from flask import request
from typing import TypeVar

class Auth:
    ''' Authorization '''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        ''' Checks if a path requires authentication '''
        if path is not None and excluded_paths is not None:
            return False
        return True
    
    def authorization_header(self, request=None) -> str:
        '''Gets the authorization header field from the request'''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        ''''Validates user'''
        return None