# Sony MDR-XB50AP
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.0; 23 -5.4; 25 -5.7; 28 -6.1; 31 -6.3; 34 -6.6; 37 -6.8; 41 -7.0; 45 -7.3; 49 -7.4; 54 -7.7; 60 -8.1; 66 -8.6; 72 -9.0; 79 -9.4; 87 -10.0; 96 -10.6; 106 -11.2; 116 -11.8; 128 -12.3; 141 -12.7; 155 -12.9; 170 -12.9; 187 -13.0; 206 -12.9; 227 -12.5; 249 -11.8; 274 -10.9; 302 -9.8; 332 -8.7; 365 -7.3; 402 -6.0; 442 -4.6; 486 -3.3; 535 -2.4; 588 -2.0; 647 -2.1; 712 -2.7; 783 -3.6; 861 -4.8; 947 -6.1; 1042 -7.3; 1146 -8.1; 1261 -8.5; 1387 -8.4; 1526 -7.5; 1678 -6.4; 1846 -5.8; 2031 -5.2; 2234 -3.6; 2457 -1.4; 2703 -0.5; 2973 -0.5; 3270 -0.6; 3597 -1.6; 3957 -2.5; 4353 -4.0; 4788 -6.0; 5267 -8.2; 5793 -5.9; 6373 -5.2; 7010 -4.5; 7711 -6.2; 8482 -6.5; 9330 -7.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-XB50AP GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB50AP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 120 Hz  | 1.04 | -2.8 dB |
| Peaking | 223 Hz  | 0.78 | -6.3 dB |
| Peaking | 592 Hz  | 0.97 | 6.9 dB  |
| Peaking | 1227 Hz | 1.36 | -4.3 dB |
| Peaking | 2933 Hz | 1.73 | 6.9 dB  |
| Peaking | 23 Hz   | 1.68 | 1.7 dB  |
| Peaking | 3972 Hz | 5.27 | 1.2 dB  |
| Peaking | 5281 Hz | 5.8  | -3.6 dB |
| Peaking | 6686 Hz | 2.51 | 1.7 dB  |
| Peaking | 8802 Hz | 2.22 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.8 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -6.4 dB |
| Peaking | 500 Hz   | 1.41 | 6.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.8 dB |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-XB50AP/Sony%20MDR-XB50AP.png)