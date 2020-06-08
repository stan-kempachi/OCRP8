
from django.core import serializers
from pbeurre.models import Food, Category

# Add all your querysets here. The key for the dictionary can be just a
# unique dummy string (A safe hack after reading django code)
app_list = {}
app_list['category'] = Category.objects.all().get()
app_list['food'] = Food.objects.filter(category='6175').get()

data = serializers.serialize("json", app_list)
f = open('test_fixture.json', 'w')
f.write(data)
f.close()
