# Scraper Wiktionary
### Piotr Filochowski 66076

### Input
Inut is a path to a file with list of url's for scraping. Example file is added to project.
Urls should be separated by semicolons.

### Output
Scraper creates json files with such structure:

```json
{
	"language1": "polski",
	"language2": "angielski",
	"words": [{
			"language1": "baleron m",
			"language2": "gammon",
			"photo": "/url/photos/baleron_m"
		}, {
			"language1": "baleron m",
			"language2": "gammon",
			"photo": "/url/photos/baleron_m"
		}
	]
}
```
and saves files to /output/url
Photos are beeing saved in seperated files in base64 format



