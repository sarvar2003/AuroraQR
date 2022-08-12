# Requirements
<ul>
<li><a href="https://www.docker.com/" target="_blank">Docker</a></li>
<li><a href="https://www.postgresql.org/" target="_blank">PostgreSQL</a></li>
<li><a href="https://www.gnu.org/software/make/manual/make.html">Makefile</a> (Optional)</li>
</ul>

# Setup

### Makefile installation (Optional):
Windows:
```bash
$ choco install make --source=cygwin
```


# Usage

If you have ```make``` installed, then execute the following command to spin-up the application
```bash
$ make run
```

If you don't have ```make``` installed in your PC, execute the following command to spin-up the application:
```bash
$ docker-compose up
```