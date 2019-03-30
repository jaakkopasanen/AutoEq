# Shure SRH1540
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.5; 23 -10.9; 25 -11.3; 28 -11.8; 31 -12.2; 34 -12.6; 37 -12.9; 41 -13.1; 45 -13.3; 49 -13.4; 54 -13.3; 60 -13.0; 66 -12.6; 72 -12.2; 79 -11.9; 87 -11.7; 96 -11.5; 106 -11.5; 116 -11.1; 128 -10.7; 141 -9.9; 155 -8.7; 170 -7.4; 187 -5.9; 206 -4.8; 227 -4.1; 249 -3.9; 274 -3.8; 302 -4.1; 332 -4.5; 365 -4.8; 402 -4.5; 442 -4.1; 486 -3.5; 535 -3.0; 588 -2.5; 647 -2.2; 712 -1.9; 783 -1.8; 861 -1.6; 947 -1.4; 1042 -1.2; 1146 -1.1; 1261 -0.8; 1387 -0.6; 1526 -0.5; 1678 -0.9; 1846 -1.7; 2031 -2.4; 2234 -3.3; 2457 -4.9; 2703 -6.9; 2973 -8.4; 3270 -9.2; 3597 -9.0; 3957 -8.4; 4353 -8.3; 4788 -8.3; 5267 -8.4; 5793 -8.8; 6373 -9.1; 7010 -7.5; 7711 -4.6; 8482 -4.8; 9330 -4.8; 10263 -4.8; 11289 -4.8; 12418 -4.8; 13660 -4.8; 15026 -4.8; 16529 -4.8; 18182 -4.8; 20000 -4.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH1540 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH1540 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 43 Hz   | 0.59 | -8.8 dB  |
| Peaking | 114 Hz  | 1.89 | -3.7 dB  |
| Peaking | 2130 Hz | 0.37 | 6.7 dB   |
| Peaking | 3323 Hz | 1.14 | -10.0 dB |
| Peaking | 5996 Hz | 2.31 | -4.9 dB  |
| Peaking | 76 Hz   | 2.82 | -0.8 dB  |
| Peaking | 155 Hz  | 2.48 | -2.4 dB  |
| Peaking | 216 Hz  | 0.9  | 2.5 dB   |
| Peaking | 378 Hz  | 1.78 | -1.7 dB  |
| Peaking | 3705 Hz | 6.25 | 0.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.5 dB |
| Peaking | 62 Hz    | 1.41 | -6.6 dB |
| Peaking | 125 Hz   | 1.41 | -5.1 dB |
| Peaking | 250 Hz   | 1.41 | 1.9 dB  |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 4000 Hz  | 1.41 | -5.9 dB |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Shure%20SRH1540/Shure%20SRH1540.png)