# Ultimate Ears UE600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.5; 23 -5.6; 25 -5.7; 28 -5.8; 31 -5.8; 34 -5.9; 37 -6.0; 41 -6.2; 45 -6.4; 49 -6.5; 54 -6.8; 60 -7.1; 66 -7.4; 72 -7.6; 79 -7.9; 87 -8.3; 96 -8.6; 106 -8.8; 116 -9.1; 128 -9.4; 141 -9.7; 155 -9.9; 170 -10.1; 187 -10.2; 206 -10.3; 227 -10.3; 249 -10.2; 274 -10.1; 302 -10.0; 332 -9.7; 365 -9.5; 402 -9.2; 442 -9.0; 486 -8.8; 535 -8.5; 588 -8.3; 647 -7.9; 712 -7.5; 783 -7.3; 861 -7.2; 947 -7.5; 1042 -7.7; 1146 -7.9; 1261 -8.1; 1387 -8.5; 1526 -8.7; 1678 -8.6; 1846 -7.9; 2031 -7.1; 2234 -5.8; 2457 -4.3; 2703 -2.8; 2973 -1.4; 3270 -0.5; 3597 -0.5; 3957 -1.3; 4353 -3.4; 4788 -3.3; 5267 -0.8; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears UE600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.6  | 1.1 dB  |
| Peaking | 213 Hz  | 0.5  | -3.9 dB |
| Peaking | 1635 Hz | 1.78 | -2.8 dB |
| Peaking | 3296 Hz | 1.86 | 6.5 dB  |
| Peaking | 5858 Hz | 3.48 | 5.8 dB  |
| Peaking | 471 Hz  | 4.83 | -0.2 dB |
| Peaking | 2600 Hz | 7.85 | 0.3 dB  |
| Peaking | 6663 Hz | 8.5  | 1.9 dB  |
| Peaking | 7842 Hz | 2.15 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultimate%20Ears%20UE600/Ultimate%20Ears%20UE600.png)