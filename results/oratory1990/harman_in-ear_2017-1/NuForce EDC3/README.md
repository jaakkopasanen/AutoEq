# NuForce EDC3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.2; 23 -2.4; 25 -2.5; 28 -2.6; 31 -2.8; 34 -2.9; 37 -3.0; 41 -3.2; 45 -3.3; 49 -3.5; 54 -3.8; 60 -4.0; 66 -4.3; 72 -4.6; 79 -4.9; 87 -5.3; 96 -5.7; 106 -6.1; 116 -6.5; 128 -6.7; 141 -7.0; 155 -7.1; 170 -7.2; 187 -7.3; 206 -7.4; 227 -7.9; 249 -8.4; 274 -8.6; 302 -8.5; 332 -8.2; 365 -7.9; 402 -7.9; 442 -7.8; 486 -7.7; 535 -7.5; 588 -7.1; 647 -6.9; 712 -6.6; 783 -6.2; 861 -6.1; 947 -6.3; 1042 -6.7; 1146 -7.2; 1261 -7.8; 1387 -7.9; 1526 -7.4; 1678 -6.4; 1846 -5.3; 2031 -3.8; 2234 -2.2; 2457 -0.7; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -12.2; 16529 -17.3; 18182 -16.6; 20000 -12.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NuForce EDC3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NuForce EDC3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 0.48 | 4.2 dB   |
| Peaking | 65 Hz    | 0.84 | 2.0 dB   |
| Peaking | 375 Hz   | 0.1  | -1.7 dB  |
| Peaking | 3826 Hz  | 0.72 | 7.8 dB   |
| Peaking | 17735 Hz | 1.03 | -12.3 dB |
| Peaking | 1476 Hz  | 3.81 | -2.1 dB  |
| Peaking | 2468 Hz  | 4.25 | 2.2 dB   |
| Peaking | 6175 Hz  | 2.68 | 6.2 dB   |
| Peaking | 6663 Hz  | 1.31 | -4.5 dB  |
| Peaking | 13245 Hz | 3.29 | 3.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB   |
| Peaking | 62 Hz    | 1.41 | 1.8 dB   |
| Peaking | 125 Hz   | 1.41 | -0.2 dB  |
| Peaking | 250 Hz   | 1.41 | -1.9 dB  |
| Peaking | 500 Hz   | 1.41 | -0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 16000 Hz | 1.41 | -10.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/NuForce%20EDC3/NuForce%20EDC3.png)