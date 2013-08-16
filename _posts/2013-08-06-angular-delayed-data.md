---
layout: post
title: "Angular.js and delayed data"
---

Say we've got a web server with some data:

{% highlight ruby %}
items = [
  {:id => 'abc123', :name => 'Alec', :age => 20},
  {:id => 'def456', :name => 'Bob', :age => 40}
]

get '/items' do
  items.to_json
end
{% endhighlight %}

we want to display it on this page:

{% highlight html %}
<!doctype html>
<html>
  <head>
    <script src="/jquery.js"></script>
    <script src="/app.js"></script>
  </head>
  <body>
    <div>
      <table id="items">
        <tr><th>id</th><th>name</th><th>age</th></tr>
      </table>
    </div>
  </body>
</html>
{% endhighlight %}

so we use some jQuery:

{% highlight javascript %}
$(function() {
  $.get('/items', function(items) {
    items = JSON.parse(items);
    for (var i = 0; i < items.length; ++i) {
      var tr = $('<tr>');
      tr.append($('<td>').html(items[i].id));
      tr.append($('<td>').html(items[i].name));
      tr.append($('<td>').html(items[i].age));

      $('#items').append(tr);
    }
  });
});
{% endhighlight %}

Simple enough. But now say we introduce some latency server-side:

{% highlight ruby %}
get '/items' do
  sleep 1 * items.size
  items.to_json
end
{% endhighlight %}

but we can fetch just the ids quickly:

{% highlight ruby %}
get '/item_ids' do
  items.map{|item| item[:id]}.to_json
end
{% endhighlight %}

and then grab each item individually:

{% highlight ruby %}
get '/item/:id' do |id|
  sleep 1
  items.find{|item| item[:id] == id}.to_json
end
{% endhighlight %}

So now we make one initial GET request for the ids, and then asynchronously GET each item:

{% highlight javascript %}
$(function() {
  $.get('/item_ids', function(ids) {
    ids = JSON.parse(ids);
    for (var i = 0; i < ids.length; ++i) {
      $.get('/item/' + ids[i], function(item) {
        item = JSON.parse(item);
        var tr = $('<tr>');
        tr.append($('<td>').html(item.id));
        tr.append($('<td>').html(item.name));
        tr.append($('<td>').html(item.age));

        $('#items').append(tr);
      });
    }
  });
});
{% endhighlight %}

But maybe we want to let the user know what the ids are as soon as we know them. So we do some kind of clever stuff with HTML id fields:

{% highlight javascript %}
for (var i = 0; i < ids.length; ++i) {
  var tr = $('<tr>').attr('id', ids[i]);
  tr.append($('<td>').html(ids[i]));
  $('#items').append(tr);
  $.get('/item/' + ids[i], function(item) {
    item = JSON.parse(item);
    var tr = $('tr#' + item.id);
    tr.append($('<td>').html(item.name));
    tr.append($('<td>').html(item.age));
  });
}
{% endhighlight %}

This is a little cumbersome, but not too bad. So let's be annoying and add another problem:

{% highlight ruby %}
# additional expensive computation
get '/num_friends/:id' do |id|
  sleep 1
  {:id => id, :num_friends => rand(100)}.to_json
end
{% endhighlight %}

Okay, so we want to process each item in parallel, and processing each item entails fetching multiple pieces of data in parallel. We could try something like this:

{% highlight javascript %}
for (var i = 0; i < ids.length; ++i) {
  var tr = $('<tr>').attr('id', ids[i]);
  tr.append($('<td>').html(ids[i]));
  $('#items').append(tr);
  $.get('/item/' + ids[i], function(item) {
    item = JSON.parse(item);
    var tr = $('tr#' + item.id);
    tr.append($('<td>').html(item.name));
    tr.append($('<td>').html(item.age));
  });
  $.get('/num_friends/' + ids[i], function(resp) {
    resp = JSON.parse(resp);
    var tr = $('tr#' + resp.id);
    tr.append($('<td>').html(resp.num_friends));
  });
}
{% endhighlight %}

But what happens if `/num_friends` happens to respond before `/item` ? The columns in our table will end up being out of order.

We can try to solve this with some more clever id use:

{% highlight javascript %}
for (var i = 0; i < ids.length; ++i) {
  var tr = $('<tr>').attr('id', ids[i]);
  tr.append($('<td>').html(ids[i]));
  tr.append($('<td>').attr('id', 'name'));
  tr.append($('<td>').attr('id', 'age'));
  tr.append($('<td>').attr('id', 'num_friends'));
  $('#items').append(tr);
  $.get('/item/' + ids[i], function(item) {
    item = JSON.parse(item);
    var tr = $('tr#' + item.id);
    tr.find('#name').html(item.name);
    tr.find('#age').html(item.age);
  });
  $.get('/num_friends/' + ids[i], function(resp) {
    resp = JSON.parse(resp);
    var tr = $('tr#' + resp.id);
    tr.find('#num_friends').html(resp.num_friends);
  });
}
{% endhighlight %}

We add all the columns we'll need ahead of time, and then just fill the appropriate ones in when we get our data back.

This is starting to get pretty hacky. Let's try [angular.js](http://angularjs.org/).

Here's our angular-ized html:

{% highlight html %}
<!doctype html>
<html ng-app>
  <head>
    <script src="/angular.js"></script>
    <script src="/app.js"></script>
  </head>
  <body>
    <div ng-controller="AppCtrl">
      <table>
        <tr>
          <th>id</th>
          <th>name</th>
          <th>age</th>
          <th>num friends</th>
        </tr>
        <tr ng-repeat="item in items">
          <td>{% raw %}{{item.id}}{% endraw %}</td>
          <td>{% raw %}{{item.name}}{% endraw %}</td>
          <td>{% raw %}{{item.age}}{% endraw %}</td>
          <td>{% raw %}{{item.num_friends}}{% endraw %}</td>
        </tr>
      </table>
    </div>
  </body>
</html>
{% endhighlight %}

And our new app logic:

{% highlight javascript %}
function AppCtrl($scope, $http) {
  $scope.items = {};

  $http.get('/item_ids').success(function(ids) {
    for (var i = 0; i < ids.length; ++i) {
      $scope.items[ids[i]] = {id: ids[i]}
      $http.get('/item/' + ids[i]).success(function(item) {
        $scope.items[item.id].name = item.name;
        $scope.items[item.id].age = item.age;
      });
      $http.get('/num_friends/' + ids[i]).success(function(resp) {
        $scope.items[resp.id].num_friends = resp.num_friends
      });
    }
  });
}
{% endhighlight %}

The entire connection between the view and data is encapsulated into `$scope.items`. The html reads from `$scope.items` without worrying about whether or not the fields are available yet, the javascript updates `$scope.items` without worrying about messing with the UI at all, and angular magic takes care of the rest.

## A loading indicator

Now let's say we want to display a message while we're loading each item. First we define a function in our controller to tell us when an item is done:

{% highlight javascript %}
$scope.finished = function(item) {
  return item.name != undefined && item.num_friends != undefined;
}
{% endhighlight %}

and then we just add an extra `td` to our rows with an `ng-hide` directive:

{% highlight html %}
<tr ng-repeat="item in items">
  <td>{% raw %}{{item.id}}{% endraw %}</td>
  <td>{% raw %}{{item.name}}{% endraw %}</td>
  <td>{% raw %}{{item.age}}{% endraw %}</td>
  <td>{% raw %}{{item.num_friends}}{% endraw %}</td>
  <td ng-hide="finished(item)">loading</td>
</tr>
{% endhighlight %}

That's _all_. If we'd kept using jQuery, we'd need to do something like manually check `finished(item)` after each piece of data to see if the item's complete yet, and then do something like `$('td#loading').hide()`. None of that with angular.
