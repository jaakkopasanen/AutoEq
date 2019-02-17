# Thinksound Rain2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.7; 23 -11.9; 25 -12.0; 28 -12.1; 31 -12.2; 34 -12.3; 37 -12.3; 41 -12.5; 45 -12.6; 49 -12.7; 54 -12.9; 60 -13.1; 66 -13.4; 72 -13.6; 79 -13.8; 87 -14.1; 96 -14.3; 106 -14.4; 116 -14.4; 128 -14.5; 141 -14.4; 155 -14.3; 170 -14.1; 187 -13.7; 206 -13.4; 227 -12.9; 249 -12.5; 274 -11.9; 302 -11.3; 332 -10.6; 365 -10.0; 402 -9.3; 442 -8.4; 486 -7.8; 535 -7.0; 588 -6.0; 647 -5.2; 712 -4.7; 783 -3.9; 861 -3.6; 947 -3.2; 1042 -2.9; 1146 -2.6; 1261 -2.5; 1387 -2.8; 1526 -3.7; 1678 -4.2; 1846 -4.1; 2031 -3.6; 2234 -3.0; 2457 -1.9; 2703 -1.5; 2973 -0.8; 3270 -0.5; 3597 -0.9; 3957 -2.4; 4353 -5.2; 4788 -6.9; 5267 -9.3; 5793 -13.7; 6373 -11.0; 7010 -6.0; 7711 -3.0; 8482 -3.0; 9330 -3.5; 10263 -5.5; 11289 -3.6; 12418 -3.1; 13660 -3.1; 15026 -3.1; 16529 -5.6; 18182 -3.6; 20000 -3.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Thinksound Rain2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Thinksound Rain2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.21 | -8.5 dB  |
| Peaking | 155 Hz   | 0.64 | -6.3 dB  |
| Peaking | 333 Hz   | 1.18 | -3.3 dB  |
| Peaking | 3258 Hz  | 2.73 | 3.5 dB   |
| Peaking | 5829 Hz  | 3.64 | -11.4 dB |
| Peaking | 1200 Hz  | 1.75 | 1.4 dB   |
| Peaking | 1711 Hz  | 3.77 | -1.6 dB  |
| Peaking | 7909 Hz  | 4.72 | 2.5 dB   |
| Peaking | 16761 Hz | 0.21 | -0.9 dB  |
| Peaking | 19521 Hz | 2.78 | 0.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.8 dB |
| Peaking | 62 Hz    | 1.41 | -7.3 dB |
| Peaking | 125 Hz   | 1.41 | -9.4 dB |
| Peaking | 250 Hz   | 1.41 | -7.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.9 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.9 dB |
| Peaking | 8000 Hz  | 1.41 | -3.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Thinksound%20Rain2/Thinksound%20Rain2.png)