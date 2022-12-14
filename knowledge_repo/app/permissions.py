from . import roles
from flask_principal import Permission

# Site roles and permissions
admin = Permission(roles.admin)
stats_view = Permission(roles.stats_view)

# Index permissions
index_view = Permission(roles.index_view)

# Tags permissions
tags_view = Permission(roles.tags_view)

# Post permissions
post_comment = Permission(roles.post_comment)
post_edit = Permission(roles.post_edit)
post_view = Permission(roles.post_view)
post_download = Permission(roles.post_download)
