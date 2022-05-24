[Unit]
Description=beets-import-app

[Service]
WorkingDirectory=<path-to-repository>
ExecStart=/usr/bin/python <path-to-repository>/server.py --ip 0.0.0.0 --port 8899

[Install]
WantedBy=default.target