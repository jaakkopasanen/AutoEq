# Ultimate Ears UE18+ sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -4.0; 25 -4.2; 28 -4.5; 31 -4.8; 34 -5.0; 37 -5.3; 41 -5.6; 45 -5.8; 49 -6.1; 54 -6.4; 60 -6.8; 66 -7.2; 72 -7.6; 79 -8.0; 87 -8.5; 96 -8.9; 106 -9.4; 116 -9.7; 128 -10.0; 141 -10.3; 155 -10.5; 170 -10.7; 187 -10.7; 206 -10.8; 227 -10.8; 249 -10.7; 274 -10.7; 302 -10.6; 332 -10.4; 365 -10.3; 402 -10.2; 442 -10.1; 486 -9.9; 535 -9.6; 588 -9.3; 647 -8.8; 712 -8.1; 783 -7.4; 861 -6.7; 947 -6.3; 1042 -6.4; 1146 -7.1; 1261 -8.0; 1387 -8.3; 1526 -7.9; 1678 -6.8; 1846 -5.5; 2031 -4.4; 2234 -3.7; 2457 -3.3; 2703 -2.9; 2973 -2.2; 3270 -0.9; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.4; 5793 -2.8; 6373 -2.9; 7010 -4.3; 7711 -6.4; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.4; 15026 -14.0; 16529 -17.7; 18182 -14.4; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears UE18+ sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE18+ sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 13 Hz    | 0.31 | 3.1 dB   |
| Peaking | 219 Hz   | 0.41 | -4.6 dB  |
| Peaking | 1452 Hz  | 4.22 | -2.6 dB  |
| Peaking | 3979 Hz  | 0.9  | 6.5 dB   |
| Peaking | 16841 Hz | 1.53 | -12.6 dB |
| Peaking | 544 Hz   | 2.6  | -0.7 dB  |
| Peaking | 915 Hz   | 4.16 | 1.3 dB   |
| Peaking | 8004 Hz  | 5.03 | -1.7 dB  |
| Peaking | 13364 Hz | 2.75 | 2.9 dB   |
| Peaking | 15164 Hz | 3.89 | -3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB   |
| Peaking | 62 Hz    | 1.41 | -0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -3.1 dB  |
| Peaking | 250 Hz   | 1.41 | -3.7 dB  |
| Peaking | 500 Hz   | 1.41 | -2.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 16000 Hz | 1.41 | -10.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Ultimate%20Ears%20UE18+%20sample%202/Ultimate%20Ears%20UE18+%20sample%202.png)