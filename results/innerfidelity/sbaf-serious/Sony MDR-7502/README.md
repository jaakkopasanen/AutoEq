# Sony MDR-7502
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -1.3; 155 -2.3; 170 -2.1; 187 -2.9; 206 -3.1; 227 -3.5; 249 -3.7; 274 -3.8; 302 -3.7; 332 -3.5; 365 -4.0; 402 -4.1; 442 -4.5; 486 -5.2; 535 -5.4; 588 -5.1; 647 -5.2; 712 -5.4; 783 -5.5; 861 -6.0; 947 -6.4; 1042 -6.7; 1146 -7.3; 1261 -7.9; 1387 -8.2; 1526 -9.0; 1678 -10.0; 1846 -10.1; 2031 -9.8; 2234 -9.4; 2457 -7.8; 2703 -6.4; 2973 -5.0; 3270 -4.1; 3597 -3.4; 3957 -2.1; 4353 -1.3; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.6; 9330 -9.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7502 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7502 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.09 | 5.7 dB  |
| Peaking | 183 Hz  | 0.24 | 1.5 dB  |
| Peaking | 1914 Hz | 1.35 | -5.4 dB |
| Peaking | 5651 Hz | 0.81 | 8.5 dB  |
| Peaking | 8476 Hz | 1.42 | -6.0 dB |
| Peaking | 121 Hz  | 1.8  | 1.6 dB  |
| Peaking | 282 Hz  | 0.38 | -1.6 dB |
| Peaking | 455 Hz  | 0.84 | 2.3 dB  |
| Peaking | 504 Hz  | 3.35 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.5 dB  |
| Peaking | 125 Hz   | 1.41 | 4.8 dB  |
| Peaking | 250 Hz   | 1.41 | 1.9 dB  |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.3 dB |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-7502/Sony%20MDR-7502.png)