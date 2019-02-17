# Sony MDR-EX1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.0; 23 -2.3; 25 -2.5; 28 -2.8; 31 -3.0; 34 -3.2; 37 -3.4; 41 -3.6; 45 -3.8; 49 -4.0; 54 -4.3; 60 -4.6; 66 -5.0; 72 -5.4; 79 -5.8; 87 -6.2; 96 -6.6; 106 -6.9; 116 -7.2; 128 -7.5; 141 -7.9; 155 -8.1; 170 -8.2; 187 -8.2; 206 -8.4; 227 -8.3; 249 -8.3; 274 -8.2; 302 -8.0; 332 -7.9; 365 -7.7; 402 -7.6; 442 -7.2; 486 -7.1; 535 -6.8; 588 -6.3; 647 -6.0; 712 -6.0; 783 -5.6; 861 -5.9; 947 -6.2; 1042 -6.6; 1146 -7.2; 1261 -7.8; 1387 -8.7; 1526 -9.6; 1678 -10.2; 1846 -10.1; 2031 -9.5; 2234 -8.3; 2457 -6.2; 2703 -4.3; 2973 -1.7; 3270 -0.5; 3597 -0.5; 3957 -1.7; 4353 -6.1; 4788 -11.0; 5267 -12.3; 5793 -7.7; 6373 -5.1; 7010 -6.1; 7711 -10.3; 8482 -10.9; 9330 -7.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-EX1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-EX1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.99 | 4.4 dB  |
| Peaking | 1836 Hz | 1.91 | -4.9 dB |
| Peaking | 3441 Hz | 2.1  | 8.0 dB  |
| Peaking | 4938 Hz | 4.55 | -3.2 dB |
| Peaking | 5086 Hz | 4.75 | -5.4 dB |
| Peaking | 60 Hz   | 1.45 | 1.3 dB  |
| Peaking | 210 Hz  | 0.61 | -2.0 dB |
| Peaking | 756 Hz  | 1.91 | 1.5 dB  |
| Peaking | 6527 Hz | 5.24 | 2.8 dB  |
| Peaking | 8085 Hz | 4.95 | -5.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.2 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-EX1000/Sony%20MDR-EX1000.png)