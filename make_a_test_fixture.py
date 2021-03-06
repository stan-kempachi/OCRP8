
from pbeurre.models import Food, Category, User
from django.core import serializers

app_list = [
        *Category.objects.all(),
        *User.objects.all(),
        *Food.objects.filter(category=6175)
]

data = serializers.serialize("json", app_list)

f = open('pbeurre/fixtures/test_fixture.json', 'w')
f.write(data)
f.close()
