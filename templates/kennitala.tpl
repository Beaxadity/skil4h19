{% extends "base.html" %}

{% block innihald %}
    <h1>Verkefni4 a</h1>
    <ul>
        {% for item in listi %}
            <li>{{ item[0] }}:<a href="/kt/{{item[1]}}"> {{ item[1] }} </a></li>
        {% endfor %}
    </ul>
{% endblock %}