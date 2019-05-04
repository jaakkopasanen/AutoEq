# Sony MDR-XB50AP
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.8; 23 -5.2; 25 -5.5; 28 -5.9; 31 -6.2; 34 -6.4; 37 -6.6; 41 -6.9; 45 -7.0; 49 -7.2; 54 -7.5; 60 -8.0; 66 -8.4; 72 -8.7; 79 -9.2; 87 -9.7; 96 -10.3; 106 -11.0; 116 -11.6; 128 -12.1; 141 -12.5; 155 -12.7; 170 -12.7; 187 -12.8; 206 -12.8; 227 -12.4; 249 -11.7; 274 -10.8; 302 -9.7; 332 -8.6; 365 -7.3; 402 -5.9; 442 -4.6; 486 -3.4; 535 -2.5; 588 -2.1; 647 -2.2; 712 -2.8; 783 -3.8; 861 -4.9; 947 -6.2; 1042 -7.5; 1146 -8.3; 1261 -8.7; 1387 -8.5; 1526 -7.7; 1678 -6.7; 1846 -6.1; 2031 -5.7; 2234 -4.4; 2457 -2.3; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -1.4; 3957 -2.2; 4353 -3.7; 4788 -6.5; 5267 -8.5; 5793 -5.9; 6373 -4.3; 7010 -4.4; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
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

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 192 Hz   | 0.64 | -7.4 dB |
| Peaking | 585 Hz   | 1.01 | 7.0 dB  |
| Peaking | 1235 Hz  | 1.41 | -4.1 dB |
| Peaking | 3028 Hz  | 1.83 | 6.9 dB  |
| Peaking | 22028 Hz | 2.19 | 0.1 dB  |
| Peaking | 14 Hz    | 0.82 | 2.6 dB  |
| Peaking | 115 Hz   | 3.32 | -0.5 dB |
| Peaking | 4162 Hz  | 4.6  | 1.8 dB  |
| Peaking | 5205 Hz  | 4.32 | -4.1 dB |
| Peaking | 6363 Hz  | 4.29 | 2.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -6.3 dB |
| Peaking | 500 Hz   | 1.41 | 6.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.8 dB |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-XB50AP/Sony%20MDR-XB50AP.png)