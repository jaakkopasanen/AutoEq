# Tecsun Wood Headphones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.7; 23 -3.3; 25 -3.9; 28 -4.6; 31 -5.2; 34 -5.6; 37 -5.9; 41 -6.1; 45 -6.3; 49 -6.3; 54 -6.2; 60 -5.8; 66 -5.5; 72 -5.2; 79 -4.8; 87 -4.5; 96 -4.1; 106 -3.7; 116 -3.1; 128 -2.5; 141 -2.4; 155 -3.0; 170 -3.3; 187 -2.8; 206 -2.3; 227 -1.8; 249 -1.5; 274 -1.2; 302 -1.0; 332 -0.8; 365 -0.8; 402 -0.5; 442 -0.5; 486 -0.8; 535 -0.8; 588 -1.0; 647 -1.2; 712 -1.4; 783 -1.5; 861 -1.7; 947 -2.1; 1042 -2.4; 1146 -2.5; 1261 -2.5; 1387 -2.4; 1526 -2.5; 1678 -2.3; 1846 -2.0; 2031 -1.8; 2234 -2.1; 2457 -2.4; 2703 -2.4; 2973 -2.1; 3270 -2.6; 3597 -4.4; 3957 -5.8; 4353 -6.0; 4788 -5.8; 5267 -6.4; 5793 -7.0; 6373 -5.5; 7010 -1.6; 7711 -2.0; 8482 -2.3; 9330 -2.3; 10263 -2.3; 11289 -2.3; 12418 -2.3; 13660 -2.3; 15026 -2.3; 16529 -2.3; 18182 -2.3; 20000 -2.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Tecsun Wood Headphones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Tecsun Wood Headphones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 49 Hz   | 0.82 | -4.1 dB |
| Peaking | 175 Hz  | 5.59 | -1.1 dB |
| Peaking | 402 Hz  | 0.8  | 1.9 dB  |
| Peaking | 5540 Hz | 1.59 | -5.4 dB |
| Peaking | 7293 Hz | 3.33 | 3.5 dB  |
| Peaking | 1176 Hz | 2.58 | -0.6 dB |
| Peaking | 3404 Hz | 1.72 | 1.5 dB  |
| Peaking | 3902 Hz | 4.15 | -2.8 dB |
| Peaking | 4679 Hz | 0.1  | 0.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.6 dB |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | 0.6 dB  |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.7 dB |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Tecsun%20Wood%20Headphones/Tecsun%20Wood%20Headphones.png)