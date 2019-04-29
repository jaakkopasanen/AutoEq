# Ultimate Ears UE6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.1; 23 -12.2; 25 -12.3; 28 -12.3; 31 -12.2; 34 -12.2; 37 -12.1; 41 -12.0; 45 -11.9; 49 -11.9; 54 -11.7; 60 -11.6; 66 -11.6; 72 -11.6; 79 -11.7; 87 -11.7; 96 -11.7; 106 -11.7; 116 -11.7; 128 -11.6; 141 -11.5; 155 -11.4; 170 -11.2; 187 -11.0; 206 -10.7; 227 -10.4; 249 -10.2; 274 -9.9; 302 -9.5; 332 -9.1; 365 -8.7; 402 -8.4; 442 -8.1; 486 -7.8; 535 -7.4; 588 -7.1; 647 -6.7; 712 -6.4; 783 -6.0; 861 -5.7; 947 -5.7; 1042 -6.0; 1146 -6.7; 1261 -6.9; 1387 -6.4; 1526 -5.9; 1678 -5.0; 1846 -4.0; 2031 -2.8; 2234 -1.6; 2457 -0.9; 2703 -1.0; 2973 -2.2; 3270 -3.6; 3597 -1.8; 3957 -0.5; 4353 -1.5; 4788 -4.2; 5267 -5.8; 5793 -4.9; 6373 -2.4; 7010 -4.0; 7711 -6.2; 8482 -8.3; 9330 -8.8; 10263 -6.5; 11289 -6.5; 12418 -6.7; 13660 -18.1; 15026 -30.2; 16529 -34.8; 18182 -34.8; 20000 -29.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears UE6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.32 | -5.4 dB  |
| Peaking | 157 Hz   | 0.5  | -4.0 dB  |
| Peaking | 3782 Hz  | 0.29 | 20.8 dB  |
| Peaking | 12095 Hz | 0.75 | 27.4 dB  |
| Peaking | 15847 Hz | 0.17 | -47.3 dB |
| Peaking | 1448 Hz  | 2.19 | -2.5 dB  |
| Peaking | 3300 Hz  | 3.32 | -7.4 dB  |
| Peaking | 3799 Hz  | 0.99 | 9.8 dB   |
| Peaking | 5348 Hz  | 1.22 | -10.1 dB |
| Peaking | 6495 Hz  | 3.42 | 7.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.9 dB  |
| Peaking | 62 Hz    | 1.41 | -3.6 dB  |
| Peaking | 125 Hz   | 1.41 | -4.2 dB  |
| Peaking | 250 Hz   | 1.41 | -3.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 8.7 dB   |
| Peaking | 16000 Hz | 1.41 | -36.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Ultimate%20Ears%20UE6/Ultimate%20Ears%20UE6.png)