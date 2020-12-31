from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

class TestVue(View):
    def get(self, request, *args, **kwargs):
        import random
        import json
        names = (
            "bob",
             "dan",
              "jack",
               "lizzy",
                "susan"
                    )
        items = []
        for i in range(100):
            items.append({
                "name": random.choice(names),
                "age": random.randint(20,80),
                "url": "https://example.com",
            })

        context          = {}
        context["items"] = items

        return render(
              request,
              'vue_test_list.html',
              context
                    )
