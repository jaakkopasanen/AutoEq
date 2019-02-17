# California Headphone Silverado
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.5; 23 -15.5; 25 -15.4; 28 -15.3; 31 -15.1; 34 -14.9; 37 -14.6; 41 -14.2; 45 -13.4; 49 -12.8; 54 -12.5; 60 -12.3; 66 -12.3; 72 -13.5; 79 -15.0; 87 -16.4; 96 -16.9; 106 -16.8; 116 -16.6; 128 -17.3; 141 -16.6; 155 -15.3; 170 -14.8; 187 -14.7; 206 -14.1; 227 -13.8; 249 -13.6; 274 -13.3; 302 -13.0; 332 -12.3; 365 -13.0; 402 -12.0; 442 -10.5; 486 -9.2; 535 -8.2; 588 -6.8; 647 -6.0; 712 -5.5; 783 -4.8; 861 -4.7; 947 -4.5; 1042 -4.5; 1146 -4.9; 1261 -6.6; 1387 -8.4; 1526 -9.3; 1678 -9.4; 1846 -8.4; 2031 -6.2; 2234 -6.9; 2457 -4.2; 2703 -2.6; 2973 -1.6; 3270 -1.2; 3597 -0.5; 3957 -0.8; 4353 -1.5; 4788 -1.7; 5267 -2.4; 5793 -5.6; 6373 -6.9; 7010 -9.5; 7711 -11.4; 8482 -13.4; 9330 -11.1; 10263 -4.8; 11289 -4.5; 12418 -5.4; 13660 -4.5; 15026 -4.5; 16529 -4.5; 18182 -5.4; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`California Headphone Silverado GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `California Headphone Silverado ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 1    | -9.4 dB  |
| Peaking | 136 Hz   | 0.42 | -11.8 dB |
| Peaking | 1688 Hz  | 2.91 | -5.6 dB  |
| Peaking | 3781 Hz  | 1.38 | 4.8 dB   |
| Peaking | 8198 Hz  | 2.54 | -9.8 dB  |
| Peaking | 94 Hz    | 5.66 | -1.4 dB  |
| Peaking | 167 Hz   | 4.26 | 1.4 dB   |
| Peaking | 381 Hz   | 3.09 | -2.7 dB  |
| Peaking | 800 Hz   | 1.9  | 2.2 dB   |
| Peaking | 10651 Hz | 7.43 | 2.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.3 dB |
| Peaking | 62 Hz    | 1.41 | -4.4 dB  |
| Peaking | 125 Hz   | 1.41 | -11.1 dB |
| Peaking | 250 Hz   | 1.41 | -7.1 dB  |
| Peaking | 500 Hz   | 1.41 | -3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB   |
| Peaking | 8000 Hz  | 1.41 | -8.1 dB  |
| Peaking | 16000 Hz | 1.41 | 0.9 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/California%20Headphone%20Silverado/California%20Headphone%20Silverado.png)