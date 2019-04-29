# NuForce Primo8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -3.3; 25 -3.6; 28 -4.0; 31 -4.2; 34 -4.4; 37 -4.6; 41 -4.7; 45 -4.9; 49 -5.2; 54 -5.5; 60 -5.7; 66 -6.0; 72 -6.3; 79 -6.7; 87 -7.2; 96 -7.5; 106 -7.9; 116 -8.4; 128 -8.7; 141 -9.0; 155 -9.1; 170 -9.3; 187 -9.5; 206 -9.9; 227 -9.9; 249 -9.9; 274 -10.1; 302 -10.0; 332 -9.8; 365 -9.7; 402 -9.6; 442 -9.5; 486 -9.3; 535 -9.2; 588 -9.0; 647 -8.8; 712 -8.5; 783 -8.2; 861 -8.0; 947 -8.2; 1042 -8.7; 1146 -9.4; 1261 -10.2; 1387 -10.6; 1526 -10.6; 1678 -10.6; 1846 -10.4; 2031 -9.9; 2234 -8.0; 2457 -5.0; 2703 -2.6; 2973 -1.5; 3270 -2.2; 3597 -3.5; 3957 -2.9; 4353 -0.6; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.9; 7010 -4.5; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -12.8; 18182 -20.3; 20000 -20.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NuForce Primo8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NuForce Primo8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.36 | 3.5 dB   |
| Peaking | 581 Hz   | 0.1  | -3.4 dB  |
| Peaking | 2921 Hz  | 3.88 | 6.3 dB   |
| Peaking | 5084 Hz  | 1.5  | 8.5 dB   |
| Peaking | 19071 Hz | 1.18 | -17.0 dB |
| Peaking | 854 Hz   | 1.78 | 2.1 dB   |
| Peaking | 1707 Hz  | 1.56 | -2.3 dB  |
| Peaking | 2514 Hz  | 6.61 | 2.1 dB   |
| Peaking | 7841 Hz  | 6.56 | -1.2 dB  |
| Peaking | 14455 Hz | 2.69 | 3.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | -1.8 dB |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -6.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/NuForce%20Primo8/NuForce%20Primo8.png)