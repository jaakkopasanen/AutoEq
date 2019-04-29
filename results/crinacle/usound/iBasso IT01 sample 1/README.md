# iBasso IT01 sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.0; 23 -8.0; 25 -8.0; 28 -7.9; 31 -7.9; 34 -7.8; 37 -7.7; 41 -7.6; 45 -7.5; 49 -7.4; 54 -7.3; 60 -7.2; 66 -7.2; 72 -7.3; 79 -7.3; 87 -7.4; 96 -7.6; 106 -7.7; 116 -7.7; 128 -7.8; 141 -7.8; 155 -7.8; 170 -7.8; 187 -7.6; 206 -7.5; 227 -7.4; 249 -7.2; 274 -7.0; 302 -6.6; 332 -6.3; 365 -6.0; 402 -5.7; 442 -5.4; 486 -5.0; 535 -4.6; 588 -4.1; 647 -3.6; 712 -3.0; 783 -2.3; 861 -1.6; 947 -1.0; 1042 -0.8; 1146 -1.2; 1261 -1.7; 1387 -2.0; 1526 -1.9; 1678 -1.6; 1846 -1.3; 2031 -1.2; 2234 -1.3; 2457 -1.6; 2703 -1.6; 2973 -1.2; 3270 -0.7; 3597 -0.5; 3957 -0.9; 4353 -2.3; 4788 -5.1; 5267 -7.1; 5793 -4.8; 6373 -3.3; 7010 -5.9; 7711 -7.1; 8482 -4.0; 9330 -4.0; 10263 -4.0; 11289 -4.0; 12418 -4.0; 13660 -4.0; 15026 -4.0; 16529 -5.4; 18182 -5.1; 20000 -4.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`iBasso IT01 sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `iBasso IT01 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 13 Hz    | 0.96 | -3.4 dB |
| Peaking | 28 Hz    | 0.78 | -2.3 dB |
| Peaking | 175 Hz   | 0.33 | -3.8 dB |
| Peaking | 1112 Hz  | 0.68 | 3.5 dB  |
| Peaking | 3407 Hz  | 3.41 | 3.2 dB  |
| Peaking | 4341 Hz  | 2.64 | 1.8 dB  |
| Peaking | 5195 Hz  | 4.06 | -5.4 dB |
| Peaking | 6438 Hz  | 2.29 | 2.2 dB  |
| Peaking | 7414 Hz  | 5.77 | -5.1 dB |
| Peaking | 13704 Hz | 0.99 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.1 dB |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/iBasso%20IT01%20sample%201/iBasso%20IT01%20sample%201.png)