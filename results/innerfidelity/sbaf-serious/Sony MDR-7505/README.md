# Sony MDR-7505
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.6; 72 -1.5; 79 -2.4; 87 -3.4; 96 -4.5; 106 -5.0; 116 -5.0; 128 -4.9; 141 -5.8; 155 -6.6; 170 -6.5; 187 -6.8; 206 -6.8; 227 -6.8; 249 -6.8; 274 -6.4; 302 -6.7; 332 -7.1; 365 -7.7; 402 -7.8; 442 -7.7; 486 -8.6; 535 -9.0; 588 -9.1; 647 -9.7; 712 -9.6; 783 -7.9; 861 -9.0; 947 -9.4; 1042 -9.4; 1146 -8.9; 1261 -8.5; 1387 -8.1; 1526 -7.8; 1678 -7.1; 1846 -6.7; 2031 -6.1; 2234 -5.9; 2457 -5.8; 2703 -5.3; 2973 -6.3; 3270 -6.7; 3597 -6.8; 3957 -6.7; 4353 -7.5; 4788 -6.5; 5267 -3.8; 5793 -2.8; 6373 -2.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7505 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7505 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.54 | 6.8 dB  |
| Peaking | 1021 Hz | 3.25 | -0.3 dB |
| Peaking | 1650 Hz | 0.25 | -3.7 dB |
| Peaking | 2285 Hz | 1.05 | 4.3 dB  |
| Peaking | 6150 Hz | 2.7  | 6.0 dB  |
| Peaking | 38 Hz   | 2.79 | -0.9 dB |
| Peaking | 65 Hz   | 3.51 | 1.6 dB  |
| Peaking | 175 Hz  | 0.93 | -0.9 dB |
| Peaking | 290 Hz  | 1.84 | 1.2 dB  |
| Peaking | 658 Hz  | 7.8  | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 5.0 dB  |
| Peaking | 125 Hz   | 1.41 | -0.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | -2.9 dB |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-7505/Sony%20MDR-7505.png)