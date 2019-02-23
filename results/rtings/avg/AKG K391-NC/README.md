# AKG K391-NC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.0; 28 -1.3; 31 -1.5; 34 -1.7; 37 -1.8; 41 -1.9; 45 -2.0; 49 -2.0; 54 -2.1; 60 -2.3; 66 -2.5; 72 -2.6; 79 -2.8; 87 -3.0; 96 -3.2; 106 -3.5; 116 -3.8; 128 -4.2; 141 -4.5; 155 -4.8; 170 -5.1; 187 -5.4; 206 -5.8; 227 -6.3; 249 -6.7; 274 -7.1; 302 -7.6; 332 -8.0; 365 -8.4; 402 -8.7; 442 -8.7; 486 -8.5; 535 -8.0; 588 -7.0; 647 -5.6; 712 -4.1; 783 -2.9; 861 -2.4; 947 -2.6; 1042 -2.9; 1146 -3.3; 1261 -3.6; 1387 -3.6; 1526 -3.5; 1678 -3.3; 1846 -3.1; 2031 -2.7; 2234 -1.8; 2457 -0.9; 2703 -1.0; 2973 -2.2; 3270 -4.1; 3597 -6.4; 3957 -8.2; 4353 -8.9; 4788 -6.9; 5267 -3.8; 5793 -1.2; 6373 -0.6; 7010 -2.4; 7711 -4.6; 8482 -8.5; 9330 -11.4; 10263 -8.6; 11289 -4.9; 12418 -4.9; 13660 -4.9; 15026 -4.9; 16529 -4.9; 18182 -4.9; 20000 -4.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K391-NC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K391-NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.17 | 3.9 dB  |
| Peaking | 458 Hz  | 0.79 | -8.6 dB |
| Peaking | 742 Hz  | 0.53 | 5.9 dB  |
| Peaking | 6410 Hz | 5.16 | 5.5 dB  |
| Peaking | 9329 Hz | 4.27 | -7.4 dB |
| Peaking | 1425 Hz | 1.59 | -2.4 dB |
| Peaking | 2630 Hz | 3.56 | 2.6 dB  |
| Peaking | 2754 Hz | 0.41 | 1.8 dB  |
| Peaking | 4150 Hz | 3.03 | -6.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.8 dB  |
| Peaking | 62 Hz    | 1.41 | 2.0 dB  |
| Peaking | 125 Hz   | 1.41 | 1.0 dB  |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | -3.7 dB |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.2 dB |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AKG%20K391-NC/AKG%20K391-NC.png)