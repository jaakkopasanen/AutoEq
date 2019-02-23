# Ultimate Ears UE350
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.8; 23 -13.7; 25 -13.7; 28 -13.8; 31 -13.8; 34 -13.8; 37 -13.7; 41 -13.7; 45 -13.7; 49 -13.7; 54 -13.7; 60 -13.7; 66 -13.8; 72 -13.8; 79 -13.9; 87 -14.0; 96 -14.0; 106 -13.9; 116 -13.7; 128 -13.7; 141 -13.5; 155 -13.2; 170 -12.9; 187 -12.6; 206 -12.2; 227 -11.6; 249 -11.2; 274 -10.6; 302 -10.1; 332 -9.5; 365 -8.9; 402 -8.4; 442 -7.7; 486 -7.3; 535 -6.8; 588 -6.0; 647 -5.7; 712 -5.5; 783 -5.0; 861 -5.5; 947 -5.1; 1042 -5.2; 1146 -5.8; 1261 -5.9; 1387 -6.6; 1526 -7.2; 1678 -7.5; 1846 -7.2; 2031 -6.8; 2234 -6.3; 2457 -5.0; 2703 -4.0; 2973 -2.3; 3270 -0.7; 3597 -0.5; 3957 -0.5; 4353 -0.9; 4788 -1.0; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears UE350 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE350 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 55 Hz   | 0.16 | -7.6 dB |
| Peaking | 657 Hz  | 1.14 | 2.8 dB  |
| Peaking | 3557 Hz | 2.55 | 5.2 dB  |
| Peaking | 5832 Hz | 1.67 | 6.7 dB  |
| Peaking | 7846 Hz | 1.92 | -2.7 dB |
| Peaking | 41 Hz   | 0.42 | -1.1 dB |
| Peaking | 46 Hz   | 0.89 | 1.6 dB  |
| Peaking | 1074 Hz | 2.38 | 1.0 dB  |
| Peaking | 1742 Hz | 1.93 | -1.7 dB |
| Peaking | 2859 Hz | 4.52 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.3 dB |
| Peaking | 62 Hz    | 1.41 | -5.3 dB |
| Peaking | 125 Hz   | 1.41 | -6.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultimate%20Ears%20UE350/Ultimate%20Ears%20UE350.png)