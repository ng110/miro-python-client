from miro.client import MiroApiClient
from miro.utils import get_auth_token_from_env

client = MiroApiClient(base_url='https://api.miro.com',
                       auth_token="")

widgets = client.get_all_widgets_by_board_id('o9J_lESDKFI=')
for widget in widgets:
    try:
        print(widget.obj_id, widget.obj_type, widget.text)
    except:
        print(widget.obj_id, widget.obj_type, widget.start_widget_id, ' > ', widget.end_widget_id)
