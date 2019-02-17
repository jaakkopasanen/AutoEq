# Ultimate Ears UE600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.3; 23 -4.4; 25 -4.5; 28 -4.6; 31 -4.6; 34 -4.7; 37 -4.8; 41 -5.0; 45 -5.2; 49 -5.3; 54 -5.6; 60 -5.8; 66 -6.1; 72 -6.4; 79 -6.7; 87 -7.1; 96 -7.4; 106 -7.6; 116 -7.8; 128 -8.1; 141 -8.4; 155 -8.7; 170 -8.9; 187 -9.0; 206 -9.1; 227 -9.1; 249 -9.0; 274 -8.9; 302 -8.8; 332 -8.5; 365 -8.3; 402 -8.0; 442 -7.8; 486 -7.6; 535 -7.3; 588 -7.1; 647 -6.7; 712 -6.3; 783 -6.1; 861 -6.0; 947 -6.3; 1042 -6.5; 1146 -6.7; 1261 -6.9; 1387 -7.3; 1526 -7.5; 1678 -7.4; 1846 -6.7; 2031 -5.9; 2234 -4.6; 2457 -3.1; 2703 -1.6; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.6; 4353 -2.2; 4788 -2.1; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears UE600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.49 | 2.2 dB  |
| Peaking | 206 Hz   | 0.64 | -2.8 dB |
| Peaking | 3240 Hz  | 2.09 | 6.0 dB  |
| Peaking | 5927 Hz  | 1.84 | 6.5 dB  |
| Peaking | 7798 Hz  | 2.01 | -2.6 dB |
| Peaking | 808 Hz   | 2.76 | 1.0 dB  |
| Peaking | 1632 Hz  | 2.06 | -1.7 dB |
| Peaking | 2332 Hz  | 3.89 | 0.4 dB  |
| Peaking | 2636 Hz  | 6.2  | 1.0 dB  |
| Peaking | 12274 Hz | 2.27 | -0.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultimate%20Ears%20UE600/Ultimate%20Ears%20UE600.png)