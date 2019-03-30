# Sennheiser HD 598
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.7; 34 -1.2; 37 -2.0; 41 -2.8; 45 -3.2; 49 -3.4; 54 -3.6; 60 -4.4; 66 -5.1; 72 -5.5; 79 -5.8; 87 -6.1; 96 -6.4; 106 -6.8; 116 -7.1; 128 -7.3; 141 -7.6; 155 -7.6; 170 -7.6; 187 -7.6; 206 -7.6; 227 -7.5; 249 -7.3; 274 -7.2; 302 -7.2; 332 -7.1; 365 -6.8; 402 -6.7; 442 -6.8; 486 -6.6; 535 -6.3; 588 -6.0; 647 -5.4; 712 -4.8; 783 -4.8; 861 -5.0; 947 -4.7; 1042 -4.6; 1146 -4.8; 1261 -5.0; 1387 -4.9; 1526 -4.6; 1678 -4.0; 1846 -3.6; 2031 -3.5; 2234 -4.2; 2457 -5.2; 2703 -5.7; 2973 -5.5; 3270 -6.2; 3597 -8.2; 3957 -10.4; 4353 -12.0; 4788 -12.2; 5267 -10.7; 5793 -8.4; 6373 -5.9; 7010 -4.8; 7711 -6.2; 8482 -6.5; 9330 -6.6; 10263 -7.8; 11289 -8.8; 12418 -7.4; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 598 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 598 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 1.37 | 6.4 dB  |
| Peaking | 44 Hz    | 2.14 | 2.1 dB  |
| Peaking | 865 Hz   | 2.23 | 1.6 dB  |
| Peaking | 1962 Hz  | 1.39 | 3.0 dB  |
| Peaking | 4540 Hz  | 3.07 | -6.8 dB |
| Peaking | 186 Hz   | 0.91 | -1.3 dB |
| Peaking | 698 Hz   | 6.6  | 0.7 dB  |
| Peaking | 5418 Hz  | 5.78 | -1.5 dB |
| Peaking | 6773 Hz  | 4.22 | 2.6 dB  |
| Peaking | 11223 Hz | 4.28 | -2.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.7 dB |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20HD%20598/Sennheiser%20HD%20598.png)