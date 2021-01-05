# Request CLI

This is the most generic REST API form the server. This request
accept any argument from project [sherlock](https://github.com/sherlock-project/sherlock).

**TYPE:** POST
**URL:** `http://127.0.0.1:8000/cli/`

#### JSON format

```
{
    "args": "[sherlock arguments]"
}
```

#### Example

Return the version information from current server's sherlock project.

```
{
    "args": "--version"
}
```
