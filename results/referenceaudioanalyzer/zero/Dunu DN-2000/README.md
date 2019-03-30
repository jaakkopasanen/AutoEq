# Dunu DN-2000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.2; 23 -11.0; 25 -10.8; 28 -10.5; 31 -10.3; 34 -10.0; 37 -9.8; 41 -9.5; 45 -9.2; 49 -8.9; 54 -8.6; 60 -8.2; 66 -7.8; 72 -7.5; 79 -7.2; 87 -7.1; 96 -7.1; 106 -7.0; 116 -6.8; 128 -6.6; 141 -6.4; 155 -6.1; 170 -5.9; 187 -5.8; 206 -5.7; 227 -5.5; 249 -5.5; 274 -5.5; 302 -5.3; 332 -5.1; 365 -5.1; 402 -5.1; 442 -5.1; 486 -5.1; 535 -5.1; 588 -4.8; 647 -4.8; 712 -4.8; 783 -4.8; 861 -4.8; 947 -4.7; 1042 -4.5; 1146 -4.3; 1261 -3.9; 1387 -3.6; 1526 -3.1; 1678 -2.6; 1846 -1.9; 2031 -1.0; 2234 -1.1; 2457 -2.2; 2703 -3.3; 2973 -4.0; 3270 -4.2; 3597 -4.1; 3957 -4.6; 4353 -6.1; 4788 -6.8; 5267 -5.7; 5793 -3.1; 6373 -0.5; 7010 -1.6; 7711 -3.8; 8482 -4.1; 9330 -4.1; 10263 -4.1; 11289 -4.1; 12418 -4.1; 13660 -4.1; 15026 -4.1; 16529 -4.1; 18182 -4.1; 20000 -4.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dunu DN-2000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu DN-2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.24 | -7.1 dB |
| Peaking | 223 Hz  | 0.23 | -1.0 dB |
| Peaking | 2067 Hz | 2.37 | 3.5 dB  |
| Peaking | 4796 Hz | 3.41 | -3.3 dB |
| Peaking | 6491 Hz | 5.12 | 4.8 dB  |
| Peaking | 104 Hz  | 0.91 | 0.9 dB  |
| Peaking | 115 Hz  | 1.53 | -1.1 dB |
| Peaking | 3064 Hz | 3.96 | -1.1 dB |
| Peaking | 3094 Hz | 2.06 | 0.6 dB  |
| Peaking | 8004 Hz | 5.65 | -0.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.0 dB |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.9 dB |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Dunu%20DN-2000/Dunu%20DN-2000.png)