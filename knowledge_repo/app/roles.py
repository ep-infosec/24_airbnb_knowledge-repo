from flask_principal import ItemNeed, RoleNeed
from functools import partial

# Need types
GroupNeed = partial(ItemNeed, 'group')

# Site roles
admin = RoleNeed('admin')
stats_view = RoleNeed('stats_view')

# Index roles
index_view = RoleNeed('index_view')

# Tags roles
tags_view = RoleNeed('tags_view')

# Post roles
post_comment = RoleNeed('post_comment')
post_edit = RoleNeed('post_edit')
post_view = RoleNeed('post_view')
post_download = RoleNeed('post_download')
