# Beyerdynamic Custom Street
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.0; 25 -6.0; 28 -6.2; 31 -6.3; 34 -6.5; 37 -6.6; 41 -6.7; 45 -6.6; 49 -6.5; 54 -6.6; 60 -6.8; 66 -6.7; 72 -6.4; 79 -5.7; 87 -4.9; 96 -4.6; 106 -5.2; 116 -5.7; 128 -5.8; 141 -5.8; 155 -6.0; 170 -5.8; 187 -5.1; 206 -4.1; 227 -3.2; 249 -2.3; 274 -1.9; 302 -1.9; 332 -2.1; 365 -2.3; 402 -2.6; 442 -2.9; 486 -3.1; 535 -3.4; 588 -3.8; 647 -4.2; 712 -4.7; 783 -5.0; 861 -5.4; 947 -5.8; 1042 -6.0; 1146 -6.6; 1261 -6.8; 1387 -6.8; 1526 -6.8; 1678 -7.1; 1846 -7.4; 2031 -7.6; 2234 -7.8; 2457 -7.8; 2703 -7.8; 2973 -7.1; 3270 -5.1; 3597 -1.5; 3957 -0.5; 4353 -6.9; 4788 -11.3; 5267 -12.3; 5793 -11.3; 6373 -8.6; 7010 -4.5; 7711 -4.8; 8482 -5.1; 9330 -5.1; 10263 -5.1; 11289 -5.1; 12418 -5.1; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -5.1; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic Custom Street GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic Custom Street ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 59 Hz   | 0.15 | -1.3 dB |
| Peaking | 329 Hz  | 1.01 | 4.2 dB  |
| Peaking | 2211 Hz | 0.83 | -2.9 dB |
| Peaking | 3796 Hz | 4.94 | 8.8 dB  |
| Peaking | 5156 Hz | 3.15 | -8.1 dB |
| Peaking | 95 Hz   | 2.2  | 3.0 dB  |
| Peaking | 107 Hz  | 0.7  | -1.7 dB |
| Peaking | 248 Hz  | 3.72 | 1.2 dB  |
| Peaking | 6220 Hz | 5.25 | -3.0 dB |
| Peaking | 7034 Hz | 3.26 | 3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.4 dB |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | 2.5 dB  |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | -0.6 dB |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20Custom%20Street/Beyerdynamic%20Custom%20Street.png)