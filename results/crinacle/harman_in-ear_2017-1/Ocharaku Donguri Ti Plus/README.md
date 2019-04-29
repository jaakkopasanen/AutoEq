# Ocharaku Donguri Ti Plus
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.7; 23 -6.3; 25 -6.8; 28 -7.4; 31 -7.7; 34 -7.9; 37 -8.1; 41 -8.4; 45 -8.6; 49 -8.8; 54 -9.0; 60 -9.1; 66 -9.3; 72 -9.7; 79 -10.1; 87 -10.5; 96 -10.7; 106 -10.9; 116 -11.1; 128 -11.1; 141 -11.2; 155 -11.3; 170 -11.2; 187 -11.0; 206 -10.7; 227 -10.3; 249 -9.9; 274 -9.6; 302 -9.1; 332 -8.5; 365 -8.0; 402 -7.6; 442 -7.2; 486 -6.8; 535 -6.3; 588 -5.9; 647 -5.5; 712 -5.0; 783 -4.7; 861 -4.6; 947 -4.9; 1042 -5.5; 1146 -6.4; 1261 -7.5; 1387 -8.5; 1526 -9.7; 1678 -8.9; 1846 -9.3; 2031 -10.0; 2234 -9.0; 2457 -9.9; 2703 -7.2; 2973 -4.8; 3270 -3.8; 3597 -4.1; 3957 -7.5; 4353 -11.0; 4788 -5.9; 5267 -0.6; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.7; 13660 -16.5; 15026 -20.2; 16529 -14.1; 18182 -11.3; 20000 -21.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ocharaku Donguri Ti Plus GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ocharaku Donguri Ti Plus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 128 Hz   | 0.64 | -5.1 dB  |
| Peaking | 3499 Hz  | 3.05 | 10.1 dB  |
| Peaking | 4305 Hz  | 1.17 | -20.3 dB |
| Peaking | 5376 Hz  | 1.28 | 19.4 dB  |
| Peaking | 15189 Hz | 1.74 | -14.6 dB |
| Peaking | 40 Hz    | 2.16 | -0.8 dB  |
| Peaking | 868 Hz   | 1.51 | 3.2 dB   |
| Peaking | 1613 Hz  | 1.66 | -2.2 dB  |
| Peaking | 7791 Hz  | 6.28 | -1.8 dB  |
| Peaking | 11976 Hz | 5.2  | 4.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.6 dB  |
| Peaking | 62 Hz    | 1.41 | -2.2 dB  |
| Peaking | 125 Hz   | 1.41 | -4.3 dB  |
| Peaking | 250 Hz   | 1.41 | -3.3 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 16000 Hz | 1.41 | -14.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Ocharaku%20Donguri%20Ti%20Plus/Ocharaku%20Donguri%20Ti%20Plus.png)