# Sony MDR-XB300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.3; 23 -3.5; 25 -4.7; 28 -6.3; 31 -7.6; 34 -8.7; 37 -9.7; 41 -10.8; 45 -11.6; 49 -12.4; 54 -13.0; 60 -13.4; 66 -13.4; 72 -13.3; 79 -13.7; 87 -14.3; 96 -14.7; 106 -14.8; 116 -14.6; 128 -14.5; 141 -14.2; 155 -13.7; 170 -13.3; 187 -13.1; 206 -12.6; 227 -11.8; 249 -10.8; 274 -10.3; 302 -9.4; 332 -8.5; 365 -7.4; 402 -6.5; 442 -5.4; 486 -4.7; 535 -4.0; 588 -3.0; 647 -2.6; 712 -2.2; 783 -2.4; 861 -3.8; 947 -5.7; 1042 -7.0; 1146 -7.7; 1261 -8.5; 1387 -9.8; 1526 -10.4; 1678 -10.7; 1846 -11.5; 2031 -12.2; 2234 -12.6; 2457 -11.9; 2703 -10.2; 2973 -7.8; 3270 -5.6; 3597 -3.6; 3957 -2.0; 4353 -1.2; 4788 -0.5; 5267 -0.5; 5793 -0.8; 6373 -5.8; 7010 -4.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-XB300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 2.07 | 5.7 dB  |
| Peaking | 71 Hz   | 0.7  | -7.1 dB |
| Peaking | 162 Hz  | 1.32 | -5.0 dB |
| Peaking | 2175 Hz | 1.9  | -7.5 dB |
| Peaking | 4657 Hz | 1.74 | 7.2 dB  |
| Peaking | 21 Hz   | 1.88 | 1.0 dB  |
| Peaking | 109 Hz  | 5.99 | -1.0 dB |
| Peaking | 275 Hz  | 2.29 | -1.9 dB |
| Peaking | 694 Hz  | 1.27 | 5.4 dB  |
| Peaking | 1290 Hz | 1.77 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.7 dB  |
| Peaking | 62 Hz    | 1.41 | -6.6 dB |
| Peaking | 125 Hz   | 1.41 | -7.0 dB |
| Peaking | 250 Hz   | 1.41 | -4.4 dB |
| Peaking | 500 Hz   | 1.41 | 4.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -8.9 dB |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-XB300/Sony%20MDR-XB300.png)