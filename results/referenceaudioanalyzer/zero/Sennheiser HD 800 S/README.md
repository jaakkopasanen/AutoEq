# Sennheiser HD 800 S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.8; 41 -1.5; 45 -2.0; 49 -2.2; 54 -2.6; 60 -3.1; 66 -3.7; 72 -4.1; 79 -4.7; 87 -5.2; 96 -5.6; 106 -5.9; 116 -6.2; 128 -6.5; 141 -6.6; 155 -6.9; 170 -6.9; 187 -6.9; 206 -6.9; 227 -6.9; 249 -6.9; 274 -6.9; 302 -6.9; 332 -6.9; 365 -6.9; 402 -6.8; 442 -6.6; 486 -6.6; 535 -6.5; 588 -6.3; 647 -6.3; 712 -6.3; 783 -6.3; 861 -6.3; 947 -6.2; 1042 -6.0; 1146 -5.8; 1261 -5.4; 1387 -5.0; 1526 -4.4; 1678 -3.8; 1846 -3.2; 2031 -2.8; 2234 -2.7; 2457 -2.4; 2703 -2.1; 2973 -2.1; 3270 -2.4; 3597 -3.4; 3957 -5.5; 4353 -8.8; 4788 -12.5; 5267 -14.7; 5793 -15.0; 6373 -14.0; 7010 -11.9; 7711 -9.3; 8482 -6.6; 9330 -6.5; 10263 -6.5; 11289 -7.8; 12418 -9.1; 13660 -9.4; 15026 -7.8; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 800 S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.42 | 6.6 dB   |
| Peaking | 116 Hz   | 0.39 | -1.5 dB  |
| Peaking | 3107 Hz  | 0.85 | 6.6 dB   |
| Peaking | 5487 Hz  | 1.84 | -12.4 dB |
| Peaking | 13424 Hz | 3.24 | -3.2 dB  |
| Peaking | 4725 Hz  | 7.33 | -1.2 dB  |
| Peaking | 5525 Hz  | 6.58 | 1.3 dB   |
| Peaking | 6988 Hz  | 2.75 | -3.2 dB  |
| Peaking | 8339 Hz  | 1.48 | 2.7 dB   |
| Peaking | 11894 Hz | 4.27 | -1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB  |
| Peaking | 62 Hz    | 1.41 | 2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.5 dB |
| Peaking | 8000 Hz  | 1.41 | -4.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20HD%20800%20S/Sennheiser%20HD%20800%20S.png)