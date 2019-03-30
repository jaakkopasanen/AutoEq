# Venture Electronics Monk Plus
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.8; 72 -2.1; 79 -3.5; 87 -4.9; 96 -6.3; 106 -7.4; 116 -8.3; 128 -8.8; 141 -9.0; 155 -8.9; 170 -8.6; 187 -8.2; 206 -7.8; 227 -7.3; 249 -6.9; 274 -6.4; 302 -6.0; 332 -5.7; 365 -5.7; 402 -5.8; 442 -5.7; 486 -5.4; 535 -4.9; 588 -4.0; 647 -3.1; 712 -2.8; 783 -2.9; 861 -3.4; 947 -4.0; 1042 -4.8; 1146 -5.9; 1261 -7.5; 1387 -9.5; 1526 -11.6; 1678 -13.5; 1846 -15.2; 2031 -16.0; 2234 -15.3; 2457 -12.9; 2703 -9.9; 2973 -7.1; 3270 -5.1; 3597 -3.9; 3957 -3.6; 4353 -4.4; 4788 -5.7; 5267 -5.8; 5793 -4.8; 6373 -4.5; 7010 -4.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Venture Electronics Monk Plus GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Venture Electronics Monk Plus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 52 Hz   | 0.34 | 8.1 dB   |
| Peaking | 129 Hz  | 0.88 | -8.0 dB  |
| Peaking | 864 Hz  | 1.03 | 5.7 dB   |
| Peaking | 2088 Hz | 1.16 | -14.4 dB |
| Peaking | 3399 Hz | 1.04 | 7.6 dB   |
| Peaking | 41 Hz   | 2.25 | -0.7 dB  |
| Peaking | 65 Hz   | 5.06 | 1.1 dB   |
| Peaking | 3952 Hz | 1.7  | 1.7 dB   |
| Peaking | 5401 Hz | 1.19 | -3.4 dB  |
| Peaking | 6373 Hz | 2.64 | 3.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB   |
| Peaking | 62 Hz    | 1.41 | 5.6 dB   |
| Peaking | 125 Hz   | 1.41 | -3.8 dB  |
| Peaking | 250 Hz   | 1.41 | -0.5 dB  |
| Peaking | 500 Hz   | 1.41 | 1.8 dB   |
| Peaking | 1000 Hz  | 1.41 | 4.6 dB   |
| Peaking | 2000 Hz  | 1.41 | -11.5 dB |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 16000 Hz | 1.41 | -0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Venture%20Electronics%20Monk%20Plus/Venture%20Electronics%20Monk%20Plus.png)