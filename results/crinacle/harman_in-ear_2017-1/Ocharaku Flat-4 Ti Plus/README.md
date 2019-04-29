# Ocharaku Flat-4 Ti Plus
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -6.9; 25 -7.2; 28 -7.4; 31 -7.6; 34 -7.8; 37 -8.0; 41 -8.2; 45 -8.4; 49 -8.4; 54 -8.3; 60 -8.4; 66 -8.6; 72 -8.8; 79 -8.9; 87 -9.2; 96 -9.8; 106 -9.7; 116 -9.8; 128 -9.8; 141 -10.0; 155 -10.3; 170 -9.9; 187 -9.7; 206 -9.6; 227 -9.6; 249 -9.1; 274 -8.7; 302 -8.4; 332 -8.1; 365 -7.8; 402 -7.6; 442 -7.3; 486 -7.3; 535 -7.1; 588 -6.9; 647 -6.8; 712 -6.7; 783 -6.8; 861 -7.0; 947 -7.4; 1042 -7.9; 1146 -8.6; 1261 -8.4; 1387 -6.9; 1526 -4.0; 1678 -0.6; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -2.4; 2973 -6.7; 3270 -5.6; 3597 -2.4; 3957 -1.5; 4353 -2.6; 4788 -6.6; 5267 -9.5; 5793 -0.5; 6373 -2.7; 7010 -13.9; 7711 -18.6; 8482 -13.5; 9330 -7.1; 10263 -6.5; 11289 -6.5; 12418 -9.1; 13660 -15.6; 15026 -20.7; 16529 -24.2; 18182 -28.3; 20000 -28.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ocharaku Flat-4 Ti Plus GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ocharaku Flat-4 Ti Plus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 2111 Hz  | 0.23 | 27.6 dB  |
| Peaking | 6361 Hz  | 1.26 | 26.1 dB  |
| Peaking | 7327 Hz  | 1.78 | -26.6 dB |
| Peaking | 9850 Hz  | 0.03 | -27.3 dB |
| Peaking | 11087 Hz | 1.12 | 17.9 dB  |
| Peaking | 537 Hz   | 1.57 | 1.7 dB   |
| Peaking | 1235 Hz  | 3.2  | -4.8 dB  |
| Peaking | 3059 Hz  | 3.84 | -10.4 dB |
| Peaking | 3200 Hz  | 1.14 | 6.5 dB   |
| Peaking | 5086 Hz  | 9.23 | -9.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -3.1 dB  |
| Peaking | 250 Hz   | 1.41 | -2.4 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB   |
| Peaking | 1000 Hz  | 1.41 | -2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 8000 Hz  | 1.41 | -2.8 dB  |
| Peaking | 16000 Hz | 1.41 | -21.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Ocharaku%20Flat-4%20Ti%20Plus/Ocharaku%20Flat-4%20Ti%20Plus.png)