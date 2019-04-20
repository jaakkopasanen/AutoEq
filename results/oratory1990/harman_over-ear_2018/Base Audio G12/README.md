# Base Audio G12
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.7; 25 -2.7; 28 -4.0; 31 -5.0; 34 -5.9; 37 -6.6; 41 -7.3; 45 -7.8; 49 -8.2; 54 -8.5; 60 -8.7; 66 -8.7; 72 -8.8; 79 -8.9; 87 -8.9; 96 -9.0; 106 -9.0; 116 -9.0; 128 -9.0; 141 -8.9; 155 -8.8; 170 -8.6; 187 -8.4; 206 -8.2; 227 -7.8; 249 -8.6; 274 -8.3; 302 -7.2; 332 -6.7; 365 -6.2; 402 -5.9; 442 -5.7; 486 -5.7; 535 -5.5; 588 -5.3; 647 -5.1; 712 -5.1; 783 -5.1; 861 -5.2; 947 -5.5; 1042 -5.8; 1146 -6.1; 1261 -6.5; 1387 -6.8; 1526 -7.1; 1678 -7.1; 1846 -6.7; 2031 -6.2; 2234 -5.9; 2457 -6.0; 2703 -5.7; 2973 -5.5; 3270 -6.4; 3597 -3.4; 3957 -5.3; 4353 -12.2; 4788 -13.2; 5267 -11.0; 5793 -10.9; 6373 -13.0; 7010 -13.4; 7711 -9.4; 8482 -6.9; 9330 -6.9; 10263 -6.9; 11289 -6.9; 12418 -6.9; 13660 -6.9; 15026 -6.9; 16529 -6.9; 18182 -6.9; 20000 -8.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Base Audio G12 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Base Audio G12 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 20 Hz   | 1.72 | 7.0 dB   |
| Peaking | 87 Hz   | 0.67 | -2.5 dB  |
| Peaking | 3913 Hz | 2.19 | 7.9 dB   |
| Peaking | 4528 Hz | 3.24 | -11.8 dB |
| Peaking | 6719 Hz | 4.3  | -6.9 dB  |
| Peaking | 25 Hz   | 1.43 | 0.7 dB   |
| Peaking | 257 Hz  | 6.83 | -1.6 dB  |
| Peaking | 606 Hz  | 0.33 | -1.6 dB  |
| Peaking | 635 Hz  | 0.65 | 3.6 dB   |
| Peaking | 8367 Hz | 7.78 | 1.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.2 dB  |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.3 dB |
| Peaking | 8000 Hz  | 1.41 | -3.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Base%20Audio%20G12/Base%20Audio%20G12.png)