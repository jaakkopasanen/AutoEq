# Sennheiser HD 212Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.6; 54 -1.5; 60 -2.6; 66 -2.8; 72 -3.3; 79 -4.2; 87 -4.9; 96 -5.4; 106 -5.8; 116 -5.8; 128 -4.8; 141 -3.2; 155 -3.7; 170 -3.6; 187 -3.4; 206 -3.1; 227 -2.7; 249 -2.5; 274 -2.4; 302 -3.6; 332 -4.0; 365 -4.2; 402 -3.7; 442 -3.6; 486 -3.9; 535 -4.3; 588 -4.7; 647 -5.1; 712 -5.7; 783 -6.0; 861 -5.9; 947 -6.2; 1042 -6.8; 1146 -6.7; 1261 -6.6; 1387 -6.6; 1526 -6.9; 1678 -6.7; 1846 -6.0; 2031 -5.3; 2234 -4.6; 2457 -3.3; 2703 -2.5; 2973 -0.8; 3270 -0.5; 3597 -0.6; 3957 -5.6; 4353 -7.1; 4788 -4.5; 5267 -1.7; 5793 -0.5; 6373 -2.1; 7010 -5.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.7; 15026 -8.8; 16529 -7.8; 18182 -7.4; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 212Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 212Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 24 Hz    |  0.98 | 5.6 dB  |
| Peaking | 48 Hz    |  1.67 | 4.1 dB  |
| Peaking | 262 Hz   |  0.78 | 3.7 dB  |
| Peaking | 3109 Hz  |  3.05 | 6.5 dB  |
| Peaking | 5801 Hz  |  4.74 | 6.4 dB  |
| Peaking | 107 Hz   |  3.77 | -1.8 dB |
| Peaking | 163 Hz   |  0.42 | 0.5 dB  |
| Peaking | 327 Hz   |  5.35 | -1.3 dB |
| Peaking | 4194 Hz  | 10.6  | -3.1 dB |
| Peaking | 14839 Hz |  2.2  | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.4 dB  |
| Peaking | 125 Hz   | 1.41 | 0.2 dB  |
| Peaking | 250 Hz   | 1.41 | 3.6 dB  |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -2.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20212Pro/Sennheiser%20HD%20212Pro.png)