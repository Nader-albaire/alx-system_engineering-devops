0x10-https_ssl#!/usr/bin/env bash

# Function to display information about a specific subdomain
function subdomain_check {
    local domain="$1"
    local subdomain="$2"

    # Use dig to get DNS information for the subdomain
    local dns_info=$(dig "${subdomain}.${domain}" | awk '/^;; ANSWER SECTION:/{getline; print}')

    # Extract the record type and destination IP address
    local record_type=$(echo "$dns_info" | awk '{print $4}')
    local destination=$(echo "$dns_info" | awk '{print $5}')

    # Output the information
    printf "The subdomain %s is a %s record and points to %s\n" "$subdomain" "$record_type" "$destination"
}

# Function to display information about default subdomains
function domain_check {
    local domain="$1"
    local subdomains=("www" "lb-01" "web-01" "web-02")

    # Loop through default subdomains and display information
    for subdomain in "${subdomains[@]}"; do
        subdomain_check "$domain" "$subdomain"
    done
}

# Main script

# Check if domain parameter is provided
if [[ $# -lt 1 ]]; then
    echo "*** Provide domain name ***"
    exit 1
fi

# Check if both domain and subdomain parameters are provided
if [[ $# -eq 2 ]]; then
    subdomain_check "$1" "$2"
else
    domain_check "$1"
fi

