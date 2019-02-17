# Sony MDR-XB700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -17.6; 23 -17.4; 25 -17.1; 28 -16.5; 31 -16.1; 34 -16.4; 37 -17.0; 41 -17.3; 45 -16.4; 49 -15.0; 54 -13.7; 60 -14.9; 66 -17.0; 72 -18.5; 79 -19.2; 87 -19.5; 96 -19.5; 106 -19.1; 116 -18.4; 128 -17.5; 141 -16.4; 155 -15.7; 170 -15.5; 187 -14.9; 206 -13.6; 227 -12.3; 249 -11.0; 274 -10.1; 302 -9.0; 332 -8.0; 365 -7.6; 402 -7.4; 442 -7.0; 486 -6.3; 535 -5.1; 588 -4.5; 647 -2.3; 712 -0.8; 783 -1.2; 861 -2.7; 947 -4.7; 1042 -7.0; 1146 -8.7; 1261 -10.3; 1387 -11.8; 1526 -12.9; 1678 -13.4; 1846 -13.3; 2031 -12.7; 2234 -11.2; 2457 -8.9; 2703 -6.7; 2973 -3.8; 3270 -0.5; 3597 -2.7; 3957 -9.3; 4353 -8.6; 4788 -10.1; 5267 -13.0; 5793 -14.8; 6373 -5.6; 7010 -3.9; 7711 -5.8; 8482 -8.5; 9330 -11.7; 10263 -10.8; 11289 -6.0; 12418 -6.0; 13660 -6.7; 15026 -10.9; 16529 -7.5; 18182 -6.0; 20000 -11.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-XB700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 11 Hz    | 1.18 | -11.4 dB |
| Peaking | 17 Hz    | 0.18 | -8.1 dB  |
| Peaking | 113 Hz   | 0.86 | -9.7 dB  |
| Peaking | 1717 Hz  | 2.78 | -8.4 dB  |
| Peaking | 10852 Hz | 0.39 | -2.5 dB  |
| Peaking | 736 Hz   | 2.52 | 7.4 dB   |
| Peaking | 3315 Hz  | 4.25 | 10.0 dB  |
| Peaking | 5786 Hz  | 0.88 | -35.1 dB |
| Peaking | 6434 Hz  | 0.82 | 32.5 dB  |
| Peaking | 9487 Hz  | 5.73 | -5.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.6 dB |
| Peaking | 62 Hz    | 1.41 | -7.3 dB  |
| Peaking | 125 Hz   | 1.41 | -11.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB  |
| Peaking | 500 Hz   | 1.41 | 2.9 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 2000 Hz  | 1.41 | -7.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 8000 Hz  | 1.41 | -2.9 dB  |
| Peaking | 16000 Hz | 1.41 | -3.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-XB700/Sony%20MDR-XB700.png)