# Ultimate Ears UE18+ sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.9; 23 -5.1; 25 -5.3; 28 -5.6; 31 -5.9; 34 -6.2; 37 -6.4; 41 -6.7; 45 -7.0; 49 -7.2; 54 -7.5; 60 -8.0; 66 -8.4; 72 -8.8; 79 -9.2; 87 -9.6; 96 -10.1; 106 -10.5; 116 -10.8; 128 -11.2; 141 -11.5; 155 -11.7; 170 -11.8; 187 -11.9; 206 -11.9; 227 -12.0; 249 -11.9; 274 -11.8; 302 -11.7; 332 -11.4; 365 -11.2; 402 -11.0; 442 -10.9; 486 -10.6; 535 -10.3; 588 -9.9; 647 -9.5; 712 -8.8; 783 -8.1; 861 -7.4; 947 -7.1; 1042 -7.3; 1146 -7.8; 1261 -8.4; 1387 -8.5; 1526 -7.8; 1678 -6.7; 1846 -5.3; 2031 -3.9; 2234 -2.6; 2457 -1.6; 2703 -0.8; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.6; 5793 -1.7; 6373 -1.5; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -15.9; 15026 -30.4; 16529 -36.5; 18182 -30.8; 20000 -12.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears UE18+ sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE18+ sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 13 Hz    | 0.2  | 2.0 dB   |
| Peaking | 237 Hz   | 0.29 | -5.9 dB  |
| Peaking | 1454 Hz  | 2.07 | -4.9 dB  |
| Peaking | 7957 Hz  | 0.23 | 16.5 dB  |
| Peaking | 16561 Hz | 0.7  | -42.4 dB |
| Peaking | 581 Hz   | 4.56 | -0.5 dB  |
| Peaking | 1844 Hz  | 4.11 | -0.4 dB  |
| Peaking | 7979 Hz  | 3.44 | -3.6 dB  |
| Peaking | 12735 Hz | 2.42 | 9.8 dB   |
| Peaking | 14848 Hz | 2.47 | -9.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.3 dB   |
| Peaking | 62 Hz    | 1.41 | -1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -4.0 dB  |
| Peaking | 250 Hz   | 1.41 | -4.7 dB  |
| Peaking | 500 Hz   | 1.41 | -3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 7.7 dB   |
| Peaking | 16000 Hz | 1.41 | -32.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Ultimate%20Ears%20UE18+%20sample%202/Ultimate%20Ears%20UE18+%20sample%202.png)