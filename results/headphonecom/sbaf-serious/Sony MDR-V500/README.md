# Sony MDR-V500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.6; 106 -1.4; 116 -2.3; 128 -3.2; 141 -3.8; 155 -3.4; 170 -3.9; 187 -4.2; 206 -4.3; 227 -3.3; 249 -3.6; 274 -4.0; 302 -5.0; 332 -5.0; 365 -5.1; 402 -5.1; 442 -5.3; 486 -5.6; 535 -5.9; 588 -5.9; 647 -5.7; 712 -6.4; 783 -6.3; 861 -6.0; 947 -6.9; 1042 -7.3; 1146 -6.9; 1261 -8.0; 1387 -9.3; 1526 -9.7; 1678 -9.8; 1846 -9.9; 2031 -10.0; 2234 -10.1; 2457 -10.1; 2703 -10.1; 2973 -11.3; 3270 -11.4; 3597 -10.8; 3957 -10.4; 4353 -9.7; 4788 -8.3; 5267 -6.4; 5793 -6.1; 6373 -8.2; 7010 -6.2; 7711 -6.2; 8482 -6.5; 9330 -6.7; 10263 -9.2; 11289 -6.8; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-V500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-V500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 38 Hz    | 0.3  | 6.0 dB  |
| Peaking | 461 Hz   | 0.09 | 0.9 dB  |
| Peaking | 1741 Hz  | 1.21 | -3.7 dB |
| Peaking | 3378 Hz  | 1.74 | -4.7 dB |
| Peaking | 20693 Hz | 1.87 | -0.1 dB |
| Peaking | 42 Hz    | 2.86 | -0.4 dB |
| Peaking | 535 Hz   | 3.18 | -0.2 dB |
| Peaking | 9264 Hz  | 1.33 | 0.9 dB  |
| Peaking | 10363 Hz | 5.23 | -3.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 5.4 dB  |
| Peaking | 125 Hz   | 1.41 | 2.6 dB  |
| Peaking | 250 Hz   | 1.41 | 1.7 dB  |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | -3.1 dB |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-V500/Sony%20MDR-V500.png)