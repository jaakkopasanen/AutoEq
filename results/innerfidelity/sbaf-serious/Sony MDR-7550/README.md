# Sony MDR-7550
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.1; 23 -2.4; 25 -2.7; 28 -3.0; 31 -3.2; 34 -3.5; 37 -3.7; 41 -4.0; 45 -4.2; 49 -4.4; 54 -4.7; 60 -5.1; 66 -5.5; 72 -5.8; 79 -6.2; 87 -6.6; 96 -7.1; 106 -7.4; 116 -7.6; 128 -8.0; 141 -8.3; 155 -8.5; 170 -8.6; 187 -8.8; 206 -8.8; 227 -8.8; 249 -8.8; 274 -8.6; 302 -8.6; 332 -8.4; 365 -8.2; 402 -8.0; 442 -7.6; 486 -7.5; 535 -7.3; 588 -6.8; 647 -6.6; 712 -6.5; 783 -6.3; 861 -6.6; 947 -6.9; 1042 -7.1; 1146 -7.2; 1261 -8.1; 1387 -9.2; 1526 -10.2; 1678 -10.7; 1846 -10.4; 2031 -9.5; 2234 -8.0; 2457 -5.6; 2703 -3.2; 2973 -0.7; 3270 -0.5; 3597 -0.5; 3957 -0.7; 4353 -4.6; 4788 -8.9; 5267 -9.1; 5793 -3.7; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7550 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7550 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 15 Hz   |  0.33 | 4.6 dB  |
| Peaking | 195 Hz  |  0.7  | -2.7 dB |
| Peaking | 1762 Hz |  2.13 | -5.1 dB |
| Peaking | 3259 Hz |  2.65 | 7.6 dB  |
| Peaking | 6376 Hz |  8.15 | 5.8 dB  |
| Peaking | 768 Hz  |  3.21 | 0.8 dB  |
| Peaking | 4056 Hz |  5.96 | 4.2 dB  |
| Peaking | 5100 Hz |  3.17 | -5.8 dB |
| Peaking | 5789 Hz |  7.08 | 4.0 dB  |
| Peaking | 6940 Hz | 11.2  | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-7550/Sony%20MDR-7550.png)