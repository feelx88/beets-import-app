# beets-import-app

Simple web application for importing zip files with included music into beets library.

A simple systemd service file template is provided for running the service in the backgound as the user who owns the beets library.
To use it, copy the file `beets-import-app.service.tpl` to `beets-import-app.service` and change the paths the checked out repository.

You then have to enable the service:

```
systemctl --user link <path/to/>beets-import-app.service
systemctl --user daemon-reload
systemctl --user enable beets-import-app.service
systemctl --user start beets-import-app.service
```

If you want to run it e.g. in a headless raspberry pi setup,you have to enable lingering mode for your user (https://www.freedesktop.org/software/systemd/man/loginctl.html#enable-linger%20USER%E2%80%A6):

`sudo loginctl enable-linger <username>`
