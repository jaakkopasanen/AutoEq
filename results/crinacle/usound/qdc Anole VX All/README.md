# qdc Anole VX All
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.3; 23 -8.6; 25 -8.9; 28 -9.2; 31 -9.4; 34 -9.6; 37 -9.7; 41 -9.9; 45 -10.1; 49 -10.2; 54 -10.4; 60 -10.5; 66 -10.7; 72 -10.8; 79 -11.0; 87 -11.1; 96 -11.3; 106 -11.4; 116 -11.4; 128 -11.4; 141 -11.3; 155 -11.1; 170 -10.8; 187 -10.5; 206 -10.2; 227 -9.7; 249 -9.3; 274 -8.8; 302 -8.3; 332 -7.8; 365 -7.3; 402 -6.9; 442 -6.5; 486 -6.1; 535 -5.9; 588 -5.9; 647 -5.9; 712 -6.1; 783 -6.4; 861 -7.0; 947 -7.6; 1042 -8.3; 1146 -8.9; 1261 -9.1; 1387 -8.8; 1526 -7.9; 1678 -6.8; 1846 -5.8; 2031 -5.1; 2234 -4.5; 2457 -3.8; 2703 -3.1; 2973 -2.9; 3270 -2.3; 3597 -2.3; 3957 -3.3; 4353 -4.7; 4788 -1.7; 5267 -0.5; 5793 -0.6; 6373 -5.7; 7010 -9.0; 7711 -7.8; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.9; 15026 -8.6; 16529 -8.1; 18182 -6.9; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc Anole VX All GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc Anole VX All ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 57 Hz    | 0.48 | -3.6 dB |
| Peaking | 152 Hz   | 1.01 | -3.2 dB |
| Peaking | 1267 Hz  | 2.88 | -3.3 dB |
| Peaking | 3085 Hz  | 1.64 | 4.2 dB  |
| Peaking | 5346 Hz  | 5.21 | 6.2 dB  |
| Peaking | 253 Hz   | 2.98 | -0.6 dB |
| Peaking | 548 Hz   | 2.05 | 1.2 dB  |
| Peaking | 5991 Hz  | 9.69 | 2.7 dB  |
| Peaking | 7126 Hz  | 5.38 | -3.8 dB |
| Peaking | 15336 Hz | 1.93 | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.5 dB |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.4 dB |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -2.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/qdc%20Anole%20VX%20All/qdc%20Anole%20VX%20All.png)