# Sennheiser HD 600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.9; 31 -1.5; 34 -2.1; 37 -2.7; 41 -3.5; 45 -4.1; 49 -4.4; 54 -4.4; 60 -4.7; 66 -5.3; 72 -5.9; 79 -6.4; 87 -6.9; 96 -7.3; 106 -7.6; 116 -7.7; 128 -7.7; 141 -7.7; 155 -7.7; 170 -7.7; 187 -7.6; 206 -7.4; 227 -7.1; 249 -6.9; 274 -6.6; 302 -6.4; 332 -6.2; 365 -6.0; 402 -5.9; 442 -5.7; 486 -5.7; 535 -5.7; 588 -5.5; 647 -5.4; 712 -5.4; 783 -5.4; 861 -5.1; 947 -5.2; 1042 -5.7; 1146 -6.0; 1261 -6.0; 1387 -6.3; 1526 -6.2; 1678 -5.7; 1846 -5.3; 2031 -5.0; 2234 -5.2; 2457 -5.8; 2703 -6.3; 2973 -7.1; 3270 -8.0; 3597 -9.0; 3957 -9.6; 4353 -10.1; 4788 -11.6; 5267 -13.2; 5793 -13.0; 6373 -10.2; 7010 -5.4; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 23 Hz   | 1.74 | 5.7 dB   |
| Peaking | 36 Hz   | 1.85 | 2.8 dB   |
| Peaking | 3489 Hz | 0.22 | 1.7 dB   |
| Peaking | 5666 Hz | 1.32 | -10.0 dB |
| Peaking | 7091 Hz | 2.97 | 5.9 dB   |
| Peaking | 60 Hz   | 2.67 | 1.4 dB   |
| Peaking | 135 Hz  | 0.84 | -1.6 dB  |
| Peaking | 1337 Hz | 1.54 | -2.5 dB  |
| Peaking | 1395 Hz | 0.49 | 1.7 dB   |
| Peaking | 3419 Hz | 2.81 | -1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.9 dB |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20HD%20600/Sennheiser%20HD%20600.png)