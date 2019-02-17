# Sony MDR-ZX1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.9; 66 -1.9; 72 -2.8; 79 -3.6; 87 -4.3; 96 -4.7; 106 -5.0; 116 -5.5; 128 -6.2; 141 -6.7; 155 -6.6; 170 -5.7; 187 -5.5; 206 -5.2; 227 -4.8; 249 -4.7; 274 -4.8; 302 -5.1; 332 -6.0; 365 -6.7; 402 -7.0; 442 -7.1; 486 -7.2; 535 -7.1; 588 -6.7; 647 -6.4; 712 -6.6; 783 -6.4; 861 -6.4; 947 -6.5; 1042 -6.5; 1146 -6.8; 1261 -7.2; 1387 -8.3; 1526 -9.6; 1678 -10.8; 1846 -11.3; 2031 -11.1; 2234 -10.3; 2457 -9.1; 2703 -7.8; 2973 -6.3; 3270 -4.7; 3597 -1.8; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -1.0; 6373 -1.0; 7010 -4.0; 7711 -6.8; 8482 -11.8; 9330 -13.4; 10263 -9.4; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-ZX1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-ZX1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 35 Hz   | 0.66 | 6.8 dB   |
| Peaking | 254 Hz  | 3.79 | 1.8 dB   |
| Peaking | 2117 Hz | 1.33 | -7.8 dB  |
| Peaking | 4948 Hz | 0.67 | 8.3 dB   |
| Peaking | 8992 Hz | 2.68 | -11.3 dB |
| Peaking | 59 Hz   | 4.52 | 1.4 dB   |
| Peaking | 138 Hz  | 4.27 | -1.4 dB  |
| Peaking | 470 Hz  | 2.97 | -1.0 dB  |
| Peaking | 1162 Hz | 1.12 | 0.8 dB   |
| Peaking | 1623 Hz | 4.32 | -1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | 1.9 dB  |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.2 dB |
| Peaking | 4000 Hz  | 1.41 | 8.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-ZX1000/Sony%20MDR-ZX1000.png)