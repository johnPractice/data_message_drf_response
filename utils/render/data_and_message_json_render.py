from rest_framework import renderers


class CustomJSONRenderer(renderers.JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        print("here to check", data)
        message = data.pop("message", "")
        response_data = {
            "data": data.get("results", []) if "results" in data else data,
            "message": message,
        }

        return super().render(response_data, accepted_media_type, renderer_context)
