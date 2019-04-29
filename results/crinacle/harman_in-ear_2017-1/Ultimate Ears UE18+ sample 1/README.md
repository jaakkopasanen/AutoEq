# Ultimate Ears UE18+ sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.7; 23 -3.2; 25 -3.7; 28 -4.2; 31 -4.5; 34 -4.8; 37 -5.0; 41 -5.4; 45 -5.7; 49 -5.9; 54 -6.3; 60 -6.8; 66 -7.2; 72 -7.6; 79 -8.0; 87 -8.5; 96 -9.0; 106 -9.4; 116 -9.9; 128 -10.2; 141 -10.6; 155 -10.9; 170 -11.0; 187 -11.1; 206 -11.2; 227 -11.3; 249 -11.2; 274 -11.2; 302 -11.1; 332 -10.9; 365 -10.7; 402 -10.6; 442 -10.4; 486 -10.2; 535 -9.9; 588 -9.6; 647 -9.2; 712 -8.6; 783 -8.0; 861 -7.4; 947 -7.1; 1042 -7.3; 1146 -7.9; 1261 -8.5; 1387 -8.5; 1526 -7.8; 1678 -6.8; 1846 -5.6; 2031 -4.4; 2234 -3.4; 2457 -2.7; 2703 -2.2; 2973 -1.5; 3270 -0.8; 3597 -0.6; 3957 -0.8; 4353 -1.4; 4788 -0.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.8; 13660 -15.0; 15026 -25.5; 16529 -32.8; 18182 -34.2; 20000 -24.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears UE18+ sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE18+ sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 426 Hz   | 0.18 | -5.5 dB  |
| Peaking | 776 Hz   | 2.25 | 2.0 dB   |
| Peaking | 7715 Hz  | 0.26 | 16.6 dB  |
| Peaking | 17439 Hz | 0.45 | -37.6 dB |
| Peaking | 17 Hz    | 0.86 | 4.4 dB   |
| Peaking | 52 Hz    | 0.81 | 1.5 dB   |
| Peaking | 7999 Hz  | 4.17 | -3.9 dB  |
| Peaking | 12440 Hz | 2.68 | 7.0 dB   |
| Peaking | 15233 Hz | 2.56 | -5.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 2.9 dB   |
| Peaking | 62 Hz    | 1.41 | -0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -3.2 dB  |
| Peaking | 250 Hz   | 1.41 | -4.2 dB  |
| Peaking | 500 Hz   | 1.41 | -2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 7.7 dB   |
| Peaking | 16000 Hz | 1.41 | -31.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Ultimate%20Ears%20UE18+%20sample%201/Ultimate%20Ears%20UE18+%20sample%201.png)