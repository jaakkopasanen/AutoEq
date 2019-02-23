# Thinksound Rain2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.2; 23 -11.3; 25 -11.4; 28 -11.5; 31 -11.6; 34 -11.7; 37 -11.8; 41 -11.9; 45 -12.0; 49 -12.2; 54 -12.4; 60 -12.6; 66 -12.8; 72 -13.0; 79 -13.3; 87 -13.5; 96 -13.8; 106 -13.8; 116 -13.8; 128 -13.9; 141 -13.8; 155 -13.8; 170 -13.5; 187 -13.2; 206 -12.9; 227 -12.4; 249 -11.9; 274 -11.4; 302 -10.7; 332 -10.1; 365 -9.4; 402 -8.7; 442 -7.8; 486 -7.3; 535 -6.5; 588 -5.5; 647 -4.7; 712 -4.2; 783 -3.3; 861 -3.0; 947 -2.6; 1042 -2.4; 1146 -2.1; 1261 -1.9; 1387 -2.3; 1526 -3.1; 1678 -3.6; 1846 -3.5; 2031 -3.0; 2234 -2.4; 2457 -1.4; 2703 -0.9; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.8; 4353 -4.6; 4788 -6.4; 5267 -8.7; 5793 -13.1; 6373 -10.4; 7010 -5.5; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Thinksound Rain2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Thinksound Rain2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 48 Hz   | 0.21 | -4.1 dB  |
| Peaking | 216 Hz  | 0.39 | -5.8 dB  |
| Peaking | 1439 Hz | 0.22 | 5.6 dB   |
| Peaking | 5873 Hz | 4.02 | -10.2 dB |
| Peaking | 20 Hz   | 0.95 | -0.8 dB  |
| Peaking | 1908 Hz | 1.51 | -4.7 dB  |
| Peaking | 3557 Hz | 0.47 | 4.2 dB   |
| Peaking | 4760 Hz | 2.52 | -3.9 dB  |
| Peaking | 9282 Hz | 0.95 | -2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.8 dB |
| Peaking | 62 Hz    | 1.41 | -4.5 dB |
| Peaking | 125 Hz   | 1.41 | -6.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Thinksound%20Rain2/Thinksound%20Rain2.png)