# iBasso IT01 sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.8; 23 -8.8; 25 -8.8; 28 -8.8; 31 -8.8; 34 -8.8; 37 -8.7; 41 -8.6; 45 -8.6; 49 -8.5; 54 -8.5; 60 -8.4; 66 -8.4; 72 -8.5; 79 -8.5; 87 -8.6; 96 -8.7; 106 -8.9; 116 -8.9; 128 -9.0; 141 -9.1; 155 -9.1; 170 -9.0; 187 -8.9; 206 -8.8; 227 -8.7; 249 -8.5; 274 -8.3; 302 -8.0; 332 -7.7; 365 -7.5; 402 -7.2; 442 -6.9; 486 -6.6; 535 -6.1; 588 -5.4; 647 -4.6; 712 -3.8; 783 -3.1; 861 -2.5; 947 -2.2; 1042 -2.2; 1146 -2.6; 1261 -3.2; 1387 -3.5; 1526 -3.3; 1678 -2.9; 1846 -2.4; 2031 -2.2; 2234 -2.0; 2457 -1.8; 2703 -1.5; 2973 -1.1; 3270 -0.8; 3597 -0.8; 3957 -1.4; 4353 -2.8; 4788 -4.4; 5267 -3.9; 5793 -1.8; 6373 -0.5; 7010 -2.4; 7711 -6.2; 8482 -4.9; 9330 -4.7; 10263 -4.7; 11289 -4.7; 12418 -4.7; 13660 -4.7; 15026 -4.7; 16529 -6.2; 18182 -5.6; 20000 -4.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`iBasso IT01 sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `iBasso IT01 sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 84 Hz    | 0.09 | -4.2 dB |
| Peaking | 902 Hz   | 1.09 | 4.2 dB  |
| Peaking | 3008 Hz  | 1.27 | 3.9 dB  |
| Peaking | 6515 Hz  | 4.91 | 4.6 dB  |
| Peaking | 7725 Hz  | 4.73 | -2.7 dB |
| Peaking | 63 Hz    | 2.49 | 0.5 dB  |
| Peaking | 1908 Hz  | 7.29 | 0.6 dB  |
| Peaking | 4678 Hz  | 2.25 | 1.6 dB  |
| Peaking | 4848 Hz  | 5.11 | -3.3 dB |
| Peaking | 17357 Hz | 3.22 | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/iBasso%20IT01%20sample%202/iBasso%20IT01%20sample%202.png)