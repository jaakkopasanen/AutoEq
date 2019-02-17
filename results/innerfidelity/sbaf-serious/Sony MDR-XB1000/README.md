# Sony MDR-XB1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.6; 23 -8.4; 25 -9.2; 28 -10.4; 31 -11.4; 34 -12.2; 37 -12.5; 41 -12.9; 45 -13.1; 49 -13.4; 54 -14.1; 60 -14.7; 66 -15.1; 72 -15.3; 79 -15.6; 87 -16.1; 96 -16.4; 106 -16.7; 116 -17.0; 128 -17.3; 141 -17.5; 155 -17.6; 170 -17.8; 187 -17.9; 206 -17.8; 227 -17.6; 249 -17.3; 274 -16.6; 302 -15.8; 332 -15.0; 365 -14.3; 402 -13.5; 442 -12.5; 486 -11.3; 535 -10.3; 588 -8.1; 647 -5.8; 712 -4.2; 783 -2.4; 861 -2.5; 947 -4.7; 1042 -7.9; 1146 -10.9; 1261 -10.8; 1387 -8.5; 1526 -5.7; 1678 -2.6; 1846 -0.5; 2031 -0.5; 2234 -7.0; 2457 -14.8; 2703 -13.5; 2973 -11.0; 3270 -9.8; 3597 -9.2; 3957 -9.4; 4353 -9.3; 4788 -5.0; 5267 -0.6; 5793 -5.3; 6373 -9.9; 7010 -7.2; 7711 -6.2; 8482 -6.5; 9330 -6.9; 10263 -8.1; 11289 -7.4; 12418 -6.5; 13660 -6.5; 15026 -7.9; 16529 -8.9; 18182 -8.1; 20000 -7.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-XB1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 103 Hz   | 0.37 | -9.3 dB  |
| Peaking | 290 Hz   | 0.85 | -6.9 dB  |
| Peaking | 1277 Hz  | 3.02 | -10.8 dB |
| Peaking | 1978 Hz  | 0.72 | 25.9 dB  |
| Peaking | 2521 Hz  | 1.18 | -28.0 dB |
| Peaking | 759 Hz   | 1.13 | -3.1 dB  |
| Peaking | 789 Hz   | 2.8  | 6.8 dB   |
| Peaking | 5268 Hz  | 5.68 | 12.1 dB  |
| Peaking | 5420 Hz  | 1.81 | -5.2 dB  |
| Peaking | 17008 Hz | 1.14 | -2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.4 dB  |
| Peaking | 62 Hz    | 1.41 | -6.5 dB  |
| Peaking | 125 Hz   | 1.41 | -8.4 dB  |
| Peaking | 250 Hz   | 1.41 | -10.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 4000 Hz  | 1.41 | -3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 16000 Hz | 1.41 | -2.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-XB1000/Sony%20MDR-XB1000.png)