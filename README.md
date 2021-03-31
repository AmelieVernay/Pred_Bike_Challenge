## Repository architecture

* `Data`
    * `marchweekatnine.csv`: dataset used in `bad_pred_with_weather.ipynb`
    * `SaisiesTotem.csv`: `main dataset`
* `Methodology`: LaTeX files for `.pdf` report
* `Weather`
    * `init_weather.py`: initializes the weather dataset
    * `weather_update.py`: updates the weather dataset everyday
    * `bad_pred_with_weather.ipynb`: tests to find eventual links between weather and bike traffic (turns out to be irrelevent)
    * `lm_would_be_irrelevent.svg`: this image  is a visual proof that a linear model would be irrelevent here 
    * `weather.csv`: dataset for "weather VS bike traffic" analysis
* `load_data.py`: class loading the main dataset
* `preprocess.py`: functions for data preprocessing
* `resamp_interp_test.ipynb`: notebook for testing the relevance of the my method
* `forecast.ipynb`: notebook for bike traffic behaviour analysis