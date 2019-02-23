# Sony MDR-AS50G
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.4; 23 -5.9; 25 -6.2; 28 -6.7; 31 -7.1; 34 -7.5; 37 -7.8; 41 -8.1; 45 -8.4; 49 -8.7; 54 -9.0; 60 -9.3; 66 -9.6; 72 -9.8; 79 -10.1; 87 -10.5; 96 -10.6; 106 -10.7; 116 -10.8; 128 -10.8; 141 -10.9; 155 -10.7; 170 -10.6; 187 -10.4; 206 -10.1; 227 -9.7; 249 -9.4; 274 -9.1; 302 -8.5; 332 -8.0; 365 -7.4; 402 -7.1; 442 -6.7; 486 -6.2; 535 -5.8; 588 -5.2; 647 -4.8; 712 -4.7; 783 -4.5; 861 -4.4; 947 -4.3; 1042 -4.6; 1146 -5.0; 1261 -5.4; 1387 -6.3; 1526 -7.7; 1678 -8.5; 1846 -8.7; 2031 -8.6; 2234 -7.9; 2457 -6.6; 2703 -4.1; 2973 -0.8; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.7; 4788 -6.7; 5267 -8.0; 5793 -5.9; 6373 -4.8; 7010 -6.8; 7711 -10.8; 8482 -10.2; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.9; 15026 -8.6; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-AS50G GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-AS50G ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 93 Hz    | 0.83 | -3.8 dB |
| Peaking | 191 Hz   | 1.5  | -2.7 dB |
| Peaking | 2044 Hz  | 3.02 | -3.8 dB |
| Peaking | 3396 Hz  | 2.16 | 7.2 dB  |
| Peaking | 8126 Hz  | 5.9  | -5.7 dB |
| Peaking | 21 Hz    | 2.27 | 1.3 dB  |
| Peaking | 872 Hz   | 1.31 | 2.5 dB  |
| Peaking | 1618 Hz  | 5.03 | -1.9 dB |
| Peaking | 5089 Hz  | 8.91 | -3.3 dB |
| Peaking | 14660 Hz | 6    | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.2 dB  |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-AS50G/Sony%20MDR-AS50G.png)