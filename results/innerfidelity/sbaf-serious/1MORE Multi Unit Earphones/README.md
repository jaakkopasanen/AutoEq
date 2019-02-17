# 1MORE Multi Unit Earphones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.1; 23 -7.6; 25 -8.0; 28 -8.5; 31 -9.0; 34 -9.3; 37 -9.6; 41 -9.9; 45 -10.2; 49 -10.5; 54 -10.8; 60 -11.1; 66 -11.3; 72 -11.7; 79 -11.9; 87 -12.2; 96 -12.4; 106 -12.5; 116 -12.5; 128 -12.6; 141 -12.5; 155 -12.4; 170 -12.2; 187 -11.9; 206 -11.7; 227 -11.2; 249 -10.8; 274 -10.3; 302 -9.9; 332 -9.4; 365 -8.8; 402 -8.3; 442 -7.7; 486 -7.4; 535 -6.8; 588 -6.2; 647 -5.9; 712 -5.8; 783 -5.5; 861 -5.8; 947 -6.1; 1042 -6.7; 1146 -7.3; 1261 -7.8; 1387 -8.9; 1526 -10.1; 1678 -11.2; 1846 -12.0; 2031 -12.4; 2234 -12.2; 2457 -10.2; 2703 -7.8; 2973 -5.3; 3270 -4.2; 3597 -5.1; 3957 -8.1; 4353 -8.4; 4788 -2.8; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.5; 10263 -10.2; 11289 -9.0; 12418 -6.6; 13660 -6.6; 15026 -8.3; 16529 -10.2; 18182 -10.5; 20000 -8.7
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
| Peaking | 83 Hz    | 0.54 | -5.1 dB |
| Peaking | 195 Hz   | 1.07 | -3.1 dB |
| Peaking | 1966 Hz  | 2.49 | -6.7 dB |
| Peaking | 5792 Hz  | 2.72 | 7.6 dB  |
| Peaking | 19180 Hz | 0.18 | -3.0 dB |
| Peaking | 749 Hz   | 2.62 | 1.7 dB  |
| Peaking | 3271 Hz  | 5.2  | 3.3 dB  |
| Peaking | 4163 Hz  | 8.97 | -4.6 dB |
| Peaking | 10488 Hz | 5.33 | -3.2 dB |
| Peaking | 13202 Hz | 2.8  | 2.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB |
| Peaking | 62 Hz    | 1.41 | -3.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.8 dB |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -4.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/1MORE%20Multi%20Unit%20Earphones/1MORE%20Multi%20Unit%20Earphones.png)