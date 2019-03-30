# Kotion Each G9000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.0; 23 -11.3; 25 -11.6; 28 -12.1; 31 -12.7; 34 -13.4; 37 -14.0; 41 -14.7; 45 -15.4; 49 -16.0; 54 -16.5; 60 -16.6; 66 -16.9; 72 -17.3; 79 -17.6; 87 -17.6; 96 -17.3; 106 -17.2; 116 -17.5; 128 -17.6; 141 -17.4; 155 -17.2; 170 -17.2; 187 -16.9; 206 -16.3; 227 -15.3; 249 -13.9; 274 -12.8; 302 -12.4; 332 -11.8; 365 -10.3; 402 -8.7; 442 -7.9; 486 -7.4; 535 -7.0; 588 -6.7; 647 -6.6; 712 -6.5; 783 -6.0; 861 -5.5; 947 -4.9; 1042 -4.3; 1146 -3.5; 1261 -2.4; 1387 -1.2; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.7; 2973 -0.7; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.5; 4788 -5.5; 5267 -7.0; 5793 -7.1; 6373 -6.0; 7010 -4.8; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kotion Each G9000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kotion Each G9000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 70 Hz   | 0.48 | -9.8 dB |
| Peaking | 189 Hz  | 0.96 | -6.0 dB |
| Peaking | 1818 Hz | 0.95 | 6.4 dB  |
| Peaking | 3560 Hz | 2.78 | 4.5 dB  |
| Peaking | 11 Hz   | 0.48 | -1.3 dB |
| Peaking | 484 Hz  | 4.92 | 0.9 dB  |
| Peaking | 4196 Hz | 7.84 | 2.5 dB  |
| Peaking | 5388 Hz | 2.65 | -2.4 dB |
| Peaking | 6951 Hz | 7.45 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.3 dB |
| Peaking | 62 Hz    | 1.41 | -8.5 dB |
| Peaking | 125 Hz   | 1.41 | -9.4 dB |
| Peaking | 250 Hz   | 1.41 | -6.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Kotion%20Each%20G9000/Kotion%20Each%20G9000.png)