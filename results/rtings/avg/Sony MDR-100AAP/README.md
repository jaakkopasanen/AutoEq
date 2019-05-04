# Sony MDR-100AAP
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.8; 23 -5.3; 25 -5.8; 28 -6.4; 31 -6.9; 34 -7.2; 37 -7.5; 41 -7.7; 45 -7.8; 49 -7.9; 54 -7.9; 60 -8.0; 66 -8.0; 72 -8.0; 79 -8.1; 87 -8.5; 96 -8.9; 106 -9.3; 116 -9.4; 128 -9.4; 141 -9.2; 155 -9.1; 170 -8.9; 187 -8.4; 206 -7.7; 227 -6.5; 249 -6.4; 274 -7.4; 302 -6.4; 332 -5.2; 365 -4.4; 402 -3.9; 442 -3.7; 486 -3.8; 535 -3.9; 588 -3.9; 647 -3.9; 712 -3.7; 783 -3.6; 861 -3.4; 947 -3.4; 1042 -3.3; 1146 -3.2; 1261 -3.2; 1387 -3.4; 1526 -3.6; 1678 -3.7; 1846 -3.6; 2031 -3.5; 2234 -3.1; 2457 -2.3; 2703 -1.3; 2973 -0.5; 3270 -1.2; 3597 -1.9; 3957 -2.5; 4353 -2.1; 4788 -2.1; 5267 -5.8; 5793 -3.3; 6373 -1.9; 7010 -2.1; 7711 -4.1; 8482 -4.6; 9330 -4.4; 10263 -4.4; 11289 -4.4; 12418 -4.4; 13660 -4.4; 15026 -4.4; 16529 -4.4; 18182 -4.4; 20000 -4.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-100AAP GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-100AAP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.5dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 47 Hz   |  0.84 | -3.1 dB |
| Peaking | 113 Hz  |  1.37 | -3.5 dB |
| Peaking | 179 Hz  |  1.61 | -2.7 dB |
| Peaking | 3042 Hz |  1.44 | 3.4 dB  |
| Peaking | 6623 Hz |  7.03 | 2.5 dB  |
| Peaking | 283 Hz  |  6.19 | -2.3 dB |
| Peaking | 1178 Hz |  0.29 | 1.2 dB  |
| Peaking | 2233 Hz |  1.25 | -1.7 dB |
| Peaking | 2842 Hz |  5.67 | 0.8 dB  |
| Peaking | 5328 Hz | 13.29 | -3.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.1 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-100AAP/Sony%20MDR-100AAP.png)