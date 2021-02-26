#!/bin/bash

download_link=https://github.com/ArjunSahlot/2d_minecraft/archive/main.zip
temporary_dir=$(mktemp -d) \
&& curl -LO $download_link \
&& unzip -d $temporary_dir main.zip \
&& rm -rf main.zip \
&& mv $temporary_dir/2d_minecraft-main $1/2d_minecraft \
&& rm -rf $temporary_dir
echo -e "[0;32mSuccessfully downloaded to $1/2d_minecraft[0m"
