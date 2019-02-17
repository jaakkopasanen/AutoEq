# Sony MDR-XB950B1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.0; 23 -13.2; 25 -13.3; 28 -13.5; 31 -13.6; 34 -13.6; 37 -13.5; 41 -13.4; 45 -13.3; 49 -13.3; 54 -13.3; 60 -13.4; 66 -13.7; 72 -13.9; 79 -14.2; 87 -14.6; 96 -14.9; 106 -15.1; 116 -15.2; 128 -15.2; 141 -14.9; 155 -14.3; 170 -13.5; 187 -13.4; 206 -12.5; 227 -11.0; 249 -9.6; 274 -7.7; 302 -5.3; 332 -2.8; 365 -1.4; 402 -2.7; 442 -5.0; 486 -6.5; 535 -7.3; 588 -7.6; 647 -7.6; 712 -7.5; 783 -7.2; 861 -6.9; 947 -6.7; 1042 -6.2; 1146 -5.4; 1261 -5.3; 1387 -4.9; 1526 -4.6; 1678 -4.5; 1846 -4.0; 2031 -3.8; 2234 -3.1; 2457 -1.9; 2703 -0.7; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.7; 4353 -4.1; 4788 -0.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-XB950B1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB950B1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.84 | -5.1 dB |
| Peaking | 133 Hz  | 0.37 | -8.6 dB |
| Peaking | 351 Hz  | 2.1  | 10.0 dB |
| Peaking | 3038 Hz | 1.1  | 6.0 dB  |
| Peaking | 5737 Hz | 3.23 | 5.0 dB  |
| Peaking | 407 Hz  | 8.41 | 0.9 dB  |
| Peaking | 673 Hz  | 0.79 | -2.4 dB |
| Peaking | 939 Hz  | 0.47 | 2.1 dB  |
| Peaking | 2152 Hz | 2.03 | -1.2 dB |
| Peaking | 8490 Hz | 3.23 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.1 dB |
| Peaking | 62 Hz    | 1.41 | -4.4 dB |
| Peaking | 125 Hz   | 1.41 | -9.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-XB950B1/Sony%20MDR-XB950B1.png)