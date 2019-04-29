# Ultimate Ears UE18+
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.4; 23 -2.8; 25 -3.1; 28 -3.5; 31 -3.8; 34 -4.1; 37 -4.3; 41 -4.6; 45 -4.9; 49 -5.2; 54 -5.5; 60 -6.0; 66 -6.4; 72 -6.8; 79 -7.2; 87 -7.7; 96 -8.1; 106 -8.6; 116 -8.9; 128 -9.3; 141 -9.6; 155 -9.9; 170 -10.0; 187 -10.1; 206 -10.2; 227 -10.2; 249 -10.2; 274 -10.1; 302 -10.0; 332 -9.9; 365 -9.8; 402 -9.7; 442 -9.6; 486 -9.4; 535 -9.2; 588 -8.9; 647 -8.4; 712 -7.8; 783 -7.1; 861 -6.4; 947 -6.0; 1042 -6.2; 1146 -6.9; 1261 -7.7; 1387 -8.1; 1526 -7.6; 1678 -6.6; 1846 -5.4; 2031 -4.5; 2234 -3.9; 2457 -3.6; 2703 -3.4; 2973 -2.8; 3270 -1.7; 3597 -1.1; 3957 -1.1; 4353 -1.3; 4788 -0.7; 5267 -0.5; 5793 -1.1; 6373 -1.2; 7010 -3.7; 7711 -5.9; 8482 -6.2; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.7; 15026 -11.3; 16529 -15.5; 18182 -15.8; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears UE18+ GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE18+ ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 13 Hz    | 0.32 | 4.2 dB   |
| Peaking | 225 Hz   | 0.43 | -4.3 dB  |
| Peaking | 1439 Hz  | 4.49 | -2.5 dB  |
| Peaking | 4386 Hz  | 0.84 | 5.9 dB   |
| Peaking | 17527 Hz | 1.2  | -11.4 dB |
| Peaking | 928 Hz   | 5.47 | 1.2 dB   |
| Peaking | 6516 Hz  | 3.45 | 3.4 dB   |
| Peaking | 7419 Hz  | 3.43 | -0.4 dB  |
| Peaking | 7482 Hz  | 2.19 | -2.8 dB  |
| Peaking | 13091 Hz | 4.04 | 2.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.2 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -2.5 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -9.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Ultimate%20Ears%20UE18+/Ultimate%20Ears%20UE18+.png)