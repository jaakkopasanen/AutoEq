# Ultimate Ears UE18+ sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.6; 23 -2.1; 25 -2.5; 28 -3.0; 31 -3.4; 34 -3.7; 37 -3.9; 41 -4.2; 45 -4.5; 49 -4.8; 54 -5.2; 60 -5.6; 66 -6.0; 72 -6.4; 79 -6.9; 87 -7.4; 96 -7.8; 106 -8.3; 116 -8.7; 128 -9.0; 141 -9.4; 155 -9.7; 170 -9.9; 187 -10.0; 206 -10.1; 227 -10.1; 249 -10.1; 274 -10.1; 302 -10.0; 332 -9.9; 365 -9.9; 402 -9.7; 442 -9.6; 486 -9.4; 535 -9.2; 588 -8.9; 647 -8.5; 712 -8.0; 783 -7.3; 861 -6.6; 947 -6.3; 1042 -6.4; 1146 -7.2; 1261 -8.0; 1387 -8.3; 1526 -7.9; 1678 -6.9; 1846 -5.8; 2031 -5.0; 2234 -4.5; 2457 -4.4; 2703 -4.3; 2973 -3.8; 3270 -3.0; 3597 -2.6; 3957 -2.4; 4353 -2.5; 4788 -1.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.6; 15026 -9.1; 16529 -13.9; 18182 -17.7; 20000 -13.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears UE18+ sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE18+ sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 12 Hz    | 0.29 | 5.3 dB   |
| Peaking | 233 Hz   | 0.46 | -4.0 dB  |
| Peaking | 1417 Hz  | 5.34 | -2.2 dB  |
| Peaking | 4852 Hz  | 0.95 | 5.6 dB   |
| Peaking | 18465 Hz | 1.01 | -12.3 dB |
| Peaking | 931 Hz   | 5.71 | 1.2 dB   |
| Peaking | 4458 Hz  | 4.78 | -2.0 dB  |
| Peaking | 6461 Hz  | 1.78 | 3.7 dB   |
| Peaking | 7635 Hz  | 2.31 | -4.4 dB  |
| Peaking | 13563 Hz | 3.32 | 2.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -2.4 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -7.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Ultimate%20Ears%20UE18+%20sample%201/Ultimate%20Ears%20UE18+%20sample%201.png)