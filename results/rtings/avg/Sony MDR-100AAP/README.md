# Sony MDR-100AAP
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -5.7; 25 -6.1; 28 -6.7; 31 -7.2; 34 -7.5; 37 -7.8; 41 -8.0; 45 -8.1; 49 -8.1; 54 -8.2; 60 -8.2; 66 -8.3; 72 -8.3; 79 -8.4; 87 -8.8; 96 -9.3; 106 -9.6; 116 -9.7; 128 -9.8; 141 -9.5; 155 -9.3; 170 -9.2; 187 -8.7; 206 -7.9; 227 -6.7; 249 -6.5; 274 -7.7; 302 -6.6; 332 -5.4; 365 -4.5; 402 -4.0; 442 -3.9; 486 -3.8; 535 -3.9; 588 -3.9; 647 -3.8; 712 -3.7; 783 -3.5; 861 -3.4; 947 -3.3; 1042 -3.2; 1146 -3.2; 1261 -3.2; 1387 -3.3; 1526 -3.4; 1678 -3.5; 1846 -3.3; 2031 -3.2; 2234 -2.4; 2457 -1.5; 2703 -0.8; 2973 -0.5; 3270 -1.5; 3597 -2.3; 3957 -2.8; 4353 -2.8; 4788 -1.4; 5267 -5.7; 5793 -3.7; 6373 -2.9; 7010 -1.8; 7711 -3.0; 8482 -5.0; 9330 -3.8; 10263 -3.3; 11289 -3.3; 12418 -3.3; 13660 -3.3; 15026 -3.3; 16529 -3.3; 18182 -4.1; 20000 -3.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-100AAP GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-100AAP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 46 Hz    | 0.56 | -4.1 dB |
| Peaking | 140 Hz   | 0.92 | -5.4 dB |
| Peaking | 282 Hz   | 5.05 | -2.0 dB |
| Peaking | 2868 Hz  | 3.13 | 3.0 dB  |
| Peaking | 4721 Hz  | 9.92 | 2.9 dB  |
| Peaking | 5271 Hz  | 6.69 | -3.2 dB |
| Peaking | 7096 Hz  | 3.71 | 1.4 dB  |
| Peaking | 8642 Hz  | 6.93 | -2.5 dB |
| Peaking | 18976 Hz | 2.65 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB |
| Peaking | 62 Hz    | 1.41 | -3.6 dB |
| Peaking | 125 Hz   | 1.41 | -5.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-100AAP/Sony%20MDR-100AAP.png)