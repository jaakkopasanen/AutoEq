# Zoukbox ZLX30
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.7; 23 -13.7; 25 -13.7; 28 -13.6; 31 -13.6; 34 -13.5; 37 -13.5; 41 -13.3; 45 -13.2; 49 -13.1; 54 -13.0; 60 -12.9; 66 -12.8; 72 -12.7; 79 -12.7; 87 -12.6; 96 -12.5; 106 -12.3; 116 -12.0; 128 -11.7; 141 -11.4; 155 -11.0; 170 -10.7; 187 -10.2; 206 -9.7; 227 -9.1; 249 -8.6; 274 -8.0; 302 -7.4; 332 -6.9; 365 -6.2; 402 -5.8; 442 -5.1; 486 -4.7; 535 -4.3; 588 -3.6; 647 -3.3; 712 -3.2; 783 -2.9; 861 -3.1; 947 -3.6; 1042 -4.1; 1146 -4.6; 1261 -5.3; 1387 -6.3; 1526 -7.4; 1678 -8.5; 1846 -9.5; 2031 -10.4; 2234 -11.4; 2457 -11.1; 2703 -9.2; 2973 -5.8; 3270 -5.0; 3597 -7.2; 3957 -11.3; 4353 -14.0; 4788 -9.6; 5267 -1.1; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Zoukbox ZLX30 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Zoukbox ZLX30 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 30 Hz   | 0.41 | -7.3 dB  |
| Peaking | 122 Hz  | 1.12 | -3.6 dB  |
| Peaking | 2231 Hz | 3.88 | -5.7 dB  |
| Peaking | 4397 Hz | 5.08 | -10.9 dB |
| Peaking | 5649 Hz | 2.7  | 8.2 dB   |
| Peaking | 227 Hz  | 1.69 | -1.3 dB  |
| Peaking | 754 Hz  | 0.89 | 3.8 dB   |
| Peaking | 1678 Hz | 3.57 | -2.1 dB  |
| Peaking | 3134 Hz | 1.86 | -3.0 dB  |
| Peaking | 3204 Hz | 4.52 | 5.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.4 dB |
| Peaking | 4000 Hz  | 1.41 | -1.4 dB |
| Peaking | 8000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Zoukbox%20ZLX30/Zoukbox%20ZLX30.png)