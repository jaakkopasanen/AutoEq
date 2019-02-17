# Sony MDR-Z7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.6; 23 -3.9; 25 -5.0; 28 -6.3; 31 -7.2; 34 -7.9; 37 -8.2; 41 -8.5; 45 -8.6; 49 -8.5; 54 -8.4; 60 -8.4; 66 -8.3; 72 -8.1; 79 -7.9; 87 -7.7; 96 -8.1; 106 -8.8; 116 -9.0; 128 -8.5; 141 -9.4; 155 -10.5; 170 -9.5; 187 -9.6; 206 -9.2; 227 -8.8; 249 -8.3; 274 -7.7; 302 -6.9; 332 -6.3; 365 -5.7; 402 -5.2; 442 -4.6; 486 -4.6; 535 -4.5; 588 -4.2; 647 -4.5; 712 -5.1; 783 -5.6; 861 -6.0; 947 -5.5; 1042 -4.3; 1146 -1.9; 1261 -0.5; 1387 -0.5; 1526 -1.9; 1678 -4.0; 1846 -6.1; 2031 -7.8; 2234 -9.0; 2457 -9.5; 2703 -8.3; 2973 -6.8; 3270 -4.2; 3597 -2.0; 3957 -2.7; 4353 -4.7; 4788 -4.6; 5267 -2.0; 5793 -1.8; 6373 -3.7; 7010 -3.7; 7711 -4.6; 8482 -5.6; 9330 -6.7; 10263 -4.9; 11289 -4.9; 12418 -4.9; 13660 -4.9; 15026 -4.9; 16529 -4.9; 18182 -4.9; 20000 -4.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-Z7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-Z7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.56 | 5.6 dB  |
| Peaking | 38 Hz   | 0.52 | -4.1 dB |
| Peaking | 173 Hz  | 1.15 | -4.5 dB |
| Peaking | 1341 Hz | 3.46 | 5.4 dB  |
| Peaking | 2333 Hz | 3.65 | -5.5 dB |
| Peaking | 490 Hz  | 2.2  | 1.5 dB  |
| Peaking | 1165 Hz | 0.22 | -0.5 dB |
| Peaking | 3667 Hz | 6.4  | 4.0 dB  |
| Peaking | 5653 Hz | 4.47 | 3.8 dB  |
| Peaking | 9109 Hz | 6.72 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.8 dB |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-Z7/Sony%20MDR-Z7.png)