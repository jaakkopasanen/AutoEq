# AKG Y50BT
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.1; 25 -1.7; 28 -2.5; 31 -3.1; 34 -3.7; 37 -4.2; 41 -4.6; 45 -5.0; 49 -5.2; 54 -5.5; 60 -5.7; 66 -5.9; 72 -6.1; 79 -6.3; 87 -6.5; 96 -6.6; 106 -6.6; 116 -6.4; 128 -5.9; 141 -5.0; 155 -3.6; 170 -2.0; 187 -1.4; 206 -2.4; 227 -4.1; 249 -5.3; 274 -6.4; 302 -7.6; 332 -8.5; 365 -8.5; 402 -8.0; 442 -7.5; 486 -7.3; 535 -7.3; 588 -7.4; 647 -7.7; 712 -8.1; 783 -8.6; 861 -9.1; 947 -8.9; 1042 -7.7; 1146 -9.4; 1261 -10.4; 1387 -10.3; 1526 -10.2; 1678 -9.3; 1846 -8.0; 2031 -6.7; 2234 -5.4; 2457 -3.4; 2703 -2.1; 2973 -3.7; 3270 -7.5; 3597 -5.9; 3957 -5.0; 4353 -6.6; 4788 -8.0; 5267 -9.4; 5793 -9.7; 6373 -8.7; 7010 -6.5; 7711 -6.3; 8482 -6.5; 9330 -6.6; 10263 -6.6; 11289 -6.6; 12418 -7.4; 13660 -10.5; 15026 -12.1; 16529 -12.5; 18182 -11.7; 20000 -10.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG Y50BT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG Y50BT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 1.1  | 6.0 dB  |
| Peaking | 185 Hz   | 3.26 | 5.8 dB  |
| Peaking | 1793 Hz  | 0.51 | -4.4 dB |
| Peaking | 2602 Hz  | 2.06 | 8.0 dB  |
| Peaking | 17269 Hz | 0.86 | -6.6 dB |
| Peaking | 342 Hz   | 4.94 | -2.1 dB |
| Peaking | 3940 Hz  | 8.96 | 2.7 dB  |
| Peaking | 5676 Hz  | 3.37 | -3.2 dB |
| Peaking | 8398 Hz  | 1.24 | 1.7 dB  |
| Peaking | 19847 Hz | 2.38 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | 1.5 dB  |
| Peaking | 250 Hz   | 1.41 | 1.9 dB  |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | -3.1 dB |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -7.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/AKG%20Y50BT/AKG%20Y50BT.png)