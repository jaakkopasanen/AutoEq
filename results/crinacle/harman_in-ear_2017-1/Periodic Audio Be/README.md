# Periodic Audio Be
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.4; 23 -8.8; 25 -9.2; 28 -9.6; 31 -9.9; 34 -10.2; 37 -10.4; 41 -10.6; 45 -10.8; 49 -11.0; 54 -11.2; 60 -11.4; 66 -11.6; 72 -11.8; 79 -12.0; 87 -12.2; 96 -12.4; 106 -12.5; 116 -12.6; 128 -12.6; 141 -12.6; 155 -12.5; 170 -12.3; 187 -12.1; 206 -11.8; 227 -11.4; 249 -11.0; 274 -10.5; 302 -9.9; 332 -9.3; 365 -8.7; 402 -8.2; 442 -7.7; 486 -7.1; 535 -6.5; 588 -5.9; 647 -5.4; 712 -4.8; 783 -4.3; 861 -3.9; 947 -3.7; 1042 -3.8; 1146 -4.1; 1261 -4.4; 1387 -4.7; 1526 -4.9; 1678 -5.6; 1846 -6.1; 2031 -5.5; 2234 -4.7; 2457 -3.8; 2703 -2.8; 2973 -1.7; 3270 -0.7; 3597 -0.5; 3957 -1.0; 4353 -2.4; 4788 -5.2; 5267 -8.5; 5793 -6.8; 6373 -2.6; 7010 -4.0; 7711 -6.2; 8482 -6.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -15.7; 15026 -28.5; 16529 -33.4; 18182 -30.9; 20000 -20.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Periodic Audio Be GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Periodic Audio Be ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 63 Hz    | 0.36 | -3.9 dB  |
| Peaking | 179 Hz   | 0.6  | -3.7 dB  |
| Peaking | 834 Hz   | 1.68 | 2.2 dB   |
| Peaking | 9882 Hz  | 0.24 | 22.5 dB  |
| Peaking | 16642 Hz | 0.38 | -44.1 dB |
| Peaking | 3588 Hz  | 2.74 | 4.2 dB   |
| Peaking | 5320 Hz  | 6.56 | -6.0 dB  |
| Peaking | 8501 Hz  | 3.95 | -2.7 dB  |
| Peaking | 12645 Hz | 3.09 | 7.6 dB   |
| Peaking | 14800 Hz | 3.27 | -6.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.9 dB  |
| Peaking | 62 Hz    | 1.41 | -3.9 dB  |
| Peaking | 125 Hz   | 1.41 | -5.3 dB  |
| Peaking | 250 Hz   | 1.41 | -4.0 dB  |
| Peaking | 500 Hz   | 1.41 | 0.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 6.7 dB   |
| Peaking | 16000 Hz | 1.41 | -31.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Periodic%20Audio%20Be/Periodic%20Audio%20Be.png)