# Sony MDR-XB300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.7; 23 -2.9; 25 -4.1; 28 -5.6; 31 -7.0; 34 -8.1; 37 -9.1; 41 -10.1; 45 -11.0; 49 -11.7; 54 -12.4; 60 -12.8; 66 -12.8; 72 -12.7; 79 -13.1; 87 -13.6; 96 -14.1; 106 -14.1; 116 -14.0; 128 -13.9; 141 -13.5; 155 -13.1; 170 -12.6; 187 -12.4; 206 -12.0; 227 -11.2; 249 -10.1; 274 -9.7; 302 -8.8; 332 -7.9; 365 -6.8; 402 -5.9; 442 -4.8; 486 -4.1; 535 -3.4; 588 -2.4; 647 -1.9; 712 -1.6; 783 -1.8; 861 -3.2; 947 -5.0; 1042 -6.4; 1146 -7.0; 1261 -7.9; 1387 -9.2; 1526 -9.8; 1678 -10.0; 1846 -10.9; 2031 -11.6; 2234 -12.0; 2457 -11.2; 2703 -9.6; 2973 -7.2; 3270 -5.0; 3597 -2.9; 3957 -1.3; 4353 -0.8; 4788 -0.5; 5267 -0.5; 5793 -0.6; 6373 -5.2; 7010 -4.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-XB300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 2.01 | 6.1 dB  |
| Peaking | 71 Hz   | 0.77 | -6.5 dB |
| Peaking | 155 Hz  | 1.39 | -4.9 dB |
| Peaking | 2204 Hz | 2.08 | -7.1 dB |
| Peaking | 4583 Hz | 1.58 | 7.2 dB  |
| Peaking | 11 Hz   | 0.83 | -1.2 dB |
| Peaking | 262 Hz  | 1.98 | -1.9 dB |
| Peaking | 686 Hz  | 1.23 | 5.8 dB  |
| Peaking | 1340 Hz | 1.83 | -2.7 dB |
| Peaking | 8485 Hz | 3.13 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | -6.1 dB |
| Peaking | 125 Hz   | 1.41 | -6.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | 4.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -8.3 dB |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-XB300/Sony%20MDR-XB300.png)