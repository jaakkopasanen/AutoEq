# Shure SE102
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.7; 23 -4.9; 25 -5.1; 28 -5.3; 31 -5.5; 34 -5.6; 37 -5.7; 41 -5.7; 45 -5.8; 49 -5.8; 54 -5.8; 60 -5.8; 66 -5.8; 72 -5.7; 79 -5.8; 87 -5.8; 96 -5.8; 106 -5.6; 116 -5.4; 128 -5.4; 141 -5.3; 155 -5.1; 170 -5.1; 187 -5.1; 206 -5.3; 227 -5.1; 249 -4.9; 274 -4.6; 302 -4.5; 332 -4.3; 365 -4.0; 402 -3.7; 442 -3.4; 486 -3.2; 535 -3.2; 588 -3.2; 647 -3.2; 712 -2.9; 783 -2.8; 861 -2.8; 947 -3.0; 1042 -3.1; 1146 -3.3; 1261 -3.6; 1387 -4.0; 1526 -4.6; 1678 -5.5; 1846 -7.0; 2031 -9.1; 2234 -11.6; 2457 -13.0; 2703 -12.3; 2973 -9.7; 3270 -7.1; 3597 -5.9; 3957 -6.4; 4353 -9.1; 4788 -11.3; 5267 -10.8; 5793 -6.3; 6373 -0.5; 7010 -2.6; 7711 -4.8; 8482 -5.1; 9330 -5.1; 10263 -5.1; 11289 -5.1; 12418 -5.1; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -5.1; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE102 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE102 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 116 Hz  | 0.29 | -0.8 dB  |
| Peaking | 1265 Hz | 0.26 | 2.9 dB   |
| Peaking | 2439 Hz | 2.17 | -10.6 dB |
| Peaking | 5057 Hz | 3.31 | -8.0 dB  |
| Peaking | 6477 Hz | 5.47 | 6.3 dB   |
| Peaking | 16 Hz   | 1.57 | 0.7 dB   |
| Peaking | 2854 Hz | 6.6  | -1.4 dB  |
| Peaking | 3940 Hz | 2.03 | 1.6 dB   |
| Peaking | 4427 Hz | 6.41 | -2.3 dB  |
| Peaking | 8326 Hz | 2.41 | -0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.1 dB |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.0 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.5 dB |
| Peaking | 4000 Hz  | 1.41 | -3.6 dB |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Shure%20SE102/Shure%20SE102.png)