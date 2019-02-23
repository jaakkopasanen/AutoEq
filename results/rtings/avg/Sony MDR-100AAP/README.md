# Sony MDR-100AAP
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -5.7; 25 -6.1; 28 -6.7; 31 -7.2; 34 -7.5; 37 -7.8; 41 -8.0; 45 -8.1; 49 -8.1; 54 -8.2; 60 -8.2; 66 -8.3; 72 -8.3; 79 -8.4; 87 -8.8; 96 -9.3; 106 -9.6; 116 -9.7; 128 -9.8; 141 -9.5; 155 -9.3; 170 -9.2; 187 -8.7; 206 -7.9; 227 -6.7; 249 -6.5; 274 -7.7; 302 -6.6; 332 -5.4; 365 -4.5; 402 -4.0; 442 -3.9; 486 -3.8; 535 -3.9; 588 -3.9; 647 -3.8; 712 -3.7; 783 -3.5; 861 -3.4; 947 -3.3; 1042 -3.2; 1146 -3.2; 1261 -3.2; 1387 -3.3; 1526 -3.4; 1678 -3.5; 1846 -3.3; 2031 -3.2; 2234 -2.4; 2457 -1.5; 2703 -0.8; 2973 -0.5; 3270 -1.5; 3597 -2.3; 3957 -2.8; 4353 -2.8; 4788 -1.4; 5267 -5.7; 5793 -3.7; 6373 -2.9; 7010 -2.4; 7711 -4.2; 8482 -5.1; 9330 -4.5; 10263 -4.5; 11289 -4.5; 12418 -4.5; 13660 -4.5; 15026 -4.5; 16529 -4.5; 18182 -4.5; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-100AAP GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-100AAP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 46 Hz   | 0.75 | -2.9 dB |
| Peaking | 138 Hz  | 0.87 | -5.6 dB |
| Peaking | 282 Hz  | 5.78 | -2.0 dB |
| Peaking | 856 Hz  | 0.13 | 1.2 dB  |
| Peaking | 2904 Hz | 2.6  | 3.0 dB  |
| Peaking | 1759 Hz | 4.86 | -0.4 dB |
| Peaking | 4525 Hz | 3.02 | 1.0 dB  |
| Peaking | 4749 Hz | 8.45 | 4.0 dB  |
| Peaking | 5262 Hz | 2.59 | -4.2 dB |
| Peaking | 6199 Hz | 3.68 | 3.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-100AAP/Sony%20MDR-100AAP.png)