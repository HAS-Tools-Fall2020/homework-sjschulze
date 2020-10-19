## Scott Schulze, 10/18/2020, Homework #8 aka code review #1 readme

# Model summary

The AR model that I built is a simple lag-2 autoregression. This was done to keep things as simple as possible with respect to the regressions. The dataset that I used to train the model however was tuned from 200 that I had originally used with my reviewer to 275. The 275 data points chosen were the 275 lowest flow weeks of the dataset, and was increased to 275 to help mitigate the under-forecasting of the model without an increase in the spread (r^2) of the data.

# Forecast generation

To generate my forecasts I used a function to call the autoregressive modeling features. This was then placed in a loop to generate all 16 forecasts. The output seemed to be reasonable so I used the model outputs for my forecasts.

# Peer evaluation

Following my peer evaluation, I made efforts to further define my variables used in my function in the docstring. I also made certain to change my script to have the proper pathing to my data. Using the positive feedback I received regarding how compact and neat my script was I further edited and refined where able, which leads me to....

# What I am most proud of in my script

I am most proud of the succinctness of my script, I accomplished the tasks in a relatively short block of script, which having seen other's work, is a unique feature. This brevity makes the whole appearance neater and I like that. I was told in a programming code once that you can write anything in an infinite number of lines of code, but the skill is in doing so in FEW lines.
