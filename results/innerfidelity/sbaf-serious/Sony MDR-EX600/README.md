# Sony MDR-EX600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.6; 23 -1.0; 25 -1.3; 28 -1.7; 31 -2.0; 34 -2.2; 37 -2.5; 41 -2.8; 45 -3.1; 49 -3.3; 54 -3.7; 60 -4.0; 66 -4.5; 72 -4.8; 79 -5.2; 87 -5.7; 96 -6.3; 106 -6.6; 116 -6.8; 128 -7.2; 141 -7.5; 155 -7.7; 170 -7.9; 187 -8.1; 206 -8.2; 227 -8.3; 249 -8.3; 274 -8.2; 302 -8.1; 332 -8.0; 365 -7.8; 402 -7.8; 442 -7.5; 486 -7.4; 535 -7.2; 588 -6.6; 647 -6.4; 712 -6.4; 783 -6.2; 861 -6.5; 947 -6.8; 1042 -7.3; 1146 -7.8; 1261 -8.3; 1387 -9.1; 1526 -9.9; 1678 -10.3; 1846 -10.0; 2031 -9.0; 2234 -7.5; 2457 -5.0; 2703 -2.9; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -3.0; 4788 -7.0; 5267 -11.3; 5793 -7.7; 6373 -3.2; 7010 -4.0; 7711 -6.2; 8482 -7.0; 9330 -7.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-EX600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-EX600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.84 | 5.7 dB  |
| Peaking | 1803 Hz | 1.48 | -5.7 dB |
| Peaking | 3390 Hz | 1.36 | 8.3 dB  |
| Peaking | 5330 Hz | 4.56 | -8.2 dB |
| Peaking | 6536 Hz | 6.58 | 4.3 dB  |
| Peaking | 28 Hz   | 0.3  | 2.6 dB  |
| Peaking | 29 Hz   | 1.32 | -3.3 dB |
| Peaking | 204 Hz  | 0.49 | -2.2 dB |
| Peaking | 752 Hz  | 1.77 | 1.2 dB  |
| Peaking | 8926 Hz | 5.76 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB  |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-EX600/Sony%20MDR-EX600.png)