# Advanced M55D
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.7; 23 -8.9; 25 -9.1; 28 -9.3; 31 -9.4; 34 -9.5; 37 -9.6; 41 -9.6; 45 -9.7; 49 -9.8; 54 -9.8; 60 -9.8; 66 -9.9; 72 -10.1; 79 -10.2; 87 -10.4; 96 -10.6; 106 -10.8; 116 -11.0; 128 -11.1; 141 -11.2; 155 -11.3; 170 -11.3; 187 -11.3; 206 -11.2; 227 -11.0; 249 -10.9; 274 -10.7; 302 -10.4; 332 -10.1; 365 -9.7; 402 -9.4; 442 -9.2; 486 -8.8; 535 -8.5; 588 -8.1; 647 -7.8; 712 -7.3; 783 -6.8; 861 -6.4; 947 -6.1; 1042 -6.0; 1146 -6.0; 1261 -5.9; 1387 -5.3; 1526 -4.5; 1678 -3.7; 1846 -3.4; 2031 -3.2; 2234 -2.8; 2457 -1.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -4.9; 5793 -5.9; 6373 -7.2; 7010 -9.1; 7711 -11.9; 8482 -10.4; 9330 -7.8; 10263 -6.5; 11289 -6.5; 12418 -8.4; 13660 -18.9; 15026 -29.5; 16529 -34.4; 18182 -34.8; 20000 -31.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Advanced M55D GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Advanced M55D ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.82 | -1.8 dB  |
| Peaking | 286 Hz   | 0.21 | -5.5 dB  |
| Peaking | 7429 Hz  | 2.47 | -13.4 dB |
| Peaking | 7888 Hz  | 0.23 | 29.5 dB  |
| Peaking | 17185 Hz | 0.25 | -46.0 dB |
| Peaking | 5195 Hz  | 1.07 | 3.2 dB   |
| Peaking | 5605 Hz  | 3.85 | -6.2 dB  |
| Peaking | 8513 Hz  | 4.97 | -3.5 dB  |
| Peaking | 12080 Hz | 2.76 | 7.0 dB   |
| Peaking | 14809 Hz | 2.71 | -7.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.7 dB  |
| Peaking | 62 Hz    | 1.41 | -2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -3.8 dB  |
| Peaking | 250 Hz   | 1.41 | -3.8 dB  |
| Peaking | 500 Hz   | 1.41 | -1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.6 dB   |
| Peaking | 16000 Hz | 1.41 | -34.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Advanced%20M55D/Advanced%20M55D.png)