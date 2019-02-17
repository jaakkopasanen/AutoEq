# Ultimate Ears UE350
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.1; 23 -15.0; 25 -15.0; 28 -15.1; 31 -15.1; 34 -15.1; 37 -15.0; 41 -15.0; 45 -15.0; 49 -15.0; 54 -15.0; 60 -15.0; 66 -15.1; 72 -15.1; 79 -15.2; 87 -15.3; 96 -15.3; 106 -15.2; 116 -15.0; 128 -15.0; 141 -14.8; 155 -14.5; 170 -14.2; 187 -13.8; 206 -13.5; 227 -12.9; 249 -12.5; 274 -11.9; 302 -11.4; 332 -10.8; 365 -10.2; 402 -9.7; 442 -9.0; 486 -8.6; 535 -8.1; 588 -7.3; 647 -7.0; 712 -6.8; 783 -6.2; 861 -6.7; 947 -6.3; 1042 -6.5; 1146 -7.1; 1261 -7.2; 1387 -7.8; 1526 -8.5; 1678 -8.8; 1846 -8.5; 2031 -8.1; 2234 -7.5; 2457 -6.3; 2703 -5.3; 2973 -3.6; 3270 -1.8; 3597 -0.5; 3957 -0.7; 4353 -2.1; 4788 -2.2; 5267 -1.0; 5793 -0.5; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears UE350 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE350 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.18 | -8.3 dB |
| Peaking | 177 Hz  | 0.66 | -4.0 dB |
| Peaking | 1831 Hz | 2.25 | -2.8 dB |
| Peaking | 3647 Hz | 2.32 | 6.0 dB  |
| Peaking | 5826 Hz | 3.16 | 5.7 dB  |
| Peaking | 93 Hz   | 4.05 | -0.4 dB |
| Peaking | 354 Hz  | 1.89 | -0.7 dB |
| Peaking | 778 Hz  | 1.48 | 1.0 dB  |
| Peaking | 1480 Hz | 5.41 | -0.7 dB |
| Peaking | 8219 Hz | 4.56 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.7 dB |
| Peaking | 62 Hz    | 1.41 | -6.1 dB |
| Peaking | 125 Hz   | 1.41 | -7.0 dB |
| Peaking | 250 Hz   | 1.41 | -4.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultimate%20Ears%20UE350/Ultimate%20Ears%20UE350.png)