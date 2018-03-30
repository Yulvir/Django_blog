import pygal

from .models import Post


class ChoicesPieChart:

    def __init__(self, **kwargs):
        self.chart = pygal.Pie(**kwargs)
        self.chart.title = 'Amount of Fruits'

    def get_data(self):
        '''
        Query the db for chart data, pack them into a dict and return it.
        '''
        data = {}
        for post in Post.objects.all():
            data[post.user_choice] = post.amt
        return data

    def generate(self):
        # Get chart data
        chart_data = self.get_data()

        # Add data to chart
        for key, value in chart_data.items():
            self.chart.add(key, value)

        # Return the rendered SVG
        return self.chart.render(is_unicode=True)