# Ultimate Ears UE500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -17.0; 23 -16.9; 25 -16.8; 28 -16.6; 31 -16.3; 34 -16.1; 37 -15.9; 41 -15.6; 45 -15.4; 49 -15.2; 54 -15.0; 60 -14.8; 66 -14.7; 72 -14.6; 79 -14.4; 87 -14.3; 96 -14.0; 106 -13.7; 116 -13.5; 128 -13.3; 141 -13.2; 155 -12.9; 170 -12.7; 187 -12.3; 206 -12.0; 227 -11.6; 249 -11.2; 274 -10.8; 302 -10.3; 332 -9.8; 365 -9.2; 402 -8.7; 442 -8.3; 486 -7.8; 535 -7.3; 588 -6.8; 647 -6.4; 712 -6.0; 783 -5.9; 861 -6.0; 947 -6.2; 1042 -6.7; 1146 -7.2; 1261 -7.5; 1387 -6.9; 1526 -6.7; 1678 -7.2; 1846 -7.7; 2031 -8.1; 2234 -8.0; 2457 -7.6; 2703 -5.9; 2973 -3.2; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
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

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 16 Hz   | 0.13 | -10.1 dB |
| Peaking | 197 Hz  | 0.84 | -2.9 dB  |
| Peaking | 2015 Hz | 2.33 | -3.0 dB  |
| Peaking | 2496 Hz | 4.82 | -2.8 dB  |
| Peaking | 4153 Hz | 1.03 | 7.2 dB   |
| Peaking | 752 Hz  | 2.48 | 1.2 dB   |
| Peaking | 1215 Hz | 5.42 | -1.1 dB  |
| Peaking | 4340 Hz | 5.65 | -1.1 dB  |
| Peaking | 6308 Hz | 2.57 | 4.4 dB   |
| Peaking | 7567 Hz | 1.73 | -3.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.6 dB |
| Peaking | 62 Hz    | 1.41 | -5.7 dB  |
| Peaking | 125 Hz   | 1.41 | -5.4 dB  |
| Peaking | 250 Hz   | 1.41 | -3.9 dB  |
| Peaking | 500 Hz   | 1.41 | -0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultimate%20Ears%20UE500/Ultimate%20Ears%20UE500.png)