# Moondrop Blessing
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.3; 23 -2.4; 25 -2.6; 28 -2.7; 31 -2.8; 34 -2.8; 37 -2.9; 41 -2.9; 45 -2.8; 49 -2.8; 54 -2.7; 60 -2.8; 66 -2.8; 72 -2.9; 79 -3.0; 87 -3.1; 96 -3.3; 106 -3.5; 116 -3.6; 128 -3.7; 141 -3.8; 155 -3.9; 170 -4.0; 187 -4.0; 206 -3.9; 227 -3.9; 249 -3.8; 274 -3.7; 302 -3.7; 332 -3.6; 365 -3.5; 402 -3.4; 442 -3.3; 486 -3.2; 535 -3.0; 588 -2.9; 647 -2.7; 712 -2.5; 783 -2.2; 861 -2.0; 947 -2.1; 1042 -2.5; 1146 -3.4; 1261 -4.2; 1387 -4.7; 1526 -4.8; 1678 -4.6; 1846 -4.5; 2031 -4.6; 2234 -5.0; 2457 -5.6; 2703 -5.9; 2973 -5.6; 3270 -4.8; 3597 -4.2; 3957 -4.0; 4353 -3.9; 4788 -3.7; 5267 -3.5; 5793 -2.2; 6373 -0.5; 7010 -3.0; 7711 -6.0; 8482 -4.9; 9330 -3.7; 10263 -3.7; 11289 -3.7; 12418 -3.7; 13660 -3.7; 15026 -6.1; 16529 -8.3; 18182 -9.1; 20000 -11.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Moondrop Blessing GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Moondrop Blessing ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.52 | 1.1 dB  |
| Peaking | 834 Hz   | 1.92 | 2.0 dB  |
| Peaking | 2415 Hz  | 1.08 | -1.8 dB |
| Peaking | 6311 Hz  | 6.74 | 3.9 dB  |
| Peaking | 19527 Hz | 0.62 | -7.5 dB |
| Peaking | 1393 Hz  | 6.62 | -0.9 dB |
| Peaking | 7862 Hz  | 4.99 | -3.7 dB |
| Peaking | 8201 Hz  | 1.06 | 1.1 dB  |
| Peaking | 13725 Hz | 2.31 | 1.7 dB  |
| Peaking | 15850 Hz | 2.24 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | -0.0 dB |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -4.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Moondrop%20Blessing/Moondrop%20Blessing.png)