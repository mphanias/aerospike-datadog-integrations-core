# CHANGELOG - lighttpd

<!-- towncrier release notes start -->

## 3.5.1 / 2024-05-31

***Fixed***:

* Update the description for the `tls_ca_cert` config option to use `openssl rehash` instead of `c_rehash` ([#16981](https://github.com/DataDog/integrations-core/pull/16981))

## 3.5.0 / 2024-02-16 / Agent 7.52.0

***Added***:

* Update the configuration file to include the new oauth options parameter ([#16835](https://github.com/DataDog/integrations-core/pull/16835))

## 3.4.0 / 2024-01-05 / Agent 7.51.0

***Added***:

* Bump the Python version from py3.9 to py3.11 ([#15997](https://github.com/DataDog/integrations-core/pull/15997))

## 3.3.1 / 2023-08-18 / Agent 7.48.0

***Fixed***:

* Update datadog-checks-base dependency version to 32.6.0 ([#15604](https://github.com/DataDog/integrations-core/pull/15604))

## 3.3.0 / 2023-08-10

***Added***:

* Update generated config models ([#15212](https://github.com/DataDog/integrations-core/pull/15212))

***Fixed***:

* Fix types for generated config models ([#15334](https://github.com/DataDog/integrations-core/pull/15334))

## 3.2.1 / 2023-07-10 / Agent 7.47.0

***Fixed***:

* Bump Python version from py3.8 to py3.9 ([#14701](https://github.com/DataDog/integrations-core/pull/14701))

## 3.2.0 / 2022-09-16 / Agent 7.40.0

***Added***:

* Update HTTP config spec templates ([#12890](https://github.com/DataDog/integrations-core/pull/12890))

## 3.1.0 / 2022-04-05 / Agent 7.36.0

***Added***:

* Add metric_patterns options to filter all metric submission by a list of regexes ([#11695](https://github.com/DataDog/integrations-core/pull/11695))

***Fixed***:

* Remove outdated warning in the description for the `tls_ignore_warning` option ([#11591](https://github.com/DataDog/integrations-core/pull/11591))

## 3.0.0 / 2022-02-19 / Agent 7.35.0

***Changed***:

* Add tls_protocols_allowed option documentation ([#11251](https://github.com/DataDog/integrations-core/pull/11251))

***Added***:

* Add `pyproject.toml` file ([#11389](https://github.com/DataDog/integrations-core/pull/11389))

***Fixed***:

* Fix namespace packaging on Python 2 ([#11532](https://github.com/DataDog/integrations-core/pull/11532))

## 2.0.0 / 2022-01-08 / Agent 7.34.0

***Changed***:

* Add `server` default group for all monitor special cases ([#10976](https://github.com/DataDog/integrations-core/pull/10976))

***Fixed***:

* Fix lighttpd service check name for monitors ([#10977](https://github.com/DataDog/integrations-core/pull/10977))
* Add comment to autogenerated model files ([#10945](https://github.com/DataDog/integrations-core/pull/10945))

## 1.14.0 / 2021-10-04 / Agent 7.32.0

***Added***:

* Add runtime configuration validation ([#8947](https://github.com/DataDog/integrations-core/pull/8947))
* Add HTTP option to control the size of streaming responses ([#10183](https://github.com/DataDog/integrations-core/pull/10183))
* Add allow_redirect option ([#10160](https://github.com/DataDog/integrations-core/pull/10160))

***Fixed***:

* Fix the description of the `allow_redirects` HTTP option ([#10195](https://github.com/DataDog/integrations-core/pull/10195))

## 1.13.2 / 2021-03-07 / Agent 7.27.0

***Fixed***:

* Bump minimum base package version ([#8443](https://github.com/DataDog/integrations-core/pull/8443))

## 1.13.1 / 2020-11-03 / Agent 7.24.0

***Fixed***:

* Remove default `encoding` example in logs config ([#7916](https://github.com/DataDog/integrations-core/pull/7916))

## 1.13.0 / 2020-10-31

***Added***:

* Add ability to dynamically get authentication information ([#7660](https://github.com/DataDog/integrations-core/pull/7660))
* Add lighttpd logs ([#7719](https://github.com/DataDog/integrations-core/pull/7719))

## 1.12.0 / 2020-09-21 / Agent 7.23.0

***Added***:

* Add RequestsWrapper option to support UTF-8 for basic auth ([#7441](https://github.com/DataDog/integrations-core/pull/7441))

***Fixed***:

* Update proxy section in conf.yaml ([#7336](https://github.com/DataDog/integrations-core/pull/7336))

## 1.11.0 / 2020-08-10 / Agent 7.22.0

***Added***:

* Add config specs ([#7057](https://github.com/DataDog/integrations-core/pull/7057))

***Fixed***:

* DOCS-838 Template wording ([#7038](https://github.com/DataDog/integrations-core/pull/7038))
* Update ntlm_domain example ([#7118](https://github.com/DataDog/integrations-core/pull/7118))

## 1.10.0 / 2020-06-29 / Agent 7.21.0

***Added***:

* Add note about warning concurrency ([#6967](https://github.com/DataDog/integrations-core/pull/6967))

## 1.9.0 / 2020-05-17 / Agent 7.20.0

***Added***:

* Allow optional dependency installation for all checks ([#6589](https://github.com/DataDog/integrations-core/pull/6589))

## 1.8.1 / 2020-04-04 / Agent 7.19.0

***Fixed***:

* Update deprecated imports ([#6088](https://github.com/DataDog/integrations-core/pull/6088))

## 1.8.0 / 2020-02-22 / Agent 7.18.0

***Added***:

* Add version metadata ([#5600](https://github.com/DataDog/integrations-core/pull/5600))

## 1.7.0 / 2019-12-02 / Agent 7.16.0

***Added***:

* Add auth type to RequestsWrapper ([#4708](https://github.com/DataDog/integrations-core/pull/4708))

## 1.6.0 / 2019-10-11 / Agent 6.15.0

***Added***:

* Add option to override KRB5CCNAME env var ([#4578](https://github.com/DataDog/integrations-core/pull/4578))

***Fixed***:

* Fix lighttpd logging format ([#4716](https://github.com/DataDog/integrations-core/pull/4716))
* Fix support for no authentication ([#4689](https://github.com/DataDog/integrations-core/pull/4689))

## 1.5.0 / 2019-08-24 / Agent 6.14.0

***Added***:

* Add requests wrapper to lighttpd ([#4220](https://github.com/DataDog/integrations-core/pull/4220))

***Fixed***:

* Update __init__ method params ([#4243](https://github.com/DataDog/integrations-core/pull/4243))

## 1.4.0 / 2019-05-14 / Agent 6.12.0

***Added***:

* Adhere to code style ([#3532](https://github.com/DataDog/integrations-core/pull/3532))

## 1.3.0 / 2019-01-04 / Agent 6.9.0

***Added***:

* Support Python 3 ([#2834][1])

## 1.2.1 / 2018-09-04 / Agent 6.5.0

***Fixed***:

* Add data files to the wheel package ([#1727][2])

## 1.2.0 / 2018-05-11

***Added***:

* Support digest authentication on the server status page.

## 1.1.0 / 2018-03-23

***Added***:

* Adds custom tag support to service checks.

## 1.0.0 / 2017-03-22

***Added***:

* adds lighttpd integration.

[1]: https://github.com/DataDog/integrations-core/pull/2834
[2]: https://github.com/DataDog/integrations-core/pull/1727