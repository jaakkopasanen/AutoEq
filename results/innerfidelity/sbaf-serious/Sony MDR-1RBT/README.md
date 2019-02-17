# Sony MDR-1RBT
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.0; 23 -6.1; 25 -7.0; 28 -8.1; 31 -9.1; 34 -9.9; 37 -10.6; 41 -11.4; 45 -12.1; 49 -12.7; 54 -13.2; 60 -13.7; 66 -14.3; 72 -14.9; 79 -15.2; 87 -15.9; 96 -15.7; 106 -14.9; 116 -14.1; 128 -14.1; 141 -14.3; 155 -14.3; 170 -10.6; 187 -10.5; 206 -8.3; 227 -5.6; 249 -2.4; 274 -1.5; 302 -0.5; 332 -1.0; 365 -1.5; 402 -3.1; 442 -5.0; 486 -5.7; 535 -4.7; 588 -3.5; 647 -4.4; 712 -5.4; 783 -4.1; 861 -5.3; 947 -6.5; 1042 -6.2; 1146 -5.9; 1261 -7.5; 1387 -9.6; 1526 -12.0; 1678 -13.4; 1846 -15.1; 2031 -14.8; 2234 -14.8; 2457 -11.5; 2703 -8.1; 2973 -5.2; 3270 -5.0; 3597 -6.7; 3957 -7.6; 4353 -6.1; 4788 -2.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -9.4; 9330 -11.3; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-1RBT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-1RBT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 75 Hz   | 1.24 | -9.5 dB  |
| Peaking | 140 Hz  | 3.36 | -6.0 dB  |
| Peaking | 1956 Hz | 2.74 | -10.1 dB |
| Peaking | 5625 Hz | 3.23 | 7.3 dB   |
| Peaking | 309 Hz  | 2.6  | 7.2 dB   |
| Peaking | 671 Hz  | 1.8  | 2.2 dB   |
| Peaking | 6612 Hz | 7.71 | 2.3 dB   |
| Peaking | 9086 Hz | 5.33 | -5.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB |
| Peaking | 62 Hz    | 1.41 | -6.8 dB |
| Peaking | 125 Hz   | 1.41 | -9.5 dB |
| Peaking | 250 Hz   | 1.41 | 5.4 dB  |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -9.9 dB |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-1RBT/Sony%20MDR-1RBT.png)