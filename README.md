#HASI - Home Analytical System Interface

##eMetering for everyone

While the need for more efficient use of energy is commonly accepted,
for the individual it is often difficult to act accordingly. Firstly,
there may be an information lack about the energy costs caused by a
certain activity or a neglected activity, such as leaving on lights
or electrical appliances in stand-by mode. So-called eMetering
devices aim at filling this information gap. Mounted between a socket
outlet and an electrical appliance they measure power consumption
and may translate consumption values into monetary costs. However,
the provision of information about energy consumption alone does not
necessarily imply acting. Rather, assisting people in actually
changing their behaviours is a much harder challenge.

The question of how to utilize computer technology to assist people
in changing behaviours, especially to get rid of bad habits,
is dealt within the field of "persuasive computing". A pioneer
in this field is BJ Fogg from Stanford University who postulates
the statement "Put triggers in the path of motivated people"
as a design mantra for behaviour change. According to
Fogg's behaviour model, for a behaviour change to happen
three factors must coincide:
 * the person must be motivated in principle,
 * a trigger must be present that just-in-time reminds
   the user to do the right thing instantly, and 
 * he/she must be able to act.

While metering devices as well as home automation hardware
are available on the market there is the problem of
non-interoperability of hardware components produced
by different vendors. HASI is a first try at implementing
a layered architecture able to communicate with various devices
through their protocols.

##The team

HASI was implemented during the summer term 2011 at
Augsburg University of Applied Sciences. The project was a part if the global research program called [IT4SE](http://it4se.informatik.fh-augsburg.de/project_german.html).

The team consists of:

* Miriam Berschneider
* Jennifer Meier
* Falk Alexander
* Martin Gutmair
* Thomas Hipp [(Github profile)](https://github.com/monstermunchkin)
* Tobias Scholze
* Christoph Biesinger
* Felix Wagner
 
## Technologies
It runs on a lightweight open source system (Linux and Python) and uses a MySQL database as a backend. It is able to run on small-scale, low energy consuming hardware (e.g. an IoT-device) within a user's home. Event notifications from sensors as well as power consumption measurements are logged in the database and are made accessible as a web-resource for other services. A test installation of HASI including sensors for power consumption,
temperature and state indicators for windows and doors has been set-up at an apartment and run from May to July 2011. HASI is / was now installed in a office room at the faculty of computer science and serves as a test-bed for further development.

<center>
<img src="https://github.com/tscholze/py-hasi-home-analytical-system-interface/blob/master/documentation/screenshots/screenshot-annotations-desktop.png" title="Desktop UI with annotations"  width="500"/>

<img src="https://github.com/tscholze/py-hasi-home-analytical-system-interface/blob/master/documentation/screenshots/screenshot-smartphone-tablet-ui.png" title="Smartphone and Tablet UI screenshot" width="500"/>
</center>


## Recommended files to read
To get a better understanding what HASI is / was. Please read the (German) [presenation slides](https://github.com/tscholze/py-hasi-home-analytical-system-interface/blob/master/documentation/hasi_presentation.pdf).

## Keep in mind
HASI is out of development for years now. All dependencies are dated-out or mostly no longer available to download. This repository is a one-time mirror of Felix's Bitbucket project. 
