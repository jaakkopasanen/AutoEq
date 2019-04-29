# Ultimate Ears UE18+
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.8; 23 -4.2; 25 -4.5; 28 -4.9; 31 -5.2; 34 -5.5; 37 -5.7; 41 -6.0; 45 -6.3; 49 -6.6; 54 -6.9; 60 -7.4; 66 -7.8; 72 -8.2; 79 -8.6; 87 -9.1; 96 -9.5; 106 -10.0; 116 -10.3; 128 -10.7; 141 -11.0; 155 -11.3; 170 -11.4; 187 -11.5; 206 -11.6; 227 -11.6; 249 -11.6; 274 -11.5; 302 -11.4; 332 -11.1; 365 -11.0; 402 -10.8; 442 -10.7; 486 -10.4; 535 -10.1; 588 -9.8; 647 -9.3; 712 -8.7; 783 -8.0; 861 -7.4; 947 -7.1; 1042 -7.3; 1146 -7.9; 1261 -8.5; 1387 -8.5; 1526 -7.8; 1678 -6.7; 1846 -5.5; 2031 -4.2; 2234 -3.0; 2457 -2.1; 2703 -1.5; 2973 -0.8; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -15.4; 15026 -27.9; 16529 -34.7; 18182 -32.5; 20000 -18.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears UE18+ GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE18+ ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 14 Hz    | 0.21 | 3.1 dB   |
| Peaking | 381 Hz   | 0.17 | -5.8 dB  |
| Peaking | 784 Hz   | 2.36 | 2.0 dB   |
| Peaking | 7484 Hz  | 0.26 | 15.8 dB  |
| Peaking | 16957 Hz | 0.6  | -38.5 dB |
| Peaking | 1494 Hz  | 1.94 | -3.6 dB  |
| Peaking | 1997 Hz  | 0.48 | 1.6 dB   |
| Peaking | 7942 Hz  | 3.17 | -4.1 dB  |
| Peaking | 12569 Hz | 2.67 | 8.2 dB   |
| Peaking | 15048 Hz | 2.74 | -7.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 2.1 dB   |
| Peaking | 62 Hz    | 1.41 | -0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -3.6 dB  |
| Peaking | 250 Hz   | 1.41 | -4.5 dB  |
| Peaking | 500 Hz   | 1.41 | -2.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 7.8 dB   |
| Peaking | 16000 Hz | 1.41 | -31.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Ultimate%20Ears%20UE18+/Ultimate%20Ears%20UE18+.png)