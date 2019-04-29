# Vsonic GR01
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -3.4; 25 -3.8; 28 -4.3; 31 -4.6; 34 -4.9; 37 -5.2; 41 -5.5; 45 -5.8; 49 -6.1; 54 -6.4; 60 -6.7; 66 -7.0; 72 -7.4; 79 -7.8; 87 -8.2; 96 -8.7; 106 -9.1; 116 -9.6; 128 -9.9; 141 -10.2; 155 -10.4; 170 -10.6; 187 -10.8; 206 -11.0; 227 -11.1; 249 -11.0; 274 -10.9; 302 -10.8; 332 -10.6; 365 -10.3; 402 -10.1; 442 -9.9; 486 -9.7; 535 -9.3; 588 -9.0; 647 -8.5; 712 -8.0; 783 -7.4; 861 -6.9; 947 -6.6; 1042 -6.6; 1146 -7.0; 1261 -7.2; 1387 -6.8; 1526 -6.1; 1678 -5.1; 1846 -4.1; 2031 -3.1; 2234 -2.1; 2457 -1.6; 2703 -0.9; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.7; 4788 -1.8; 5267 -1.8; 5793 -2.0; 6373 -2.3; 7010 -4.0; 7711 -6.2; 8482 -7.5; 9330 -10.8; 10263 -8.6; 11289 -6.5; 12418 -6.5; 13660 -12.4; 15026 -19.6; 16529 -22.0; 18182 -22.0; 20000 -20.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Vsonic GR01 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Vsonic GR01 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 11 Hz    | 0.29 | 4.0 dB   |
| Peaking | 236 Hz   | 0.41 | -4.7 dB  |
| Peaking | 3638 Hz  | 0.79 | 6.8 dB   |
| Peaking | 15994 Hz | 1.89 | -10.0 dB |
| Peaking | 19108 Hz | 0.7  | -15.2 dB |
| Peaking | 1379 Hz  | 4.36 | -1.5 dB  |
| Peaking | 2257 Hz  | 4.09 | 0.8 dB   |
| Peaking | 6403 Hz  | 5.58 | 2.0 dB   |
| Peaking | 9366 Hz  | 4.65 | -4.7 dB  |
| Peaking | 12135 Hz | 3.51 | 4.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 2.7 dB   |
| Peaking | 62 Hz    | 1.41 | -0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.8 dB  |
| Peaking | 250 Hz   | 1.41 | -4.2 dB  |
| Peaking | 500 Hz   | 1.41 | -2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 16000 Hz | 1.41 | -18.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Vsonic%20GR01/Vsonic%20GR01.png)