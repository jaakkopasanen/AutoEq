# Skullcandy Smokin Buds
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.7; 23 -1.3; 25 -1.9; 28 -2.7; 31 -3.4; 34 -3.9; 37 -4.5; 41 -5.1; 45 -5.8; 49 -6.3; 54 -6.9; 60 -7.6; 66 -8.2; 72 -8.8; 79 -9.3; 87 -9.7; 96 -10.3; 106 -10.5; 116 -10.7; 128 -11.0; 141 -11.3; 155 -11.6; 170 -11.5; 187 -11.6; 206 -11.5; 227 -11.3; 249 -11.1; 274 -10.8; 302 -10.4; 332 -9.9; 365 -9.4; 402 -9.1; 442 -8.9; 486 -8.6; 535 -8.2; 588 -8.0; 647 -7.5; 712 -7.4; 783 -7.2; 861 -7.3; 947 -7.1; 1042 -5.8; 1146 -3.4; 1261 -4.8; 1387 -6.5; 1526 -8.2; 1678 -10.6; 1846 -11.0; 2031 -11.0; 2234 -10.4; 2457 -8.8; 2703 -6.6; 2973 -3.9; 3270 -1.5; 3597 -0.5; 3957 -1.7; 4353 -4.9; 4788 -7.5; 5267 -9.4; 5793 -9.0; 6373 -6.5; 7010 -5.5; 7711 -7.5; 8482 -10.6; 9330 -8.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Smokin Buds GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Smokin Buds ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.8  | 6.2 dB  |
| Peaking | 163 Hz  | 0.53 | -5.4 dB |
| Peaking | 2043 Hz | 2.8  | -5.8 dB |
| Peaking | 3612 Hz | 2.56 | 7.5 dB  |
| Peaking | 5318 Hz | 2.89 | -4.2 dB |
| Peaking | 408 Hz  | 1.12 | -0.3 dB |
| Peaking | 1181 Hz | 5.25 | 4.1 dB  |
| Peaking | 1672 Hz | 8.16 | -2.1 dB |
| Peaking | 6908 Hz | 5.39 | 2.2 dB  |
| Peaking | 8566 Hz | 5.84 | -4.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.9 dB |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Skullcandy%20Smokin%20Buds/Skullcandy%20Smokin%20Buds.png)