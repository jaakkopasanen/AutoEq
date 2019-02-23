# Sony MDR-ZX1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -1.5; 66 -2.6; 72 -3.5; 79 -4.3; 87 -5.0; 96 -5.4; 106 -5.7; 116 -6.2; 128 -6.9; 141 -7.3; 155 -7.3; 170 -6.4; 187 -6.1; 206 -5.9; 227 -5.5; 249 -5.4; 274 -5.5; 302 -5.8; 332 -6.7; 365 -7.4; 402 -7.7; 442 -7.8; 486 -7.9; 535 -7.8; 588 -7.4; 647 -7.1; 712 -7.3; 783 -7.1; 861 -7.1; 947 -7.2; 1042 -7.2; 1146 -7.5; 1261 -7.9; 1387 -8.9; 1526 -10.3; 1678 -11.5; 1846 -12.0; 2031 -11.8; 2234 -11.0; 2457 -9.8; 2703 -8.5; 2973 -7.0; 3270 -5.4; 3597 -2.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.7; 5793 -1.7; 6373 -1.0; 7010 -4.0; 7711 -7.2; 8482 -12.5; 9330 -14.1; 10263 -10.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-ZX1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-ZX1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 34 Hz   | 0.75 | 6.9 dB   |
| Peaking | 468 Hz  | 2.94 | -1.5 dB  |
| Peaking | 2133 Hz | 1.18 | -8.7 dB  |
| Peaking | 4884 Hz | 0.66 | 8.6 dB   |
| Peaking | 8997 Hz | 2.7  | -12.1 dB |
| Peaking | 56 Hz   | 4.27 | 1.7 dB   |
| Peaking | 139 Hz  | 2.36 | -1.7 dB  |
| Peaking | 246 Hz  | 2.84 | 1.3 dB   |
| Peaking | 3143 Hz | 6.97 | -1.3 dB  |
| Peaking | 3855 Hz | 8.24 | 1.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 3.7 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | 1.4 dB  |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.9 dB |
| Peaking | 4000 Hz  | 1.41 | 8.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-ZX1000/Sony%20MDR-ZX1000.png)