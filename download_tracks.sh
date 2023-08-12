#!/bin/bash

# Repository details
repo_url="https://github.com/aws-deepracer-community/deepracer-race-data.git"
dir_path="raw_data/tracks/npy"
tracks_dir="tracks"
tmp_dir=".temp"

# Remove the existing trackloader directory if it exists
if [ -d "$tracks_dir" ]; then
    rm -rf "$tracks_dir"
fi
mkdir $tracks_dir

git clone --no-checkout "$repo_url" "$tmp_dir"

cd "$tmp_dir"

git config core.protectNTFS false
git sparse-checkout init --cone
git sparse-checkout set "$dir_path"
git checkout main

cd ..

mv "$tmp_dir/$dir_path/"* "$tracks_dir"

rm -rf "$tmp_dir"

echo "Downloaded all tracks!"

