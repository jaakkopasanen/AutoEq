# Sony MDR-V6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.8; 34 5.1; 37 4.3; 41 3.3; 45 2.6; 49 1.9; 54 1.4; 60 1.6; 66 1.1; 72 0.6; 79 0.2; 87 -0.0; 96 -0.2; 106 -0.2; 116 -0.3; 128 -0.2; 141 -0.2; 155 -0.1; 170 0.8; 187 2.6; 206 2.5; 227 1.5; 249 1.2; 274 1.8; 302 1.6; 332 1.3; 365 0.4; 402 -0.4; 442 -0.8; 486 -0.9; 535 -0.8; 588 -0.6; 647 -0.4; 712 -0.3; 783 -0.2; 861 -0.3; 947 -0.0; 1042 -0.2; 1146 -0.4; 1261 -1.1; 1387 -1.5; 1526 -2.7; 1678 -3.7; 1846 -4.1; 2031 -4.3; 2234 -4.2; 2457 -3.8; 2703 -4.5; 2973 -5.1; 3270 -4.2; 3597 -2.8; 3957 -2.5; 4353 -5.7; 4788 -4.6; 5267 -0.0; 5793 2.8; 6373 1.8; 7010 -1.9; 7711 -3.3; 8482 -5.5; 9330 -8.6; 10263 -7.2; 11289 -0.8; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-V6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-V6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 1.2  | 6.7 dB  |
| Peaking | 209 Hz   | 2.99 | 2.4 dB  |
| Peaking | 1869 Hz  | 2.16 | -3.2 dB |
| Peaking | 3130 Hz  | 1.45 | -4.1 dB |
| Peaking | 9485 Hz  | 4.02 | -9.6 dB |
| Peaking | 300 Hz   | 6.38 | 1.4 dB  |
| Peaking | 4609 Hz  | 5.91 | -6.3 dB |
| Peaking | 6070 Hz  | 2.14 | 7.3 dB  |
| Peaking | 7170 Hz  | 2.23 | -4.8 dB |
| Peaking | 11955 Hz | 5.9  | 1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-V6/Sony%20MDR-V6.png)