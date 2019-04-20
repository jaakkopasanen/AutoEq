# Periodic Audio Be
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.4; 23 -13.4; 25 -13.3; 28 -13.3; 31 -13.2; 34 -13.1; 37 -13.1; 41 -13.0; 45 -12.9; 49 -12.9; 54 -12.9; 60 -12.9; 66 -12.8; 72 -12.7; 79 -12.7; 87 -12.7; 96 -12.7; 106 -12.7; 116 -12.6; 128 -12.5; 141 -12.2; 155 -11.9; 170 -11.5; 187 -11.1; 206 -10.5; 227 -9.8; 249 -9.6; 274 -10.3; 302 -9.7; 332 -8.8; 365 -8.1; 402 -7.8; 442 -7.4; 486 -6.8; 535 -6.3; 588 -5.8; 647 -5.3; 712 -4.9; 783 -4.6; 861 -4.4; 947 -4.7; 1042 -5.2; 1146 -5.9; 1261 -6.3; 1387 -6.3; 1526 -6.1; 1678 -6.0; 1846 -6.3; 2031 -6.0; 2234 -5.3; 2457 -4.6; 2703 -3.5; 2973 -2.4; 3270 -1.4; 3597 -0.7; 3957 -0.5; 4353 -0.6; 4788 -1.4; 5267 -3.3; 5793 -7.0; 6373 -8.6; 7010 -4.8; 7711 -6.2; 8482 -6.5; 9330 -7.4; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -12.3; 15026 -22.4; 16529 -28.9; 18182 -29.7; 20000 -24.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Periodic Audio Be GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Periodic Audio Be ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.29 | -6.7 dB  |
| Peaking | 135 Hz   | 0.99 | -3.6 dB  |
| Peaking | 286 Hz   | 3.97 | -2.1 dB  |
| Peaking | 4030 Hz  | 1.07 | 6.5 dB   |
| Peaking | 18059 Hz | 1    | -26.7 dB |
| Peaking | 803 Hz   | 2.11 | 2.3 dB   |
| Peaking | 1903 Hz  | 2.11 | -1.2 dB  |
| Peaking | 6097 Hz  | 7.44 | -5.1 dB  |
| Peaking | 12772 Hz | 1.38 | 10.1 dB  |
| Peaking | 15436 Hz | 1.53 | -11.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.9 dB  |
| Peaking | 62 Hz    | 1.41 | -4.5 dB  |
| Peaking | 125 Hz   | 1.41 | -5.0 dB  |
| Peaking | 250 Hz   | 1.41 | -2.9 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 16000 Hz | 1.41 | -25.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Periodic%20Audio%20Be/Periodic%20Audio%20Be.png)