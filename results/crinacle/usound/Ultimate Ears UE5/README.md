# Ultimate Ears UE5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.3; 23 -5.5; 25 -5.7; 28 -5.9; 31 -6.1; 34 -6.3; 37 -6.4; 41 -6.6; 45 -6.8; 49 -6.9; 54 -7.1; 60 -7.4; 66 -7.7; 72 -8.0; 79 -8.4; 87 -8.7; 96 -9.2; 106 -9.5; 116 -9.9; 128 -10.1; 141 -10.4; 155 -10.7; 170 -10.7; 187 -10.8; 206 -10.8; 227 -10.7; 249 -10.6; 274 -10.4; 302 -10.2; 332 -9.9; 365 -9.6; 402 -9.3; 442 -8.9; 486 -8.6; 535 -8.2; 588 -7.7; 647 -7.2; 712 -6.6; 783 -6.1; 861 -5.6; 947 -5.4; 1042 -5.5; 1146 -6.1; 1261 -6.7; 1387 -7.1; 1526 -6.9; 1678 -6.3; 1846 -5.6; 2031 -5.1; 2234 -4.9; 2457 -4.3; 2703 -3.6; 2973 -3.1; 3270 -2.5; 3597 -0.8; 3957 -0.5; 4353 -0.7; 4788 -0.9; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -9.7; 9330 -9.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears UE5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 16 Hz    | 0.13 | 1.2 dB  |
| Peaking | 184 Hz   | 0.42 | -4.7 dB |
| Peaking | 861 Hz   | 2.86 | 1.9 dB  |
| Peaking | 4955 Hz  | 0.89 | 6.8 dB  |
| Peaking | 8706 Hz  | 3.28 | -6.6 dB |
| Peaking | 1073 Hz  | 4.97 | 0.7 dB  |
| Peaking | 1451 Hz  | 3.05 | -1.3 dB |
| Peaking | 4495 Hz  | 1.7  | 1.9 dB  |
| Peaking | 4724 Hz  | 3.72 | -2.9 dB |
| Peaking | 13258 Hz | 1.53 | -0.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Ultimate%20Ears%20UE5/Ultimate%20Ears%20UE5.png)