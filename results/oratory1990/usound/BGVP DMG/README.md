# BGVP DMG
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.7; 23 -6.0; 25 -6.3; 28 -6.7; 31 -7.0; 34 -7.3; 37 -7.5; 41 -7.8; 45 -8.0; 49 -8.2; 54 -8.4; 60 -8.7; 66 -8.9; 72 -9.1; 79 -9.4; 87 -9.6; 96 -9.8; 106 -10.0; 116 -10.2; 128 -10.3; 141 -10.2; 155 -10.1; 170 -9.8; 187 -9.6; 206 -9.3; 227 -9.0; 249 -8.6; 274 -8.1; 302 -7.6; 332 -7.0; 365 -6.4; 402 -5.8; 442 -5.3; 486 -4.7; 535 -4.1; 588 -3.5; 647 -2.9; 712 -2.2; 783 -1.7; 861 -1.1; 947 -0.8; 1042 -0.6; 1146 -0.5; 1261 -0.5; 1387 -0.8; 1526 -1.5; 1678 -2.0; 1846 -2.0; 2031 -1.7; 2234 -1.6; 2457 -2.0; 2703 -2.8; 2973 -4.2; 3270 -2.4; 3597 -1.6; 3957 -4.1; 4353 -5.4; 4788 -6.2; 5267 -7.1; 5793 -9.3; 6373 -7.8; 7010 -6.3; 7711 -8.0; 8482 -9.9; 9330 -9.4; 10263 -8.2; 11289 -7.2; 12418 -5.4; 13660 -5.4; 15026 -5.4; 16529 -5.4; 18182 -5.4; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`BGVP DMG GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BGVP DMG ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 76 Hz    | 0.41 | -1.4 dB |
| Peaking | 166 Hz   | 0.41 | -4.1 dB |
| Peaking | 1113 Hz  | 0.49 | 5.3 dB  |
| Peaking | 3544 Hz  | 6.38 | 3.5 dB  |
| Peaking | 7662 Hz  | 0.85 | -3.8 dB |
| Peaking | 2325 Hz  | 7.26 | 1.0 dB  |
| Peaking | 5987 Hz  | 6.09 | -2.9 dB |
| Peaking | 7132 Hz  | 2.98 | 4.3 dB  |
| Peaking | 8422 Hz  | 1.68 | -2.8 dB |
| Peaking | 12653 Hz | 1.6  | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.1 dB |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/BGVP%20DMG/BGVP%20DMG.png)