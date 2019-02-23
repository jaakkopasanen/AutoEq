# Apple AirPods
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.8; 72 -1.6; 79 -2.3; 87 -2.9; 96 -3.5; 106 -4.0; 116 -4.4; 128 -4.7; 141 -4.9; 155 -5.0; 170 -5.0; 187 -4.9; 206 -4.8; 227 -4.8; 249 -4.7; 274 -4.7; 302 -4.6; 332 -4.5; 365 -4.5; 402 -4.5; 442 -4.6; 486 -4.6; 535 -4.6; 588 -4.7; 647 -4.8; 712 -5.0; 783 -5.2; 861 -5.5; 947 -5.9; 1042 -6.4; 1146 -7.0; 1261 -7.7; 1387 -8.6; 1526 -9.6; 1678 -10.4; 1846 -10.9; 2031 -10.7; 2234 -10.2; 2457 -9.8; 2703 -9.8; 2973 -9.1; 3270 -7.8; 3597 -7.1; 3957 -7.1; 4353 -7.3; 4788 -8.0; 5267 -9.5; 5793 -8.7; 6373 -4.3; 7010 -4.0; 7711 -6.2; 8482 -8.2; 9330 -10.8; 10263 -9.3; 11289 -6.5; 12418 -9.5; 13660 -19.2; 15026 -25.7; 16529 -24.2; 18182 -17.2; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple AirPods GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple AirPods ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 18 Hz    | 0.16 | 6.3 dB   |
| Peaking | 1776 Hz  | 2.91 | -4.0 dB  |
| Peaking | 2538 Hz  | 2.42 | -2.9 dB  |
| Peaking | 14875 Hz | 2.89 | -13.8 dB |
| Peaking | 16894 Hz | 1.53 | -15.2 dB |
| Peaking | 529 Hz   | 1.08 | 1.9 dB   |
| Peaking | 7004 Hz  | 3.47 | 7.1 dB   |
| Peaking | 8274 Hz  | 0.86 | -3.9 dB  |
| Peaking | 11677 Hz | 3.36 | 6.3 dB   |
| Peaking | 13653 Hz | 6.45 | -2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB   |
| Peaking | 62 Hz    | 1.41 | 4.8 dB   |
| Peaking | 125 Hz   | 1.41 | 0.5 dB   |
| Peaking | 250 Hz   | 1.41 | 1.3 dB   |
| Peaking | 500 Hz   | 1.41 | 2.0 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 16000 Hz | 1.41 | -22.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Apple%20AirPods/Apple%20AirPods.png)