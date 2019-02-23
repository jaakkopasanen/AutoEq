# Sony MDR-SA3000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.8; 66 -1.7; 72 -2.5; 79 -3.3; 87 -4.0; 96 -4.4; 106 -5.2; 116 -5.7; 128 -6.2; 141 -6.5; 155 -6.8; 170 -6.5; 187 -6.6; 206 -6.6; 227 -6.4; 249 -6.5; 274 -6.5; 302 -6.7; 332 -6.9; 365 -7.4; 402 -7.4; 442 -7.7; 486 -8.2; 535 -8.7; 588 -8.5; 647 -9.2; 712 -9.6; 783 -9.4; 861 -9.1; 947 -8.3; 1042 -7.1; 1146 -5.9; 1261 -4.5; 1387 -3.8; 1526 -3.7; 1678 -3.5; 1846 -4.3; 2031 -5.5; 2234 -8.3; 2457 -9.3; 2703 -9.6; 2973 -8.6; 3270 -7.1; 3597 -3.7; 3957 -0.5; 4353 -2.2; 4788 -5.0; 5267 -0.6; 5793 -1.2; 6373 -1.9; 7010 -6.2; 7711 -8.4; 8482 -11.4; 9330 -11.9; 10263 -6.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-SA3000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-SA3000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.71 | 7.0 dB  |
| Peaking | 2732 Hz | 4.26 | -4.1 dB |
| Peaking | 3968 Hz | 5.86 | 6.1 dB  |
| Peaking | 5789 Hz | 3.02 | 6.4 dB  |
| Peaking | 8769 Hz | 3.74 | -6.8 dB |
| Peaking | 38 Hz   | 2.98 | -1.3 dB |
| Peaking | 59 Hz   | 2.12 | 1.6 dB  |
| Peaking | 142 Hz  | 2.26 | -1.0 dB |
| Peaking | 761 Hz  | 1.04 | -3.5 dB |
| Peaking | 1450 Hz | 2.09 | 4.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.5 dB  |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | -2.6 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-SA3000/Sony%20MDR-SA3000.png)