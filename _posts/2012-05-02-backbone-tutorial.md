---
layout: post
title: "A Backbone.js tutorial"
---
So I've recently been trying to get into backbone.js, and I've found that the existing tutorials for it haven't been as helpful as would've liked. The [main backbone.js page](http://documentcloud.github.com/backbone/) has good documentation for all of the components, but has no real tutorials on how to put it all together, and most of the tutorials I've found are a bit out-dated, and either feel like they gloss over a lot of details, or, like the docs, don't explain exactly how to put everything together. So I thought I'd throw together my own tutorial as I went through the learning process myself.

We'll be making a simple document editing app that uses "deep linking" (ie, the resources in your app will all have unique URLs, like you'd except from a normal non-javascript app).

## Models and Collections

So first fire up a text-editor and make an `app.js` file. The first thing we'll put in this file is a definition for the model that'll hold our document:

{% highlight js %}
var Doc = Backbone.Model.extend({});
{% endhighlight %}

Well, that was easy. We don't need to really define any properties for our `Doc` model, since we can dynamically add them as we go. Just for self-documentation's sake, though, I'll modify the definition a bit:

{% highlight js %}
var Doc = Backbone.Model.extend({
  initialize: function() {
    this.title = null;
    this.body = null;
  }
)};
{% endhighlight %}

We've added an `initialize` method that just gives our model two properties, `title` and `body`, and sets them both to `null`.

Since our app is going to be dealing with multiple documents, and not just one, we'll also want to make a backbone.js collection for our documents. So let's define the class for our document collection:

{% highlight js %}
var Docs = Backbone.Collection.extend({
  model: Doc
});
{% endhighlight %}

Alright, so now we've got a class for a collection of documents. If our app was dealing with multiple sets of documents, we might end up having multiple instances of our `Docs` class, but we'll just need one. So let's make that:

{% highlight js %}
var docs = new Docs();
{% endhighlight %}

Just for fun, let's actually instantiate our `docs` collection with some data instead of having it start empty:

{% highlight js %}
var docs = new Docs([
  {id: 1, title: "Bananas", body: "Are an interesting fruit"},
  {id: 2, title: "Apples", body: "Are not quite as interesting"}
]);
{% endhighlight %}

So you'll notice that we're doing some annoying stuff with specifying our own `id` values for the documents. Eventually, we'll hook up our app with a backend that will deal with this kind of stuff for us, but for now, we're going to be assigning id values on our own. To do this, we'll just use a `next_id` variable:

{% highlight js %}
var next_id = 3; //because we already used 1 and 2
{% endhighlight %}

## Our Router

So that's it for our models and collections. We've set up (client-side) architecture for dealing with our data. Next, we're going to set up the part of our app that will handle app "state-control" and our urls: our router.

So here's the code for our router class:

{% highlight js %}
var Router = Backbone.Router.extend({
  routes: {
    '': 'index',
    'doc/:id': 'edit',
    'new': 'newDoc'
  },

  index: function() {
    console.log("index");
  },

  edit: function(id) {
    console.log("show doc " + id);
  },

  newDoc: function() {
    console.log("new doc");
  }
});
{% endhighlight %}

So our router class has this main `routes` object that maps urls to the names of functions that are defined further down in the class. Unlike "real" urls, the urls we will use will come after a `#` at the end of our site's main url. Ie, if our app is hosted on example.com, the url example.com/ or example.com/# will correspond to the index action. The url example.com/#doc/5 will correspond to the edit action wtih an id of 5.

Right now none of our actions actually do anything other than print to the javascript console, but that's okay. Let's try running our app now and see what happens.

Well, before we do that, we'll have to make an actual html page that loads our `app.js` file. We'll use this simple html file:

{% highlight html %}
<!DOCTYPE HTML>
<html>
  <head>
    <title>DocEdit</title>
  </head>
  <body>
    <!-- stuff will go here -->
    <script type="text/javascript" src="http://documentcloud.github.com/underscore/underscore.js"></script>
    <script type="text/javascript" src="http://documentcloud.github.com/backbone/backbone.js"></script>
    <script type="text/javascript" src="app.js"></script>
  </body>
</html>
{% endhighlight %}
    
We just load the `backbone.js` library and the `underscore.js` library it depends on, and then we load our own app's javascript.

Save the above as `index.html` and open it up in a web browser. You should see the message "index" in your javascript console (if you don't have access to a javascript console, you can just try changing all of the `console.log` calls to `alert` calls. Now, try changing the url bar by adding `#new` to the end of it. You should see the "new doc" message appear in your log. Now, try getting rid of the `new` part of the url and leave it with just a "#" (don't backspace the "#" too, because this will result in a page-refresh). Now you should see the "index" message again.

So cool, our app's routes are working. Now let's change the routes so that they actually, you know, do stuff. Let's go back to our index method, for example:

{% highlight js %}
index: function() {
  console.log("index");
  new IndexView({docs: docs});
},
{% endhighlight js %}

Alright, cool. So now we've got this `IndexView` object that we're instantiating with an options `docs: docs`, where the first `docs` is what we're calling the option and the second `docs` is the instance of our backbone collection that we defined before. In good MVC style, we're keeping our router/controller pretty light in terms of code, and delegating the actual rendering stuff to this `IndexView` class which we're about to define.

Although really, there's no _real_ need for views in backbone. We could, if we wanted to, just stick all of our rendering code into our router. Views are here more to just help us organize our app. Regardless, let's set up a view.

## Views

So we're going to implement the `IndexView` we talked about from above.

{% highlight js %}
var IndexView = Backbone.View.extend({
  initialize: function() {
    this.docs = this.options.docs; //cause we really don't want to be typing the whole thing each time
    this.render();
  },

  render: function() {
    var out = "<ul>";
    this.docs.each(function(doc){
      out += "<li><a href='#doc/" + doc.get('id') + "'>" + doc.get('title') + "</a></li>";
    });
    out += "</ul>";
    console.log(out);
    $(this.el).html(out);
    $('#app').html(this.el);
    return this;
  }
});
{% endhighlight %}

So in our view's initialize method, we just copy over the `this.options.docs` collection that we got from the options passed to our object and store it in `this.docs`, because we're lazy and don't want to type `this.options.docs` every time. We also call `this.render()`, which makes sure our view is rendered as soon as we create it.

The `render` method is where the real bulk of our view is. `render` sort of stupidly pastes together a bunch of html representing a `ul` of the names of all of our docs, with the name of each doc being a link to its page. It does this by using the `each` method provided by undersore.js (that other library we loaded when we set up `index.html`).

Now trying loading your page in your browser again. Now, instead of a blank page, you should see an unordered list of the two documents we hard-coded into our `docs` collection. If you click on the links for any of the documents, you should see a "show doc" message pop up, but nothing will actually happen in your app. Let's fix that by having a view for editing documents.

First, let's modify our router's `show` function:

{% highlight js %}
show: function(id) {
  new EditView({doc: docs.get(id)});
},
{% endhighlight %}

We just create an instance of an `EditView` (which we're about to define) and pass it a document from our `docs` collection.

Now, create the 'EditView' view:

{% highlight js %}
var EditView = Backbone.View.extend({
  events: {
    'submit form': 'save'
  },

  initialize: function() {
    this.doc = this.options.doc;
    this.render();
  },

  render: function() {
    var out = "<h1>New Doc</h1><form><input name='title' type='text' /><br /><input name='body' type='text' /><br /><input type='submit' value='Save' /></form>";
    $(this.el).html(out);
    $('#app').html(this.el);
  },

  save: function(event) {
    this.doc.set('title',this.$('[name=title]').val());
    this.doc.set('body',this.$('[name=body]').val());
    doc.add(this.doc);
    this.render();
    this.delegateEvents();

    return false;
  }
});
{% endhighlight %}

This view is a bit more complicated than the `IndexView` from before. The first new thing to notice is this `events` object we have. This works kind of like the `routes` object in our router. Whenever the `submit form` event occurs in our view (ie, when someone submits the form we render later on in our view), our view will run the `save` function. This is a handy way of dealing with actions for our view.

Next, we've got a pretty standard looking `initialize` function, followed by `render`. `render` does this whole ugly "paste a bunch of html into a string" thing, which we'll fix later, but for now, it works and it's simple.

Lastly, we have `save`, which is the function that actually saves our modified document....
