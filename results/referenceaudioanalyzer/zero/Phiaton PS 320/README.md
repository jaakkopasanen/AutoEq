# Phiaton PS 320
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.5; 23 -2.6; 25 -2.6; 28 -2.7; 31 -2.8; 34 -3.0; 37 -3.1; 41 -3.3; 45 -3.5; 49 -3.6; 54 -3.5; 60 -3.4; 66 -3.7; 72 -4.1; 79 -4.7; 87 -5.0; 96 -5.4; 106 -5.9; 116 -6.3; 128 -6.4; 141 -6.3; 155 -5.8; 170 -4.8; 187 -3.4; 206 -2.9; 227 -4.1; 249 -5.5; 274 -6.7; 302 -7.3; 332 -7.1; 365 -6.2; 402 -5.0; 442 -3.7; 486 -2.4; 535 -1.2; 588 -0.5; 647 -0.5; 712 -1.0; 783 -1.9; 861 -2.9; 947 -3.9; 1042 -4.8; 1146 -5.4; 1261 -5.7; 1387 -6.1; 1526 -6.6; 1678 -6.9; 1846 -7.2; 2031 -8.0; 2234 -8.7; 2457 -8.2; 2703 -6.5; 2973 -4.7; 3270 -3.1; 3597 -2.1; 3957 -2.6; 4353 -3.2; 4788 -3.4; 5267 -4.1; 5793 -7.7; 6373 -10.7; 7010 -10.0; 7711 -7.3; 8482 -6.3; 9330 -7.3; 10263 -7.3; 11289 -5.4; 12418 -5.2; 13660 -5.2; 15026 -5.2; 16529 -5.2; 18182 -5.2; 20000 -5.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton PS 320 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton PS 320 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.88 | 2.7 dB  |
| Peaking | 645 Hz  | 2.27 | 5.4 dB  |
| Peaking | 2365 Hz | 1.33 | -6.0 dB |
| Peaking | 3612 Hz | 1.12 | 5.8 dB  |
| Peaking | 6614 Hz | 2.72 | -6.9 dB |
| Peaking | 133 Hz  | 2.42 | -1.8 dB |
| Peaking | 202 Hz  | 3.3  | 3.2 dB  |
| Peaking | 311 Hz  | 2.25 | -3.0 dB |
| Peaking | 496 Hz  | 4.03 | 1.5 dB  |
| Peaking | 9868 Hz | 6.26 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Phiaton%20PS%20320/Phiaton%20PS%20320.png)