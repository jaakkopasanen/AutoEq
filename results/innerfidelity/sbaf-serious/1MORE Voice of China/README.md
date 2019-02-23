# 1MORE Voice of China
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.5; 23 -2.1; 25 -2.7; 28 -3.4; 31 -4.0; 34 -4.5; 37 -4.9; 41 -5.4; 45 -5.9; 49 -6.3; 54 -6.7; 60 -7.2; 66 -7.6; 72 -7.9; 79 -8.4; 87 -8.8; 96 -9.2; 106 -9.3; 116 -9.5; 128 -9.6; 141 -9.7; 155 -9.6; 170 -9.5; 187 -9.3; 206 -9.1; 227 -8.7; 249 -8.3; 274 -7.9; 302 -7.3; 332 -6.9; 365 -6.3; 402 -5.7; 442 -5.0; 486 -4.6; 535 -4.1; 588 -3.3; 647 -2.8; 712 -2.6; 783 -2.1; 861 -2.0; 947 -2.3; 1042 -2.5; 1146 -2.7; 1261 -3.0; 1387 -3.4; 1526 -3.9; 1678 -4.5; 1846 -4.7; 2031 -4.8; 2234 -5.3; 2457 -5.9; 2703 -6.3; 2973 -5.9; 3270 -4.9; 3597 -4.1; 3957 -5.0; 4353 -7.9; 4788 -10.0; 5267 -8.9; 5793 -3.9; 6373 -0.5; 7010 -2.6; 7711 -4.8; 8482 -5.1; 9330 -5.1; 10263 -5.1; 11289 -5.1; 12418 -5.1; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -5.1; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Voice of China GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Voice of China ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.9  | 4.6 dB  |
| Peaking | 139 Hz  | 0.48 | -4.8 dB |
| Peaking | 796 Hz  | 0.98 | 3.7 dB  |
| Peaking | 4935 Hz | 4.34 | -6.2 dB |
| Peaking | 6384 Hz | 5.04 | 5.9 dB  |
| Peaking | 1275 Hz | 3.79 | 0.5 dB  |
| Peaking | 2773 Hz | 2.56 | -1.8 dB |
| Peaking | 3668 Hz | 3.34 | 2.3 dB  |
| Peaking | 4379 Hz | 6.86 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.3 dB  |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | -1.8 dB |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/1MORE%20Voice%20of%20China/1MORE%20Voice%20of%20China.png)