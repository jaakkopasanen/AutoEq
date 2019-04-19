# AuGlamour F300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.9; 23 -10.0; 25 -10.1; 28 -10.3; 31 -10.5; 34 -10.6; 37 -10.6; 41 -10.7; 45 -10.8; 49 -10.8; 54 -11.0; 60 -11.2; 66 -11.3; 72 -11.4; 79 -11.6; 87 -11.8; 96 -12.0; 106 -12.1; 116 -11.9; 128 -11.9; 141 -12.1; 155 -12.0; 170 -11.8; 187 -11.5; 206 -11.2; 227 -10.9; 249 -10.5; 274 -10.1; 302 -9.8; 332 -9.3; 365 -8.9; 402 -8.6; 442 -8.2; 486 -7.8; 535 -7.3; 588 -7.0; 647 -6.8; 712 -6.5; 783 -6.3; 861 -6.1; 947 -6.0; 1042 -6.1; 1146 -6.1; 1261 -6.0; 1387 -5.8; 1526 -5.7; 1678 -5.8; 1846 -6.0; 2031 -6.3; 2234 -6.6; 2457 -6.7; 2703 -6.3; 2973 -5.6; 3270 -5.9; 3597 -6.9; 3957 -7.5; 4353 -7.2; 4788 -4.9; 5267 -1.0; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.2; 15026 -17.5; 16529 -19.4; 18182 -16.2; 20000 -12.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AuGlamour F300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AuGlamour F300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 39 Hz    | 0.33 | -3.8 dB  |
| Peaking | 134 Hz   | 0.79 | -3.4 dB  |
| Peaking | 260 Hz   | 1.26 | -1.9 dB  |
| Peaking | 5953 Hz  | 3.07 | 7.1 dB   |
| Peaking | 17021 Hz | 1.22 | -14.1 dB |
| Peaking | 1244 Hz  | 1.07 | 0.8 dB   |
| Peaking | 4226 Hz  | 4.37 | -2.3 dB  |
| Peaking | 5231 Hz  | 8.88 | 2.0 dB   |
| Peaking | 12480 Hz | 2.46 | 4.6 dB   |
| Peaking | 20555 Hz | 0.15 | -2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.8 dB  |
| Peaking | 62 Hz    | 1.41 | -3.5 dB  |
| Peaking | 125 Hz   | 1.41 | -4.8 dB  |
| Peaking | 250 Hz   | 1.41 | -3.4 dB  |
| Peaking | 500 Hz   | 1.41 | -0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.9 dB   |
| Peaking | 16000 Hz | 1.41 | -14.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/AuGlamour%20F300/AuGlamour%20F300.png)