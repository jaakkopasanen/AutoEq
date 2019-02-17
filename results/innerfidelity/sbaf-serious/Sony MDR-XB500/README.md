# Sony MDR-XB500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.5; 23 -12.0; 25 -12.4; 28 -12.8; 31 -13.2; 34 -13.4; 37 -13.6; 41 -13.9; 45 -14.1; 49 -14.3; 54 -14.4; 60 -14.3; 66 -14.3; 72 -14.6; 79 -15.2; 87 -15.7; 96 -15.9; 106 -16.7; 116 -17.2; 128 -17.8; 141 -18.5; 155 -18.8; 170 -18.7; 187 -19.0; 206 -19.3; 227 -19.6; 249 -19.4; 274 -18.7; 302 -18.3; 332 -17.5; 365 -16.6; 402 -16.0; 442 -15.1; 486 -14.1; 535 -12.8; 588 -11.0; 647 -9.4; 712 -7.9; 783 -6.4; 861 -5.6; 947 -6.0; 1042 -6.6; 1146 -7.6; 1261 -9.5; 1387 -11.1; 1526 -11.9; 1678 -11.9; 1846 -11.4; 2031 -10.4; 2234 -9.1; 2457 -7.3; 2703 -5.1; 2973 -3.0; 3270 -0.8; 3597 -0.5; 3957 -2.4; 4353 -6.3; 4788 -10.5; 5267 -11.2; 5793 -9.4; 6373 -8.3; 7010 -6.7; 7711 -6.2; 8482 -6.5; 9330 -6.9; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-XB500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 56 Hz   | 0.28 | -7.0 dB |
| Peaking | 203 Hz  | 0.87 | -8.7 dB |
| Peaking | 379 Hz  | 1.67 | -5.1 dB |
| Peaking | 1709 Hz | 2.5  | -5.9 dB |
| Peaking | 3397 Hz | 4.48 | 7.6 dB  |
| Peaking | 531 Hz  | 3.73 | -1.8 dB |
| Peaking | 871 Hz  | 2.13 | 3.1 dB  |
| Peaking | 1366 Hz | 5.75 | -2.1 dB |
| Peaking | 3895 Hz | 6.59 | 3.3 dB  |
| Peaking | 5135 Hz | 3.61 | -5.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.3 dB  |
| Peaking | 62 Hz    | 1.41 | -5.1 dB  |
| Peaking | 125 Hz   | 1.41 | -8.5 dB  |
| Peaking | 250 Hz   | 1.41 | -11.8 dB |
| Peaking | 500 Hz   | 1.41 | -4.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB  |
| Peaking | 16000 Hz | 1.41 | 0.3 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-XB500/Sony%20MDR-XB500.png)