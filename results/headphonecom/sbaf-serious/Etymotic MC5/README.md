# Etymotic MC5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.6; 54 -0.8; 60 -1.3; 66 -1.6; 72 -1.9; 79 -2.2; 87 -2.6; 96 -3.0; 106 -3.3; 116 -3.5; 128 -3.8; 141 -4.1; 155 -4.3; 170 -4.5; 187 -4.7; 206 -4.7; 227 -4.8; 249 -4.8; 274 -4.8; 302 -4.7; 332 -4.5; 365 -4.4; 402 -4.3; 442 -4.4; 486 -4.3; 535 -4.3; 588 -4.3; 647 -4.3; 712 -4.4; 783 -4.6; 861 -5.1; 947 -5.9; 1042 -6.8; 1146 -7.7; 1261 -8.8; 1387 -10.0; 1526 -11.3; 1678 -12.1; 1846 -11.4; 2031 -8.6; 2234 -7.8; 2457 -6.8; 2703 -5.3; 2973 -3.6; 3270 -1.8; 3597 -0.5; 3957 -0.5; 4353 -1.3; 4788 -1.4; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic MC5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic MC5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 32 Hz   |  0.34 | 6.2 dB  |
| Peaking | 617 Hz  |  0.66 | 2.5 dB  |
| Peaking | 1641 Hz |  1.71 | -6.9 dB |
| Peaking | 3705 Hz |  1.87 | 6.2 dB  |
| Peaking | 5784 Hz |  3.08 | 5.3 dB  |
| Peaking | 1116 Hz |  7.37 | -0.3 dB |
| Peaking | 1495 Hz | 11.24 | 0.4 dB  |
| Peaking | 6579 Hz |  8.12 | 1.9 dB  |
| Peaking | 7820 Hz |  2.37 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.5 dB  |
| Peaking | 62 Hz    | 1.41 | 4.0 dB  |
| Peaking | 125 Hz   | 1.41 | 1.7 dB  |
| Peaking | 250 Hz   | 1.41 | 0.8 dB  |
| Peaking | 500 Hz   | 1.41 | 2.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | -5.7 dB |
| Peaking | 4000 Hz  | 1.41 | 8.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Etymotic%20MC5/Etymotic%20MC5.png)