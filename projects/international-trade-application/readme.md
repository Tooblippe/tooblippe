![trade](assets/case-slide-trade.PNG)

#### Development of international trade application that is used by clients and governments in South-Africa, Australia, New-Zealand and Europe,

# Background
An internationally acclaimed Economist developed an international trade application for local and international clients.
The initial application was shipped as a Qlik (Tableau) package. The prohibitive licencing costs, significant effort to update
as well as the extremely large datasets made this distribution model difficult. The application was ported to a web application.


# Solution provided
A specialised web application was developed using the Vuejs framework for the front-end development and Django as the backed.
The solution is connected to a managed Postgres database and hosted via a load balancer.


# Unique project attributes
The Django backend primary deals with complex report generation based on a specific set of parameters and study boundaries 
defined by the user using the front end application. The application needed these outputs to be in the main Microsoft Office
formats due to client requirements.

### Specialised Word report generation
One of the main strengths of the application is the automatic generation of Microsoft Word reports. PDF reports would 
not be sufficient since it is mostly non editable. The clients would obtain a near 100% populated Word report for 
the specific study that was conducted and only has to do minimal editing for specific use cases. A template system was
developed that allows for the population of a present Word template as well as writing Pandas Data frames directly into 
embedded Word graphs. Each word document will have the client template and corporate identity applied to the document. This includes
* dynamic image insertion
* table creation and population
* live and linked graphs
* dynamic addition of reporting sections based on number of report entities
* dynamic interpretation of results leads to specific text updates in the report

### Specialised PowerPoint generation
The application also generates publication ready PowerPoint slides with the client template and corporate identity applied to
the slide deck.

### Specialised Excel generation
The application also allows for the offloading of large datasets into a pre-set Excel analysis environment. This enables
more advanced users to fine tune a specific economic study.


## Timeframe and Budget
The project was developed over a period of two years with a Budget of R1,500,000.
The appication is stull under development and more features are introduced during a 6 week cycle.

# Tools Employed
## Frontend
* vuejs
* vuex
* vue-router
* axios


## Backend
* Python
* Django
* pandas
* postgres

## Deployment platform
* Digital Ocean
