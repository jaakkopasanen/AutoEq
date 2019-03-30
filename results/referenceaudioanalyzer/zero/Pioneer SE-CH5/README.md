# Pioneer SE-CH5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.1; 25 -1.6; 28 -2.3; 31 -2.8; 34 -3.3; 37 -3.7; 41 -4.1; 45 -4.5; 49 -4.8; 54 -5.1; 60 -5.4; 66 -5.6; 72 -5.8; 79 -6.0; 87 -6.1; 96 -6.4; 106 -6.4; 116 -6.4; 128 -6.4; 141 -6.4; 155 -6.4; 170 -6.4; 187 -6.4; 206 -6.3; 227 -6.0; 249 -5.6; 274 -5.3; 302 -5.0; 332 -4.5; 365 -3.8; 402 -3.5; 442 -4.0; 486 -4.9; 535 -5.5; 588 -5.7; 647 -5.7; 712 -5.5; 783 -5.3; 861 -5.1; 947 -4.8; 1042 -4.5; 1146 -4.0; 1261 -3.7; 1387 -3.5; 1526 -3.8; 1678 -3.9; 1846 -4.4; 2031 -5.0; 2234 -6.0; 2457 -7.2; 2703 -8.8; 2973 -10.0; 3270 -10.2; 3597 -9.4; 3957 -8.2; 4353 -7.2; 4788 -6.3; 5267 -5.5; 5793 -5.7; 6373 -7.4; 7010 -9.1; 7711 -8.3; 8482 -5.8; 9330 -5.8; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -5.8; 16529 -5.8; 18182 -5.8; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pioneer SE-CH5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer SE-CH5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.42 | 5.2 dB  |
| Peaking | 394 Hz  | 3.89 | 2.4 dB  |
| Peaking | 1502 Hz | 1.37 | 2.6 dB  |
| Peaking | 3139 Hz | 2.34 | -5.2 dB |
| Peaking | 7192 Hz | 5.71 | -3.6 dB |
| Peaking | 201 Hz  | 0.59 | -1.1 dB |
| Peaking | 295 Hz  | 1.51 | 1.2 dB  |
| Peaking | 3987 Hz | 5.45 | -0.5 dB |
| Peaking | 5412 Hz | 6.16 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.8 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | 0.4 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.2 dB |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Pioneer%20SE-CH5/Pioneer%20SE-CH5.png)