# Sony MDR-7520
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.3; 23 -3.8; 25 -4.4; 28 -5.1; 31 -5.7; 34 -6.2; 37 -6.6; 41 -7.0; 45 -7.3; 49 -7.6; 54 -8.0; 60 -8.4; 66 -9.0; 72 -9.4; 79 -9.9; 87 -10.3; 96 -10.7; 106 -11.0; 116 -11.2; 128 -11.1; 141 -10.8; 155 -10.2; 170 -9.6; 187 -8.8; 206 -7.7; 227 -6.2; 249 -4.8; 274 -5.7; 302 -3.3; 332 -2.5; 365 -3.1; 402 -4.1; 442 -5.0; 486 -5.5; 535 -5.5; 588 -5.4; 647 -5.0; 712 -4.7; 783 -4.5; 861 -4.1; 947 -3.7; 1042 -3.8; 1146 -4.1; 1261 -4.7; 1387 -5.4; 1526 -6.3; 1678 -7.4; 1846 -8.8; 2031 -9.5; 2234 -9.2; 2457 -9.2; 2703 -10.6; 2973 -11.3; 3270 -9.5; 3597 -6.3; 3957 -1.7; 4353 -0.5; 4788 -0.5; 5267 -3.0; 5793 -5.1; 6373 -2.1; 7010 -4.0; 7711 -8.1; 8482 -14.5; 9330 -17.0; 10263 -13.7; 11289 -7.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -9.6; 18182 -8.8; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7520 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7520 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 107 Hz   | 0.65 | -9.0 dB  |
| Peaking | 172 Hz   | 0.12 | 4.1 dB   |
| Peaking | 3122 Hz  | 1.04 | -15.4 dB |
| Peaking | 4163 Hz  | 1    | 15.7 dB  |
| Peaking | 9238 Hz  | 3.21 | -13.5 dB |
| Peaking | 21 Hz    | 3.09 | 1.9 dB   |
| Peaking | 331 Hz   | 4.22 | 2.8 dB   |
| Peaking | 521 Hz   | 2.8  | -1.9 dB  |
| Peaking | 12146 Hz | 4.19 | 1.5 dB   |
| Peaking | 17140 Hz | 2.27 | -3.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.7 dB |
| Peaking | 250 Hz   | 1.41 | 2.4 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.5 dB |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.4 dB |
| Peaking | 16000 Hz | 1.41 | -1.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-7520/Sony%20MDR-7520.png)