# NVX XPT100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.6; 23 -0.8; 25 -1.1; 28 -1.6; 31 -2.0; 34 -2.3; 37 -2.6; 41 -2.9; 45 -3.1; 49 -3.3; 54 -3.6; 60 -4.0; 66 -4.2; 72 -4.5; 79 -4.8; 87 -5.1; 96 -5.4; 106 -5.5; 116 -5.6; 128 -6.3; 141 -7.1; 155 -7.5; 170 -6.7; 187 -7.3; 206 -7.2; 227 -6.4; 249 -4.8; 274 -2.3; 302 -0.8; 332 -1.6; 365 -2.8; 402 -3.7; 442 -4.3; 486 -5.2; 535 -5.5; 588 -5.4; 647 -5.7; 712 -5.9; 783 -5.5; 861 -5.6; 947 -6.2; 1042 -6.6; 1146 -7.1; 1261 -7.5; 1387 -8.3; 1526 -9.1; 1678 -9.3; 1846 -9.4; 2031 -9.3; 2234 -8.9; 2457 -8.1; 2703 -7.5; 2973 -5.3; 3270 -3.3; 3597 -6.0; 3957 -5.6; 4353 -4.7; 4788 -3.3; 5267 -0.6; 5793 -0.5; 6373 -3.2; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.4; 20000 -11.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NVX XPT100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NVX XPT100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.98 | 5.6 dB  |
| Peaking | 55 Hz    | 1.56 | 1.8 dB  |
| Peaking | 322 Hz   | 2.78 | 5.7 dB  |
| Peaking | 1830 Hz  | 2.16 | -3.6 dB |
| Peaking | 5552 Hz  | 2.65 | 6.3 dB  |
| Peaking | 184 Hz   | 1.53 | -2.5 dB |
| Peaking | 249 Hz   | 0.31 | 0.9 dB  |
| Peaking | 3010 Hz  | 1.86 | -1.7 dB |
| Peaking | 3176 Hz  | 6.62 | 5.1 dB  |
| Peaking | 20135 Hz | 1.04 | -5.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | 2.3 dB  |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NVX%20XPT100/NVX%20XPT100.png)