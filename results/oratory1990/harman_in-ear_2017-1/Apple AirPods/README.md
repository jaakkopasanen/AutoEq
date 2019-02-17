# Apple AirPods
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -1.1; 72 -1.9; 79 -2.6; 87 -3.2; 96 -3.8; 106 -4.3; 116 -4.8; 128 -5.1; 141 -5.3; 155 -5.4; 170 -5.4; 187 -5.3; 206 -5.2; 227 -5.1; 249 -5.1; 274 -5.0; 302 -5.0; 332 -4.9; 365 -4.8; 402 -4.9; 442 -4.9; 486 -5.0; 535 -5.0; 588 -5.1; 647 -5.2; 712 -5.4; 783 -5.6; 861 -5.9; 947 -6.2; 1042 -6.7; 1146 -7.3; 1261 -8.1; 1387 -9.0; 1526 -9.9; 1678 -10.8; 1846 -11.2; 2031 -11.0; 2234 -10.6; 2457 -10.2; 2703 -10.2; 2973 -9.5; 3270 -8.1; 3597 -7.5; 3957 -7.4; 4353 -7.6; 4788 -8.3; 5267 -9.8; 5793 -9.0; 6373 -4.7; 7010 -4.1; 7711 -6.2; 8482 -8.6; 9330 -11.2; 10263 -9.7; 11289 -6.9; 12418 -9.8; 13660 -19.6; 15026 -26.1; 16529 -24.6; 18182 -17.6; 20000 -6.5
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
| Peaking | 32 Hz    | 0.38 | 6.3 dB   |
| Peaking | 1752 Hz  | 2.72 | -4.0 dB  |
| Peaking | 2536 Hz  | 1.98 | -3.1 dB  |
| Peaking | 14903 Hz | 2.82 | -13.7 dB |
| Peaking | 16894 Hz | 1.46 | -15.4 dB |
| Peaking | 492 Hz   | 1.08 | 1.6 dB   |
| Peaking | 5552 Hz  | 3.79 | -6.1 dB  |
| Peaking | 6734 Hz  | 1.79 | 8.0 dB   |
| Peaking | 9969 Hz  | 0.98 | -6.7 dB  |
| Peaking | 11501 Hz | 3.09 | 8.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB   |
| Peaking | 62 Hz    | 1.41 | 4.6 dB   |
| Peaking | 125 Hz   | 1.41 | 0.2 dB   |
| Peaking | 250 Hz   | 1.41 | 1.0 dB   |
| Peaking | 500 Hz   | 1.41 | 1.7 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 2000 Hz  | 1.41 | -5.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 16000 Hz | 1.41 | -22.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Apple%20AirPods/Apple%20AirPods.png)