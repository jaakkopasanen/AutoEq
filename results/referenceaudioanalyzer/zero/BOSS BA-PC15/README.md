# BOSS BA-PC15
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.4; 25 -2.1; 28 -3.0; 31 -3.7; 34 -4.2; 37 -4.6; 41 -5.0; 45 -5.3; 49 -5.6; 54 -6.0; 60 -6.2; 66 -6.3; 72 -6.3; 79 -6.3; 87 -6.3; 96 -6.6; 106 -6.5; 116 -6.3; 128 -6.1; 141 -5.6; 155 -5.2; 170 -5.2; 187 -5.6; 206 -5.9; 227 -6.0; 249 -5.9; 274 -5.7; 302 -5.4; 332 -5.1; 365 -4.7; 402 -4.3; 442 -3.9; 486 -3.5; 535 -3.1; 588 -2.7; 647 -2.2; 712 -1.8; 783 -1.5; 861 -1.4; 947 -1.2; 1042 -1.1; 1146 -1.1; 1261 -1.3; 1387 -1.6; 1526 -2.2; 1678 -2.9; 1846 -4.1; 2031 -5.9; 2234 -7.9; 2457 -9.8; 2703 -13.3; 2973 -17.0; 3270 -17.9; 3597 -16.0; 3957 -13.1; 4353 -11.2; 4788 -10.1; 5267 -10.4; 5793 -11.7; 6373 -12.0; 7010 -10.1; 7711 -6.5; 8482 -6.2; 9330 -6.2; 10263 -6.2; 11289 -6.5; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`BOSS BA-PC15 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BOSS BA-PC15 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 20 Hz   | 1.6  | 5.7 dB   |
| Peaking | 1078 Hz | 0.63 | 6.2 dB   |
| Peaking | 1976 Hz | 1.07 | 5.1 dB   |
| Peaking | 2907 Hz | 0.74 | -10.2 dB |
| Peaking | 3178 Hz | 3.6  | -6.2 dB  |
| Peaking | 147 Hz  | 1.1  | -1.7 dB  |
| Peaking | 160 Hz  | 2.28 | 2.4 dB   |
| Peaking | 4823 Hz | 3.98 | 2.1 dB   |
| Peaking | 6500 Hz | 2.39 | -5.6 dB  |
| Peaking | 7786 Hz | 1.79 | 4.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB   |
| Peaking | 62 Hz    | 1.41 | -1.1 dB  |
| Peaking | 125 Hz   | 1.41 | 0.3 dB   |
| Peaking | 250 Hz   | 1.41 | -0.1 dB  |
| Peaking | 500 Hz   | 1.41 | 1.8 dB   |
| Peaking | 1000 Hz  | 1.41 | 6.3 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 4000 Hz  | 1.41 | -10.2 dB |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 16000 Hz | 1.41 | 0.2 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/BOSS%20BA-PC15/BOSS%20BA-PC15.png)