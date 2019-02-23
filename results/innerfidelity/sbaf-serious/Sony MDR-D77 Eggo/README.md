# Sony MDR-D77 Eggo
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -1.2; 37 -2.1; 41 -3.2; 45 -4.2; 49 -4.9; 54 -5.6; 60 -6.3; 66 -6.8; 72 -7.2; 79 -7.5; 87 -7.8; 96 -8.1; 106 -8.2; 116 -8.0; 128 -7.8; 141 -8.0; 155 -8.2; 170 -7.9; 187 -7.9; 206 -7.8; 227 -7.2; 249 -6.9; 274 -6.6; 302 -5.9; 332 -5.9; 365 -6.7; 402 -6.1; 442 -6.0; 486 -6.6; 535 -7.3; 588 -7.8; 647 -8.4; 712 -8.8; 783 -8.9; 861 -9.2; 947 -9.3; 1042 -9.6; 1146 -9.8; 1261 -8.4; 1387 -7.0; 1526 -9.2; 1678 -10.8; 1846 -11.2; 2031 -10.5; 2234 -9.5; 2457 -7.5; 2703 -6.2; 2973 -4.5; 3270 -3.6; 3597 -4.7; 3957 -5.1; 4353 -4.0; 4788 -0.8; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.5; 9330 -9.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-D77 Eggo GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-D77 Eggo ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 1.64 | 7.1 dB  |
| Peaking | 905 Hz  | 1.51 | -2.9 dB |
| Peaking | 1902 Hz | 2.65 | -4.8 dB |
| Peaking | 3160 Hz | 4.17 | 2.9 dB  |
| Peaking | 5471 Hz | 2.68 | 7.0 dB  |
| Peaking | 132 Hz  | 0.76 | -2.0 dB |
| Peaking | 338 Hz  | 1.58 | 1.2 dB  |
| Peaking | 3894 Hz | 6.82 | -0.3 dB |
| Peaking | 6523 Hz | 8.44 | 2.2 dB  |
| Peaking | 8970 Hz | 5.09 | -4.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.4 dB |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-D77%20Eggo/Sony%20MDR-D77%20Eggo.png)