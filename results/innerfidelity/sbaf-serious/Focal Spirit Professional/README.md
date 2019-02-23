# Focal Spirit Professional
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.7; 23 -9.8; 25 -9.8; 28 -9.9; 31 -9.9; 34 -9.9; 37 -9.9; 41 -9.9; 45 -10.0; 49 -10.0; 54 -9.9; 60 -10.0; 66 -10.0; 72 -10.0; 79 -9.9; 87 -9.9; 96 -10.4; 106 -10.7; 116 -10.5; 128 -10.2; 141 -10.3; 155 -10.2; 170 -9.7; 187 -9.7; 206 -9.4; 227 -8.9; 249 -8.6; 274 -8.2; 302 -7.9; 332 -7.7; 365 -7.2; 402 -7.1; 442 -7.5; 486 -8.2; 535 -8.2; 588 -7.7; 647 -7.6; 712 -7.5; 783 -7.1; 861 -7.0; 947 -6.7; 1042 -6.8; 1146 -6.7; 1261 -6.6; 1387 -6.9; 1526 -7.2; 1678 -7.2; 1846 -6.7; 2031 -6.3; 2234 -5.8; 2457 -5.1; 2703 -4.9; 2973 -5.1; 3270 -6.4; 3597 -7.3; 3957 -6.7; 4353 -5.3; 4788 -3.8; 5267 -1.6; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -7.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Spirit Professional GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Spirit Professional ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.53 | -3.0 dB |
| Peaking | 126 Hz  | 0.55 | -3.5 dB |
| Peaking | 2688 Hz | 2.23 | 3.5 dB  |
| Peaking | 4439 Hz | 0.52 | -3.1 dB |
| Peaking | 5702 Hz | 2.15 | 9.0 dB  |
| Peaking | 409 Hz  | 2.33 | 1.3 dB  |
| Peaking | 497 Hz  | 2.18 | -1.7 dB |
| Peaking | 3599 Hz | 4.96 | -0.9 dB |
| Peaking | 5988 Hz | 0.07 | 0.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Spirit%20Professional/Focal%20Spirit%20Professional.png)