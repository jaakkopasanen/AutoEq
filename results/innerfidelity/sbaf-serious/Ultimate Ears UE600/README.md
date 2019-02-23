# Ultimate Ears UE600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.2; 23 -4.3; 25 -4.4; 28 -4.5; 31 -4.6; 34 -4.7; 37 -4.9; 41 -5.1; 45 -5.2; 49 -5.4; 54 -5.6; 60 -5.8; 66 -6.2; 72 -6.6; 79 -7.0; 87 -7.5; 96 -7.9; 106 -8.2; 116 -8.3; 128 -8.6; 141 -8.9; 155 -9.2; 170 -9.4; 187 -9.4; 206 -9.6; 227 -9.5; 249 -9.6; 274 -9.4; 302 -9.4; 332 -9.2; 365 -9.1; 402 -8.9; 442 -8.6; 486 -8.6; 535 -8.4; 588 -7.6; 647 -7.4; 712 -7.3; 783 -7.1; 861 -7.2; 947 -7.4; 1042 -7.6; 1146 -7.7; 1261 -7.7; 1387 -7.9; 1526 -8.0; 1678 -7.8; 1846 -7.1; 2031 -6.0; 2234 -5.0; 2457 -3.5; 2703 -2.4; 2973 -1.0; 3270 -0.5; 3597 -0.5; 3957 -1.8; 4353 -4.1; 4788 -4.1; 5267 -1.6; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.8; 9330 -7.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears UE600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.43 | 2.3 dB  |
| Peaking | 204 Hz   | 0.54 | -3.3 dB |
| Peaking | 3233 Hz  | 1.41 | 10.1 dB |
| Peaking | 3526 Hz  | 0.43 | -4.1 dB |
| Peaking | 5974 Hz  | 2.9  | 7.6 dB  |
| Peaking | 787 Hz   | 3.36 | 0.7 dB  |
| Peaking | 1584 Hz  | 3.49 | -0.8 dB |
| Peaking | 2388 Hz  | 6.3  | 0.7 dB  |
| Peaking | 8757 Hz  | 4.47 | -2.1 dB |
| Peaking | 10270 Hz | 1.22 | 0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultimate%20Ears%20UE600/Ultimate%20Ears%20UE600.png)