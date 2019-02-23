# Soul Jet Pro ANC On
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.5; 23 -5.2; 25 -6.6; 28 -8.5; 31 -9.6; 34 -9.8; 37 -9.5; 41 -8.8; 45 -8.4; 49 -8.1; 54 -7.9; 60 -7.7; 66 -7.6; 72 -7.6; 79 -7.6; 87 -7.7; 96 -8.0; 106 -8.1; 116 -8.2; 128 -8.8; 141 -9.4; 155 -9.7; 170 -9.8; 187 -10.2; 206 -10.5; 227 -10.5; 249 -10.8; 274 -10.8; 302 -11.0; 332 -11.2; 365 -11.2; 402 -11.0; 442 -9.9; 486 -6.4; 535 -1.3; 588 -0.5; 647 -0.5; 712 -0.5; 783 -0.5; 861 -0.5; 947 -0.7; 1042 -2.0; 1146 -3.2; 1261 -4.7; 1387 -6.4; 1526 -9.6; 1678 -12.1; 1846 -14.8; 2031 -17.0; 2234 -16.8; 2457 -14.1; 2703 -11.2; 2973 -7.7; 3270 -5.5; 3597 -6.4; 3957 -8.9; 4353 -12.4; 4788 -9.4; 5267 -5.3; 5793 -1.1; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Soul Jet Pro ANC On GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Soul Jet Pro ANC On ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 399 Hz  | 0.46 | -24.0 dB |
| Peaking | 606 Hz  | 0.43 | 25.4 dB  |
| Peaking | 2053 Hz | 1.85 | -16.1 dB |
| Peaking | 4387 Hz | 6.02 | -7.7 dB  |
| Peaking | 6091 Hz | 5.01 | 6.0 dB   |
| Peaking | 34 Hz   | 3.65 | -2.9 dB  |
| Peaking | 442 Hz  | 9.82 | -1.1 dB  |
| Peaking | 1002 Hz | 3.76 | 1.3 dB   |
| Peaking | 3324 Hz | 6.04 | 3.3 dB   |
| Peaking | 4734 Hz | 0.24 | -0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.2 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB  |
| Peaking | 250 Hz   | 1.41 | -6.1 dB  |
| Peaking | 500 Hz   | 1.41 | 1.3 dB   |
| Peaking | 1000 Hz  | 1.41 | 9.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -11.6 dB |
| Peaking | 4000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Soul%20Jet%20Pro%20ANC%20On/Soul%20Jet%20Pro%20ANC%20On.png)