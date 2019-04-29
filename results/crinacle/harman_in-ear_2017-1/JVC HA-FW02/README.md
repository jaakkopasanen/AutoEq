# JVC HA-FW02
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.5; 23 -4.1; 25 -4.6; 28 -5.3; 31 -5.8; 34 -6.3; 37 -6.7; 41 -7.1; 45 -7.5; 49 -7.8; 54 -8.2; 60 -8.6; 66 -9.0; 72 -9.4; 79 -9.8; 87 -10.2; 96 -10.6; 106 -10.9; 116 -11.1; 128 -11.3; 141 -11.4; 155 -11.6; 170 -11.4; 187 -11.4; 206 -11.2; 227 -10.9; 249 -10.6; 274 -10.3; 302 -9.8; 332 -9.2; 365 -8.6; 402 -8.1; 442 -7.5; 486 -7.0; 535 -6.5; 588 -5.9; 647 -5.3; 712 -4.7; 783 -4.1; 861 -3.5; 947 -2.9; 1042 -3.2; 1146 -3.5; 1261 -4.1; 1387 -3.8; 1526 -2.6; 1678 -3.0; 1846 -3.1; 2031 -3.1; 2234 -3.2; 2457 -3.9; 2703 -4.8; 2973 -5.1; 3270 -4.7; 3597 -4.4; 3957 -4.8; 4353 -6.1; 4788 -7.0; 5267 -5.4; 5793 -2.2; 6373 -0.5; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -6.0; 13660 -12.5; 15026 -17.2; 16529 -19.9; 18182 -20.9; 20000 -14.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JVC HA-FW02 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JVC HA-FW02 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 159 Hz   | 0.51 | -5.8 dB  |
| Peaking | 896 Hz   | 1.36 | 3.1 dB   |
| Peaking | 1830 Hz  | 1.77 | 2.6 dB   |
| Peaking | 11145 Hz | 0.49 | 10.2 dB  |
| Peaking | 16897 Hz | 0.43 | -20.2 dB |
| Peaking | 21 Hz    | 2.03 | 2.8 dB   |
| Peaking | 4887 Hz  | 4.9  | -3.2 dB  |
| Peaking | 6328 Hz  | 3.39 | 6.1 dB   |
| Peaking | 7727 Hz  | 1.71 | -2.9 dB  |
| Peaking | 12373 Hz | 6.69 | 3.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB   |
| Peaking | 62 Hz    | 1.41 | -2.5 dB  |
| Peaking | 125 Hz   | 1.41 | -4.8 dB  |
| Peaking | 250 Hz   | 1.41 | -4.3 dB  |
| Peaking | 500 Hz   | 1.41 | -0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 4000 Hz  | 1.41 | -0.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 3.8 dB   |
| Peaking | 16000 Hz | 1.41 | -17.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/JVC%20HA-FW02/JVC%20HA-FW02.png)