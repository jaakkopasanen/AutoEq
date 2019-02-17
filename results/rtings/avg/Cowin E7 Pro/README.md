# Cowin E7 Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.6; 37 -1.5; 41 -3.3; 45 -4.8; 49 -5.9; 54 -6.8; 60 -7.9; 66 -9.1; 72 -9.4; 79 -8.4; 87 -7.5; 96 -7.0; 106 -6.8; 116 -6.7; 128 -6.7; 141 -6.5; 155 -6.4; 170 -6.2; 187 -5.9; 206 -5.5; 227 -5.0; 249 -4.7; 274 -4.3; 302 -3.6; 332 -2.4; 365 -1.0; 402 -0.5; 442 -0.9; 486 -2.2; 535 -2.8; 588 -2.7; 647 -2.5; 712 -2.9; 783 -3.1; 861 -4.2; 947 -5.6; 1042 -7.1; 1146 -8.8; 1261 -11.0; 1387 -12.5; 1526 -13.2; 1678 -12.6; 1846 -10.4; 2031 -8.6; 2234 -6.5; 2457 -3.8; 2703 -2.0; 2973 -1.0; 3270 -1.0; 3597 -1.6; 3957 -3.0; 4353 -5.1; 4788 -6.8; 5267 -8.2; 5793 -6.4; 6373 -7.9; 7010 -9.8; 7711 -9.3; 8482 -10.0; 9330 -11.5; 10263 -10.9; 11289 -8.6; 12418 -7.3; 13660 -9.4; 15026 -13.6; 16529 -13.9; 18182 -11.3; 20000 -13.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cowin E7 Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cowin E7 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 1.96 | 7.3 dB  |
| Peaking | 497 Hz   | 0.88 | 5.6 dB  |
| Peaking | 1542 Hz  | 1.82 | -8.8 dB |
| Peaking | 3114 Hz  | 1.65 | 7.9 dB  |
| Peaking | 19958 Hz | 0.08 | -5.3 dB |
| Peaking | 38 Hz    | 3.45 | 2.7 dB  |
| Peaking | 69 Hz    | 1.86 | -3.3 dB |
| Peaking | 380 Hz   | 7.1  | 1.8 dB  |
| Peaking | 12606 Hz | 3.73 | 4.6 dB  |
| Peaking | 15689 Hz | 2.57 | -3.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.8 dB  |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | 1.2 dB  |
| Peaking | 500 Hz   | 1.41 | 6.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.0 dB |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.8 dB |
| Peaking | 16000 Hz | 1.41 | -8.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Cowin%20E7%20Pro/Cowin%20E7%20Pro.png)