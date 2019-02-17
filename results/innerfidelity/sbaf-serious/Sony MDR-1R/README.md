# Sony MDR-1R
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.8; 34 -1.4; 37 -2.1; 41 -2.9; 45 -3.5; 49 -4.1; 54 -4.7; 60 -5.3; 66 -5.8; 72 -6.4; 79 -7.1; 87 -7.6; 96 -7.9; 106 -8.2; 116 -8.2; 128 -7.5; 141 -7.2; 155 -8.0; 170 -6.8; 187 -6.9; 206 -7.6; 227 -7.8; 249 -7.2; 274 -7.0; 302 -5.9; 332 -4.9; 365 -3.6; 402 -2.9; 442 -2.5; 486 -2.8; 535 -3.1; 588 -3.3; 647 -4.0; 712 -4.6; 783 -4.6; 861 -5.4; 947 -6.0; 1042 -6.7; 1146 -7.2; 1261 -7.7; 1387 -8.7; 1526 -9.6; 1678 -10.0; 1846 -9.5; 2031 -8.6; 2234 -6.9; 2457 -4.4; 2703 -2.4; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-1R GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-1R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 27 Hz   |  0.65 | 7.4 dB  |
| Peaking | 118 Hz  |  0.25 | -2.5 dB |
| Peaking | 469 Hz  |  1.11 | 5.4 dB  |
| Peaking | 1761 Hz |  1.62 | -6.3 dB |
| Peaking | 3744 Hz |  0.86 | 7.6 dB  |
| Peaking | 178 Hz  | 12.64 | 1.6 dB  |
| Peaking | 2951 Hz |  3.98 | 2.2 dB  |
| Peaking | 3499 Hz |  1.53 | -1.4 dB |
| Peaking | 6302 Hz |  2.21 | 5.8 dB  |
| Peaking | 7304 Hz |  1.51 | -4.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 4.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | -3.6 dB |
| Peaking | 4000 Hz  | 1.41 | 8.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-1R/Sony%20MDR-1R.png)