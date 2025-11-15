# The United States PostgreSQL Association website

These are the PgUS templates which override the PgEU templates.

## Installation

### Setting up PgEU

* Clone the [PgUS fork](https://github.com/pg-us/pgeu-system) of the PgEU codebase.
  * This fork is the same as the base system, but with devcontainers for Podman/VSCode
* Start the dev container with whatever you'd prefer. This has mostly been tested in VSCode.
* Run `./install.sh` from within the dev container to configure the super user, the local settings, etc.
* Run `python3 manage.py runserver` to start the server. You should see unskinned pages at this point.

### Applying Our Skin

* Clone this repository in a folder *next to the pgeu-system*.
  * The pgeu dev container has access to all peer directories of `pgeu-system` to enable skins.
* Add `SYSTEM_SKIN_DIRECTORY = "/workspaces/pgusweb"` to `local_settings.py`
* Non-HTML assets will need to be symlinked with `ln -s pgusweb/media/pgus pgeu-system/media`...
* ...and then excluded from PgEU's git with `echo 'media/pgus' > .git/info/exclude`

## Future Setup Improvements

Relying on Dev Containers is not ideal for non-VSCode users, we should migrate to basic Docker tooling.

The _ideal_ docker setup would also use the `uwsgi` server instead of the Django server. This should remove the need to symlink the PgUS assets.

## License

The code for the website is licensed under `The PostgreSQL Licence
<http://www.opensource.org/licenses/postgresql>`_, which is closely related to
the BSD license.

