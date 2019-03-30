# Beyerdynamic DT 880 Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.3; 23 -2.6; 25 -2.8; 28 -3.0; 31 -3.1; 34 -3.1; 37 -3.1; 41 -3.1; 45 -3.1; 49 -3.1; 54 -3.2; 60 -3.3; 66 -3.2; 72 -3.1; 79 -3.3; 87 -3.5; 96 -3.7; 106 -3.8; 116 -3.8; 128 -3.7; 141 -3.8; 155 -3.9; 170 -3.9; 187 -3.8; 206 -3.7; 227 -3.8; 249 -3.7; 274 -3.5; 302 -3.4; 332 -3.1; 365 -3.1; 402 -2.9; 442 -2.7; 486 -2.5; 535 -2.3; 588 -2.1; 647 -2.1; 712 -1.8; 783 -1.7; 861 -1.5; 947 -1.5; 1042 -1.3; 1146 -0.9; 1261 -0.7; 1387 -0.5; 1526 -0.7; 1678 -0.8; 1846 -0.8; 2031 -0.8; 2234 -0.8; 2457 -0.5; 2703 -0.7; 2973 -1.0; 3270 -1.4; 3597 -2.3; 3957 -4.0; 4353 -5.7; 4788 -7.2; 5267 -10.1; 5793 -13.0; 6373 -13.0; 7010 -9.6; 7711 -5.0; 8482 -3.2; 9330 -3.3; 10263 -3.5; 11289 -4.7; 12418 -3.8; 13660 -3.3; 15026 -3.3; 16529 -3.3; 18182 -3.3; 20000 -3.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 880 Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 880 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 11 Hz    | 0.75 | 1.5 dB   |
| Peaking | 180 Hz   | 0.77 | -0.8 dB  |
| Peaking | 3660 Hz  | 0.23 | 3.6 dB   |
| Peaking | 5939 Hz  | 1.99 | -14.0 dB |
| Peaking | 12037 Hz | 3.23 | -2.3 dB  |
| Peaking | 3211 Hz  | 2.86 | 0.7 dB   |
| Peaking | 4194 Hz  | 6.44 | -0.8 dB  |
| Peaking | 5878 Hz  | 3.58 | 2.8 dB   |
| Peaking | 6705 Hz  | 1.66 | -3.4 dB  |
| Peaking | 8014 Hz  | 3.66 | 3.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -0.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.6 dB |
| Peaking | 8000 Hz  | 1.41 | -4.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20DT%20880%20Pro/Beyerdynamic%20DT%20880%20Pro.png)