# Onkyo E900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.2; 23 -4.5; 25 -4.8; 28 -5.2; 31 -5.5; 34 -5.7; 37 -6.0; 41 -6.3; 45 -6.5; 49 -6.8; 54 -7.0; 60 -7.4; 66 -7.7; 72 -8.1; 79 -8.4; 87 -8.8; 96 -9.2; 106 -9.5; 116 -9.8; 128 -10.0; 141 -10.1; 155 -10.2; 170 -10.2; 187 -10.2; 206 -10.0; 227 -9.8; 249 -9.6; 274 -9.4; 302 -9.1; 332 -8.9; 365 -8.6; 402 -8.4; 442 -8.2; 486 -8.0; 535 -7.8; 588 -7.6; 647 -7.3; 712 -6.9; 783 -6.5; 861 -6.1; 947 -5.9; 1042 -6.0; 1146 -6.4; 1261 -6.8; 1387 -6.8; 1526 -6.4; 1678 -5.6; 1846 -4.8; 2031 -4.1; 2234 -3.8; 2457 -3.6; 2703 -3.2; 2973 -2.1; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -2.9; 5267 -4.6; 5793 -5.8; 6373 -10.0; 7010 -13.0; 7711 -9.1; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -8.9; 13660 -10.2; 15026 -9.5; 16529 -9.9; 18182 -11.7; 20000 -11.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Onkyo E900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Onkyo E900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.65 | 3.1 dB  |
| Peaking | 110 Hz  | 1.07 | -0.8 dB |
| Peaking | 188 Hz  | 0.57 | -3.4 dB |
| Peaking | 3737 Hz | 1.27 | 6.7 dB  |
| Peaking | 6871 Hz | 4.33 | -8.5 dB |
| Peaking | 974 Hz  | 1.99 | 2.2 dB  |
| Peaking | 1364 Hz | 0.89 | -2.3 dB |
| Peaking | 2026 Hz | 1.55 | 2.2 dB  |
| Peaking | 2637 Hz | 3.8  | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.7 dB  |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.6 dB |
| Peaking | 16000 Hz | 1.41 | -4.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Onkyo%20E900/Onkyo%20E900.png)