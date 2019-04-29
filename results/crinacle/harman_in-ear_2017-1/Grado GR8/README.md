# Grado GR8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.7; 23 -5.8; 25 -6.0; 28 -6.2; 31 -6.5; 34 -6.7; 37 -6.9; 41 -7.0; 45 -7.1; 49 -7.0; 54 -7.2; 60 -7.5; 66 -7.9; 72 -8.3; 79 -8.7; 87 -9.0; 96 -9.6; 106 -9.9; 116 -10.2; 128 -10.6; 141 -11.0; 155 -11.3; 170 -11.4; 187 -11.5; 206 -11.5; 227 -11.5; 249 -11.6; 274 -11.5; 302 -11.3; 332 -11.1; 365 -10.8; 402 -10.6; 442 -10.3; 486 -10.0; 535 -9.7; 588 -9.2; 647 -8.8; 712 -8.2; 783 -7.7; 861 -7.2; 947 -6.9; 1042 -6.9; 1146 -7.2; 1261 -7.2; 1387 -6.9; 1526 -6.1; 1678 -5.1; 1846 -4.0; 2031 -2.9; 2234 -3.5; 2457 -2.2; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.6; 3957 -5.4; 4353 -5.8; 4788 -3.0; 5267 -2.1; 5793 -3.9; 6373 -7.5; 7010 -4.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -14.5; 16529 -19.7; 18182 -18.0; 20000 -15.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado GR8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado GR8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 135 Hz   | 0.89 | -2.0 dB  |
| Peaking | 292 Hz   | 0.52 | -4.3 dB  |
| Peaking | 2997 Hz  | 1.22 | 6.5 dB   |
| Peaking | 13453 Hz | 0.58 | 15.0 dB  |
| Peaking | 16534 Hz | 0.53 | -23.8 dB |
| Peaking | 20 Hz    | 1.36 | 1.0 dB   |
| Peaking | 1332 Hz  | 6.09 | -1.1 dB  |
| Peaking | 4158 Hz  | 9.27 | -4.2 dB  |
| Peaking | 5235 Hz  | 6.08 | 3.4 dB   |
| Peaking | 10224 Hz | 1.75 | -1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB   |
| Peaking | 62 Hz    | 1.41 | -0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -3.5 dB  |
| Peaking | 250 Hz   | 1.41 | -4.6 dB  |
| Peaking | 500 Hz   | 1.41 | -2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 16000 Hz | 1.41 | -12.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Grado%20GR8/Grado%20GR8.png)