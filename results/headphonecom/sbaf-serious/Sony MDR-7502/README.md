# Sony MDR-7502
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.5; 206 -0.5; 227 -0.5; 249 -0.5; 274 -0.6; 302 -1.5; 332 -3.7; 365 -5.1; 402 -6.6; 442 -8.3; 486 -10.0; 535 -12.0; 588 -13.5; 647 -14.5; 712 -15.1; 783 -15.0; 861 -15.7; 947 -16.2; 1042 -16.4; 1146 -16.6; 1261 -16.8; 1387 -17.8; 1526 -19.0; 1678 -18.5; 1846 -18.3; 2031 -17.1; 2234 -15.7; 2457 -14.1; 2703 -12.6; 2973 -11.3; 3270 -10.0; 3597 -9.0; 3957 -8.2; 4353 -7.9; 4788 -7.1; 5267 -2.0; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -8.8; 11289 -7.3; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7502 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7502 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 48 Hz    | 0.18 | 6.3 dB   |
| Peaking | 268 Hz   | 1.15 | 6.1 dB   |
| Peaking | 1232 Hz  | 0.4  | -12.1 dB |
| Peaking | 5858 Hz  | 2.03 | 9.0 dB   |
| Peaking | 10815 Hz | 2.5  | -1.5 dB  |
| Peaking | 618 Hz   | 3.64 | -1.6 dB  |
| Peaking | 1281 Hz  | 1.42 | 3.8 dB   |
| Peaking | 1603 Hz  | 1.47 | -4.3 dB  |
| Peaking | 3234 Hz  | 1.85 | 2.1 dB   |
| Peaking | 4698 Hz  | 8.88 | -2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB   |
| Peaking | 62 Hz    | 1.41 | 4.4 dB   |
| Peaking | 125 Hz   | 1.41 | 4.3 dB   |
| Peaking | 250 Hz   | 1.41 | 7.1 dB   |
| Peaking | 500 Hz   | 1.41 | -4.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -8.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -10.7 dB |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 16000 Hz | 1.41 | -0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-7502/Sony%20MDR-7502.png)