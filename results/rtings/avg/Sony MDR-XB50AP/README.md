# Sony MDR-XB50AP
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.7; 23 -5.0; 25 -5.3; 28 -5.7; 31 -6.0; 34 -6.2; 37 -6.4; 41 -6.7; 45 -6.9; 49 -7.1; 54 -7.3; 60 -7.8; 66 -8.2; 72 -8.6; 79 -9.1; 87 -9.6; 96 -10.2; 106 -10.9; 116 -11.5; 128 -12.0; 141 -12.4; 155 -12.5; 170 -12.5; 187 -12.6; 206 -12.6; 227 -12.2; 249 -11.4; 274 -10.5; 302 -9.4; 332 -8.3; 365 -7.0; 402 -5.6; 442 -4.2; 486 -3.0; 535 -2.0; 588 -1.7; 647 -1.8; 712 -2.4; 783 -3.3; 861 -4.4; 947 -5.8; 1042 -7.0; 1146 -7.8; 1261 -8.2; 1387 -8.0; 1526 -7.2; 1678 -6.1; 1846 -5.5; 2031 -4.9; 2234 -3.2; 2457 -1.0; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -1.2; 3957 -2.2; 4353 -3.7; 4788 -5.6; 5267 -7.9; 5793 -5.5; 6373 -4.9; 7010 -4.3; 7711 -6.2; 8482 -6.5; 9330 -6.9; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-XB50AP GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB50AP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.48 | 2.4 dB  |
| Peaking | 175 Hz  | 0.64 | -6.7 dB |
| Peaking | 556 Hz  | 1.71 | 6.8 dB  |
| Peaking | 3053 Hz | 1.97 | 6.9 dB  |
| Peaking | 775 Hz  | 3.59 | 1.7 dB  |
| Peaking | 1264 Hz | 2.1  | -2.7 dB |
| Peaking | 2432 Hz | 8.04 | 1.9 dB  |
| Peaking | 5239 Hz | 5.49 | -5.5 dB |
| Peaking | 5480 Hz | 2.1  | 2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -6.1 dB |
| Peaking | 500 Hz   | 1.41 | 6.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-XB50AP/Sony%20MDR-XB50AP.png)