from django.core.paginator import Paginator


class PreviousNextPaginator(Paginator):
    def get_elided_page_range(self, number=1, *, on_each_side=3, on_ends=2):
        return super().get_elided_page_range(number, on_each_side=1, on_ends=0)
