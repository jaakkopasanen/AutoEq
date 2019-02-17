# Koss KPH7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -1.4; 141 -3.6; 155 -5.5; 170 -7.6; 187 -9.2; 206 -11.0; 227 -11.8; 249 -12.4; 274 -12.3; 302 -11.4; 332 -10.2; 365 -10.0; 402 -8.7; 442 -7.3; 486 -4.2; 535 -8.7; 588 -7.1; 647 -5.4; 712 -7.9; 783 -7.1; 861 -6.7; 947 -6.5; 1042 -6.4; 1146 -6.3; 1261 -6.7; 1387 -7.3; 1526 -8.6; 1678 -9.0; 1846 -9.6; 2031 -11.0; 2234 -13.4; 2457 -14.5; 2703 -12.3; 2973 -9.5; 3270 -6.8; 3597 -5.7; 3957 -4.1; 4353 -0.8; 4788 -3.2; 5267 -2.4; 5793 -0.8; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -9.4; 9330 -10.6; 10263 -7.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss KPH7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss KPH7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 78 Hz   |  0.24 | 7.7 dB   |
| Peaking | 244 Hz  |  1.15 | -11.7 dB |
| Peaking | 2436 Hz |  2.02 | -9.9 dB  |
| Peaking | 5618 Hz |  0.79 | 6.8 dB   |
| Peaking | 8918 Hz |  2.45 | -7.6 dB  |
| Peaking | 16 Hz   |  0.67 | 2.5 dB   |
| Peaking | 113 Hz  |  0.3  | -3.0 dB  |
| Peaking | 149 Hz  |  0.9  | 6.4 dB   |
| Peaking | 167 Hz  |  2.28 | -4.5 dB  |
| Peaking | 480 Hz  | 14.78 | 4.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 4.9 dB  |
| Peaking | 125 Hz   | 1.41 | 5.6 dB  |
| Peaking | 250 Hz   | 1.41 | -8.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.4 dB |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20KPH7/Koss%20KPH7.png)