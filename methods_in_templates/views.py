from django.shortcuts import render


class DummyObject:
    property = 'foo bar baz'

    def get_property(self):
        print('get_property')
        return self.property

    def get_property_with_transformation(self, transformation):
        print('get_property_with_transformation')
        if transformation == 'uppercase':
            return self.property.upper()
        if transformation == 'lowercase':
            return self.property.lower()
        return self.property


def example(request):
    return render(request, 'methods_in_templates/example.html', {'object': DummyObject()})
