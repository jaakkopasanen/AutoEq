# Soul Jet Pro ANC Off
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.5; 23 -2.1; 25 -2.6; 28 -3.3; 31 -3.9; 34 -4.5; 37 -5.1; 41 -5.7; 45 -6.3; 49 -6.8; 54 -7.5; 60 -8.2; 66 -8.8; 72 -9.4; 79 -9.9; 87 -10.3; 96 -10.5; 106 -10.5; 116 -11.0; 128 -12.5; 141 -13.8; 155 -14.6; 170 -14.5; 187 -16.0; 206 -16.7; 227 -17.3; 249 -17.4; 274 -16.8; 302 -15.7; 332 -13.8; 365 -11.4; 402 -9.6; 442 -7.2; 486 -4.9; 535 -1.8; 588 -0.5; 647 -1.7; 712 -5.3; 783 -4.0; 861 -5.7; 947 -6.7; 1042 -6.2; 1146 -6.0; 1261 -5.4; 1387 -5.3; 1526 -5.7; 1678 -5.8; 1846 -6.4; 2031 -7.9; 2234 -9.0; 2457 -9.0; 2703 -8.8; 2973 -7.6; 3270 -7.2; 3597 -9.0; 3957 -11.4; 4353 -15.1; 4788 -13.5; 5267 -11.3; 5793 -9.1; 6373 -7.5; 7010 -4.1; 7711 -6.2; 8482 -7.1; 9330 -9.2; 10263 -7.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -12.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Soul Jet Pro ANC Off GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Soul Jet Pro ANC Off ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 22 Hz   | 1.25 | 5.1 dB   |
| Peaking | 247 Hz  | 0.66 | -12.1 dB |
| Peaking | 561 Hz  | 1.57 | 10.4 dB  |
| Peaking | 2374 Hz | 5.24 | -2.5 dB  |
| Peaking | 4493 Hz | 3.48 | -8.9 dB  |
| Peaking | 75 Hz   | 4.14 | -0.9 dB  |
| Peaking | 1452 Hz | 2.68 | 1.7 dB   |
| Peaking | 1938 Hz | 0.27 | -0.3 dB  |
| Peaking | 6972 Hz | 8.68 | 3.8 dB   |
| Peaking | 9498 Hz | 6.31 | -2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 4.0 dB   |
| Peaking | 62 Hz    | 1.41 | -1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -3.4 dB  |
| Peaking | 250 Hz   | 1.41 | -13.2 dB |
| Peaking | 500 Hz   | 1.41 | 5.7 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 4000 Hz  | 1.41 | -5.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 16000 Hz | 1.41 | -0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Soul%20Jet%20Pro%20ANC%20Off/Soul%20Jet%20Pro%20ANC%20Off.png)