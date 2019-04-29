# 64 Audio N8 M15 custom sample 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.3; 23 -11.5; 25 -11.7; 28 -11.8; 31 -11.9; 34 -11.9; 37 -11.8; 41 -11.8; 45 -11.8; 49 -11.8; 54 -11.7; 60 -11.7; 66 -11.7; 72 -11.7; 79 -11.8; 87 -12.0; 96 -12.0; 106 -11.9; 116 -12.1; 128 -12.0; 141 -11.9; 155 -11.8; 170 -11.7; 187 -11.6; 206 -11.4; 227 -11.2; 249 -11.0; 274 -10.8; 302 -10.5; 332 -10.1; 365 -9.8; 402 -9.5; 442 -9.2; 486 -8.9; 535 -8.5; 588 -8.1; 647 -7.6; 712 -7.2; 783 -6.7; 861 -6.3; 947 -6.2; 1042 -6.4; 1146 -7.0; 1261 -7.7; 1387 -8.1; 1526 -8.1; 1678 -7.9; 1846 -7.5; 2031 -6.7; 2234 -5.4; 2457 -3.8; 2703 -2.3; 2973 -1.0; 3270 -0.5; 3597 -0.5; 3957 -1.2; 4353 -1.9; 4788 -2.8; 5267 -1.3; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.0; 10263 -6.7; 11289 -6.5; 12418 -7.4; 13660 -15.4; 15026 -21.1; 16529 -22.8; 18182 -23.0; 20000 -18.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 M15 custom sample 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 M15 custom sample 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 75 Hz    | 0.12 | -5.6 dB  |
| Peaking | 1714 Hz  | 1.16 | -7.7 dB  |
| Peaking | 5306 Hz  | 0.26 | 14.0 dB  |
| Peaking | 12049 Hz | 2.22 | 9.3 dB   |
| Peaking | 15883 Hz | 0.27 | -22.5 dB |
| Peaking | 891 Hz   | 5.1  | 0.6 dB   |
| Peaking | 3161 Hz  | 4.98 | 0.9 dB   |
| Peaking | 4802 Hz  | 3.29 | -3.4 dB  |
| Peaking | 6108 Hz  | 1.79 | 3.6 dB   |
| Peaking | 7474 Hz  | 3.96 | -3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.3 dB  |
| Peaking | 62 Hz    | 1.41 | -3.8 dB  |
| Peaking | 125 Hz   | 1.41 | -4.4 dB  |
| Peaking | 250 Hz   | 1.41 | -3.8 dB  |
| Peaking | 500 Hz   | 1.41 | -1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.4 dB   |
| Peaking | 16000 Hz | 1.41 | -21.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/64%20Audio%20N8%20M15%20custom%20sample%203/64%20Audio%20N8%20M15%20custom%20sample%203.png)