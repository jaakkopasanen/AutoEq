# Hyla CE-5 sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.7; 23 -5.7; 25 -5.8; 28 -5.8; 31 -5.7; 34 -5.6; 37 -5.6; 41 -5.5; 45 -5.4; 49 -5.3; 54 -5.2; 60 -5.2; 66 -5.1; 72 -5.1; 79 -5.1; 87 -5.0; 96 -5.1; 106 -5.0; 116 -4.9; 128 -4.7; 141 -4.5; 155 -4.3; 170 -4.0; 187 -4.1; 206 -3.8; 227 -3.3; 249 -2.9; 274 -2.5; 302 -2.2; 332 -1.8; 365 -1.5; 402 -1.3; 442 -1.1; 486 -0.9; 535 -0.8; 588 -0.7; 647 -0.6; 712 -0.6; 783 -0.5; 861 -0.6; 947 -0.9; 1042 -1.6; 1146 -2.7; 1261 -3.9; 1387 -4.9; 1526 -5.3; 1678 -5.4; 1846 -5.2; 2031 -5.0; 2234 -4.7; 2457 -4.1; 2703 -3.4; 2973 -2.9; 3270 -2.8; 3597 -3.2; 3957 -4.1; 4353 -4.8; 4788 -4.2; 5267 -2.5; 5793 -1.3; 6373 -1.7; 7010 -1.8; 7711 -2.7; 8482 -3.0; 9330 -4.7; 10263 -3.2; 11289 -3.0; 12418 -3.0; 13660 -5.9; 15026 -4.9; 16529 -3.0; 18182 -3.0; 20000 -3.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hyla CE-5 sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hyla CE-5 sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.09 | -2.6 dB |
| Peaking | 709 Hz   | 0.45 | 3.3 dB  |
| Peaking | 1389 Hz  | 2.66 | -2.3 dB |
| Peaking | 1840 Hz  | 1.38 | -3.2 dB |
| Peaking | 14248 Hz | 5.12 | -4.4 dB |
| Peaking | 3214 Hz  | 3.56 | 0.9 dB  |
| Peaking | 4559 Hz  | 2.47 | -3.4 dB |
| Peaking | 5630 Hz  | 1.91 | 2.8 dB  |
| Peaking | 9369 Hz  | 7.02 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.9 dB |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -0.1 dB |
| Peaking | 500 Hz   | 1.41 | 2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Hyla%20CE-5%20sample%202/Hyla%20CE-5%20sample%202.png)