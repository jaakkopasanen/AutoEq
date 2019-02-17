# Sony MDR-1000X Wireless NC Active
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.9; 23 -8.6; 25 -8.3; 28 -8.0; 31 -7.6; 34 -7.4; 37 -7.2; 41 -7.1; 45 -7.0; 49 -7.0; 54 -7.1; 60 -7.2; 66 -7.5; 72 -7.7; 79 -8.0; 87 -8.4; 96 -8.9; 106 -9.1; 116 -9.3; 128 -9.5; 141 -9.6; 155 -9.5; 170 -9.1; 187 -8.9; 206 -8.4; 227 -7.6; 249 -7.3; 274 -7.6; 302 -7.3; 332 -6.4; 365 -5.3; 402 -5.0; 442 -5.6; 486 -6.0; 535 -5.9; 588 -4.0; 647 -4.6; 712 -6.7; 783 -3.9; 861 -3.5; 947 -3.7; 1042 -3.1; 1146 -0.5; 1261 -1.8; 1387 -2.6; 1526 -5.2; 1678 -7.2; 1846 -8.7; 2031 -8.7; 2234 -8.0; 2457 -5.5; 2703 -3.3; 2973 -5.0; 3270 -5.7; 3597 -5.8; 3957 -8.9; 4353 -10.5; 4788 -7.6; 5267 -8.1; 5793 -10.7; 6373 -8.8; 7010 -4.3; 7711 -6.1; 8482 -8.6; 9330 -8.5; 10263 -6.0; 11289 -4.2; 12418 -3.4; 13660 -3.3; 15026 -3.3; 16529 -3.3; 18182 -3.3; 20000 -3.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-1000X Wireless NC Active GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-1000X Wireless NC Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.68 | -5.3 dB |
| Peaking | 142 Hz   | 0.53 | -6.0 dB |
| Peaking | 1935 Hz  | 4.58 | -5.5 dB |
| Peaking | 5574 Hz  | 0.92 | -5.8 dB |
| Peaking | 22050 Hz | 2.33 | -4.2 dB |
| Peaking | 1070 Hz  | 0.87 | -1.2 dB |
| Peaking | 1184 Hz  | 3.41 | 4.6 dB  |
| Peaking | 6100 Hz  | 6.74 | -3.9 dB |
| Peaking | 6941 Hz  | 3.69 | 4.8 dB  |
| Peaking | 8922 Hz  | 4.14 | -4.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | -5.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | -3.6 dB |
| Peaking | 8000 Hz  | 1.41 | -4.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-1000X%20Wireless%20NC%20Active/Sony%20MDR-1000X%20Wireless%20NC%20Active.png)