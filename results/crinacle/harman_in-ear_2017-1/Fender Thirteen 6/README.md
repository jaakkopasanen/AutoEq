# Fender Thirteen 6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.3; 23 -3.5; 25 -3.7; 28 -4.0; 31 -4.1; 34 -4.3; 37 -4.5; 41 -4.8; 45 -5.0; 49 -5.2; 54 -5.4; 60 -5.7; 66 -6.1; 72 -6.4; 79 -6.9; 87 -7.3; 96 -7.8; 106 -8.4; 116 -8.9; 128 -9.3; 141 -9.7; 155 -10.0; 170 -10.4; 187 -10.6; 206 -10.9; 227 -11.0; 249 -11.1; 274 -11.2; 302 -11.3; 332 -11.2; 365 -11.1; 402 -11.1; 442 -11.2; 486 -11.2; 535 -11.3; 588 -11.4; 647 -11.5; 712 -11.4; 783 -11.3; 861 -10.9; 947 -10.5; 1042 -10.2; 1146 -10.3; 1261 -10.4; 1387 -10.1; 1526 -9.5; 1678 -9.0; 1846 -8.7; 2031 -8.2; 2234 -6.2; 2457 -2.9; 2703 -0.6; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.4; 15026 -15.5; 16529 -18.1; 18182 -15.0; 20000 -9.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fender Thirteen 6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fender Thirteen 6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 19 Hz    | 0.21 | 3.2 dB   |
| Peaking | 459 Hz   | 0.19 | -5.5 dB  |
| Peaking | 1845 Hz  | 1.12 | -5.8 dB  |
| Peaking | 3110 Hz  | 0.6  | 10.6 dB  |
| Peaking | 16897 Hz | 1.19 | -12.7 dB |
| Peaking | 2694 Hz  | 5.32 | 2.5 dB   |
| Peaking | 3234 Hz  | 1.21 | -1.2 dB  |
| Peaking | 6307 Hz  | 2.36 | 3.7 dB   |
| Peaking | 7606 Hz  | 2.47 | -3.8 dB  |
| Peaking | 13057 Hz | 4.68 | 3.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 2.9 dB   |
| Peaking | 62 Hz    | 1.41 | 0.8 dB   |
| Peaking | 125 Hz   | 1.41 | -2.3 dB  |
| Peaking | 250 Hz   | 1.41 | -3.9 dB  |
| Peaking | 500 Hz   | 1.41 | -3.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -4.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 16000 Hz | 1.41 | -11.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Fender%20Thirteen%206/Fender%20Thirteen%206.png)