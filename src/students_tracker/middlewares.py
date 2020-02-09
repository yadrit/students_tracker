import time
from students.models import Logger
from students_tracker import model_choices


class LoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        start_time = time.time()
        response = self.get_response(request)
        diff = time.time() - start_time

        admin_url = '/admin/'
        if request.path.startswith(admin_url):
            Logger.objects.create(
                path=request.path,
                method=model_choices.METHOD_CHOICES_REVERSE[request.method],
                time_delta=diff,
                # user_id=



            )

        # time_delta = models.DecimalField(max_digits=5, decimal_places=3)
        # user_id = models.IntegerField(null=True, blank=True)
        # created = models.DateTimeField(auto_now_add=True)

        # Code to be executed for each request/response after
        # the view is called.

        return response