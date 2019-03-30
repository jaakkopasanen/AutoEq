# AKG K518 DJ
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -1.0; 54 -1.9; 60 -2.5; 66 -3.0; 72 -3.4; 79 -3.5; 87 -3.3; 96 -3.5; 106 -3.7; 116 -4.4; 128 -5.2; 141 -5.8; 155 -5.9; 170 -5.9; 187 -5.9; 206 -6.0; 227 -6.1; 249 -5.9; 274 -5.9; 302 -5.9; 332 -5.7; 365 -4.8; 402 -3.9; 442 -3.3; 486 -2.9; 535 -3.0; 588 -3.7; 647 -4.4; 712 -4.8; 783 -5.0; 861 -5.4; 947 -5.8; 1042 -6.2; 1146 -6.5; 1261 -6.7; 1387 -7.1; 1526 -7.5; 1678 -7.5; 1846 -7.1; 2031 -6.8; 2234 -6.9; 2457 -7.3; 2703 -7.6; 2973 -7.8; 3270 -7.8; 3597 -7.4; 3957 -6.7; 4353 -6.5; 4788 -8.0; 5267 -10.2; 5793 -11.0; 6373 -10.3; 7010 -10.2; 7711 -10.5; 8482 -10.0; 9330 -9.1; 10263 -8.2; 11289 -7.5; 12418 -7.3; 13660 -7.1; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K518 DJ GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K518 DJ ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.49 | 5.0 dB  |
| Peaking | 50 Hz   | 0.67 | 2.2 dB  |
| Peaking | 517 Hz  | 1.72 | 3.6 dB  |
| Peaking | 1576 Hz | 2.77 | -1.0 dB |
| Peaking | 6975 Hz | 1.2  | -4.3 dB |
| Peaking | 104 Hz  | 2.34 | 2.4 dB  |
| Peaking | 112 Hz  | 1.12 | -1.5 dB |
| Peaking | 3253 Hz | 2.22 | -1.9 dB |
| Peaking | 4413 Hz | 1.6  | 2.8 dB  |
| Peaking | 5388 Hz | 4.17 | -3.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 2.9 dB  |
| Peaking | 125 Hz   | 1.41 | 0.9 dB  |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | 3.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | -0.6 dB |
| Peaking | 8000 Hz  | 1.41 | -4.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20K518%20DJ/AKG%20K518%20DJ.png)