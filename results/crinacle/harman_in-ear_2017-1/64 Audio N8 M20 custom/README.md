# 64 Audio N8 M20 custom
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.2; 23 -11.2; 25 -11.2; 28 -11.1; 31 -11.0; 34 -10.8; 37 -10.7; 41 -10.5; 45 -10.4; 49 -10.3; 54 -10.1; 60 -10.0; 66 -9.9; 72 -9.9; 79 -10.0; 87 -10.0; 96 -10.0; 106 -10.1; 116 -10.2; 128 -10.3; 141 -10.4; 155 -10.4; 170 -10.5; 187 -10.5; 206 -10.5; 227 -10.4; 249 -10.3; 274 -10.3; 302 -10.1; 332 -9.9; 365 -9.6; 402 -9.4; 442 -9.2; 486 -8.9; 535 -8.6; 588 -8.3; 647 -7.9; 712 -7.5; 783 -7.0; 861 -6.6; 947 -6.5; 1042 -6.8; 1146 -7.4; 1261 -8.1; 1387 -8.5; 1526 -8.4; 1678 -8.0; 1846 -7.4; 2031 -6.4; 2234 -5.1; 2457 -3.6; 2703 -2.4; 2973 -1.6; 3270 -1.2; 3597 -1.4; 3957 -1.9; 4353 -2.2; 4788 -2.8; 5267 -3.0; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.1; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.7; 13660 -18.7; 15026 -29.2; 16529 -30.5; 18182 -26.8; 20000 -20.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 M20 custom GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 M20 custom ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 19 Hz    | 0.66 | -3.7 dB  |
| Peaking | 327 Hz   | 0.1  | -3.7 dB  |
| Peaking | 5380 Hz  | 0.38 | 18.0 dB  |
| Peaking | 12146 Hz | 1.43 | 17.6 dB  |
| Peaking | 15308 Hz | 0.37 | -36.1 dB |
| Peaking | 914 Hz   | 0.94 | 6.5 dB   |
| Peaking | 1375 Hz  | 0.52 | -6.6 dB  |
| Peaking | 2925 Hz  | 1.24 | 5.0 dB   |
| Peaking | 5429 Hz  | 1.71 | -4.2 dB  |
| Peaking | 6025 Hz  | 3.81 | 5.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.8 dB  |
| Peaking | 62 Hz    | 1.41 | -2.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.9 dB  |
| Peaking | 250 Hz   | 1.41 | -3.4 dB  |
| Peaking | 500 Hz   | 1.41 | -1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 6.9 dB   |
| Peaking | 16000 Hz | 1.41 | -30.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/64%20Audio%20N8%20M20%20custom/64%20Audio%20N8%20M20%20custom.png)