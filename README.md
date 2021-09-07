# restapi
This is a basic(ID-Password-based) user authentication system with the necessary REST APIs needed for the client using Django RESTFramework.
It takes User Register/Login credentials are returns necessary REST APIs and has a basic Profile Form.

Requirements Assumptions:
Takes Registration/Login Credentials with REST APIs 
Generates Tokens
Permissions on UserViewSets

urls:
^admin/
^api/ ^ ^users/$ [name='user-list']
^api/ ^ ^users\.(?P<format>[a-z0-9]+)/?$ [name='user-list']
^api/ ^ ^users/(?P<pk>[^/.]+)/$ [name='user-detail']
^api/ ^ ^users/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='user-detail']
^api/ ^ ^$ [name='api-root']
^api/ ^ ^\.(?P<format>[a-z0-9]+)/?$ [name='api-root']
^api/ ^auth/
^api/ register/ [name='register']
