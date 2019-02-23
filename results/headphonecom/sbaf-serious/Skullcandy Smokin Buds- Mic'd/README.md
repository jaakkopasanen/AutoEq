# Skullcandy Smokin Buds- Mic'd
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.0; 31 -1.6; 34 -2.2; 37 -2.8; 41 -3.4; 45 -4.0; 49 -4.6; 54 -5.2; 60 -5.9; 66 -6.5; 72 -7.1; 79 -7.6; 87 -8.0; 96 -8.5; 106 -8.8; 116 -9.0; 128 -9.3; 141 -9.6; 155 -9.9; 170 -9.8; 187 -9.9; 206 -9.8; 227 -9.6; 249 -9.3; 274 -9.0; 302 -8.6; 332 -8.2; 365 -7.7; 402 -7.4; 442 -7.2; 486 -6.9; 535 -6.5; 588 -6.3; 647 -5.8; 712 -5.6; 783 -5.4; 861 -5.6; 947 -5.4; 1042 -4.1; 1146 -1.7; 1261 -3.1; 1387 -4.8; 1526 -6.5; 1678 -8.9; 1846 -9.3; 2031 -9.3; 2234 -8.6; 2457 -7.1; 2703 -4.9; 2973 -2.2; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -3.1; 4788 -5.8; 5267 -7.7; 5793 -7.3; 6373 -4.8; 7010 -4.2; 7711 -6.3; 8482 -8.9; 9330 -7.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Smokin Buds- Mic'd GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Smokin Buds- Mic'd ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.78 | 6.3 dB  |
| Peaking | 160 Hz  | 0.68 | -3.7 dB |
| Peaking | 1211 Hz | 2.03 | 5.7 dB  |
| Peaking | 1879 Hz | 1.56 | -5.2 dB |
| Peaking | 3437 Hz | 2.42 | 7.7 dB  |
| Peaking | 640 Hz  | 3.64 | 0.8 dB  |
| Peaking | 4096 Hz | 7.97 | 2.2 dB  |
| Peaking | 5483 Hz | 3.3  | -3.3 dB |
| Peaking | 6648 Hz | 3.88 | 3.4 dB  |
| Peaking | 8542 Hz | 6.32 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.5 dB |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Skullcandy%20Smokin%20Buds-%20Mic'd/Skullcandy%20Smokin%20Buds-%20Mic'd.png)