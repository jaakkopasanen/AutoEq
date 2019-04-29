# qdc Anole V3 Bass
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.0; 23 -11.2; 25 -11.3; 28 -11.5; 31 -11.6; 34 -11.7; 37 -11.8; 41 -12.0; 45 -12.1; 49 -12.1; 54 -12.2; 60 -12.3; 66 -12.5; 72 -12.7; 79 -13.0; 87 -13.2; 96 -13.5; 106 -13.6; 116 -13.8; 128 -13.9; 141 -14.0; 155 -14.0; 170 -13.9; 187 -13.7; 206 -13.5; 227 -13.2; 249 -12.9; 274 -12.5; 302 -12.0; 332 -11.6; 365 -11.0; 402 -10.5; 442 -9.9; 486 -9.2; 535 -8.5; 588 -7.7; 647 -6.8; 712 -5.9; 783 -4.9; 861 -4.0; 947 -3.3; 1042 -3.0; 1146 -3.1; 1261 -3.3; 1387 -3.2; 1526 -2.7; 1678 -1.9; 1846 -1.2; 2031 -0.9; 2234 -1.0; 2457 -1.5; 2703 -2.0; 2973 -1.9; 3270 -1.4; 3597 -0.6; 3957 -0.5; 4353 -0.8; 4788 -0.5; 5267 -0.5; 5793 -2.3; 6373 -4.6; 7010 -4.6; 7711 -6.2; 8482 -6.7; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc Anole V3 Bass GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc Anole V3 Bass ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.69 | -1.8 dB |
| Peaking | 52 Hz   | 0.28 | -3.0 dB |
| Peaking | 212 Hz  | 0.38 | -6.0 dB |
| Peaking | 1580 Hz | 0.46 | 5.3 dB  |
| Peaking | 4548 Hz | 1.83 | 4.4 dB  |
| Peaking | 968 Hz  | 2.76 | 1.3 dB  |
| Peaking | 1379 Hz | 1.78 | -1.5 dB |
| Peaking | 2013 Hz | 2.73 | 1.3 dB  |
| Peaking | 5445 Hz | 8.38 | 1.7 dB  |
| Peaking | 8429 Hz | 1.48 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.9 dB |
| Peaking | 62 Hz    | 1.41 | -4.2 dB |
| Peaking | 125 Hz   | 1.41 | -6.2 dB |
| Peaking | 250 Hz   | 1.41 | -5.6 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/qdc%20Anole%20V3%20Bass/qdc%20Anole%20V3%20Bass.png)