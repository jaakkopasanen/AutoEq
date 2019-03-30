# AKG K80
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.9; 128 -1.5; 141 -2.1; 155 -2.4; 170 -2.8; 187 -3.0; 206 -3.3; 227 -3.5; 249 -3.7; 274 -3.8; 302 -4.0; 332 -4.1; 365 -4.3; 402 -4.5; 442 -4.7; 486 -4.9; 535 -5.1; 588 -5.4; 647 -5.6; 712 -5.9; 783 -6.3; 861 -6.7; 947 -7.1; 1042 -7.7; 1146 -8.6; 1261 -9.6; 1387 -10.7; 1526 -11.9; 1678 -12.9; 1846 -13.4; 2031 -12.8; 2234 -9.9; 2457 -4.6; 2703 -2.5; 2973 -4.5; 3270 -9.4; 3597 -14.5; 3957 -15.7; 4353 -13.9; 4788 -11.2; 5267 -9.5; 5793 -7.6; 6373 -6.9; 7010 -6.7; 7711 -6.3; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K80 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K80 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 51 Hz   | 0.19 | 5.9 dB   |
| Peaking | 1878 Hz | 1.61 | -8.7 dB  |
| Peaking | 2706 Hz | 2.93 | 10.2 dB  |
| Peaking | 3886 Hz | 2.72 | -10.6 dB |
| Peaking | 17 Hz   | 1.07 | 1.0 dB   |
| Peaking | 105 Hz  | 2.13 | 1.0 dB   |
| Peaking | 164 Hz  | 1.19 | -0.9 dB  |
| Peaking | 533 Hz  | 1.32 | 0.6 dB   |
| Peaking | 7296 Hz | 2.6  | 0.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 4.7 dB  |
| Peaking | 125 Hz   | 1.41 | 4.2 dB  |
| Peaking | 250 Hz   | 1.41 | 1.7 dB  |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | -5.2 dB |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20K80/AKG%20K80.png)