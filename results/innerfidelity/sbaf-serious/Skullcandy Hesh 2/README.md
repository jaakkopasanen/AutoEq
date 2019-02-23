# Skullcandy Hesh 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.1; 23 -6.7; 25 -7.1; 28 -7.6; 31 -8.0; 34 -8.2; 37 -8.4; 41 -8.6; 45 -8.7; 49 -8.7; 54 -8.8; 60 -8.8; 66 -8.9; 72 -9.0; 79 -9.1; 87 -9.1; 96 -8.9; 106 -9.1; 116 -8.9; 128 -8.7; 141 -9.4; 155 -9.8; 170 -9.4; 187 -9.2; 206 -9.3; 227 -9.5; 249 -9.4; 274 -9.3; 302 -9.2; 332 -9.0; 365 -8.7; 402 -8.9; 442 -9.3; 486 -10.1; 535 -10.7; 588 -10.7; 647 -11.1; 712 -11.4; 783 -11.2; 861 -11.3; 947 -11.2; 1042 -11.0; 1146 -10.6; 1261 -10.2; 1387 -10.1; 1526 -10.0; 1678 -9.4; 1846 -8.5; 2031 -7.3; 2234 -6.0; 2457 -4.3; 2703 -2.7; 2973 -2.7; 3270 -2.6; 3597 -0.5; 3957 -0.5; 4353 -2.0; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.5; 10263 -6.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Hesh 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Hesh 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 97 Hz   |  0.33 | -2.5 dB |
| Peaking | 1197 Hz |  0.49 | -6.3 dB |
| Peaking | 4573 Hz |  0.51 | 8.8 dB  |
| Peaking | 8900 Hz |  1.2  | -5.3 dB |
| Peaking | 382 Hz  |  6.42 | 0.8 dB  |
| Peaking | 1804 Hz |  4.76 | -0.8 dB |
| Peaking | 2673 Hz |  7.37 | 1.3 dB  |
| Peaking | 4360 Hz | 11.37 | -1.8 dB |
| Peaking | 6201 Hz |  7.98 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.0 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | -2.5 dB |
| Peaking | 1000 Hz  | 1.41 | -4.9 dB |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Skullcandy%20Hesh%202/Skullcandy%20Hesh%202.png)