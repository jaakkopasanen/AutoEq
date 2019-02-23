# Sony MDR-7550
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -3.3; 25 -3.5; 28 -3.8; 31 -4.0; 34 -4.2; 37 -4.4; 41 -4.6; 45 -4.9; 49 -5.1; 54 -5.3; 60 -5.8; 66 -6.2; 72 -6.4; 79 -6.8; 87 -7.1; 96 -7.4; 106 -7.6; 116 -7.9; 128 -8.2; 141 -8.5; 155 -8.7; 170 -8.9; 187 -9.0; 206 -9.1; 227 -9.1; 249 -8.9; 274 -8.9; 302 -8.8; 332 -8.4; 365 -8.3; 402 -7.9; 442 -7.8; 486 -7.5; 535 -7.4; 588 -7.1; 647 -6.7; 712 -6.5; 783 -6.6; 861 -6.7; 947 -7.0; 1042 -6.8; 1146 -7.3; 1261 -8.5; 1387 -9.5; 1526 -10.5; 1678 -11.0; 1846 -10.8; 2031 -10.1; 2234 -8.6; 2457 -6.5; 2703 -4.0; 2973 -1.3; 3270 -0.5; 3597 -0.5; 3957 -0.7; 4353 -4.5; 4788 -8.9; 5267 -8.7; 5793 -2.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7550 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7550 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.51 | 3.5 dB  |
| Peaking | 199 Hz  | 0.72 | -2.8 dB |
| Peaking | 1784 Hz | 2    | -5.4 dB |
| Peaking | 3309 Hz | 2.8  | 7.7 dB  |
| Peaking | 6315 Hz | 7.27 | 6.1 dB  |
| Peaking | 971 Hz  | 1.41 | 0.7 dB  |
| Peaking | 1386 Hz | 4.62 | -0.9 dB |
| Peaking | 4028 Hz | 7.44 | 3.4 dB  |
| Peaking | 5053 Hz | 4.78 | -5.8 dB |
| Peaking | 5800 Hz | 7.14 | 3.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-7550/Sony%20MDR-7550.png)