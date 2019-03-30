# Periodic Audio Be
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.0; 23 -5.6; 25 -6.1; 28 -6.8; 31 -7.3; 34 -7.7; 37 -8.1; 41 -8.4; 45 -8.7; 49 -9.0; 54 -9.2; 60 -9.4; 66 -9.5; 72 -9.7; 79 -9.7; 87 -9.7; 96 -9.7; 106 -9.5; 116 -9.4; 128 -9.4; 141 -9.1; 155 -9.0; 170 -8.7; 187 -8.3; 206 -7.9; 227 -7.5; 249 -7.1; 274 -6.8; 302 -6.5; 332 -6.2; 365 -5.7; 402 -5.2; 442 -4.6; 486 -4.1; 535 -3.5; 588 -3.0; 647 -2.5; 712 -2.0; 783 -1.5; 861 -1.1; 947 -0.8; 1042 -0.6; 1146 -0.6; 1261 -0.7; 1387 -1.3; 1526 -2.2; 1678 -3.3; 1846 -4.6; 2031 -5.7; 2234 -6.5; 2457 -7.0; 2703 -6.6; 2973 -5.4; 3270 -3.6; 3597 -1.9; 3957 -1.0; 4353 -0.7; 4788 -0.5; 5267 -0.5; 5793 -1.8; 6373 -5.2; 7010 -7.5; 7711 -6.1; 8482 -4.3; 9330 -4.3; 10263 -4.3; 11289 -4.3; 12418 -4.3; 13660 -4.3; 15026 -4.3; 16529 -4.3; 18182 -4.3; 20000 -4.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Periodic Audio Be GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Periodic Audio Be ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 93 Hz   | 0.34 | -5.5 dB |
| Peaking | 1126 Hz | 0.72 | 4.8 dB  |
| Peaking | 2437 Hz | 1.36 | -6.2 dB |
| Peaking | 4601 Hz | 1.1  | 5.5 dB  |
| Peaking | 6998 Hz | 3.59 | -5.8 dB |
| Peaking | 21 Hz   | 2.07 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.2 dB |
| Peaking | 62 Hz    | 1.41 | -4.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Periodic%20Audio%20Be/Periodic%20Audio%20Be.png)