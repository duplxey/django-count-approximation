from django.db import connections
from django.db.models import QuerySet, Manager


class InfiniteCountQuerySet(QuerySet):
    def count(self):
        return 999_999_999


class ApproximateCountQuerySet(QuerySet):
    def count(self):
        if self.query.where:
            return super(ApproximateCountQuerySet, self).count()

        cursor = connections[self.db].cursor()
        cursor.execute("SELECT reltuples FROM pg_class "
                       "WHERE relname = '%s';" % self.model._meta.db_table)

        return int(cursor.fetchone()[0])


InfiniteCountManager = Manager.from_queryset(InfiniteCountQuerySet)
ApproximateCountManager = Manager.from_queryset(ApproximateCountQuerySet)