# MyST IzoEM-1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.5; 206 -0.5; 227 -0.5; 249 -0.5; 274 -0.9; 302 -2.3; 332 -3.7; 365 -5.3; 402 -6.9; 442 -8.6; 486 -10.5; 535 -12.5; 588 -14.5; 647 -16.4; 712 -17.9; 783 -19.0; 861 -19.4; 947 -19.4; 1042 -18.9; 1146 -17.2; 1261 -14.6; 1387 -11.5; 1526 -9.6; 1678 -9.9; 1846 -12.8; 2031 -16.4; 2234 -18.4; 2457 -18.0; 2703 -15.7; 2973 -13.4; 3270 -12.1; 3597 -11.5; 3957 -10.8; 4353 -9.8; 4788 -7.9; 5267 -4.7; 5793 -1.0; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MyST IzoEM-1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MyST IzoEM-1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 32 Hz   | 0.13 | 6.2 dB   |
| Peaking | 252 Hz  | 1.17 | 4.6 dB   |
| Peaking | 812 Hz  | 1.13 | -14.2 dB |
| Peaking | 2486 Hz | 2.01 | -10.2 dB |
| Peaking | 6099 Hz | 4.49 | 7.6 dB   |
| Peaking | 1122 Hz | 4.01 | -3.3 dB  |
| Peaking | 1583 Hz | 3.22 | 3.7 dB   |
| Peaking | 2106 Hz | 3.86 | -4.4 dB  |
| Peaking | 2879 Hz | 0.8  | 2.5 dB   |
| Peaking | 3884 Hz | 2.24 | -3.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB   |
| Peaking | 62 Hz    | 1.41 | 4.4 dB   |
| Peaking | 125 Hz   | 1.41 | 4.3 dB   |
| Peaking | 250 Hz   | 1.41 | 7.4 dB   |
| Peaking | 500 Hz   | 1.41 | -4.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -11.0 dB |
| Peaking | 2000 Hz  | 1.41 | -6.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 3.2 dB   |
| Peaking | 16000 Hz | 1.41 | -0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/MyST%20IzoEM-1/MyST%20IzoEM-1.png)