# Skullcandy Mix Master
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.4; 23 -2.2; 25 -2.9; 28 -3.8; 31 -4.5; 34 -4.9; 37 -5.3; 41 -5.6; 45 -5.8; 49 -6.0; 54 -6.2; 60 -6.3; 66 -6.3; 72 -6.4; 79 -6.8; 87 -7.2; 96 -7.7; 106 -7.8; 116 -8.0; 128 -8.3; 141 -8.6; 155 -8.8; 170 -8.7; 187 -9.0; 206 -9.2; 227 -9.1; 249 -8.8; 274 -8.3; 302 -8.0; 332 -8.0; 365 -7.5; 402 -7.6; 442 -7.1; 486 -6.6; 535 -5.8; 588 -5.0; 647 -4.9; 712 -5.1; 783 -5.1; 861 -5.9; 947 -6.5; 1042 -6.5; 1146 -6.7; 1261 -7.4; 1387 -8.7; 1526 -9.3; 1678 -9.5; 1846 -8.5; 2031 -7.9; 2234 -6.5; 2457 -4.6; 2703 -3.0; 2973 -1.7; 3270 -1.0; 3597 -4.5; 3957 -7.9; 4353 -5.7; 4788 -3.3; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Mix Master GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Mix Master ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.25 | 5.5 dB  |
| Peaking | 183 Hz  | 1.05 | -2.8 dB |
| Peaking | 1649 Hz | 3.13 | -3.6 dB |
| Peaking | 3018 Hz | 4.07 | 5.7 dB  |
| Peaking | 5765 Hz | 3.33 | 6.8 dB  |
| Peaking | 671 Hz  | 2.8  | 2.1 dB  |
| Peaking | 3396 Hz | 9.12 | 2.9 dB  |
| Peaking | 3899 Hz | 5.16 | -3.5 dB |
| Peaking | 4993 Hz | 8.34 | 2.0 dB  |
| Peaking | 8263 Hz | 4.79 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.8 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Skullcandy%20Mix%20Master/Skullcandy%20Mix%20Master.png)