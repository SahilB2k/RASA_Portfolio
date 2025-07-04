#!/bin/bash
#!/bin/bash

web: rasa run --enable-api --cors "*" --port $PORT
