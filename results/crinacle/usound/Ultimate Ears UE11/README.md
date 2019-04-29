# Ultimate Ears UE11
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.3; 23 -8.5; 25 -8.7; 28 -8.9; 31 -9.0; 34 -9.1; 37 -9.3; 41 -9.4; 45 -9.6; 49 -9.7; 54 -9.9; 60 -10.1; 66 -10.3; 72 -10.6; 79 -10.8; 87 -11.1; 96 -11.3; 106 -11.6; 116 -11.7; 128 -11.8; 141 -11.9; 155 -11.9; 170 -11.8; 187 -11.6; 206 -11.3; 227 -11.0; 249 -10.7; 274 -10.2; 302 -9.8; 332 -9.3; 365 -8.8; 402 -8.4; 442 -7.9; 486 -7.3; 535 -6.7; 588 -6.1; 647 -5.5; 712 -4.8; 783 -4.1; 861 -3.5; 947 -3.2; 1042 -3.3; 1146 -3.7; 1261 -4.3; 1387 -4.6; 1526 -4.4; 1678 -3.9; 1846 -3.3; 2031 -3.0; 2234 -3.1; 2457 -2.9; 2703 -2.2; 2973 -2.0; 3270 -2.8; 3597 -2.7; 3957 -0.5; 4353 -1.6; 4788 -4.4; 5267 -3.4; 5793 -2.3; 6373 -4.4; 7010 -3.9; 7711 -5.9; 8482 -8.3; 9330 -7.2; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -7.6; 15026 -6.8; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears UE11 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE11 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.32 | -2.1 dB |
| Peaking | 165 Hz   | 0.5  | -5.0 dB |
| Peaking | 899 Hz   | 1.43 | 3.3 dB  |
| Peaking | 2379 Hz  | 1.33 | 2.6 dB  |
| Peaking | 4152 Hz  | 1.59 | 3.8 dB  |
| Peaking | 4919 Hz  | 6.5  | -3.8 dB |
| Peaking | 5475 Hz  | 2.2  | 2.4 dB  |
| Peaking | 8655 Hz  | 5.72 | -3.4 dB |
| Peaking | 14009 Hz | 6.15 | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.4 dB |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Ultimate%20Ears%20UE11/Ultimate%20Ears%20UE11.png)