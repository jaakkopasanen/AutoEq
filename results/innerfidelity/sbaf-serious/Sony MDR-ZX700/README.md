# Sony MDR-ZX700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.7; 49 -1.7; 54 -3.3; 60 -5.1; 66 -6.4; 72 -7.2; 79 -7.9; 87 -8.2; 96 -9.0; 106 -9.4; 116 -9.3; 128 -10.1; 141 -10.4; 155 -10.2; 170 -8.9; 187 -9.7; 206 -9.9; 227 -9.7; 249 -9.7; 274 -9.4; 302 -9.2; 332 -10.2; 365 -9.2; 402 -8.8; 442 -8.4; 486 -8.2; 535 -7.7; 588 -6.8; 647 -6.2; 712 -6.0; 783 -5.8; 861 -5.8; 947 -6.2; 1042 -6.7; 1146 -7.2; 1261 -7.7; 1387 -9.1; 1526 -10.7; 1678 -12.6; 1846 -14.0; 2031 -13.8; 2234 -12.1; 2457 -10.1; 2703 -8.8; 2973 -7.4; 3270 -6.2; 3597 -3.8; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.7; 5793 -2.9; 6373 -1.1; 7010 -4.0; 7711 -8.0; 8482 -15.4; 9330 -16.8; 10263 -9.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-ZX700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-ZX700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 31 Hz   | 1.6  | 7.4 dB   |
| Peaking | 1958 Hz | 1.98 | -8.3 dB  |
| Peaking | 4360 Hz | 2.28 | 7.1 dB   |
| Peaking | 6532 Hz | 3.1  | 5.2 dB   |
| Peaking | 8936 Hz | 3.94 | -13.0 dB |
| Peaking | 21 Hz   | 3.34 | 3.0 dB   |
| Peaking | 47 Hz   | 3.57 | 3.5 dB   |
| Peaking | 123 Hz  | 0.98 | -3.6 dB  |
| Peaking | 228 Hz  | 2.37 | -1.7 dB  |
| Peaking | 346 Hz  | 2.74 | -2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -9.9 dB |
| Peaking | 4000 Hz  | 1.41 | 9.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-ZX700/Sony%20MDR-ZX700.png)