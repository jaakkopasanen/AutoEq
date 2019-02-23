# 1MORE Triple Driver LTNG
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.7; 23 -5.1; 25 -5.4; 28 -5.8; 31 -6.2; 34 -6.4; 37 -6.7; 41 -7.0; 45 -7.2; 49 -7.4; 54 -7.7; 60 -8.0; 66 -8.2; 72 -8.5; 79 -8.8; 87 -9.1; 96 -9.4; 106 -9.6; 116 -9.8; 128 -9.9; 141 -10.0; 155 -9.9; 170 -9.8; 187 -9.6; 206 -9.3; 227 -9.0; 249 -8.7; 274 -8.3; 302 -7.9; 332 -7.5; 365 -7.0; 402 -6.7; 442 -6.3; 486 -5.8; 535 -5.4; 588 -5.0; 647 -4.6; 712 -4.2; 783 -3.9; 861 -3.8; 947 -3.8; 1042 -4.2; 1146 -4.7; 1261 -5.0; 1387 -5.4; 1526 -5.7; 1678 -5.9; 1846 -6.2; 2031 -6.7; 2234 -7.6; 2457 -8.2; 2703 -8.0; 2973 -7.4; 3270 -7.0; 3597 -7.4; 3957 -9.0; 4353 -10.0; 4788 -7.2; 5267 -1.3; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.8; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.6; 12418 -9.1; 13660 -11.6; 15026 -13.9; 16529 -15.7; 18182 -9.2; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Triple Driver LTNG GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Triple Driver LTNG ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 143 Hz   | 0.65 | -3.7 dB |
| Peaking | 816 Hz   | 1.19 | 3.1 dB  |
| Peaking | 4535 Hz  | 1.92 | -7.3 dB |
| Peaking | 5593 Hz  | 2.4  | 10.9 dB |
| Peaking | 16092 Hz | 1.38 | -9.8 dB |
| Peaking | 21 Hz    | 1.77 | 2.0 dB  |
| Peaking | 2547 Hz  | 2.91 | -3.2 dB |
| Peaking | 2883 Hz  | 1.59 | 1.8 dB  |
| Peaking | 11009 Hz | 2.58 | 3.7 dB  |
| Peaking | 11276 Hz | 1.22 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB   |
| Peaking | 62 Hz    | 1.41 | -1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -3.3 dB  |
| Peaking | 250 Hz   | 1.41 | -2.2 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.0 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 3.2 dB   |
| Peaking | 16000 Hz | 1.41 | -10.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/1MORE%20Triple%20Driver%20LTNG/1MORE%20Triple%20Driver%20LTNG.png)