# Koss KPH7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.9; 141 -3.1; 155 -5.1; 170 -7.1; 187 -8.7; 206 -10.5; 227 -11.4; 249 -12.0; 274 -11.8; 302 -10.9; 332 -9.7; 365 -9.5; 402 -8.2; 442 -6.8; 486 -3.7; 535 -8.3; 588 -6.7; 647 -5.0; 712 -7.5; 783 -6.6; 861 -6.2; 947 -6.1; 1042 -5.9; 1146 -5.9; 1261 -6.3; 1387 -6.9; 1526 -8.1; 1678 -8.5; 1846 -9.2; 2031 -10.5; 2234 -12.9; 2457 -14.0; 2703 -11.8; 2973 -9.0; 3270 -6.3; 3597 -5.3; 3957 -3.6; 4353 -0.7; 4788 -2.7; 5267 -1.9; 5793 -0.7; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.9; 9330 -10.1; 10263 -7.3; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss KPH7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss KPH7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 83 Hz   |  0.21 | 7.7 dB   |
| Peaking | 246 Hz  |  1.16 | -11.7 dB |
| Peaking | 2439 Hz |  2.14 | -9.6 dB  |
| Peaking | 5508 Hz |  0.8  | 6.9 dB   |
| Peaking | 8930 Hz |  2.36 | -7.0 dB  |
| Peaking | 19 Hz   |  1.28 | 2.2 dB   |
| Peaking | 56 Hz   |  0.27 | -1.0 dB  |
| Peaking | 119 Hz  |  3.28 | 2.5 dB   |
| Peaking | 485 Hz  | 11.39 | 3.9 dB   |
| Peaking | 533 Hz  | 10.1  | -2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 4.8 dB  |
| Peaking | 125 Hz   | 1.41 | 5.7 dB  |
| Peaking | 250 Hz   | 1.41 | -7.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.0 dB |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20KPH7/Koss%20KPH7.png)