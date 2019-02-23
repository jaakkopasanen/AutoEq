# NVX XPT100 Flat Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -1.4; 28 -1.8; 31 -2.2; 34 -2.6; 37 -2.9; 41 -3.2; 45 -3.4; 49 -3.5; 54 -3.7; 60 -4.0; 66 -4.4; 72 -4.7; 79 -5.1; 87 -5.5; 96 -5.9; 106 -5.9; 116 -5.9; 128 -5.9; 141 -6.5; 155 -7.3; 170 -6.5; 187 -7.1; 206 -7.1; 227 -6.4; 249 -5.1; 274 -3.2; 302 -2.1; 332 -3.0; 365 -4.1; 402 -4.8; 442 -5.2; 486 -6.0; 535 -6.1; 588 -6.0; 647 -6.2; 712 -6.4; 783 -6.2; 861 -6.1; 947 -6.8; 1042 -7.3; 1146 -7.6; 1261 -8.0; 1387 -8.9; 1526 -10.2; 1678 -10.6; 1846 -11.3; 2031 -11.3; 2234 -11.0; 2457 -10.0; 2703 -9.7; 2973 -7.2; 3270 -5.6; 3597 -8.0; 3957 -8.1; 4353 -6.9; 4788 -5.5; 5267 -3.0; 5793 -1.3; 6373 -2.7; 7010 -3.5; 7711 -5.7; 8482 -6.0; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.7; 20000 -12.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NVX XPT100 Flat Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NVX XPT100 Flat Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.14 | 5.3 dB  |
| Peaking | 50 Hz   | 1.98 | 1.6 dB  |
| Peaking | 312 Hz  | 3.97 | 4.3 dB  |
| Peaking | 1969 Hz | 1.36 | -5.6 dB |
| Peaking | 5934 Hz | 3.39 | 5.2 dB  |
| Peaking | 35 Hz   | 0.83 | 0.5 dB  |
| Peaking | 202 Hz  | 1.49 | -3.0 dB |
| Peaking | 245 Hz  | 1.17 | 1.9 dB  |
| Peaking | 3186 Hz | 8.43 | 4.0 dB  |
| Peaking | 3631 Hz | 2.81 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.5 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | 1.6 dB  |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -5.9 dB |
| Peaking | 4000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NVX%20XPT100%20Flat%20Pads/NVX%20XPT100%20Flat%20Pads.png)