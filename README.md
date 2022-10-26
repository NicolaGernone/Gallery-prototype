# Gallery Tracking Optimizer

Most of the e-commerces have a product gallery on their website, where they show their products to the customers trying
to sell them but showing how other buyers are using/consuming it. These galleries, most of the time, are a 
good complement for their websites, as the conversion rate is better than ~~fake~~ plain product images. 

Despite that, most of the companies that offer these services (creating a gallery from the e-commerce catalogue) has a 
very weak and poor technology behind. So, we want to create an amazing API where the companies can 
create a gallery for their website and optimize it based on user interest. 

## How it works?

The aim of this API is to **load a dataset of images**, provided by the company, and 
**sort them regarding a calculated weight**. To be able to calculate these weights, the client of this API will inform 
us every time a user `view` or `click` over any of the images showed on the gallery.

Those events will help our *super-fancy algorithm* to create an amazing order where the most interacted images will be
at the top of the gallery, and the least, at the bottom. 

You could find the whole description of the API in the [OpenAPI description file](/api.spec.yaml)

### Order algorithm 

As we said, one of the most important things on an e-commerce gallery is the order you show the images to the user, 
finding a way to optimize the ROI vs the interest of the users.

So, in this case we want to implement a really simple, but effective, algorithm. 

For the first version of this API we will just have 2 type of events:
* `view` → When the image is rendered on the user's screen. So, if the gallery has a pagination and the user is 
 scrolling down, every time an image is rendered, this event will be dispatched.
* `click` → When any user clicks on the image to see the product behind, or anywhere that the company wants to redirect 
 the user, this event will be triggered.

As you may know, when a user `click` on an image, the level of interest on this image/product is way higher than just a 
view. In our case **the `click` will represent a 70% of interest, while a `view` just 30%**.

So, our algorithm will take this into account to calculate the `weight` of every image and specify an optimized order.
You should calculate this and perform the best algorithm for your case. 

### Workflow

The workflow of this API is as follows:
1. **Collect the data**, synchronously, and store them in terms of being able to track the events later and optimize the
grid. By default, the order would be based on the creation timestamp (the most recently first). 
[Here](https://static.rviewer.io/challenges/datasets/gallery-tracking-optimizer/data.json) you could find the given 
dataset to request. 
2. **Start receiving events** and calculating the weight for the image where the event has been dispatched. At this 
point, you should **optimize the order of the images**. Choose the best algorithm to sort the entire dataset, taking 
into account the time and complexity of your implementation. 
3. **Serve the images** with the expected order. 

## Technical requirements

* Create a **clean**, **maintainable** and **well-designed** code. We expect to see a good and clear architecture that
allows to add or modify the solution without so much troubles. 
* **Test** your code until you are comfortable with it. We don't expect a 100% of Code Coverage but some tests that
helps to have a more stable and confident base code. 

To understand how you take decisions during the implementation, **please write a COMMENTS.md** file explaining some of 
the most important parts of the application. You would also be able to defend your code through 
[Rviewer](https://rviewer.io), once you submit your solution.

## Technical Considerations

The order of the images will change as the API is receiving events, so you can solve this using multiple approaches, 
think about the trade-offs of yours before implementing it. We are not expecting to see the most scalable solution
but the rationale behind it 😊

---

## How to submit your solution

* Push your code to the `devel` branch - we encourage you to commit regularly to show your thinking process was.
* **Create a new Pull Request** to `main` branch & **merge it**.

Once merged you **won't be able to change or add** anything to your solution, so double-check that everything is as 
you expected!

Remember that **there is no countdown**, so take your time and implement a solution that you are proud!

--- 

<p align="center">
  If you have any feedback or problem, <a href="mailto:help@rviewer.io">let us know!</a> 🤘
  <br><br>
  Made with ❤️ by <a href="https://rviewer.io">Rviewer</a>
</p>
