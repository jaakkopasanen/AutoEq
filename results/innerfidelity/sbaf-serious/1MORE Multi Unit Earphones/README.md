# 1MORE Multi Unit Earphones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.3; 23 -6.8; 25 -7.2; 28 -7.7; 31 -8.1; 34 -8.5; 37 -8.8; 41 -9.1; 45 -9.4; 49 -9.6; 54 -10.0; 60 -10.3; 66 -10.5; 72 -10.8; 79 -11.0; 87 -11.4; 96 -11.6; 106 -11.7; 116 -11.7; 128 -11.7; 141 -11.7; 155 -11.6; 170 -11.4; 187 -11.1; 206 -10.8; 227 -10.3; 249 -10.0; 274 -9.5; 302 -9.0; 332 -8.5; 365 -8.0; 402 -7.5; 442 -6.9; 486 -6.5; 535 -6.0; 588 -5.4; 647 -5.1; 712 -5.0; 783 -4.7; 861 -4.9; 947 -5.3; 1042 -5.8; 1146 -6.5; 1261 -7.0; 1387 -8.0; 1526 -9.3; 1678 -10.4; 1846 -11.2; 2031 -11.6; 2234 -11.4; 2457 -9.4; 2703 -7.0; 2973 -4.5; 3270 -3.4; 3597 -4.3; 3957 -7.3; 4353 -7.6; 4788 -2.0; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.9; 10263 -9.3; 11289 -8.1; 12418 -6.5; 13660 -6.5; 15026 -7.4; 16529 -9.3; 18182 -9.7; 20000 -7.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Multi Unit Earphones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Multi Unit Earphones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 86 Hz    | 0.68 | -4.5 dB |
| Peaking | 188 Hz   | 1.31 | -3.0 dB |
| Peaking | 1992 Hz  | 3.06 | -6.0 dB |
| Peaking | 5654 Hz  | 2.45 | 7.3 dB  |
| Peaking | 18750 Hz | 0.22 | -2.2 dB |
| Peaking | 745 Hz   | 2.19 | 2.4 dB  |
| Peaking | 3278 Hz  | 5.18 | 3.6 dB  |
| Peaking | 4182 Hz  | 8.4  | -4.4 dB |
| Peaking | 10483 Hz | 5.17 | -2.7 dB |
| Peaking | 13258 Hz | 2.47 | 1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.8 dB |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.1 dB |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -3.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/1MORE%20Multi%20Unit%20Earphones/1MORE%20Multi%20Unit%20Earphones.png)