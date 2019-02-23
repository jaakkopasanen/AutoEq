# Soul Jet Pro ANC Off
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.8; 31 -1.3; 34 -1.9; 37 -2.5; 41 -3.1; 45 -3.7; 49 -4.2; 54 -4.9; 60 -5.6; 66 -6.3; 72 -6.8; 79 -7.3; 87 -7.7; 96 -7.9; 106 -7.9; 116 -8.4; 128 -9.9; 141 -11.2; 155 -12.0; 170 -11.9; 187 -13.4; 206 -14.1; 227 -14.7; 249 -14.8; 274 -14.2; 302 -13.1; 332 -11.2; 365 -8.8; 402 -7.0; 442 -4.6; 486 -2.3; 535 -0.5; 588 -0.5; 647 -0.5; 712 -2.7; 783 -1.4; 861 -3.2; 947 -4.1; 1042 -3.6; 1146 -3.4; 1261 -2.8; 1387 -2.8; 1526 -3.1; 1678 -3.2; 1846 -3.8; 2031 -5.3; 2234 -6.4; 2457 -6.4; 2703 -6.2; 2973 -5.0; 3270 -4.6; 3597 -6.4; 3957 -8.8; 4353 -12.5; 4788 -10.9; 5267 -8.7; 5793 -6.5; 6373 -4.9; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -9.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Soul Jet Pro ANC Off GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Soul Jet Pro ANC Off ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 24 Hz   | 0.72 | 6.3 dB   |
| Peaking | 258 Hz  | 0.81 | -11.0 dB |
| Peaking | 541 Hz  | 1.22 | 8.4 dB   |
| Peaking | 1571 Hz | 0.21 | 2.2 dB   |
| Peaking | 4455 Hz | 3.79 | -8.0 dB  |
| Peaking | 111 Hz  | 8.53 | 1.1 dB   |
| Peaking | 1655 Hz | 1.39 | 5.0 dB   |
| Peaking | 2472 Hz | 0.79 | -6.7 dB  |
| Peaking | 3253 Hz | 1.71 | 5.4 dB   |
| Peaking | 6714 Hz | 7.93 | 3.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.5 dB   |
| Peaking | 62 Hz    | 1.41 | 0.1 dB   |
| Peaking | 125 Hz   | 1.41 | -1.7 dB  |
| Peaking | 250 Hz   | 1.41 | -10.7 dB |
| Peaking | 500 Hz   | 1.41 | 6.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 4000 Hz  | 1.41 | -3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 16000 Hz | 1.41 | -0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Soul%20Jet%20Pro%20ANC%20Off/Soul%20Jet%20Pro%20ANC%20Off.png)