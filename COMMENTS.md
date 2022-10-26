## Steps

Setting models, organize DB Table of Images with the parameters needed, for now i'm implementing it for 1 user only, after i'll change it for multimples users.

Adjusting settings to the env and creating the admin page to add images to DB.

This option is not good for a lot of data but i'm having issues with manage.py loaddata command for the data.json file that i have. i'll check again in the multiple user implementation.

I decide to implement the api structure in 3 parts, the service that collects the DB datas and serialize them, the client that is the Api view that make tha calls (get, post in this case) and the django view to render the templates. To records the events i choose to use ajax to be able to collect the events in the fornt part.

For user usability i decided to add the categories field to the image entity and use it for filter in a future the images.

For that i create a DB table with the categories names to allow to add them in the future without enter in the code to modify some list.

I add to event table the userId field, this will the events for all the user that will use the app.

I decide to change the view structure to make it more compact and http oriented so the ApiView will render the response directly.

Due to the null  weight in the events table a better and effective way to sort the data is by ORDER BY weight, is good for few data but if the quantity is very large it could  slow a lot the query buffer.

The UI part is a mockup to make the page look nice and more or less as it will be presented.

Change of mind, order by with decimal do not work properly so i adapt a sorted function to my key and NoneType elements and it works.

With this implementation the Gridposition value is not really needed, it represent the row-column intersection in the front but is not usefull in the response body.

Tests for models are quite simples because i did'n need to implement or override any method of the model, i kept them easy.

Making api view tests i could be able to made some correction to exeptions and database transactions.

# Considerations

I think django is not very usefull for a Hexagonal arquitecture, it loose a bit what is his structure and agility.

The need to use connection to DB could slow down a lot the the application if the quantity of the files is very large.

I try to mantain the queries very simple to not slow down the buffer connetion but it require a lot of calls to check the existence and the consistance of the data.

Making tests i could be able to made some correction to exeptions and database transactions.

# Usage

Create a super user with `make superuser` , use it to login, from admin page is possible to move to gallery and from gallery to admin. In Administration is allowed to create new instances for image entity and new users.