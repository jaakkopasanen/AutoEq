# InEar ProPhile-8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.3; 23 -4.6; 25 -4.8; 28 -5.0; 31 -5.2; 34 -5.4; 37 -5.4; 41 -5.5; 45 -5.6; 49 -5.8; 54 -6.1; 60 -6.4; 66 -6.7; 72 -6.9; 79 -7.2; 87 -7.1; 96 -7.0; 106 -7.2; 116 -7.0; 128 -7.2; 141 -6.9; 155 -6.6; 170 -6.5; 187 -6.3; 206 -5.9; 227 -5.6; 249 -5.2; 274 -4.9; 302 -4.6; 332 -4.3; 365 -4.1; 402 -3.9; 442 -3.7; 486 -3.6; 535 -3.5; 588 -3.4; 647 -3.2; 712 -2.9; 783 -2.6; 861 -2.4; 947 -2.5; 1042 -2.8; 1146 -3.6; 1261 -4.4; 1387 -4.8; 1526 -4.7; 1678 -4.2; 1846 -3.4; 2031 -2.7; 2234 -2.1; 2457 -1.5; 2703 -1.1; 2973 -1.3; 3270 -1.8; 3597 -1.5; 3957 -1.0; 4353 -0.5; 4788 -0.7; 5267 -2.5; 5793 -4.2; 6373 -3.3; 7010 -4.5; 7711 -6.5; 8482 -4.9; 9330 -3.8; 10263 -3.8; 11289 -3.8; 12418 -3.8; 13660 -3.8; 15026 -3.8; 16529 -4.5; 18182 -10.5; 20000 -15.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`InEar ProPhile-8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `InEar ProPhile-8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 76 Hz    | 0.7  | -2.9 dB  |
| Peaking | 158 Hz   | 1.32 | -1.7 dB  |
| Peaking | 2709 Hz  | 2.61 | 2.6 dB   |
| Peaking | 4380 Hz  | 3.07 | 3.3 dB   |
| Peaking | 7776 Hz  | 5.59 | -3.2 dB  |
| Peaking | 29 Hz    | 2.03 | -0.4 dB  |
| Peaking | 963 Hz   | 1.31 | 2.0 dB   |
| Peaking | 1378 Hz  | 1.92 | -2.3 dB  |
| Peaking | 2083 Hz  | 3.62 | 0.6 dB   |
| Peaking | 19589 Hz | 1.3  | -12.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/InEar%20ProPhile-8/InEar%20ProPhile-8.png)