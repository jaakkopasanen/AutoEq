# NVX XPT100 Flat Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -0.8; 28 -1.3; 31 -1.6; 34 -2.0; 37 -2.3; 41 -2.6; 45 -2.8; 49 -2.9; 54 -3.1; 60 -3.5; 66 -3.8; 72 -4.1; 79 -4.5; 87 -4.9; 96 -5.3; 106 -5.4; 116 -5.3; 128 -5.3; 141 -6.0; 155 -6.7; 170 -5.9; 187 -6.5; 206 -6.5; 227 -5.8; 249 -4.5; 274 -2.6; 302 -1.5; 332 -2.4; 365 -3.5; 402 -4.2; 442 -4.6; 486 -5.4; 535 -5.6; 588 -5.5; 647 -5.6; 712 -5.9; 783 -5.6; 861 -5.6; 947 -6.3; 1042 -6.7; 1146 -7.0; 1261 -7.4; 1387 -8.4; 1526 -9.6; 1678 -10.0; 1846 -10.7; 2031 -10.7; 2234 -10.4; 2457 -9.4; 2703 -9.1; 2973 -6.7; 3270 -5.0; 3597 -7.5; 3957 -7.5; 4353 -6.4; 4788 -4.9; 5267 -2.4; 5793 -0.7; 6373 -2.2; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.7; 20000 -11.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NVX XPT100 Flat Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NVX XPT100 Flat Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.8  | 5.7 dB  |
| Peaking | 57 Hz   | 1.31 | 1.8 dB  |
| Peaking | 319 Hz  | 2.33 | 4.8 dB  |
| Peaking | 1971 Hz | 1.9  | -4.8 dB |
| Peaking | 5852 Hz | 3.38 | 6.2 dB  |
| Peaking | 204 Hz  | 4.5  | -1.2 dB |
| Peaking | 786 Hz  | 1.39 | 0.9 dB  |
| Peaking | 1503 Hz | 7.55 | -0.9 dB |
| Peaking | 3183 Hz | 7.07 | 5.5 dB  |
| Peaking | 3258 Hz | 2.62 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.5 dB  |
| Peaking | 62 Hz    | 1.41 | 2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | 2.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.1 dB |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NVX%20XPT100%20Flat%20Pads/NVX%20XPT100%20Flat%20Pads.png)