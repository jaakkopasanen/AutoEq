# Ultimate Ears UE600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.2; 23 -3.3; 25 -3.4; 28 -3.5; 31 -3.6; 34 -3.7; 37 -3.8; 41 -4.0; 45 -4.2; 49 -4.3; 54 -4.5; 60 -4.8; 66 -5.1; 72 -5.5; 79 -5.9; 87 -6.4; 96 -6.9; 106 -7.2; 116 -7.2; 128 -7.6; 141 -7.9; 155 -8.2; 170 -8.4; 187 -8.4; 206 -8.5; 227 -8.5; 249 -8.5; 274 -8.4; 302 -8.3; 332 -8.2; 365 -8.1; 402 -7.9; 442 -7.6; 486 -7.6; 535 -7.4; 588 -6.6; 647 -6.4; 712 -6.3; 783 -6.1; 861 -6.2; 947 -6.3; 1042 -6.6; 1146 -6.6; 1261 -6.7; 1387 -6.9; 1526 -7.0; 1678 -6.8; 1846 -6.0; 2031 -5.0; 2234 -4.0; 2457 -2.4; 2703 -1.4; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.9; 4353 -3.1; 4788 -3.1; 5267 -0.7; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.8; 9330 -6.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears UE600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.63 | 3.2 dB  |
| Peaking | 55 Hz   | 1.4  | 1.1 dB  |
| Peaking | 212 Hz  | 0.64 | -2.2 dB |
| Peaking | 3225 Hz | 1.8  | 6.5 dB  |
| Peaking | 5829 Hz | 3.39 | 5.7 dB  |
| Peaking | 763 Hz  | 2.96 | 0.8 dB  |
| Peaking | 1577 Hz | 2.43 | -1.2 dB |
| Peaking | 2483 Hz | 5.3  | 1.1 dB  |
| Peaking | 6571 Hz | 8.93 | 1.8 dB  |
| Peaking | 8186 Hz | 2.32 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultimate%20Ears%20UE600/Ultimate%20Ears%20UE600.png)