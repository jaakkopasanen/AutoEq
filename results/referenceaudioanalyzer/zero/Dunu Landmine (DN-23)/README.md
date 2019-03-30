# Dunu Landmine (DN-23)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.7; 23 -9.8; 25 -9.9; 28 -9.9; 31 -9.9; 34 -9.8; 37 -9.7; 41 -9.6; 45 -9.6; 49 -9.5; 54 -9.3; 60 -9.1; 66 -8.9; 72 -8.7; 79 -8.5; 87 -8.2; 96 -7.9; 106 -7.6; 116 -7.2; 128 -6.8; 141 -6.4; 155 -6.3; 170 -6.1; 187 -5.7; 206 -5.4; 227 -5.0; 249 -4.6; 274 -4.3; 302 -4.0; 332 -3.7; 365 -3.4; 402 -3.1; 442 -3.0; 486 -2.8; 535 -2.7; 588 -2.4; 647 -2.4; 712 -2.3; 783 -2.1; 861 -2.1; 947 -2.1; 1042 -2.1; 1146 -1.8; 1261 -1.8; 1387 -1.6; 1526 -1.2; 1678 -0.9; 1846 -0.8; 2031 -0.8; 2234 -0.6; 2457 -0.5; 2703 -0.8; 2973 -1.0; 3270 -0.9; 3597 -0.5; 3957 -0.8; 4353 -2.3; 4788 -3.9; 5267 -4.9; 5793 -4.9; 6373 -3.4; 7010 -0.5; 7711 -1.9; 8482 -2.2; 9330 -2.2; 10263 -2.2; 11289 -2.2; 12418 -2.2; 13660 -2.2; 15026 -2.2; 16529 -2.2; 18182 -2.2; 20000 -2.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dunu Landmine (DN-23) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu Landmine (DN-23) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.3dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.15 | -7.6 dB |
| Peaking | 3287 Hz | 0.61 | 2.2 dB  |
| Peaking | 5532 Hz | 2.14 | -4.7 dB |
| Peaking | 7052 Hz | 7.11 | 2.7 dB  |
| Peaking | 534 Hz  | 2.15 | 0.1 dB  |
| Peaking | 3084 Hz | 3.97 | -1.0 dB |
| Peaking | 3799 Hz | 2.08 | 1.0 dB  |
| Peaking | 4634 Hz | 5.38 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.0 dB |
| Peaking | 62 Hz    | 1.41 | -5.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.2 dB |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Dunu%20Landmine%20(DN-23)/Dunu%20Landmine%20(DN-23).png)