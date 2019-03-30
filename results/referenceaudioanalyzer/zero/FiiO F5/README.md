# FiiO F5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.4; 23 -6.4; 25 -6.4; 28 -6.4; 31 -6.4; 34 -6.4; 37 -6.4; 41 -6.4; 45 -6.4; 49 -6.4; 54 -6.4; 60 -6.4; 66 -6.3; 72 -6.1; 79 -6.0; 87 -6.0; 96 -6.0; 106 -5.9; 116 -5.7; 128 -5.7; 141 -5.5; 155 -5.4; 170 -5.1; 187 -5.0; 206 -4.7; 227 -4.5; 249 -4.2; 274 -4.0; 302 -3.8; 332 -3.5; 365 -3.3; 402 -3.0; 442 -2.6; 486 -2.2; 535 -1.9; 588 -1.6; 647 -1.3; 712 -1.1; 783 -0.8; 861 -0.7; 947 -0.5; 1042 -0.5; 1146 -0.6; 1261 -0.9; 1387 -1.2; 1526 -1.8; 1678 -2.6; 1846 -3.8; 2031 -5.5; 2234 -7.4; 2457 -8.9; 2703 -8.6; 2973 -6.9; 3270 -4.9; 3597 -3.5; 3957 -3.3; 4353 -4.7; 4788 -6.7; 5267 -7.9; 5793 -6.9; 6373 -3.5; 7010 -0.7; 7711 -2.8; 8482 -3.0; 9330 -3.1; 10263 -3.1; 11289 -3.1; 12418 -3.1; 13660 -3.1; 15026 -3.1; 16529 -3.1; 18182 -3.1; 20000 -3.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FiiO F5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FiiO F5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.11 | -3.3 dB |
| Peaking | 1675 Hz  | 0.33 | 3.8 dB  |
| Peaking | 2476 Hz  | 1.89 | -9.4 dB |
| Peaking | 5409 Hz  | 2.71 | -6.5 dB |
| Peaking | 6838 Hz  | 6.48 | 3.8 dB  |
| Peaking | 2893 Hz  | 8.12 | -0.7 dB |
| Peaking | 3729 Hz  | 6.61 | 1.0 dB  |
| Peaking | 10185 Hz | 1.12 | -0.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.4 dB |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | -2.6 dB |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/FiiO%20F5/FiiO%20F5.png)