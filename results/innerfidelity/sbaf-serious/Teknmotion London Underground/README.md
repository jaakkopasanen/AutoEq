# Teknmotion London Underground
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.8; 41 -1.5; 45 -2.2; 49 -2.8; 54 -3.5; 60 -4.2; 66 -4.7; 72 -5.0; 79 -5.3; 87 -5.4; 96 -5.6; 106 -5.7; 116 -5.6; 128 -5.5; 141 -5.3; 155 -5.1; 170 -4.7; 187 -4.3; 206 -3.9; 227 -3.4; 249 -3.0; 274 -2.6; 302 -1.9; 332 -1.3; 365 -0.6; 402 -0.5; 442 -0.5; 486 -0.5; 535 -0.8; 588 -1.6; 647 -3.2; 712 -4.8; 783 -5.5; 861 -6.0; 947 -6.2; 1042 -6.5; 1146 -5.9; 1261 -5.9; 1387 -7.0; 1526 -6.6; 1678 -5.5; 1846 -3.7; 2031 -1.6; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Teknmotion London Underground GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Teknmotion London Underground ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.81 | 6.5 dB  |
| Peaking | 336 Hz  | 1.27 | 4.8 dB  |
| Peaking | 513 Hz  | 2.76 | 4.1 dB  |
| Peaking | 2614 Hz | 1.87 | 5.6 dB  |
| Peaking | 4931 Hz | 1.52 | 6.0 dB  |
| Peaking | 948 Hz  | 3.86 | -0.9 dB |
| Peaking | 1478 Hz | 4.19 | -2.0 dB |
| Peaking | 2071 Hz | 6.46 | 1.9 dB  |
| Peaking | 6419 Hz | 4.39 | 3.6 dB  |
| Peaking | 7467 Hz | 1.73 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | 2.8 dB  |
| Peaking | 500 Hz   | 1.41 | 6.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.7 dB |
| Peaking | 2000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Teknmotion%20London%20Underground/Teknmotion%20London%20Underground.png)