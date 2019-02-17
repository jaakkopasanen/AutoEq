# Sony MDR-XB500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.7; 23 -15.9; 25 -16.0; 28 -16.2; 31 -16.3; 34 -16.4; 37 -16.5; 41 -16.5; 45 -16.6; 49 -16.7; 54 -16.8; 60 -16.8; 66 -16.7; 72 -16.8; 79 -17.4; 87 -18.0; 96 -18.2; 106 -17.9; 116 -18.5; 128 -19.1; 141 -19.7; 155 -19.9; 170 -19.0; 187 -18.9; 206 -19.8; 227 -20.1; 249 -19.6; 274 -19.2; 302 -18.9; 332 -18.5; 365 -18.0; 402 -17.3; 442 -16.5; 486 -15.5; 535 -14.1; 588 -12.5; 647 -10.6; 712 -8.5; 783 -6.6; 861 -5.4; 947 -5.8; 1042 -6.9; 1146 -8.1; 1261 -9.7; 1387 -11.1; 1526 -11.7; 1678 -11.3; 1846 -10.3; 2031 -9.1; 2234 -7.7; 2457 -5.9; 2703 -3.9; 2973 -2.3; 3270 -0.5; 3597 -0.5; 3957 -2.0; 4353 -5.8; 4788 -8.9; 5267 -8.1; 5793 -6.4; 6373 -5.7; 7010 -8.0; 7711 -8.0; 8482 -6.5; 9330 -6.5; 10263 -7.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-XB500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 0.18 | -9.2 dB |
| Peaking | 224 Hz   | 0.64 | -8.1 dB |
| Peaking | 413 Hz   | 1.91 | -4.1 dB |
| Peaking | 3413 Hz  | 4.22 | 7.4 dB  |
| Peaking | 920 Hz   | 1.76 | 7.3 dB  |
| Peaking | 1735 Hz  | 0.67 | -8.9 dB |
| Peaking | 2614 Hz  | 1.07 | 6.9 dB  |
| Peaking | 4853 Hz  | 7.13 | -3.3 dB |
| Peaking | 21016 Hz | 1.81 | -0.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -9.8 dB  |
| Peaking | 62 Hz    | 1.41 | -6.8 dB  |
| Peaking | 125 Hz   | 1.41 | -9.4 dB  |
| Peaking | 250 Hz   | 1.41 | -11.5 dB |
| Peaking | 500 Hz   | 1.41 | -6.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB   |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB  |
| Peaking | 16000 Hz | 1.41 | 0.2 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-XB500/Sony%20MDR-XB500.png)