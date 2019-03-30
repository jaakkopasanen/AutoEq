# Sennheiser HD 449
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.1; 23 -6.5; 25 -6.9; 28 -7.3; 31 -7.6; 34 -7.9; 37 -8.1; 41 -8.2; 45 -8.2; 49 -8.4; 54 -8.8; 60 -9.1; 66 -9.1; 72 -9.0; 79 -8.9; 87 -8.3; 96 -7.3; 106 -7.0; 116 -7.2; 128 -7.6; 141 -7.7; 155 -7.7; 170 -7.9; 187 -7.7; 206 -7.2; 227 -6.7; 249 -6.2; 274 -5.9; 302 -5.6; 332 -5.3; 365 -5.0; 402 -4.8; 442 -4.8; 486 -5.0; 535 -5.2; 588 -5.4; 647 -5.8; 712 -6.0; 783 -5.9; 861 -5.5; 947 -5.3; 1042 -5.1; 1146 -5.0; 1261 -5.3; 1387 -5.4; 1526 -5.1; 1678 -4.8; 1846 -4.7; 2031 -4.5; 2234 -4.3; 2457 -4.4; 2703 -5.4; 2973 -6.4; 3270 -6.7; 3597 -6.2; 3957 -4.4; 4353 -0.5; 4788 -1.0; 5267 -4.9; 5793 -7.0; 6373 -8.1; 7010 -7.1; 7711 -5.1; 8482 -5.3; 9330 -5.3; 10263 -5.3; 11289 -5.3; 12418 -5.3; 13660 -5.3; 15026 -5.3; 16529 -5.3; 18182 -5.3; 20000 -5.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 449 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 449 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 57 Hz    | 0.76 | -3.7 dB |
| Peaking | 173 Hz   | 2.38 | -1.9 dB |
| Peaking | 3414 Hz  | 4.77 | -2.1 dB |
| Peaking | 4535 Hz  | 5    | 6.4 dB  |
| Peaking | 6252 Hz  | 4.2  | -3.4 dB |
| Peaking | 417 Hz   | 2.85 | 0.9 dB  |
| Peaking | 713 Hz   | 4.78 | -0.8 dB |
| Peaking | 2168 Hz  | 3.41 | 1.2 dB  |
| Peaking | 22050 Hz | 1.73 | -0.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.8 dB |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20HD%20449/Sennheiser%20HD%20449.png)