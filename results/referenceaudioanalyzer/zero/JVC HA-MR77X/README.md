# JVC HA-MR77X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -1.9; 28 -3.4; 31 -4.6; 34 -5.4; 37 -5.9; 41 -6.4; 45 -6.7; 49 -7.0; 54 -7.3; 60 -7.3; 66 -7.3; 72 -7.3; 79 -7.6; 87 -7.8; 96 -8.0; 106 -8.2; 116 -8.4; 128 -8.6; 141 -8.8; 155 -8.9; 170 -8.9; 187 -8.9; 206 -9.0; 227 -9.2; 249 -9.5; 274 -9.8; 302 -10.0; 332 -10.2; 365 -10.4; 402 -10.6; 442 -10.3; 486 -9.4; 535 -8.6; 588 -9.0; 647 -10.5; 712 -12.6; 783 -14.2; 861 -14.8; 947 -14.5; 1042 -13.1; 1146 -10.4; 1261 -7.2; 1387 -4.3; 1526 -1.7; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -8.4; 4788 -14.7; 5267 -15.0; 5793 -10.7; 6373 -10.9; 7010 -11.4; 7711 -8.4; 8482 -6.5; 9330 -7.2; 10263 -9.1; 11289 -9.6; 12418 -9.4; 13660 -8.2; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JVC HA-MR77X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JVC HA-MR77X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 2.39 | 6.6 dB   |
| Peaking | 322 Hz   | 0.48 | -4.3 dB  |
| Peaking | 903 Hz   | 2.04 | -11.8 dB |
| Peaking | 3628 Hz  | 0.49 | 25.4 dB  |
| Peaking | 4992 Hz  | 0.81 | -28.6 dB |
| Peaking | 1149 Hz  | 5.23 | -2.2 dB  |
| Peaking | 1635 Hz  | 3.06 | 2.8 dB   |
| Peaking | 2984 Hz  | 5.33 | -1.8 dB  |
| Peaking | 8644 Hz  | 5.32 | 2.7 dB   |
| Peaking | 11665 Hz | 2.2  | -2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | -8.8 dB |
| Peaking | 2000 Hz  | 1.41 | 10.7 dB |
| Peaking | 4000 Hz  | 1.41 | -0.4 dB |
| Peaking | 8000 Hz  | 1.41 | -4.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/JVC%20HA-MR77X/JVC%20HA-MR77X.png)