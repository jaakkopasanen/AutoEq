# JVC HA-FW01
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.6; 23 -5.0; 25 -5.3; 28 -5.8; 31 -6.1; 34 -6.4; 37 -6.7; 41 -7.0; 45 -7.3; 49 -7.5; 54 -7.8; 60 -8.1; 66 -8.5; 72 -8.9; 79 -9.2; 87 -9.7; 96 -10.1; 106 -10.4; 116 -10.8; 128 -11.0; 141 -11.3; 155 -11.4; 170 -11.4; 187 -11.4; 206 -11.3; 227 -11.1; 249 -10.9; 274 -10.6; 302 -10.2; 332 -9.7; 365 -9.1; 402 -8.6; 442 -8.1; 486 -7.6; 535 -7.0; 588 -6.4; 647 -5.3; 712 -4.1; 783 -3.9; 861 -3.5; 947 -3.1; 1042 -3.2; 1146 -3.5; 1261 -3.9; 1387 -4.1; 1526 -4.0; 1678 -3.8; 1846 -3.5; 2031 -3.2; 2234 -2.7; 2457 -2.7; 2703 -3.1; 2973 -3.4; 3270 -3.6; 3597 -3.5; 3957 -3.6; 4353 -4.2; 4788 -5.1; 5267 -4.8; 5793 -2.6; 6373 -0.5; 7010 -3.3; 7711 -5.5; 8482 -5.8; 9330 -5.8; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -7.1; 15026 -18.6; 16529 -24.1; 18182 -22.2; 20000 -19.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JVC HA-FW01 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JVC HA-FW01 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 182 Hz   | 0.45 | -5.9 dB  |
| Peaking | 865 Hz   | 1.3  | 2.9 dB   |
| Peaking | 8135 Hz  | 0.3  | 14.0 dB  |
| Peaking | 13337 Hz | 1.5  | 13.9 dB  |
| Peaking | 15781 Hz | 0.34 | -30.4 dB |
| Peaking | 20 Hz    | 1.86 | 1.6 dB   |
| Peaking | 2324 Hz  | 4.44 | 1.1 dB   |
| Peaking | 5056 Hz  | 3.07 | -2.6 dB  |
| Peaking | 6373 Hz  | 4    | 4.5 dB   |
| Peaking | 7617 Hz  | 3.8  | -2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.4 dB   |
| Peaking | 62 Hz    | 1.41 | -1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -4.6 dB  |
| Peaking | 250 Hz   | 1.41 | -4.8 dB  |
| Peaking | 500 Hz   | 1.41 | -1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.1 dB   |
| Peaking | 16000 Hz | 1.41 | -19.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/JVC%20HA-FW01/JVC%20HA-FW01.png)