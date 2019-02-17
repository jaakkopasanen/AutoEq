# Sony MDR-Q68LW
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.8; 66 -2.2; 72 -3.5; 79 -4.5; 87 -5.3; 96 -6.0; 106 -6.5; 116 -6.6; 128 -6.9; 141 -7.1; 155 -7.1; 170 -7.2; 187 -7.1; 206 -7.0; 227 -7.0; 249 -6.8; 274 -6.4; 302 -6.1; 332 -6.0; 365 -5.8; 402 -5.7; 442 -5.6; 486 -5.5; 535 -5.3; 588 -5.3; 647 -5.3; 712 -5.4; 783 -5.6; 861 -5.8; 947 -6.3; 1042 -6.6; 1146 -6.9; 1261 -7.6; 1387 -8.7; 1526 -10.2; 1678 -11.1; 1846 -11.9; 2031 -11.9; 2234 -11.8; 2457 -11.6; 2703 -11.2; 2973 -9.9; 3270 -8.2; 3597 -8.1; 3957 -10.4; 4353 -9.4; 4788 -5.8; 5267 -2.4; 5793 -0.5; 6373 -1.8; 7010 -5.5; 7711 -8.2; 8482 -6.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-Q68LW GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-Q68LW ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.86 | 7.1 dB  |
| Peaking | 758 Hz  | 1.05 | 1.8 dB  |
| Peaking | 2076 Hz | 1.2  | -6.1 dB |
| Peaking | 4156 Hz | 6.36 | -3.7 dB |
| Peaking | 5748 Hz | 3.84 | 7.4 dB  |
| Peaking | 36 Hz   | 3.53 | -1.2 dB |
| Peaking | 58 Hz   | 2.95 | 2.5 dB  |
| Peaking | 131 Hz  | 1.08 | -1.5 dB |
| Peaking | 6533 Hz | 9.05 | 1.9 dB  |
| Peaking | 7611 Hz | 6.05 | -2.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 3.9 dB  |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.5 dB |
| Peaking | 4000 Hz  | 1.41 | -0.0 dB |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-Q68LW/Sony%20MDR-Q68LW.png)