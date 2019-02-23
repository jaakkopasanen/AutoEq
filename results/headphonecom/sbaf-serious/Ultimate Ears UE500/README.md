# Ultimate Ears UE500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.9; 23 -16.8; 25 -16.7; 28 -16.5; 31 -16.2; 34 -16.0; 37 -15.8; 41 -15.5; 45 -15.3; 49 -15.1; 54 -14.9; 60 -14.7; 66 -14.6; 72 -14.5; 79 -14.3; 87 -14.2; 96 -14.0; 106 -13.6; 116 -13.4; 128 -13.2; 141 -13.1; 155 -12.8; 170 -12.6; 187 -12.2; 206 -11.9; 227 -11.5; 249 -11.1; 274 -10.7; 302 -10.2; 332 -9.7; 365 -9.1; 402 -8.6; 442 -8.2; 486 -7.7; 535 -7.2; 588 -6.7; 647 -6.3; 712 -5.9; 783 -5.8; 861 -5.9; 947 -6.1; 1042 -6.6; 1146 -7.1; 1261 -7.4; 1387 -6.8; 1526 -6.6; 1678 -7.1; 1846 -7.6; 2031 -8.0; 2234 -7.9; 2457 -7.5; 2703 -5.8; 2973 -3.1; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears UE500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.16 | -9.9 dB |
| Peaking | 194 Hz  | 0.84 | -2.9 dB |
| Peaking | 2022 Hz | 2.46 | -2.9 dB |
| Peaking | 2493 Hz | 4.78 | -2.8 dB |
| Peaking | 4148 Hz | 1.02 | 7.1 dB  |
| Peaking | 754 Hz  | 2.53 | 1.2 dB  |
| Peaking | 1222 Hz | 5.4  | -1.1 dB |
| Peaking | 4411 Hz | 5.62 | -1.1 dB |
| Peaking | 6424 Hz | 2.58 | 4.4 dB  |
| Peaking | 7447 Hz | 1.72 | -3.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.5 dB |
| Peaking | 62 Hz    | 1.41 | -5.6 dB  |
| Peaking | 125 Hz   | 1.41 | -5.4 dB  |
| Peaking | 250 Hz   | 1.41 | -3.9 dB  |
| Peaking | 500 Hz   | 1.41 | -0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultimate%20Ears%20UE500/Ultimate%20Ears%20UE500.png)