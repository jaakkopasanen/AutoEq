# Sony MDR-ZX770BN
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.8; 23 -6.5; 25 -7.1; 28 -7.9; 31 -8.5; 34 -8.9; 37 -9.1; 41 -9.2; 45 -9.2; 49 -9.2; 54 -9.1; 60 -9.0; 66 -8.9; 72 -8.6; 79 -8.4; 87 -8.1; 96 -7.9; 106 -7.9; 116 -8.0; 128 -8.0; 141 -7.8; 155 -7.3; 170 -7.7; 187 -8.4; 206 -8.2; 227 -7.9; 249 -7.7; 274 -7.4; 302 -6.9; 332 -6.2; 365 -5.2; 402 -4.2; 442 -3.2; 486 -2.3; 535 -1.6; 588 -1.6; 647 -1.7; 712 -1.9; 783 -2.0; 861 -1.8; 947 -1.8; 1042 -2.0; 1146 -2.5; 1261 -2.4; 1387 -2.3; 1526 -3.0; 1678 -4.9; 1846 -7.9; 2031 -9.9; 2234 -9.3; 2457 -7.5; 2703 -6.2; 2973 -5.9; 3270 -3.7; 3597 -0.5; 3957 -6.5; 4353 -10.7; 4788 -12.2; 5267 -10.0; 5793 -4.7; 6373 -2.2; 7010 -4.2; 7711 -8.6; 8482 -10.9; 9330 -10.1; 10263 -10.3; 11289 -10.7; 12418 -7.9; 13660 -6.0; 15026 -9.1; 16529 -13.4; 18182 -13.2; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-ZX770BN GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-ZX770BN ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 578 Hz   | 2.65 | 3.7 dB  |
| Peaking | 1170 Hz  | 1.13 | 4.1 dB  |
| Peaking | 2063 Hz  | 3.73 | -6.1 dB |
| Peaking | 9765 Hz  | 2.02 | -4.8 dB |
| Peaking | 17564 Hz | 1.39 | -9.1 dB |
| Peaking | 52 Hz    | 0.62 | -3.5 dB |
| Peaking | 211 Hz   | 1.8  | -2.3 dB |
| Peaking | 3600 Hz  | 5.24 | 8.7 dB  |
| Peaking | 4734 Hz  | 2.03 | -8.3 dB |
| Peaking | 6222 Hz  | 4.05 | 8.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.4 dB |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 3.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.5 dB |
| Peaking | 16000 Hz | 1.41 | -7.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-ZX770BN/Sony%20MDR-ZX770BN.png)