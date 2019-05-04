# Sony MDR-NC8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -1.1; 49 -2.1; 54 -3.2; 60 -4.2; 66 -5.2; 72 -6.1; 79 -7.0; 87 -7.8; 96 -8.5; 106 -9.3; 116 -9.8; 128 -9.6; 141 -8.8; 155 -7.6; 170 -6.6; 187 -7.1; 206 -7.8; 227 -7.8; 249 -7.4; 274 -6.9; 302 -6.1; 332 -5.5; 365 -5.1; 402 -4.6; 442 -4.3; 486 -5.0; 535 -5.8; 588 -6.4; 647 -6.2; 712 -7.4; 783 -8.6; 861 -8.0; 947 -9.8; 1042 -10.6; 1146 -9.1; 1261 -7.5; 1387 -6.7; 1526 -6.6; 1678 -6.1; 1846 -6.1; 2031 -5.8; 2234 -5.4; 2457 -6.2; 2703 -6.4; 2973 -6.4; 3270 -6.0; 3597 -4.9; 3957 -4.0; 4353 -1.8; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.4; 7711 -12.4; 8482 -14.7; 9330 -11.3; 10263 -9.6; 11289 -11.4; 12418 -11.3; 13660 -8.9; 15026 -9.2; 16529 -9.0; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-NC8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-NC8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 1.35 | 7.3 dB   |
| Peaking | 1018 Hz  | 3.73 | -4.4 dB  |
| Peaking | 5901 Hz  | 1.43 | 8.9 dB   |
| Peaking | 8172 Hz  | 3.75 | -10.7 dB |
| Peaking | 11982 Hz | 0.94 | -4.7 dB  |
| Peaking | 47 Hz    | 2.92 | 2.2 dB   |
| Peaking | 114 Hz   | 1.94 | -3.8 dB  |
| Peaking | 228 Hz   | 4.61 | -1.3 dB  |
| Peaking | 418 Hz   | 2.69 | 2.4 dB   |
| Peaking | 3050 Hz  | 5.25 | -1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.7 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -0.0 dB |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.5 dB |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.0 dB |
| Peaking | 16000 Hz | 1.41 | -3.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-NC8/Sony%20MDR-NC8.png)