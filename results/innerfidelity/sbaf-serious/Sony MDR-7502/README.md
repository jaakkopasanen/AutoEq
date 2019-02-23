# Sony MDR-7502
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.8; 72 -1.1; 79 -1.6; 87 -2.2; 96 -2.7; 106 -2.8; 116 -2.4; 128 -2.7; 141 -3.9; 155 -4.8; 170 -4.6; 187 -5.4; 206 -5.6; 227 -6.0; 249 -6.2; 274 -6.3; 302 -6.2; 332 -6.0; 365 -6.6; 402 -6.7; 442 -7.0; 486 -7.8; 535 -8.0; 588 -7.6; 647 -7.7; 712 -7.9; 783 -8.0; 861 -8.5; 947 -9.0; 1042 -9.3; 1146 -9.9; 1261 -10.5; 1387 -10.7; 1526 -11.5; 1678 -12.5; 1846 -12.7; 2031 -12.3; 2234 -11.9; 2457 -10.3; 2703 -8.9; 2973 -7.5; 3270 -6.7; 3597 -5.9; 3957 -4.7; 4353 -3.9; 4788 -2.2; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.0; 9330 -11.5; 10263 -7.3; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7502 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7502 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.4  | 5.6 dB  |
| Peaking | 78 Hz   | 0.75 | 2.8 dB  |
| Peaking | 1804 Hz | 0.92 | -6.4 dB |
| Peaking | 5499 Hz | 1.39 | 7.2 dB  |
| Peaking | 9149 Hz | 4.13 | -6.6 dB |
| Peaking | 122 Hz  | 1.56 | -1.4 dB |
| Peaking | 122 Hz  | 3.48 | 2.5 dB  |
| Peaking | 518 Hz  | 4.5  | -1.0 dB |
| Peaking | 1415 Hz | 8.23 | 0.7 dB  |
| Peaking | 3077 Hz | 7.49 | 0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 4.6 dB  |
| Peaking | 125 Hz   | 1.41 | 2.5 dB  |
| Peaking | 250 Hz   | 1.41 | -0.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB |
| Peaking | 2000 Hz  | 1.41 | -7.4 dB |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-7502/Sony%20MDR-7502.png)