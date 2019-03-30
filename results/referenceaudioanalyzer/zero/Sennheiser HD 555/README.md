# Sennheiser HD 555
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.1; 31 -1.8; 34 -2.5; 37 -3.0; 41 -3.7; 45 -4.2; 49 -4.6; 54 -4.8; 60 -4.6; 66 -4.6; 72 -5.0; 79 -5.5; 87 -5.7; 96 -6.0; 106 -6.2; 116 -6.4; 128 -6.7; 141 -7.0; 155 -7.1; 170 -7.0; 187 -7.0; 206 -7.0; 227 -7.0; 249 -7.1; 274 -7.1; 302 -7.1; 332 -7.1; 365 -7.1; 402 -7.0; 442 -6.9; 486 -6.8; 535 -6.6; 588 -6.4; 647 -6.1; 712 -6.1; 783 -5.9; 861 -6.1; 947 -6.1; 1042 -6.1; 1146 -6.4; 1261 -6.5; 1387 -6.3; 1526 -5.8; 1678 -5.0; 1846 -4.5; 2031 -4.6; 2234 -5.6; 2457 -7.0; 2703 -7.9; 2973 -7.9; 3270 -7.4; 3597 -6.4; 3957 -5.6; 4353 -5.8; 4788 -6.6; 5267 -6.2; 5793 -4.1; 6373 -2.4; 7010 -4.5; 7711 -8.6; 8482 -10.3; 9330 -9.2; 10263 -7.8; 11289 -7.6; 12418 -6.7; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 555 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 555 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.87 | 6.0 dB  |
| Peaking | 1862 Hz | 4.74 | 2.4 dB  |
| Peaking | 6536 Hz | 3.86 | 6.0 dB  |
| Peaking | 8351 Hz | 2.28 | -4.7 dB |
| Peaking | 69 Hz   | 2.63 | 0.9 dB  |
| Peaking | 265 Hz  | 0.48 | -0.8 dB |
| Peaking | 753 Hz  | 1.46 | 0.8 dB  |
| Peaking | 2896 Hz | 4.36 | -1.9 dB |
| Peaking | 4020 Hz | 7.14 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20HD%20555/Sennheiser%20HD%20555.png)