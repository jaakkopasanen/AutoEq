# Koss ESP950
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.7; 79 -2.7; 87 -3.0; 96 -3.1; 106 -3.2; 116 -2.9; 128 -3.0; 141 -3.4; 155 -3.8; 170 -4.1; 187 -4.2; 206 -4.2; 227 -4.3; 249 -4.3; 274 -4.2; 302 -4.0; 332 -3.7; 365 -3.6; 402 -3.5; 442 -3.8; 486 -4.0; 535 -4.2; 588 -4.3; 647 -4.2; 712 -4.2; 783 -5.0; 861 -6.0; 947 -6.4; 1042 -6.6; 1146 -6.8; 1261 -7.3; 1387 -6.7; 1526 -5.1; 1678 -3.6; 1846 -0.7; 2031 -0.5; 2234 -0.5; 2457 -0.8; 2703 -2.8; 2973 -3.8; 3270 -3.1; 3597 -1.4; 3957 -0.6; 4353 -0.7; 4788 -0.5; 5267 -0.7; 5793 -2.6; 6373 -2.4; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss ESP950 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss ESP950 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.4  | 4.7 dB  |
| Peaking | 48 Hz   | 0.19 | 1.7 dB  |
| Peaking | 426 Hz  | 1.22 | 2.4 dB  |
| Peaking | 2118 Hz | 2.88 | 6.0 dB  |
| Peaking | 4589 Hz | 1.53 | 6.3 dB  |
| Peaking | 70 Hz   | 6.72 | 0.7 dB  |
| Peaking | 696 Hz  | 5.84 | 1.2 dB  |
| Peaking | 1230 Hz | 3.72 | -2.0 dB |
| Peaking | 6672 Hz | 7.9  | 2.7 dB  |
| Peaking | 8044 Hz | 2.18 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB  |
| Peaking | 62 Hz    | 1.41 | 4.4 dB  |
| Peaking | 125 Hz   | 1.41 | 1.9 dB  |
| Peaking | 250 Hz   | 1.41 | 1.4 dB  |
| Peaking | 500 Hz   | 1.41 | 3.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.0 dB |
| Peaking | 2000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Koss%20ESP950/Koss%20ESP950.png)