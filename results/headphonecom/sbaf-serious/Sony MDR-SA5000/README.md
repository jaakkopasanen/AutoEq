# Sony MDR-SA5000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.9; 87 -1.9; 96 -2.3; 106 -2.5; 116 -2.5; 128 -2.4; 141 -2.3; 155 -2.3; 170 -1.9; 187 -1.8; 206 -1.6; 227 -1.6; 249 -1.3; 274 -1.2; 302 -0.9; 332 -1.3; 365 -2.0; 402 -1.8; 442 -2.0; 486 -2.5; 535 -3.1; 588 -3.9; 647 -4.4; 712 -5.0; 783 -5.6; 861 -6.3; 947 -6.8; 1042 -6.0; 1146 -4.0; 1261 -2.5; 1387 -2.1; 1526 -2.4; 1678 -3.0; 1846 -4.2; 2031 -5.5; 2234 -6.3; 2457 -9.5; 2703 -13.1; 2973 -12.0; 3270 -9.3; 3597 -5.8; 3957 -5.3; 4353 -7.8; 4788 -5.9; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -5.6; 7711 -9.6; 8482 -10.7; 9330 -11.1; 10263 -7.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -9.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-SA5000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-SA5000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 23 Hz   |  0.07 | 5.3 dB  |
| Peaking | 1119 Hz |  0.22 | 2.0 dB  |
| Peaking | 2806 Hz |  3.98 | -9.2 dB |
| Peaking | 5914 Hz |  3.45 | 7.3 dB  |
| Peaking | 8528 Hz |  2.49 | -6.1 dB |
| Peaking | 124 Hz  |  2.06 | -1.5 dB |
| Peaking | 353 Hz  |  1.06 | 1.3 dB  |
| Peaking | 968 Hz  |  1.55 | -4.5 dB |
| Peaking | 1336 Hz |  1.97 | 4.6 dB  |
| Peaking | 4457 Hz | 10.59 | -3.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.7 dB  |
| Peaking | 125 Hz   | 1.41 | 2.2 dB  |
| Peaking | 250 Hz   | 1.41 | 4.8 dB  |
| Peaking | 500 Hz   | 1.41 | 2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-SA5000/Sony%20MDR-SA5000.png)