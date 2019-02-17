# Sony MDR-V6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.7; 34 -1.4; 37 -2.2; 41 -3.2; 45 -3.9; 49 -4.6; 54 -5.1; 60 -4.9; 66 -5.4; 72 -5.9; 79 -6.3; 87 -6.5; 96 -6.7; 106 -6.7; 116 -6.8; 128 -6.7; 141 -6.7; 155 -6.6; 170 -5.7; 187 -3.9; 206 -4.0; 227 -5.0; 249 -5.3; 274 -4.7; 302 -4.9; 332 -5.2; 365 -6.1; 402 -6.9; 442 -7.3; 486 -7.4; 535 -7.3; 588 -7.1; 647 -6.9; 712 -6.8; 783 -6.7; 861 -6.8; 947 -6.5; 1042 -6.7; 1146 -6.9; 1261 -7.6; 1387 -8.0; 1526 -9.2; 1678 -10.2; 1846 -10.6; 2031 -10.8; 2234 -10.7; 2457 -10.3; 2703 -11.0; 2973 -11.6; 3270 -10.7; 3597 -9.3; 3957 -9.0; 4353 -12.2; 4788 -11.1; 5267 -6.5; 5793 -3.7; 6373 -4.7; 7010 -8.4; 7711 -9.8; 8482 -12.0; 9330 -15.1; 10263 -13.7; 11289 -7.3; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-V6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-V6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 1.2  | 6.7 dB  |
| Peaking | 210 Hz   | 2.98 | 2.4 dB  |
| Peaking | 1868 Hz  | 2.16 | -3.2 dB |
| Peaking | 3130 Hz  | 1.44 | -4.1 dB |
| Peaking | 9492 Hz  | 3.8  | -9.6 dB |
| Peaking | 300 Hz   | 6.27 | 1.4 dB  |
| Peaking | 4612 Hz  | 6.1  | -6.2 dB |
| Peaking | 6067 Hz  | 2.23 | 6.9 dB  |
| Peaking | 7163 Hz  | 2.25 | -4.3 dB |
| Peaking | 11942 Hz | 5.56 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.3 dB |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | 2.5 dB  |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.5 dB |
| Peaking | 4000 Hz  | 1.41 | -1.8 dB |
| Peaking | 8000 Hz  | 1.41 | -3.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-V6/Sony%20MDR-V6.png)