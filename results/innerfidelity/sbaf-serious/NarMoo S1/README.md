# NarMoo S1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.9; 23 -15.0; 25 -15.0; 28 -15.1; 31 -15.1; 34 -15.1; 37 -15.1; 41 -15.2; 45 -15.2; 49 -15.2; 54 -15.3; 60 -15.3; 66 -15.4; 72 -15.5; 79 -15.6; 87 -15.6; 96 -15.7; 106 -15.7; 116 -15.5; 128 -15.4; 141 -15.2; 155 -14.9; 170 -14.6; 187 -14.2; 206 -13.7; 227 -13.1; 249 -12.6; 274 -11.9; 302 -11.3; 332 -10.5; 365 -9.8; 402 -9.0; 442 -8.0; 486 -7.3; 535 -6.5; 588 -5.4; 647 -4.7; 712 -4.2; 783 -3.6; 861 -3.4; 947 -3.2; 1042 -3.6; 1146 -3.5; 1261 -3.9; 1387 -4.6; 1526 -5.8; 1678 -6.4; 1846 -7.0; 2031 -7.2; 2234 -8.0; 2457 -9.0; 2703 -10.9; 2973 -12.7; 3270 -8.9; 3597 -6.1; 3957 -7.4; 4353 -11.0; 4788 -14.2; 5267 -9.3; 5793 -3.7; 6373 -0.5; 7010 -0.9; 7711 -3.1; 8482 -5.3; 9330 -8.9; 10263 -9.3; 11289 -4.5; 12418 -3.4; 13660 -3.4; 15026 -3.4; 16529 -3.4; 18182 -5.9; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NarMoo S1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NarMoo S1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 35 Hz    | 0.19 | -11.6 dB |
| Peaking | 194 Hz   | 0.65 | -5.4 dB  |
| Peaking | 2790 Hz  | 2.24 | -8.2 dB  |
| Peaking | 4745 Hz  | 6.15 | -10.6 dB |
| Peaking | 19776 Hz | 0.57 | -2.9 dB  |
| Peaking | 898 Hz   | 1.91 | 1.7 dB   |
| Peaking | 1727 Hz  | 3.63 | -1.9 dB  |
| Peaking | 6649 Hz  | 4.88 | 5.2 dB   |
| Peaking | 9880 Hz  | 3.18 | -7.8 dB  |
| Peaking | 12280 Hz | 1.03 | 1.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.9 dB |
| Peaking | 62 Hz    | 1.41 | -8.5 dB  |
| Peaking | 125 Hz   | 1.41 | -9.7 dB  |
| Peaking | 250 Hz   | 1.41 | -7.5 dB  |
| Peaking | 500 Hz   | 1.41 | -2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB   |
| Peaking | 16000 Hz | 1.41 | -0.8 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NarMoo%20S1/NarMoo%20S1.png)