# Sennheiser HD 700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -1.2; 49 -1.8; 54 -2.5; 60 -3.2; 66 -3.9; 72 -4.5; 79 -5.1; 87 -5.6; 96 -6.1; 106 -6.5; 116 -6.8; 128 -7.0; 141 -7.3; 155 -7.5; 170 -7.7; 187 -7.7; 206 -7.7; 227 -7.7; 249 -7.6; 274 -7.4; 302 -7.3; 332 -7.3; 365 -7.2; 402 -7.0; 442 -7.0; 486 -6.7; 535 -6.7; 588 -6.7; 647 -6.5; 712 -6.3; 783 -6.4; 861 -6.4; 947 -6.2; 1042 -5.9; 1146 -5.5; 1261 -5.0; 1387 -4.5; 1526 -3.9; 1678 -3.2; 1846 -2.2; 2031 -1.1; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.9; 3597 -1.8; 3957 -2.6; 4353 -4.9; 4788 -9.9; 5267 -14.8; 5793 -16.0; 6373 -13.5; 7010 -11.9; 7711 -13.0; 8482 -13.3; 9330 -12.2; 10263 -10.5; 11289 -8.0; 12418 -6.5; 13660 -6.5; 15026 -7.2; 16529 -7.1; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 32 Hz   | 0.5  | 7.4 dB   |
| Peaking | 116 Hz  | 0.33 | -2.3 dB  |
| Peaking | 3100 Hz | 0.8  | 7.8 dB   |
| Peaking | 5553 Hz | 2.68 | -12.4 dB |
| Peaking | 8556 Hz | 1.96 | -6.8 dB  |
| Peaking | 1023 Hz | 2.35 | -0.6 dB  |
| Peaking | 2128 Hz | 4.08 | 1.2 dB   |
| Peaking | 3260 Hz | 1.59 | -0.9 dB  |
| Peaking | 4308 Hz | 3.05 | 1.7 dB   |
| Peaking | 4864 Hz | 7.21 | -1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -9.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20HD%20700/Sennheiser%20HD%20700.png)