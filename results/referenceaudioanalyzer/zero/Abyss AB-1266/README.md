# Abyss AB-1266
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.8; 23 -6.7; 25 -6.6; 28 -6.5; 31 -6.3; 34 -6.2; 37 -6.1; 41 -5.9; 45 -5.8; 49 -5.7; 54 -5.7; 60 -5.8; 66 -5.7; 72 -5.5; 79 -5.4; 87 -5.4; 96 -5.4; 106 -5.4; 116 -5.4; 128 -5.4; 141 -5.5; 155 -5.8; 170 -6.2; 187 -5.9; 206 -5.0; 227 -4.4; 249 -4.7; 274 -4.8; 302 -5.0; 332 -5.3; 365 -5.5; 402 -5.7; 442 -6.1; 486 -6.1; 535 -6.1; 588 -6.1; 647 -6.5; 712 -7.5; 783 -8.8; 861 -10.2; 947 -11.3; 1042 -11.9; 1146 -11.5; 1261 -10.3; 1387 -8.4; 1526 -6.1; 1678 -3.7; 1846 -2.0; 2031 -1.3; 2234 -1.0; 2457 -1.1; 2703 -2.2; 2973 -2.8; 3270 -2.0; 3597 -0.5; 3957 -0.5; 4353 -4.2; 4788 -6.2; 5267 -4.0; 5793 -4.3; 6373 -9.2; 7010 -8.8; 7711 -6.0; 8482 -5.5; 9330 -5.5; 10263 -5.6; 11289 -7.1; 12418 -8.6; 13660 -8.8; 15026 -7.9; 16529 -7.3; 18182 -7.3; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Abyss AB-1266 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Abyss AB-1266 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 1095 Hz  | 1.69 | -7.9 dB |
| Peaking | 2104 Hz  | 1.42 | 5.8 dB  |
| Peaking | 3753 Hz  | 5    | 4.8 dB  |
| Peaking | 6671 Hz  | 7.41 | -4.7 dB |
| Peaking | 14133 Hz | 1.28 | -3.3 dB |
| Peaking | 21 Hz    | 1.1  | -1.2 dB |
| Peaking | 257 Hz   | 2.75 | 1.2 dB  |
| Peaking | 10596 Hz | 1.71 | 1.2 dB  |
| Peaking | 12080 Hz | 4.03 | -1.6 dB |
| Peaking | 18802 Hz | 1.53 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.0 dB |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | 0.7 dB  |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -7.8 dB |
| Peaking | 2000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | -3.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Abyss%20AB-1266/Abyss%20AB-1266.png)