# Focal Listen
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.7; 23 -5.0; 25 -5.2; 28 -5.4; 31 -5.5; 34 -5.5; 37 -5.5; 41 -5.4; 45 -5.2; 49 -5.0; 54 -4.6; 60 -4.0; 66 -3.4; 72 -2.8; 79 -2.1; 87 -1.6; 96 -1.3; 106 -1.5; 116 -2.3; 128 -3.8; 141 -4.9; 155 -5.4; 170 -5.8; 187 -7.4; 206 -8.0; 227 -8.3; 249 -8.5; 274 -8.6; 302 -8.5; 332 -8.4; 365 -8.0; 402 -7.8; 442 -7.5; 486 -7.7; 535 -7.7; 588 -7.2; 647 -7.1; 712 -7.0; 783 -6.5; 861 -5.9; 947 -6.3; 1042 -6.6; 1146 -6.6; 1261 -6.5; 1387 -6.9; 1526 -7.4; 1678 -7.7; 1846 -7.6; 2031 -7.0; 2234 -6.0; 2457 -4.5; 2703 -3.3; 2973 -1.1; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -3.4; 4788 -5.2; 5267 -1.2; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.0; 9330 -7.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Listen GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Listen ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 18 Hz   |  1.47 | 1.8 dB  |
| Peaking | 97 Hz   |  1.12 | 6.0 dB  |
| Peaking | 248 Hz  |  0.77 | -2.9 dB |
| Peaking | 3423 Hz |  2.58 | 6.7 dB  |
| Peaking | 5917 Hz |  3.92 | 6.1 dB  |
| Peaking | 868 Hz  |  5.41 | 1.0 dB  |
| Peaking | 1811 Hz |  2.53 | -1.8 dB |
| Peaking | 2770 Hz |  4.39 | 1.2 dB  |
| Peaking | 6722 Hz | 12.31 | 1.5 dB  |
| Peaking | 9032 Hz |  4.25 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.2 dB  |
| Peaking | 62 Hz    | 1.41 | 3.1 dB  |
| Peaking | 125 Hz   | 1.41 | 3.8 dB  |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Listen/Focal%20Listen.png)