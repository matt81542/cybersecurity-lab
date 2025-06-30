# Splunk SIEM Log Analysis - Failed Login Detection

## Overview

This folder contains an example Splunk query (SPL) to detect repeated failed login attempts, which may indicate a brute force attack or unauthorized access attempts.

## Query Explanation

```spl
source="auth.log" sourcetype="linux_secure" "Failed password"
| rex field=_raw "from (?<src_ip>\d+\.\d+\.\d+\.\d+)"
| stats count by src_ip
| where count > 3
| sort - count

```
See example output: [failed_login_detection_results.csv](./failed_login_detection_results.csv)
