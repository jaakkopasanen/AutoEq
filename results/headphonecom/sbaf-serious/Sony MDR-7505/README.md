# Sony MDR-7505
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.8; 116 -1.9; 128 -2.8; 141 -3.5; 155 -4.1; 170 -4.4; 187 -4.9; 206 -5.0; 227 -4.5; 249 -3.8; 274 -3.7; 302 -4.1; 332 -5.2; 365 -6.5; 402 -6.3; 442 -6.0; 486 -6.0; 535 -6.1; 588 -6.2; 647 -6.5; 712 -5.7; 783 -5.2; 861 -5.8; 947 -6.6; 1042 -6.2; 1146 -5.8; 1261 -6.2; 1387 -6.7; 1526 -7.2; 1678 -6.7; 1846 -6.2; 2031 -5.8; 2234 -5.5; 2457 -5.3; 2703 -4.4; 2973 -5.4; 3270 -5.8; 3597 -5.9; 3957 -6.0; 4353 -6.7; 4788 -5.9; 5267 -4.1; 5793 -4.5; 6373 -5.6; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7505 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7505 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 33 Hz    | 0.25 | 6.1 dB  |
| Peaking | 94 Hz    | 2.65 | 1.8 dB  |
| Peaking | 787 Hz   | 7.41 | 1.2 dB  |
| Peaking | 2657 Hz  | 3.97 | 1.8 dB  |
| Peaking | 5866 Hz  | 2.4  | 2.1 dB  |
| Peaking | 198 Hz   | 2.15 | -1.2 dB |
| Peaking | 244 Hz   | 3    | 0.8 dB  |
| Peaking | 287 Hz   | 2.75 | 1.7 dB  |
| Peaking | 365 Hz   | 4.48 | -1.4 dB |
| Peaking | 20858 Hz | 1.8  | -0.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 5.4 dB  |
| Peaking | 125 Hz   | 1.41 | 2.8 dB  |
| Peaking | 250 Hz   | 1.41 | 1.3 dB  |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-7505/Sony%20MDR-7505.png)