# Acoustune HS1501
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.4; 23 -9.6; 25 -9.8; 28 -10.1; 31 -10.3; 34 -10.4; 37 -10.5; 41 -10.6; 45 -10.7; 49 -10.8; 54 -10.9; 60 -11.0; 66 -11.1; 72 -11.3; 79 -11.5; 87 -11.6; 96 -11.8; 106 -11.9; 116 -12.0; 128 -11.9; 141 -11.9; 155 -11.8; 170 -11.6; 187 -11.4; 206 -11.0; 227 -10.7; 249 -10.3; 274 -9.8; 302 -9.3; 332 -8.7; 365 -8.2; 402 -7.7; 442 -7.3; 486 -6.9; 535 -6.4; 588 -6.1; 647 -5.7; 712 -5.3; 783 -5.1; 861 -5.0; 947 -5.0; 1042 -5.4; 1146 -6.3; 1261 -7.2; 1387 -7.7; 1526 -8.0; 1678 -8.2; 1846 -8.2; 2031 -7.8; 2234 -6.5; 2457 -4.3; 2703 -1.8; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -2.5; 5267 -7.0; 5793 -9.2; 6373 -3.7; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -14.9; 15026 -21.9; 16529 -24.2; 18182 -24.4; 20000 -19.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Acoustune HS1501 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Acoustune HS1501 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 44 Hz    | 0.42 | -3.8 dB  |
| Peaking | 131 Hz   | 0.99 | -3.5 dB  |
| Peaking | 237 Hz   | 1.73 | -2.2 dB  |
| Peaking | 3699 Hz  | 1.68 | 7.3 dB   |
| Peaking | 17816 Hz | 0.93 | -20.9 dB |
| Peaking | 1803 Hz  | 3.26 | -3.1 dB  |
| Peaking | 5680 Hz  | 5.4  | -9.9 dB  |
| Peaking | 6128 Hz  | 2.16 | 5.6 dB   |
| Peaking | 12306 Hz | 1.9  | 7.4 dB   |
| Peaking | 14738 Hz | 2.01 | -8.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB  |
| Peaking | 62 Hz    | 1.41 | -3.4 dB  |
| Peaking | 125 Hz   | 1.41 | -4.8 dB  |
| Peaking | 250 Hz   | 1.41 | -3.4 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 16000 Hz | 1.41 | -21.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Acoustune%20HS1501/Acoustune%20HS1501.png)