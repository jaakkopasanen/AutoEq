# 1MORE Triple Driver
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.3; 23 -4.8; 25 -5.2; 28 -5.7; 31 -6.1; 34 -6.5; 37 -6.8; 41 -7.1; 45 -7.3; 49 -7.5; 54 -7.8; 60 -8.1; 66 -8.4; 72 -8.6; 79 -8.9; 87 -9.1; 96 -9.4; 106 -9.6; 116 -9.7; 128 -9.8; 141 -9.7; 155 -9.7; 170 -9.5; 187 -9.3; 206 -9.0; 227 -8.6; 249 -8.2; 274 -7.8; 302 -7.3; 332 -6.8; 365 -6.3; 402 -5.8; 442 -5.3; 486 -4.8; 535 -4.3; 588 -3.8; 647 -3.3; 712 -2.7; 783 -2.2; 861 -1.8; 947 -1.6; 1042 -1.8; 1146 -2.4; 1261 -3.1; 1387 -3.8; 1526 -4.1; 1678 -4.1; 1846 -4.2; 2031 -4.6; 2234 -5.2; 2457 -5.9; 2703 -5.8; 2973 -5.1; 3270 -4.3; 3597 -4.5; 3957 -5.8; 4353 -7.9; 4788 -7.0; 5267 -2.9; 5793 -0.5; 6373 -0.7; 7010 -5.6; 7711 -4.9; 8482 -5.0; 9330 -5.0; 10263 -5.0; 11289 -5.0; 12418 -5.0; 13660 -5.0; 15026 -7.5; 16529 -11.3; 18182 -14.5; 20000 -15.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Triple Driver GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Triple Driver ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 65 Hz    | 0.8  | -1.7 dB  |
| Peaking | 156 Hz   | 0.65 | -4.3 dB  |
| Peaking | 880 Hz   | 1.32 | 3.8 dB   |
| Peaking | 5559 Hz  | 2.06 | 2.0 dB   |
| Peaking | 18945 Hz | 0.84 | -10.9 dB |
| Peaking | 3681 Hz  | 3.1  | 4.1 dB   |
| Peaking | 4513 Hz  | 1.68 | -8.1 dB  |
| Peaking | 5915 Hz  | 2.13 | 7.4 dB   |
| Peaking | 7110 Hz  | 6.4  | -3.7 dB  |
| Peaking | 13270 Hz | 2.77 | 2.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.4 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | -0.6 dB |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -6.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/1MORE%20Triple%20Driver/1MORE%20Triple%20Driver.png)