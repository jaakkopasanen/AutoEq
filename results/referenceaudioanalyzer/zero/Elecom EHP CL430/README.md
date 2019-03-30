# Elecom EHP CL430
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.7; 45 -2.0; 49 -3.3; 54 -4.6; 60 -5.5; 66 -6.2; 72 -6.9; 79 -7.7; 87 -8.3; 96 -8.7; 106 -9.0; 116 -9.0; 128 -9.0; 141 -9.0; 155 -9.0; 170 -9.0; 187 -9.0; 206 -8.8; 227 -8.6; 249 -8.6; 274 -8.6; 302 -8.6; 332 -8.6; 365 -8.6; 402 -8.6; 442 -8.6; 486 -8.6; 535 -8.6; 588 -8.6; 647 -8.6; 712 -8.7; 783 -8.6; 861 -8.3; 947 -7.7; 1042 -6.8; 1146 -6.0; 1261 -7.0; 1387 -9.2; 1526 -11.0; 1678 -11.4; 1846 -10.5; 2031 -8.8; 2234 -6.6; 2457 -3.6; 2703 -1.1; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.8; 5267 -6.6; 5793 -9.1; 6373 -8.4; 7010 -6.9; 7711 -7.5; 8482 -7.8; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Elecom EHP CL430 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Elecom EHP CL430 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 31 Hz   |  0.86 | 8.6 dB  |
| Peaking | 146 Hz  |  0.2  | -3.1 dB |
| Peaking | 1751 Hz |  2.41 | -7.5 dB |
| Peaking | 4014 Hz |  0.83 | 10.4 dB |
| Peaking | 5998 Hz |  1.46 | -8.4 dB |
| Peaking | 767 Hz  |  2.97 | -0.9 dB |
| Peaking | 1158 Hz |  6.2  | 2.0 dB  |
| Peaking | 2749 Hz |  1.7  | -2.0 dB |
| Peaking | 2759 Hz |  4.29 | 3.4 dB  |
| Peaking | 6912 Hz | 10.2  | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.0 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Elecom%20EHP%20CL430/Elecom%20EHP%20CL430.png)