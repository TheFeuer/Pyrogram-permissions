from pyrogram.types import ChatPermissions


def perm(state):
    permissions = ChatPermissions(
        can_send_messages=state,
        can_send_media_messages=state,
        can_send_polls=state,
        can_send_other_messages=state,
        can_add_web_page_previews=state,
        can_change_info=False,
        can_invite_users=False,
        can_pin_messages=False,
    )
    return permissions
