# Sony MDR-Z1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.7; 60 -1.7; 66 -2.8; 72 -3.6; 79 -4.4; 87 -5.1; 96 -5.4; 106 -5.9; 116 -6.6; 128 -7.5; 141 -8.1; 155 -8.1; 170 -7.5; 187 -7.4; 206 -7.1; 227 -6.7; 249 -6.2; 274 -5.2; 302 -6.2; 332 -7.1; 365 -7.7; 402 -8.1; 442 -8.3; 486 -8.5; 535 -8.3; 588 -8.1; 647 -7.8; 712 -7.6; 783 -7.9; 861 -7.8; 947 -8.0; 1042 -7.8; 1146 -8.0; 1261 -8.6; 1387 -9.6; 1526 -10.9; 1678 -11.9; 1846 -12.1; 2031 -11.7; 2234 -9.8; 2457 -8.4; 2703 -7.0; 2973 -5.4; 3270 -3.9; 3597 -0.8; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.5; 5793 -0.7; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -10.8; 9330 -15.0; 10263 -10.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-Z1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-Z1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 34 Hz   | 0.87 | 7.1 dB   |
| Peaking | 2073 Hz | 0.88 | -8.5 dB  |
| Peaking | 3935 Hz | 0.85 | 9.3 dB   |
| Peaking | 6247 Hz | 4.55 | 2.7 dB   |
| Peaking | 9285 Hz | 3.91 | -10.9 dB |
| Peaking | 57 Hz   | 3.46 | 1.8 dB   |
| Peaking | 146 Hz  | 2.17 | -2.2 dB  |
| Peaking | 278 Hz  | 5.87 | 2.0 dB   |
| Peaking | 450 Hz  | 1.7  | -1.6 dB  |
| Peaking | 1142 Hz | 3.82 | 1.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 3.8 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | 0.7 dB  |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -7.3 dB |
| Peaking | 4000 Hz  | 1.41 | 9.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-Z1000/Sony%20MDR-Z1000.png)