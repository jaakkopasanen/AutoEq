# OPPO PM2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -3.8; 25 -3.8; 28 -3.7; 31 -3.5; 34 -3.4; 37 -3.6; 41 -4.3; 45 -4.9; 49 -5.2; 54 -5.2; 60 -5.2; 66 -5.2; 72 -5.3; 79 -5.5; 87 -5.5; 96 -5.4; 106 -5.2; 116 -5.2; 128 -5.2; 141 -5.2; 155 -5.2; 170 -5.2; 187 -5.1; 206 -4.9; 227 -4.9; 249 -4.9; 274 -4.9; 302 -4.7; 332 -4.1; 365 -3.2; 402 -2.9; 442 -3.4; 486 -4.1; 535 -4.7; 588 -5.2; 647 -5.5; 712 -5.6; 783 -5.3; 861 -4.7; 947 -4.0; 1042 -3.6; 1146 -3.3; 1261 -3.3; 1387 -2.8; 1526 -1.9; 1678 -1.1; 1846 -0.5; 2031 -0.5; 2234 -1.1; 2457 -1.8; 2703 -2.5; 2973 -3.1; 3270 -3.3; 3597 -3.3; 3957 -3.0; 4353 -2.7; 4788 -3.1; 5267 -4.5; 5793 -5.9; 6373 -5.6; 7010 -2.5; 7711 -3.1; 8482 -3.4; 9330 -3.4; 10263 -3.4; 11289 -3.4; 12418 -3.4; 13660 -3.4; 15026 -3.4; 16529 -3.4; 18182 -3.4; 20000 -3.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`OPPO PM2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `OPPO PM2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 102 Hz  | 0.49 | -2.1 dB |
| Peaking | 708 Hz  | 2.43 | -2.3 dB |
| Peaking | 1944 Hz | 2.13 | 3.2 dB  |
| Peaking | 6095 Hz | 4.52 | -3.3 dB |
| Peaking | 7209 Hz | 5.8  | 1.7 dB  |
| Peaking | 34 Hz   | 3.43 | 0.7 dB  |
| Peaking | 297 Hz  | 2.25 | -1.1 dB |
| Peaking | 389 Hz  | 2.45 | 1.7 dB  |
| Peaking | 538 Hz  | 3.93 | -0.7 dB |
| Peaking | 1280 Hz | 3.65 | -0.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.1 dB  |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.8 dB |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/OPPO%20PM2/OPPO%20PM2.png)