# iBasso IT01
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.3; 23 -8.3; 25 -8.3; 28 -8.2; 31 -8.2; 34 -8.1; 37 -8.1; 41 -8.0; 45 -7.9; 49 -7.8; 54 -7.7; 60 -7.7; 66 -7.7; 72 -7.7; 79 -7.8; 87 -7.9; 96 -8.0; 106 -8.1; 116 -8.2; 128 -8.3; 141 -8.3; 155 -8.3; 170 -8.3; 187 -8.1; 206 -8.0; 227 -7.9; 249 -7.7; 274 -7.5; 302 -7.2; 332 -6.9; 365 -6.6; 402 -6.3; 442 -6.0; 486 -5.6; 535 -5.2; 588 -4.6; 647 -4.0; 712 -3.3; 783 -2.6; 861 -1.9; 947 -1.5; 1042 -1.3; 1146 -1.8; 1261 -2.3; 1387 -2.6; 1526 -2.5; 1678 -2.1; 1846 -1.7; 2031 -1.5; 2234 -1.5; 2457 -1.6; 2703 -1.4; 2973 -1.0; 3270 -0.6; 3597 -0.5; 3957 -1.0; 4353 -2.4; 4788 -4.6; 5267 -5.3; 5793 -3.2; 6373 -1.7; 7010 -4.1; 7711 -6.5; 8482 -4.3; 9330 -4.2; 10263 -4.2; 11289 -4.2; 12418 -4.2; 13660 -4.2; 15026 -4.2; 16529 -5.6; 18182 -5.1; 20000 -4.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`iBasso IT01 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `iBasso IT01 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 13 Hz    | 0.91 | -2.9 dB |
| Peaking | 28 Hz    | 0.79 | -2.2 dB |
| Peaking | 198 Hz   | 0.26 | -4.1 dB |
| Peaking | 966 Hz   | 0.68 | 4.0 dB  |
| Peaking | 3247 Hz  | 1.96 | 3.3 dB  |
| Peaking | 4060 Hz  | 5.32 | 1.3 dB  |
| Peaking | 5135 Hz  | 4.09 | -3.1 dB |
| Peaking | 6400 Hz  | 3.26 | 3.3 dB  |
| Peaking | 7481 Hz  | 5.62 | -3.8 dB |
| Peaking | 17245 Hz | 3    | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.2 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/iBasso%20IT01/iBasso%20IT01.png)