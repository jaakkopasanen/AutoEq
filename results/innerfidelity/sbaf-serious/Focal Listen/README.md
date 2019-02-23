# Focal Listen
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.7; 23 -6.0; 25 -6.2; 28 -6.4; 31 -6.5; 34 -6.6; 37 -6.6; 41 -6.4; 45 -6.3; 49 -6.0; 54 -5.6; 60 -5.0; 66 -4.4; 72 -3.8; 79 -3.2; 87 -2.6; 96 -2.3; 106 -2.6; 116 -3.4; 128 -4.9; 141 -6.0; 155 -6.4; 170 -6.8; 187 -8.4; 206 -9.1; 227 -9.4; 249 -9.6; 274 -9.6; 302 -9.5; 332 -9.4; 365 -9.1; 402 -8.8; 442 -8.6; 486 -8.7; 535 -8.7; 588 -8.2; 647 -8.1; 712 -8.1; 783 -7.5; 861 -7.0; 947 -7.3; 1042 -7.6; 1146 -7.6; 1261 -7.6; 1387 -7.9; 1526 -8.4; 1678 -8.7; 1846 -8.6; 2031 -8.0; 2234 -7.1; 2457 -5.5; 2703 -4.3; 2973 -2.1; 3270 -0.6; 3597 -0.9; 3957 -0.9; 4353 -4.4; 4788 -6.2; 5267 -2.2; 5793 -0.5; 6373 -0.9; 7010 -3.9; 7711 -6.1; 8482 -7.9; 9330 -8.8; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Listen GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Listen ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 98 Hz   |  1.43 | 5.1 dB  |
| Peaking | 267 Hz  |  0.76 | -3.6 dB |
| Peaking | 3422 Hz |  1.75 | 11.3 dB |
| Peaking | 3625 Hz |  0.48 | -5.4 dB |
| Peaking | 6027 Hz |  3.05 | 8.7 dB  |
| Peaking | 1763 Hz |  2.23 | -2.4 dB |
| Peaking | 1796 Hz |  1.06 | 1.6 dB  |
| Peaking | 4644 Hz | 13.23 | -3.2 dB |
| Peaking | 9037 Hz |  4.94 | -3.4 dB |
| Peaking | 9932 Hz |  1.17 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.0 dB |
| Peaking | 62 Hz    | 1.41 | 2.2 dB  |
| Peaking | 125 Hz   | 1.41 | 2.9 dB  |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Listen/Focal%20Listen.png)