# Moondrop Blessing
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.0; 23 -4.6; 25 -4.7; 28 -4.6; 31 -4.5; 34 -4.6; 37 -4.5; 41 -4.5; 45 -4.3; 49 -4.3; 54 -4.4; 60 -4.4; 66 -4.6; 72 -4.5; 79 -4.7; 87 -4.6; 96 -4.2; 106 -4.5; 116 -4.2; 128 -4.4; 141 -4.2; 155 -4.1; 170 -4.1; 187 -4.2; 206 -4.1; 227 -4.1; 249 -4.0; 274 -3.9; 302 -3.8; 332 -3.8; 365 -3.6; 402 -3.5; 442 -3.5; 486 -3.3; 535 -3.2; 588 -3.1; 647 -2.9; 712 -2.6; 783 -2.3; 861 -2.2; 947 -2.2; 1042 -2.7; 1146 -3.5; 1261 -4.3; 1387 -4.9; 1526 -5.0; 1678 -4.8; 1846 -4.6; 2031 -4.7; 2234 -5.1; 2457 -5.7; 2703 -6.1; 2973 -5.9; 3270 -5.1; 3597 -4.4; 3957 -4.2; 4353 -4.1; 4788 -3.9; 5267 -3.7; 5793 -2.7; 6373 -0.5; 7010 -2.9; 7711 -6.5; 8482 -5.4; 9330 -3.9; 10263 -3.9; 11289 -3.9; 12418 -3.9; 13660 -3.9; 15026 -6.4; 16529 -8.4; 18182 -9.1; 20000 -13.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Moondrop Blessing GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Moondrop Blessing ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 916 Hz   | 1.34 | 2.2 dB  |
| Peaking | 1390 Hz  | 2.09 | -1.8 dB |
| Peaking | 2721 Hz  | 2.7  | -2.3 dB |
| Peaking | 6359 Hz  | 7.94 | 4.2 dB  |
| Peaking | 19913 Hz | 0.54 | -8.2 dB |
| Peaking | 49 Hz    | 0.38 | -0.6 dB |
| Peaking | 6883 Hz  | 7.82 | 1.3 dB  |
| Peaking | 7840 Hz  | 5.28 | -3.5 dB |
| Peaking | 14818 Hz | 0.87 | 2.5 dB  |
| Peaking | 15747 Hz | 1.88 | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.6 dB |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | -0.0 dB |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -4.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Moondrop%20Blessing/Moondrop%20Blessing.png)