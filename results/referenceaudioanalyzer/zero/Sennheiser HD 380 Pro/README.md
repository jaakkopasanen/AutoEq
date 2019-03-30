# Sennheiser HD 380 Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.4; 23 -3.8; 25 -4.3; 28 -4.9; 31 -5.4; 34 -5.8; 37 -6.2; 41 -6.5; 45 -6.8; 49 -7.0; 54 -7.4; 60 -7.7; 66 -7.6; 72 -7.2; 79 -6.5; 87 -5.8; 96 -5.8; 106 -6.3; 116 -6.6; 128 -6.6; 141 -6.1; 155 -5.5; 170 -5.1; 187 -4.3; 206 -3.2; 227 -2.4; 249 -1.8; 274 -1.0; 302 -0.5; 332 -0.7; 365 -1.3; 402 -2.0; 442 -2.6; 486 -3.0; 535 -3.1; 588 -3.1; 647 -2.9; 712 -3.0; 783 -3.4; 861 -3.6; 947 -3.8; 1042 -3.8; 1146 -4.1; 1261 -4.1; 1387 -4.4; 1526 -4.8; 1678 -5.4; 1846 -6.0; 2031 -5.2; 2234 -3.3; 2457 -2.6; 2703 -4.5; 2973 -6.9; 3270 -7.2; 3597 -6.1; 3957 -6.3; 4353 -7.4; 4788 -7.6; 5267 -6.9; 5793 -6.1; 6373 -4.7; 7010 -2.1; 7711 -3.4; 8482 -3.7; 9330 -3.7; 10263 -3.7; 11289 -3.7; 12418 -3.7; 13660 -3.7; 15026 -3.7; 16529 -3.7; 18182 -3.7; 20000 -3.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 380 Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 380 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 56 Hz   | 1.1  | -3.8 dB |
| Peaking | 135 Hz  | 1.65 | -2.5 dB |
| Peaking | 301 Hz  | 1.53 | 3.5 dB  |
| Peaking | 1766 Hz | 4.52 | -2.1 dB |
| Peaking | 4366 Hz | 1.76 | -3.9 dB |
| Peaking | 2474 Hz | 4.22 | 4.1 dB  |
| Peaking | 3082 Hz | 1.78 | -3.7 dB |
| Peaking | 3792 Hz | 3.55 | 3.1 dB  |
| Peaking | 5918 Hz | 3.05 | -1.1 dB |
| Peaking | 7033 Hz | 4.53 | 2.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | 2.8 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | -3.8 dB |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20HD%20380%20Pro/Sennheiser%20HD%20380%20Pro.png)