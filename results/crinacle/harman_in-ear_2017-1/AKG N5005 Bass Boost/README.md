# AKG N5005 Bass Boost
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.9; 23 -11.0; 25 -11.1; 28 -11.1; 31 -11.1; 34 -11.0; 37 -10.9; 41 -10.8; 45 -10.7; 49 -10.6; 54 -10.4; 60 -10.2; 66 -10.0; 72 -9.9; 79 -9.7; 87 -9.6; 96 -9.3; 106 -9.2; 116 -9.0; 128 -8.9; 141 -8.9; 155 -8.9; 170 -8.9; 187 -9.0; 206 -8.9; 227 -8.9; 249 -9.0; 274 -9.0; 302 -9.0; 332 -8.8; 365 -8.7; 402 -8.7; 442 -8.5; 486 -8.4; 535 -8.2; 588 -8.0; 647 -7.8; 712 -7.5; 783 -7.2; 861 -7.0; 947 -6.9; 1042 -6.9; 1146 -7.6; 1261 -8.2; 1387 -8.6; 1526 -8.7; 1678 -8.7; 1846 -8.5; 2031 -7.8; 2234 -6.3; 2457 -4.1; 2703 -2.0; 2973 -0.8; 3270 -1.1; 3597 -1.6; 3957 -2.6; 4353 -4.9; 4788 -5.6; 5267 -2.4; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -9.4; 15026 -19.6; 16529 -26.6; 18182 -25.1; 20000 -10.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG N5005 Bass Boost GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG N5005 Bass Boost ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.38 | -4.5 dB  |
| Peaking | 598 Hz   | 0.16 | -2.2 dB  |
| Peaking | 5212 Hz  | 0.55 | 7.0 dB   |
| Peaking | 12765 Hz | 1.81 | 9.9 dB   |
| Peaking | 16903 Hz | 0.69 | -23.7 dB |
| Peaking | 992 Hz   | 0.95 | 4.8 dB   |
| Peaking | 1901 Hz  | 0.49 | -6.4 dB  |
| Peaking | 2936 Hz  | 1.58 | 7.7 dB   |
| Peaking | 4623 Hz  | 4.95 | -4.2 dB  |
| Peaking | 5874 Hz  | 3.95 | 4.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.0 dB  |
| Peaking | 62 Hz    | 1.41 | -2.7 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB  |
| Peaking | 250 Hz   | 1.41 | -2.1 dB  |
| Peaking | 500 Hz   | 1.41 | -1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.0 dB   |
| Peaking | 16000 Hz | 1.41 | -20.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/AKG%20N5005%20Bass%20Boost/AKG%20N5005%20Bass%20Boost.png)