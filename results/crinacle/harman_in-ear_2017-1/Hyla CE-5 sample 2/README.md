# Hyla CE-5 sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.2; 23 -7.2; 25 -7.3; 28 -7.2; 31 -7.2; 34 -7.1; 37 -7.1; 41 -7.0; 45 -6.9; 49 -6.8; 54 -6.7; 60 -6.6; 66 -6.6; 72 -6.6; 79 -6.6; 87 -6.5; 96 -6.5; 106 -6.5; 116 -6.4; 128 -6.2; 141 -6.0; 155 -5.8; 170 -5.5; 187 -5.6; 206 -5.2; 227 -4.8; 249 -4.4; 274 -4.0; 302 -3.6; 332 -3.1; 365 -2.7; 402 -2.4; 442 -2.2; 486 -2.0; 535 -1.8; 588 -1.7; 647 -1.6; 712 -1.6; 783 -1.5; 861 -1.6; 947 -2.0; 1042 -2.7; 1146 -3.8; 1261 -4.8; 1387 -5.4; 1526 -5.6; 1678 -5.5; 1846 -5.3; 2031 -4.8; 2234 -3.8; 2457 -2.7; 2703 -1.6; 2973 -1.0; 3270 -0.9; 3597 -1.6; 3957 -2.9; 4353 -4.0; 4788 -3.6; 5267 -2.0; 5793 -0.5; 6373 -0.6; 7010 -1.0; 7711 -3.0; 8482 -3.3; 9330 -6.0; 10263 -5.3; 11289 -3.3; 12418 -3.6; 13660 -15.1; 15026 -21.5; 16529 -15.3; 18182 -8.7; 20000 -8.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hyla CE-5 sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hyla CE-5 sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 40 Hz    | 0.29 | -4.0 dB  |
| Peaking | 1682 Hz  | 2.85 | -3.0 dB  |
| Peaking | 3054 Hz  | 3.52 | 2.6 dB   |
| Peaking | 12405 Hz | 0.48 | 13.5 dB  |
| Peaking | 14962 Hz | 1.03 | -31.1 dB |
| Peaking | 629 Hz   | 1.4  | 2.2 dB   |
| Peaking | 4566 Hz  | 4.44 | -2.1 dB  |
| Peaking | 6099 Hz  | 3.53 | 2.6 dB   |
| Peaking | 9670 Hz  | 5.06 | -4.3 dB  |
| Peaking | 12288 Hz | 7.08 | 3.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB  |
| Peaking | 62 Hz    | 1.41 | -2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -2.6 dB  |
| Peaking | 250 Hz   | 1.41 | -1.1 dB  |
| Peaking | 500 Hz   | 1.41 | 2.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 16000 Hz | 1.41 | -17.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Hyla%20CE-5%20sample%202/Hyla%20CE-5%20sample%202.png)