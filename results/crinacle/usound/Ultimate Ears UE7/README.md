# Ultimate Ears UE7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -3.3; 25 -3.5; 28 -3.8; 31 -4.1; 34 -4.2; 37 -4.4; 41 -4.7; 45 -4.9; 49 -5.0; 54 -5.3; 60 -5.5; 66 -5.9; 72 -6.2; 79 -6.6; 87 -7.0; 96 -7.5; 106 -7.9; 116 -8.2; 128 -8.6; 141 -8.9; 155 -9.2; 170 -9.3; 187 -9.5; 206 -9.5; 227 -9.5; 249 -9.5; 274 -9.4; 302 -9.3; 332 -9.2; 365 -8.9; 402 -8.7; 442 -8.5; 486 -8.2; 535 -7.9; 588 -7.5; 647 -7.1; 712 -6.5; 783 -6.0; 861 -5.5; 947 -5.1; 1042 -5.1; 1146 -5.5; 1261 -5.8; 1387 -5.8; 1526 -5.2; 1678 -4.4; 1846 -3.7; 2031 -3.3; 2234 -3.2; 2457 -2.4; 2703 -1.4; 2973 -1.2; 3270 -1.8; 3597 -1.8; 3957 -0.5; 4353 -0.8; 4788 -3.4; 5267 -3.6; 5793 -2.2; 6373 -3.1; 7010 -4.8; 7711 -5.7; 8482 -6.5; 9330 -6.8; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears UE7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.16 | 2.8 dB  |
| Peaking | 201 Hz  | 0.39 | -4.1 dB |
| Peaking | 899 Hz  | 2.54 | 1.5 dB  |
| Peaking | 2618 Hz | 1.4  | 3.1 dB  |
| Peaking | 4181 Hz | 1.48 | 3.8 dB  |
| Peaking | 1388 Hz | 5.39 | -0.6 dB |
| Peaking | 1792 Hz | 5.31 | 0.6 dB  |
| Peaking | 5002 Hz | 8.94 | -2.0 dB |
| Peaking | 5990 Hz | 5.53 | 2.2 dB  |
| Peaking | 8890 Hz | 4.74 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Ultimate%20Ears%20UE7/Ultimate%20Ears%20UE7.png)