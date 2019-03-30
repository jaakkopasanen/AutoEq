# Angry Birds Angry Birds
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.5; 23 -16.0; 25 -16.4; 28 -16.8; 31 -17.2; 34 -17.4; 37 -17.6; 41 -17.8; 45 -17.9; 49 -17.9; 54 -17.9; 60 -17.9; 66 -17.9; 72 -17.9; 79 -17.8; 87 -17.6; 96 -17.4; 106 -17.2; 116 -16.9; 128 -16.6; 141 -16.3; 155 -15.9; 170 -15.4; 187 -14.8; 206 -14.0; 227 -13.4; 249 -13.4; 274 -13.5; 302 -12.8; 332 -12.0; 365 -11.1; 402 -10.3; 442 -9.4; 486 -8.6; 535 -7.7; 588 -6.8; 647 -5.9; 712 -5.0; 783 -4.1; 861 -3.3; 947 -2.6; 1042 -2.0; 1146 -1.5; 1261 -1.1; 1387 -0.9; 1526 -0.7; 1678 -0.7; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -1.2; 2973 -2.7; 3270 -4.3; 3597 -5.8; 3957 -6.4; 4353 -6.6; 4788 -7.2; 5267 -7.2; 5793 -5.3; 6373 -1.5; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Angry Birds Angry Birds GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Angry Birds Angry Birds ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.22 | -4.8 dB |
| Peaking | 111 Hz  | 0.2  | -8.8 dB |
| Peaking | 1942 Hz | 0.34 | 8.7 dB  |
| Peaking | 4817 Hz | 0.82 | -7.0 dB |
| Peaking | 6428 Hz | 4.69 | 6.8 dB  |
| Peaking | 227 Hz  | 4.03 | 1.0 dB  |
| Peaking | 279 Hz  | 2.89 | -0.8 dB |
| Peaking | 1801 Hz | 1.66 | -2.0 dB |
| Peaking | 2203 Hz | 0.96 | 1.9 dB  |
| Peaking | 3497 Hz | 3.9  | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.4 dB |
| Peaking | 62 Hz    | 1.41 | -8.8 dB  |
| Peaking | 125 Hz   | 1.41 | -8.0 dB  |
| Peaking | 250 Hz   | 1.41 | -5.7 dB  |
| Peaking | 500 Hz   | 1.41 | -1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.1 dB   |
| Peaking | 2000 Hz  | 1.41 | 6.7 dB   |
| Peaking | 4000 Hz  | 1.41 | -0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Angry%20Birds%20Angry%20Birds/Angry%20Birds%20Angry%20Birds.png)