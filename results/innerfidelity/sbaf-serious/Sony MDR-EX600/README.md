# Sony MDR-EX600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.7; 28 -1.0; 31 -1.3; 34 -1.5; 37 -1.8; 41 -2.1; 45 -2.4; 49 -2.6; 54 -3.0; 60 -3.3; 66 -3.8; 72 -4.1; 79 -4.5; 87 -5.0; 96 -5.6; 106 -5.9; 116 -6.1; 128 -6.5; 141 -6.8; 155 -7.0; 170 -7.2; 187 -7.4; 206 -7.5; 227 -7.6; 249 -7.6; 274 -7.5; 302 -7.4; 332 -7.3; 365 -7.1; 402 -7.1; 442 -6.8; 486 -6.7; 535 -6.5; 588 -5.9; 647 -5.7; 712 -5.7; 783 -5.5; 861 -5.8; 947 -6.1; 1042 -6.6; 1146 -7.1; 1261 -7.6; 1387 -8.4; 1526 -9.2; 1678 -9.6; 1846 -9.3; 2031 -8.3; 2234 -6.8; 2457 -4.3; 2703 -2.2; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.3; 4788 -6.3; 5267 -10.6; 5793 -7.0; 6373 -2.5; 7010 -4.0; 7711 -6.2; 8482 -6.6; 9330 -6.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-EX600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-EX600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 1.03 | 6.0 dB  |
| Peaking | 53 Hz    | 1.62 | 2.5 dB  |
| Peaking | 1760 Hz  | 2.24 | -4.4 dB |
| Peaking | 3258 Hz  | 1.97 | 7.4 dB  |
| Peaking | 22050 Hz | 2.29 | 1.2 dB  |
| Peaking | 242 Hz   | 1.11 | -1.3 dB |
| Peaking | 746 Hz   | 2.46 | 1.3 dB  |
| Peaking | 4208 Hz  | 5.98 | 3.3 dB  |
| Peaking | 5342 Hz  | 4.41 | -6.5 dB |
| Peaking | 6454 Hz  | 5.59 | 5.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-EX600/Sony%20MDR-EX600.png)