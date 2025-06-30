# Splunk SIEM Log Analysis - Failed Login Detection

## Overview

This folder contains an example Splunk query (SPL) to detect repeated failed login attempts, which may indicate a brute force attack or unauthorized access attempts.

## Query Explanation

```spl
index=your_index sourcetype=your_sourcetype ("failed login" OR "authentication failure")
| stats count by src_ip
| where count > 5
| sort - count

```
See example output: [failed_login_detection_results.csv](./failed_login_detection_results.csv)
