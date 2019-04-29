# 64 Audio N8 M15 sample 4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.5; 23 -7.7; 25 -7.8; 28 -7.9; 31 -7.9; 34 -7.9; 37 -7.9; 41 -7.8; 45 -7.8; 49 -7.7; 54 -7.7; 60 -7.6; 66 -7.5; 72 -7.5; 79 -7.6; 87 -7.7; 96 -7.7; 106 -7.6; 116 -7.7; 128 -7.6; 141 -7.5; 155 -7.3; 170 -7.2; 187 -7.0; 206 -6.8; 227 -6.6; 249 -6.3; 274 -6.1; 302 -5.9; 332 -5.6; 365 -5.4; 402 -5.2; 442 -5.1; 486 -4.9; 535 -4.8; 588 -4.6; 647 -4.4; 712 -4.1; 783 -3.8; 861 -3.5; 947 -3.4; 1042 -3.6; 1146 -4.2; 1261 -4.9; 1387 -5.4; 1526 -5.3; 1678 -4.8; 1846 -4.2; 2031 -3.7; 2234 -3.2; 2457 -2.6; 2703 -2.0; 2973 -1.5; 3270 -1.3; 3597 -1.7; 3957 -2.5; 4353 -3.0; 4788 -4.3; 5267 -3.1; 5793 -0.5; 6373 -1.9; 7010 -3.0; 7711 -4.2; 8482 -4.5; 9330 -4.5; 10263 -4.5; 11289 -4.5; 12418 -4.5; 13660 -4.5; 15026 -4.5; 16529 -5.0; 18182 -13.0; 20000 -8.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 M15 sample 4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 M15 sample 4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 49 Hz    | 0.19 | -3.4 dB  |
| Peaking | 850 Hz   | 3.47 | 1.3 dB   |
| Peaking | 3910 Hz  | 0.81 | 2.5 dB   |
| Peaking | 16308 Hz | 1.48 | 4.3 dB   |
| Peaking | 18604 Hz | 0.97 | -10.5 dB |
| Peaking | 1501 Hz  | 3.6  | -1.7 dB  |
| Peaking | 3014 Hz  | 3.01 | 1.2 dB   |
| Peaking | 4950 Hz  | 3.46 | -3.9 dB  |
| Peaking | 5798 Hz  | 3.67 | 4.2 dB   |
| Peaking | 8226 Hz  | 4.01 | -0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -2.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/64%20Audio%20N8%20M15%20sample%204/64%20Audio%20N8%20M15%20sample%204.png)