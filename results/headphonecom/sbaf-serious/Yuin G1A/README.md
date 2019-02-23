# Yuin G1A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -1.0; 60 -2.2; 66 -3.3; 72 -4.0; 79 -4.4; 87 -5.5; 96 -6.3; 106 -7.0; 116 -7.5; 128 -8.0; 141 -8.3; 155 -8.7; 170 -8.5; 187 -8.4; 206 -8.4; 227 -8.2; 249 -7.9; 274 -7.9; 302 -7.5; 332 -7.1; 365 -6.8; 402 -6.5; 442 -6.3; 486 -6.1; 535 -5.7; 588 -5.7; 647 -5.5; 712 -5.3; 783 -5.3; 861 -5.3; 947 -5.6; 1042 -6.0; 1146 -6.3; 1261 -6.4; 1387 -6.7; 1526 -7.2; 1678 -8.6; 1846 -9.4; 2031 -10.1; 2234 -10.0; 2457 -9.5; 2703 -6.9; 2973 -4.0; 3270 -0.5; 3597 -0.5; 3957 -2.3; 4353 -8.8; 4788 -14.4; 5267 -9.6; 5793 -4.9; 6373 -1.0; 7010 -4.4; 7711 -6.2; 8482 -7.4; 9330 -9.9; 10263 -8.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yuin G1A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yuin G1A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 34 Hz   | 1.01 | 7.2 dB   |
| Peaking | 2249 Hz | 2.24 | -5.7 dB  |
| Peaking | 3595 Hz | 2.16 | 10.0 dB  |
| Peaking | 4746 Hz | 3.64 | -11.8 dB |
| Peaking | 6278 Hz | 5.94 | 7.0 dB   |
| Peaking | 33 Hz   | 1.57 | -5.9 dB  |
| Peaking | 35 Hz   | 0.38 | 5.0 dB   |
| Peaking | 137 Hz  | 0.64 | -3.9 dB  |
| Peaking | 702 Hz  | 1.17 | 1.5 dB   |
| Peaking | 9504 Hz | 5.83 | -4.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | 3.5 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Yuin%20G1A/Yuin%20G1A.png)