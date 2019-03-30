# Sennheiser MM 100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -1.6; 66 -2.9; 72 -4.1; 79 -5.2; 87 -6.2; 96 -7.1; 106 -7.6; 116 -8.0; 128 -8.1; 141 -8.1; 155 -8.1; 170 -7.9; 187 -7.6; 206 -7.3; 227 -7.0; 249 -6.6; 274 -6.1; 302 -5.6; 332 -5.3; 365 -5.0; 402 -4.7; 442 -4.3; 486 -4.1; 535 -3.8; 588 -3.6; 647 -3.3; 712 -3.2; 783 -3.1; 861 -2.9; 947 -2.9; 1042 -2.9; 1146 -3.1; 1261 -3.2; 1387 -3.4; 1526 -3.9; 1678 -4.7; 1846 -5.5; 2031 -6.1; 2234 -7.4; 2457 -9.6; 2703 -11.8; 2973 -12.1; 3270 -10.5; 3597 -10.2; 3957 -12.6; 4353 -14.6; 4788 -14.0; 5267 -11.2; 5793 -7.6; 6373 -4.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -8.2; 10263 -9.1; 11289 -8.4; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser MM 100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser MM 100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 34 Hz    | 1.05 | 7.2 dB  |
| Peaking | 979 Hz   | 0.73 | 4.0 dB  |
| Peaking | 2768 Hz  | 3.53 | -5.4 dB |
| Peaking | 4554 Hz  | 2.13 | -8.5 dB |
| Peaking | 6559 Hz  | 4.83 | 5.9 dB  |
| Peaking | 34 Hz    | 1.51 | -7.7 dB |
| Peaking | 43 Hz    | 0.49 | 7.7 dB  |
| Peaking | 107 Hz   | 0.71 | -5.5 dB |
| Peaking | 395 Hz   | 1.39 | 1.1 dB  |
| Peaking | 10399 Hz | 4.31 | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | 3.6 dB  |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -7.6 dB |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20MM%20100/Sennheiser%20MM%20100.png)