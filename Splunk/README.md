# Splunk SIEM Example Queries

This repo demonstrates example SPL queries for SIEM detections using Splunk Cloud.

## Sample Logs

- `failed_ssh.log` — Sample Linux SSH failed login events.

## Queries

- `failed_login_extraction.spl` — Extract user and source IP from failed login logs.
- `failed_login_bruteforce.spl` — Detect brute force login attempts (multiple failures within 5 minutes).

## Usage

1. Upload `failed_ssh.log` to Splunk Cloud, assign sourcetype `linux secure`.
2. Run the queries in the `/queries` folder.
3. Review dashboards or alerts built on these detections.
4. See csv files in `extracts` for example outputs.
