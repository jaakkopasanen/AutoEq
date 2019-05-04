# Oppo PM3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.5; 23 -2.3; 25 -2.1; 28 -1.8; 31 -1.5; 34 -1.3; 37 -1.1; 41 -0.9; 45 -0.8; 49 -0.8; 54 -0.9; 60 -1.3; 66 -1.8; 72 -2.4; 79 -3.0; 87 -3.5; 96 -4.1; 106 -4.5; 116 -4.9; 128 -5.2; 141 -5.4; 155 -5.4; 170 -5.3; 187 -5.1; 206 -4.7; 227 -4.2; 249 -3.7; 274 -3.1; 302 -2.5; 332 -2.1; 365 -1.9; 402 -2.1; 442 -2.5; 486 -3.1; 535 -3.7; 588 -4.2; 647 -4.3; 712 -3.9; 783 -3.4; 861 -2.4; 947 -1.6; 1042 -1.4; 1146 -2.5; 1261 -3.4; 1387 -3.8; 1526 -4.4; 1678 -4.9; 1846 -5.8; 2031 -6.1; 2234 -6.9; 2457 -6.5; 2703 -6.2; 2973 -5.5; 3270 -4.7; 3597 -4.2; 3957 -3.7; 4353 -4.1; 4788 -3.3; 5267 -1.4; 5793 -0.5; 6373 -3.5; 7010 -9.4; 7711 -11.3; 8482 -11.8; 9330 -10.1; 10263 -5.6; 11289 -4.5; 12418 -4.5; 13660 -4.5; 15026 -4.5; 16529 -4.5; 18182 -4.5; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oppo PM3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 42 Hz    | 1.17 | 4.2 dB  |
| Peaking | 369 Hz   | 2.53 | 2.8 dB  |
| Peaking | 998 Hz   | 3.82 | 3.4 dB  |
| Peaking | 5768 Hz  | 3.67 | 6.7 dB  |
| Peaking | 7959 Hz  | 2.28 | -8.8 dB |
| Peaking | 19 Hz    | 2.03 | 0.9 dB  |
| Peaking | 66 Hz    | 3.58 | 0.9 dB  |
| Peaking | 145 Hz   | 2.03 | -1.5 dB |
| Peaking | 2290 Hz  | 3.01 | -2.6 dB |
| Peaking | 11133 Hz | 5.07 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | 3.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | 1.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Oppo%20PM3/Oppo%20PM3.png)