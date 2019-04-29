# Custom Art FIBAE 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.1; 23 -7.2; 25 -7.3; 28 -7.4; 31 -7.5; 34 -7.6; 37 -7.8; 41 -7.9; 45 -8.1; 49 -8.2; 54 -8.4; 60 -8.7; 66 -8.9; 72 -9.3; 79 -9.6; 87 -10.0; 96 -10.4; 106 -10.8; 116 -11.1; 128 -11.4; 141 -11.7; 155 -11.9; 170 -12.0; 187 -12.2; 206 -12.2; 227 -12.1; 249 -12.1; 274 -12.0; 302 -11.7; 332 -11.4; 365 -11.1; 402 -10.8; 442 -10.5; 486 -10.1; 535 -9.7; 588 -9.2; 647 -8.7; 712 -8.0; 783 -7.3; 861 -6.7; 947 -6.2; 1042 -6.1; 1146 -6.0; 1261 -5.9; 1387 -5.3; 1526 -4.5; 1678 -3.7; 1846 -3.3; 2031 -3.6; 2234 -4.8; 2457 -7.5; 2703 -9.0; 2973 -7.2; 3270 -3.0; 3597 -2.2; 3957 -6.2; 4353 -4.4; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -10.0; 9330 -9.0; 10263 -7.1; 11289 -7.5; 12418 -7.0; 13660 -9.6; 15026 -19.6; 16529 -28.0; 18182 -30.7; 20000 -33.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Custom Art FIBAE 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Custom Art FIBAE 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 201 Hz   | 0.43 | -5.8 dB  |
| Peaking | 1664 Hz  | 1.36 | 4.6 dB   |
| Peaking | 5647 Hz  | 0.98 | 15.7 dB  |
| Peaking | 12721 Hz | 1.15 | 19.4 dB  |
| Peaking | 18364 Hz | 0.15 | -29.2 dB |
| Peaking | 912 Hz   | 3.81 | 1.3 dB   |
| Peaking | 2137 Hz  | 3.07 | 4.3 dB   |
| Peaking | 2612 Hz  | 1.62 | -4.8 dB  |
| Peaking | 3381 Hz  | 6.11 | 6.5 dB   |
| Peaking | 22049 Hz | 2.87 | 0.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -4.1 dB  |
| Peaking | 250 Hz   | 1.41 | -4.9 dB  |
| Peaking | 500 Hz   | 1.41 | -3.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.8 dB   |
| Peaking | 16000 Hz | 1.41 | -25.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Custom%20Art%20FIBAE%203/Custom%20Art%20FIBAE%203.png)