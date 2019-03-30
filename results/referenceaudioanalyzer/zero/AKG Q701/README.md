# AKG Q701
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.9; 72 -1.5; 79 -2.1; 87 -2.5; 96 -2.7; 106 -3.2; 116 -3.7; 128 -4.1; 141 -4.3; 155 -4.5; 170 -4.7; 187 -5.0; 206 -5.2; 227 -5.2; 249 -5.5; 274 -5.5; 302 -5.3; 332 -5.2; 365 -5.2; 402 -5.0; 442 -4.7; 486 -4.4; 535 -4.2; 588 -3.9; 647 -3.4; 712 -3.1; 783 -3.2; 861 -3.6; 947 -4.0; 1042 -4.4; 1146 -4.8; 1261 -5.1; 1387 -5.5; 1526 -6.0; 1678 -7.0; 1846 -8.2; 2031 -9.2; 2234 -9.4; 2457 -8.7; 2703 -7.1; 2973 -4.9; 3270 -3.2; 3597 -3.0; 3957 -4.4; 4353 -6.1; 4788 -7.5; 5267 -9.1; 5793 -11.2; 6373 -14.9; 7010 -18.3; 7711 -18.8; 8482 -15.9; 9330 -12.2; 10263 -10.7; 11289 -10.4; 12418 -9.6; 13660 -8.0; 15026 -6.6; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG Q701 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG Q701 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 36 Hz    | 0.39 | 6.4 dB   |
| Peaking | 767 Hz   | 0.96 | 3.3 dB   |
| Peaking | 2307 Hz  | 1.85 | -5.7 dB  |
| Peaking | 3432 Hz  | 1.34 | 6.4 dB   |
| Peaking | 7431 Hz  | 1.66 | -13.5 dB |
| Peaking | 40 Hz    | 2.22 | -0.4 dB  |
| Peaking | 59 Hz    | 3.51 | 0.7 dB   |
| Peaking | 9697 Hz  | 4.62 | 1.2 dB   |
| Peaking | 12163 Hz | 1.95 | -1.8 dB  |
| Peaking | 14879 Hz | 1.39 | 1.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB   |
| Peaking | 62 Hz    | 1.41 | 4.6 dB   |
| Peaking | 125 Hz   | 1.41 | 1.6 dB   |
| Peaking | 250 Hz   | 1.41 | 0.1 dB   |
| Peaking | 500 Hz   | 1.41 | 1.9 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB   |
| Peaking | 8000 Hz  | 1.41 | -12.6 dB |
| Peaking | 16000 Hz | 1.41 | 1.1 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20Q701/AKG%20Q701.png)