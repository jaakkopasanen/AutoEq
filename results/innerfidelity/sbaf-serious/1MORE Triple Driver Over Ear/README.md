# 1MORE Triple Driver Over Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.4; 23 -4.8; 25 -5.2; 28 -5.8; 31 -6.3; 34 -6.7; 37 -7.0; 41 -7.2; 45 -7.4; 49 -7.5; 54 -7.6; 60 -7.4; 66 -7.0; 72 -6.9; 79 -7.5; 87 -8.0; 96 -7.6; 106 -7.3; 116 -7.5; 128 -7.5; 141 -7.0; 155 -6.3; 170 -5.5; 187 -4.9; 206 -4.2; 227 -3.2; 249 -2.4; 274 -1.7; 302 -1.1; 332 -0.8; 365 -0.8; 402 -1.3; 442 -1.9; 486 -3.2; 535 -4.0; 588 -4.1; 647 -4.2; 712 -4.6; 783 -4.5; 861 -4.6; 947 -4.3; 1042 -3.7; 1146 -3.8; 1261 -3.6; 1387 -3.6; 1526 -3.6; 1678 -3.2; 1846 -2.5; 2031 -2.0; 2234 -1.7; 2457 -0.8; 2703 -0.5; 2973 -0.9; 3270 -1.1; 3597 -2.2; 3957 -5.2; 4353 -5.0; 4788 -3.7; 5267 -2.0; 5793 -2.3; 6373 -3.1; 7010 -2.0; 7711 -3.5; 8482 -3.8; 9330 -3.8; 10263 -3.8; 11289 -3.8; 12418 -3.8; 13660 -3.8; 15026 -3.8; 16529 -3.8; 18182 -3.8; 20000 -3.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Triple Driver Over Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Triple Driver Over Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 160 Hz  | 0.2  | -5.0 dB |
| Peaking | 319 Hz  | 0.94 | 7.6 dB  |
| Peaking | 3018 Hz | 1.05 | 4.1 dB  |
| Peaking | 4162 Hz | 3.2  | -4.6 dB |
| Peaking | 5395 Hz | 3.5  | 1.5 dB  |
| Peaking | 18 Hz   | 1.22 | 1.3 dB  |
| Peaking | 36 Hz   | 1.15 | -0.7 dB |
| Peaking | 71 Hz   | 3.8  | 1.2 dB  |
| Peaking | 82 Hz   | 4.17 | -0.5 dB |
| Peaking | 1592 Hz | 4.4  | -0.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.2 dB |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | 2.7 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/1MORE%20Triple%20Driver%20Over%20Ear/1MORE%20Triple%20Driver%20Over%20Ear.png)