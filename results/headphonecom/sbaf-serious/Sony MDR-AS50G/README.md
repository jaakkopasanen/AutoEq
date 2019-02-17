# Sony MDR-AS50G
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.5; 23 -7.9; 25 -8.3; 28 -8.8; 31 -9.2; 34 -9.5; 37 -9.8; 41 -10.1; 45 -10.4; 49 -10.7; 54 -11.0; 60 -11.3; 66 -11.6; 72 -11.9; 79 -12.2; 87 -12.5; 96 -12.6; 106 -12.8; 116 -12.8; 128 -12.9; 141 -12.9; 155 -12.8; 170 -12.6; 187 -12.4; 206 -12.1; 227 -11.7; 249 -11.4; 274 -11.1; 302 -10.6; 332 -10.1; 365 -9.5; 402 -9.1; 442 -8.7; 486 -8.3; 535 -7.8; 588 -7.3; 647 -6.9; 712 -6.7; 783 -6.5; 861 -6.4; 947 -6.3; 1042 -6.7; 1146 -7.0; 1261 -7.5; 1387 -8.3; 1526 -9.7; 1678 -10.5; 1846 -10.8; 2031 -10.6; 2234 -10.0; 2457 -8.6; 2703 -6.2; 2973 -2.3; 3270 -0.5; 3597 -0.5; 3957 -0.6; 4353 -4.8; 4788 -8.8; 5267 -10.0; 5793 -8.0; 6373 -6.9; 7010 -8.8; 7711 -12.8; 8482 -12.2; 9330 -7.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -9.8; 15026 -10.6; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-AS50G GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-AS50G ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 88 Hz    | 0.47 | -5.4 dB |
| Peaking | 216 Hz   | 0.91 | -2.9 dB |
| Peaking | 1977 Hz  | 1.92 | -5.2 dB |
| Peaking | 3400 Hz  | 3.14 | 8.2 dB  |
| Peaking | 7954 Hz  | 3.82 | -7.2 dB |
| Peaking | 867 Hz   | 2.49 | 1.1 dB  |
| Peaking | 4037 Hz  | 9.12 | 3.3 dB  |
| Peaking | 5068 Hz  | 5.04 | -4.5 dB |
| Peaking | 13180 Hz | 0.76 | 1.8 dB  |
| Peaking | 14356 Hz | 3.17 | -7.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.9 dB |
| Peaking | 62 Hz    | 1.41 | -4.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.8 dB |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.3 dB |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-AS50G/Sony%20MDR-AS50G.png)