# Phiaton MS 400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.6; 23 -0.9; 25 -1.3; 28 -2.2; 31 -2.9; 34 -3.5; 37 -4.0; 41 -4.4; 45 -4.7; 49 -4.9; 54 -5.3; 60 -5.6; 66 -5.8; 72 -6.0; 79 -6.2; 87 -6.3; 96 -6.6; 106 -6.8; 116 -7.0; 128 -7.2; 141 -7.3; 155 -7.3; 170 -7.5; 187 -7.3; 206 -7.0; 227 -6.4; 249 -5.8; 274 -5.8; 302 -6.0; 332 -6.0; 365 -5.9; 402 -5.7; 442 -5.9; 486 -6.1; 535 -6.5; 588 -6.8; 647 -7.2; 712 -7.6; 783 -7.9; 861 -8.4; 947 -9.0; 1042 -9.7; 1146 -10.3; 1261 -10.8; 1387 -11.3; 1526 -11.6; 1678 -12.0; 1846 -12.2; 2031 -11.6; 2234 -10.4; 2457 -8.9; 2703 -7.5; 2973 -6.1; 3270 -4.7; 3597 -3.3; 3957 -1.4; 4353 -0.5; 4788 -0.5; 5267 -4.9; 5793 -8.3; 6373 -7.5; 7010 -4.4; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton MS 400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton MS 400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 21 Hz   |  0.89 | 6.0 dB  |
| Peaking | 143 Hz  |  2.45 | -1.1 dB |
| Peaking | 1720 Hz |  1.09 | -6.4 dB |
| Peaking | 4483 Hz |  1.63 | 8.2 dB  |
| Peaking | 5757 Hz |  4.49 | -6.2 dB |
| Peaking | 186 Hz  |  4.04 | -0.9 dB |
| Peaking | 363 Hz  |  1    | 1.0 dB  |
| Peaking | 1006 Hz |  3.11 | -0.8 dB |
| Peaking | 7028 Hz | 12.68 | 2.0 dB  |
| Peaking | 8342 Hz |  1.75 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.5 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | 0.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.6 dB |
| Peaking | 2000 Hz  | 1.41 | -6.4 dB |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Phiaton%20MS%20400/Phiaton%20MS%20400.png)