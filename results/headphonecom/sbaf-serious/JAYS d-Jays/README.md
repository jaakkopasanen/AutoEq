# JAYS d-Jays
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.8; 23 -1.1; 25 -1.4; 28 -1.7; 31 -1.9; 34 -2.2; 37 -2.4; 41 -2.7; 45 -2.9; 49 -3.2; 54 -3.5; 60 -4.0; 66 -4.3; 72 -4.6; 79 -5.1; 87 -5.4; 96 -5.7; 106 -6.0; 116 -6.2; 128 -6.5; 141 -7.1; 155 -7.3; 170 -7.5; 187 -7.6; 206 -7.5; 227 -7.5; 249 -7.7; 274 -8.0; 302 -7.8; 332 -7.5; 365 -7.3; 402 -7.0; 442 -6.9; 486 -6.8; 535 -6.6; 588 -6.4; 647 -6.0; 712 -5.9; 783 -5.8; 861 -5.9; 947 -6.3; 1042 -6.7; 1146 -7.1; 1261 -7.5; 1387 -8.1; 1526 -8.8; 1678 -9.5; 1846 -10.5; 2031 -10.9; 2234 -10.6; 2457 -8.7; 2703 -5.0; 2973 -0.9; 3270 -0.5; 3597 -0.5; 3957 -1.1; 4353 -3.8; 4788 -5.1; 5267 -1.8; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JAYS d-Jays GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JAYS d-Jays ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 1.09 | 5.4 dB  |
| Peaking | 49 Hz   | 1.63 | 2.4 dB  |
| Peaking | 2164 Hz | 1.73 | -7.1 dB |
| Peaking | 3221 Hz | 2    | 8.8 dB  |
| Peaking | 5976 Hz | 4.07 | 6.0 dB  |
| Peaking | 248 Hz  | 1.08 | -1.4 dB |
| Peaking | 770 Hz  | 2.13 | 1.2 dB  |
| Peaking | 6697 Hz | 8.35 | 1.7 dB  |
| Peaking | 7698 Hz | 2.58 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB  |
| Peaking | 62 Hz    | 1.41 | 1.7 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.3 dB |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/JAYS%20d-Jays/JAYS%20d-Jays.png)