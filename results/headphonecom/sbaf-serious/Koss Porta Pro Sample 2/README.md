# Koss Porta Pro sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.7; 34 -1.3; 37 -2.1; 41 -3.1; 45 -4.1; 49 -5.0; 54 -6.0; 60 -7.0; 66 -8.0; 72 -8.9; 79 -9.6; 87 -10.3; 96 -10.8; 106 -11.2; 116 -11.2; 128 -11.4; 141 -11.2; 155 -11.2; 170 -11.0; 187 -10.6; 206 -10.0; 227 -9.7; 249 -9.2; 274 -8.9; 302 -8.4; 332 -8.0; 365 -7.4; 402 -6.8; 442 -6.5; 486 -6.3; 535 -6.0; 588 -5.7; 647 -5.4; 712 -5.3; 783 -5.1; 861 -5.2; 947 -5.3; 1042 -5.4; 1146 -5.6; 1261 -6.0; 1387 -6.8; 1526 -7.7; 1678 -8.6; 1846 -9.4; 2031 -10.1; 2234 -10.1; 2457 -8.8; 2703 -6.7; 2973 -4.3; 3270 -2.7; 3597 -2.1; 3957 -3.7; 4353 -5.5; 4788 -7.6; 5267 -5.8; 5793 -2.9; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -8.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -9.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss Porta Pro sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Porta Pro sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.53 | 8.1 dB  |
| Peaking | 105 Hz  | 0.44 | -6.8 dB |
| Peaking | 1744 Hz | 0.27 | 3.6 dB  |
| Peaking | 2093 Hz | 1.19 | -7.4 dB |
| Peaking | 3320 Hz | 3.37 | 4.5 dB  |
| Peaking | 3784 Hz | 8.39 | 1.3 dB  |
| Peaking | 4842 Hz | 4.32 | -3.2 dB |
| Peaking | 6261 Hz | 4.87 | 5.3 dB  |
| Peaking | 9051 Hz | 2.71 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.5 dB  |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Koss%20Porta%20Pro%20sample%202/Koss%20Porta%20Pro%20sample%202.png)